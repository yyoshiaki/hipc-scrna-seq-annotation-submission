import argparse
import json
import os
import shutil
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", "/tmp/hipc_v14_apply_mplconfig")
os.environ.setdefault("NUMBA_CACHE_DIR", "/tmp/hipc_v14_apply_numba_cache")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scanpy as sc
import yaml


parser = argparse.ArgumentParser(description="Apply v14 marker-registry gates to HIPC final annotations.")
parser.add_argument("--v13-root", default="outputs/final_annotations/260526_v13_input_contract_repair")
parser.add_argument("--marker-gate-root", default="outputs/final_annotations/260527_v14_marker_registry")
parser.add_argument("--manifest", default="configs/v13_manifest.tsv")
parser.add_argument("--registry", default="configs/marker_registry_v14.yaml")
parser.add_argument("--ontology", default="data/reference/CT_Ontology_Spreadsheet_20260323.tsv")
parser.add_argument("--out-root", default="outputs/final_annotations/260602_v14_marker_gate_applied")
args = parser.parse_args()

project_root = Path.cwd()
v13_root = project_root / args.v13_root
marker_gate_root = project_root / args.marker_gate_root
out_root = project_root / args.out_root
manifest = pd.read_csv(project_root / args.manifest, sep="\t").fillna("")
registry = yaml.safe_load((project_root / args.registry).read_text())
ontology = pd.read_csv(project_root / args.ontology, sep="\t")
official_set = set(ontology["Celltype"].astype(str))
excluded_labels = {"Effector B"}
submit_allowed = official_set - excluded_labels

submission_dir = out_root / "submissions"
cxg_dir = out_root / "cellxgene"
tables_dir = out_root / "tables"
asset_dir = out_root / "report_assets"
for path in [submission_dir, cxg_dir, tables_dir, asset_dir]:
    path.mkdir(parents=True, exist_ok=True)

labels = registry["labels"]
label_role = {label: spec.get("marker_role", "") for label, spec in labels.items()}
label_broad = {label: spec.get("broad_lineage", "") for label, spec in labels.items()}
parents = {
    "B": "B Cell",
    "T/NK": "T Cell",
    "Myeloid/DC": "Myeloid Cell",
    "Artifact/Other": "Blood Cell",
}


def broad_label(label):
    label = str(label)
    broad = label_broad.get(label, "")
    if broad == "B":
        return "B"
    if broad == "T/NK":
        return "T/NK"
    if broad == "Myeloid/DC":
        return "Myeloid/DC"
    if broad == "Artifact/Other":
        return "Artifact/Other"
    if label in {"Doublet", "Platelet", "RBC", "HSC", "Blood Cell"}:
        return "Artifact/Other"
    return "Other"


availability = pd.read_csv(marker_gate_root / "tables/marker_registry_v14_availability.tsv", sep="\t").fillna("")
availability_alert = {
    (row.study, row.label): row.availability_alert
    for row in availability.itertuples(index=False)
}

summary_rows = []
label_rows = []
change_rows = []
reason_rows = []
validation_rows = []

sc.settings.figdir = str(asset_dir)
sc.settings.set_figure_params(dpi=120, frameon=False)
plt.rcParams["pdf.fonttype"] = 42
plt.rcParams["ps.fonttype"] = 42

for manifest_row in manifest.itertuples(index=False):
    study = manifest_row.study_id
    v13_cxg = v13_root / "cellxgene" / f"{study}.final_v13_recursive_screfmapping.cxg.h5ad"
    marker_scores_path = marker_gate_root / "tables" / f"{study}_v14_marker_scores.tsv.gz"
    adata = sc.read_h5ad(v13_cxg)
    scores = pd.read_csv(marker_scores_path, sep="\t").set_index("cell_barcode").reindex(adata.obs_names.astype(str))

    base_label = adata.obs["submission_cell_type_v13_recursive_screfmapping"].astype(str).copy()
    base_conf = pd.to_numeric(adata.obs["confidence_score_v13_recursive_screfmapping"], errors="coerce").fillna(0.45)
    v14_label = base_label.copy()
    v14_conf = base_conf.copy()
    v14_reason = pd.Series("v14_marker_gate_keep_v13_label", index=adata.obs_names, dtype="object")

    gated_label = scores["v14_marker_best_label_gated"].astype(str).fillna("Unassigned")
    gated_score = pd.to_numeric(scores["v14_marker_best_score_gated"], errors="coerce")
    gated_margin = pd.to_numeric(scores["v14_marker_margin_gated"], errors="coerce")
    eligible_n = pd.to_numeric(scores["v14_marker_n_eligible_labels_gated"], errors="coerce").fillna(0)
    audit_lineage = scores["audit_lineage_gate"].astype(str).fillna("Ambiguous")

    for cell in adata.obs_names.astype(str):
        base = str(base_label.loc[cell])
        gated = str(gated_label.loc[cell])
        base_broad = broad_label(base)
        gated_broad = broad_label(gated)
        base_role = label_role.get(base, "")
        gated_is_available = gated not in {"", "nan", "Unassigned", "not_available"}
        same_broad = base_broad == gated_broad and base_broad != "Other"
        strong_gated = (
            gated_is_available
            and pd.notna(gated_margin.loc[cell])
            and float(gated_margin.loc[cell]) >= 0.18
            and pd.notna(gated_score.loc[cell])
        )
        base_score = scores.loc[cell, f"score__{base}"] if f"score__{base}" in scores.columns else np.nan

        if base == "Doublet":
            v14_label.loc[cell] = "Doublet"
            v14_conf.loc[cell] = min(float(v14_conf.loc[cell]), 0.60)
            v14_reason.loc[cell] = "v14_doublet_override_preserved"
            continue

        if base == "Effector B":
            v14_label.loc[cell] = "B Cell"
            v14_conf.loc[cell] = min(float(v14_conf.loc[cell]), 0.70)
            v14_reason.loc[cell] = "v14_effector_b_excluded"
            continue

        if gated == base:
            v14_reason.loc[cell] = "v14_marker_gate_exact_support"
            if pd.notna(gated_margin.loc[cell]) and float(gated_margin.loc[cell]) >= 0.30:
                v14_conf.loc[cell] = min(0.94, max(float(v14_conf.loc[cell]), 0.72 + 0.18 * min(float(gated_margin.loc[cell]), 1.0)))
        elif base_role in {"parent", "fallback_parent"} or base in {"Blood Cell", "B Cell", "T Cell", "Myeloid Cell", "Monocyte", "DC"}:
            if strong_gated and (same_broad or base in {"Blood Cell"}):
                v14_label.loc[cell] = gated
                v14_conf.loc[cell] = min(0.82, max(float(v14_conf.loc[cell]), 0.62 + 0.25 * min(float(gated_margin.loc[cell]), 1.0)))
                v14_reason.loc[cell] = "v14_marker_gate_parent_rescue"
            elif gated == "Unassigned" or float(eligible_n.loc[cell]) == 0:
                v14_conf.loc[cell] = min(float(v14_conf.loc[cell]), 0.58)
                v14_reason.loc[cell] = "v14_marker_gate_parent_unresolved"
        elif gated == "Unassigned" or float(eligible_n.loc[cell]) == 0:
            v14_conf.loc[cell] = min(float(v14_conf.loc[cell]), 0.68)
            v14_reason.loc[cell] = "v14_marker_gate_unassigned_confidence_cap"
        elif same_broad:
            if strong_gated and (pd.isna(base_score) or float(gated_score.loc[cell]) >= float(base_score) + 0.08) and float(base_conf.loc[cell]) < 0.80:
                v14_label.loc[cell] = gated
                v14_conf.loc[cell] = min(0.82, max(0.62, 0.60 + 0.25 * min(float(gated_margin.loc[cell]), 1.0)))
                v14_reason.loc[cell] = "v14_marker_gate_same_lineage_switch"
            else:
                v14_conf.loc[cell] = min(float(v14_conf.loc[cell]), 0.78)
                v14_reason.loc[cell] = "v14_marker_gate_same_lineage_disagreement_cap"
        else:
            v14_conf.loc[cell] = min(float(v14_conf.loc[cell]), 0.70)
            v14_reason.loc[cell] = "v14_marker_gate_cross_lineage_disagreement_cap"

        alert = availability_alert.get((study, str(v14_label.loc[cell])), "pass")
        if alert == "critical":
            v14_conf.loc[cell] = min(float(v14_conf.loc[cell]), 0.70)
            v14_reason.loc[cell] = str(v14_reason.loc[cell]) + "_critical_marker_availability"
        elif alert == "warning":
            v14_conf.loc[cell] = min(float(v14_conf.loc[cell]), 0.82)
            v14_reason.loc[cell] = str(v14_reason.loc[cell]) + "_warning_marker_availability"

    v14_label = v14_label.where(v14_label.isin(submit_allowed), "Blood Cell")
    v14_conf = v14_conf.clip(0.05, 0.95)

    submission = pd.DataFrame(
        {
            "cell_barcode": adata.obs_names.astype(str),
            "predicted_cell_type": v14_label.astype(str).values,
            "confidence_score": v14_conf.round(4).values,
        }
    )
    submission.to_csv(submission_dir / f"{study}_annotation.tsv", sep="\t", index=False)

    adata.obs["submission_cell_type_v14_marker_gate_applied"] = v14_label.astype(str).values
    adata.obs["confidence_score_v14_marker_gate_applied"] = v14_conf.round(4).values
    adata.obs["v14_marker_gate_reason"] = v14_reason.astype(str).values
    adata.obs["v14_marker_gate_best_label"] = gated_label.astype(str).values
    adata.obs["v14_marker_gate_score"] = gated_score.values
    adata.obs["v14_marker_gate_margin"] = gated_margin.values
    adata.obs["v14_marker_gate_audit_lineage"] = audit_lineage.astype(str).values
    adata.obs["annotation_logic_version_v14_marker_gate_applied"] = "260602_v14_marker_gate_applied"

    diagnostics = adata.obs[
        [
            "submission_cell_type_v13_recursive_screfmapping",
            "confidence_score_v13_recursive_screfmapping",
            "submission_cell_type_v14_marker_gate_applied",
            "confidence_score_v14_marker_gate_applied",
            "v14_marker_gate_reason",
            "v14_marker_gate_best_label",
            "v14_marker_gate_score",
            "v14_marker_gate_margin",
            "v14_marker_gate_audit_lineage",
        ]
    ].copy()
    diagnostics.insert(0, "cell_barcode", adata.obs_names.astype(str))
    diagnostics.to_csv(tables_dir / f"{study}_v14_marker_gate_diagnostics.tsv.gz", sep="\t", index=False)

    label_counts = submission["predicted_cell_type"].value_counts()
    for label_name, n_cells in label_counts.items():
        label_rows.append({"study": study, "predicted_cell_type": label_name, "n_cells": int(n_cells)})
    for reason, n_cells in v14_reason.value_counts().items():
        reason_rows.append({"study": study, "v14_marker_gate_reason": reason, "n_cells": int(n_cells)})

    changed = base_label.ne(v14_label)
    for (old, new), count in pd.DataFrame({"old_label": base_label[changed], "new_label": v14_label[changed]}).value_counts(["old_label", "new_label"]).head(50).items():
        change_rows.append({"study": study, "old_label": old, "new_label": new, "n_cells": int(count)})

    invalid = sorted(set(submission["predicted_cell_type"]) - official_set)
    parent_or_blood = submission["predicted_cell_type"].isin(["B Cell", "T Cell", "Myeloid Cell", "Blood Cell"])
    artifact = submission["predicted_cell_type"].isin(["Platelet", "RBC", "HSC"])
    summary_rows.append(
        {
            "study": study,
            "n_cells": int(adata.n_obs),
            "n_v13_changed_cells": int(changed.sum()),
            "changed_fraction": float(changed.mean()),
            "n_v14_labels": int(submission["predicted_cell_type"].nunique()),
            "b_cell_n": int(submission["predicted_cell_type"].eq("B Cell").sum()),
            "t_cell_n": int(submission["predicted_cell_type"].eq("T Cell").sum()),
            "myeloid_cell_n": int(submission["predicted_cell_type"].eq("Myeloid Cell").sum()),
            "blood_cell_n": int(submission["predicted_cell_type"].eq("Blood Cell").sum()),
            "parent_or_blood_n": int(parent_or_blood.sum()),
            "parent_or_blood_fraction": float(parent_or_blood.mean()),
            "artifact_n": int(artifact.sum()),
            "doublet_n": int(submission["predicted_cell_type"].eq("Doublet").sum()),
            "effector_b_n": int(submission["predicted_cell_type"].eq("Effector B").sum()),
            "median_confidence": float(submission["confidence_score"].median()),
            "low_confidence_n": int(submission["confidence_score"].lt(0.60).sum()),
            "invalid_labels": ",".join(invalid),
        }
    )
    validation_rows.append(
        {
            "study": study,
            "n_submission_rows": int(submission.shape[0]),
            "n_h5ad_cells": int(adata.n_obs),
            "label_column": "submission_cell_type_v14_marker_gate_applied",
            "confidence_column": "confidence_score_v14_marker_gate_applied",
            "invalid_labels": ",".join(invalid),
            "h5ad_submission_label_match": bool(submission["predicted_cell_type"].reset_index(drop=True).eq(adata.obs["submission_cell_type_v14_marker_gate_applied"].astype(str).reset_index(drop=True)).all()),
        }
    )

    sc.pl.umap(adata, color=["submission_cell_type_v14_marker_gate_applied"], legend_loc="right margin", frameon=False, show=False)
    plt.savefig(asset_dir / f"umap_{study}_v14_label.png", dpi=180, bbox_inches="tight")
    plt.close("all")
    sc.pl.umap(adata, color=["v13_parent_lineage", "v14_marker_gate_reason"], legend_loc="right margin", frameon=False, show=False)
    plt.savefig(asset_dir / f"umap_{study}_v14_lineage_reason.png", dpi=180, bbox_inches="tight")
    plt.close("all")
    sc.pl.umap(adata, color=["n_genes_by_counts", "pct_counts_mt", "confidence_score_v14_marker_gate_applied"], frameon=False, show=False)
    plt.savefig(asset_dir / f"umap_{study}_v14_qc_confidence.png", dpi=180, bbox_inches="tight")
    plt.close("all")

    adata.write_h5ad(cxg_dir / f"{study}.final_v14_marker_gate_applied.cxg.h5ad", compression="gzip")
    print(f"{study}: cells={adata.n_obs:,} changed={int(changed.sum()):,} labels={submission['predicted_cell_type'].nunique()}")
    del adata

summary_df = pd.DataFrame(summary_rows)
summary_df.to_csv(tables_dir / "final_annotation_summary_v14_marker_gate_applied.tsv", sep="\t", index=False)
summary_df.to_csv(tables_dir / "final_annotation_summary_v13_recursive_screfmapping.tsv", sep="\t", index=False)
pd.DataFrame(label_rows).to_csv(tables_dir / "final_annotation_label_counts_v14_marker_gate_applied.tsv", sep="\t", index=False)
pd.DataFrame(reason_rows).to_csv(tables_dir / "v14_marker_gate_reason_counts.tsv", sep="\t", index=False)
pd.DataFrame(change_rows).to_csv(tables_dir / "v14_marker_gate_label_changes.tsv", sep="\t", index=False)
pd.DataFrame(validation_rows).to_csv(tables_dir / "final_annotation_validation_v14_marker_gate_applied.tsv", sep="\t", index=False)

for filename in [
    "v13_input_contract_audit.tsv",
    "marker_gene_availability.tsv",
    "marker_gene_availability_alerts.tsv",
    "v13_lineage_subcluster_evidence.tsv.gz",
]:
    source = v13_root / "tables" / filename
    if source.exists():
        shutil.copy2(source, tables_dir / filename)

(out_root / "final_annotation_summary_v14_marker_gate_applied.json").write_text(
    json.dumps({"version": "260602_v14_marker_gate_applied", "summary": summary_df.to_dict(orient="records")}, indent=2),
    encoding="utf-8",
)
print(summary_df.to_string(index=False))
print(f"Wrote v14 marker-gate-applied outputs to {out_root}")
