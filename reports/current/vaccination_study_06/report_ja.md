# vaccination_study_06 Annotation Report

Updated: 2026-06-02 22:28:28 EDT

## Dataset-Specific Assessment

最も conservative な call set で、parent label が多く残っています。T/NK と B compartment に quality または sampling 由来の曖昧さがあり、marker expression review を優先すべきです。

## Key Metrics

| Metric | Value |
| --- | --- |
| Cells | 57,419 |
| Genes in H5AD var | 11,878 |
| Submitted labels | 19 |
| Parent or Blood fallback cells | 7,949 (13.8%) |
| Doublet calls | 1,502 |
| Median confidence | 0.92 |
| CD4 T Effector Memory calls | 445 |
| Generic T Cell calls | 2,959 |
| Generic B Cell calls | 29 |


## Label Composition

この dataset の submitted label 上位です。

| label | cells | fraction |
| --- | --- | --- |
| CD4 Naive / T Central Memory | 25,096 | 43.7% |
| NK Cell | 8,728 | 15.2% |
| CD8 Cytotoxic / T Effector Memory | 7,885 | 13.7% |
| Blood Cell | 4,957 | 8.6% |
| T Cell | 2,959 | 5.2% |
| Memory B Cell | 2,772 | 4.8% |
| Doublet | 1,502 | 2.6% |
| MAIT Cell | 1,339 | 2.3% |
| CD8 Naive / T Central Memory | 869 | 1.5% |
| Naive B Cell | 791 | 1.4% |
| CD4 T Effector Memory | 445 | 0.8% |
| B Cell | 29 | 0.1% |

## Cluster Consensus Review

下の表は、大きい accepted cluster-level decision を示します。`source_fraction` は reference/evidence source が選択 label を支持した cluster 内割合、`marker_pct` は選択 label の cluster-level marker support です。どちらか一方だけではなく、両方が高い場合により強い証拠と見ます。

| lineage | cluster | cells | chosen_label | margin | source_fraction | marker_pct | reason |
| --- | --- | --- | --- | --- | --- | --- | --- |
| T/NK | T_NK_lineage:0 | 3,297 | NK Cell | 1.42 | 0.65 | 0.95 | cluster_consensus_marker_source_support |
| T/NK | T_NK_lineage:2 | 2,948 | CD4 Naive / T Central Memory | 0.84 | 0.49 | 0.61 | cluster_consensus_marker_source_support |
| T/NK | T_NK_lineage:6 | 2,810 | CD4 Naive / T Central Memory | 1.64 | 0.74 | 0.91 | cluster_consensus_marker_source_support |
| T/NK | T_NK_lineage:7 | 2,780 | CD4 Naive / T Central Memory | 0.83 | 0.50 | 0.83 | cluster_consensus_marker_source_support |
| T/NK | T_NK_lineage:3 | 2,743 | CD8 Cytotoxic / T Effector Memory | 1.56 | 0.49 | 0.95 | cluster_consensus_marker_source_support |
| T/NK | T_NK_lineage:9 | 2,730 | CD4 Naive / T Central Memory | 1.61 | 0.74 | 0.92 | cluster_consensus_marker_source_support |
| T/NK | T_NK_lineage:4 | 2,662 | CD4 Naive / T Central Memory | 0.18 | 0.35 | 0.55 | cluster_consensus_marker_source_support |
| T/NK | T_NK_lineage:11 | 2,587 | CD4 Naive / T Central Memory | 1.30 | 0.66 | 0.83 | cluster_consensus_marker_source_support |
| T/NK | T_NK_lineage:10 | 2,521 | CD4 Naive / T Central Memory | 0.92 | 0.50 | 0.69 | cluster_consensus_marker_source_support |
| T/NK | T_NK_lineage:12 | 2,177 | CD4 Naive / T Central Memory | 0.98 | 0.51 | 0.72 | cluster_consensus_marker_source_support |
| T/NK | T_NK_lineage:5 | 2,163 | CD8 Cytotoxic / T Effector Memory | 0.92 | 0.45 | 0.76 | cluster_consensus_marker_source_support |
| T/NK | T_NK_lineage:8 | 1,950 | NK Cell | 1.02 | 0.51 | 0.86 | cluster_consensus_marker_source_support |

## Conservative Fallbacks

Fallback cluster はそれ自体が失敗ではありません。best fine label の margin、source support、marker support、key-marker support が十分でない場合に、過剰な fine label を避けて parent/fallback label に残した cluster です。

| lineage | cluster | cells | chosen_label | best_candidate | margin | reason |
| --- | --- | --- | --- | --- | --- | --- |
| T/NK | T_NK_lineage:1 | 3,162 | T Cell | CD4 T Effector Memory | 0.04 | cluster_parent_insufficient_consensus |
| Artifact/Other | leiden:12 | 698 | Blood Cell | RBC | 0.02 | cluster_parent_insufficient_consensus |
| Artifact/Other | leiden:8 | 165 | Blood Cell | Platelet | 0.31 | cluster_parent_insufficient_consensus |
| Artifact/Other | leiden:4 | 113 | Blood Cell | Platelet | 0.04 | cluster_parent_insufficient_consensus |
| Artifact/Other | leiden:2 | 87 | Blood Cell | HSC | 0.11 | cluster_parent_insufficient_consensus |
| Artifact/Other | leiden:13 | 57 | Blood Cell | HSC | 0.13 | cluster_parent_insufficient_consensus |
| Artifact/Other | leiden:3 | 51 | Blood Cell | Platelet | 0.67 | cluster_parent_insufficient_consensus |
| Artifact/Other | leiden:0 | 48 | Blood Cell | HSC | 0.44 | cluster_parent_insufficient_consensus |
| Artifact/Other | leiden:15 | 39 | Blood Cell | Platelet | 0.23 | cluster_parent_insufficient_consensus |
| B | leiden:18 | 26 | B Cell | Memory B Cell | 0.07 | cluster_parent_insufficient_consensus |
| Artifact/Other | leiden:21 | 23 | Blood Cell | Platelet | 0.03 | cluster_parent_insufficient_consensus |
| Artifact/Other | leiden:24 | 23 | Blood Cell | Platelet | 0.12 | cluster_parent_insufficient_consensus |

## Source Support Snapshot

CellTypist、Azimuth、Pan-human Azimuth、lineage-scoped scRefMapping が大きい cluster でどの程度一致・不一致かを素早く見るための表です。

| cluster | cells | chosen_label | CellTypist | Azimuth_l2 | PanHuman | scRefMapping |
| --- | --- | --- | --- | --- | --- | --- |
| T_NK_lineage:0 | 3,297 | NK Cell | NK Cell:2945; CD8 Cytotoxic / T Effector Memory:287; Blood Cell:48; CD4 T Effector Memory:9 | NK Cell:3245; CD4 Naive / T Central Memory:20; CD8 Cytotoxic / T Effector Memory:17; ydT Cell:12 | NK Cell:2776; Blood Cell:460; CD8 Cytotoxic / T Effector Memory:46; CD8 T Cell (ab):6 | not_available:3297 |
| T_NK_lineage:1 | 3,162 | T Cell | CD4 T Effector Memory:2685; CD8 Cytotoxic / T Effector Memory:155; CD4 Naive / T Central Memo... | CD4 Naive / T Central Memory:2743; CD8 Naive / T Central Memory:330; Plasmablast:29; Treg:25 | CD4 T Cell (ab):1698; CD4 T Effector Memory:873; Treg:326; Blood Cell:224 | CD4 Naive / T Central Memory:2059; not_available:539; CD4 T Effector Memory:490; Treg:74 |
| T_NK_lineage:2 | 2,948 | CD4 Naive / T Central Memory | CD4 Naive / T Central Memory:2784; CD4 T Effector Memory:32; CD8 Cytotoxic / T Effector Memor... | T Cell:2648; CD4 Naive / T Central Memory:282; RBC:7; Treg:5 | CD4 Naive / T Central Memory:1607; Blood Cell:671; Treg:289; CD4 T Cell (ab):222 | CD4 Naive / T Central Memory:2438; not_available:433; CD4 T Effector Memory:47; Treg:30 |
| T_NK_lineage:6 | 2,810 | CD4 Naive / T Central Memory | CD4 Naive / T Central Memory:2735; CD4 T Effector Memory:50; Treg:11; CD8 Naive / T Central M... | CD4 Naive / T Central Memory:2808; CD8 Cytotoxic / T Effector Memory:1; Treg:1 | CD4 Naive / T Central Memory:1735; Blood Cell:687; Treg:203; CD4 T Effector Memory:102 | CD4 Naive / T Central Memory:2761; not_available:25; Treg:20; CD4 T Effector Memory:4 |
| T_NK_lineage:7 | 2,780 | CD4 Naive / T Central Memory | CD4 Naive / T Central Memory:1294; CD4 T Effector Memory:1211; Treg:168; Blood Cell:55 | CD4 Naive / T Central Memory:2742; CD8 Naive / T Central Memory:21; Treg:15; CD8 Cytotoxic / ... | CD4 T Cell (ab):885; CD4 T Effector Memory:784; Treg:596; CD4 Naive / T Central Memory:287 | CD4 Naive / T Central Memory:2483; Treg:170; CD4 T Effector Memory:67; not_available:60 |
| T_NK_lineage:3 | 2,743 | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory:2571; CD4 T Effector Memory:50; ydT Cell:48; NK Cell:23 | CD8 Cytotoxic / T Effector Memory:2041; CD4 Naive / T Central Memory:401; NK Cell:99; ydT Cel... | CD8 Cytotoxic / T Effector Memory:2067; Blood Cell:364; CD8 T Cell (ab):89; CD4 T Cell (ab):69 | not_available:2654; CD4 T Effector Memory:81; CD4 Naive / T Central Memory:8 |
| T_NK_lineage:9 | 2,730 | CD4 Naive / T Central Memory | CD4 Naive / T Central Memory:2668; CD4 T Effector Memory:26; CD8 Naive / T Central Memory:22;... | CD4 Naive / T Central Memory:2704; CD8 Naive / T Central Memory:25; Treg:1 | CD4 Naive / T Central Memory:2040; Blood Cell:304; Treg:174; CD4 T Effector Memory:106 | CD4 Naive / T Central Memory:2677; not_available:44; Treg:5; CD4 T Effector Memory:4 |
| T_NK_lineage:4 | 2,662 | CD4 Naive / T Central Memory | CD4 Naive / T Central Memory:1417; CD4 T Effector Memory:535; CD8 Cytotoxic / T Effector Memo... | T Cell:1678; CD4 Naive / T Central Memory:798; CD4 T Effector Memory:54; Treg:53 | CD4 T Effector Memory:711; Treg:644; Blood Cell:512; CD4 T Cell (ab):510 | CD4 Naive / T Central Memory:1596; CD4 T Effector Memory:567; not_available:347; Treg:152 |
| T_NK_lineage:11 | 2,587 | CD4 Naive / T Central Memory | CD4 Naive / T Central Memory:2282; CD4 T Effector Memory:164; Blood Cell:55; CD8 Naive / T Ce... | CD4 Naive / T Central Memory:2549; CD8 Naive / T Central Memory:30; Plasmablast:6; Treg:2 | CD4 Naive / T Central Memory:1115; CD4 T Cell (ab):697; Treg:409; Blood Cell:247 | CD4 Naive / T Central Memory:2498; not_available:44; Treg:34; CD4 T Effector Memory:11 |
| T_NK_lineage:10 | 2,521 | CD4 Naive / T Central Memory | CD4 Naive / T Central Memory:2387; CD8 Naive / T Central Memory:61; Treg:26; Blood Cell:18 | T Cell:2171; CD4 Naive / T Central Memory:350 | CD4 Naive / T Central Memory:1383; Blood Cell:635; Treg:270; CD4 T Effector Memory:85 | CD4 Naive / T Central Memory:2132; not_available:352; Treg:29; CD4 T Effector Memory:8 |

## Review Priorities

- cellxgene で residual parent または Blood fallback population を確認する。UMAP 上で分離している場合は特に重要。
- biological に狭い label や marker gene 欠損の影響を受けやすい label は、marker expression を確認する。
- Doublet は filter out ではなく submitted annotation として扱う。
- この dataset の主な確認対象: 最も conservative な call set で、parent label が多く残っています。T/NK と B compartment に quality または sampling 由来の曖昧さがあり、marker expression review を優先すべきです。

## Output Files

- Per-dataset report: `reports/current/vaccination_study_06/report_en.md`
- Japanese report: `reports/current/vaccination_study_06/report_ja.md`
- Label counts: `reports/current/vaccination_study_06/tables/label_counts.tsv`
- Cluster decisions: `reports/current/vaccination_study_06/tables/cluster_consensus_decisions.tsv`
- Local H5AD output: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/final_annotations/current_cluster_consensus/cellxgene/vaccination_study_06.final_annotation.cluster_consensus.cxg.h5ad`
- Local submission TSV: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/final_annotations/current_cluster_consensus/submissions/vaccination_study_06_annotation.tsv`
