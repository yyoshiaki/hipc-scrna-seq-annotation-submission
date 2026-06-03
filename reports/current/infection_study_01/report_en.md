# infection_study_01 Annotation Report

Updated: 2026-06-02 22:28:28 EDT

## Dataset-Specific Assessment

The current annotation is intentionally conservative. Most major PBMC lineages are resolved, but the residual parent-label burden is still visible in T-lineage cells, so CD4/T subtype calls should be reviewed in cellxgene before treating this dataset as final-final.

## Key Metrics

| Metric | Value |
| --- | --- |
| Cells | 54,924 |
| Genes in H5AD var | 33,538 |
| Submitted labels | 22 |
| Parent or Blood fallback cells | 4,827 (8.8%) |
| Doublet calls | 1,278 |
| Median confidence | 0.92 |
| CD4 T Effector Memory calls | 1,159 |
| Generic T Cell calls | 3,672 |
| Generic B Cell calls | 29 |


## Label Composition

Top submitted labels for this dataset:

| label | cells | fraction |
| --- | --- | --- |
| Classical Monocyte | 16,771 | 30.5% |
| CD8 Cytotoxic / T Effector Memory | 9,299 | 16.9% |
| NK Cell | 7,851 | 14.3% |
| Naive B Cell | 4,157 | 7.6% |
| T Cell | 3,672 | 6.7% |
| CD4 Naive / T Central Memory | 2,779 | 5.1% |
| Memory B Cell | 2,165 | 3.9% |
| Non-Classical Monocyte | 2,122 | 3.9% |
| Platelet | 1,391 | 2.5% |
| Doublet | 1,278 | 2.3% |
| CD4 T Effector Memory | 1,159 | 2.1% |
| Blood Cell | 679 | 1.2% |

## Cluster Consensus Review

The table below shows the largest accepted cluster-level decisions. `source_fraction` is the within-cluster fraction supporting the selected label across reference/evidence sources, and `marker_pct` is the cluster-level marker support for the chosen label. High values in both columns are stronger evidence than either value alone.

| lineage | cluster | cells | chosen_label | margin | source_fraction | marker_pct | reason |
| --- | --- | --- | --- | --- | --- | --- | --- |
| T/NK | T_NK_lineage:0 | 1,627 | CD4 Naive / T Central Memory | 1.09 | 0.63 | 0.96 | cluster_consensus_marker_source_support |
| T/NK | T_NK_lineage:1 | 1,482 | NK Cell | 0.67 | 0.48 | 0.89 | cluster_consensus_marker_source_support |
| Myeloid/DC | Myeloid_lineage:0 | 1,455 | Non-Classical Monocyte | 2.09 | 0.66 | 0.98 | cluster_consensus_marker_source_support |
| Myeloid/DC | Myeloid_lineage:1 | 1,411 | Classical Monocyte | 1.15 | 0.70 | 0.88 | cluster_consensus_marker_source_support |
| Myeloid/DC | Myeloid_lineage:2 | 1,354 | Classical Monocyte | 1.12 | 0.66 | 0.82 | cluster_consensus_marker_source_support |
| Artifact/Other | leiden:16 | 1,335 | Platelet | 2.96 | 0.84 | 0.99 | cluster_consensus_marker_source_support |
| T/NK | T_NK_lineage:4 | 1,323 | CD8 Cytotoxic / T Effector Memory | 1.79 | 0.55 | 0.94 | cluster_consensus_marker_source_support |
| Myeloid/DC | Myeloid_lineage:3 | 1,295 | Classical Monocyte | 0.91 | 0.68 | 0.75 | cluster_consensus_marker_source_support |
| T/NK | T_NK_lineage:2 | 1,290 | NK Cell | 1.21 | 0.62 | 0.94 | cluster_consensus_marker_source_support |
| Myeloid/DC | Myeloid_lineage:4 | 1,199 | Classical Monocyte | 1.47 | 0.68 | 0.90 | cluster_consensus_marker_source_support |
| Myeloid/DC | Myeloid_lineage:5 | 1,196 | Classical Monocyte | 1.29 | 0.71 | 0.86 | cluster_consensus_marker_source_support |
| Myeloid/DC | Myeloid_lineage:6 | 1,187 | Classical Monocyte | 1.22 | 0.68 | 0.80 | cluster_consensus_marker_source_support |

## Conservative Fallbacks

Fallback clusters are not failures by themselves. They mark clusters where the best fine label did not have enough margin, source support, marker support, or key-marker support to safely replace the parent/fallback label.

| lineage | cluster | cells | chosen_label | best_candidate | margin | reason |
| --- | --- | --- | --- | --- | --- | --- |
| T/NK | T_NK_lineage:3 | 1,317 | T Cell | CD4 T Effector Memory | 0.23 | cluster_parent_insufficient_consensus |
| T/NK | T_NK_lineage:9 | 847 | T Cell | CD8 Cytotoxic / T Effector Memory | 0.00 | cluster_parent_insufficient_consensus |
| T/NK | T_NK_lineage:14 | 720 | T Cell | CD4 T Effector Memory | 0.14 | cluster_parent_insufficient_consensus |
| T/NK | T_NK_lineage:25 | 469 | T Cell | CD4 T Effector Memory | 0.11 | cluster_parent_insufficient_consensus |
| Myeloid/DC | Myeloid_lineage:18 | 413 | Myeloid Cell | Non-Classical Monocyte | 0.00 | cluster_parent_insufficient_consensus |
| T/NK | T_NK_lineage:32 | 273 | T Cell | NK Cell | 0.00 | cluster_parent_insufficient_consensus |
| T/NK | T_NK_lineage:34 | 253 | T Cell | CD4 T Effector Memory | 0.45 | cluster_parent_insufficient_consensus |
| Myeloid/DC | Myeloid_lineage:32 | 34 | Myeloid Cell | Conventional DC 2 | 0.01 | cluster_parent_insufficient_consensus |
| Artifact/Other | leiden:23 | 32 | Blood Cell | RBC | 0.08 | cluster_parent_insufficient_consensus |
| B | B_lineage:26 | 28 | B Cell | Plasmablast | 0.08 | cluster_parent_insufficient_consensus |
| Artifact/Other | leiden:6 | 19 | Blood Cell | RBC | 0.36 | cluster_parent_insufficient_consensus |
| Artifact/Other | leiden:12 | 17 | Blood Cell | RBC | 1.61 | cluster_parent_insufficient_consensus |

## Source Support Snapshot

This table is intended for quick review of where CellTypist, Azimuth, Pan-human Azimuth, and lineage-scoped scRefMapping agree or disagree in large clusters.

| cluster | cells | chosen_label | CellTypist | Azimuth_l2 | PanHuman | scRefMapping |
| --- | --- | --- | --- | --- | --- | --- |
| T_NK_lineage:0 | 1,627 | CD4 Naive / T Central Memory | CD4 Naive / T Central Memory:1331; CD8 Naive / T Central Memory:268; Treg:15; CD8 Cytotoxic /... | CD4 Naive / T Central Memory:1274; CD8 Naive / T Central Memory:318; Treg:18; CD4 T Effector ... | CD4 Naive / T Central Memory:1188; CD8 Naive / T Central Memory:321; CD4 T Effector Memory:59... | CD4 Naive / T Central Memory:1391; not_available:204; Treg:27; CD4 T Effector Memory:5 |
| T_NK_lineage:1 | 1,482 | NK Cell | NK Cell:1026; CD8 Cytotoxic / T Effector Memory:452; ydT Cell:3; Blood Cell:1 | NK Cell:987; ydT Cell:267; CD8 Cytotoxic / T Effector Memory:224; CD4 T Effector Memory:4 | NK Cell:786; CD8 Cytotoxic / T Effector Memory:630; Blood Cell:63; Lymphoid Cell:2 | not_available:1482 |
| Myeloid_lineage:0 | 1,455 | Non-Classical Monocyte | Non-Classical Monocyte:1413; Classical Monocyte:41; Blood Cell:1 | Non-Classical Monocyte:1426; Classical Monocyte:29 | Non-Classical Monocyte:1067; Intermediate Monocyte:327; Blood Cell:53; Classical Monocyte:5 | not_available:1455 |
| Myeloid_lineage:1 | 1,411 | Classical Monocyte | Classical Monocyte:1393; Non-Classical Monocyte:17; Blood Cell:1 | Classical Monocyte:1408; Non-Classical Monocyte:3 | Classical Monocyte:1264; Blood Cell:103; Neutrophil:26; Intermediate Monocyte:12 | not_available:1411 |
| Myeloid_lineage:2 | 1,354 | Classical Monocyte | Classical Monocyte:1293; Non-Classical Monocyte:61 | Classical Monocyte:1322; Non-Classical Monocyte:32 | Classical Monocyte:979; Intermediate Monocyte:292; Blood Cell:61; Conventional DC 2:18 | not_available:1354 |
| leiden:16 | 1,335 | Platelet | Platelet:1258; CD4 Naive / T Central Memory:35; Classical Monocyte:34; Blood Cell:3 | Platelet:1324; CD4 Naive / T Central Memory:6; Classical Monocyte:5 | Platelet:1324; Blood Cell:11 | not_available:1293; CD4 Naive / T Central Memory:36; CD4 T Effector Memory:6 |
| T_NK_lineage:4 | 1,323 | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory:1305; NK Cell:17; Treg:1 | CD8 Cytotoxic / T Effector Memory:1227; CD8 Naive / T Central Memory:35; NK Cell:34; CD4 T Ef... | CD8 Cytotoxic / T Effector Memory:1286; NK Cell:24; Blood Cell:8; Lymphoid Cell:3 | not_available:1322; CD4 T Effector Memory:1 |
| T_NK_lineage:3 | 1,317 | T Cell | CD4 T Effector Memory:822; CD4 Naive / T Central Memory:359; CD8 Cytotoxic / T Effector Memor... | CD4 Naive / T Central Memory:961; CD8 Naive / T Central Memory:231; CD4 T Effector Memory:90;... | CD4 T Effector Memory:1181; CD8 Cytotoxic / T Effector Memory:37; Treg:37; Blood Cell:33 | CD4 Naive / T Central Memory:940; not_available:223; CD4 T Effector Memory:145; Treg:9 |
| Myeloid_lineage:3 | 1,295 | Classical Monocyte | Classical Monocyte:1257; Non-Classical Monocyte:35; Blood Cell:2; Conventional DC 2:1 | Classical Monocyte:1275; Non-Classical Monocyte:18; Conventional DC 2:2 | Classical Monocyte:1084; Blood Cell:100; Conventional DC 2:56; Intermediate Monocyte:53 | not_available:1295 |
| T_NK_lineage:2 | 1,290 | NK Cell | NK Cell:806; CD8 Cytotoxic / T Effector Memory:480; ydT Cell:4 | NK Cell:1247; CD8 Cytotoxic / T Effector Memory:21; ydT Cell:20; CD4 T Effector Memory:1 | NK Cell:1149; CD8 Cytotoxic / T Effector Memory:116; Blood Cell:24; Lymphoid Cell:1 | not_available:1290 |

## Review Priorities

- Inspect residual parent or Blood fallback populations in cellxgene, especially if they are spatially separated on UMAP.
- Check marker expression for labels that are biologically narrow or sensitive to missing genes.
- Treat doublet labels as submitted annotations, not filtered cells.
- For this dataset, the main review target is: The current annotation is intentionally conservative. Most major PBMC lineages are resolved, but the residual parent-label burden is still visible in T-lineage cells, so CD4/T subtype calls should be reviewed in cellxgene before treating this dataset as final-final.

## Output Files

- Per-dataset report: `reports/current/infection_study_01/report_en.md`
- Japanese report: `reports/current/infection_study_01/report_ja.md`
- Label counts: `reports/current/infection_study_01/tables/label_counts.tsv`
- Cluster decisions: `reports/current/infection_study_01/tables/cluster_consensus_decisions.tsv`
- Local H5AD output: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/final_annotations/current_cluster_consensus/cellxgene/infection_study_01.final_annotation.cluster_consensus.cxg.h5ad`
- Local submission TSV: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/final_annotations/current_cluster_consensus/submissions/infection_study_01_annotation.tsv`
