# vaccination_study_06 annotation review

Updated: 2026-05-27 EDT

## Dataset-specific assessment

vaccination_study_06 は 57,419 cells / 11,878 portal genes の dataset です。親ラベルまたは Blood Cell に残った割合は 0.4%、doublet は 1,502 cells、低 confidence は 1,771 cells でした。注意すべき marker gene 欠損は Treg(warning: FOXP3); Plasma_ASC(warning: JCHAIN) です。 T/NK 優位で、gene space が小さいため fine label は marker availability と一緒に読む必要があります。 subcluster evidence では CD4 Naive / T Central Memory: 29,888 cells; NK Cell: 10,386 cells; CD8 Cytotoxic / T Effector Memory: 9,282 cells; Memory B Cell: 3,050 cells; MAIT Cell: 1,458 cells; CD8 Naive / T Central Memory: 873 cells が主要な構造です。全細胞に近い coverage で最も broad lineage に沿った source は Cluster consensus (broad concordance 95.0%) で、相対的に不一致が目立つ source は Azimuth PBMC L3 (15.4%) です。 screfmap は適用範囲を B/CD4T に限定すると coverage 56.4%、broad concordance 97.3% でした。

## Methods

この report は、portal input の raw/count-like gene space、CellTypist、Azimuth PBMC、Pan-human Azimuth、screfmap、marker score、lineage-specific subclustering を dataset 単位で照合したものです。ここでの tool concordance は ground truth accuracy ではなく、最終 annotation に対する support/disagreement の診断指標です。

## Input and QC

| cells | portal_genes | raw_count_source | count_like_fraction | available_marker_umap_genes | missing_marker_umap_genes | parent_or_blood_fraction | median_confidence | low_confidence_n | doublet_n |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 57,419 | 11,878 | layers[counts] | 1.000 | 28 | CD1C;CLEC10A;CLEC4C;CLEC9A;FCER1A;FCN1;FCRL5;FOXP3;IGHD;JCHAIN;LYZ;MS4A7;PF4;PPBP;S100A8;S100A9;SDC1;TNFRSF13B;VCAN;XCR1 | 0.004 | 0.820 | 1,771 | 1,502 |

### Marker gene availability alerts

| marker_set | n_genes_present | n_genes_expected | alert_level | missing_critical_markers |
| --- | --- | --- | --- | --- |
| Treg | 5 | 7 | warning | FOXP3 |
| Plasma_ASC | 4 | 9 | warning | JCHAIN |

### QC and annotation UMAPs

![Final labels](assets/umap_vaccination_study_06_v13_label.png)

![QC and confidence](assets/umap_vaccination_study_06_v13_qc_confidence.png)

![Lineage and annotation reason](assets/umap_vaccination_study_06_v13_lineage_reason.png)

## Marker expression UMAPs

### lineage_core

![lineage_core marker expression](assets/umap_vaccination_study_06_lineage_core_marker_expression.png)

### b_t_fine

![b_t_fine marker expression](assets/umap_vaccination_study_06_b_t_fine_marker_expression.png)

### myeloid_dc

![myeloid_dc marker expression](assets/umap_vaccination_study_06_myeloid_dc_marker_expression.png)

## Annotation source assessment

![Annotation source UMAPs](assets/umap_vaccination_study_06_annotation_source_labels.png)

![Tool concordance](assets/bar_vaccination_study_06_tool_concordance.png)

各 source は適用範囲が異なるため、coverage と concordance を分けて読んでください。screfmap は B/CD4T scoped cells だけで評価しています。

| tool | covered_n | coverage_fraction | exact_final_concordance | broad_final_concordance | top_supported_labels | top_disagreements |
| --- | --- | --- | --- | --- | --- | --- |
| CellTypist | 57,419 | 1.000 | 0.672 | 0.922 | CD4 Naive / T Central Memory: 22,002; CD8 Cytotoxic / T Effector Memory: 9,707; NK Cell: 8,926; CD4 T Effector Memory: 6,259; Blood Cell: 2,153 | CD4 Naive / T Central Memory vs CD4 T Effector Memory: 5,762; Memory B Cell vs B Cell: 1,502; NK Cell vs CD8 Cytotoxic / T Effector Memory: 1,475; CD4 Naive / T Central Memory vs Blood Cell: 1,048; CD4 Naive / T Central Memory vs CD8 Cytotoxic / T Effector Memory: 798 |
| Azimuth PBMC L2 | 57,419 | 1.000 | 0.597 | 0.944 | CD4 Naive / T Central Memory: 20,411; T Cell: 11,447; NK Cell: 9,324; CD8 Cytotoxic / T Effector Memory: 8,211; B Cell: 2,368 | CD4 Naive / T Central Memory vs T Cell: 10,401; Memory B Cell vs B Cell: 1,851; NK Cell vs CD8 Cytotoxic / T Effector Memory: 1,430; CD8 Cytotoxic / T Effector Memory vs T Cell: 872; CD8 Cytotoxic / T Effector Memory vs CD4 Naive / T Central Memory: 814 |
| Azimuth PBMC L3 | 57,419 | 1.000 | 0.099 | 0.154 | Blood Cell: 48,850; CD4 Naive / T Central Memory: 4,203; MAIT Cell: 1,596; RBC: 749; CD8 Naive / T Central Memory: 656 | CD4 Naive / T Central Memory vs Blood Cell: 24,697; NK Cell vs Blood Cell: 10,158; CD8 Cytotoxic / T Effector Memory vs Blood Cell: 8,411; Memory B Cell vs Blood Cell: 2,714; Doublet vs Blood Cell: 1,329 |
| Pan-human Azimuth fine | 57,419 | 1.000 | 0.432 | 0.757 | Blood Cell: 13,263; CD4 Naive / T Central Memory: 10,554; NK Cell: 6,730; CD4 T Cell (ab): 6,257; CD8 Cytotoxic / T Effector Memory: 5,409 | CD4 Naive / T Central Memory vs Blood Cell: 5,766; CD4 Naive / T Central Memory vs CD4 T Cell (ab): 5,381; CD4 Naive / T Central Memory vs Treg: 4,267; CD4 Naive / T Central Memory vs CD4 T Effector Memory: 3,980; NK Cell vs Blood Cell: 3,389 |
| Pan-human Azimuth medium | 57,419 | 1.000 | 0.114 | 0.808 | T Cell: 36,741; Blood Cell: 10,254; NK Cell: 6,731; B Cell: 3,670; Monocyte: 14 | CD4 Naive / T Central Memory vs T Cell: 25,221; CD8 Cytotoxic / T Effector Memory vs T Cell: 6,881; CD4 Naive / T Central Memory vs Blood Cell: 4,620; Memory B Cell vs B Cell: 2,916; CD8 Cytotoxic / T Effector Memory vs Blood Cell: 2,221 |
| Cluster consensus | 57,419 | 1.000 | 0.861 | 0.950 | CD4 Naive / T Central Memory: 29,353; NK Cell: 10,608; CD8 Cytotoxic / T Effector Memory: 9,819; B Cell: 3,826; Blood Cell: 1,548 | Memory B Cell vs B Cell: 2,885; CD4 Naive / T Central Memory vs Blood Cell: 999; Naive B Cell vs B Cell: 603; Doublet vs CD4 Naive / T Central Memory: 505; NK Cell vs CD8 Cytotoxic / T Effector Memory: 419 |
| Marker score | 57,419 | 1.000 | 0.175 | 0.858 | CD4 T Cell (ab): 21,811; NK Cell: 14,769; T Cell: 8,430; CD8 T Cell (ab): 4,210; DC: 2,628 | CD4 Naive / T Central Memory vs CD4 T Cell (ab): 18,974; CD4 Naive / T Central Memory vs T Cell: 6,189; CD8 Cytotoxic / T Effector Memory vs NK Cell: 3,387; CD8 Cytotoxic / T Effector Memory vs CD8 T Cell (ab): 2,940; Memory B Cell vs DC: 1,759 |
| screfmap scoped | 32,412 | 0.564 | 0.793 | 0.973 | CD4 Naive / T Central Memory: 24,886; CD4 T Effector Memory: 2,831; Naive B Cell: 2,121; Memory B Cell: 1,413; Treg: 900 | CD4 Naive / T Central Memory vs CD4 T Effector Memory: 1,581; Memory B Cell vs Naive B Cell: 1,435; CD8 Cytotoxic / T Effector Memory vs CD4 T Effector Memory: 1,009; CD4 Naive / T Central Memory vs Treg: 820; CD8 Naive / T Central Memory vs CD4 Naive / T Central Memory: 432 |

### Lineage-scoped source support

| final_broad_lineage | tool | covered_n | exact_final_concordance | broad_final_concordance |
| --- | --- | --- | --- | --- |
| B | CellTypist | 3,667 | 0.341 | 0.938 |
| B | Azimuth PBMC L2 | 3,667 | 0.054 | 0.756 |
| B | Azimuth PBMC L3 | 3,667 | 0.000 | 0.058 |
| B | Pan-human Azimuth fine | 3,667 | 0.787 | 0.960 |
| B | Pan-human Azimuth medium | 3,667 | 0.003 | 0.955 |
| B | Cluster consensus | 3,667 | 0.004 | 0.955 |
| B | Marker score | 3,667 | 0.001 | 0.366 |
| B | screfmap scoped | 3,592 | 0.528 | 0.998 |
| T/NK | CellTypist | 51,894 | 0.718 | 0.952 |
| T/NK | Azimuth PBMC L2 | 51,894 | 0.656 | 0.987 |
| T/NK | Azimuth PBMC L3 | 51,894 | 0.107 | 0.134 |
| T/NK | Pan-human Azimuth fine | 51,894 | 0.419 | 0.759 |
| T/NK | Pan-human Azimuth medium | 51,894 | 0.123 | 0.816 |
| T/NK | Cluster consensus | 51,894 | 0.950 | 0.978 |
| T/NK | Marker score | 51,894 | 0.193 | 0.921 |
| T/NK | screfmap scoped | 27,969 | 0.851 | 0.999 |
| Myeloid/DC | CellTypist | 138 | 0.043 | 0.080 |
| Myeloid/DC | Azimuth PBMC L2 | 138 | 0.312 | 0.486 |
| Myeloid/DC | Azimuth PBMC L3 | 138 | 0.297 | 0.464 |
| Myeloid/DC | Pan-human Azimuth fine | 138 | 0.080 | 0.094 |

## Lineage-specific subclustering

### B_lineage

![B_lineage subcluster labels](assets/umap_vaccination_study_06_B_lineage_v13_subcluster_label.png)

![B_lineage subcluster QC](assets/umap_vaccination_study_06_B_lineage_v13_subcluster_qc.png)

| cluster | n_cells | chosen_label | accepted | score_margin | calibrated_cluster_confidence | marker_availability_alert | top_celltypist | top_panhuman_fine | top_marker | top_screfmapping |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 339 | Memory B Cell | True | 1.211 | 0.717 | pass | Memory B Cell:158; Naive B Cell:99; B Cell:41; Plasma Cell:13; CD8 Cytotoxic / T Effector Memory:12 | Memory B Cell:328; Blood Cell:6; Plasma Cell:2; CD4 T Cell (ab):1; B Cell:1 | DC:240; B Cell:59; Monocyte:22; Plasmacytoid DC:13; Plasma Cell:4 | Naive B Cell:202; Memory B Cell:78; Plasma Cell:56; not_available:2; CD4 Naive / T Central Memory:1 |
| 1 | 327 | Memory B Cell | True | 1.134 | 0.789 | pass | Memory B Cell:167; Naive B Cell:108; B Cell:42; CD8 Cytotoxic / T Effector Memory:4; Blood Cell:3 | Memory B Cell:327 | DC:216; B Cell:95; Plasma Cell:12; Plasmacytoid DC:3; Monocyte:1 | Naive B Cell:213; Memory B Cell:108; Plasma Cell:4; not_available:2 |
| 2 | 268 | Memory B Cell | True | 1.016 | 0.719 | pass | B Cell:97; Naive B Cell:85; Memory B Cell:66; Blood Cell:9; Plasma Cell:7 | Memory B Cell:268 | DC:220; B Cell:47; Plasma Cell:1 | Plasma Cell:103; Naive B Cell:94; Memory B Cell:64; not_available:7 |
| 3 | 263 | Naive B Cell | True | 0.580 | 0.785 | pass | B Cell:133; Naive B Cell:102; Blood Cell:24; Memory B Cell:3; CD8 Cytotoxic / T Effector Memory:1 | Memory B Cell:260; Blood Cell:3 | B Cell:115; Monocyte:104; DC:42; Plasma Cell:1; Plasmacytoid DC:1 | Naive B Cell:261; Plasma Cell:1; Memory B Cell:1 |
| 4 | 257 | Memory B Cell | True | 2.971 | 0.827 | pass | B Cell:176; Memory B Cell:66; Blood Cell:10; Naive B Cell:5 | Memory B Cell:257 | DC:177; B Cell:69; Monocyte:10; Plasmacytoid DC:1 | Memory B Cell:148; Naive B Cell:100; not_available:5; Plasma Cell:4 |
| 5 | 244 | Memory B Cell | True | 2.643 | 0.770 | pass | B Cell:226; Blood Cell:17; Memory B Cell:1 | Memory B Cell:244 | DC:226; B Cell:13; Monocyte:3; Plasma Cell:2 | Memory B Cell:127; Naive B Cell:85; Plasma Cell:19; not_available:13 |
| 6 | 243 | Memory B Cell | True | 3.604 | 0.846 | pass | Memory B Cell:195; B Cell:46; Naive B Cell:2 | Memory B Cell:243 | B Cell:189; DC:50; Monocyte:2; Plasma Cell:1; Plasmacytoid DC:1 | Memory B Cell:191; Naive B Cell:51; Plasma Cell:1 |
| 7 | 226 | Naive B Cell | True | 0.079 | 0.647 | pass | Naive B Cell:99; B Cell:93; Blood Cell:9; CD4 Naive / T Central Memory:6; Memory B Cell:5 | Memory B Cell:198; Blood Cell:18; B Cell:7; Naive B Cell:2; Plasma Cell:1 | Monocyte:97; B Cell:79; DC:27; Plasmacytoid DC:13; NK Cell:5 | Naive B Cell:217; not_available:5; Memory B Cell:4 |
| 8 | 209 | Memory B Cell | True | 3.204 | 0.830 | pass | B Cell:198; Memory B Cell:11 | Memory B Cell:208; Blood Cell:1 | DC:136; B Cell:71; Plasma Cell:1; Monocyte:1 | Memory B Cell:135; Naive B Cell:66; Plasma Cell:8 |
| 9 | 194 | Memory B Cell | True | 1.982 | 0.737 | pass | B Cell:164; Memory B Cell:10; Naive B Cell:7; Blood Cell:5; CD8 Cytotoxic / T Effector Memory:3 | Memory B Cell:177; Blood Cell:10; Plasma Cell:5; B Cell:2 | DC:127; B Cell:34; Monocyte:24; Plasma Cell:6; CD4 T Cell (ab):1 | Naive B Cell:109; Memory B Cell:66; Plasma Cell:15; not_available:4 |

### T_NK_lineage

![T_NK_lineage subcluster labels](assets/umap_vaccination_study_06_T_NK_lineage_v13_subcluster_label.png)

![T_NK_lineage subcluster QC](assets/umap_vaccination_study_06_T_NK_lineage_v13_subcluster_qc.png)

| cluster | n_cells | chosen_label | accepted | score_margin | calibrated_cluster_confidence | marker_availability_alert | top_celltypist | top_panhuman_fine | top_marker | top_screfmapping |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 3,594 | NK Cell | True | 2.354 | 0.850 | pass | NK Cell:3187; CD8 Cytotoxic / T Effector Memory:319; Blood Cell:65; CD4 T Effector Memory:11; CD4 Naive / T Central Memory:3 | NK Cell:2776; Blood Cell:757; CD8 Cytotoxic / T Effector Memory:46; CD8 T Cell (ab):6; CD4 T Cell (ab):3 | NK Cell:3583; T Cell:6; CD8 T Cell (ab):4; Monocyte:1 | not_available:3594 |
| 1 | 3,197 | CD4 Naive / T Central Memory | True | 0.322 | 0.742 | pass | CD4 T Effector Memory:2699; CD8 Cytotoxic / T Effector Memory:163; CD4 Naive / T Central Memory:123; Blood Cell:110; Treg:59 | CD4 T Cell (ab):1698; CD4 T Effector Memory:873; Treg:326; Blood Cell:259; CD8 Cytotoxic / T Effector Memory:24 | CD4 T Cell (ab):2314; T Cell:663; CD8 T Cell (ab):198; NK Cell:14; Plasma Cell:4 | CD4 Naive / T Central Memory:2065; not_available:562; CD4 T Effector Memory:495; Treg:75 |
| 2 | 3,126 | CD4 Naive / T Central Memory | True | 3.496 | 0.822 | pass | CD4 Naive / T Central Memory:2939; Blood Cell:37; CD4 T Effector Memory:34; CD8 Cytotoxic / T Effector Memory:32; CD8 Naive / T Central Memory:28 | CD4 Naive / T Central Memory:1608; Blood Cell:847; Treg:289; CD4 T Cell (ab):222; CD4 T Effector Memory:119 | CD4 T Cell (ab):1689; T Cell:492; Plasmacytoid DC:213; Monocyte:191; NK Cell:166 | CD4 Naive / T Central Memory:2503; not_available:543; CD4 T Effector Memory:49; Treg:31 |
| 3 | 2,918 | CD8 Cytotoxic / T Effector Memory | True | 2.071 | 0.740 | pass | CD8 Cytotoxic / T Effector Memory:2726; CD4 T Effector Memory:56; ydT Cell:49; NK Cell:29; Blood Cell:27 | CD8 Cytotoxic / T Effector Memory:2067; Blood Cell:539; CD8 T Cell (ab):89; CD4 T Cell (ab):69; ydT Cell:64 | CD8 T Cell (ab):1544; NK Cell:823; T Cell:433; CD4 T Cell (ab):117; Plasma Cell:1 | not_available:2827; CD4 T Effector Memory:83; CD4 Naive / T Central Memory:8 |
| 4 | 2,874 | CD4 Naive / T Central Memory | True | 1.618 | 0.800 | pass | CD4 Naive / T Central Memory:1507; CD4 T Effector Memory:553; CD8 Cytotoxic / T Effector Memory:245; Blood Cell:235; Treg:142 | Blood Cell:724; CD4 T Effector Memory:711; Treg:644; CD4 T Cell (ab):510; CD4 Naive / T Central Memory:246 | CD4 T Cell (ab):1790; T Cell:259; Monocyte:223; Plasmacytoid DC:140; Plasma Cell:132 | CD4 Naive / T Central Memory:1670; CD4 T Effector Memory:595; not_available:453; Treg:155; Plasma Cell:1 |
| 5 | 2,831 | CD8 Cytotoxic / T Effector Memory | True | 1.314 | 0.727 | pass | CD8 Cytotoxic / T Effector Memory:2151; NK Cell:244; CD4 Naive / T Central Memory:137; Blood Cell:115; ydT Cell:85 | CD8 Cytotoxic / T Effector Memory:1325; Blood Cell:1090; NK Cell:106; ydT Cell:90; CD8 T Cell (ab):46 | NK Cell:1595; CD8 T Cell (ab):505; CD4 T Cell (ab):255; T Cell:249; Monocyte:95 | not_available:2615; CD4 T Effector Memory:204; CD4 Naive / T Central Memory:11; Treg:1 |
| 6 | 2,822 | CD4 Naive / T Central Memory | True | 3.811 | 0.850 | pass | CD4 Naive / T Central Memory:2746; CD4 T Effector Memory:50; Treg:11; CD8 Naive / T Central Memory:7; Blood Cell:4 | CD4 Naive / T Central Memory:1735; Blood Cell:699; Treg:203; CD4 T Effector Memory:102; CD4 T Cell (ab):82 | CD4 T Cell (ab):1923; T Cell:892; NK Cell:3; Monocyte:2; Plasmacytoid DC:1 | CD4 Naive / T Central Memory:2768; not_available:30; Treg:20; CD4 T Effector Memory:4 |
| 7 | 2,797 | CD4 Naive / T Central Memory | True | 1.984 | 0.835 | pass | CD4 Naive / T Central Memory:1298; CD4 T Effector Memory:1214; Treg:170; Blood Cell:61; CD8 Cytotoxic / T Effector Memory:34 | CD4 T Cell (ab):885; CD4 T Effector Memory:784; Treg:596; CD4 Naive / T Central Memory:287; Blood Cell:244 | CD4 T Cell (ab):2046; T Cell:742; CD8 T Cell (ab):4; Monocyte:2; Plasmacytoid DC:1 | CD4 Naive / T Central Memory:2497; Treg:171; CD4 T Effector Memory:67; not_available:62 |
| 8 | 2,750 | NK Cell | True | 1.793 | 0.734 | pass | NK Cell:2142; CD8 Cytotoxic / T Effector Memory:286; Blood Cell:121; Plasma Cell:72; CD4 Naive / T Central Memory:58 | Blood Cell:1511; NK Cell:1050; CD8 Cytotoxic / T Effector Memory:105; CD8 T Cell (ab):26; ydT Cell:20 | NK Cell:2581; Plasmacytoid DC:48; DC:29; Monocyte:28; Plasma Cell:24 | not_available:2725; CD4 T Effector Memory:22; CD4 Naive / T Central Memory:3 |
| 9 | 2,733 | CD4 Naive / T Central Memory | True | 3.776 | 0.850 | pass | CD4 Naive / T Central Memory:2670; CD4 T Effector Memory:26; CD8 Naive / T Central Memory:22; Blood Cell:6; Treg:4 | CD4 Naive / T Central Memory:2040; Blood Cell:307; Treg:174; CD4 T Effector Memory:106; CD4 T Cell (ab):89 | CD4 T Cell (ab):1900; T Cell:826; CD8 T Cell (ab):3; Monocyte:2; Plasmacytoid DC:1 | CD4 Naive / T Central Memory:2678; not_available:45; Treg:6; CD4 T Effector Memory:4 |

### Myeloid_lineage

![Myeloid_lineage subcluster labels](assets/umap_vaccination_study_06_Myeloid_lineage_v13_subcluster_label.png)

![Myeloid_lineage subcluster QC](assets/umap_vaccination_study_06_Myeloid_lineage_v13_subcluster_qc.png)

| cluster | n_cells | chosen_label | accepted | score_margin | calibrated_cluster_confidence | marker_availability_alert | top_celltypist | top_panhuman_fine | top_marker | top_screfmapping |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 18 | Plasmacytoid DC | True | 0.888 | 0.663 | pass | CD4 Naive / T Central Memory:6; Memory B Cell:6; Blood Cell:1; CD8 Cytotoxic / T Effector Memory:1; Naive B Cell:1 | Blood Cell:15; B Cell:1; T Cell:1; Memory B Cell:1 | DC:7; Plasmacytoid DC:6; Monocyte:5 | not_available:7; CD4 Naive / T Central Memory:6; Treg:2; CD4 T Effector Memory:1; Naive B Cell:1 |
| 1 | 18 | Intermediate Monocyte | True | 0.610 | 0.824 | pass | Blood Cell:17; Plasma Cell:1 | Intermediate Monocyte:11; Blood Cell:6; Classical Monocyte:1 | DC:10; Monocyte:7; Plasmacytoid DC:1 | not_available:18 |
| 2 | 18 | Plasmacytoid DC | True | 0.952 | 0.697 | pass | Blood Cell:6; B Cell:6; CD4 Naive / T Central Memory:2; NK Cell:2; Naive B Cell:1 | Blood Cell:12; Memory B Cell:5; Plasma Cell:1 | Monocyte:13; DC:3; Plasmacytoid DC:1; CD8 T Cell (ab):1 | not_available:14; Naive B Cell:4 |
| 3 | 15 | Plasmacytoid DC | True | 2.442 | 0.699 | pass | B Cell:5; NK Cell:3; CD4 Naive / T Central Memory:2; Naive B Cell:2; CD8 Cytotoxic / T Effector Memory:1 | Blood Cell:13; Platelet:1; Plasma Cell:1 | Monocyte:12; DC:1; Plasmacytoid DC:1; Plasma Cell:1 | not_available:14; Naive B Cell:1 |
| 4 | 15 | Myeloid Cell | False | 0.007 | 0.362 | pass | Blood Cell:7; CD4 Naive / T Central Memory:5; Plasma Cell:1; B Cell:1; T Cell:1 | Blood Cell:15 | Monocyte:9; Plasmacytoid DC:3; DC:3 | not_available:9; CD4 T Effector Memory:2; Treg:2; CD4 Naive / T Central Memory:2 |
| 5 | 12 | Myeloid Cell | False | 0.450 | 0.476 | pass | CD4 Naive / T Central Memory:4; Memory B Cell:2; Myeloid Cell:2; Blood Cell:1; Plasma Cell:1 | Blood Cell:11; Platelet:1 | Monocyte:6; DC:5; Plasmacytoid DC:1 | not_available:5; CD4 Naive / T Central Memory:3; Naive B Cell:2; Treg:1; Memory B Cell:1 |
| 6 | 10 | Conventional DC 2 | True | 0.365 | 0.565 | pass | Blood Cell:4; Conventional DC 2:3; CD4 Naive / T Central Memory:1; Memory B Cell:1; Classical Monocyte:1 | Blood Cell:6; Memory B Cell:3; CD4 T Cell (ab):1 | DC:8; Monocyte:2 | not_available:7; CD4 Naive / T Central Memory:2; Memory B Cell:1 |
| 7 | 10 | Plasmacytoid DC | True | 1.403 | 0.666 | pass | Blood Cell:3; Memory B Cell:3; CD4 Naive / T Central Memory:1; Plasma Cell:1; B Cell:1 | Blood Cell:9; CD4 T Cell (ab):1 | Monocyte:5; Plasmacytoid DC:3; DC:2 | not_available:6; Memory B Cell:3; CD4 Naive / T Central Memory:1 |
| 8 | 9 | Classical Monocyte | True | 0.119 | 0.484 | pass | Blood Cell:6; CD4 Naive / T Central Memory:2; CD8 Cytotoxic / T Effector Memory:1 | Blood Cell:8; Intermediate Monocyte:1 | Monocyte:5; DC:3; Plasma Cell:1 | not_available:7; CD4 Naive / T Central Memory:2 |
| 9 | 7 | Plasmacytoid DC | True | 0.439 | 0.546 | pass | CD4 Naive / T Central Memory:3; Blood Cell:2; Memory B Cell:1; NK Cell:1 | Blood Cell:6; Memory B Cell:1 | Monocyte:5; DC:1; Plasmacytoid DC:1 | not_available:4; Naive B Cell:1; CD4 T Effector Memory:1; CD4 Naive / T Central Memory:1 |

## Interpretation and caveats

この評価は ground truth label との accuracy ではなく、複数 annotation source と marker/subcluster evidence の整合性評価です。 marker gene が欠損している cell type では、reference mapping 単独の fine label は過信しない設計です。 Azimuth PBMC L3 の disagreement は、ontology 粒度の違い、gene availability、dataset enrichment の影響を含む可能性があります。 whole PBMC と仮定した解釈より、dataset-specific enrichment と QC structure を優先して読むべきです。

## Files

- Submission TSV: `submissions/vaccination_study_06_annotation.tsv`
- cellxgene H5AD: `cellxgene/vaccination_study_06.final_v13_recursive_screfmapping.cxg.h5ad`
- Report context JSON: `report_context.json`
- Tool support TSV: `tool_support_summary.tsv`
