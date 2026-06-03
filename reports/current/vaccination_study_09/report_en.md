# vaccination_study_09 Annotation Report

Updated: 2026-06-02 22:28:28 EDT

## Dataset-Specific Assessment

This large dataset has few generic T Cell residuals but retains a large Blood Cell fallback group. B-cell labels look comparatively stable, while effector-memory T labels are intentionally gated and remain limited to strongly supported subclusters.

## Key Metrics

| Metric | Value |
| --- | --- |
| Cells | 139,960 |
| Genes in H5AD var | 19,141 |
| Submitted labels | 20 |
| Parent or Blood fallback cells | 9,999 (7.1%) |
| Doublet calls | 579 |
| Median confidence | 0.92 |
| CD4 T Effector Memory calls | 865 |
| Generic T Cell calls | 1 |
| Generic B Cell calls | 0 |


## Label Composition

Top submitted labels for this dataset:

| label | cells | fraction |
| --- | --- | --- |
| CD4 Naive / T Central Memory | 53,666 | 38.3% |
| Classical Monocyte | 18,932 | 13.5% |
| CD8 Cytotoxic / T Effector Memory | 10,915 | 7.8% |
| Naive B Cell | 10,783 | 7.7% |
| Blood Cell | 9,998 | 7.1% |
| CD8 Naive / T Central Memory | 9,693 | 6.9% |
| NK Cell | 9,004 | 6.4% |
| Non-Classical Monocyte | 4,238 | 3.0% |
| Memory B Cell | 3,849 | 2.8% |
| MAIT Cell | 3,420 | 2.4% |
| Conventional DC 2 | 1,496 | 1.1% |
| Treg | 1,195 | 0.9% |

## Cluster Consensus Review

The table below shows the largest accepted cluster-level decisions. `source_fraction` is the within-cluster fraction supporting the selected label across reference/evidence sources, and `marker_pct` is the cluster-level marker support for the chosen label. High values in both columns are stronger evidence than either value alone.

| lineage | cluster | cells | chosen_label | margin | source_fraction | marker_pct | reason |
| --- | --- | --- | --- | --- | --- | --- | --- |
| T/NK | T_NK_lineage:0 | 7,308 | NK Cell | 1.47 | 0.65 | 0.97 | cluster_consensus_marker_source_support |
| T/NK | T_NK_lineage:1 | 6,935 | CD4 Naive / T Central Memory | 0.88 | 0.56 | 0.83 | cluster_consensus_marker_source_support |
| T/NK | T_NK_lineage:3 | 6,576 | CD4 Naive / T Central Memory | 1.03 | 0.59 | 0.78 | cluster_consensus_marker_source_support |
| T/NK | T_NK_lineage:2 | 6,487 | CD8 Cytotoxic / T Effector Memory | 0.81 | 0.38 | 0.94 | cluster_consensus_marker_source_support |
| T/NK | T_NK_lineage:4 | 6,070 | CD4 Naive / T Central Memory | 0.55 | 0.50 | 0.78 | cluster_consensus_marker_source_support |
| T/NK | T_NK_lineage:5 | 5,379 | CD4 Naive / T Central Memory | 0.91 | 0.51 | 0.71 | cluster_consensus_marker_source_support |
| T/NK | T_NK_lineage:6 | 5,179 | CD8 Naive / T Central Memory | 0.09 | 0.30 | 0.86 | cluster_consensus_marker_source_support |
| T/NK | T_NK_lineage:7 | 4,788 | CD4 Naive / T Central Memory | 0.97 | 0.58 | 0.79 | cluster_consensus_marker_source_support |
| T/NK | T_NK_lineage:8 | 4,521 | CD8 Naive / T Central Memory | 0.34 | 0.33 | 0.85 | cluster_consensus_marker_source_support |
| T/NK | T_NK_lineage:9 | 3,668 | CD8 Cytotoxic / T Effector Memory | 0.94 | 0.35 | 0.90 | cluster_consensus_marker_source_support |
| T/NK | T_NK_lineage:11 | 3,560 | CD4 Naive / T Central Memory | 0.46 | 0.43 | 0.81 | cluster_consensus_marker_source_support |
| T/NK | T_NK_lineage:10 | 3,500 | MAIT Cell | 0.17 | 0.35 | 0.67 | cluster_consensus_marker_source_support |

## Conservative Fallbacks

Fallback clusters are not failures by themselves. They mark clusters where the best fine label did not have enough margin, source support, marker support, or key-marker support to safely replace the parent/fallback label.

| lineage | cluster | cells | chosen_label | best_candidate | margin | reason |
| --- | --- | --- | --- | --- | --- | --- |
| Artifact/Other | leiden:8 | 5,722 | Blood Cell | RBC | 0.51 | cluster_parent_insufficient_consensus |
| Artifact/Other | leiden:2 | 1,091 | Blood Cell | RBC | 0.38 | cluster_parent_insufficient_consensus |
| Artifact/Other | leiden:9 | 293 | Blood Cell | RBC | 0.47 | cluster_parent_insufficient_consensus |
| Artifact/Other | leiden:6 | 192 | Blood Cell | RBC | 0.61 | cluster_parent_insufficient_consensus |
| Artifact/Other | leiden:4 | 175 | Blood Cell | RBC | 0.03 | cluster_parent_insufficient_consensus |
| Artifact/Other | leiden:7 | 102 | Blood Cell | RBC | 0.46 | cluster_parent_insufficient_consensus |
| Artifact/Other | leiden:14 | 94 | Blood Cell | RBC | 0.45 | cluster_parent_insufficient_consensus |
| Artifact/Other | leiden:10 | 93 | Blood Cell | RBC | 0.12 | cluster_parent_insufficient_consensus |
| Artifact/Other | leiden:1 | 48 | Blood Cell | HSC | 0.22 | cluster_parent_insufficient_consensus |
| Artifact/Other | leiden:13 | 34 | Blood Cell | RBC | 0.15 | cluster_parent_insufficient_consensus |
| Artifact/Other | leiden:11 | 33 | Blood Cell | Platelet | 0.36 | cluster_parent_insufficient_consensus |
| Artifact/Other | leiden:26 | 13 | Blood Cell | RBC | 0.09 | cluster_parent_insufficient_consensus |

## Source Support Snapshot

This table is intended for quick review of where CellTypist, Azimuth, Pan-human Azimuth, and lineage-scoped scRefMapping agree or disagree in large clusters.

| cluster | cells | chosen_label | CellTypist | Azimuth_l2 | PanHuman | scRefMapping |
| --- | --- | --- | --- | --- | --- | --- |
| T_NK_lineage:0 | 7,308 | NK Cell | NK Cell:7149; Blood Cell:60; CD4 Naive / T Central Memory:46; CD8 Cytotoxic / T Effector Memo... | NK Cell:5414; CD8 Cytotoxic / T Effector Memory:1333; CD4 T Effector Memory:291; RBC:160 | NK Cell:6762; CD8 Cytotoxic / T Effector Memory:307; Blood Cell:232; Treg:2 | not_available:7308 |
| T_NK_lineage:1 | 6,935 | CD4 Naive / T Central Memory | CD4 Naive / T Central Memory:5706; CD8 Naive / T Central Memory:989; CD8 Cytotoxic / T Effect... | CD4 Naive / T Central Memory:4458; CD8 Naive / T Central Memory:1568; Treg:763; T Cell:61 | CD4 Naive / T Central Memory:5700; CD8 Naive / T Central Memory:779; CD4 T Effector Memory:17... | CD4 Naive / T Central Memory:3550; not_available:3179; CD4 T Effector Memory:142; Treg:64 |
| T_NK_lineage:3 | 6,576 | CD4 Naive / T Central Memory | CD4 Naive / T Central Memory:6072; CD8 Naive / T Central Memory:322; CD8 Cytotoxic / T Effect... | CD4 Naive / T Central Memory:3375; Treg:2325; CD8 Naive / T Central Memory:723; T Cell:64 | CD4 Naive / T Central Memory:5984; Blood Cell:287; CD8 Naive / T Central Memory:178; CD8 Cyto... | CD4 Naive / T Central Memory:4629; not_available:1809; CD4 T Effector Memory:90; Treg:48 |
| T_NK_lineage:2 | 6,487 | CD8 Cytotoxic / T Effector Memory | NK Cell:3927; CD8 Cytotoxic / T Effector Memory:1906; CD4 Naive / T Central Memory:295; MAIT ... | CD8 Cytotoxic / T Effector Memory:3988; CD4 T Effector Memory:1654; CD8 Naive / T Central Mem... | CD8 Cytotoxic / T Effector Memory:5818; Blood Cell:357; NK Cell:194; CD4 Naive / T Central Me... | not_available:6443; CD4 T Effector Memory:28; CD4 Naive / T Central Memory:15; Treg:1 |
| T_NK_lineage:4 | 6,070 | CD4 Naive / T Central Memory | CD4 Naive / T Central Memory:4525; CD4 T Effector Memory:905; MAIT Cell:210; CD8 Cytotoxic / ... | CD4 Naive / T Central Memory:5202; Treg:358; CD8 Naive / T Central Memory:192; CD4 T Effector... | CD4 T Effector Memory:2999; CD4 Naive / T Central Memory:2515; Blood Cell:258; CD8 Cytotoxic ... | CD4 Naive / T Central Memory:3527; not_available:1770; CD4 T Effector Memory:713; Treg:60 |
| leiden:8 | 5,722 | Blood Cell | Classical Monocyte:3777; Blood Cell:1527; Plasma Cell:291; CD4 Naive / T Central Memory:92 | RBC:5717; Non-Classical Monocyte:2; Treg:1; HSC:1 | Blood Cell:4637; Classical Monocyte:1080; Conventional DC 2:2; Non-Classical Monocyte:2 | not_available:5357; Memory B Cell:275; CD4 Naive / T Central Memory:44; CD4 T Effector Memory:25 |
| T_NK_lineage:5 | 5,379 | CD4 Naive / T Central Memory | CD4 Naive / T Central Memory:4754; CD8 Naive / T Central Memory:150; CD8 Cytotoxic / T Effect... | CD4 Naive / T Central Memory:2356; Treg:2352; CD8 Naive / T Central Memory:368; CD8 Cytotoxic... | CD4 Naive / T Central Memory:4100; Blood Cell:853; CD8 Cytotoxic / T Effector Memory:213; CD4... | CD4 Naive / T Central Memory:3043; not_available:1951; CD4 T Effector Memory:276; Treg:109 |
| T_NK_lineage:6 | 5,179 | CD8 Naive / T Central Memory | CD4 Naive / T Central Memory:3320; CD8 Naive / T Central Memory:1705; CD8 Cytotoxic / T Effec... | CD8 Naive / T Central Memory:2680; CD4 Naive / T Central Memory:1533; Treg:875; CD8 Cytotoxic... | CD4 Naive / T Central Memory:3607; CD8 Naive / T Central Memory:1172; Blood Cell:258; CD8 Cyt... | not_available:3039; CD4 Naive / T Central Memory:2067; CD4 T Effector Memory:57; Treg:16 |
| T_NK_lineage:7 | 4,788 | CD4 Naive / T Central Memory | CD4 Naive / T Central Memory:4392; CD8 Naive / T Central Memory:344; CD8 Cytotoxic / T Effect... | CD4 Naive / T Central Memory:2207; Treg:1771; CD8 Naive / T Central Memory:767; ydT Cell:17 | CD4 Naive / T Central Memory:4430; CD8 Naive / T Central Memory:220; Blood Cell:103; CD8 Cyto... | CD4 Naive / T Central Memory:3192; not_available:1551; Treg:26; CD4 T Effector Memory:19 |
| T_NK_lineage:8 | 4,521 | CD8 Naive / T Central Memory | CD4 Naive / T Central Memory:2885; CD8 Naive / T Central Memory:1523; CD8 Cytotoxic / T Effec... | CD8 Naive / T Central Memory:2525; Treg:1099; CD4 Naive / T Central Memory:824; CD8 Cytotoxic... | CD4 Naive / T Central Memory:3066; CD8 Naive / T Central Memory:1064; Blood Cell:311; CD8 Cyt... | not_available:2915; CD4 Naive / T Central Memory:1562; CD4 T Effector Memory:32; Treg:12 |

## Review Priorities

- Inspect residual parent or Blood fallback populations in cellxgene, especially if they are spatially separated on UMAP.
- Check marker expression for labels that are biologically narrow or sensitive to missing genes.
- Treat doublet labels as submitted annotations, not filtered cells.
- For this dataset, the main review target is: This large dataset has few generic T Cell residuals but retains a large Blood Cell fallback group. B-cell labels look comparatively stable, while effector-memory T labels are intentionally gated and remain limited to strongly supported subclusters.

## Output Files

- Per-dataset report: `reports/current/vaccination_study_09/report_en.md`
- Japanese report: `reports/current/vaccination_study_09/report_ja.md`
- Label counts: `reports/current/vaccination_study_09/tables/label_counts.tsv`
- Cluster decisions: `reports/current/vaccination_study_09/tables/cluster_consensus_decisions.tsv`
- Local H5AD output: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/final_annotations/current_cluster_consensus/cellxgene/vaccination_study_09.final_annotation.cluster_consensus.cxg.h5ad`
- Local submission TSV: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/final_annotations/current_cluster_consensus/submissions/vaccination_study_09_annotation.tsv`
