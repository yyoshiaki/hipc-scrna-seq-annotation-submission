# infection_study_04 Annotation Report

Updated: 2026-06-02 22:28:28 EDT

## Dataset-Specific Assessment

This dataset still contains moderate parent-label residuals in both B and T compartments. The cluster consensus prevents over-confident fine labels where reference sources disagree, but B-memory/naive and T-state boundaries remain the main review targets.

## Key Metrics

| Metric | Value |
| --- | --- |
| Cells | 43,767 |
| Genes in H5AD var | 26,361 |
| Submitted labels | 23 |
| Parent or Blood fallback cells | 3,516 (8.0%) |
| Doublet calls | 132 |
| Median confidence | 0.92 |
| CD4 T Effector Memory calls | 53 |
| Generic T Cell calls | 458 |
| Generic B Cell calls | 450 |


## Label Composition

Top submitted labels for this dataset:

| label | cells | fraction |
| --- | --- | --- |
| Classical Monocyte | 10,292 | 23.5% |
| CD4 Naive / T Central Memory | 7,960 | 18.2% |
| NK Cell | 6,813 | 15.6% |
| CD8 Cytotoxic / T Effector Memory | 5,780 | 13.2% |
| Blood Cell | 2,597 | 5.9% |
| Plasma Cell | 2,323 | 5.3% |
| Naive B Cell | 1,540 | 3.5% |
| Memory B Cell | 1,366 | 3.1% |
| Non-Classical Monocyte | 1,240 | 2.8% |
| Plasmablast | 571 | 1.3% |
| Conventional DC 2 | 547 | 1.2% |
| MAIT Cell | 481 | 1.1% |

## Cluster Consensus Review

The table below shows the largest accepted cluster-level decisions. `source_fraction` is the within-cluster fraction supporting the selected label across reference/evidence sources, and `marker_pct` is the cluster-level marker support for the chosen label. High values in both columns are stronger evidence than either value alone.

| lineage | cluster | cells | chosen_label | margin | source_fraction | marker_pct | reason |
| --- | --- | --- | --- | --- | --- | --- | --- |
| T/NK | T_NK_lineage:0 | 1,748 | NK Cell | 1.65 | 0.69 | 0.94 | cluster_consensus_marker_source_support |
| T/NK | T_NK_lineage:3 | 1,482 | CD4 Naive / T Central Memory | 0.83 | 0.63 | 0.89 | cluster_consensus_marker_source_support |
| T/NK | T_NK_lineage:2 | 1,423 | CD8 Cytotoxic / T Effector Memory | 1.59 | 0.49 | 0.90 | cluster_consensus_marker_source_support |
| T/NK | T_NK_lineage:4 | 1,418 | CD4 Naive / T Central Memory | 1.36 | 0.66 | 0.94 | cluster_consensus_marker_source_support |
| T/NK | T_NK_lineage:1 | 1,388 | NK Cell | 1.20 | 0.56 | 0.91 | cluster_consensus_marker_source_support |
| T/NK | T_NK_lineage:5 | 1,262 | NK Cell | 1.35 | 0.59 | 0.94 | cluster_consensus_marker_source_support |
| Myeloid/DC | Myeloid_lineage:0 | 1,194 | Classical Monocyte | 1.10 | 0.66 | 0.78 | cluster_consensus_marker_source_support |
| T/NK | T_NK_lineage:8 | 1,186 | CD4 Naive / T Central Memory | 1.00 | 0.55 | 0.90 | cluster_consensus_marker_source_support |
| T/NK | T_NK_lineage:6 | 1,111 | NK Cell | 0.31 | 0.35 | 0.85 | cluster_consensus_marker_source_support |
| T/NK | T_NK_lineage:7 | 1,089 | CD8 Cytotoxic / T Effector Memory | 1.17 | 0.40 | 0.88 | cluster_consensus_marker_source_support |
| Myeloid/DC | Myeloid_lineage:2 | 1,050 | Classical Monocyte | 1.50 | 0.66 | 0.88 | cluster_consensus_marker_source_support |
| Myeloid/DC | Myeloid_lineage:4 | 1,030 | Classical Monocyte | 1.54 | 0.69 | 0.89 | cluster_consensus_marker_source_support |

## Conservative Fallbacks

Fallback clusters are not failures by themselves. They mark clusters where the best fine label did not have enough margin, source support, marker support, or key-marker support to safely replace the parent/fallback label.

| lineage | cluster | cells | chosen_label | best_candidate | margin | reason |
| --- | --- | --- | --- | --- | --- | --- |
| Artifact/Other | leiden:15 | 449 | Blood Cell | RBC | 0.23 | cluster_parent_insufficient_consensus |
| B | B_lineage:6 | 322 | B Cell | Plasma Cell | 0.03 | cluster_parent_insufficient_consensus |
| T/NK | T_NK_lineage:24 | 241 | T Cell | CD4 Naive / T Central Memory | 0.07 | cluster_parent_insufficient_consensus |
| T/NK | T_NK_lineage:23 | 170 | T Cell | CD4 Naive / T Central Memory | 0.22 | cluster_parent_insufficient_consensus |
| B | B_lineage:16 | 96 | B Cell | Naive B Cell | 0.04 | cluster_parent_insufficient_consensus |
| Artifact/Other | leiden:22 | 95 | Blood Cell | HSC | 0.07 | cluster_parent_insufficient_consensus |
| Artifact/Other | leiden:33 | 81 | Blood Cell | RBC | 0.43 | cluster_parent_insufficient_consensus |
| Artifact/Other | leiden:4 | 66 | Blood Cell | RBC | 0.17 | cluster_parent_insufficient_consensus |
| Artifact/Other | leiden:17 | 60 | Blood Cell | RBC | 0.15 | cluster_parent_insufficient_consensus |
| T/NK | T_NK_lineage:27 | 38 | T Cell | NK Cell | 0.06 | cluster_parent_insufficient_consensus |
| Artifact/Other | leiden:0 | 37 | Blood Cell | RBC | 0.15 | cluster_parent_insufficient_consensus |
| B | B_lineage:21 | 32 | B Cell | Plasma Cell | 0.04 | cluster_parent_insufficient_consensus |

## Source Support Snapshot

This table is intended for quick review of where CellTypist, Azimuth, Pan-human Azimuth, and lineage-scoped scRefMapping agree or disagree in large clusters.

| cluster | cells | chosen_label | CellTypist | Azimuth_l2 | PanHuman | scRefMapping |
| --- | --- | --- | --- | --- | --- | --- |
| T_NK_lineage:0 | 1,748 | NK Cell | NK Cell:1646; CD8 Cytotoxic / T Effector Memory:50; CD4 Naive / T Central Memory:41; Blood Ce... | NK Cell:1712; CD8 Cytotoxic / T Effector Memory:34; Lymphoid Cell:1; ydT Cell:1 | NK Cell:1700; Blood Cell:35; Lymphoid Cell:10; CD8 Cytotoxic / T Effector Memory:3 | not_available:1748 |
| T_NK_lineage:3 | 1,482 | CD4 Naive / T Central Memory | CD4 Naive / T Central Memory:1361; CD8 Naive / T Central Memory:93; Treg:10; CD8 Cytotoxic / ... | CD4 Naive / T Central Memory:963; CD8 Naive / T Central Memory:472; CD8 Cytotoxic / T Effecto... | CD4 Naive / T Central Memory:1058; CD8 Naive / T Central Memory:237; Blood Cell:99; Treg:30 | CD4 Naive / T Central Memory:1074; not_available:378; Treg:16; CD4 T Effector Memory:14 |
| T_NK_lineage:2 | 1,423 | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory:1190; NK Cell:118; CD4 Naive / T Central Memory:75; Treg:16 | CD8 Cytotoxic / T Effector Memory:1258; NK Cell:68; ydT Cell:65; CD4 T Effector Memory:10 | CD8 Cytotoxic / T Effector Memory:1169; NK Cell:112; Blood Cell:94; ydT Cell:17 | not_available:1409; CD4 T Effector Memory:12; CD4 Naive / T Central Memory:2 |
| T_NK_lineage:4 | 1,418 | CD4 Naive / T Central Memory | CD4 Naive / T Central Memory:1352; Treg:32; CD8 Naive / T Central Memory:14; CD4 T Effector M... | CD4 Naive / T Central Memory:1300; CD8 Naive / T Central Memory:78; Treg:20; CD8 Cytotoxic / ... | CD4 Naive / T Central Memory:969; CD4 T Effector Memory:268; Treg:59; Blood Cell:55 | CD4 Naive / T Central Memory:1236; not_available:136; CD4 T Effector Memory:26; Treg:20 |
| T_NK_lineage:1 | 1,388 | NK Cell | NK Cell:898; CD8 Cytotoxic / T Effector Memory:241; CD4 Naive / T Central Memory:226; Treg:11 | NK Cell:1035; CD8 Cytotoxic / T Effector Memory:297; ydT Cell:45; CD4 Naive / T Central Memory:6 | NK Cell:1119; CD8 Cytotoxic / T Effector Memory:124; Blood Cell:115; ydT Cell:15 | not_available:1375; CD4 T Effector Memory:12; CD4 Naive / T Central Memory:1 |
| T_NK_lineage:5 | 1,262 | NK Cell | NK Cell:781; CD8 Cytotoxic / T Effector Memory:404; CD4 Naive / T Central Memory:62; Treg:8 | NK Cell:1087; CD8 Cytotoxic / T Effector Memory:157; ydT Cell:16; CD8 T Cell (ab):1 | NK Cell:1105; CD8 Cytotoxic / T Effector Memory:86; Blood Cell:58; ydT Cell:7 | not_available:1262 |
| Myeloid_lineage:0 | 1,194 | Classical Monocyte | Classical Monocyte:1080; Non-Classical Monocyte:60; CD4 Naive / T Central Memory:41; Myeloid ... | Classical Monocyte:1153; Non-Classical Monocyte:37; Conventional DC 2:3; RBC:1 | Classical Monocyte:1006; Blood Cell:81; Intermediate Monocyte:70; Non-Classical Monocyte:17 | not_available:1194 |
| T_NK_lineage:8 | 1,186 | CD4 Naive / T Central Memory | CD4 Naive / T Central Memory:1066; Treg:64; CD4 T Effector Memory:24; CD8 Cytotoxic / T Effec... | CD4 Naive / T Central Memory:1066; CD8 Cytotoxic / T Effector Memory:43; Treg:43; CD8 Naive /... | CD4 T Effector Memory:523; CD4 Naive / T Central Memory:369; Blood Cell:123; Treg:103 | CD4 Naive / T Central Memory:905; not_available:129; CD4 T Effector Memory:109; Treg:43 |
| T_NK_lineage:6 | 1,111 | NK Cell | NK Cell:488; CD8 Cytotoxic / T Effector Memory:411; CD4 Naive / T Central Memory:182; Treg:16 | CD8 Cytotoxic / T Effector Memory:480; NK Cell:458; CD4 Naive / T Central Memory:89; ydT Cell:75 | NK Cell:504; CD8 Cytotoxic / T Effector Memory:346; Blood Cell:207; ydT Cell:29 | not_available:1099; CD4 T Effector Memory:7; CD4 Naive / T Central Memory:5 |
| T_NK_lineage:7 | 1,089 | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory:553; CD4 Naive / T Central Memory:344; NK Cell:137; Blood C... | CD8 Cytotoxic / T Effector Memory:898; NK Cell:55; CD4 Naive / T Central Memory:49; ydT Cell:35 | CD8 Cytotoxic / T Effector Memory:729; Blood Cell:181; NK Cell:87; CD4 Naive / T Central Memo... | not_available:1005; CD4 T Effector Memory:68; CD4 Naive / T Central Memory:16 |

## Review Priorities

- Inspect residual parent or Blood fallback populations in cellxgene, especially if they are spatially separated on UMAP.
- Check marker expression for labels that are biologically narrow or sensitive to missing genes.
- Treat doublet labels as submitted annotations, not filtered cells.
- For this dataset, the main review target is: This dataset still contains moderate parent-label residuals in both B and T compartments. The cluster consensus prevents over-confident fine labels where reference sources disagree, but B-memory/naive and T-state boundaries remain the main review targets.

## Output Files

- Per-dataset report: `reports/current/infection_study_04/report_en.md`
- Japanese report: `reports/current/infection_study_04/report_ja.md`
- Label counts: `reports/current/infection_study_04/tables/label_counts.tsv`
- Cluster decisions: `reports/current/infection_study_04/tables/cluster_consensus_decisions.tsv`
- Local H5AD output: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/final_annotations/current_cluster_consensus/cellxgene/infection_study_04.final_annotation.cluster_consensus.cxg.h5ad`
- Local submission TSV: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/final_annotations/current_cluster_consensus/submissions/infection_study_04_annotation.tsv`
