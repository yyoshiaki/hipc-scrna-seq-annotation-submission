# HIPC データセットアノテーションレポート: infection_study_01

更新日: 2026-06-04 EDT

このレポートは `hipc-annotation` Codex workflow によって生成したデータセット別レビュー文書です。固定 method は repository README に置き、このレポートでは実際の evidence、弱い箇所、レビュー優先度、UMAP / dotplot を確認します。

## データセット概要

| study | cells | analysis_X_genes | pre_hvg_genes | counts_layer_genes | labels | parent_or_blood_fraction | Blood Cell | Doublet | artifact_like | median_confidence | low_confidence | source_disagreement | invalid_labels |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| infection_study_01 | 54,924 | 33,538 | 33,538 | 33,538 | 19 | 0.006 | 279 | 1,278 | 1,355 | 0.777 | 7,918 | 8,109 (0.148) | none |

## 実行概要

- 実行単位: one dataset in, one annotated dataset out。
- 実行経路: Codex skill `hipc-annotation` -> bundled helper `run_one.sh` -> annotation CLI -> validator -> report inspection。
- 検証: submission row count、H5AD observation count、official label validity、H5AD/submission agreement、confidence column、report image link を確認する。
- このレポートは workflow の再掲ではなく、このデータセットの marker 欠損、UMAP、label 構成、review concern を読むためのもの。

## データセット固有の解釈

- `infection_study_01`: 54,924 cells、analysis X/var 33,538 genes、pre-HVG slot 33,538 genes、submitted label 19 種、parent/Blood residual fraction 0.006、median confidence 0.777。
  - 7,918 cells は low confidence。QC / confidence UMAP 上で局在を確認する。
  - 1,278 cells は `Doublet` として提出。mixed-lineage marker expression と scrublet support を確認する。
  - 279 cells は `Blood Cell` として残存。これは filter-out ではなく、曖昧な細胞を公式 parent label で残したもの。

## データセット固有の評価

- 全体像: 54,924 cells / analysis X/var 33,538 genes / pre-HVG slot 33,538 genes。parent/Blood residual は 0.006、low-confidence は 7,918 cells、source disagreement flag は 8,109 cells (0.148)。
- 優先確認: low-confidence 領域が QC UMAP と source-disagreement UMAP で同じ場所に集まるかを確認する。
- 優先確認: `Blood Cell` 残存が孤立 cluster なのか、複数 lineage に分散した曖昧領域なのかを UMAP で確認する。

## Marker Gene 欠損アラート

なし。

## ソース間不一致

| study | predicted_cell_type | cells | median_source_agreement | disagreement_cells | disagreement_fraction |
| --- | --- | --- | --- | --- | --- |
| infection_study_01 | Doublet | 1,278 | 0.000 | 1,278 | 1.000 |
| infection_study_01 | B Cell | 40 | 0.000 | 40 | 1.000 |
| infection_study_01 | Treg | 520 | 0.000 | 320 | 0.615 |
| infection_study_01 | MAIT Cell | 936 | 0.333 | 473 | 0.505 |
| infection_study_01 | CD4 Naive / T Central Memory | 4,743 | 0.500 | 1,898 | 0.400 |
| infection_study_01 | Blood Cell | 279 | 0.667 | 105 | 0.376 |
| infection_study_01 | CD4 T Effector Memory | 778 | 0.667 | 224 | 0.288 |
| infection_study_01 | Plasma Cell | 170 | 0.500 | 45 | 0.265 |
| infection_study_01 | Plasmacytoid DC | 102 | 0.667 | 16 | 0.157 |
| infection_study_01 | NK Cell | 9,740 | 1.000 | 1,499 | 0.154 |
| infection_study_01 | CD8 Cytotoxic / T Effector Memory | 8,855 | 1.000 | 802 | 0.091 |
| infection_study_01 | Conventional DC 2 | 440 | 1.000 | 35 | 0.080 |

## レビュー優先事項

| study | concern | cells |
| --- | --- | --- |
| infection_study_01 | High source disagreement for B Cell | 40 |
| infection_study_01 | High source disagreement for Doublet | 1,278 |
| infection_study_01 | High source disagreement for MAIT Cell | 473 |
| infection_study_01 | High source disagreement for Treg | 320 |

## ラベル構成

| study | predicted_cell_type | cells |
| --- | --- | --- |
| infection_study_01 | Classical Monocyte | 17,386 |
| infection_study_01 | NK Cell | 9,740 |
| infection_study_01 | CD8 Cytotoxic / T Effector Memory | 8,855 |
| infection_study_01 | CD4 Naive / T Central Memory | 4,743 |
| infection_study_01 | Naive B Cell | 4,233 |
| infection_study_01 | Memory B Cell | 2,120 |
| infection_study_01 | Non-Classical Monocyte | 1,916 |
| infection_study_01 | Platelet | 1,347 |
| infection_study_01 | Doublet | 1,278 |
| infection_study_01 | MAIT Cell | 936 |
| infection_study_01 | CD4 T Effector Memory | 778 |
| infection_study_01 | Treg | 520 |
| infection_study_01 | Conventional DC 2 | 440 |
| infection_study_01 | Blood Cell | 279 |
| infection_study_01 | Plasma Cell | 170 |
| infection_study_01 | Plasmacytoid DC | 102 |
| infection_study_01 | B Cell | 40 |
| infection_study_01 | Conventional DC 1 | 33 |
| infection_study_01 | HSC | 8 |

## Inline Figures

### infection_study_01

![infection_study_01 final labels](assets/umap_infection_study_01_annotation_label.png)

![infection_study_01 lineage and annotation reason](assets/umap_infection_study_01_annotation_lineage_reason.png)

![infection_study_01 QC and confidence](assets/umap_infection_study_01_annotation_qc_confidence.png)

![infection_study_01 source agreement and disagreement](assets/umap_infection_study_01_annotation_source_disagreement.png)

![infection_study_01 marker expression UMAPs](assets/umap_infection_study_01_annotation_marker_expression.png)

![infection_study_01 submitted-label marker dotplot](assets/dotplot_infection_study_01_annotation_marker_dotplot.png)

#### infection_study_01 B_lineage true subcluster UMAP

![infection_study_01 B_lineage true subcluster labels](assets/umap_infection_study_01_B_lineage_true_subcluster_label.png)

![infection_study_01 B_lineage true subcluster source labels](assets/umap_infection_study_01_B_lineage_true_subcluster_source_labels.png)

![infection_study_01 B_lineage true subcluster QC](assets/umap_infection_study_01_B_lineage_true_subcluster_qc.png)

![infection_study_01 B_lineage true subcluster marker scores](assets/umap_infection_study_01_B_lineage_true_subcluster_marker_scores.png)

![infection_study_01 B_lineage true subcluster marker expression](assets/umap_infection_study_01_B_lineage_true_subcluster_marker_expression.png)

![infection_study_01 B_lineage subcluster marker score heatmap](assets/subcluster_marker_score_heatmap_infection_study_01_B_lineage.png)

![infection_study_01 B_lineage subcluster marker dotplot](assets/dotplot_infection_study_01_B_lineage_true_subcluster_marker_dotplot.png)

Tables: `tables/infection_study_01_B_lineage_true_subcluster_umap.tsv.gz`, `tables/infection_study_01_B_lineage_subcluster_candidate_scores.tsv`.

#### infection_study_01 T_NK_lineage true subcluster UMAP

![infection_study_01 T_NK_lineage true subcluster labels](assets/umap_infection_study_01_T_NK_lineage_true_subcluster_label.png)

![infection_study_01 T_NK_lineage true subcluster source labels](assets/umap_infection_study_01_T_NK_lineage_true_subcluster_source_labels.png)

![infection_study_01 T_NK_lineage true subcluster QC](assets/umap_infection_study_01_T_NK_lineage_true_subcluster_qc.png)

![infection_study_01 T_NK_lineage true subcluster marker scores](assets/umap_infection_study_01_T_NK_lineage_true_subcluster_marker_scores.png)

![infection_study_01 T_NK_lineage true subcluster marker expression](assets/umap_infection_study_01_T_NK_lineage_true_subcluster_marker_expression.png)

![infection_study_01 T_NK_lineage subcluster marker score heatmap](assets/subcluster_marker_score_heatmap_infection_study_01_T_NK_lineage.png)

![infection_study_01 T_NK_lineage subcluster marker dotplot](assets/dotplot_infection_study_01_T_NK_lineage_true_subcluster_marker_dotplot.png)

Tables: `tables/infection_study_01_T_NK_lineage_true_subcluster_umap.tsv.gz`, `tables/infection_study_01_T_NK_lineage_subcluster_candidate_scores.tsv`.

#### infection_study_01 Myeloid_lineage true subcluster UMAP

![infection_study_01 Myeloid_lineage true subcluster labels](assets/umap_infection_study_01_Myeloid_lineage_true_subcluster_label.png)

![infection_study_01 Myeloid_lineage true subcluster source labels](assets/umap_infection_study_01_Myeloid_lineage_true_subcluster_source_labels.png)

![infection_study_01 Myeloid_lineage true subcluster QC](assets/umap_infection_study_01_Myeloid_lineage_true_subcluster_qc.png)

![infection_study_01 Myeloid_lineage true subcluster marker scores](assets/umap_infection_study_01_Myeloid_lineage_true_subcluster_marker_scores.png)

![infection_study_01 Myeloid_lineage true subcluster marker expression](assets/umap_infection_study_01_Myeloid_lineage_true_subcluster_marker_expression.png)

![infection_study_01 Myeloid_lineage subcluster marker score heatmap](assets/subcluster_marker_score_heatmap_infection_study_01_Myeloid_lineage.png)

![infection_study_01 Myeloid_lineage subcluster marker dotplot](assets/dotplot_infection_study_01_Myeloid_lineage_true_subcluster_marker_dotplot.png)

Tables: `tables/infection_study_01_Myeloid_lineage_true_subcluster_umap.tsv.gz`, `tables/infection_study_01_Myeloid_lineage_subcluster_candidate_scores.tsv`.


## Subcluster Marker Score Review

上の lineage-specific panel は、各 lineage subset で HVG 選択、PCA、neighbors、Leiden、UMAP を再計算した true local subcluster analysis から生成しています。Marker gene による fine label の確認は global UMAP だけではなく、この local UMAP、CellTypist/Azimuth/Pan-human/cluster-level marker gene assignment overlay、cluster marker gate score UMAP、marker-expression UMAP、dotplot を主に見ます。Treg など sparse marker label は cell-wise marker winner ではなく、local cluster の FOXP3/IL2RA/CTLA4 など key-marker support と reference support で判定します。

## Marker Assignment Feedback

Marker gene assignment は final label を強制的に上書きするものではなく、cluster-level の自己点検です。この表は marker-only assignment と final/reference-driven label がずれる cluster、marker specificity が弱い cluster、scRefMap が期待される lineage で欠落する cluster を示します。`marker_score` は raw marker base score から negative/confound marker penalty を差し引いた cluster-level marker gate score です。

| study | lineage | cluster | cells | chosen_label | marker_assignment | marker_score | base_score | penalty | flags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| infection_study_01 | Myeloid_lineage | 1 | 1,533 | Classical Monocyte | Intermediate Monocyte | 0.522 | 1.000 | 0.478 | marker_final_disagreement |
| infection_study_01 | Myeloid_lineage | 2 | 1,499 | Classical Monocyte | Intermediate Monocyte | 0.548 | 1.000 | 0.452 | marker_final_disagreement |
| infection_study_01 | Myeloid_lineage | 3 | 1,385 | Non-Classical Monocyte | Intermediate Monocyte | 0.469 | 1.000 | 0.531 | marker_final_disagreement |
| infection_study_01 | Myeloid_lineage | 4 | 1,383 | Classical Monocyte | Intermediate Monocyte | 0.481 | 1.000 | 0.519 | marker_final_disagreement |
| infection_study_01 | Myeloid_lineage | 5 | 1,344 | Classical Monocyte | Intermediate Monocyte | 0.472 | 1.000 | 0.528 | marker_final_disagreement |
| infection_study_01 | T_NK_lineage | 1 | 1,305 | NK Cell | NK Cell | 0.498 | 1.000 | 0.502 | screfmapping_missing_for_scope |
| infection_study_01 | T_NK_lineage | 2 | 1,300 | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | 0.540 | 1.000 | 0.460 | screfmapping_missing_for_scope |
| infection_study_01 | Myeloid_lineage | 6 | 1,202 | Classical Monocyte | Intermediate Monocyte | 0.450 | 1.000 | 0.550 | marker_final_disagreement |
| infection_study_01 | T_NK_lineage | 4 | 1,036 | NK Cell | NK Cell | 0.561 | 1.000 | 0.439 | screfmapping_missing_for_scope |
| infection_study_01 | T_NK_lineage | 5 | 1,001 | NK Cell | NK Cell | 0.699 | 1.000 | 0.301 | screfmapping_missing_for_scope |
| infection_study_01 | Myeloid_lineage | 8 | 978 | Classical Monocyte | Intermediate Monocyte | 0.507 | 1.000 | 0.493 | marker_final_disagreement |
| infection_study_01 | T_NK_lineage | 6 | 969 | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | 0.746 | 1.000 | 0.254 | screfmapping_missing_for_scope |
| infection_study_01 | T_NK_lineage | 7 | 927 | NK Cell | NK Cell | 0.757 | 1.000 | 0.243 | screfmapping_missing_for_scope |
| infection_study_01 | T_NK_lineage | 8 | 925 | CD8 Cytotoxic / T Effector Memory | CD8 Naive / T Central Memory | 0.497 | 1.000 | 0.503 | marker_final_disagreement;screfmapping_missing_for_scope |
| infection_study_01 | T_NK_lineage | 9 | 880 | NK Cell | NK Cell | 0.744 | 1.000 | 0.256 | screfmapping_missing_for_scope |
| infection_study_01 | Myeloid_lineage | 9 | 857 | Classical Monocyte | Intermediate Monocyte | 0.479 | 1.000 | 0.521 | marker_final_disagreement |
| infection_study_01 | T_NK_lineage | 11 | 851 | CD8 Cytotoxic / T Effector Memory | CD8 Naive / T Central Memory | 0.495 | 1.000 | 0.505 | marker_final_disagreement;screfmapping_missing_for_scope |
| infection_study_01 | Myeloid_lineage | 10 | 793 | Classical Monocyte | Intermediate Monocyte | 0.513 | 1.000 | 0.487 | marker_final_disagreement |
| infection_study_01 | T_NK_lineage | 12 | 695 | MAIT Cell | MAIT Cell | 0.501 | 1.000 | 0.499 | screfmapping_missing_for_scope |
| infection_study_01 | T_NK_lineage | 14 | 687 | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | 0.536 | 1.000 | 0.464 | screfmapping_missing_for_scope |

## Cluster Consensus Evidence

| study | lineage | cluster | cells | chosen_label | accepted | score_margin | cluster_marker_assignment | treg_key_any | treg_key_bonus | marker_set | marker_alert |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| infection_study_01 | B_lineage | 0 | 528 | Naive B Cell | True | 4.100 | Naive B Cell | nan | nan | B_naive | pass |
| infection_study_01 | B_lineage | 1 | 445 | Naive B Cell | True | 4.521 | Naive B Cell | nan | nan | B_naive | pass |
| infection_study_01 | B_lineage | 2 | 391 | Naive B Cell | True | 4.250 | Naive B Cell | nan | nan | B_naive | pass |
| infection_study_01 | B_lineage | 3 | 363 | Memory B Cell | True | 2.668 | Naive B Cell | nan | nan | B_memory_ABC | pass |
| infection_study_01 | B_lineage | 4 | 348 | Naive B Cell | True | 3.982 | Naive B Cell | nan | nan | B_naive | pass |
| infection_study_01 | B_lineage | 5 | 328 | Naive B Cell | True | 4.538 | Naive B Cell | nan | nan | B_naive | pass |
| infection_study_01 | B_lineage | 6 | 318 | Memory B Cell | True | 3.843 | Memory B Cell | nan | nan | B_memory_ABC | pass |
| infection_study_01 | B_lineage | 7 | 309 | Memory B Cell | True | 4.238 | Memory B Cell | nan | nan | B_memory_ABC | pass |
| infection_study_01 | B_lineage | 8 | 309 | Memory B Cell | True | 3.307 | Memory B Cell | nan | nan | B_memory_ABC | pass |
| infection_study_01 | B_lineage | 9 | 302 | Naive B Cell | True | 3.958 | Naive B Cell | nan | nan | B_naive | pass |
| infection_study_01 | B_lineage | 10 | 294 | Naive B Cell | True | 4.284 | Naive B Cell | nan | nan | B_naive | pass |
| infection_study_01 | B_lineage | 11 | 292 | Naive B Cell | True | 4.407 | Naive B Cell | nan | nan | B_naive | pass |
| infection_study_01 | B_lineage | 12 | 249 | Memory B Cell | True | 3.237 | Naive B Cell | nan | nan | B_memory_ABC | pass |
| infection_study_01 | B_lineage | 13 | 228 | Memory B Cell | True | 3.674 | Memory B Cell | nan | nan | B_memory_ABC | pass |
| infection_study_01 | B_lineage | 14 | 227 | Naive B Cell | True | 4.323 | Naive B Cell | nan | nan | B_naive | pass |
| infection_study_01 | B_lineage | 15 | 218 | Naive B Cell | True | 2.901 | Naive B Cell | nan | nan | B_naive | pass |
| infection_study_01 | B_lineage | 16 | 217 | Naive B Cell | True | 1.713 | Naive B Cell | nan | nan | B_naive | pass |
| infection_study_01 | B_lineage | 17 | 216 | Memory B Cell | True | 3.602 | Memory B Cell | nan | nan | B_memory_ABC | pass |
| infection_study_01 | B_lineage | 18 | 190 | Naive B Cell | True | 3.850 | Naive B Cell | nan | nan | B_naive | pass |
| infection_study_01 | B_lineage | 19 | 170 | Naive B Cell | True | 4.100 | Naive B Cell | nan | nan | B_naive | pass |
| infection_study_01 | B_lineage | 20 | 152 | Naive B Cell | True | 3.306 | Naive B Cell | nan | nan | B_naive | pass |
| infection_study_01 | B_lineage | 21 | 102 | Memory B Cell | True | 3.994 | Memory B Cell | nan | nan | B_memory_ABC | pass |
| infection_study_01 | B_lineage | 22 | 92 | Naive B Cell | True | 0.524 | Naive B Cell | nan | nan | B_naive | pass |
| infection_study_01 | B_lineage | 23 | 85 | Plasma Cell | True | 3.587 | Memory B Cell | nan | nan | Plasma_ASC | pass |
| infection_study_01 | B_lineage | 24 | 43 | Plasma Cell | True | 2.382 | Plasma Cell | nan | nan | Plasma_ASC | pass |
| infection_study_01 | B_lineage | 25 | 42 | Plasma Cell | True | 3.365 | Memory B Cell | nan | nan | Plasma_ASC | pass |
| infection_study_01 | B_lineage | 26 | 40 | B Cell | False | 0.627 | Memory B Cell | nan | nan | Plasma_ASC | pass |
| infection_study_01 | B_lineage | 27 | 39 | Naive B Cell | True | 1.375 | Naive B Cell | nan | nan | B_naive | pass |
| infection_study_01 | B_lineage | 28 | 26 | Memory B Cell | True | 3.450 | Memory B Cell | nan | nan | B_memory_ABC | pass |
| infection_study_01 | Myeloid_lineage | 0 | 1,695 | Classical Monocyte | True | 2.619 | Classical Monocyte | nan | nan | not_applicable | pass |

## 出力ファイル

- Submission TSVs: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_clean_v18_obsfix/infection_study_01/submissions/`
- cellxgene H5ADs: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_clean_v18_obsfix/infection_study_01/cellxgene/`
- Marker availability table: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_clean_v18_obsfix/infection_study_01/tables/marker_gene_availability.tsv`
- Marker availability alerts: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_clean_v18_obsfix/infection_study_01/tables/marker_gene_availability_alerts.tsv`
- Subcluster evidence: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_clean_v18_obsfix/infection_study_01/tables/lineage_subcluster_evidence.tsv.gz`
- Source disagreement summary: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_clean_v18_obsfix/infection_study_01/tables/source_disagreement_summary.tsv`
- Diagnostics tables: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_clean_v18_obsfix/infection_study_01/tables/`

