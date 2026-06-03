# vaccination_study_04 Annotation Report

Updated: 2026-06-02 22:28:28 EDT

## Dataset-Specific Assessment

This dataset has the lowest parent-label burden among the current set and appears more myeloid/DC-skewed than a balanced whole-PBMC sample. pDC and DC calls should be interpreted with multi-marker support rather than single-gene evidence.

## Key Metrics

| Metric | Value |
| --- | --- |
| Cells | 66,065 |
| Genes in H5AD var | 16,983 |
| Submitted labels | 17 |
| Parent or Blood fallback cells | 1,321 (2.0%) |
| Doublet calls | 647 |
| Median confidence | 0.92 |
| CD4 T Effector Memory calls | 0 |
| Generic T Cell calls | 23 |
| Generic B Cell calls | 12 |


## Label Composition

Top submitted labels for this dataset:

| label | cells | fraction |
| --- | --- | --- |
| Classical Monocyte | 32,748 | 49.6% |
| Non-Classical Monocyte | 15,624 | 23.6% |
| Conventional DC 2 | 7,770 | 11.8% |
| Plasmacytoid DC | 5,615 | 8.5% |
| Conventional DC 1 | 1,099 | 1.7% |
| Myeloid Cell | 984 | 1.5% |
| HSC | 884 | 1.3% |
| Doublet | 647 | 1.0% |
| Blood Cell | 302 | 0.5% |
| NK Cell | 210 | 0.3% |
| Plasma Cell | 82 | 0.1% |
| Platelet | 26 | 0.0% |

## Cluster Consensus Review

The table below shows the largest accepted cluster-level decisions. `source_fraction` is the within-cluster fraction supporting the selected label across reference/evidence sources, and `marker_pct` is the cluster-level marker support for the chosen label. High values in both columns are stronger evidence than either value alone.

| lineage | cluster | cells | chosen_label | margin | source_fraction | marker_pct | reason |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Myeloid/DC | Myeloid_lineage:0 | 5,886 | Non-Classical Monocyte | 1.73 | 0.71 | 0.92 | cluster_consensus_marker_source_support |
| Myeloid/DC | Myeloid_lineage:1 | 5,457 | Classical Monocyte | 1.60 | 0.71 | 0.91 | cluster_consensus_marker_source_support |
| Myeloid/DC | Myeloid_lineage:2 | 5,421 | Classical Monocyte | 1.29 | 0.70 | 0.75 | cluster_consensus_marker_source_support |
| Myeloid/DC | Myeloid_lineage:3 | 5,343 | Classical Monocyte | 1.14 | 0.70 | 0.70 | cluster_consensus_marker_source_support |
| Myeloid/DC | Myeloid_lineage:4 | 3,752 | Conventional DC 2 | 0.98 | 0.49 | 0.85 | cluster_consensus_marker_source_support |
| Myeloid/DC | Myeloid_lineage:5 | 3,677 | Classical Monocyte | 1.04 | 0.71 | 0.74 | cluster_consensus_marker_source_support |
| Myeloid/DC | Myeloid_lineage:6 | 3,501 | Classical Monocyte | 0.99 | 0.68 | 0.53 | cluster_consensus_marker_source_support |
| Myeloid/DC | Myeloid_lineage:7 | 3,017 | Classical Monocyte | 1.47 | 0.71 | 0.79 | cluster_consensus_marker_source_support |
| Myeloid/DC | Myeloid_lineage:8 | 2,583 | Classical Monocyte | 1.12 | 0.70 | 0.70 | cluster_consensus_marker_source_support |
| Myeloid/DC | Myeloid_lineage:9 | 2,565 | Non-Classical Monocyte | 1.56 | 0.70 | 0.86 | cluster_consensus_marker_source_support |
| Myeloid/DC | Myeloid_lineage:10 | 2,458 | Non-Classical Monocyte | 1.51 | 0.67 | 0.87 | cluster_consensus_marker_source_support |
| Myeloid/DC | Myeloid_lineage:11 | 2,348 | Plasmacytoid DC | 1.57 | 0.71 | 0.95 | cluster_consensus_marker_source_support |

## Conservative Fallbacks

Fallback clusters are not failures by themselves. They mark clusters where the best fine label did not have enough margin, source support, marker support, or key-marker support to safely replace the parent/fallback label.

| lineage | cluster | cells | chosen_label | best_candidate | margin | reason |
| --- | --- | --- | --- | --- | --- | --- |
| Myeloid/DC | Myeloid_lineage:21 | 984 | Myeloid Cell | Classical Monocyte | 0.07 | cluster_parent_insufficient_consensus |
| Artifact/Other | leiden:31 | 23 | Blood Cell | HSC | 0.79 | cluster_parent_insufficient_consensus |
| Artifact/Other | leiden:34 | 22 | Blood Cell | RBC | 0.15 | cluster_parent_insufficient_consensus |
| T/NK | T_NK_lineage:7 | 17 | T Cell | CD8 Cytotoxic / T Effector Memory | 0.02 | cluster_parent_insufficient_consensus |
| Artifact/Other | leiden:4 | 13 | Blood Cell | Platelet | 0.45 | cluster_parent_insufficient_consensus |
| B | B_lineage:6 | 8 | B Cell | Plasmablast | 0.02 | cluster_parent_insufficient_consensus |
| Artifact/Other | leiden:16 | 8 | Blood Cell | HSC | 0.35 | cluster_parent_insufficient_consensus |
| B | B_lineage:14 | 4 | B Cell | Plasma Cell | 0.01 | cluster_parent_insufficient_consensus |
| T/NK | T_NK_lineage:10 | 4 | T Cell | NK Cell | 0.01 | cluster_parent_insufficient_consensus |
| Artifact/Other | leiden:27 | 3 | Blood Cell | HSC | 1.06 | cluster_parent_insufficient_consensus |
| Artifact/Other | leiden:30 | 3 | Blood Cell | HSC | 0.16 | cluster_parent_insufficient_consensus |
| T/NK | leiden:23 | 2 | T Cell | CD4 Naive / T Central Memory | 0.11 | cluster_parent_insufficient_consensus |

## Source Support Snapshot

This table is intended for quick review of where CellTypist, Azimuth, Pan-human Azimuth, and lineage-scoped scRefMapping agree or disagree in large clusters.

| cluster | cells | chosen_label | CellTypist | Azimuth_l2 | PanHuman | scRefMapping |
| --- | --- | --- | --- | --- | --- | --- |
| Myeloid_lineage:0 | 5,886 | Non-Classical Monocyte | Non-Classical Monocyte:5872; Classical Monocyte:13; NK Cell:1 | Non-Classical Monocyte:5885; Lymphoid Cell:1 | Non-Classical Monocyte:5833; Intermediate Monocyte:38; Blood Cell:14; Conventional DC 2:1 | not_available:5886 |
| Myeloid_lineage:1 | 5,457 | Classical Monocyte | Classical Monocyte:5457 | Classical Monocyte:5457 | Classical Monocyte:5410; Blood Cell:47 | not_available:5457 |
| Myeloid_lineage:2 | 5,421 | Classical Monocyte | Classical Monocyte:5417; Non-Classical Monocyte:2; Conventional DC 2:2 | Classical Monocyte:5416; Lymphoid Cell:4; Non-Classical Monocyte:1 | Classical Monocyte:4984; Blood Cell:330; Intermediate Monocyte:44; Conventional DC 2:36 | not_available:5421 |
| Myeloid_lineage:3 | 5,343 | Classical Monocyte | Classical Monocyte:5340; Non-Classical Monocyte:3 | Classical Monocyte:5339; Non-Classical Monocyte:4 | Classical Monocyte:4970; Blood Cell:199; Conventional DC 2:96; Intermediate Monocyte:66 | not_available:5343 |
| Myeloid_lineage:4 | 3,752 | Conventional DC 2 | Conventional DC 2:2744; Classical Monocyte:995; Blood Cell:11; Plasmacytoid DC:2 | Conventional DC 2:3022; Classical Monocyte:718; Blood Cell:9; Conventional DC 1:1 | Conventional DC 2:3447; Blood Cell:184; Classical Monocyte:120; Conventional DC 1:1 | not_available:3752 |
| Myeloid_lineage:5 | 3,677 | Classical Monocyte | Classical Monocyte:3677 | Classical Monocyte:3676; CD8 Cytotoxic / T Effector Memory:1 | Classical Monocyte:3648; Blood Cell:27; Non-Classical Monocyte:2 | not_available:3677 |
| Myeloid_lineage:6 | 3,501 | Classical Monocyte | Classical Monocyte:3464; Non-Classical Monocyte:36; Conventional DC 2:1 | Classical Monocyte:3454; Non-Classical Monocyte:42; Lymphoid Cell:5 | Classical Monocyte:2940; Intermediate Monocyte:213; Blood Cell:203; Non-Classical Monocyte:123 | not_available:3501 |
| Myeloid_lineage:7 | 3,017 | Classical Monocyte | Classical Monocyte:3017 | Classical Monocyte:3007; Lymphoid Cell:6; CD8 Cytotoxic / T Effector Memory:4 | Classical Monocyte:2867; Blood Cell:108; Conventional DC 2:28; Non-Classical Monocyte:13 | not_available:3017 |
| Myeloid_lineage:8 | 2,583 | Classical Monocyte | Classical Monocyte:2581; Conventional DC 2:1; Non-Classical Monocyte:1 | Classical Monocyte:2569; Lymphoid Cell:11; Non-Classical Monocyte:3 | Classical Monocyte:2396; Blood Cell:104; Conventional DC 2:50; Non-Classical Monocyte:16 | not_available:2583 |
| Myeloid_lineage:9 | 2,565 | Non-Classical Monocyte | Non-Classical Monocyte:2493; Classical Monocyte:70; CD8 Cytotoxic / T Effector Memory:1; Bloo... | Non-Classical Monocyte:2507; Classical Monocyte:37; Lymphoid Cell:17; CD4 Naive / T Central M... | Non-Classical Monocyte:2538; Intermediate Monocyte:20; Blood Cell:6; Conventional DC 2:1 | not_available:2565 |

## Review Priorities

- Inspect residual parent or Blood fallback populations in cellxgene, especially if they are spatially separated on UMAP.
- Check marker expression for labels that are biologically narrow or sensitive to missing genes.
- Treat doublet labels as submitted annotations, not filtered cells.
- For this dataset, the main review target is: This dataset has the lowest parent-label burden among the current set and appears more myeloid/DC-skewed than a balanced whole-PBMC sample. pDC and DC calls should be interpreted with multi-marker support rather than single-gene evidence.

## Output Files

- Per-dataset report: `reports/current/vaccination_study_04/report_en.md`
- Japanese report: `reports/current/vaccination_study_04/report_ja.md`
- Label counts: `reports/current/vaccination_study_04/tables/label_counts.tsv`
- Cluster decisions: `reports/current/vaccination_study_04/tables/cluster_consensus_decisions.tsv`
- Local H5AD output: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/final_annotations/current_cluster_consensus/cellxgene/vaccination_study_04.final_annotation.cluster_consensus.cxg.h5ad`
- Local submission TSV: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/final_annotations/current_cluster_consensus/submissions/vaccination_study_04_annotation.tsv`
