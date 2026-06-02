import argparse
import json
import os
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", "/tmp/hipc_v14_marker_audit_mplconfig")
os.environ.setdefault("NUMBA_CACHE_DIR", "/tmp/hipc_v14_marker_audit_numba_cache")

import anndata as ad
import numpy as np
import pandas as pd
import yaml
from scipy import sparse


parser = argparse.ArgumentParser(description="Audit and score the HIPC v14 ontology-aware marker registry.")
parser.add_argument("--registry", default="configs/marker_registry_v14.yaml")
parser.add_argument("--manifest", default="configs/v13_manifest.tsv")
parser.add_argument("--v13-out-root", default="outputs/final_annotations/260526_v13_input_contract_repair")
parser.add_argument("--out-root", default="outputs/final_annotations/260527_v14_marker_registry")
args = parser.parse_args()

project_root = Path.cwd()
registry = yaml.safe_load((project_root / args.registry).read_text())
manifest = pd.read_csv(project_root / args.manifest, sep="\t").fillna("")
v13_out_root = project_root / args.v13_out_root
out_root = project_root / args.out_root
tables_dir = out_root / "tables"
tables_dir.mkdir(parents=True, exist_ok=True)

labels = registry["labels"]
scoring = registry["scoring"]
eligible_best_labels = [
    label
    for label, spec in labels.items()
    if spec.get("marker_role") in {"terminal", "artifact", "rare_parent"}
    and len(spec.get("positive", [])) > 0
    and spec.get("marker_role") != "excluded_parent"
]
all_marker_genes = sorted(
    {
        gene
        for spec in labels.values()
        for field in ["positive", "negative", "confound", "key"]
        for gene in spec.get(field, [])
    }
)
rare_marker_labels = {
    "HSC",
    "Eosinophil",
    "Basophil",
    "Mast Cell",
    "Conventional DC 1",
    "Plasmacytoid DC",
    "Platelet",
    "RBC",
    "ydT Cell",
    "MAIT Cell",
    "NKT Cell",
    "Treg",
}
lineage_allowed_labels = {
    "B_lineage": {label for label, spec in labels.items() if spec.get("applicable_lineage") in {"B_lineage", "Any"}},
    "T_NK_lineage": {label for label, spec in labels.items() if spec.get("applicable_lineage") in {"T_NK_lineage", "Any"}},
    "Myeloid_lineage": {label for label, spec in labels.items() if spec.get("applicable_lineage") in {"Myeloid_lineage", "Any"}},
    "Other_lineage": {label for label, spec in labels.items() if spec.get("applicable_lineage") == "Any"},
    "Ambiguous": set(eligible_best_labels),
}

coverage_rows = []
score_summary_rows = []
gated_score_summary_rows = []
by_final_label_rows = []
subcluster_rows = []

for row in manifest.itertuples(index=False):
    study = row.study_id
    portal_path = project_root / row.portal_input_h5ad
    cxg_path = v13_out_root / "cellxgene" / f"{study}.final_v13_recursive_screfmapping.cxg.h5ad"

    portal = ad.read_h5ad(portal_path, backed="r")
    available_genes = [gene for gene in all_marker_genes if gene in portal.var_names]
    sub = portal[:, available_genes].to_memory()
    matrix = sub.layers["counts"] if "counts" in sub.layers else sub.X
    if sparse.issparse(matrix):
        matrix = matrix.tocsr().astype("float64")
        totals = np.asarray(matrix.sum(axis=1)).ravel()
        totals[totals == 0] = 1.0
        matrix = matrix.multiply(10000.0 / totals[:, None])
        matrix.data = np.log1p(matrix.data)
        expr = pd.DataFrame(matrix.toarray(), index=portal.obs_names.astype(str), columns=available_genes)
    else:
        matrix = np.asarray(matrix, dtype="float64")
        totals = matrix.sum(axis=1)
        totals[totals == 0] = 1.0
        expr = pd.DataFrame(np.log1p(matrix / totals[:, None] * 10000.0), index=portal.obs_names.astype(str), columns=available_genes)
    portal_n_obs = portal.n_obs
    portal_n_vars = portal.n_vars
    portal.file.close()

    expr_pct = expr.rank(pct=True)
    score_frame = pd.DataFrame(index=expr.index)
    support_frame = pd.DataFrame(index=expr.index)
    key_support_frame = pd.DataFrame(index=expr.index)
    confound_frame = pd.DataFrame(index=expr.index)
    availability_alert_by_label = {}

    for label, spec in labels.items():
        positive = [gene for gene in spec.get("positive", []) if gene in expr_pct.columns]
        negative = [gene for gene in spec.get("negative", []) if gene in expr_pct.columns]
        confound = [gene for gene in spec.get("confound", []) if gene in expr_pct.columns]
        key = [gene for gene in spec.get("key", []) if gene in expr_pct.columns]
        expected = sorted(set(spec.get("positive", []) + spec.get("negative", []) + spec.get("confound", []) + spec.get("key", [])))
        present = [gene for gene in expected if gene in available_genes]
        missing = [gene for gene in expected if gene not in available_genes]
        positive_score = expr_pct[positive].mean(axis=1) if positive else pd.Series(0.0, index=expr.index)
        negative_score = expr_pct[negative].mean(axis=1) if negative else pd.Series(0.0, index=expr.index)
        confound_score = expr_pct[confound].mean(axis=1) if confound else pd.Series(0.0, index=expr.index)
        final_score = (
            positive_score
            - float(scoring["negative_weight"]) * negative_score
            - float(scoring["confound_weight"]) * confound_score
        )
        score_frame[label] = final_score.astype("float32")
        support_frame[label] = positive_score.astype("float32")
        key_support = expr_pct[key].mean(axis=1) if key else pd.Series(0.0, index=expr.index)
        key_support_frame[label] = key_support.astype("float32")
        confound_frame[label] = confound_score.astype("float32")
        present_fraction = len(present) / len(expected) if expected else 1.0
        key_present_fraction = len(key) / len(spec.get("key", [])) if spec.get("key", []) else 1.0
        if present_fraction < float(scoring["min_present_fraction_critical"]) or key_present_fraction < float(scoring["min_present_fraction_critical"]):
            alert = "critical"
        elif present_fraction < float(scoring["min_present_fraction_warning"]) or key_present_fraction < float(scoring["min_present_fraction_warning"]):
            alert = "warning"
        else:
            alert = "pass"
        availability_alert_by_label[label] = alert
        coverage_rows.append(
            {
                "study": study,
                "label": label,
                "broad_lineage": spec.get("broad_lineage", ""),
                "applicable_lineage": spec.get("applicable_lineage", ""),
                "marker_role": spec.get("marker_role", ""),
                "provenance": spec.get("provenance", ""),
                "n_expected_markers": len(expected),
                "n_present_markers": len(present),
                "present_fraction": present_fraction,
                "n_key_markers": len(spec.get("key", [])),
                "n_key_present": len(key),
                "key_present_fraction": key_present_fraction,
                "availability_alert": alert,
                "missing_key_markers": ";".join([gene for gene in spec.get("key", []) if gene not in available_genes]),
                "missing_markers": ";".join(missing),
            }
        )

    score_cols = eligible_best_labels
    best_label = score_frame[score_cols].idxmax(axis=1)
    best_score = score_frame[score_cols].max(axis=1)
    ungated_values = score_frame[score_cols].to_numpy(dtype="float64")
    ungated_filled = np.where(np.isfinite(ungated_values), ungated_values, -np.inf)
    ungated_sorted = np.sort(ungated_filled, axis=1)
    second_score = pd.Series(ungated_sorted[:, -2], index=score_frame.index).replace(-np.inf, np.nan)
    margin = best_score - second_score
    out = pd.DataFrame(
        {
            "cell_barcode": score_frame.index,
            "v14_marker_best_label": best_label.values,
            "v14_marker_best_score": best_score.round(5).values,
            "v14_marker_margin": margin.round(5).values,
        }
    ).set_index("cell_barcode", drop=False)

    if cxg_path.exists():
        cxg = ad.read_h5ad(cxg_path, backed="r")
        final_label = cxg.obs["submission_cell_type_v13_recursive_screfmapping"].astype(str).reindex(score_frame.index)
        final_conf = cxg.obs["confidence_score_v13_recursive_screfmapping"].reindex(score_frame.index)
        audit_lineage = cxg.obs["v13_parent_lineage"].astype(str).reindex(score_frame.index).fillna("Ambiguous")
        subcluster_candidates = [
            "v13_B_lineage_leiden",
            "v13_T_NK_lineage_leiden",
            "v13_Myeloid_lineage_leiden",
            "leiden",
        ]
        subcluster_frame = cxg.obs[[col for col in subcluster_candidates if col in cxg.obs.columns]].reindex(score_frame.index)
        cxg.file.close()
        out["final_label_v13"] = final_label.values
        out["final_confidence_v13"] = final_conf.values
    else:
        final_label = pd.Series("not_available", index=score_frame.index)
        audit_lineage = pd.Series("Ambiguous", index=score_frame.index)
        subcluster_frame = pd.DataFrame(index=score_frame.index)

    gated_score_frame = score_frame[score_cols].copy()
    gated_score_frame.loc[:, :] = np.nan
    for label in score_cols:
        spec = labels[label]
        if availability_alert_by_label[label] == "critical":
            continue

        role = spec.get("marker_role")
        if spec.get("broad_lineage") == "Artifact/Other":
            lineage_mask = audit_lineage.isin(["Other_lineage", "Ambiguous"])
        else:
            allowed_lineages = [
                lineage
                for lineage, allowed_labels in lineage_allowed_labels.items()
                if label in allowed_labels
            ]
            lineage_mask = audit_lineage.isin(allowed_lineages)

        if label in rare_marker_labels or role in {"artifact", "rare_parent"}:
            min_key_support = 0.80
            min_positive_support = 0.50
        else:
            min_key_support = 0.55
            min_positive_support = 0.35

        if availability_alert_by_label[label] == "warning":
            min_key_support += 0.10
            min_positive_support += 0.05

        key_mask = key_support_frame[label].ge(min_key_support)
        positive_mask = support_frame[label].ge(min_positive_support)
        gated_mask = lineage_mask & key_mask & positive_mask
        gated_score_frame.loc[gated_mask, label] = score_frame.loc[gated_mask, label]

    gated_values = gated_score_frame.to_numpy(dtype="float64")
    gated_valid_counts = np.isfinite(gated_values).sum(axis=1)
    gated_filled = np.where(np.isfinite(gated_values), gated_values, -np.inf)
    gated_best_index = np.argmax(gated_filled, axis=1)
    gated_best_values = gated_filled[np.arange(gated_filled.shape[0]), gated_best_index]
    gated_sorted = np.sort(gated_filled, axis=1)
    gated_second_values = gated_sorted[:, -2]
    gated_label = pd.Series(
        np.where(gated_valid_counts > 0, np.asarray(score_cols, dtype=object)[gated_best_index], "Unassigned"),
        index=score_frame.index,
    )
    gated_score = pd.Series(np.where(gated_valid_counts > 0, gated_best_values, np.nan), index=score_frame.index)
    gated_second_score = pd.Series(
        np.where(gated_valid_counts >= 2, gated_second_values, np.nan),
        index=score_frame.index,
    )
    gated_margin = gated_score - gated_second_score
    out["v14_marker_best_label_gated"] = gated_label.values
    out["v14_marker_best_score_gated"] = gated_score.round(5).values
    out["v14_marker_margin_gated"] = gated_margin.round(5).values
    out["v14_marker_n_eligible_labels_gated"] = gated_score_frame.notna().sum(axis=1).values
    out["audit_lineage_gate"] = audit_lineage.values

    score_export = pd.concat(
        [
            out,
            score_frame.add_prefix("score__"),
            key_support_frame[score_cols].add_prefix("key_support__"),
        ],
        axis=1,
    )
    score_export.to_csv(tables_dir / f"{study}_v14_marker_scores.tsv.gz", sep="\t", index=False)

    label_summary = score_export.groupby("v14_marker_best_label").size().reset_index(name="n_cells")
    label_summary.insert(0, "study", study)
    for summary_row in label_summary.itertuples(index=False):
        score_summary_rows.append(summary_row._asdict())

    gated_label_summary = (
        score_export.groupby(["audit_lineage_gate", "v14_marker_best_label_gated"])
        .size()
        .reset_index(name="n_cells")
    )
    gated_label_summary.insert(0, "study", study)
    for summary_row in gated_label_summary.itertuples(index=False):
        gated_score_summary_rows.append(summary_row._asdict())

    if final_label.astype(str).ne("not_available").any():
        concordance = pd.DataFrame(
            {
                "final_label": final_label.astype(str),
                "v14_marker_best_label": best_label.astype(str),
                "v14_marker_margin": margin,
                "v14_marker_best_score": best_score,
                "v14_marker_best_label_gated": gated_label.astype(str),
                "v14_marker_margin_gated": gated_margin,
                "v14_marker_best_score_gated": gated_score,
                "audit_lineage_gate": audit_lineage.astype(str),
            },
            index=score_frame.index,
        )
        for final_name, frame in concordance.groupby("final_label"):
            top_marker = frame["v14_marker_best_label"].value_counts().head(5)
            top_gated_marker = frame["v14_marker_best_label_gated"].value_counts().head(5)
            final_label_score = score_frame.loc[frame.index, final_name] if final_name in score_frame.columns else pd.Series(np.nan, index=frame.index)
            by_final_label_rows.append(
                {
                    "study": study,
                    "final_label": final_name,
                    "n_cells": int(frame.shape[0]),
                    "marker_exact_fraction": float(frame["v14_marker_best_label"].eq(final_name).mean()),
                    "marker_exact_fraction_gated": float(frame["v14_marker_best_label_gated"].eq(final_name).mean()),
                    "unassigned_fraction_gated": float(frame["v14_marker_best_label_gated"].eq("Unassigned").mean()),
                    "median_final_label_marker_score": float(final_label_score.dropna().median()),
                    "median_best_marker_score": float(frame["v14_marker_best_score"].dropna().median()),
                    "median_best_marker_score_gated": float(frame["v14_marker_best_score_gated"].dropna().median()),
                    "median_marker_margin": float(frame["v14_marker_margin"].dropna().median()),
                    "median_marker_margin_gated": float(frame["v14_marker_margin_gated"].dropna().median()),
                    "top_marker_best_labels": "; ".join(f"{label}:{count}" for label, count in top_marker.items()),
                    "top_marker_best_labels_gated": "; ".join(f"{label}:{count}" for label, count in top_gated_marker.items()),
                }
            )

    for cluster_col in subcluster_frame.columns:
        cluster_data = pd.DataFrame(
            {
                "cluster": subcluster_frame[cluster_col].astype(str),
                "audit_lineage_gate": audit_lineage.astype(str),
                "final_label": final_label.astype(str),
                "v14_marker_best_label_gated": gated_label.astype(str),
                "v14_marker_margin_gated": gated_margin,
            },
            index=score_frame.index,
        )
        for (lineage_name, cluster_name), frame in cluster_data.groupby(["audit_lineage_gate", "cluster"]):
            if cluster_name in {"", "nan", "None"}:
                continue
            top_final = frame["final_label"].value_counts().head(5)
            top_gated = frame["v14_marker_best_label_gated"].value_counts().head(5)
            subcluster_rows.append(
                {
                    "study": study,
                    "cluster_column": cluster_col,
                    "audit_lineage_gate": lineage_name,
                    "cluster": cluster_name,
                    "n_cells": int(frame.shape[0]),
                    "median_marker_margin_gated": float(frame["v14_marker_margin_gated"].dropna().median()),
                    "top_final_labels": "; ".join(f"{label}:{count}" for label, count in top_final.items()),
                    "top_gated_marker_labels": "; ".join(f"{label}:{count}" for label, count in top_gated.items()),
                    "unassigned_fraction_gated": float(frame["v14_marker_best_label_gated"].eq("Unassigned").mean()),
                }
            )

    print(f"{study}: cells={portal_n_obs:,} genes={portal_n_vars:,} marker_genes_present={len(available_genes):,}")

pd.DataFrame(coverage_rows).to_csv(tables_dir / "marker_registry_v14_availability.tsv", sep="\t", index=False)
pd.DataFrame(score_summary_rows).to_csv(tables_dir / "marker_registry_v14_best_label_counts.tsv", sep="\t", index=False)
pd.DataFrame(gated_score_summary_rows).to_csv(tables_dir / "marker_registry_v14_gated_best_label_counts.tsv", sep="\t", index=False)
pd.DataFrame(by_final_label_rows).to_csv(tables_dir / "marker_registry_v14_by_final_label.tsv", sep="\t", index=False)
pd.DataFrame(subcluster_rows).to_csv(tables_dir / "marker_registry_v14_subcluster_marker_summary.tsv", sep="\t", index=False)
(out_root / "marker_registry_v14_audit_summary.json").write_text(
    json.dumps(
        {
            "registry": str(project_root / args.registry),
            "manifest": str(project_root / args.manifest),
            "studies": manifest["study_id"].astype(str).tolist(),
            "n_registry_labels": len(labels),
            "n_registry_marker_genes": len(all_marker_genes),
        },
        indent=2,
    ),
    encoding="utf-8",
)
