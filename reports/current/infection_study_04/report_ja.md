# HIPC データセットアノテーションレポート: infection_study_04

更新日: 2026-06-04 EDT

このレポートは `hipc-annotation` Codex workflow によって生成したデータセット別レビュー文書です。固定 method は repository README に置き、このレポートでは実際の evidence、弱い箇所、レビュー優先度、UMAP / dotplot を確認します。

## データセット概要

| study | cells | analysis_X_genes | pre_hvg_genes | counts_layer_genes | labels | parent_or_blood_fraction | Blood Cell | Doublet | artifact_like | median_confidence | low_confidence | source_disagreement | invalid_labels |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| infection_study_04 | 43,767 | 26,361 | 26,361 | 26,361 | 17 | 0.045 | 1,549 | 132 | 324 | 0.820 | 2,082 | 8,697 (0.199) | none |

## 実行概要

- 実行単位: one dataset in, one annotated dataset out。
- 実行経路: Codex skill `hipc-annotation` -> bundled helper `run_one.sh` -> annotation CLI -> validator -> report inspection。
- 検証: submission row count、H5AD observation count、official label validity、H5AD/submission agreement、confidence column、report image link を確認する。
- このレポートは workflow の再掲ではなく、このデータセットの marker 欠損、UMAP、label 構成、review concern を読むためのもの。

## データセット固有の解釈

- `infection_study_04`: 43,767 cells、analysis X/var 26,361 genes、pre-HVG slot 26,361 genes、submitted label 17 種、parent/Blood residual fraction 0.045、median confidence 0.820。
  - 2,082 cells は low confidence。QC / confidence UMAP 上で局在を確認する。
  - 132 cells は `Doublet` として提出。mixed-lineage marker expression と scrublet support を確認する。
  - 1,549 cells は `Blood Cell` として残存。これは filter-out ではなく、曖昧な細胞を公式 parent label で残したもの。
  - Marker gene 欠損アラート: Plasma_ASC。該当 marker set に依存する fine label は慎重に見る。

## データセット固有の評価

- 全体像: 43,767 cells / analysis X/var 26,361 genes / pre-HVG slot 26,361 genes。parent/Blood residual は 0.045、low-confidence は 2,082 cells、source disagreement flag は 8,697 cells (0.199)。
- 優先確認: low-confidence 領域が QC UMAP と source-disagreement UMAP で同じ場所に集まるかを確認する。
- 優先確認: `Blood Cell` 残存が孤立 cluster なのか、複数 lineage に分散した曖昧領域なのかを UMAP で確認する。
- Marker gene 欠損: Plasma_ASC は confidence cap 対象。該当 label は marker expression UMAP と dotplot で妥当性を確認する。

## Marker Gene 欠損アラート

| study | marker_set | alert | present_fraction | missing_critical_markers | missing_genes |
| --- | --- | --- | --- | --- | --- |
| infection_study_04 | Plasma_ASC | warning | 0.889 | JCHAIN | JCHAIN |

## ソース間不一致

| study | predicted_cell_type | cells | median_source_agreement | disagreement_cells | disagreement_fraction |
| --- | --- | --- | --- | --- | --- |
| infection_study_04 | T Cell | 401 | 0.000 | 401 | 1.000 |
| infection_study_04 | Doublet | 132 | 0.000 | 132 | 1.000 |
| infection_study_04 | Memory B Cell | 1,468 | 0.250 | 884 | 0.602 |
| infection_study_04 | Blood Cell | 1,549 | 0.250 | 906 | 0.585 |
| infection_study_04 | Naive B Cell | 1,795 | 0.500 | 740 | 0.412 |
| infection_study_04 | MAIT Cell | 318 | 0.500 | 120 | 0.377 |
| infection_study_04 | CD8 Cytotoxic / T Effector Memory | 6,418 | 0.750 | 1,582 | 0.246 |
| infection_study_04 | NK Cell | 7,363 | 0.750 | 1,534 | 0.208 |
| infection_study_04 | Treg | 488 | 0.500 | 100 | 0.205 |
| infection_study_04 | Conventional DC 2 | 415 | 0.500 | 72 | 0.173 |
| infection_study_04 | CD4 Naive / T Central Memory | 7,845 | 0.750 | 908 | 0.116 |
| infection_study_04 | Classical Monocyte | 10,485 | 0.750 | 1,101 | 0.105 |

## レビュー優先事項

| study | concern | cells |
| --- | --- | --- |
| infection_study_04 | High source disagreement for Blood Cell | 906 |
| infection_study_04 | High source disagreement for Doublet | 132 |
| infection_study_04 | High source disagreement for Memory B Cell | 884 |
| infection_study_04 | High source disagreement for T Cell | 401 |
| infection_study_04 | warning marker availability for Plasma_ASC | 3,137 |
| infection_study_04 | Large Blood Cell/ambiguous residual remains | 1,549 |

## ラベル構成

| study | predicted_cell_type | cells |
| --- | --- | --- |
| infection_study_04 | Classical Monocyte | 10,485 |
| infection_study_04 | CD4 Naive / T Central Memory | 7,845 |
| infection_study_04 | NK Cell | 7,363 |
| infection_study_04 | CD8 Cytotoxic / T Effector Memory | 6,418 |
| infection_study_04 | Plasma Cell | 3,137 |
| infection_study_04 | Naive B Cell | 1,795 |
| infection_study_04 | Blood Cell | 1,549 |
| infection_study_04 | Memory B Cell | 1,468 |
| infection_study_04 | Non-Classical Monocyte | 1,400 |
| infection_study_04 | Treg | 488 |
| infection_study_04 | Conventional DC 2 | 415 |
| infection_study_04 | T Cell | 401 |
| infection_study_04 | MAIT Cell | 318 |
| infection_study_04 | Plasmacytoid DC | 229 |
| infection_study_04 | Platelet | 201 |
| infection_study_04 | Doublet | 132 |
| infection_study_04 | HSC | 123 |

## Inline Figures

### infection_study_04

![infection_study_04 final labels](assets/umap_infection_study_04_annotation_label.png)

![infection_study_04 lineage and annotation reason](assets/umap_infection_study_04_annotation_lineage_reason.png)

![infection_study_04 QC and confidence](assets/umap_infection_study_04_annotation_qc_confidence.png)

![infection_study_04 source agreement and disagreement](assets/umap_infection_study_04_annotation_source_disagreement.png)

![infection_study_04 marker expression UMAPs](assets/umap_infection_study_04_annotation_marker_expression.png)

![infection_study_04 submitted-label marker dotplot](assets/dotplot_infection_study_04_annotation_marker_dotplot.png)

#### infection_study_04 B_lineage true subcluster UMAP

![infection_study_04 B_lineage true subcluster labels](assets/umap_infection_study_04_B_lineage_true_subcluster_label.png)

![infection_study_04 B_lineage true subcluster QC](assets/umap_infection_study_04_B_lineage_true_subcluster_qc.png)

![infection_study_04 B_lineage true subcluster marker scores](assets/umap_infection_study_04_B_lineage_true_subcluster_marker_scores.png)

![infection_study_04 B_lineage true subcluster marker expression](assets/umap_infection_study_04_B_lineage_true_subcluster_marker_expression.png)

![infection_study_04 B_lineage subcluster marker score heatmap](assets/subcluster_marker_score_heatmap_infection_study_04_B_lineage.png)

![infection_study_04 B_lineage subcluster marker dotplot](assets/dotplot_infection_study_04_B_lineage_true_subcluster_marker_dotplot.png)

Tables: `tables/infection_study_04_B_lineage_true_subcluster_umap.tsv.gz`, `tables/infection_study_04_B_lineage_subcluster_candidate_scores.tsv`.

#### infection_study_04 T_NK_lineage true subcluster UMAP

![infection_study_04 T_NK_lineage true subcluster labels](assets/umap_infection_study_04_T_NK_lineage_true_subcluster_label.png)

![infection_study_04 T_NK_lineage true subcluster QC](assets/umap_infection_study_04_T_NK_lineage_true_subcluster_qc.png)

![infection_study_04 T_NK_lineage true subcluster marker scores](assets/umap_infection_study_04_T_NK_lineage_true_subcluster_marker_scores.png)

![infection_study_04 T_NK_lineage true subcluster marker expression](assets/umap_infection_study_04_T_NK_lineage_true_subcluster_marker_expression.png)

![infection_study_04 T_NK_lineage subcluster marker score heatmap](assets/subcluster_marker_score_heatmap_infection_study_04_T_NK_lineage.png)

![infection_study_04 T_NK_lineage subcluster marker dotplot](assets/dotplot_infection_study_04_T_NK_lineage_true_subcluster_marker_dotplot.png)

Tables: `tables/infection_study_04_T_NK_lineage_true_subcluster_umap.tsv.gz`, `tables/infection_study_04_T_NK_lineage_subcluster_candidate_scores.tsv`.

#### infection_study_04 Myeloid_lineage true subcluster UMAP

![infection_study_04 Myeloid_lineage true subcluster labels](assets/umap_infection_study_04_Myeloid_lineage_true_subcluster_label.png)

![infection_study_04 Myeloid_lineage true subcluster QC](assets/umap_infection_study_04_Myeloid_lineage_true_subcluster_qc.png)

![infection_study_04 Myeloid_lineage true subcluster marker scores](assets/umap_infection_study_04_Myeloid_lineage_true_subcluster_marker_scores.png)

![infection_study_04 Myeloid_lineage true subcluster marker expression](assets/umap_infection_study_04_Myeloid_lineage_true_subcluster_marker_expression.png)

![infection_study_04 Myeloid_lineage subcluster marker score heatmap](assets/subcluster_marker_score_heatmap_infection_study_04_Myeloid_lineage.png)

![infection_study_04 Myeloid_lineage subcluster marker dotplot](assets/dotplot_infection_study_04_Myeloid_lineage_true_subcluster_marker_dotplot.png)

Tables: `tables/infection_study_04_Myeloid_lineage_true_subcluster_umap.tsv.gz`, `tables/infection_study_04_Myeloid_lineage_subcluster_candidate_scores.tsv`.


## Subcluster Marker Score Review

上の lineage-specific panel は、各 lineage subset で HVG 選択、PCA、neighbors、Leiden、UMAP を再計算した true local subcluster analysis から生成しています。Marker gene による fine label の確認は global UMAP だけではなく、この local UMAP、marker-score UMAP、marker-expression UMAP、dotplot を主に見ます。

## Cluster Consensus Evidence

| study | lineage | cluster | cells | chosen_label | accepted | score_margin | marker_set | marker_alert |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| infection_study_04 | B_lineage | 0 | 929 | Naive B Cell | True | 3.071 | B_naive | pass |
| infection_study_04 | B_lineage | 1 | 590 | Plasma Cell | True | 2.393 | Plasma_ASC | warning |
| infection_study_04 | B_lineage | 2 | 457 | Plasma Cell | True | 2.770 | Plasma_ASC | warning |
| infection_study_04 | B_lineage | 3 | 436 | Plasma Cell | True | 2.786 | Plasma_ASC | warning |
| infection_study_04 | B_lineage | 4 | 411 | Memory B Cell | True | 1.495 | B_memory_ABC | pass |
| infection_study_04 | B_lineage | 5 | 403 | Memory B Cell | True | 0.961 | B_memory_ABC | pass |
| infection_study_04 | B_lineage | 6 | 401 | Naive B Cell | True | 1.894 | B_naive | pass |
| infection_study_04 | B_lineage | 7 | 384 | Memory B Cell | True | 1.498 | B_memory_ABC | pass |
| infection_study_04 | B_lineage | 8 | 329 | Plasma Cell | True | 2.545 | Plasma_ASC | warning |
| infection_study_04 | B_lineage | 9 | 270 | Memory B Cell | True | 2.077 | B_memory_ABC | pass |
| infection_study_04 | B_lineage | 10 | 269 | Plasma Cell | True | 2.729 | Plasma_ASC | warning |
| infection_study_04 | B_lineage | 11 | 258 | Plasma Cell | True | 2.693 | Plasma_ASC | warning |
| infection_study_04 | B_lineage | 12 | 254 | Plasma Cell | True | 2.769 | Plasma_ASC | warning |
| infection_study_04 | B_lineage | 13 | 244 | Naive B Cell | True | 1.073 | B_naive | pass |
| infection_study_04 | B_lineage | 14 | 221 | Naive B Cell | True | 0.733 | B_naive | pass |
| infection_study_04 | B_lineage | 15 | 197 | Plasma Cell | True | 2.601 | Plasma_ASC | warning |
| infection_study_04 | B_lineage | 16 | 187 | Plasma Cell | True | 2.643 | Plasma_ASC | warning |
| infection_study_04 | B_lineage | 17 | 70 | Plasma Cell | True | 1.705 | Plasma_ASC | warning |
| infection_study_04 | B_lineage | 18 | 54 | Plasma Cell | True | 2.401 | Plasma_ASC | warning |
| infection_study_04 | B_lineage | 19 | 36 | Plasma Cell | True | 0.878 | Plasma_ASC | warning |
| infection_study_04 | Myeloid_lineage | 0 | 1,091 | Classical Monocyte | True | 2.273 | not_applicable | pass |
| infection_study_04 | Myeloid_lineage | 1 | 952 | Classical Monocyte | True | 2.630 | not_applicable | pass |
| infection_study_04 | Myeloid_lineage | 2 | 913 | Classical Monocyte | True | 2.686 | not_applicable | pass |
| infection_study_04 | Myeloid_lineage | 3 | 912 | Classical Monocyte | True | 2.733 | not_applicable | pass |
| infection_study_04 | Myeloid_lineage | 4 | 871 | Classical Monocyte | True | 2.441 | not_applicable | pass |
| infection_study_04 | Myeloid_lineage | 5 | 838 | Classical Monocyte | True | 1.892 | not_applicable | pass |
| infection_study_04 | Myeloid_lineage | 6 | 677 | Non-Classical Monocyte | True | 1.903 | not_applicable | pass |
| infection_study_04 | Myeloid_lineage | 7 | 640 | Classical Monocyte | True | 2.385 | not_applicable | pass |
| infection_study_04 | Myeloid_lineage | 8 | 609 | Classical Monocyte | True | 2.630 | not_applicable | pass |
| infection_study_04 | Myeloid_lineage | 9 | 589 | Classical Monocyte | True | 2.185 | not_applicable | pass |

## 出力ファイル

- Submission TSVs: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_clean_v16/infection_study_04/submissions/`
- cellxgene H5ADs: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_clean_v16/infection_study_04/cellxgene/`
- Marker availability table: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_clean_v16/infection_study_04/tables/marker_gene_availability.tsv`
- Marker availability alerts: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_clean_v16/infection_study_04/tables/marker_gene_availability_alerts.tsv`
- Subcluster evidence: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_clean_v16/infection_study_04/tables/lineage_subcluster_evidence.tsv.gz`
- Source disagreement summary: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_clean_v16/infection_study_04/tables/source_disagreement_summary.tsv`
- Diagnostics tables: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_clean_v16/infection_study_04/tables/`

