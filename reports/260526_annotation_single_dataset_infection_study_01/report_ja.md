# infection_study_01 annotation review

Updated: 2026-05-27 EDT

## Dataset-specific assessment

infection_study_01 は 54,924 cells / 33,538 portal genes の dataset です。親ラベルまたは Blood Cell に残った割合は 0.3%、doublet は 1,278 cells、低 confidence は 2,209 cells でした。重大な marker gene 欠損は目立ちません。 whole PBMC に近い構成として読めます。 subcluster evidence では Classical Monocyte: 17,228 cells; CD8 Cytotoxic / T Effector Memory: 10,828 cells; NK Cell: 8,163 cells; Naive B Cell: 4,174 cells; CD4 Naive / T Central Memory: 4,134 cells; CD4 T Effector Memory: 2,303 cells が主要な構造です。全細胞に近い coverage で最も broad lineage に沿った source は Azimuth PBMC L2 (broad concordance 97.2%) で、相対的に不一致が目立つ source は Azimuth PBMC L3 (45.0%) です。 screfmap は適用範囲を B/CD4T に限定すると coverage 22.8%、broad concordance 97.7% でした。

## Methods

この report は、portal input の raw/count-like gene space、CellTypist、Azimuth PBMC、Pan-human Azimuth、screfmap、marker score、lineage-specific subclustering を dataset 単位で照合したものです。ここでの tool concordance は ground truth accuracy ではなく、最終 annotation に対する support/disagreement の診断指標です。

## Input and QC

| cells | portal_genes | raw_count_source | count_like_fraction | available_marker_umap_genes | missing_marker_umap_genes | parent_or_blood_fraction | median_confidence | low_confidence_n | doublet_n |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 54,924 | 33,538 | layers[counts] | 1.000 | 48 | none | 0.003 | 0.846 | 2,209 | 1,278 |

### QC and annotation UMAPs

![Final labels](assets/umap_infection_study_01_v13_label.png)

![QC and confidence](assets/umap_infection_study_01_v13_qc_confidence.png)

![Lineage and annotation reason](assets/umap_infection_study_01_v13_lineage_reason.png)

## Marker expression UMAPs

### lineage_core

![lineage_core marker expression](assets/umap_infection_study_01_lineage_core_marker_expression.png)

### b_t_fine

![b_t_fine marker expression](assets/umap_infection_study_01_b_t_fine_marker_expression.png)

### myeloid_dc

![myeloid_dc marker expression](assets/umap_infection_study_01_myeloid_dc_marker_expression.png)

## Annotation source assessment

![Annotation source UMAPs](assets/umap_infection_study_01_annotation_source_labels.png)

![Tool concordance](assets/bar_infection_study_01_tool_concordance.png)

各 source は適用範囲が異なるため、coverage と concordance を分けて読んでください。screfmap は B/CD4T scoped cells だけで評価しています。

| tool | covered_n | coverage_fraction | exact_final_concordance | broad_final_concordance | top_supported_labels | top_disagreements |
| --- | --- | --- | --- | --- | --- | --- |
| CellTypist | 54,924 | 1.000 | 0.796 | 0.968 | Classical Monocyte: 17,334; CD8 Cytotoxic / T Effector Memory: 10,859; NK Cell: 8,294; Naive B Cell: 4,151; CD4 Naive / T Central Memory: 3,551 | CD8 Cytotoxic / T Effector Memory vs NK Cell: 1,726; NK Cell vs CD8 Cytotoxic / T Effector Memory: 1,500; CD4 Naive / T Central Memory vs CD4 T Effector Memory: 994; CD4 T Effector Memory vs CD8 Cytotoxic / T Effector Memory: 812; Doublet vs Classical Monocyte: 705 |
| Azimuth PBMC L2 | 54,924 | 1.000 | 0.777 | 0.972 | Classical Monocyte: 17,464; NK Cell: 8,590; CD8 Cytotoxic / T Effector Memory: 7,486; CD4 Naive / T Central Memory: 4,975; Naive B Cell: 4,042 | CD8 Cytotoxic / T Effector Memory vs NK Cell: 1,537; Memory B Cell vs B Cell: 1,136; CD4 T Effector Memory vs CD4 Naive / T Central Memory: 1,007; CD8 Cytotoxic / T Effector Memory vs CD4 T Effector Memory: 986; CD8 Cytotoxic / T Effector Memory vs ydT Cell: 832 |
| Azimuth PBMC L3 | 54,924 | 1.000 | 0.393 | 0.450 | Blood Cell: 29,371; Classical Monocyte: 17,469; Non-Classical Monocyte: 2,621; Platelet: 1,552; CD4 T Effector Memory: 1,046 | CD8 Cytotoxic / T Effector Memory vs Blood Cell: 9,480; NK Cell vs Blood Cell: 7,331; Naive B Cell vs Blood Cell: 4,166; CD4 Naive / T Central Memory vs Blood Cell: 3,239; Memory B Cell vs Blood Cell: 2,165 |
| Pan-human Azimuth fine | 54,924 | 1.000 | 0.725 | 0.907 | Classical Monocyte: 13,795; CD8 Cytotoxic / T Effector Memory: 9,701; NK Cell: 7,361; Blood Cell: 3,933; Naive B Cell: 3,693 | Classical Monocyte vs Blood Cell: 1,845; CD4 Naive / T Central Memory vs CD4 T Effector Memory: 1,661; CD8 Cytotoxic / T Effector Memory vs NK Cell: 1,265; Classical Monocyte vs Intermediate Monocyte: 1,060; NK Cell vs CD8 Cytotoxic / T Effector Memory: 871 |
| Pan-human Azimuth medium | 54,924 | 1.000 | 0.136 | 0.910 | Monocyte: 17,204; T Cell: 16,536; NK Cell: 7,365; B Cell: 6,553; Blood Cell: 3,601 | Classical Monocyte vs Monocyte: 14,547; CD8 Cytotoxic / T Effector Memory vs T Cell: 8,961; Naive B Cell vs B Cell: 4,103; CD4 Naive / T Central Memory vs T Cell: 4,022; CD4 T Effector Memory vs T Cell: 2,204 |
| Cluster consensus | 54,924 | 1.000 | 0.810 | 0.969 | Classical Monocyte: 18,521; NK Cell: 9,776; CD8 Cytotoxic / T Effector Memory: 8,004; CD4 T Effector Memory: 4,181; Naive B Cell: 4,014 | Memory B Cell vs B Cell: 2,115; CD8 Cytotoxic / T Effector Memory vs NK Cell: 1,842; CD4 Naive / T Central Memory vs CD4 T Effector Memory: 1,680; Doublet vs Classical Monocyte: 948; CD8 Cytotoxic / T Effector Memory vs MAIT Cell: 686 |
| Marker score | 54,924 | 1.000 | 0.178 | 0.965 | Monocyte: 19,593; NK Cell: 10,947; B Cell: 6,446; CD8 T Cell (ab): 6,284; CD4 T Cell (ab): 4,895 | Classical Monocyte vs Monocyte: 17,024; CD8 Cytotoxic / T Effector Memory vs CD8 T Cell (ab): 5,216; Naive B Cell vs B Cell: 4,103; CD8 Cytotoxic / T Effector Memory vs NK Cell: 3,337; CD4 Naive / T Central Memory vs CD4 T Cell (ab): 2,862 |
| screfmap scoped | 12,525 | 0.228 | 0.783 | 0.977 | CD4 Naive / T Central Memory: 4,753; Naive B Cell: 4,145; Memory B Cell: 2,382; CD4 T Effector Memory: 847; Treg: 262 | CD4 T Effector Memory vs CD4 Naive / T Central Memory: 930; CD8 Cytotoxic / T Effector Memory vs CD4 Naive / T Central Memory: 332; Naive B Cell vs Memory B Cell: 208; CD8 Cytotoxic / T Effector Memory vs CD4 T Effector Memory: 180; CD4 Naive / T Central Memory vs CD4 T Effector Memory: 179 |

### Lineage-scoped source support

| final_broad_lineage | tool | covered_n | exact_final_concordance | broad_final_concordance |
| --- | --- | --- | --- | --- |
| B | CellTypist | 6,509 | 0.857 | 0.988 |
| B | Azimuth PBMC L2 | 6,509 | 0.742 | 0.991 |
| B | Azimuth PBMC L3 | 6,509 | 0.013 | 0.020 |
| B | Pan-human Azimuth fine | 6,509 | 0.896 | 0.984 |
| B | Pan-human Azimuth medium | 6,509 | 0.000 | 0.984 |
| B | Cluster consensus | 6,509 | 0.620 | 0.984 |
| B | Marker score | 6,509 | 0.025 | 0.988 |
| B | screfmap scoped | 6,502 | 0.940 | 0.998 |
| T/NK | CellTypist | 25,685 | 0.698 | 0.992 |
| T/NK | Azimuth PBMC L2 | 25,685 | 0.674 | 0.993 |
| T/NK | Azimuth PBMC L3 | 25,685 | 0.052 | 0.128 |
| T/NK | Pan-human Azimuth fine | 25,685 | 0.671 | 0.922 |
| T/NK | Pan-human Azimuth medium | 25,685 | 0.236 | 0.926 |
| T/NK | Cluster consensus | 25,685 | 0.771 | 0.990 |
| T/NK | Marker score | 25,685 | 0.289 | 0.983 |
| T/NK | screfmap scoped | 5,750 | 0.642 | 0.999 |
| Myeloid/DC | CellTypist | 19,897 | 0.946 | 0.996 |
| Myeloid/DC | Azimuth PBMC L2 | 19,897 | 0.963 | 0.997 |
| Myeloid/DC | Azimuth PBMC L3 | 19,897 | 0.944 | 0.974 |
| Myeloid/DC | Pan-human Azimuth fine | 19,897 | 0.763 | 0.898 |

## Lineage-specific subclustering

### B_lineage

![B_lineage subcluster labels](assets/umap_infection_study_01_B_lineage_v13_subcluster_label.png)

![B_lineage subcluster QC](assets/umap_infection_study_01_B_lineage_v13_subcluster_qc.png)

| cluster | n_cells | chosen_label | accepted | score_margin | calibrated_cluster_confidence | marker_availability_alert | top_celltypist | top_panhuman_fine | top_marker | top_screfmapping |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 475 | Naive B Cell | True | 4.230 | 0.850 | pass | Naive B Cell:473; Memory B Cell:2 | Naive B Cell:450; Memory B Cell:21; Blood Cell:4 | B Cell:475 | Naive B Cell:473; Plasma Cell:2 |
| 1 | 434 | Naive B Cell | True | 4.195 | 0.850 | pass | Naive B Cell:422; Blood Cell:10; B Cell:1; Memory B Cell:1 | Naive B Cell:427; Memory B Cell:5; Blood Cell:2 | B Cell:434 | Naive B Cell:431; Plasma Cell:2; Memory B Cell:1 |
| 2 | 402 | Naive B Cell | True | 4.192 | 0.850 | pass | Naive B Cell:394; Memory B Cell:8 | Naive B Cell:373; Memory B Cell:27; Blood Cell:2 | B Cell:402 | Naive B Cell:394; Memory B Cell:8 |
| 3 | 372 | Naive B Cell | True | 3.966 | 0.850 | pass | Naive B Cell:358; Memory B Cell:12; B Cell:2 | Naive B Cell:310; Memory B Cell:52; Blood Cell:10 | B Cell:372 | Naive B Cell:356; Memory B Cell:16 |
| 4 | 365 | Naive B Cell | True | 4.264 | 0.850 | pass | Naive B Cell:363; Memory B Cell:2 | Naive B Cell:323; Memory B Cell:35; Blood Cell:7 | B Cell:365 | Naive B Cell:364; Memory B Cell:1 |
| 5 | 360 | Memory B Cell | True | 2.762 | 0.818 | pass | Memory B Cell:315; Naive B Cell:41; B Cell:4 | Memory B Cell:342; Naive B Cell:15; Blood Cell:3 | B Cell:359; Plasma Cell:1 | Memory B Cell:322; Naive B Cell:37; Plasma Cell:1 |
| 6 | 351 | Memory B Cell | True | 3.403 | 0.828 | pass | Memory B Cell:334; Naive B Cell:13; B Cell:4 | Memory B Cell:350; Naive B Cell:1 | B Cell:350; Non-Classical Monocyte:1 | Memory B Cell:343; Naive B Cell:8 |
| 7 | 302 | Memory B Cell | True | 3.957 | 0.848 | pass | Memory B Cell:298; B Cell:3; Naive B Cell:1 | Memory B Cell:302 | B Cell:301; RBC:1 | Memory B Cell:302 |
| 8 | 296 | Memory B Cell | True | 3.229 | 0.850 | pass | Memory B Cell:173; B Cell:83; Naive B Cell:39; Blood Cell:1 | Memory B Cell:285; Naive B Cell:9; Blood Cell:2 | B Cell:296 | Memory B Cell:276; Naive B Cell:20 |
| 9 | 281 | Naive B Cell | True | 4.368 | 0.850 | pass | Naive B Cell:277; Blood Cell:2; Memory B Cell:2 | Naive B Cell:266; Memory B Cell:10; Blood Cell:5 | B Cell:281 | Naive B Cell:278; Memory B Cell:3 |

### T_NK_lineage

![T_NK_lineage subcluster labels](assets/umap_infection_study_01_T_NK_lineage_v13_subcluster_label.png)

![T_NK_lineage subcluster QC](assets/umap_infection_study_01_T_NK_lineage_v13_subcluster_qc.png)

| cluster | n_cells | chosen_label | accepted | score_margin | calibrated_cluster_confidence | marker_availability_alert | top_celltypist | top_panhuman_fine | top_marker | top_screfmapping |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1,634 | CD4 Naive / T Central Memory | True | 2.985 | 0.850 | pass | CD4 Naive / T Central Memory:1336; CD8 Naive / T Central Memory:268; Treg:15; CD8 Cytotoxic / T Effector Memory:10; CD4 T Effector Memory:3 | CD4 Naive / T Central Memory:1188; CD8 Naive / T Central Memory:321; CD4 T Effector Memory:59; Blood Cell:35; Treg:22 | CD4 T Cell (ab):1058; T Cell:514; CD8 T Cell (ab):50; Monocyte:5; RBC:4 | CD4 Naive / T Central Memory:1397; not_available:205; Treg:27; CD4 T Effector Memory:5 |
| 1 | 1,571 | NK Cell | True | 1.124 | 0.850 | pass | NK Cell:1087; CD8 Cytotoxic / T Effector Memory:480; ydT Cell:3; Blood Cell:1 | NK Cell:786; CD8 Cytotoxic / T Effector Memory:630; Blood Cell:152; Lymphoid Cell:2; ydT Cell:1 | NK Cell:1487; CD8 T Cell (ab):67; T Cell:17 | not_available:1571 |
| 2 | 1,342 | NK Cell | True | 1.553 | 0.850 | pass | NK Cell:828; CD8 Cytotoxic / T Effector Memory:510; ydT Cell:4 | NK Cell:1149; CD8 Cytotoxic / T Effector Memory:116; Blood Cell:76; Lymphoid Cell:1 | NK Cell:1332; CD8 T Cell (ab):8; RBC:1; T Cell:1 | not_available:1342 |
| 3 | 1,327 | CD4 Naive / T Central Memory | True | 0.028 | 0.680 | pass | CD4 T Effector Memory:826; CD4 Naive / T Central Memory:360; CD8 Cytotoxic / T Effector Memory:63; CD8 Naive / T Central Memory:29; NK Cell:19 | CD4 T Effector Memory:1181; Blood Cell:43; CD8 Cytotoxic / T Effector Memory:37; Treg:37; CD8 Naive / T Central Memory:15 | CD4 T Cell (ab):1065; T Cell:205; CD8 T Cell (ab):35; NK Cell:15; DC:3 | CD4 Naive / T Central Memory:943; not_available:229; CD4 T Effector Memory:146; Treg:9 |
| 4 | 1,327 | CD8 Cytotoxic / T Effector Memory | True | 2.272 | 0.740 | pass | CD8 Cytotoxic / T Effector Memory:1308; NK Cell:18; Treg:1 | CD8 Cytotoxic / T Effector Memory:1286; NK Cell:24; Blood Cell:12; Lymphoid Cell:3; Treg:1 | CD8 T Cell (ab):942; NK Cell:324; T Cell:45; Monocyte:9; CD4 T Cell (ab):6 | not_available:1326; CD4 T Effector Memory:1 |
| 5 | 1,175 | CD8 Cytotoxic / T Effector Memory | True | 2.141 | 0.737 | pass | CD8 Cytotoxic / T Effector Memory:1129; NK Cell:39; CD4 Naive / T Central Memory:5; ydT Cell:1; T Cell:1 | CD8 Cytotoxic / T Effector Memory:1159; Blood Cell:6; NK Cell:5; CD4 T Effector Memory:3; MAIT Cell:1 | CD8 T Cell (ab):627; NK Cell:300; T Cell:222; CD4 T Cell (ab):26 | not_available:1172; CD4 T Effector Memory:2; CD4 Naive / T Central Memory:1 |
| 6 | 1,000 | CD8 Cytotoxic / T Effector Memory | True | 1.817 | 0.722 | pass | CD8 Cytotoxic / T Effector Memory:854; NK Cell:96; ydT Cell:24; MAIT Cell:21; Memory B Cell:2 | CD8 Cytotoxic / T Effector Memory:876; Blood Cell:56; NK Cell:22; ydT Cell:20; MAIT Cell:19 | CD8 T Cell (ab):592; NK Cell:234; T Cell:139; CD4 T Cell (ab):35 | not_available:986; CD4 T Effector Memory:13; CD4 Naive / T Central Memory:1 |
| 7 | 999 | NK Cell | True | 2.646 | 0.850 | pass | NK Cell:997; CD8 Cytotoxic / T Effector Memory:2 | NK Cell:979; Blood Cell:15; CD8 Cytotoxic / T Effector Memory:4; Lymphoid Cell:1 | NK Cell:999 | not_available:999 |
| 8 | 901 | CD8 Cytotoxic / T Effector Memory | True | 1.405 | 0.725 | pass | CD8 Cytotoxic / T Effector Memory:661; NK Cell:178; ydT Cell:41; MAIT Cell:12; CD4 Naive / T Central Memory:5 | CD8 Cytotoxic / T Effector Memory:670; NK Cell:138; Blood Cell:55; MAIT Cell:32; ydT Cell:2 | CD8 T Cell (ab):407; NK Cell:356; T Cell:103; CD4 T Cell (ab):34; RBC:1 | not_available:889; CD4 T Effector Memory:12 |
| 9 | 880 | CD8 Cytotoxic / T Effector Memory | True | 0.204 | 0.658 | pass | CD8 Cytotoxic / T Effector Memory:512; NK Cell:350; ydT Cell:5; CD4 Naive / T Central Memory:5; CD4 T Effector Memory:4 | CD8 Cytotoxic / T Effector Memory:465; NK Cell:314; Blood Cell:93; CD4 T Effector Memory:4; MAIT Cell:2 | NK Cell:499; CD8 T Cell (ab):200; T Cell:144; CD4 T Cell (ab):33; Monocyte:3 | not_available:866; CD4 Naive / T Central Memory:8; CD4 T Effector Memory:6 |

### Myeloid_lineage

![Myeloid_lineage subcluster labels](assets/umap_infection_study_01_Myeloid_lineage_v13_subcluster_label.png)

![Myeloid_lineage subcluster QC](assets/umap_infection_study_01_Myeloid_lineage_v13_subcluster_qc.png)

| cluster | n_cells | chosen_label | accepted | score_margin | calibrated_cluster_confidence | marker_availability_alert | top_celltypist | top_panhuman_fine | top_marker | top_screfmapping |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1,455 | Non-Classical Monocyte | True | 1.846 | 0.850 | pass | Non-Classical Monocyte:1413; Classical Monocyte:41; Blood Cell:1 | Non-Classical Monocyte:1067; Intermediate Monocyte:327; Blood Cell:53; Classical Monocyte:5; Conventional DC 2:3 | Monocyte:885; Non-Classical Monocyte:569; RBC:1 | not_available:1455 |
| 1 | 1,411 | Classical Monocyte | True | 2.790 | 0.850 | pass | Classical Monocyte:1393; Non-Classical Monocyte:17; Blood Cell:1 | Classical Monocyte:1264; Blood Cell:103; Neutrophil:26; Intermediate Monocyte:12; Conventional DC 2:5 | Monocyte:1409; RBC:1; Non-Classical Monocyte:1 | not_available:1411 |
| 2 | 1,354 | Classical Monocyte | True | 2.247 | 0.848 | pass | Classical Monocyte:1293; Non-Classical Monocyte:61 | Classical Monocyte:979; Intermediate Monocyte:292; Blood Cell:61; Conventional DC 2:18; Non-Classical Monocyte:3 | Monocyte:1353; DC:1 | not_available:1354 |
| 3 | 1,295 | Classical Monocyte | True | 2.450 | 0.840 | pass | Classical Monocyte:1257; Non-Classical Monocyte:35; Blood Cell:2; Conventional DC 2:1 | Classical Monocyte:1084; Blood Cell:100; Conventional DC 2:56; Intermediate Monocyte:53; Non-Classical Monocyte:2 | Monocyte:1291; DC:3; Non-Classical Monocyte:1 | not_available:1295 |
| 4 | 1,199 | Classical Monocyte | True | 2.677 | 0.850 | pass | Classical Monocyte:1190; Non-Classical Monocyte:9 | Classical Monocyte:986; Blood Cell:162; Neutrophil:27; Intermediate Monocyte:12; Non-Classical Monocyte:7 | Monocyte:1196; Platelet:3 | not_available:1199 |
| 5 | 1,196 | Classical Monocyte | True | 2.766 | 0.850 | pass | Classical Monocyte:1194; Blood Cell:1; Non-Classical Monocyte:1 | Classical Monocyte:1168; Blood Cell:25; Intermediate Monocyte:1; Conventional DC 2:1; Neutrophil:1 | Monocyte:1196 | not_available:1196 |
| 6 | 1,187 | Classical Monocyte | True | 2.465 | 0.846 | pass | Classical Monocyte:1171; Non-Classical Monocyte:15; Conventional DC 2:1 | Classical Monocyte:960; Blood Cell:105; Intermediate Monocyte:59; Conventional DC 2:57; Plasmacytoid DC:6 | Monocyte:1185; DC:1; Non-Classical Monocyte:1 | not_available:1187 |
| 7 | 949 | Classical Monocyte | True | 2.283 | 0.836 | pass | Classical Monocyte:868; Non-Classical Monocyte:80; Conventional DC 2:1 | Classical Monocyte:597; Blood Cell:120; Conventional DC 2:113; Intermediate Monocyte:112; Plasmacytoid DC:5 | Monocyte:949 | not_available:949 |
| 8 | 919 | Classical Monocyte | True | 2.670 | 0.845 | pass | Classical Monocyte:915; Blood Cell:2; Non-Classical Monocyte:2 | Classical Monocyte:773; Blood Cell:124; Neutrophil:9; Conventional DC 2:8; Intermediate Monocyte:5 | Monocyte:915; RBC:2; Plasma Cell:1; Non-Classical Monocyte:1 | not_available:919 |
| 9 | 894 | Classical Monocyte | True | 2.358 | 0.836 | pass | Classical Monocyte:814; Non-Classical Monocyte:72; Blood Cell:6; Conventional DC 2:2 | Classical Monocyte:698; Blood Cell:87; Intermediate Monocyte:74; Conventional DC 2:29; Non-Classical Monocyte:6 | Monocyte:893; DC:1 | not_available:894 |

## Interpretation and caveats

この評価は ground truth label との accuracy ではなく、複数 annotation source と marker/subcluster evidence の整合性評価です。 Azimuth PBMC L3 の disagreement は、ontology 粒度の違い、gene availability、dataset enrichment の影響を含む可能性があります。

## Files

- Submission TSV: `submissions/infection_study_01_annotation.tsv`
- cellxgene H5AD: `cellxgene/infection_study_01.final_v13_recursive_screfmapping.cxg.h5ad`
- Report context JSON: `report_context.json`
- Tool support TSV: `tool_support_summary.tsv`
