import argparse
from datetime import datetime
from zoneinfo import ZoneInfo
import json
import os
import re
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", "/tmp/hipc_annotation_mplconfig")
os.environ.setdefault("NUMBA_CACHE_DIR", "/tmp/hipc_annotation_numba_cache")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scanpy as sc
from scipy import sparse


# Reused small utilities keep repeated scoring blocks readable.
def mean_expr_score(adata, genes):
    available = [gene for gene in genes if gene in adata.var_names]
    if not available:
        return pd.Series(0.0, index=adata.obs_names)
    matrix = adata[:, available].X
    if sparse.issparse(matrix):
        values = np.asarray(matrix.mean(axis=1)).ravel()
    else:
        values = np.asarray(matrix).mean(axis=1)
    return pd.Series(values, index=adata.obs_names)


def source_fraction(frame, columns, label):
    hit = pd.Series(False, index=frame.index)
    for column in columns:
        hit |= frame[column].astype(str).eq(label)
    return float(hit.mean())


def raw_fraction(frame, columns, pattern):
    hit = pd.Series(False, index=frame.index)
    for column in columns:
        hit |= frame[column].astype(str).str.contains(pattern, case=False, regex=True, na=False)
    return float(hit.mean())


def cluster_marker_metrics(expr_frame, background_positive, genes, key_genes):
    available = [gene for gene in genes if gene in expr_frame.columns]
    available_key = [gene for gene in key_genes if gene in expr_frame.columns]
    if available:
        positive = expr_frame[available].gt(0)
        any_positive_fraction = float(positive.any(axis=1).mean())
        mean_positive_fraction = float(positive.mean(axis=0).mean())
    else:
        any_positive_fraction = 0.0
        mean_positive_fraction = 0.0
    if available_key:
        key_positive = expr_frame[available_key].gt(0)
        key_any_fraction = float(key_positive.any(axis=1).mean())
        key_two_fraction = float(key_positive.sum(axis=1).ge(min(2, len(available_key))).mean())
        key_max_fraction = float(key_positive.mean(axis=0).max())
        background_key_any = float(background_positive[available_key].any(axis=1).mean())
        key_enrichment = (key_any_fraction + 0.01) / (background_key_any + 0.01)
    else:
        key_any_fraction = any_positive_fraction
        key_two_fraction = 0.0
        key_max_fraction = mean_positive_fraction
        background_any = float(background_positive[available].any(axis=1).mean()) if available else 0.0
        key_enrichment = (any_positive_fraction + 0.01) / (background_any + 0.01)
    return {
        "marker_any_fraction": any_positive_fraction,
        "marker_mean_positive_fraction": mean_positive_fraction,
        "key_marker_any_fraction": key_any_fraction,
        "key_marker_two_fraction": key_two_fraction,
        "key_marker_max_fraction": key_max_fraction,
        "key_marker_enrichment": key_enrichment,
    }


def fill_obs_alias(obs, canonical, aliases, default):
    if canonical in obs.columns:
        return
    for alias in aliases:
        if alias in obs.columns:
            obs[canonical] = obs[alias].values
            return
    obs[canonical] = default


def map_screfmapping_label(query_type, cluster_l1, cluster_l2):
    label_text = f"{cluster_l1} {cluster_l2}"
    if query_type == "B":
        if re.search("ASC|Plasma|preASC", label_text, flags=re.IGNORECASE):
            return "Plasma Cell"
        if re.search("Memory|ABC", label_text, flags=re.IGNORECASE):
            return "Memory B Cell"
        if re.search("Naive", label_text, flags=re.IGNORECASE):
            return "Naive B Cell"
    if query_type == "CD4T":
        if re.search("Treg", label_text, flags=re.IGNORECASE):
            return "Treg"
        if re.search("Tnaive|Naive|Tcm|Tfh|PHLDA3|SOX4", label_text, flags=re.IGNORECASE):
            return "CD4 Naive / T Central Memory"
        if re.search("Tem|Tph|Th1|Th2|Th17|Th0|Act|cytotoxic|CTL|GZ", label_text, flags=re.IGNORECASE):
            return "CD4 T Effector Memory"
    return "not_available"


def load_screfmapping_evidence(study, index):
    evidence = pd.DataFrame(index=index)
    evidence["screfmapping_query_type"] = "not_available"
    evidence["screfmapping_clusterL1"] = "not_available"
    evidence["screfmapping_clusterL1_prob"] = 0.0
    evidence["screfmapping_clusterL2"] = "not_available"
    evidence["screfmapping_clusterL2_prob"] = 0.0
    evidence["screfmapping_official_label"] = "not_available"
    for query_type in ["B", "CD4T"]:
        result_path = output_root / "screfmapping_results" / study / query_type / f"{study}_{query_type}_Reference_Mapping.csv"
        if not result_path.exists():
            continue
        result = pd.read_csv(result_path)
        result = result[result["cell_barcode"].astype(str).isin(index)]
        result = result.set_index("cell_barcode")
        target = result.index.intersection(index)
        evidence.loc[target, "screfmapping_query_type"] = query_type
        evidence.loc[target, "screfmapping_clusterL1"] = result.loc[target, "clusterL1"].astype(str).values
        evidence.loc[target, "screfmapping_clusterL1_prob"] = pd.to_numeric(result.loc[target, "clusterL1_prob"], errors="coerce").fillna(0).values
        evidence.loc[target, "screfmapping_clusterL2"] = result.loc[target, "clusterL2"].astype(str).values
        evidence.loc[target, "screfmapping_clusterL2_prob"] = pd.to_numeric(result.loc[target, "clusterL2_prob"], errors="coerce").fillna(0).values
        mapped = [map_screfmapping_label(query_type, l1, l2) for l1, l2 in zip(result.loc[target, "clusterL1"].astype(str), result.loc[target, "clusterL2"].astype(str))]
        evidence.loc[target, "screfmapping_official_label"] = mapped
    return evidence

def project_path(path):
    path = Path(path)
    if path.is_absolute():
        return path
    return project_root / path

def markdown_table(rows, columns):
    if not rows:
        return "None."
    lines = ["| " + " | ".join(columns) + " |", "| " + " | ".join(["---"] * len(columns)) + " |"]
    for row in rows:
        values = [str(row.get(column, "")).replace("|", ";") for column in columns]
        lines.append("| " + " | ".join(values) + " |")
    return "\n".join(lines)


def render_template(path, values):
    text = path.read_text(encoding="utf-8")
    for key, value in values.items():
        text = text.replace("{{" + key + "}}", str(value))
    return text


parser = argparse.ArgumentParser(description="HIPC independent annotation runner")
parser.add_argument("--config", required=True)
parser.add_argument("--manifest", required=True)
parser.add_argument("--out")
parser.add_argument("--report-languages", default="en")
args = parser.parse_args()

project_root = Path.cwd()
config = json.loads(project_path(args.config).read_text())
manifest = pd.read_csv(project_path(args.manifest), sep="\t").fillna("")
version = config["version"]
report_updated = datetime.now(ZoneInfo("America/New_York")).strftime("%Y-%m-%d EDT")
output_root = project_path(args.out or config["output_root"])
try:
    output_root_display = str(output_root.relative_to(project_root))
except ValueError:
    output_root_display = str(output_root)
submission_dir = output_root / "submissions"
tables_dir = output_root / "tables"
cxg_dir = output_root / "cellxgene"
figures_dir = output_root / "figures"
report_dir = output_root
asset_dir = output_root / "assets"
template_dir = project_path(config.get("report", {}).get("template_dir", "skills/hipc-annotation/templates"))

for path in [submission_dir, tables_dir, cxg_dir, figures_dir, report_dir, asset_dir]:
    path.mkdir(parents=True, exist_ok=True)

ontology = pd.read_csv(project_path(config["ontology"]["path"]), sep="\t")
official_set = set(ontology["Celltype"].astype(str))
submit_allowed = official_set - set(config["ontology"].get("excluded_submission_labels", []))

sc.settings.figdir = str(figures_dir)
sc.settings.set_figure_params(dpi=120, frameon=False)
plt.rcParams["pdf.fonttype"] = 42
plt.rcParams["ps.fonttype"] = 42

ref_cols = ["celltypist_v3_label", "panhuman_fine_v3_label", "cluster_consensus_v3_label", "top_marker_v3_label"]
raw_cols = ["majority_voting_Immune_All_Low", "panhuman_azimuth_fine"]

b_labels = {"B Cell", "Naive B Cell", "Memory B Cell", "Plasma Cell", "Plasmablast"}
t_labels = {
    "T Cell",
    "CD4 T Cell (ab)",
    "CD8 T Cell (ab)",
    "CD4 Naive / T Central Memory",
    "CD4 T Effector Memory",
    "CD8 Naive / T Central Memory",
    "CD8 Cytotoxic / T Effector Memory",
    "Treg",
    "MAIT Cell",
    "ydT Cell",
    "NKT Cell",
    "NK Cell",
}
myeloid_labels = {
    "Myeloid Cell",
    "Monocyte",
    "Classical Monocyte",
    "Non-Classical Monocyte",
    "Intermediate Monocyte",
    "DC",
    "Plasmacytoid DC",
    "Conventional DC 1",
    "Conventional DC 2",
    "Granulocyte",
    "Neutrophil",
}
other_direct_labels = {"Platelet", "RBC", "HSC"}

score_gene_sets = {
    "marker_score_b_naive": ["TCL1A", "IGHM", "IGHD", "FCER2"],
    "marker_score_b_memory": ["CD27", "TNFRSF13B", "AIM2", "FCRL5", "ITGAX", "TBX21"],
    "marker_score_b_plasma": ["MZB1", "JCHAIN", "XBP1", "PRDM1", "SDC1"],
    "marker_score_cd4_naive_tcm": ["CD4", "IL7R", "CCR7", "TCF7", "LEF1", "SELL"],
    "marker_score_cd4_tem": ["CD4", "IL7R", "GZMK", "CCL5", "ANXA1"],
    "marker_score_cd8_naive_tcm": ["CD8A", "CD8B", "CCR7", "TCF7", "LEF1"],
    "marker_score_cd8_cytotoxic": ["CD8A", "CD8B", "NKG7", "GNLY", "PRF1", "GZMB", "GZMH"],
    "marker_score_treg": ["FOXP3", "IL2RA", "CTLA4", "IKZF2"],
    "marker_score_mait": ["SLC4A10", "KLRB1", "DPP4", "TRAV1-2"],
    "marker_score_gdt": ["TRDC", "TRGC1", "TRGC2"],
    "marker_score_nk": ["NKG7", "GNLY", "KLRD1", "FCGR3A", "PRF1"],
    "marker_score_classical_mono": ["LYZ", "S100A8", "S100A9", "FCN1", "VCAN"],
    "marker_score_nonclassical_mono": ["FCGR3A", "MS4A7", "CX3CR1", "LST1"],
    "marker_score_intermediate_mono": ["FCN1", "MS4A7", "HLA-DRA", "LST1"],
    "marker_score_pdc": ["LILRA4", "CLEC4C", "IRF7", "TCF4"],
    "marker_score_cdc1": ["CLEC9A", "XCR1", "BATF3"],
    "marker_score_cdc2": ["CD1C", "FCER1A", "CLEC10A"],
}

lineage_configs = {
    "B_lineage": {
        "parent": "B Cell",
        "resolution": 2.2,
        "candidate_scores": {
            "Naive B Cell": "marker_score_b_naive_pct",
            "Memory B Cell": "marker_score_b_memory_pct",
            "Plasma Cell": "marker_score_b_plasma_pct",
        },
        "raw_bonus": {
            "Naive B Cell": "Naive B",
            "Memory B Cell": "Memory B|Age-associated B|ABC",
            "Plasma Cell": "Plasma|Plasmablast",
        },
    },
    "T_NK_lineage": {
        "parent": "T Cell",
        "resolution": 2.6,
        "candidate_scores": {
            "CD4 Naive / T Central Memory": "marker_score_cd4_naive_tcm_pct",
            "CD4 T Effector Memory": "marker_score_cd4_tem_pct",
            "CD8 Naive / T Central Memory": "marker_score_cd8_naive_tcm_pct",
            "CD8 Cytotoxic / T Effector Memory": "marker_score_cd8_cytotoxic_pct",
            "Treg": "marker_score_treg_pct",
            "MAIT Cell": "marker_score_mait_pct",
            "ydT Cell": "marker_score_gdt_pct",
            "NK Cell": "marker_score_nk_pct",
        },
        "raw_bonus": {
            "CD4 Naive / T Central Memory": "Tcm/Naive helper|Tfh|Naive CD4",
            "CD4 T Effector Memory": "Tem/Effector helper|Memory CD4|cytotoxic CD4",
            "CD8 Naive / T Central Memory": "Tcm/Naive cytotoxic|Naive CD8",
            "CD8 Cytotoxic / T Effector Memory": "Tem/Temra cytotoxic|Tem/Trm cytotoxic|GZMB CD8|GZMK CD8",
            "Treg": "Regulatory T|Treg",
            "MAIT Cell": "MAIT",
            "ydT Cell": "gdT|ydT|gamma",
            "NK Cell": "NK",
        },
    },
    "Myeloid_lineage": {
        "parent": "Myeloid Cell",
        "resolution": 1.8,
        "candidate_scores": {
            "Classical Monocyte": "marker_score_classical_mono_pct",
            "Non-Classical Monocyte": "marker_score_nonclassical_mono_pct",
            "Intermediate Monocyte": "marker_score_intermediate_mono_pct",
            "Plasmacytoid DC": "marker_score_pdc_pct",
            "Conventional DC 1": "marker_score_cdc1_pct",
            "Conventional DC 2": "marker_score_cdc2_pct",
        },
        "raw_bonus": {
            "Classical Monocyte": "Classical",
            "Non-Classical Monocyte": "Non-Classical|CD16",
            "Intermediate Monocyte": "Intermediate",
            "Plasmacytoid DC": "Plasmacytoid|pDC",
            "Conventional DC 1": "Conventional DC 1|cDC1",
            "Conventional DC 2": "Conventional DC 2|cDC2",
        },
    },
}

summary_rows = []
label_rows = []
reason_rows = []
subcluster_rows = []
validation_rows = []
concern_rows = []

marker_set_to_labels = {marker_set: spec["official_labels"] for marker_set, spec in config["marker_sets"].items()}
label_to_marker_set = {label: marker_set for marker_set, labels in marker_set_to_labels.items() for label in labels}
marker_set_gene_lookup = {marker_set: list(spec["genes"]) for marker_set, spec in config["marker_sets"].items()}
marker_set_key_gene_lookup = {marker_set: list(spec.get("critical_genes", [])) for marker_set, spec in config["marker_sets"].items()}
critical_threshold = float(config["screfmapping"]["marker_availability_alerts"]["critical_present_fraction_lt"])
warning_threshold = float(config["screfmapping"]["marker_availability_alerts"]["warning_present_fraction_lt"])
marker_alert_confidence_caps = config["decision_engine"].get("marker_alert_confidence_caps", {"critical": 0.70, "warning": 0.82})
review_concern_thresholds = config["decision_engine"].get(
    "review_concern_thresholds",
    {"dataset_source_disagreement_fraction_gt": 0.20, "label_source_disagreement_fraction_gt": 0.50},
)
marker_availability_rows = []
source_disagreement_rows = []
subcluster_candidate_score_rows = []
subcluster_umap_rows = []
lineage_panel_status_rows = []

evidence_aliases = {
    "celltypist_v3_label": ["celltypist_label", "majority_voting", "majority_voting_Immune_All_Low"],
    "panhuman_fine_v3_label": ["panhuman_fine_label", "panhuman_azimuth_fine"],
    "cluster_consensus_v3_label": ["cluster_consensus_label"],
    "top_marker_v3_label": ["marker_best_label", "top_marker_label"],
    "majority_voting_Immune_All_Low": ["celltypist_label", "majority_voting"],
    "panhuman_azimuth_fine": ["panhuman_fine_label", "panhuman_fine_v3_label"],
}

for input_row in manifest.itertuples(index=False):
    study = input_row.study_id
    h5ad = project_path(input_row.input_h5ad)
    adata = sc.read_h5ad(h5ad)
    obs = adata.obs.copy()

    for canonical, aliases in evidence_aliases.items():
        fill_obs_alias(obs, canonical, aliases, "not_available")
        if canonical not in adata.obs.columns:
            adata.obs[canonical] = obs[canonical].values

    study_marker_alert = {}
    varnames = pd.Index(adata.var_names.astype(str))
    for marker_set, spec in config["marker_sets"].items():
        genes = list(spec["genes"])
        present = [gene for gene in genes if gene in varnames]
        missing = [gene for gene in genes if gene not in varnames]
        critical_genes = list(spec.get("critical_genes", []))
        missing_critical = [gene for gene in critical_genes if gene not in varnames]
        present_fraction = len(present) / len(genes)
        if present_fraction < critical_threshold:
            alert_level = "critical"
        elif present_fraction < warning_threshold:
            alert_level = "warning"
        elif missing_critical and marker_set in {"Treg", "Plasma_ASC"}:
            alert_level = "warning"
        else:
            alert_level = "pass"
        study_marker_alert[marker_set] = alert_level
        marker_availability_rows.append({
            "study": study,
            "marker_set": marker_set,
            "official_labels_relevant_to_set": ";".join(spec["official_labels"]),
            "n_genes_expected": len(genes),
            "n_genes_present": len(present),
            "present_fraction": present_fraction,
            "alert_level": alert_level,
            "missing_critical_markers": ";".join(missing_critical),
            "present_genes": ";".join(present),
            "missing_genes": ";".join(missing),
        })

    for column in ref_cols + raw_cols:
        if column not in obs.columns:
            obs[column] = "not_available"
            adata.obs[column] = "not_available"

    required_scref_cols = ["screfmapping_query_type", "screfmapping_clusterL1", "screfmapping_clusterL1_prob", "screfmapping_clusterL2", "screfmapping_clusterL2_prob", "screfmapping_official_label"]
    if "screfmapping_official_label" not in obs.columns:
        screfmapping = load_screfmapping_evidence(study, obs.index)
        for column in screfmapping.columns:
            obs[column] = screfmapping[column].values
            adata.obs[column] = screfmapping[column].values
    else:
        for column in required_scref_cols:
            if column not in obs.columns:
                obs[column] = "not_available" if not column.endswith("prob") else 0.0
                adata.obs[column] = obs[column].values

    for score_name, genes in score_gene_sets.items():
        obs[score_name] = mean_expr_score(adata, genes)
        obs[f"{score_name}_pct"] = obs[score_name].rank(pct=True)

    b_signal = pd.Series(0, index=obs.index, dtype="int64")
    t_signal = pd.Series(0, index=obs.index, dtype="int64")
    my_signal = pd.Series(0, index=obs.index, dtype="int64")
    other_signal = pd.Series(0, index=obs.index, dtype="int64")

    for column in ref_cols:
        b_signal += obs[column].astype(str).isin(b_labels).astype(int)
        t_signal += obs[column].astype(str).isin(t_labels).astype(int)
        my_signal += obs[column].astype(str).isin(myeloid_labels).astype(int)
        other_signal += obs[column].astype(str).isin(other_direct_labels).astype(int)

    b_signal += obs["majority_voting_Immune_All_Low"].astype(str).str.contains("B cell|Plasma|Plasmablast", case=False, regex=True, na=False).astype(int)
    b_signal += obs["panhuman_azimuth_fine"].astype(str).str.contains("B cell|Plasma|Plasmablast", case=False, regex=True, na=False).astype(int)
    t_signal += obs["majority_voting_Immune_All_Low"].astype(str).str.contains("T cell|helper|cytotoxic|MAIT|Treg|NK|gdT", case=False, regex=True, na=False).astype(int)
    t_signal += obs["panhuman_azimuth_fine"].astype(str).str.contains("T cell|CD4|CD8|MAIT|Treg|NK|gdT|Tfh", case=False, regex=True, na=False).astype(int)
    my_signal += obs["majority_voting_Immune_All_Low"].astype(str).str.contains("monocyte|macrophage|DC|dendritic|neutrophil", case=False, regex=True, na=False).astype(int)
    my_signal += obs["panhuman_azimuth_fine"].astype(str).str.contains("monocyte|macrophage|DC|cDC|pDC|neutrophil", case=False, regex=True, na=False).astype(int)
    other_signal += obs["majority_voting_Immune_All_Low"].astype(str).str.contains("Platelet|erythro|RBC|HSC", case=False, regex=True, na=False).astype(int)
    other_signal += obs["panhuman_azimuth_fine"].astype(str).str.contains("Platelet|erythro|RBC|HSC", case=False, regex=True, na=False).astype(int)

    for column in ["marker_score_B", "marker_score_Plasma"]:
        if column in obs.columns:
            b_signal += pd.to_numeric(obs[column], errors="coerce").fillna(0).ge(0.50).astype(int)
    for column in ["marker_score_T", "marker_score_CD4_T", "marker_score_CD8_T", "marker_score_NK"]:
        if column in obs.columns:
            t_signal += pd.to_numeric(obs[column], errors="coerce").fillna(0).ge(0.50).astype(int)
    for column in ["marker_score_Mono", "marker_score_CD16_Mono", "marker_score_DC", "marker_score_pDC"]:
        if column in obs.columns:
            my_signal += pd.to_numeric(obs[column], errors="coerce").fillna(0).ge(0.50).astype(int)

    lineage_scores = pd.DataFrame(
        {
            "B_lineage": b_signal,
            "T_NK_lineage": t_signal,
            "Myeloid_lineage": my_signal,
            "Other_lineage": other_signal,
        },
        index=obs.index,
    )
    lineage = lineage_scores.idxmax(axis=1)
    lineage_max = lineage_scores.max(axis=1)
    lineage_second = lineage_scores.apply(lambda row: row.sort_values(ascending=False).iloc[1], axis=1)
    lineage = lineage.where((lineage_max >= 2) & ((lineage_max - lineage_second) >= 1), "Ambiguous")

    if "doublet_flag_v3_independent" in obs.columns:
        doublet = obs["doublet_flag_v3_independent"].astype(str).str.lower().eq("true")
    elif "doublet_flag" in obs.columns:
        doublet = obs["doublet_flag"].astype(str).str.lower().eq("true")
    elif "predicted_doublet" in obs.columns:
        doublet = obs["predicted_doublet"].astype(str).str.lower().eq("true")
    else:
        doublet = pd.Series(False, index=obs.index)
    mixed = obs["mixed_lineage_marker_monitor_v3_independent"].astype(str).str.lower().eq("true") if "mixed_lineage_marker_monitor_v3_independent" in obs.columns else pd.Series(False, index=obs.index)
    lineage.loc[doublet] = "Ambiguous"

    annotation_label = pd.Series("Blood Cell", index=obs.index, dtype="object")
    annotation_conf = pd.Series(0.45, index=obs.index, dtype="float64")
    annotation_reason = pd.Series("ambiguous_default_blood_cell", index=obs.index, dtype="object")

    for direct_label in sorted(other_direct_labels):
        direct_votes = pd.Series(0, index=obs.index, dtype="int64")
        for column in ref_cols:
            direct_votes += obs[column].astype(str).eq(direct_label).astype(int)
        raw_direct = pd.Series(False, index=obs.index)
        for column in raw_cols:
            raw_direct |= obs[column].astype(str).str.contains(direct_label, case=False, regex=False, na=False)
        direct_mask = lineage.eq("Other_lineage") & direct_votes.ge(2) & raw_direct
        annotation_label.loc[direct_mask] = direct_label
        annotation_conf.loc[direct_mask] = 0.72
        annotation_reason.loc[direct_mask] = f"independent_other_direct_{direct_label}"

    for lineage_name, lineage_config in lineage_configs.items():
        mask = lineage.eq(lineage_name)
        if int(mask.sum()) < 50:
            adata.obs[f"{lineage_name}_leiden"] = "not_in_lineage"
            pd.DataFrame(columns=["cell_barcode", "study", "lineage", "local_cluster", "subcluster_label", "subcluster_reason", "local_umap_1", "local_umap_2"]).to_csv(
                tables_dir / f"{study}_{lineage_name}_true_subcluster_umap.tsv.gz", sep="\t", index=False
            )
            pd.DataFrame(columns=["study", "lineage", "cluster", "candidate_label", "rank_within_cluster", "n_cells", "marker_pct", "ref_fraction", "raw_fraction", "screfmapping_fraction", "total_score"]).to_csv(
                tables_dir / f"{study}_{lineage_name}_subcluster_candidate_scores.tsv", sep="\t", index=False
            )
            lineage_panel_status_rows.append(
                {
                    "study": study,
                    "lineage": lineage_name,
                    "n_cells": int(mask.sum()),
                    "status": "skipped_lt50",
                    "reason": "fewer than 50 cells assigned to this broad lineage",
                }
            )
            continue

        sub = adata[mask].copy()
        sc.pp.highly_variable_genes(sub, n_top_genes=min(3000, max(500, sub.n_vars - 1)), flavor="seurat")
        patterns_to_exclude = [
            "^IGKV", "^IGLV", "^IGHV", "^IGLC",
            "^TRAV", "^TRAJ", "^TRBV", "^TRBD", "^TRBJ",
            "^TRGV", "^TRGJ", "^TRDV", "^TRDD", "^TRDJ",
            "^MT-", "^RPL", "^RPS",
        ]
        excluded = sub.var_names.str.contains("|".join(patterns_to_exclude), flags=re.IGNORECASE)
        sub.var["highly_variable"] = sub.var["highly_variable"] & (~excluded)
        if int(sub.var["highly_variable"].sum()) >= 100:
            sub = sub[:, sub.var["highly_variable"]].copy()
        sc.pp.scale(sub, max_value=10)
        if sparse.issparse(sub.X):
            sub.X.data = np.nan_to_num(sub.X.data, nan=0.0, posinf=10.0, neginf=-10.0)
        else:
            sub.X = np.nan_to_num(sub.X, nan=0.0, posinf=10.0, neginf=-10.0)

        n_comps = min(30, sub.n_obs - 1, sub.n_vars - 1)
        sc.tl.pca(sub, n_comps=n_comps, svd_solver="arpack")
        sc.pp.neighbors(sub, n_neighbors=20, n_pcs=n_comps)
        chosen_key = f"leiden_{lineage_config['resolution']}"
        sc.tl.leiden(sub, resolution=lineage_config["resolution"], key_added=chosen_key)
        sc.tl.umap(sub, min_dist=0.35)

        cluster_values = pd.Series("not_in_lineage", index=adata.obs_names, dtype="object")
        cluster_values.loc[sub.obs_names] = sub.obs[chosen_key].astype(str).map(lambda x: f"{lineage_name}:{x}").values
        adata.obs[f"{lineage_name}_leiden"] = cluster_values.values

        lineage_obs = obs.loc[sub.obs_names].copy()
        lineage_obs["annotation_cluster"] = sub.obs[chosen_key].astype(str).values
        for score_col in lineage_config["candidate_scores"].values():
            lineage_obs[score_col] = obs.loc[sub.obs_names, score_col]
            sub.obs[score_col] = obs.loc[sub.obs_names, score_col].values

        lineage_marker_genes = []
        for candidate, score_col in lineage_config["candidate_scores"].items():
            marker_set = label_to_marker_set.get(candidate, "")
            lineage_marker_genes.extend(score_gene_sets.get(score_col.replace("_pct", ""), []))
            lineage_marker_genes.extend(marker_set_gene_lookup.get(marker_set, []))
            lineage_marker_genes.extend(marker_set_key_gene_lookup.get(marker_set, []))
        lineage_marker_genes = [gene for gene in dict.fromkeys(lineage_marker_genes) if gene in adata.var_names]
        lineage_expr = pd.DataFrame(index=sub.obs_names)
        lineage_positive = pd.DataFrame(index=sub.obs_names)
        if lineage_marker_genes:
            lineage_matrix = adata[sub.obs_names, lineage_marker_genes].X
            if sparse.issparse(lineage_matrix):
                lineage_matrix = lineage_matrix.toarray()
            lineage_expr = pd.DataFrame(lineage_matrix, index=sub.obs_names, columns=lineage_marker_genes)
            lineage_positive = lineage_expr.gt(0)

        cluster_to_label = {}
        cluster_to_marker_label = {}
        cluster_to_conf = {}
        cluster_to_reason = {}
        cluster_to_candidate_marker_scores = {candidate: {} for candidate in lineage_config["candidate_scores"]}
        lineage_candidate_score_rows = []
        for cluster_id in sorted(lineage_obs["annotation_cluster"].astype(str).unique()):
            cluster_mask = lineage_obs["annotation_cluster"].astype(str).eq(cluster_id)
            cluster_frame = lineage_obs.loc[cluster_mask]
            cluster_expr = lineage_expr.loc[cluster_frame.index] if not lineage_expr.empty else pd.DataFrame(index=cluster_frame.index)
            candidate_rows = []
            for candidate, score_col in lineage_config["candidate_scores"].items():
                ref_frac = source_fraction(cluster_frame, ref_cols, candidate)
                raw_frac = raw_fraction(cluster_frame, raw_cols, lineage_config["raw_bonus"][candidate])
                marker_pct = float(pd.to_numeric(cluster_frame[score_col], errors="coerce").median())
                scref_frac = source_fraction(cluster_frame, ["screfmapping_official_label"], candidate)
                marker_set = label_to_marker_set.get(candidate, "")
                marker_genes = list(score_gene_sets.get(score_col.replace("_pct", ""), []))
                marker_genes.extend(marker_set_gene_lookup.get(marker_set, []))
                key_genes = marker_set_key_gene_lookup.get(marker_set, [])
                marker_metrics = cluster_marker_metrics(cluster_expr, lineage_positive, marker_genes, key_genes)
                key_marker_bonus = 0.0
                if candidate == "Treg":
                    foxp3_fraction = float(cluster_expr["FOXP3"].gt(0).mean()) if "FOXP3" in cluster_expr.columns else 0.0
                    has_foxp3_support = foxp3_fraction >= 0.03
                    has_multi_key_support = marker_metrics["key_marker_two_fraction"] >= 0.05
                    has_treg_marker_context = (
                        marker_metrics["key_marker_any_fraction"] >= 0.25
                        and (has_foxp3_support or has_multi_key_support)
                    )
                    has_treg_reference_context = (ref_frac >= 0.30) or ((ref_frac >= 0.20) and (raw_frac >= 0.20))
                    if has_treg_marker_context and has_treg_reference_context:
                        key_marker_bonus = 0.80
                    elif marker_metrics["key_marker_any_fraction"] >= 0.18 and has_foxp3_support and ref_frac >= 0.20:
                        key_marker_bonus = 0.35
                marker_decision_score = max(marker_pct, marker_metrics["key_marker_any_fraction"], marker_metrics["marker_mean_positive_fraction"])
                marker_gate_score = min(1.0, marker_decision_score + key_marker_bonus)
                total_score = (1.6 * ref_frac) + raw_frac + marker_decision_score + (1.2 * scref_frac) + key_marker_bonus
                candidate_rows.append(
                    {
                        "candidate": candidate,
                        "ref_fraction": ref_frac,
                        "raw_fraction": raw_frac,
                        "marker_pct": marker_pct,
                        "marker_decision_score": marker_decision_score,
                        "marker_gate_score": marker_gate_score,
                        "key_marker_bonus": key_marker_bonus,
                        "screfmapping_fraction": scref_frac,
                        "total_score": total_score,
                        **marker_metrics,
                    }
                )
            candidate_df = pd.DataFrame(candidate_rows).sort_values("total_score", ascending=False)
            best = candidate_df.iloc[0]
            marker_best = candidate_df.sort_values(
                ["marker_gate_score", "key_marker_bonus", "key_marker_any_fraction", "marker_pct"],
                ascending=False,
            ).iloc[0]
            second_score = float(candidate_df.iloc[1]["total_score"]) if candidate_df.shape[0] > 1 else 0.0
            for rank, candidate_row in enumerate(candidate_df.itertuples(index=False), start=1):
                score_row = {
                    "study": study,
                    "lineage": lineage_name,
                    "cluster": cluster_id,
                    "candidate_label": candidate_row.candidate,
                    "rank_within_cluster": rank,
                    "n_cells": int(cluster_mask.sum()),
                    "marker_pct": float(candidate_row.marker_pct),
                    "marker_decision_score": float(candidate_row.marker_decision_score),
                    "marker_gate_score": float(candidate_row.marker_gate_score),
                    "key_marker_bonus": float(candidate_row.key_marker_bonus),
                    "marker_any_fraction": float(candidate_row.marker_any_fraction),
                    "marker_mean_positive_fraction": float(candidate_row.marker_mean_positive_fraction),
                    "key_marker_any_fraction": float(candidate_row.key_marker_any_fraction),
                    "key_marker_two_fraction": float(candidate_row.key_marker_two_fraction),
                    "key_marker_max_fraction": float(candidate_row.key_marker_max_fraction),
                    "key_marker_enrichment": float(candidate_row.key_marker_enrichment),
                    "ref_fraction": float(candidate_row.ref_fraction),
                    "raw_fraction": float(candidate_row.raw_fraction),
                    "screfmapping_fraction": float(candidate_row.screfmapping_fraction),
                    "total_score": float(candidate_row.total_score),
                }
                lineage_candidate_score_rows.append(score_row)
                subcluster_candidate_score_rows.append(score_row)
                cluster_to_candidate_marker_scores[candidate_row.candidate][cluster_id] = float(candidate_row.marker_gate_score)
            accepted = (float(best["total_score"]) >= 1.05) and (
                (float(best["ref_fraction"]) >= 0.25)
                or (float(best["raw_fraction"]) >= 0.35)
                or (float(best["marker_decision_score"]) >= 0.72)
                or (float(best["screfmapping_fraction"]) >= 0.35)
                or (float(best["key_marker_bonus"]) >= 0.70)
            )
            if lineage_name == "B_lineage" and best["candidate"] == "Plasma Cell":
                accepted = accepted and ((float(best["marker_decision_score"]) >= 0.65) or (float(best["ref_fraction"]) >= 0.40))
            if lineage_name == "T_NK_lineage" and best["candidate"] == "NK Cell":
                accepted = accepted and ((float(best["marker_decision_score"]) >= 0.65) or (float(best["ref_fraction"]) >= 0.35))
            if lineage_name == "T_NK_lineage" and best["candidate"] == "Treg":
                accepted = accepted and (
                    (float(best["key_marker_bonus"]) >= 0.70)
                    or (
                        float(best["ref_fraction"]) >= 0.45
                        and float(best["key_marker_any_fraction"]) >= 0.20
                    )
                )
            if lineage_name == "Myeloid_lineage" and best["candidate"] in {"Plasmacytoid DC", "Conventional DC 1", "Conventional DC 2"}:
                accepted = accepted and ((float(best["marker_decision_score"]) >= 0.60) or (float(best["ref_fraction"]) >= 0.35))

            marker_set = label_to_marker_set.get(str(best["candidate"]), "not_applicable")
            marker_alert = study_marker_alert.get(marker_set, "pass")
            single_scref_rescue = (
                float(best["screfmapping_fraction"]) >= 0.35
                and float(best["ref_fraction"]) < 0.25
                and float(best["raw_fraction"]) < 0.35
                and float(best["marker_decision_score"]) < 0.72
            )
            if marker_alert == "critical" and single_scref_rescue:
                accepted = False
            if marker_alert == "warning" and single_scref_rescue:
                accepted = False

            chosen_label = str(best["candidate"]) if accepted else lineage_config["parent"]
            cluster_to_label[cluster_id] = chosen_label
            cluster_to_marker_label[cluster_id] = str(marker_best["candidate"])
            purity = max(float(best["ref_fraction"]), float(best["raw_fraction"]), float(best["marker_decision_score"]))
            margin = float(best["total_score"]) - second_score
            support_terms = [
                min(float(best["ref_fraction"]) / 0.60, 1.0),
                min(float(best["raw_fraction"]) / 0.60, 1.0),
                min(float(best["marker_decision_score"]) / 0.85, 1.0),
                min(max(margin, 0.0) / 0.75, 1.0),
            ]
            if cluster_frame["screfmapping_official_label"].astype(str).ne("not_available").any():
                support_terms.append(min(float(best["screfmapping_fraction"]) / 0.60, 1.0))
            calibrated_conf = 0.30 + (0.55 * np.mean(support_terms))
            if not accepted:
                calibrated_conf = min(calibrated_conf, 0.55)
            elif margin < 0.15:
                calibrated_conf = min(calibrated_conf, 0.68)
            elif margin < 0.30:
                calibrated_conf = min(calibrated_conf, 0.78)
            if accepted and marker_alert in marker_alert_confidence_caps:
                calibrated_conf = min(calibrated_conf, float(marker_alert_confidence_caps[marker_alert]))
            cluster_to_conf[cluster_id] = min(0.93, max(0.35, calibrated_conf))
            marker_suffix = f"_marker_{marker_alert}" if marker_alert in {"critical", "warning"} else ""
            cluster_to_reason[cluster_id] = f"independent_{lineage_name}_subcluster_to_{chosen_label.replace(' ', '_')}{marker_suffix}"

            row = {
                "study": study,
                "lineage": lineage_name,
                "cluster": cluster_id,
                "n_cells": int(cluster_mask.sum()),
                "chosen_label": chosen_label,
                "accepted": bool(accepted),
                "best_total_score": float(best["total_score"]),
                "second_total_score": second_score,
                "score_margin": margin,
                "calibrated_cluster_confidence": cluster_to_conf[cluster_id],
                "top_celltypist": "; ".join([f"{k}:{v}" for k, v in cluster_frame["celltypist_v3_label"].astype(str).value_counts().head(5).items()]),
                "top_panhuman_fine": "; ".join([f"{k}:{v}" for k, v in cluster_frame["panhuman_fine_v3_label"].astype(str).value_counts().head(5).items()]),
                "top_cluster_consensus": "; ".join([f"{k}:{v}" for k, v in cluster_frame["cluster_consensus_v3_label"].astype(str).value_counts().head(5).items()]),
                "top_marker": "; ".join([f"{k}:{v}" for k, v in cluster_frame["top_marker_v3_label"].astype(str).value_counts().head(5).items()]),
                "top_screfmapping": "; ".join([f"{k}:{v}" for k, v in cluster_frame["screfmapping_official_label"].astype(str).value_counts().head(5).items()]),
                "cluster_marker_gene_assignment": cluster_to_marker_label[cluster_id],
                "marker_set": marker_set,
                "marker_availability_alert": marker_alert,
                "single_screfmapping_rescue_blocked": bool(single_scref_rescue and marker_alert in {"critical", "warning"}),
            }
            for column in ["n_genes_by_counts", "total_counts", "pct_counts_mt"]:
                if column in obs.columns:
                    row[f"median_{column}"] = float(pd.to_numeric(obs.loc[cluster_frame.index, column], errors="coerce").median())
            for item in candidate_rows:
                row[f"{item['candidate']}_total_score"] = item["total_score"]
                row[f"{item['candidate']}_ref_fraction"] = item["ref_fraction"]
                row[f"{item['candidate']}_raw_fraction"] = item["raw_fraction"]
                row[f"{item['candidate']}_marker_pct"] = item["marker_pct"]
                row[f"{item['candidate']}_marker_decision_score"] = item["marker_decision_score"]
                row[f"{item['candidate']}_marker_gate_score"] = item["marker_gate_score"]
                row[f"{item['candidate']}_key_marker_bonus"] = item["key_marker_bonus"]
                row[f"{item['candidate']}_key_marker_any_fraction"] = item["key_marker_any_fraction"]
                row[f"{item['candidate']}_key_marker_two_fraction"] = item["key_marker_two_fraction"]
                row[f"{item['candidate']}_key_marker_max_fraction"] = item["key_marker_max_fraction"]
                row[f"{item['candidate']}_screfmapping_fraction"] = item["screfmapping_fraction"]
            subcluster_rows.append(row)

        sub.obs["subcluster_label"] = sub.obs[chosen_key].astype(str).map(cluster_to_label).astype(str)
        sub.obs["cluster_marker_gene_assignment"] = sub.obs[chosen_key].astype(str).map(cluster_to_marker_label).astype(str)
        sub.obs["subcluster_reason"] = sub.obs[chosen_key].astype(str).map(cluster_to_reason).astype(str)
        cluster_marker_score_cols = []
        for candidate, cluster_scores in cluster_to_candidate_marker_scores.items():
            safe_candidate = re.sub(r"[^A-Za-z0-9]+", "_", candidate).strip("_").lower()
            score_column = f"cluster_marker_score_{safe_candidate}"
            sub.obs[score_column] = sub.obs[chosen_key].astype(str).map(cluster_scores).astype(float)
            cluster_marker_score_cols.append(score_column)

        local_umap = pd.DataFrame(
            {
                "cell_barcode": sub.obs_names.astype(str),
                "study": study,
                "lineage": lineage_name,
                "local_cluster": sub.obs[chosen_key].astype(str).values,
                "subcluster_label": sub.obs["subcluster_label"].astype(str).values,
                "subcluster_reason": sub.obs["subcluster_reason"].astype(str).values,
                "celltypist_label": sub.obs["celltypist_v3_label"].astype(str).values if "celltypist_v3_label" in sub.obs.columns else "not_available",
                "panhuman_fine_label": sub.obs["panhuman_fine_v3_label"].astype(str).values if "panhuman_fine_v3_label" in sub.obs.columns else "not_available",
                "panhuman_azimuth_fine": sub.obs["panhuman_azimuth_fine"].astype(str).values if "panhuman_azimuth_fine" in sub.obs.columns else "not_available",
                "cluster_consensus_label": sub.obs["cluster_consensus_v3_label"].astype(str).values if "cluster_consensus_v3_label" in sub.obs.columns else "not_available",
                "marker_gene_based_assignment": sub.obs["cluster_marker_gene_assignment"].astype(str).values,
                "cellwise_marker_gene_label": sub.obs["top_marker_v3_label"].astype(str).values if "top_marker_v3_label" in sub.obs.columns else "not_available",
                "screfmapping_label": sub.obs["screfmapping_official_label"].astype(str).values if "screfmapping_official_label" in sub.obs.columns else "not_available",
                "local_umap_1": sub.obsm["X_umap"][:, 0],
                "local_umap_2": sub.obsm["X_umap"][:, 1],
            }
        )
        for candidate, score_col in lineage_config["candidate_scores"].items():
            local_umap[f"{candidate}_marker_pct"] = pd.to_numeric(sub.obs[score_col], errors="coerce").values
            safe_candidate = re.sub(r"[^A-Za-z0-9]+", "_", candidate).strip("_").lower()
            local_umap[f"{candidate}_cluster_marker_decision_score"] = pd.to_numeric(sub.obs[f"cluster_marker_score_{safe_candidate}"], errors="coerce").values
            local_umap[f"{candidate}_cluster_marker_gate_score"] = pd.to_numeric(sub.obs[f"cluster_marker_score_{safe_candidate}"], errors="coerce").values
        local_umap.to_csv(tables_dir / f"{study}_{lineage_name}_true_subcluster_umap.tsv.gz", sep="\t", index=False)
        subcluster_umap_rows.append({"study": study, "lineage": lineage_name, "n_cells": int(sub.n_obs), "n_local_clusters": int(sub.obs[chosen_key].astype(str).nunique())})
        lineage_panel_status_rows.append(
            {
                "study": study,
                "lineage": lineage_name,
                "n_cells": int(sub.n_obs),
                "status": "generated",
                "reason": "true lineage-specific subcluster UMAP generated",
            }
        )

        lineage_candidate_score_df = pd.DataFrame(lineage_candidate_score_rows)
        lineage_candidate_score_df.to_csv(tables_dir / f"{study}_{lineage_name}_subcluster_candidate_scores.tsv", sep="\t", index=False)
        if not lineage_candidate_score_df.empty:
            heatmap = lineage_candidate_score_df.pivot(index="candidate_label", columns="cluster", values="marker_gate_score").fillna(0)
            fig, ax = plt.subplots(figsize=(max(5, 0.35 * heatmap.shape[1]), max(3, 0.35 * heatmap.shape[0])))
            image = ax.imshow(heatmap.values, aspect="auto", vmin=0, vmax=1, cmap="viridis")
            ax.set_xticks(np.arange(heatmap.shape[1]))
            ax.set_xticklabels(heatmap.columns.astype(str), rotation=90, fontsize=7)
            ax.set_yticks(np.arange(heatmap.shape[0]))
            ax.set_yticklabels(heatmap.index.astype(str), fontsize=8)
            ax.set_xlabel("Local subcluster")
            ax.set_ylabel("Candidate label")
            ax.set_title(f"{study} {lineage_name} cluster marker gate score")
            fig.colorbar(image, ax=ax, label="cluster marker gate score")
            fig.tight_layout()
            fig.savefig(asset_dir / f"subcluster_marker_score_heatmap_{study}_{lineage_name}.png", dpi=180)
            fig.savefig(figures_dir / f"subcluster_marker_score_heatmap_{study}_{lineage_name}.pdf")
            plt.close(fig)

        sc.pl.umap(
            sub,
            color=[chosen_key, "subcluster_label"],
            ncols=1,
            legend_loc="right margin",
            legend_fontsize=6,
            legend_fontoutline=1,
            wspace=0.75,
            frameon=False,
            show=False,
            save=f"_{study}_{lineage_name}_true_subcluster_label.png",
        )
        plt.close("all")
        source_label_colors = [
            column
            for column in [
                "celltypist_v3_label",
                "panhuman_fine_v3_label",
                "panhuman_azimuth_fine",
                "cluster_consensus_v3_label",
                "cluster_marker_gene_assignment",
                "top_marker_v3_label",
                "screfmapping_official_label",
                "subcluster_label",
            ]
            if column in sub.obs.columns
        ]
        if source_label_colors:
            sc.pl.umap(
                sub,
                color=source_label_colors,
                ncols=1,
                legend_loc="right margin",
                legend_fontsize=6,
                legend_fontoutline=1,
                wspace=0.75,
                frameon=False,
                show=False,
                save=f"_{study}_{lineage_name}_true_subcluster_source_labels.png",
            )
            plt.close("all")
        sub_qc_colors = [column for column in ["n_genes_by_counts", "pct_counts_mt", "subcluster_reason"] if column in sub.obs.columns]
        if sub_qc_colors:
            sc.pl.umap(
                sub,
                color=sub_qc_colors,
                ncols=1,
                legend_loc="right margin",
                legend_fontsize=6,
                legend_fontoutline=1,
                wspace=0.75,
                frameon=False,
                show=False,
                save=f"_{study}_{lineage_name}_true_subcluster_qc.png",
            )
            plt.close("all")
        sc.pl.umap(sub, color=cluster_marker_score_cols, ncols=3, wspace=0.45, frameon=False, show=False, save=f"_{study}_{lineage_name}_true_subcluster_marker_scores.png")
        plt.close("all")

        if lineage_marker_genes:
            sub_plot = adata[sub.obs_names, lineage_marker_genes].copy()
            sub_plot.obsm["X_umap"] = sub.obsm["X_umap"].copy()
            sub_plot.obs[chosen_key] = sub.obs[chosen_key].astype(str).values
            sub_plot.obs["subcluster_label"] = sub.obs["subcluster_label"].astype(str).values
            sub_plot.obs["subcluster_reason"] = sub.obs["subcluster_reason"].astype(str).values
            sc.pl.umap(sub_plot, color=lineage_marker_genes, ncols=4, wspace=0.45, frameon=False, show=False, save=f"_{study}_{lineage_name}_true_subcluster_marker_expression.png")
            plt.close("all")
            sc.pl.dotplot(sub_plot, var_names=lineage_marker_genes, groupby="subcluster_label", standard_scale="var", dendrogram=False, show=False, save=f"_{study}_{lineage_name}_true_subcluster_marker_dotplot.png")
            plt.close("all")
            dotplot_png = figures_dir / f"dotplot__{study}_{lineage_name}_true_subcluster_marker_dotplot.png"
            if dotplot_png.exists():
                asset_dir.joinpath(f"dotplot_{study}_{lineage_name}_true_subcluster_marker_dotplot.png").write_bytes(dotplot_png.read_bytes())
            del sub_plot

        for figure_name in [
            f"umap_{study}_{lineage_name}_true_subcluster_label.png",
            f"umap_{study}_{lineage_name}_true_subcluster_source_labels.png",
            f"umap_{study}_{lineage_name}_true_subcluster_qc.png",
            f"umap_{study}_{lineage_name}_true_subcluster_marker_scores.png",
            f"umap_{study}_{lineage_name}_true_subcluster_marker_expression.png",
        ]:
            source_png = figures_dir / figure_name
            if source_png.exists():
                asset_dir.joinpath(figure_name).write_bytes(source_png.read_bytes())

        full_cluster = adata.obs.loc[obs.index, f"{lineage_name}_leiden"].astype(str).str.replace(f"{lineage_name}:", "", regex=False)
        in_lineage = lineage.eq(lineage_name)
        proposed = full_cluster.map(cluster_to_label)
        proposed_conf = full_cluster.map(cluster_to_conf)
        proposed_reason = full_cluster.map(cluster_to_reason)
        annotation_label.loc[in_lineage & proposed.notna()] = proposed.loc[in_lineage & proposed.notna()].astype(str)
        annotation_conf.loc[in_lineage & proposed_conf.notna()] = proposed_conf.loc[in_lineage & proposed_conf.notna()].astype(float)
        annotation_reason.loc[in_lineage & proposed_reason.notna()] = proposed_reason.loc[in_lineage & proposed_reason.notna()].astype(str)

        del sub

    # Independent fallback for ambiguous cells with two exact source votes.
    source_vote_labels = []
    for label in sorted((b_labels | t_labels | myeloid_labels | other_direct_labels) & submit_allowed):
        votes = pd.Series(0, index=obs.index, dtype="int64")
        for column in ref_cols:
            votes += obs[column].astype(str).eq(label).astype(int)
        source_vote_labels.append((label, votes))
    fallback_mask = lineage.eq("Ambiguous") & ~doublet
    for label, votes in source_vote_labels:
        assign = fallback_mask & votes.ge(3) & annotation_label.eq("Blood Cell")
        annotation_label.loc[assign] = label
        annotation_conf.loc[assign] = 0.62
        annotation_reason.loc[assign] = f"independent_ambiguous_exact_source_votes_{label}"

    low_qc = pd.Series(False, index=obs.index)
    if "n_genes_by_counts" in obs.columns:
        low_qc |= pd.to_numeric(obs["n_genes_by_counts"], errors="coerce").fillna(99999).lt(500)
    if "pct_counts_mt" in obs.columns:
        low_qc |= pd.to_numeric(obs["pct_counts_mt"], errors="coerce").fillna(0).gt(20)
    annotation_conf.loc[(low_qc | mixed) & ~doublet] = annotation_conf.loc[(low_qc | mixed) & ~doublet].clip(0.05, 0.65)

    annotation_label.loc[annotation_label.eq("Effector B")] = "B Cell"
    annotation_label = annotation_label.where(annotation_label.isin(submit_allowed), "Blood Cell")
    annotation_label.loc[doublet] = "Doublet"
    annotation_reason.loc[doublet] = "doublet_override"
    annotation_conf.loc[doublet] = annotation_conf.loc[doublet].clip(0.05, 0.60)

    final_marker_set = annotation_label.map(label_to_marker_set).fillna("not_applicable")
    final_marker_alert = final_marker_set.map(study_marker_alert).fillna("not_applicable")
    for alert_level, cap in marker_alert_confidence_caps.items():
        cap_mask = final_marker_alert.eq(alert_level) & ~doublet
        annotation_conf.loc[cap_mask] = annotation_conf.loc[cap_mask].clip(0.05, float(cap))

    evidence_cols = [column for column in ref_cols + ["screfmapping_official_label"] if column in obs.columns]
    source_agreement_n = pd.Series(0, index=obs.index, dtype="int64")
    source_informative_n = pd.Series(0, index=obs.index, dtype="int64")
    for column in evidence_cols:
        values = obs[column].astype(str)
        informative = values.ne("not_available")
        source_informative_n += informative.astype(int)
        source_agreement_n += (informative & values.eq(annotation_label.astype(str))).astype(int)
    source_disagreement_n = (source_informative_n - source_agreement_n).clip(lower=0)
    source_agreement_fraction = (source_agreement_n / source_informative_n.replace(0, np.nan)).fillna(0.0)
    source_disagreement_flag = source_disagreement_n.ge(2) & source_agreement_fraction.lt(0.50)

    submission = pd.DataFrame(
        {
            "cell_barcode": adata.obs_names.astype(str),
            "predicted_cell_type": annotation_label.astype(str).values,
            "confidence_score": annotation_conf.round(4).values,
        }
    )
    submission.to_csv(submission_dir / f"{study}_annotation.tsv", sep="\t", index=False)

    for column in obs.columns:
        if column.startswith("marker_score_"):
            adata.obs[column] = pd.to_numeric(obs[column], errors="coerce").values
    adata.obs["submission_cell_type"] = annotation_label.astype(str).values
    adata.obs["confidence_score"] = annotation_conf.round(4).values
    adata.obs["parent_lineage"] = lineage.astype(str).values
    adata.obs["annotation_reason"] = annotation_reason.astype(str).values
    adata.obs["annotation_logic_version"] = version
    adata.obs["marker_availability_alert_for_label"] = final_marker_alert.astype(str).values
    adata.obs["source_agreement_n"] = source_agreement_n.values
    adata.obs["source_informative_n"] = source_informative_n.values
    adata.obs["source_disagreement_n"] = source_disagreement_n.values
    adata.obs["source_agreement_fraction"] = source_agreement_fraction.round(4).values
    adata.obs["source_disagreement_flag"] = source_disagreement_flag.astype(str).values

    diagnostics_cols = [
        "submission_cell_type",
        "confidence_score",
        "parent_lineage",
        "annotation_reason",
        "marker_availability_alert_for_label",
        "source_agreement_n",
        "source_informative_n",
        "source_disagreement_n",
        "source_agreement_fraction",
        "source_disagreement_flag",
        "B_lineage_leiden",
        "T_NK_lineage_leiden",
        "Myeloid_lineage_leiden",
        "celltypist_v3_label",
        "panhuman_fine_v3_label",
        "cluster_consensus_v3_label",
        "top_marker_v3_label",
        "majority_voting_Immune_All_Low",
        "panhuman_azimuth_fine",
        "screfmapping_query_type",
        "screfmapping_clusterL1",
        "screfmapping_clusterL1_prob",
        "screfmapping_clusterL2",
        "screfmapping_clusterL2_prob",
        "screfmapping_official_label",
    ]
    diagnostics_cols = [column for column in diagnostics_cols if column in adata.obs.columns]
    diagnostics = adata.obs[diagnostics_cols].copy()
    diagnostics.insert(0, "cell_barcode", adata.obs_names.astype(str))
    diagnostics.to_csv(tables_dir / f"{study}_annotation_diagnostics.tsv.gz", sep="\t", index=False)

    sc.pl.umap(adata, color=["submission_cell_type"], legend_loc="right margin", frameon=False, show=False, save=f"_{study}_annotation_label.png")
    plt.close("all")
    sc.pl.umap(adata, color=["parent_lineage", "annotation_reason"], legend_loc="right margin", frameon=False, show=False, save=f"_{study}_annotation_lineage_reason.png")
    plt.close("all")
    sc.pl.umap(adata, color=["n_genes_by_counts", "pct_counts_mt", "confidence_score"], frameon=False, show=False, save=f"_{study}_annotation_qc_confidence.png")
    plt.close("all")
    sc.pl.umap(adata, color=["source_agreement_fraction", "source_disagreement_n", "source_disagreement_flag"], frameon=False, show=False, save=f"_{study}_annotation_source_disagreement.png")
    plt.close("all")

    focus_markers = [
        "MS4A1", "CD79A", "TCL1A", "IGHM", "IGHD", "CD27", "TNFRSF13B", "MZB1", "JCHAIN", "XBP1",
        "CD3D", "CD3E", "CD4", "IL7R", "CCR7", "TCF7", "FOXP3", "IL2RA",
        "CD8A", "NKG7", "GNLY", "GZMB", "SLC4A10", "TRDC",
        "LYZ", "S100A8", "S100A9", "FCGR3A", "MS4A7", "LILRA4", "CLEC4C", "CD1C", "FCER1A", "CLEC9A", "XCR1",
    ]
    available_markers = [gene for gene in focus_markers if gene in adata.var_names]
    sc.pl.dotplot(adata, var_names=available_markers, groupby="submission_cell_type", standard_scale="var", dendrogram=False, show=False, save=f"_{study}_annotation_marker_dotplot.png")
    plt.close("all")

    feature_markers = [
        "MS4A1", "CD79A", "MZB1", "CD3D", "CD4", "CD8A",
        "NKG7", "GNLY", "LYZ", "S100A8", "FCGR3A", "LILRA4",
    ]
    available_feature_markers = [gene for gene in feature_markers if gene in adata.var_names]
    if available_feature_markers:
        sc.pl.umap(adata, color=available_feature_markers, ncols=4, frameon=False, show=False, save=f"_{study}_annotation_marker_expression.png")
        plt.close("all")

    for figure_name in [
        f"umap_{study}_annotation_label.png",
        f"umap_{study}_annotation_lineage_reason.png",
        f"umap_{study}_annotation_qc_confidence.png",
        f"umap_{study}_annotation_source_disagreement.png",
        f"umap_{study}_annotation_marker_expression.png",
    ]:
        source_png = figures_dir / figure_name
        if source_png.exists():
            asset_dir.joinpath(figure_name).write_bytes(source_png.read_bytes())
    dotplot_png = figures_dir / f"dotplot__{study}_annotation_marker_dotplot.png"
    if dotplot_png.exists():
        asset_dir.joinpath(f"dotplot_{study}_annotation_marker_dotplot.png").write_bytes(dotplot_png.read_bytes())

    label_counts = submission["predicted_cell_type"].value_counts()
    for label_name, n_cells in label_counts.items():
        label_rows.append({"study": study, "predicted_cell_type": label_name, "n_cells": int(n_cells)})
    for reason, n_cells in annotation_reason.value_counts().items():
        reason_rows.append({"study": study, "annotation_reason": reason, "n_cells": int(n_cells)})
    for row in (
        pd.DataFrame(
            {
                "predicted_cell_type": annotation_label.astype(str),
                "source_agreement_fraction": source_agreement_fraction,
                "source_disagreement_flag": source_disagreement_flag,
            }
        )
        .groupby("predicted_cell_type")
        .agg(
            n_cells=("predicted_cell_type", "size"),
            median_source_agreement_fraction=("source_agreement_fraction", "median"),
            source_disagreement_flag_n=("source_disagreement_flag", "sum"),
        )
        .reset_index()
        .itertuples(index=False)
    ):
        source_disagreement_rows.append(
            {
                "study": study,
                "predicted_cell_type": row.predicted_cell_type,
                "n_cells": int(row.n_cells),
                "median_source_agreement_fraction": float(row.median_source_agreement_fraction),
                "source_disagreement_flag_n": int(row.source_disagreement_flag_n),
                "source_disagreement_flag_fraction": float(row.source_disagreement_flag_n / row.n_cells),
            }
        )
        if float(row.source_disagreement_flag_n / row.n_cells) > float(review_concern_thresholds["label_source_disagreement_fraction_gt"]):
            concern_rows.append(
                {
                    "study": study,
                    "concern": f"High source disagreement for {row.predicted_cell_type}",
                    "n_cells": int(row.source_disagreement_flag_n),
                }
            )
    if float(source_disagreement_flag.mean()) > float(review_concern_thresholds["dataset_source_disagreement_fraction_gt"]):
        concern_rows.append({"study": study, "concern": "High dataset-level source disagreement", "n_cells": int(source_disagreement_flag.sum())})
    for marker_set, alert_level in study_marker_alert.items():
        if alert_level not in {"critical", "warning"}:
            continue
        affected_labels = set(marker_set_to_labels.get(marker_set, []))
        affected_n = int(annotation_label.astype(str).isin(affected_labels).sum())
        if affected_n:
            concern_rows.append({"study": study, "concern": f"{alert_level} marker availability for {marker_set}", "n_cells": affected_n})

    invalid = sorted(set(submission["predicted_cell_type"]) - official_set)
    summary_rows.append(
        {
            "study": study,
            "n_cells": int(adata.n_obs),
            "n_genes": int(adata.n_vars),
            "pre_hvg_n_genes": int(adata.raw.n_vars) if adata.raw is not None else int(adata.n_vars),
            "counts_layer_n_genes": int(adata.layers["counts"].shape[1]) if "counts" in adata.layers else int(adata.n_vars),
            "n_labels": int(submission["predicted_cell_type"].nunique()),
            "b_cell_n": int(submission["predicted_cell_type"].eq("B Cell").sum()),
            "t_cell_n": int(submission["predicted_cell_type"].eq("T Cell").sum()),
            "myeloid_cell_n": int(submission["predicted_cell_type"].eq("Myeloid Cell").sum()),
            "blood_cell_n": int(submission["predicted_cell_type"].eq("Blood Cell").sum()),
            "parent_or_blood_n": int(submission["predicted_cell_type"].isin(["B Cell", "T Cell", "Myeloid Cell", "Blood Cell"]).sum()),
            "parent_or_blood_fraction": float(submission["predicted_cell_type"].isin(["B Cell", "T Cell", "Myeloid Cell", "Blood Cell"]).mean()),
            "artifact_n": int(submission["predicted_cell_type"].isin(sorted(other_direct_labels)).sum()),
            "doublet_n": int(submission["predicted_cell_type"].eq("Doublet").sum()),
            "effector_b_n": int(submission["predicted_cell_type"].eq("Effector B").sum()),
            "median_confidence": float(submission["confidence_score"].median()),
            "low_confidence_n": int(submission["confidence_score"].lt(0.60).sum()),
            "source_disagreement_flag_n": int(source_disagreement_flag.sum()),
            "source_disagreement_flag_fraction": float(source_disagreement_flag.mean()),
            "invalid_labels": ",".join(invalid),
        }
    )
    validation_rows.append({"study": study, "n_submission_rows": int(submission.shape[0]), "n_h5ad_cells": int(adata.n_obs), "invalid_labels": ",".join(invalid)})

    ambiguous_n = int(annotation_label.eq("Blood Cell").sum())
    if ambiguous_n > 1000:
        concern_rows.append({"study": study, "concern": "Large Blood Cell/ambiguous residual remains", "n_cells": ambiguous_n})
    if int(submission["confidence_score"].lt(0.60).sum()) > 10000:
        concern_rows.append({"study": study, "concern": "Many low-confidence cells; QC or mixed-marker effects likely remain", "n_cells": int(submission["confidence_score"].lt(0.60).sum())})

    adata.write_h5ad(cxg_dir / f"{study}.final_annotation.cxg.h5ad", compression="gzip")
    del adata

summary_df = pd.DataFrame(summary_rows)
label_df = pd.DataFrame(label_rows)
reason_df = pd.DataFrame(reason_rows)
subcluster_df = pd.DataFrame(subcluster_rows)
validation_df = pd.DataFrame(validation_rows)
concern_df = pd.DataFrame(concern_rows)
source_disagreement_df = pd.DataFrame(source_disagreement_rows)
marker_availability_df = pd.DataFrame(marker_availability_rows)
marker_alert_df = marker_availability_df[marker_availability_df["alert_level"].isin(["critical", "warning"])].copy()
marker_availability_df.to_csv(tables_dir / "marker_gene_availability.tsv", sep="\t", index=False)
marker_alert_df.to_csv(tables_dir / "marker_gene_availability_alerts.tsv", sep="\t", index=False)
pd.DataFrame(subcluster_candidate_score_rows).to_csv(tables_dir / "subcluster_candidate_scores.tsv", sep="\t", index=False)
pd.DataFrame(subcluster_umap_rows).to_csv(tables_dir / "true_subcluster_umap_summary.tsv", sep="\t", index=False)
lineage_panel_status_df = pd.DataFrame(lineage_panel_status_rows)
lineage_panel_status_df.to_csv(tables_dir / "lineage_panel_status.tsv", sep="\t", index=False)

summary_df.to_csv(tables_dir / "final_annotation_summary.tsv", sep="\t", index=False)
label_df.to_csv(tables_dir / "final_annotation_label_counts.tsv", sep="\t", index=False)
reason_df.to_csv(tables_dir / "annotation_reason_counts.tsv", sep="\t", index=False)
subcluster_df.to_csv(tables_dir / "lineage_subcluster_evidence.tsv.gz", sep="\t", index=False)
validation_df.to_csv(tables_dir / "final_annotation_validation.tsv", sep="\t", index=False)
concern_df.to_csv(tables_dir / "review_concerns.tsv", sep="\t", index=False)
source_disagreement_df.to_csv(tables_dir / "source_disagreement_summary.tsv", sep="\t", index=False)

(output_root / "final_annotation_summary.json").write_text(
    json.dumps({"version": version, "manifest": str(project_path(args.manifest)), "summary": summary_df.to_dict(orient="records")}, indent=2),
    encoding="utf-8",
)

fig, ax = plt.subplots(figsize=(6, 4))
summary_df.plot(x="study", y="parent_or_blood_fraction", kind="bar", ax=ax, legend=False)
ax.set_ylabel("Parent/Blood Cell fraction")
ax.set_xlabel("")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
fig.savefig(asset_dir / "figure_01_annotation_parent_or_blood_fraction.png", dpi=180)
fig.savefig(figures_dir / "figure_01_annotation_parent_or_blood_fraction.pdf")
plt.close(fig)

asset_link_root = "assets"
requested_languages = [language.strip() for language in args.report_languages.split(",") if language.strip()]
report_title = ", ".join(summary_df["study"].astype(str).tolist())

summary_rows = []
for row in summary_df.itertuples(index=False):
    summary_rows.append(
        {
            "study": row.study,
            "cells": f"{row.n_cells:,}",
            "analysis_X_genes": f"{row.n_genes:,}",
            "pre_hvg_genes": f"{row.pre_hvg_n_genes:,}",
            "counts_layer_genes": f"{row.counts_layer_n_genes:,}",
            "labels": row.n_labels,
            "parent_or_blood_fraction": f"{row.parent_or_blood_fraction:.3f}",
            "Blood Cell": f"{row.blood_cell_n:,}",
            "Doublet": f"{row.doublet_n:,}",
            "artifact_like": f"{row.artifact_n:,}",
            "median_confidence": f"{row.median_confidence:.3f}",
            "low_confidence": f"{row.low_confidence_n:,}",
            "source_disagreement": f"{row.source_disagreement_flag_n:,} ({row.source_disagreement_flag_fraction:.3f})",
            "invalid_labels": row.invalid_labels if row.invalid_labels else "none",
        }
    )
marker_alert_rows = []
for row in marker_alert_df.itertuples(index=False):
    marker_alert_rows.append(
        {
            "study": row.study,
            "marker_set": row.marker_set,
            "alert": row.alert_level,
            "present_fraction": f"{float(row.present_fraction):.3f}",
            "missing_critical_markers": row.missing_critical_markers or "none",
            "missing_genes": row.missing_genes or "none",
        }
    )

concern_rows_for_report = []
if not concern_df.empty:
    for row in concern_df.itertuples(index=False):
        concern_rows_for_report.append({"study": row.study, "concern": row.concern, "cells": f"{row.n_cells:,}"})

label_rows_for_report = []
for row in label_df.itertuples(index=False):
    label_rows_for_report.append({"study": row.study, "predicted_cell_type": row.predicted_cell_type, "cells": f"{row.n_cells:,}"})

source_disagreement_rows_for_report = []
if not source_disagreement_df.empty:
    for row in source_disagreement_df.sort_values(["source_disagreement_flag_fraction", "source_disagreement_flag_n"], ascending=False).head(12).itertuples(index=False):
        source_disagreement_rows_for_report.append(
            {
                "study": row.study,
                "predicted_cell_type": row.predicted_cell_type,
                "cells": f"{row.n_cells:,}",
                "median_source_agreement": f"{row.median_source_agreement_fraction:.3f}",
                "disagreement_cells": f"{row.source_disagreement_flag_n:,}",
                "disagreement_fraction": f"{row.source_disagreement_flag_fraction:.3f}",
            }
        )

subcluster_evidence_rows_for_report = []
if not subcluster_df.empty:
    for row in subcluster_df.sort_values(["study", "lineage", "n_cells"], ascending=[True, True, False]).head(30).itertuples(index=False):
        subcluster_evidence_rows_for_report.append(
            {
                "study": row.study,
                "lineage": row.lineage,
                "cluster": row.cluster,
                "cells": f"{row.n_cells:,}",
                "chosen_label": row.chosen_label,
                "accepted": row.accepted,
                "score_margin": f"{row.score_margin:.3f}",
                "cluster_marker_assignment": row.cluster_marker_gene_assignment,
                "treg_key_any": f"{getattr(row, 'Treg_key_marker_any_fraction', 0.0):.3f}",
                "treg_key_bonus": f"{getattr(row, 'Treg_key_marker_bonus', 0.0):.3f}",
                "marker_set": row.marker_set,
                "marker_alert": row.marker_availability_alert,
            }
        )

lineage_panel_status_lookup = {}
if not lineage_panel_status_df.empty:
    for row in lineage_panel_status_df.itertuples(index=False):
        lineage_panel_status_lookup[(str(row.study), str(row.lineage))] = row

figure_lines = []
for study in summary_df["study"]:
    figure_lines.extend(
        [
            f"### {study}",
            "",
            f"![{study} final labels]({asset_link_root}/umap_{study}_annotation_label.png)",
            "",
            f"![{study} lineage and annotation reason]({asset_link_root}/umap_{study}_annotation_lineage_reason.png)",
            "",
            f"![{study} QC and confidence]({asset_link_root}/umap_{study}_annotation_qc_confidence.png)",
            "",
            f"![{study} source agreement and disagreement]({asset_link_root}/umap_{study}_annotation_source_disagreement.png)",
            "",
            f"![{study} marker expression UMAPs]({asset_link_root}/umap_{study}_annotation_marker_expression.png)",
            "",
            f"![{study} submitted-label marker dotplot]({asset_link_root}/dotplot_{study}_annotation_marker_dotplot.png)",
            "",
        ]
    )
    for lineage_name in ["B_lineage", "T_NK_lineage", "Myeloid_lineage"]:
        status_row = lineage_panel_status_lookup.get((str(study), lineage_name))
        if status_row is not None and status_row.status != "generated":
            figure_lines.extend(
                [
                    f"#### {study} {lineage_name} true subcluster UMAP",
                    "",
                    f"Skipped: {status_row.reason} (`n_cells={int(status_row.n_cells)}`).",
                    "",
                    f"Tables: `tables/{study}_{lineage_name}_true_subcluster_umap.tsv.gz`, `tables/{study}_{lineage_name}_subcluster_candidate_scores.tsv`.",
                    "",
                ]
            )
            continue
        figure_lines.extend(
            [
                f"#### {study} {lineage_name} true subcluster UMAP",
                "",
                f"![{study} {lineage_name} true subcluster labels]({asset_link_root}/umap_{study}_{lineage_name}_true_subcluster_label.png)",
                "",
                f"![{study} {lineage_name} true subcluster source labels]({asset_link_root}/umap_{study}_{lineage_name}_true_subcluster_source_labels.png)",
                "",
                f"![{study} {lineage_name} true subcluster QC]({asset_link_root}/umap_{study}_{lineage_name}_true_subcluster_qc.png)",
                "",
                f"![{study} {lineage_name} true subcluster marker scores]({asset_link_root}/umap_{study}_{lineage_name}_true_subcluster_marker_scores.png)",
                "",
                f"![{study} {lineage_name} true subcluster marker expression]({asset_link_root}/umap_{study}_{lineage_name}_true_subcluster_marker_expression.png)",
                "",
                f"![{study} {lineage_name} subcluster marker score heatmap]({asset_link_root}/subcluster_marker_score_heatmap_{study}_{lineage_name}.png)",
                "",
                f"![{study} {lineage_name} subcluster marker dotplot]({asset_link_root}/dotplot_{study}_{lineage_name}_true_subcluster_marker_dotplot.png)",
                "",
                f"Tables: `tables/{study}_{lineage_name}_true_subcluster_umap.tsv.gz`, `tables/{study}_{lineage_name}_subcluster_candidate_scores.tsv`.",
                "",
            ]
        )
figure_blocks = "\n".join(figure_lines)

# Language-specific report sections are centralized so EN/JA templates render
# from the same computed evidence without maintaining two divergent write paths.
def table_or_none(rows, columns, language):
    if rows:
        return markdown_table(rows, columns)
    if language == "ja":
        return "なし。"
    return "None."


def report_values(language):
    if language == "ja":
        summary_columns = ["study", "cells", "analysis_X_genes", "pre_hvg_genes", "counts_layer_genes", "labels", "parent_or_blood_fraction", "Blood Cell", "Doublet", "artifact_like", "median_confidence", "low_confidence", "source_disagreement", "invalid_labels"]
        interpretation_lines = []
        assessment_lines = []
        for row in summary_df.itertuples(index=False):
            interpretation_lines.append(
                f"- `{row.study}`: {row.n_cells:,} cells、analysis X/var {row.n_genes:,} genes、pre-HVG slot {row.pre_hvg_n_genes:,} genes、submitted label {row.n_labels} 種、"
                f"parent/Blood residual fraction {row.parent_or_blood_fraction:.3f}、median confidence {row.median_confidence:.3f}。"
            )
            assessment_lines.append(
                f"- 全体像: {row.n_cells:,} cells / analysis X/var {row.n_genes:,} genes / pre-HVG slot {row.pre_hvg_n_genes:,} genes。parent/Blood residual は {row.parent_or_blood_fraction:.3f}、"
                f"low-confidence は {row.low_confidence_n:,} cells、source disagreement flag は {row.source_disagreement_flag_n:,} cells ({row.source_disagreement_flag_fraction:.3f})。"
            )
            if row.invalid_labels:
                interpretation_lines.append(f"  - Invalid label があるため即時確認が必要: {row.invalid_labels}。")
            if row.low_confidence_n:
                interpretation_lines.append(f"  - {row.low_confidence_n:,} cells は low confidence。QC / confidence UMAP 上で局在を確認する。")
                assessment_lines.append("- 優先確認: low-confidence 領域が QC UMAP と source-disagreement UMAP で同じ場所に集まるかを確認する。")
            if row.doublet_n:
                interpretation_lines.append(f"  - {row.doublet_n:,} cells は `Doublet` として提出。mixed-lineage marker expression と scrublet support を確認する。")
            if row.blood_cell_n:
                interpretation_lines.append(f"  - {row.blood_cell_n:,} cells は `Blood Cell` として残存。これは filter-out ではなく、曖昧な細胞を公式 parent label で残したもの。")
                assessment_lines.append("- 優先確認: `Blood Cell` 残存が孤立 cluster なのか、複数 lineage に分散した曖昧領域なのかを UMAP で確認する。")
            study_alerts = marker_alert_df[marker_alert_df["study"].astype(str).eq(str(row.study))]
            if not study_alerts.empty:
                alert_labels = ", ".join(study_alerts["marker_set"].astype(str).tolist())
                interpretation_lines.append(f"  - Marker gene 欠損アラート: {alert_labels}。該当 marker set に依存する fine label は慎重に見る。")
                assessment_lines.append(f"- Marker gene 欠損: {alert_labels} は confidence cap 対象。該当 label は marker expression UMAP と dotplot で妥当性を確認する。")
        if not interpretation_lines:
            interpretation_lines.append("- データセット固有の解釈メモは生成されていない。")
        if not assessment_lines:
            assessment_lines.append("- 自動 assessment では大きな警告は検出されていない。UMAP と dotplot の目視確認は必要。")
        run_summary = "\n".join(
            [
                "- 実行単位: one dataset in, one annotated dataset out。",
                "- 実行経路: Codex skill `hipc-annotation` -> bundled helper `run_one.sh` -> annotation CLI -> validator -> report inspection。",
                "- 検証: submission row count、H5AD observation count、official label validity、H5AD/submission agreement、confidence column、report image link を確認する。",
                "- このレポートは workflow の再掲ではなく、このデータセットの marker 欠損、UMAP、label 構成、review concern を読むためのもの。",
            ]
        )
        file_block = "\n".join(
            [
                f"- Submission TSVs: `{output_root_display}/submissions/`",
                f"- cellxgene H5ADs: `{output_root_display}/cellxgene/`",
                f"- Marker availability table: `{output_root_display}/tables/marker_gene_availability.tsv`",
                f"- Marker availability alerts: `{output_root_display}/tables/marker_gene_availability_alerts.tsv`",
                f"- Subcluster evidence: `{output_root_display}/tables/lineage_subcluster_evidence.tsv.gz`",
                f"- Source disagreement summary: `{output_root_display}/tables/source_disagreement_summary.tsv`",
                f"- Diagnostics tables: `{output_root_display}/tables/`",
            ]
        )
        llm_review_prompt = "\n".join(
            [
                "このデータセット別 HIPC annotation report をレビューしてください。",
                "marker gene 欠損アラート、parent/Blood label の残存、low-confidence 領域、doublet call、marker-expression UMAP が submitted label を支持しているかに注目してください。",
                "README の固定 workflow は繰り返さず、このデータセット固有の懸念点と次に確認すべき点だけを返してください。",
            ]
        )
    else:
        summary_columns = ["study", "cells", "analysis_X_genes", "pre_hvg_genes", "counts_layer_genes", "labels", "parent_or_blood_fraction", "Blood Cell", "Doublet", "artifact_like", "median_confidence", "low_confidence", "source_disagreement", "invalid_labels"]
        interpretation_lines = []
        assessment_lines = []
        for row in summary_df.itertuples(index=False):
            interpretation_lines.append(
                f"- `{row.study}`: {row.n_cells:,} cells, {row.n_genes:,} analysis X/var genes, {row.pre_hvg_n_genes:,} pre-HVG slot genes, {row.n_labels} submitted labels, "
                f"parent/Blood residual fraction {row.parent_or_blood_fraction:.3f}, median confidence {row.median_confidence:.3f}."
            )
            assessment_lines.append(
                f"- Overall: {row.n_cells:,} cells / {row.n_genes:,} analysis X/var genes / {row.pre_hvg_n_genes:,} pre-HVG slot genes. Parent/Blood residual fraction is {row.parent_or_blood_fraction:.3f}; "
                f"low-confidence cells are {row.low_confidence_n:,}; source-disagreement flags affect {row.source_disagreement_flag_n:,} cells ({row.source_disagreement_flag_fraction:.3f})."
            )
            if row.invalid_labels:
                interpretation_lines.append(f"  - Invalid labels require immediate review: {row.invalid_labels}.")
            if row.low_confidence_n:
                interpretation_lines.append(f"  - {row.low_confidence_n:,} cells have low confidence and should be inspected on QC/confidence UMAPs.")
                assessment_lines.append("- Review priority: check whether low-confidence regions co-localize with QC artifacts or source-disagreement regions on UMAP.")
            if row.doublet_n:
                interpretation_lines.append(f"  - {row.doublet_n:,} cells are submitted as `Doublet`; inspect mixed-lineage marker expression before final submission.")
            if row.blood_cell_n:
                interpretation_lines.append(f"  - {row.blood_cell_n:,} cells remain `Blood Cell`; these are residual ambiguous cells rather than filtered cells.")
                assessment_lines.append("- Review priority: inspect whether residual `Blood Cell` cells form isolated clusters or dispersed ambiguous zones across lineages.")
            study_alerts = marker_alert_df[marker_alert_df["study"].astype(str).eq(str(row.study))]
            if not study_alerts.empty:
                alert_labels = ", ".join(study_alerts["marker_set"].astype(str).tolist())
                interpretation_lines.append(f"  - Marker availability alerts are present for: {alert_labels}. Fine labels relying on these marker sets should be treated cautiously.")
                assessment_lines.append(f"- Marker availability: {alert_labels} are confidence-capped; validate affected labels on marker-expression UMAPs and dotplots.")
        if not interpretation_lines:
            interpretation_lines.append("- No dataset-specific interpretation notes were generated.")
        if not assessment_lines:
            assessment_lines.append("- No major automated assessment warnings were detected, but UMAP and dotplot review is still required.")
        run_summary = "\n".join(
            [
                "- Execution unit: one dataset in, one annotated dataset out.",
                "- Execution path: Codex skill `hipc-annotation` -> bundled helper `run_one.sh` -> annotation CLI -> validator -> report inspection.",
                "- Validation checks: submission row count, H5AD observation count, official label validity, H5AD/submission agreement, confidence column, and report image links.",
                "- This report is for dataset-specific marker availability, UMAPs, label composition, and review concerns rather than repeating the fixed workflow.",
            ]
        )
        file_block = "\n".join(
            [
                f"- Submission TSVs: `{output_root_display}/submissions/`",
                f"- cellxgene H5ADs: `{output_root_display}/cellxgene/`",
                f"- Marker availability table: `{output_root_display}/tables/marker_gene_availability.tsv`",
                f"- Marker availability alerts: `{output_root_display}/tables/marker_gene_availability_alerts.tsv`",
                f"- Subcluster evidence: `{output_root_display}/tables/lineage_subcluster_evidence.tsv.gz`",
                f"- Source disagreement summary: `{output_root_display}/tables/source_disagreement_summary.tsv`",
                f"- Diagnostics tables: `{output_root_display}/tables/`",
            ]
        )
        llm_review_prompt = "\n".join(
            [
                "Review this dataset-specific HIPC annotation report.",
                "Focus on marker availability alerts, residual parent/Blood labels, low-confidence regions, doublet calls, and whether marker-expression UMAPs support the submitted labels.",
                "Do not restate the fixed pipeline workflow from README; provide dataset-specific concerns and suggested next checks only.",
            ]
        )
    return {
        "REPORT_TITLE": report_title,
        "REPORT_UPDATED": report_updated,
        "STUDY_SUMMARY_TABLE": table_or_none(summary_rows, summary_columns, language),
        "RUN_SUMMARY": run_summary,
        "DATASET_ASSESSMENT": "\n".join(assessment_lines),
        "INTERPRETATION_NOTES": "\n".join(interpretation_lines),
        "MARKER_ALERTS": table_or_none(marker_alert_rows, ["study", "marker_set", "alert", "present_fraction", "missing_critical_markers", "missing_genes"], language),
        "SOURCE_DISAGREEMENT": table_or_none(source_disagreement_rows_for_report, ["study", "predicted_cell_type", "cells", "median_source_agreement", "disagreement_cells", "disagreement_fraction"], language),
        "REVIEW_CONCERNS": table_or_none(concern_rows_for_report, ["study", "concern", "cells"], language),
        "LABEL_COMPOSITION": table_or_none(label_rows_for_report, ["study", "predicted_cell_type", "cells"], language),
        "SUBCLUSTER_EVIDENCE_TABLE": table_or_none(subcluster_evidence_rows_for_report, ["study", "lineage", "cluster", "cells", "chosen_label", "accepted", "score_margin", "cluster_marker_assignment", "treg_key_any", "treg_key_bonus", "marker_set", "marker_alert"], language),
        "FIGURE_BLOCKS": figure_blocks,
        "FILE_BLOCK": file_block,
        "LLM_REVIEW_PROMPT": llm_review_prompt,
    }

for language in requested_languages:
    template_path = template_dir / f"report_dataset_{language}.md"
    if not template_path.exists():
        template_path = template_dir / "report_dataset_en.md"
    report_text = render_template(template_path, report_values(language))
    (report_dir / f"report_{language}.md").write_text(report_text + "\n", encoding="utf-8")

print(summary_df.to_string(index=False))
print(f"Wrote independent outputs to {output_root}")
