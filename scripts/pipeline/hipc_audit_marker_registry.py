#!/usr/bin/env python3
import argparse
import json
import re
from pathlib import Path

import pandas as pd
import yaml


parser = argparse.ArgumentParser(description="Audit ontology coverage and schema validity of a HIPC marker registry.")
parser.add_argument("--config", default="configs/annotation_pipeline.json")
parser.add_argument("--out", default="outputs/marker_registry_audit")
args = parser.parse_args()

project_root = Path.cwd()
config = json.loads((project_root / args.config).read_text())
registry_path = project_root / config["marker_registry"]["path"]
ontology_path = project_root / config["ontology"]["path"]
label_column = config["ontology"]["label_column"]
excluded_labels = set(config["ontology"].get("excluded_submission_labels", []))

registry = yaml.safe_load(registry_path.read_text())
ontology = pd.read_csv(ontology_path, sep="\t").fillna("")
out_dir = project_root / args.out
out_dir.mkdir(parents=True, exist_ok=True)

labels = registry.get("labels", {})
alias_to_canonical = {}
for label, spec in labels.items():
    for alias in spec.get("aliases", []):
        alias_to_canonical[str(alias)] = str(label)


def canonical_label(label):
    return alias_to_canonical.get(str(label), str(label))


required_fields = [
    "broad_lineage",
    "applicable_lineage",
    "marker_role",
    "positive",
    "key",
    "negative",
    "confound",
    "notes",
    "provenance",
]
allowed_roles = {
    "terminal",
    "parent",
    "fallback_parent",
    "excluded_parent",
    "artifact",
    "rare_parent",
    "rare_terminal",
    "ambiguous_terminal",
}
allowed_lineages = {"Any", "B_lineage", "T_NK_lineage", "Myeloid_lineage"}
ontology_labels = set(ontology[label_column].astype(str)) - excluded_labels
registry_labels = {canonical_label(label) for label in labels}

coverage_rows = []
for label in sorted(ontology_labels | registry_labels):
    coverage_rows.append(
        {
            "label": label,
            "in_ontology": label in ontology_labels,
            "in_registry": label in registry_labels,
            "covered_by_alias": label in alias_to_canonical,
            "canonical_label": canonical_label(label),
        }
    )

schema_rows = []
gene_rows = []
for label, spec in sorted(labels.items()):
    canonical = canonical_label(label)
    missing_fields = [field for field in required_fields if field not in spec]
    positive = list(spec.get("positive", []))
    key = list(spec.get("key", []))
    negative = list(spec.get("negative", []))
    confound = list(spec.get("confound", []))
    all_genes = positive + key + negative + confound
    duplicate_genes = sorted({gene for gene in all_genes if all_genes.count(gene) > 1})
    policy = dict(spec.get("candidate_policy", {}))
    policy_fields = sorted(policy) if policy else []
    schema_rows.append(
        {
            "label": canonical,
            "raw_label": label,
            "missing_fields": ";".join(missing_fields),
            "unknown_marker_role": spec.get("marker_role") not in allowed_roles,
            "unknown_applicable_lineage": spec.get("applicable_lineage") not in allowed_lineages,
            "n_positive": len(positive),
            "n_key": len(key),
            "n_negative": len(negative),
            "n_confound": len(confound),
            "duplicate_genes_across_fields": ";".join(duplicate_genes),
            "has_candidate_policy": bool(policy),
            "candidate_policy_fields": ";".join(policy_fields),
        }
    )
    for field_name, genes in [
        ("positive", positive),
        ("key", key),
        ("negative", negative),
        ("confound", confound),
        ("policy_required_any", list(policy.get("required_any_markers", []))),
    ]:
        for gene in genes:
            gene_rows.append(
                {
                    "label": canonical,
                    "field": field_name,
                    "gene": gene,
                    "gene_symbol_format_ok": bool(re.match(r"^[A-Za-z0-9_.-]+$", str(gene))),
                }
            )

coverage = pd.DataFrame(coverage_rows)
schema = pd.DataFrame(schema_rows)
genes = pd.DataFrame(gene_rows)
coverage.to_csv(out_dir / "ontology_registry_coverage.tsv", sep="\t", index=False)
schema.to_csv(out_dir / "marker_registry_schema_audit.tsv", sep="\t", index=False)
genes.to_csv(out_dir / "marker_registry_gene_audit.tsv", sep="\t", index=False)

errors = []
missing_registry = coverage.query("in_ontology and not in_registry and not covered_by_alias")
if not missing_registry.empty:
    errors.append(f"ontology labels missing from registry: {missing_registry.shape[0]}")
missing_required = schema[schema["missing_fields"].astype(str).ne("")]
if not missing_required.empty:
    errors.append(f"registry labels with missing required fields: {missing_required.shape[0]}")
unknown_roles = schema[schema["unknown_marker_role"]]
if not unknown_roles.empty:
    errors.append(f"registry labels with unknown marker_role: {unknown_roles.shape[0]}")
unknown_lineages = schema[schema["unknown_applicable_lineage"]]
if not unknown_lineages.empty:
    errors.append(f"registry labels with unknown applicable_lineage: {unknown_lineages.shape[0]}")
bad_genes = genes[~genes["gene_symbol_format_ok"]] if not genes.empty else pd.DataFrame()
if not bad_genes.empty:
    errors.append(f"genes with unexpected symbol format: {bad_genes.shape[0]}")

summary = pd.DataFrame(
    [
        {
            "registry": str(registry_path),
            "ontology": str(ontology_path),
            "ontology_labels": len(ontology_labels),
            "registry_labels": len(registry_labels),
            "missing_registry_labels": int(missing_registry.shape[0]),
            "schema_errors": len(errors),
            "errors": "; ".join(errors),
        }
    ]
)
summary.to_csv(out_dir / "marker_registry_audit_summary.tsv", sep="\t", index=False)
print(summary.to_string(index=False))
if errors:
    raise SystemExit(1)
