# HIPC データセットアノテーションレポート: vaccination_study_04

更新日: 2026-06-04 EDT

このレポートは `hipc-annotation` Codex workflow によって生成したデータセット別レビュー文書です。固定 method は repository README に置き、このレポートでは実際の evidence、弱い箇所、レビュー優先度、UMAP / dotplot を確認します。

## データセット概要

| study | cells | analysis_X_genes | pre_hvg_genes | counts_layer_genes | labels | parent_or_blood_fraction | Blood Cell | Doublet | artifact_like | median_confidence | low_confidence | source_disagreement | invalid_labels |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| vaccination_study_04 | 66,065 | 16,983 | 16,983 | 16,983 | 15 | 0.009 | 575 | 647 | 343 | 0.850 | 1,250 | 2,787 (0.042) | none |

## 実行概要

- 実行単位: one dataset in, one annotated dataset out。
- 実行経路: Codex skill `hipc-annotation` -> bundled helper `run_one.sh` -> annotation CLI -> validator -> report inspection。
- 検証: submission row count、H5AD observation count、official label validity、H5AD/submission agreement、confidence column、report image link を確認する。
- このレポートは workflow の再掲ではなく、このデータセットの marker 欠損、UMAP、label 構成、review concern を読むためのもの。

## データセット固有の解釈

- `vaccination_study_04`: 66,065 cells、analysis X/var 16,983 genes、pre-HVG slot 16,983 genes、submitted label 15 種、parent/Blood residual fraction 0.009、median confidence 0.850。
  - 1,250 cells は low confidence。QC / confidence UMAP 上で局在を確認する。
  - 647 cells は `Doublet` として提出。mixed-lineage marker expression と scrublet support を確認する。
  - 575 cells は `Blood Cell` として残存。これは filter-out ではなく、曖昧な細胞を公式 parent label で残したもの。
  - Marker gene 欠損アラート: Treg。該当 marker set に依存する fine label は慎重に見る。

## データセット固有の評価

- 全体像: 66,065 cells / analysis X/var 16,983 genes / pre-HVG slot 16,983 genes。parent/Blood residual は 0.009、low-confidence は 1,250 cells、source disagreement flag は 2,787 cells (0.042)。
- 優先確認: low-confidence 領域が QC UMAP と source-disagreement UMAP で同じ場所に集まるかを確認する。
- 優先確認: `Blood Cell` 残存が孤立 cluster なのか、複数 lineage に分散した曖昧領域なのかを UMAP で確認する。
- Marker gene 欠損: Treg は confidence cap 対象。該当 label は marker expression UMAP と dotplot で妥当性を確認する。

## Marker Gene 欠損アラート

| study | marker_set | alert | present_fraction | missing_critical_markers | missing_genes |
| --- | --- | --- | --- | --- | --- |
| vaccination_study_04 | Treg | critical | 0.286 | FOXP3;IL2RA | FOXP3;IL2RA;TIGIT;TNFRSF18;CCR8 |

## ソース間不一致

| study | predicted_cell_type | cells | median_source_agreement | disagreement_cells | disagreement_fraction |
| --- | --- | --- | --- | --- | --- |
| vaccination_study_04 | Doublet | 647 | 0.000 | 647 | 1.000 |
| vaccination_study_04 | Treg | 2 | 0.250 | 2 | 1.000 |
| vaccination_study_04 | Naive B Cell | 6 | 0.250 | 4 | 0.667 |
| vaccination_study_04 | CD4 Naive / T Central Memory | 28 | 0.250 | 16 | 0.571 |
| vaccination_study_04 | NK Cell | 252 | 0.750 | 58 | 0.230 |
| vaccination_study_04 | Conventional DC 2 | 7,705 | 0.750 | 819 | 0.106 |
| vaccination_study_04 | Blood Cell | 575 | 0.750 | 30 | 0.052 |
| vaccination_study_04 | Plasma Cell | 100 | 0.750 | 5 | 0.050 |
| vaccination_study_04 | Classical Monocyte | 34,238 | 0.750 | 977 | 0.029 |
| vaccination_study_04 | Conventional DC 1 | 1,110 | 0.750 | 31 | 0.028 |
| vaccination_study_04 | Plasmacytoid DC | 5,505 | 0.750 | 53 | 0.010 |
| vaccination_study_04 | Non-Classical Monocyte | 15,552 | 0.750 | 145 | 0.009 |

## レビュー優先事項

| study | concern | cells |
| --- | --- | --- |
| vaccination_study_04 | High source disagreement for CD4 Naive / T Central Memory | 16 |
| vaccination_study_04 | High source disagreement for Doublet | 647 |
| vaccination_study_04 | High source disagreement for Naive B Cell | 4 |
| vaccination_study_04 | High source disagreement for Treg | 2 |
| vaccination_study_04 | critical marker availability for Treg | 2 |

## ラベル構成

| study | predicted_cell_type | cells |
| --- | --- | --- |
| vaccination_study_04 | Classical Monocyte | 34,238 |
| vaccination_study_04 | Non-Classical Monocyte | 15,552 |
| vaccination_study_04 | Conventional DC 2 | 7,705 |
| vaccination_study_04 | Plasmacytoid DC | 5,505 |
| vaccination_study_04 | Conventional DC 1 | 1,110 |
| vaccination_study_04 | Doublet | 647 |
| vaccination_study_04 | Blood Cell | 575 |
| vaccination_study_04 | HSC | 337 |
| vaccination_study_04 | NK Cell | 252 |
| vaccination_study_04 | Plasma Cell | 100 |
| vaccination_study_04 | CD4 Naive / T Central Memory | 28 |
| vaccination_study_04 | Naive B Cell | 6 |
| vaccination_study_04 | Platelet | 6 |
| vaccination_study_04 | Treg | 2 |
| vaccination_study_04 | Memory B Cell | 2 |

## Inline Figures

### vaccination_study_04

![vaccination_study_04 final labels](assets/umap_vaccination_study_04_annotation_label.png)

![vaccination_study_04 lineage and annotation reason](assets/umap_vaccination_study_04_annotation_lineage_reason.png)

![vaccination_study_04 QC and confidence](assets/umap_vaccination_study_04_annotation_qc_confidence.png)

![vaccination_study_04 source agreement and disagreement](assets/umap_vaccination_study_04_annotation_source_disagreement.png)

![vaccination_study_04 marker expression UMAPs](assets/umap_vaccination_study_04_annotation_marker_expression.png)

![vaccination_study_04 submitted-label marker dotplot](assets/dotplot_vaccination_study_04_annotation_marker_dotplot.png)

#### vaccination_study_04 B_lineage true subcluster UMAP

![vaccination_study_04 B_lineage true subcluster labels](assets/umap_vaccination_study_04_B_lineage_true_subcluster_label.png)

![vaccination_study_04 B_lineage true subcluster QC](assets/umap_vaccination_study_04_B_lineage_true_subcluster_qc.png)

![vaccination_study_04 B_lineage true subcluster marker scores](assets/umap_vaccination_study_04_B_lineage_true_subcluster_marker_scores.png)

![vaccination_study_04 B_lineage true subcluster marker expression](assets/umap_vaccination_study_04_B_lineage_true_subcluster_marker_expression.png)

![vaccination_study_04 B_lineage subcluster marker score heatmap](assets/subcluster_marker_score_heatmap_vaccination_study_04_B_lineage.png)

![vaccination_study_04 B_lineage subcluster marker dotplot](assets/dotplot_vaccination_study_04_B_lineage_true_subcluster_marker_dotplot.png)

Tables: `tables/vaccination_study_04_B_lineage_true_subcluster_umap.tsv.gz`, `tables/vaccination_study_04_B_lineage_subcluster_candidate_scores.tsv`.

#### vaccination_study_04 T_NK_lineage true subcluster UMAP

![vaccination_study_04 T_NK_lineage true subcluster labels](assets/umap_vaccination_study_04_T_NK_lineage_true_subcluster_label.png)

![vaccination_study_04 T_NK_lineage true subcluster QC](assets/umap_vaccination_study_04_T_NK_lineage_true_subcluster_qc.png)

![vaccination_study_04 T_NK_lineage true subcluster marker scores](assets/umap_vaccination_study_04_T_NK_lineage_true_subcluster_marker_scores.png)

![vaccination_study_04 T_NK_lineage true subcluster marker expression](assets/umap_vaccination_study_04_T_NK_lineage_true_subcluster_marker_expression.png)

![vaccination_study_04 T_NK_lineage subcluster marker score heatmap](assets/subcluster_marker_score_heatmap_vaccination_study_04_T_NK_lineage.png)

![vaccination_study_04 T_NK_lineage subcluster marker dotplot](assets/dotplot_vaccination_study_04_T_NK_lineage_true_subcluster_marker_dotplot.png)

Tables: `tables/vaccination_study_04_T_NK_lineage_true_subcluster_umap.tsv.gz`, `tables/vaccination_study_04_T_NK_lineage_subcluster_candidate_scores.tsv`.

#### vaccination_study_04 Myeloid_lineage true subcluster UMAP

![vaccination_study_04 Myeloid_lineage true subcluster labels](assets/umap_vaccination_study_04_Myeloid_lineage_true_subcluster_label.png)

![vaccination_study_04 Myeloid_lineage true subcluster QC](assets/umap_vaccination_study_04_Myeloid_lineage_true_subcluster_qc.png)

![vaccination_study_04 Myeloid_lineage true subcluster marker scores](assets/umap_vaccination_study_04_Myeloid_lineage_true_subcluster_marker_scores.png)

![vaccination_study_04 Myeloid_lineage true subcluster marker expression](assets/umap_vaccination_study_04_Myeloid_lineage_true_subcluster_marker_expression.png)

![vaccination_study_04 Myeloid_lineage subcluster marker score heatmap](assets/subcluster_marker_score_heatmap_vaccination_study_04_Myeloid_lineage.png)

![vaccination_study_04 Myeloid_lineage subcluster marker dotplot](assets/dotplot_vaccination_study_04_Myeloid_lineage_true_subcluster_marker_dotplot.png)

Tables: `tables/vaccination_study_04_Myeloid_lineage_true_subcluster_umap.tsv.gz`, `tables/vaccination_study_04_Myeloid_lineage_subcluster_candidate_scores.tsv`.


## Subcluster Marker Score Review

上の lineage-specific panel は、各 lineage subset で HVG 選択、PCA、neighbors、Leiden、UMAP を再計算した true local subcluster analysis から生成しています。Marker gene による fine label の確認は global UMAP だけではなく、この local UMAP、marker-score UMAP、marker-expression UMAP、dotplot を主に見ます。

## Cluster Consensus Evidence

| study | lineage | cluster | cells | chosen_label | accepted | score_margin | marker_set | marker_alert |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| vaccination_study_04 | B_lineage | 0 | 15 | Plasma Cell | True | 3.157 | Plasma_ASC | pass |
| vaccination_study_04 | B_lineage | 1 | 11 | Plasma Cell | True | 2.920 | Plasma_ASC | pass |
| vaccination_study_04 | B_lineage | 2 | 9 | Plasma Cell | True | 2.761 | Plasma_ASC | pass |
| vaccination_study_04 | B_lineage | 3 | 9 | Plasma Cell | True | 1.823 | Plasma_ASC | pass |
| vaccination_study_04 | B_lineage | 4 | 8 | Plasma Cell | True | 2.658 | Plasma_ASC | pass |
| vaccination_study_04 | B_lineage | 5 | 8 | Plasma Cell | True | 3.110 | Plasma_ASC | pass |
| vaccination_study_04 | B_lineage | 6 | 6 | Plasma Cell | True | 2.623 | Plasma_ASC | pass |
| vaccination_study_04 | B_lineage | 7 | 6 | Plasma Cell | True | 3.129 | Plasma_ASC | pass |
| vaccination_study_04 | B_lineage | 10 | 4 | Plasma Cell | True | 3.157 | Plasma_ASC | pass |
| vaccination_study_04 | B_lineage | 11 | 4 | Naive B Cell | True | 0.106 | B_naive | pass |
| vaccination_study_04 | B_lineage | 12 | 4 | Plasma Cell | True | 2.657 | Plasma_ASC | pass |
| vaccination_study_04 | B_lineage | 13 | 4 | Plasma Cell | True | 3.157 | Plasma_ASC | pass |
| vaccination_study_04 | B_lineage | 8 | 4 | Plasma Cell | True | 2.798 | Plasma_ASC | pass |
| vaccination_study_04 | B_lineage | 9 | 4 | Plasma Cell | True | 3.113 | Plasma_ASC | pass |
| vaccination_study_04 | B_lineage | 14 | 2 | Plasma Cell | True | 3.157 | Plasma_ASC | pass |
| vaccination_study_04 | B_lineage | 15 | 2 | Naive B Cell | True | 2.304 | B_naive | pass |
| vaccination_study_04 | B_lineage | 16 | 2 | Plasma Cell | True | 2.610 | Plasma_ASC | pass |
| vaccination_study_04 | B_lineage | 17 | 2 | Memory B Cell | True | 2.184 | B_memory_ABC | pass |
| vaccination_study_04 | B_lineage | 18 | 2 | Plasma Cell | True | 3.145 | Plasma_ASC | pass |
| vaccination_study_04 | B_lineage | 19 | 2 | Plasma Cell | True | 2.599 | Plasma_ASC | pass |
| vaccination_study_04 | Myeloid_lineage | 0 | 5,841 | Non-Classical Monocyte | True | 2.214 | not_applicable | pass |
| vaccination_study_04 | Myeloid_lineage | 1 | 5,555 | Classical Monocyte | True | 2.803 | not_applicable | pass |
| vaccination_study_04 | Myeloid_lineage | 2 | 4,757 | Classical Monocyte | True | 2.156 | not_applicable | pass |
| vaccination_study_04 | Myeloid_lineage | 3 | 3,925 | Classical Monocyte | True | 2.295 | not_applicable | pass |
| vaccination_study_04 | Myeloid_lineage | 4 | 3,738 | Conventional DC 2 | True | 2.428 | not_applicable | pass |
| vaccination_study_04 | Myeloid_lineage | 5 | 3,249 | Classical Monocyte | True | 2.968 | not_applicable | pass |
| vaccination_study_04 | Myeloid_lineage | 6 | 3,204 | Classical Monocyte | True | 2.937 | not_applicable | pass |
| vaccination_study_04 | Myeloid_lineage | 7 | 3,037 | Classical Monocyte | True | 2.710 | not_applicable | pass |
| vaccination_study_04 | Myeloid_lineage | 8 | 2,683 | Classical Monocyte | True | 3.111 | not_applicable | pass |
| vaccination_study_04 | Myeloid_lineage | 9 | 2,474 | Plasmacytoid DC | True | 2.781 | not_applicable | pass |

## 出力ファイル

- Submission TSVs: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_clean_v16/vaccination_study_04/submissions/`
- cellxgene H5ADs: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_clean_v16/vaccination_study_04/cellxgene/`
- Marker availability table: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_clean_v16/vaccination_study_04/tables/marker_gene_availability.tsv`
- Marker availability alerts: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_clean_v16/vaccination_study_04/tables/marker_gene_availability_alerts.tsv`
- Subcluster evidence: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_clean_v16/vaccination_study_04/tables/lineage_subcluster_evidence.tsv.gz`
- Source disagreement summary: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_clean_v16/vaccination_study_04/tables/source_disagreement_summary.tsv`
- Diagnostics tables: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_clean_v16/vaccination_study_04/tables/`

