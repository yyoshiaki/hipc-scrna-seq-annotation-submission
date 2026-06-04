# HIPC データセットアノテーションレポート: vaccination_study_09

更新日: 2026-06-04 EDT

このレポートは `hipc-annotation` Codex workflow によって生成したデータセット別レビュー文書です。固定 method は repository README に置き、このレポートでは実際の evidence、弱い箇所、レビュー優先度、UMAP / dotplot を確認します。

## データセット概要

| study | cells | analysis_X_genes | pre_hvg_genes | counts_layer_genes | labels | parent_or_blood_fraction | Blood Cell | Doublet | artifact_like | median_confidence | low_confidence | source_disagreement | invalid_labels |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| vaccination_study_09 | 139,960 | 19,141 | 19,141 | 19,141 | 19 | 0.013 | 1,796 | 579 | 101 | 0.734 | 19,477 | 19,969 (0.143) | none |

## 実行概要

- 実行単位: one dataset in, one annotated dataset out。
- 実行経路: Codex skill `hipc-annotation` -> bundled helper `run_one.sh` -> annotation CLI -> validator -> report inspection。
- 検証: submission row count、H5AD observation count、official label validity、H5AD/submission agreement、confidence column、report image link を確認する。
- このレポートは workflow の再掲ではなく、このデータセットの marker 欠損、UMAP、label 構成、review concern を読むためのもの。

## データセット固有の解釈

- `vaccination_study_09`: 139,960 cells、analysis X/var 19,141 genes、pre-HVG slot 19,141 genes、submitted label 19 種、parent/Blood residual fraction 0.013、median confidence 0.734。
  - 19,477 cells は low confidence。QC / confidence UMAP 上で局在を確認する。
  - 579 cells は `Doublet` として提出。mixed-lineage marker expression と scrublet support を確認する。
  - 1,796 cells は `Blood Cell` として残存。これは filter-out ではなく、曖昧な細胞を公式 parent label で残したもの。
  - Marker gene 欠損アラート: Plasma_ASC。該当 marker set に依存する fine label は慎重に見る。

## データセット固有の評価

- 全体像: 139,960 cells / analysis X/var 19,141 genes / pre-HVG slot 19,141 genes。parent/Blood residual は 0.013、low-confidence は 19,477 cells、source disagreement flag は 19,969 cells (0.143)。
- 優先確認: low-confidence 領域が QC UMAP と source-disagreement UMAP で同じ場所に集まるかを確認する。
- 優先確認: `Blood Cell` 残存が孤立 cluster なのか、複数 lineage に分散した曖昧領域なのかを UMAP で確認する。
- Marker gene 欠損: Plasma_ASC は confidence cap 対象。該当 label は marker expression UMAP と dotplot で妥当性を確認する。

## Marker Gene 欠損アラート

| study | marker_set | alert | present_fraction | missing_critical_markers | missing_genes |
| --- | --- | --- | --- | --- | --- |
| vaccination_study_09 | Plasma_ASC | warning | 0.667 | JCHAIN | JCHAIN;IGHG1;IGHA1 |

## ソース間不一致

| study | predicted_cell_type | cells | median_source_agreement | disagreement_cells | disagreement_fraction |
| --- | --- | --- | --- | --- | --- |
| vaccination_study_09 | Doublet | 579 | 0.000 | 579 | 1.000 |
| vaccination_study_09 | T Cell | 7 | 0.333 | 7 | 1.000 |
| vaccination_study_09 | Plasma Cell | 719 | 0.250 | 558 | 0.776 |
| vaccination_study_09 | CD8 Naive / T Central Memory | 11,344 | 0.667 | 5,151 | 0.454 |
| vaccination_study_09 | Treg | 2,389 | 0.500 | 875 | 0.366 |
| vaccination_study_09 | CD8 Cytotoxic / T Effector Memory | 15,756 | 0.667 | 4,249 | 0.270 |
| vaccination_study_09 | Classical Monocyte | 25,131 | 1.000 | 4,379 | 0.174 |
| vaccination_study_09 | Blood Cell | 1,796 | 1.000 | 214 | 0.119 |
| vaccination_study_09 | MAIT Cell | 3,819 | 0.667 | 381 | 0.100 |
| vaccination_study_09 | NK Cell | 9,895 | 1.000 | 698 | 0.071 |
| vaccination_study_09 | Non-Classical Monocyte | 4,023 | 1.000 | 272 | 0.068 |
| vaccination_study_09 | Naive B Cell | 11,136 | 0.750 | 611 | 0.055 |

## レビュー優先事項

| study | concern | cells |
| --- | --- | --- |
| vaccination_study_09 | High source disagreement for Doublet | 579 |
| vaccination_study_09 | High source disagreement for Plasma Cell | 558 |
| vaccination_study_09 | High source disagreement for T Cell | 7 |
| vaccination_study_09 | warning marker availability for Plasma_ASC | 719 |
| vaccination_study_09 | Large Blood Cell/ambiguous residual remains | 1,796 |
| vaccination_study_09 | Many low-confidence cells; QC or mixed-marker effects likely remain | 19,477 |

## ラベル構成

| study | predicted_cell_type | cells |
| --- | --- | --- |
| vaccination_study_09 | CD4 Naive / T Central Memory | 47,034 |
| vaccination_study_09 | Classical Monocyte | 25,131 |
| vaccination_study_09 | CD8 Cytotoxic / T Effector Memory | 15,756 |
| vaccination_study_09 | CD8 Naive / T Central Memory | 11,344 |
| vaccination_study_09 | Naive B Cell | 11,136 |
| vaccination_study_09 | NK Cell | 9,895 |
| vaccination_study_09 | Memory B Cell | 4,090 |
| vaccination_study_09 | Non-Classical Monocyte | 4,023 |
| vaccination_study_09 | MAIT Cell | 3,819 |
| vaccination_study_09 | Treg | 2,389 |
| vaccination_study_09 | Blood Cell | 1,796 |
| vaccination_study_09 | Conventional DC 2 | 1,292 |
| vaccination_study_09 | Plasmacytoid DC | 801 |
| vaccination_study_09 | Plasma Cell | 719 |
| vaccination_study_09 | Doublet | 579 |
| vaccination_study_09 | Platelet | 86 |
| vaccination_study_09 | Conventional DC 1 | 48 |
| vaccination_study_09 | HSC | 15 |
| vaccination_study_09 | T Cell | 7 |

## Inline Figures

### vaccination_study_09

![vaccination_study_09 final labels](assets/umap_vaccination_study_09_annotation_label.png)

![vaccination_study_09 lineage and annotation reason](assets/umap_vaccination_study_09_annotation_lineage_reason.png)

![vaccination_study_09 QC and confidence](assets/umap_vaccination_study_09_annotation_qc_confidence.png)

![vaccination_study_09 source agreement and disagreement](assets/umap_vaccination_study_09_annotation_source_disagreement.png)

![vaccination_study_09 marker expression UMAPs](assets/umap_vaccination_study_09_annotation_marker_expression.png)

![vaccination_study_09 submitted-label marker dotplot](assets/dotplot_vaccination_study_09_annotation_marker_dotplot.png)

#### vaccination_study_09 B_lineage true subcluster UMAP

![vaccination_study_09 B_lineage true subcluster labels](assets/umap_vaccination_study_09_B_lineage_true_subcluster_label.png)

![vaccination_study_09 B_lineage true subcluster source labels](assets/umap_vaccination_study_09_B_lineage_true_subcluster_source_labels.png)

![vaccination_study_09 B_lineage true subcluster QC](assets/umap_vaccination_study_09_B_lineage_true_subcluster_qc.png)

![vaccination_study_09 B_lineage true subcluster marker scores](assets/umap_vaccination_study_09_B_lineage_true_subcluster_marker_scores.png)

![vaccination_study_09 B_lineage true subcluster marker expression](assets/umap_vaccination_study_09_B_lineage_true_subcluster_marker_expression.png)

![vaccination_study_09 B_lineage subcluster marker score heatmap](assets/subcluster_marker_score_heatmap_vaccination_study_09_B_lineage.png)

![vaccination_study_09 B_lineage subcluster marker dotplot](assets/dotplot_vaccination_study_09_B_lineage_true_subcluster_marker_dotplot.png)

Tables: `tables/vaccination_study_09_B_lineage_true_subcluster_umap.tsv.gz`, `tables/vaccination_study_09_B_lineage_subcluster_candidate_scores.tsv`.

#### vaccination_study_09 T_NK_lineage true subcluster UMAP

![vaccination_study_09 T_NK_lineage true subcluster labels](assets/umap_vaccination_study_09_T_NK_lineage_true_subcluster_label.png)

![vaccination_study_09 T_NK_lineage true subcluster source labels](assets/umap_vaccination_study_09_T_NK_lineage_true_subcluster_source_labels.png)

![vaccination_study_09 T_NK_lineage true subcluster QC](assets/umap_vaccination_study_09_T_NK_lineage_true_subcluster_qc.png)

![vaccination_study_09 T_NK_lineage true subcluster marker scores](assets/umap_vaccination_study_09_T_NK_lineage_true_subcluster_marker_scores.png)

![vaccination_study_09 T_NK_lineage true subcluster marker expression](assets/umap_vaccination_study_09_T_NK_lineage_true_subcluster_marker_expression.png)

![vaccination_study_09 T_NK_lineage subcluster marker score heatmap](assets/subcluster_marker_score_heatmap_vaccination_study_09_T_NK_lineage.png)

![vaccination_study_09 T_NK_lineage subcluster marker dotplot](assets/dotplot_vaccination_study_09_T_NK_lineage_true_subcluster_marker_dotplot.png)

Tables: `tables/vaccination_study_09_T_NK_lineage_true_subcluster_umap.tsv.gz`, `tables/vaccination_study_09_T_NK_lineage_subcluster_candidate_scores.tsv`.

#### vaccination_study_09 Myeloid_lineage true subcluster UMAP

![vaccination_study_09 Myeloid_lineage true subcluster labels](assets/umap_vaccination_study_09_Myeloid_lineage_true_subcluster_label.png)

![vaccination_study_09 Myeloid_lineage true subcluster source labels](assets/umap_vaccination_study_09_Myeloid_lineage_true_subcluster_source_labels.png)

![vaccination_study_09 Myeloid_lineage true subcluster QC](assets/umap_vaccination_study_09_Myeloid_lineage_true_subcluster_qc.png)

![vaccination_study_09 Myeloid_lineage true subcluster marker scores](assets/umap_vaccination_study_09_Myeloid_lineage_true_subcluster_marker_scores.png)

![vaccination_study_09 Myeloid_lineage true subcluster marker expression](assets/umap_vaccination_study_09_Myeloid_lineage_true_subcluster_marker_expression.png)

![vaccination_study_09 Myeloid_lineage subcluster marker score heatmap](assets/subcluster_marker_score_heatmap_vaccination_study_09_Myeloid_lineage.png)

![vaccination_study_09 Myeloid_lineage subcluster marker dotplot](assets/dotplot_vaccination_study_09_Myeloid_lineage_true_subcluster_marker_dotplot.png)

Tables: `tables/vaccination_study_09_Myeloid_lineage_true_subcluster_umap.tsv.gz`, `tables/vaccination_study_09_Myeloid_lineage_subcluster_candidate_scores.tsv`.


## Subcluster Marker Score Review

上の lineage-specific panel は、各 lineage subset で HVG 選択、PCA、neighbors、Leiden、UMAP を再計算した true local subcluster analysis から生成しています。Marker gene による fine label の確認は global UMAP だけではなく、この local UMAP、CellTypist/Azimuth/Pan-human/cluster-level marker gene assignment overlay、cluster marker gate score UMAP、marker-expression UMAP、dotplot を主に見ます。Treg など sparse marker label は cell-wise marker winner ではなく、local cluster の FOXP3/IL2RA/CTLA4 など key-marker support と reference support で判定します。

## Marker Assignment Feedback

Marker gene assignment は final label を強制的に上書きするものではなく、cluster-level の自己点検です。この表は marker-only assignment と final/reference-driven label がずれる cluster、marker specificity が弱い cluster、scRefMap が期待される lineage で欠落する cluster を示します。`marker_score` は raw marker base score から negative/confound marker penalty を差し引いた cluster-level marker gate score です。

| study | lineage | cluster | cells | chosen_label | marker_assignment | marker_score | base_score | penalty | flags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| vaccination_study_09 | T_NK_lineage | 1 | 6,386 | NK Cell | NK Cell | 0.842 | 1.000 | 0.158 | screfmapping_missing_for_scope |
| vaccination_study_09 | T_NK_lineage | 3 | 5,941 | CD4 Naive / T Central Memory | ydT Cell | 0.706 | 0.808 | 0.102 | marker_final_disagreement |
| vaccination_study_09 | T_NK_lineage | 5 | 5,252 | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | 0.652 | 1.000 | 0.348 | screfmapping_missing_for_scope |
| vaccination_study_09 | T_NK_lineage | 6 | 4,889 | CD8 Naive / T Central Memory | CD8 Naive / T Central Memory | 0.900 | 0.973 | 0.073 | screfmapping_missing_for_scope |
| vaccination_study_09 | T_NK_lineage | 8 | 4,705 | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | 0.719 | 1.000 | 0.281 | screfmapping_missing_for_scope |
| vaccination_study_09 | T_NK_lineage | 10 | 3,848 | CD4 Naive / T Central Memory | MAIT Cell | 0.744 | 0.898 | 0.154 | marker_final_disagreement |
| vaccination_study_09 | T_NK_lineage | 11 | 3,819 | MAIT Cell | CD8 Cytotoxic / T Effector Memory | 0.834 | 1.000 | 0.166 | marker_final_disagreement;screfmapping_missing_for_scope |
| vaccination_study_09 | T_NK_lineage | 12 | 3,633 | CD4 Naive / T Central Memory | ydT Cell | 0.635 | 0.854 | 0.219 | marker_final_disagreement |
| vaccination_study_09 | T_NK_lineage | 13 | 3,044 | CD4 Naive / T Central Memory | ydT Cell | 0.657 | 0.808 | 0.151 | marker_final_disagreement |
| vaccination_study_09 | Myeloid_lineage | 0 | 2,880 | Classical Monocyte | Intermediate Monocyte | 0.682 | 1.000 | 0.318 | marker_final_disagreement |
| vaccination_study_09 | T_NK_lineage | 15 | 2,733 | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | 0.650 | 1.000 | 0.350 | screfmapping_missing_for_scope |
| vaccination_study_09 | Myeloid_lineage | 1 | 2,676 | Non-Classical Monocyte | Intermediate Monocyte | 0.536 | 1.000 | 0.464 | marker_final_disagreement |
| vaccination_study_09 | T_NK_lineage | 16 | 2,666 | NK Cell | NK Cell | 0.814 | 1.000 | 0.186 | screfmapping_missing_for_scope |
| vaccination_study_09 | Myeloid_lineage | 2 | 2,657 | Classical Monocyte | Intermediate Monocyte | 0.591 | 1.000 | 0.409 | marker_final_disagreement |
| vaccination_study_09 | T_NK_lineage | 17 | 2,396 | CD8 Naive / T Central Memory | CD8 Naive / T Central Memory | 0.864 | 1.000 | 0.136 | screfmapping_missing_for_scope |
| vaccination_study_09 | T_NK_lineage | 19 | 2,386 | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | 0.854 | 1.000 | 0.146 | screfmapping_missing_for_scope |
| vaccination_study_09 | T_NK_lineage | 20 | 2,244 | CD4 Naive / T Central Memory | ydT Cell | 0.447 | 0.585 | 0.138 | marker_final_disagreement |
| vaccination_study_09 | Myeloid_lineage | 3 | 2,042 | Classical Monocyte | Intermediate Monocyte | 0.546 | 1.000 | 0.454 | marker_final_disagreement |
| vaccination_study_09 | Myeloid_lineage | 4 | 1,955 | Classical Monocyte | Intermediate Monocyte | 0.596 | 1.000 | 0.404 | marker_final_disagreement |
| vaccination_study_09 | Myeloid_lineage | 5 | 1,941 | Classical Monocyte | Intermediate Monocyte | 0.695 | 1.000 | 0.305 | marker_final_disagreement |

## Cluster Consensus Evidence

| study | lineage | cluster | cells | chosen_label | accepted | score_margin | cluster_marker_assignment | treg_key_any | treg_key_bonus | marker_set | marker_alert |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| vaccination_study_09 | B_lineage | 0 | 1,479 | Naive B Cell | True | 4.152 | Naive B Cell | nan | nan | B_naive | pass |
| vaccination_study_09 | B_lineage | 1 | 1,336 | Naive B Cell | True | 3.861 | Naive B Cell | nan | nan | B_naive | pass |
| vaccination_study_09 | B_lineage | 2 | 1,330 | Naive B Cell | True | 3.945 | Naive B Cell | nan | nan | B_naive | pass |
| vaccination_study_09 | B_lineage | 3 | 1,328 | Naive B Cell | True | 3.993 | Naive B Cell | nan | nan | B_naive | pass |
| vaccination_study_09 | B_lineage | 4 | 1,201 | Memory B Cell | True | 3.200 | Memory B Cell | nan | nan | B_memory_ABC | pass |
| vaccination_study_09 | B_lineage | 5 | 1,050 | Memory B Cell | True | 3.672 | Memory B Cell | nan | nan | B_memory_ABC | pass |
| vaccination_study_09 | B_lineage | 6 | 930 | Naive B Cell | True | 4.169 | Naive B Cell | nan | nan | B_naive | pass |
| vaccination_study_09 | B_lineage | 7 | 815 | Naive B Cell | True | 4.048 | Naive B Cell | nan | nan | B_naive | pass |
| vaccination_study_09 | B_lineage | 8 | 771 | Naive B Cell | True | 4.086 | Naive B Cell | nan | nan | B_naive | pass |
| vaccination_study_09 | B_lineage | 9 | 764 | Naive B Cell | True | 4.449 | Naive B Cell | nan | nan | B_naive | pass |
| vaccination_study_09 | B_lineage | 10 | 626 | Memory B Cell | True | 3.315 | Memory B Cell | nan | nan | B_memory_ABC | pass |
| vaccination_study_09 | B_lineage | 11 | 613 | Naive B Cell | True | 4.339 | Naive B Cell | nan | nan | B_naive | pass |
| vaccination_study_09 | B_lineage | 12 | 587 | Memory B Cell | True | 3.575 | Memory B Cell | nan | nan | B_memory_ABC | pass |
| vaccination_study_09 | B_lineage | 13 | 536 | Naive B Cell | True | 4.210 | Naive B Cell | nan | nan | B_naive | pass |
| vaccination_study_09 | B_lineage | 14 | 472 | Naive B Cell | True | 4.148 | Naive B Cell | nan | nan | B_naive | pass |
| vaccination_study_09 | B_lineage | 15 | 463 | Naive B Cell | True | 3.770 | Naive B Cell | nan | nan | B_naive | pass |
| vaccination_study_09 | B_lineage | 16 | 330 | Memory B Cell | True | 3.700 | Memory B Cell | nan | nan | B_memory_ABC | pass |
| vaccination_study_09 | B_lineage | 17 | 297 | Plasma Cell | True | 1.322 | Memory B Cell | nan | nan | Plasma_ASC | warning |
| vaccination_study_09 | B_lineage | 18 | 296 | Memory B Cell | True | 3.311 | Memory B Cell | nan | nan | B_memory_ABC | pass |
| vaccination_study_09 | B_lineage | 19 | 263 | Plasma Cell | True | 0.844 | Naive B Cell | nan | nan | Plasma_ASC | warning |
| vaccination_study_09 | B_lineage | 20 | 183 | Naive B Cell | True | 1.912 | Naive B Cell | nan | nan | B_naive | pass |
| vaccination_study_09 | B_lineage | 21 | 159 | Plasma Cell | True | 3.688 | Memory B Cell | nan | nan | Plasma_ASC | warning |
| vaccination_study_09 | B_lineage | 22 | 95 | Naive B Cell | True | 2.026 | Naive B Cell | nan | nan | B_naive | pass |
| vaccination_study_09 | B_lineage | 23 | 17 | Naive B Cell | True | 2.394 | Naive B Cell | nan | nan | B_naive | pass |
| vaccination_study_09 | B_lineage | 24 | 4 | Naive B Cell | True | 4.497 | Naive B Cell | nan | nan | B_naive | pass |
| vaccination_study_09 | Myeloid_lineage | 0 | 2,880 | Classical Monocyte | True | 2.477 | Intermediate Monocyte | nan | nan | not_applicable | pass |
| vaccination_study_09 | Myeloid_lineage | 1 | 2,676 | Non-Classical Monocyte | True | 1.664 | Intermediate Monocyte | nan | nan | not_applicable | pass |
| vaccination_study_09 | Myeloid_lineage | 2 | 2,657 | Classical Monocyte | True | 2.438 | Intermediate Monocyte | nan | nan | not_applicable | pass |
| vaccination_study_09 | Myeloid_lineage | 3 | 2,042 | Classical Monocyte | True | 2.449 | Intermediate Monocyte | nan | nan | not_applicable | pass |
| vaccination_study_09 | Myeloid_lineage | 4 | 1,955 | Classical Monocyte | True | 2.439 | Intermediate Monocyte | nan | nan | not_applicable | pass |

## 出力ファイル

- Submission TSVs: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_clean_v18_obsfix/vaccination_study_09/submissions/`
- cellxgene H5ADs: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_clean_v18_obsfix/vaccination_study_09/cellxgene/`
- Marker availability table: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_clean_v18_obsfix/vaccination_study_09/tables/marker_gene_availability.tsv`
- Marker availability alerts: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_clean_v18_obsfix/vaccination_study_09/tables/marker_gene_availability_alerts.tsv`
- Subcluster evidence: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_clean_v18_obsfix/vaccination_study_09/tables/lineage_subcluster_evidence.tsv.gz`
- Source disagreement summary: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_clean_v18_obsfix/vaccination_study_09/tables/source_disagreement_summary.tsv`
- Diagnostics tables: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_clean_v18_obsfix/vaccination_study_09/tables/`

