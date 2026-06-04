# HIPC データセットアノテーションレポート: vaccination_study_09

更新日: 2026-06-04 EDT

このレポートは `hipc-annotation` Codex workflow によって生成したデータセット別レビュー文書です。固定 method は repository README に置き、このレポートでは実際の evidence、弱い箇所、レビュー優先度、UMAP / dotplot を確認します。

## データセット概要

| study | cells | analysis_X_genes | pre_hvg_genes | counts_layer_genes | labels | parent_or_blood_fraction | Blood Cell | Doublet | artifact_like | median_confidence | low_confidence | source_disagreement | invalid_labels |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| vaccination_study_09 | 139,960 | 19,141 | 19,141 | 19,141 | 19 | 0.012 | 1,708 | 579 | 132 | 0.713 | 3,059 | 26,497 (0.189) | none |

## 実行概要

- 実行単位: one dataset in, one annotated dataset out。
- 実行経路: Codex skill `hipc-annotation` -> bundled helper `run_one.sh` -> annotation CLI -> validator -> report inspection。
- 検証: submission row count、H5AD observation count、official label validity、H5AD/submission agreement、confidence column、report image link を確認する。
- このレポートは workflow の再掲ではなく、このデータセットの marker 欠損、UMAP、label 構成、review concern を読むためのもの。

## データセット固有の解釈

- `vaccination_study_09`: 139,960 cells、analysis X/var 19,141 genes、pre-HVG slot 19,141 genes、submitted label 19 種、parent/Blood residual fraction 0.012、median confidence 0.713。
  - 3,059 cells は low confidence。QC / confidence UMAP 上で局在を確認する。
  - 579 cells は `Doublet` として提出。mixed-lineage marker expression と scrublet support を確認する。
  - 1,708 cells は `Blood Cell` として残存。これは filter-out ではなく、曖昧な細胞を公式 parent label で残したもの。
  - Marker gene 欠損アラート: Plasma_ASC。該当 marker set に依存する fine label は慎重に見る。

## データセット固有の評価

- 全体像: 139,960 cells / analysis X/var 19,141 genes / pre-HVG slot 19,141 genes。parent/Blood residual は 0.012、low-confidence は 3,059 cells、source disagreement flag は 26,497 cells (0.189)。
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
| vaccination_study_09 | Plasma Cell | 645 | 0.250 | 477 | 0.740 |
| vaccination_study_09 | NK Cell | 18,502 | 0.500 | 9,108 | 0.492 |
| vaccination_study_09 | Treg | 2,459 | 0.500 | 1,186 | 0.482 |
| vaccination_study_09 | CD8 Naive / T Central Memory | 11,312 | 0.500 | 4,328 | 0.383 |
| vaccination_study_09 | CD8 Cytotoxic / T Effector Memory | 7,531 | 0.500 | 2,296 | 0.305 |
| vaccination_study_09 | Conventional DC 2 | 1,645 | 0.500 | 361 | 0.219 |
| vaccination_study_09 | Blood Cell | 1,708 | 0.750 | 282 | 0.165 |
| vaccination_study_09 | Classical Monocyte | 24,881 | 0.750 | 3,121 | 0.125 |
| vaccination_study_09 | Naive B Cell | 11,096 | 0.750 | 1,103 | 0.099 |
| vaccination_study_09 | Memory B Cell | 4,201 | 0.750 | 416 | 0.099 |
| vaccination_study_09 | MAIT Cell | 3,840 | 0.500 | 365 | 0.095 |

## レビュー優先事項

| study | concern | cells |
| --- | --- | --- |
| vaccination_study_09 | High source disagreement for Doublet | 579 |
| vaccination_study_09 | High source disagreement for Plasma Cell | 477 |
| vaccination_study_09 | warning marker availability for Plasma_ASC | 645 |
| vaccination_study_09 | Large Blood Cell/ambiguous residual remains | 1,708 |

## ラベル構成

| study | predicted_cell_type | cells |
| --- | --- | --- |
| vaccination_study_09 | CD4 Naive / T Central Memory | 46,629 |
| vaccination_study_09 | Classical Monocyte | 24,881 |
| vaccination_study_09 | NK Cell | 18,502 |
| vaccination_study_09 | CD8 Naive / T Central Memory | 11,312 |
| vaccination_study_09 | Naive B Cell | 11,096 |
| vaccination_study_09 | CD8 Cytotoxic / T Effector Memory | 7,531 |
| vaccination_study_09 | Memory B Cell | 4,201 |
| vaccination_study_09 | Non-Classical Monocyte | 3,947 |
| vaccination_study_09 | MAIT Cell | 3,840 |
| vaccination_study_09 | Treg | 2,459 |
| vaccination_study_09 | Blood Cell | 1,708 |
| vaccination_study_09 | Conventional DC 2 | 1,645 |
| vaccination_study_09 | Plasmacytoid DC | 802 |
| vaccination_study_09 | Plasma Cell | 645 |
| vaccination_study_09 | Doublet | 579 |
| vaccination_study_09 | Platelet | 86 |
| vaccination_study_09 | Conventional DC 1 | 51 |
| vaccination_study_09 | HSC | 45 |
| vaccination_study_09 | RBC | 1 |

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

![vaccination_study_09 B_lineage true subcluster QC](assets/umap_vaccination_study_09_B_lineage_true_subcluster_qc.png)

![vaccination_study_09 B_lineage true subcluster marker scores](assets/umap_vaccination_study_09_B_lineage_true_subcluster_marker_scores.png)

![vaccination_study_09 B_lineage true subcluster marker expression](assets/umap_vaccination_study_09_B_lineage_true_subcluster_marker_expression.png)

![vaccination_study_09 B_lineage subcluster marker score heatmap](assets/subcluster_marker_score_heatmap_vaccination_study_09_B_lineage.png)

![vaccination_study_09 B_lineage subcluster marker dotplot](assets/dotplot_vaccination_study_09_B_lineage_true_subcluster_marker_dotplot.png)

Tables: `tables/vaccination_study_09_B_lineage_true_subcluster_umap.tsv.gz`, `tables/vaccination_study_09_B_lineage_subcluster_candidate_scores.tsv`.

#### vaccination_study_09 T_NK_lineage true subcluster UMAP

![vaccination_study_09 T_NK_lineage true subcluster labels](assets/umap_vaccination_study_09_T_NK_lineage_true_subcluster_label.png)

![vaccination_study_09 T_NK_lineage true subcluster QC](assets/umap_vaccination_study_09_T_NK_lineage_true_subcluster_qc.png)

![vaccination_study_09 T_NK_lineage true subcluster marker scores](assets/umap_vaccination_study_09_T_NK_lineage_true_subcluster_marker_scores.png)

![vaccination_study_09 T_NK_lineage true subcluster marker expression](assets/umap_vaccination_study_09_T_NK_lineage_true_subcluster_marker_expression.png)

![vaccination_study_09 T_NK_lineage subcluster marker score heatmap](assets/subcluster_marker_score_heatmap_vaccination_study_09_T_NK_lineage.png)

![vaccination_study_09 T_NK_lineage subcluster marker dotplot](assets/dotplot_vaccination_study_09_T_NK_lineage_true_subcluster_marker_dotplot.png)

Tables: `tables/vaccination_study_09_T_NK_lineage_true_subcluster_umap.tsv.gz`, `tables/vaccination_study_09_T_NK_lineage_subcluster_candidate_scores.tsv`.

#### vaccination_study_09 Myeloid_lineage true subcluster UMAP

![vaccination_study_09 Myeloid_lineage true subcluster labels](assets/umap_vaccination_study_09_Myeloid_lineage_true_subcluster_label.png)

![vaccination_study_09 Myeloid_lineage true subcluster QC](assets/umap_vaccination_study_09_Myeloid_lineage_true_subcluster_qc.png)

![vaccination_study_09 Myeloid_lineage true subcluster marker scores](assets/umap_vaccination_study_09_Myeloid_lineage_true_subcluster_marker_scores.png)

![vaccination_study_09 Myeloid_lineage true subcluster marker expression](assets/umap_vaccination_study_09_Myeloid_lineage_true_subcluster_marker_expression.png)

![vaccination_study_09 Myeloid_lineage subcluster marker score heatmap](assets/subcluster_marker_score_heatmap_vaccination_study_09_Myeloid_lineage.png)

![vaccination_study_09 Myeloid_lineage subcluster marker dotplot](assets/dotplot_vaccination_study_09_Myeloid_lineage_true_subcluster_marker_dotplot.png)

Tables: `tables/vaccination_study_09_Myeloid_lineage_true_subcluster_umap.tsv.gz`, `tables/vaccination_study_09_Myeloid_lineage_subcluster_candidate_scores.tsv`.


## Subcluster Marker Score Review

上の lineage-specific panel は、各 lineage subset で HVG 選択、PCA、neighbors、Leiden、UMAP を再計算した true local subcluster analysis から生成しています。Marker gene による fine label の確認は global UMAP だけではなく、この local UMAP、marker-score UMAP、marker-expression UMAP、dotplot を主に見ます。

## Cluster Consensus Evidence

| study | lineage | cluster | cells | chosen_label | accepted | score_margin | marker_set | marker_alert |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| vaccination_study_09 | B_lineage | 0 | 1,654 | Naive B Cell | True | 2.817 | B_naive | pass |
| vaccination_study_09 | B_lineage | 1 | 1,317 | Naive B Cell | True | 2.617 | B_naive | pass |
| vaccination_study_09 | B_lineage | 2 | 1,136 | Memory B Cell | True | 2.096 | B_memory_ABC | pass |
| vaccination_study_09 | B_lineage | 3 | 1,126 | Naive B Cell | True | 2.717 | B_naive | pass |
| vaccination_study_09 | B_lineage | 4 | 1,067 | Memory B Cell | True | 2.279 | B_memory_ABC | pass |
| vaccination_study_09 | B_lineage | 5 | 1,060 | Naive B Cell | True | 2.835 | B_naive | pass |
| vaccination_study_09 | B_lineage | 6 | 1,013 | Naive B Cell | True | 2.545 | B_naive | pass |
| vaccination_study_09 | B_lineage | 7 | 876 | Naive B Cell | True | 2.884 | B_naive | pass |
| vaccination_study_09 | B_lineage | 8 | 838 | Naive B Cell | True | 2.661 | B_naive | pass |
| vaccination_study_09 | B_lineage | 9 | 773 | Naive B Cell | True | 2.655 | B_naive | pass |
| vaccination_study_09 | B_lineage | 10 | 641 | Memory B Cell | True | 2.146 | B_memory_ABC | pass |
| vaccination_study_09 | B_lineage | 11 | 640 | Naive B Cell | True | 2.789 | B_naive | pass |
| vaccination_study_09 | B_lineage | 12 | 543 | Memory B Cell | True | 1.703 | B_memory_ABC | pass |
| vaccination_study_09 | B_lineage | 13 | 482 | Memory B Cell | True | 2.156 | B_memory_ABC | pass |
| vaccination_study_09 | B_lineage | 14 | 459 | Naive B Cell | True | 2.388 | B_naive | pass |
| vaccination_study_09 | B_lineage | 15 | 430 | Naive B Cell | True | 2.711 | B_naive | pass |
| vaccination_study_09 | B_lineage | 16 | 416 | Naive B Cell | True | 2.354 | B_naive | pass |
| vaccination_study_09 | B_lineage | 17 | 293 | Plasma Cell | True | 2.441 | Plasma_ASC | warning |
| vaccination_study_09 | B_lineage | 18 | 262 | Naive B Cell | True | 2.736 | B_naive | pass |
| vaccination_study_09 | B_lineage | 19 | 261 | Memory B Cell | True | 1.550 | B_memory_ABC | pass |
| vaccination_study_09 | B_lineage | 20 | 193 | Plasma Cell | True | 0.685 | Plasma_ASC | warning |
| vaccination_study_09 | B_lineage | 21 | 159 | Plasma Cell | True | 2.601 | Plasma_ASC | warning |
| vaccination_study_09 | B_lineage | 22 | 122 | Naive B Cell | True | 2.363 | B_naive | pass |
| vaccination_study_09 | B_lineage | 23 | 93 | Naive B Cell | True | 1.822 | B_naive | pass |
| vaccination_study_09 | B_lineage | 24 | 71 | Memory B Cell | True | 0.766 | B_memory_ABC | pass |
| vaccination_study_09 | B_lineage | 25 | 17 | Naive B Cell | True | 1.554 | B_naive | pass |
| vaccination_study_09 | Myeloid_lineage | 0 | 2,801 | Classical Monocyte | True | 2.583 | not_applicable | pass |
| vaccination_study_09 | Myeloid_lineage | 1 | 2,525 | Classical Monocyte | True | 2.608 | not_applicable | pass |
| vaccination_study_09 | Myeloid_lineage | 2 | 2,304 | Non-Classical Monocyte | True | 1.811 | not_applicable | pass |
| vaccination_study_09 | Myeloid_lineage | 3 | 2,116 | Classical Monocyte | True | 2.450 | not_applicable | pass |

## 出力ファイル

- Submission TSVs: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_clean_v16/vaccination_study_09/submissions/`
- cellxgene H5ADs: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_clean_v16/vaccination_study_09/cellxgene/`
- Marker availability table: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_clean_v16/vaccination_study_09/tables/marker_gene_availability.tsv`
- Marker availability alerts: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_clean_v16/vaccination_study_09/tables/marker_gene_availability_alerts.tsv`
- Subcluster evidence: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_clean_v16/vaccination_study_09/tables/lineage_subcluster_evidence.tsv.gz`
- Source disagreement summary: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_clean_v16/vaccination_study_09/tables/source_disagreement_summary.tsv`
- Diagnostics tables: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_clean_v16/vaccination_study_09/tables/`

