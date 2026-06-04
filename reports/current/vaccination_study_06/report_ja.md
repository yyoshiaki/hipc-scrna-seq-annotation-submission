# HIPC データセットアノテーションレポート: vaccination_study_06

更新日: 2026-06-04 EDT

このレポートは `hipc-annotation` Codex workflow によって生成したデータセット別レビュー文書です。固定 method は repository README に置き、このレポートでは実際の evidence、弱い箇所、レビュー優先度、UMAP / dotplot を確認します。

## データセット概要

| study | cells | analysis_X_genes | pre_hvg_genes | counts_layer_genes | labels | parent_or_blood_fraction | Blood Cell | Doublet | artifact_like | median_confidence | low_confidence | source_disagreement | invalid_labels |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| vaccination_study_06 | 57,419 | 11,878 | 11,878 | 11,878 | 10 | 0.017 | 992 | 1,502 | 0 | 0.713 | 2,494 | 16,255 (0.283) | none |

## 実行概要

- 実行単位: one dataset in, one annotated dataset out。
- 実行経路: Codex skill `hipc-annotation` -> bundled helper `run_one.sh` -> annotation CLI -> validator -> report inspection。
- 検証: submission row count、H5AD observation count、official label validity、H5AD/submission agreement、confidence column、report image link を確認する。
- このレポートは workflow の再掲ではなく、このデータセットの marker 欠損、UMAP、label 構成、review concern を読むためのもの。

## データセット固有の解釈

- `vaccination_study_06`: 57,419 cells、analysis X/var 11,878 genes、pre-HVG slot 11,878 genes、submitted label 10 種、parent/Blood residual fraction 0.017、median confidence 0.713。
  - 2,494 cells は low confidence。QC / confidence UMAP 上で局在を確認する。
  - 1,502 cells は `Doublet` として提出。mixed-lineage marker expression と scrublet support を確認する。
  - 992 cells は `Blood Cell` として残存。これは filter-out ではなく、曖昧な細胞を公式 parent label で残したもの。
  - Marker gene 欠損アラート: Treg, Plasma_ASC。該当 marker set に依存する fine label は慎重に見る。

## データセット固有の評価

- 全体像: 57,419 cells / analysis X/var 11,878 genes / pre-HVG slot 11,878 genes。parent/Blood residual は 0.017、low-confidence は 2,494 cells、source disagreement flag は 16,255 cells (0.283)。
- 優先確認: low-confidence 領域が QC UMAP と source-disagreement UMAP で同じ場所に集まるかを確認する。
- 優先確認: `Blood Cell` 残存が孤立 cluster なのか、複数 lineage に分散した曖昧領域なのかを UMAP で確認する。
- Marker gene 欠損: Treg, Plasma_ASC は confidence cap 対象。該当 label は marker expression UMAP と dotplot で妥当性を確認する。

## Marker Gene 欠損アラート

| study | marker_set | alert | present_fraction | missing_critical_markers | missing_genes |
| --- | --- | --- | --- | --- | --- |
| vaccination_study_06 | Treg | warning | 0.714 | FOXP3 | FOXP3;CCR8 |
| vaccination_study_06 | Plasma_ASC | warning | 0.444 | JCHAIN | JCHAIN;SDC1;TNFRSF17;IGHG1;IGHA1 |

## ソース間不一致

| study | predicted_cell_type | cells | median_source_agreement | disagreement_cells | disagreement_fraction |
| --- | --- | --- | --- | --- | --- |
| vaccination_study_06 | Doublet | 1,502 | 0.000 | 1,502 | 1.000 |
| vaccination_study_06 | Plasma Cell | 180 | 0.250 | 161 | 0.894 |
| vaccination_study_06 | Memory B Cell | 3,619 | 0.250 | 2,305 | 0.637 |
| vaccination_study_06 | Naive B Cell | 201 | 0.250 | 105 | 0.522 |
| vaccination_study_06 | CD4 Naive / T Central Memory | 29,433 | 0.500 | 8,608 | 0.292 |
| vaccination_study_06 | MAIT Cell | 1,404 | 0.500 | 359 | 0.256 |
| vaccination_study_06 | CD8 Cytotoxic / T Effector Memory | 9,129 | 0.750 | 1,987 | 0.218 |
| vaccination_study_06 | Blood Cell | 992 | 0.500 | 202 | 0.204 |
| vaccination_study_06 | CD8 Naive / T Central Memory | 872 | 0.750 | 104 | 0.119 |
| vaccination_study_06 | NK Cell | 10,087 | 0.750 | 922 | 0.091 |

## レビュー優先事項

| study | concern | cells |
| --- | --- | --- |
| vaccination_study_06 | High source disagreement for Doublet | 1,502 |
| vaccination_study_06 | High source disagreement for Memory B Cell | 2,305 |
| vaccination_study_06 | High source disagreement for Naive B Cell | 105 |
| vaccination_study_06 | High source disagreement for Plasma Cell | 161 |
| vaccination_study_06 | High dataset-level source disagreement | 16,255 |
| vaccination_study_06 | warning marker availability for Plasma_ASC | 180 |

## ラベル構成

| study | predicted_cell_type | cells |
| --- | --- | --- |
| vaccination_study_06 | CD4 Naive / T Central Memory | 29,433 |
| vaccination_study_06 | NK Cell | 10,087 |
| vaccination_study_06 | CD8 Cytotoxic / T Effector Memory | 9,129 |
| vaccination_study_06 | Memory B Cell | 3,619 |
| vaccination_study_06 | Doublet | 1,502 |
| vaccination_study_06 | MAIT Cell | 1,404 |
| vaccination_study_06 | Blood Cell | 992 |
| vaccination_study_06 | CD8 Naive / T Central Memory | 872 |
| vaccination_study_06 | Naive B Cell | 201 |
| vaccination_study_06 | Plasma Cell | 180 |

## Inline Figures

### vaccination_study_06

![vaccination_study_06 final labels](assets/umap_vaccination_study_06_annotation_label.png)

![vaccination_study_06 lineage and annotation reason](assets/umap_vaccination_study_06_annotation_lineage_reason.png)

![vaccination_study_06 QC and confidence](assets/umap_vaccination_study_06_annotation_qc_confidence.png)

![vaccination_study_06 source agreement and disagreement](assets/umap_vaccination_study_06_annotation_source_disagreement.png)

![vaccination_study_06 marker expression UMAPs](assets/umap_vaccination_study_06_annotation_marker_expression.png)

![vaccination_study_06 submitted-label marker dotplot](assets/dotplot_vaccination_study_06_annotation_marker_dotplot.png)

#### vaccination_study_06 B_lineage true subcluster UMAP

![vaccination_study_06 B_lineage true subcluster labels](assets/umap_vaccination_study_06_B_lineage_true_subcluster_label.png)

![vaccination_study_06 B_lineage true subcluster source labels](assets/umap_vaccination_study_06_B_lineage_true_subcluster_source_labels.png)

![vaccination_study_06 B_lineage true subcluster QC](assets/umap_vaccination_study_06_B_lineage_true_subcluster_qc.png)

![vaccination_study_06 B_lineage true subcluster marker scores](assets/umap_vaccination_study_06_B_lineage_true_subcluster_marker_scores.png)

![vaccination_study_06 B_lineage true subcluster marker expression](assets/umap_vaccination_study_06_B_lineage_true_subcluster_marker_expression.png)

![vaccination_study_06 B_lineage subcluster marker score heatmap](assets/subcluster_marker_score_heatmap_vaccination_study_06_B_lineage.png)

![vaccination_study_06 B_lineage subcluster marker dotplot](assets/dotplot_vaccination_study_06_B_lineage_true_subcluster_marker_dotplot.png)

Tables: `tables/vaccination_study_06_B_lineage_true_subcluster_umap.tsv.gz`, `tables/vaccination_study_06_B_lineage_subcluster_candidate_scores.tsv`.

#### vaccination_study_06 T_NK_lineage true subcluster UMAP

![vaccination_study_06 T_NK_lineage true subcluster labels](assets/umap_vaccination_study_06_T_NK_lineage_true_subcluster_label.png)

![vaccination_study_06 T_NK_lineage true subcluster source labels](assets/umap_vaccination_study_06_T_NK_lineage_true_subcluster_source_labels.png)

![vaccination_study_06 T_NK_lineage true subcluster QC](assets/umap_vaccination_study_06_T_NK_lineage_true_subcluster_qc.png)

![vaccination_study_06 T_NK_lineage true subcluster marker scores](assets/umap_vaccination_study_06_T_NK_lineage_true_subcluster_marker_scores.png)

![vaccination_study_06 T_NK_lineage true subcluster marker expression](assets/umap_vaccination_study_06_T_NK_lineage_true_subcluster_marker_expression.png)

![vaccination_study_06 T_NK_lineage subcluster marker score heatmap](assets/subcluster_marker_score_heatmap_vaccination_study_06_T_NK_lineage.png)

![vaccination_study_06 T_NK_lineage subcluster marker dotplot](assets/dotplot_vaccination_study_06_T_NK_lineage_true_subcluster_marker_dotplot.png)

Tables: `tables/vaccination_study_06_T_NK_lineage_true_subcluster_umap.tsv.gz`, `tables/vaccination_study_06_T_NK_lineage_subcluster_candidate_scores.tsv`.

#### vaccination_study_06 Myeloid_lineage true subcluster UMAP

Skipped: fewer than 50 cells assigned to this broad lineage (`n_cells=45`).

Tables: `tables/vaccination_study_06_Myeloid_lineage_true_subcluster_umap.tsv.gz`, `tables/vaccination_study_06_Myeloid_lineage_subcluster_candidate_scores.tsv`.


## Subcluster Marker Score Review

上の lineage-specific panel は、各 lineage subset で HVG 選択、PCA、neighbors、Leiden、UMAP を再計算した true local subcluster analysis から生成しています。Marker gene による fine label の確認は global UMAP だけではなく、この local UMAP、CellTypist/Azimuth/Pan-human/cluster-level marker gene assignment overlay、cluster marker gate score UMAP、marker-expression UMAP、dotplot を主に見ます。Treg など sparse marker label は cell-wise marker winner ではなく、local cluster の FOXP3/IL2RA/CTLA4 など key-marker support と reference support で判定します。

## Cluster Consensus Evidence

| study | lineage | cluster | cells | chosen_label | accepted | score_margin | cluster_marker_assignment | treg_key_any | treg_key_bonus | marker_set | marker_alert |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| vaccination_study_06 | B_lineage | 0 | 345 | Memory B Cell | True | 2.101 | Naive B Cell | nan | nan | B_memory_ABC | pass |
| vaccination_study_06 | B_lineage | 1 | 336 | Memory B Cell | True | 1.137 | Naive B Cell | nan | nan | B_memory_ABC | pass |
| vaccination_study_06 | B_lineage | 2 | 306 | Memory B Cell | True | 1.370 | Naive B Cell | nan | nan | B_memory_ABC | pass |
| vaccination_study_06 | B_lineage | 3 | 302 | Memory B Cell | True | 1.158 | Naive B Cell | nan | nan | B_memory_ABC | pass |
| vaccination_study_06 | B_lineage | 4 | 298 | Memory B Cell | True | 0.934 | Naive B Cell | nan | nan | B_memory_ABC | pass |
| vaccination_study_06 | B_lineage | 5 | 282 | Memory B Cell | True | 2.143 | Naive B Cell | nan | nan | B_memory_ABC | pass |
| vaccination_study_06 | B_lineage | 6 | 279 | Memory B Cell | True | 2.098 | Naive B Cell | nan | nan | B_memory_ABC | pass |
| vaccination_study_06 | B_lineage | 7 | 268 | Memory B Cell | True | 2.047 | Naive B Cell | nan | nan | B_memory_ABC | pass |
| vaccination_study_06 | B_lineage | 8 | 264 | Memory B Cell | True | 0.513 | Naive B Cell | nan | nan | B_memory_ABC | pass |
| vaccination_study_06 | B_lineage | 9 | 221 | Memory B Cell | True | 1.783 | Naive B Cell | nan | nan | B_memory_ABC | pass |
| vaccination_study_06 | B_lineage | 10 | 201 | Naive B Cell | True | 0.141 | Naive B Cell | nan | nan | B_naive | pass |
| vaccination_study_06 | B_lineage | 11 | 199 | Memory B Cell | True | 1.498 | Naive B Cell | nan | nan | B_memory_ABC | pass |
| vaccination_study_06 | B_lineage | 12 | 180 | Plasma Cell | True | 1.626 | Naive B Cell | nan | nan | Plasma_ASC | warning |
| vaccination_study_06 | B_lineage | 13 | 154 | Memory B Cell | True | 1.573 | Naive B Cell | nan | nan | B_memory_ABC | pass |
| vaccination_study_06 | B_lineage | 14 | 129 | Memory B Cell | True | 1.386 | Naive B Cell | nan | nan | B_memory_ABC | pass |
| vaccination_study_06 | B_lineage | 15 | 94 | Memory B Cell | True | 0.759 | Naive B Cell | nan | nan | B_memory_ABC | pass |
| vaccination_study_06 | B_lineage | 16 | 92 | Memory B Cell | True | 0.811 | Naive B Cell | nan | nan | B_memory_ABC | pass |
| vaccination_study_06 | B_lineage | 17 | 50 | Memory B Cell | True | 1.606 | Naive B Cell | nan | nan | B_memory_ABC | pass |
| vaccination_study_06 | T_NK_lineage | 0 | 3,945 | CD4 Naive / T Central Memory | True | 1.593 | CD4 Naive / T Central Memory | 0.160 | 0.000 | CD4_naive_tcm | pass |
| vaccination_study_06 | T_NK_lineage | 1 | 3,362 | CD4 Naive / T Central Memory | True | 1.165 | CD4 Naive / T Central Memory | 0.133 | 0.000 | CD4_naive_tcm | pass |
| vaccination_study_06 | T_NK_lineage | 2 | 3,164 | CD8 Cytotoxic / T Effector Memory | True | 1.304 | CD4 T Effector Memory | 0.020 | 0.000 | not_applicable | pass |
| vaccination_study_06 | T_NK_lineage | 3 | 3,066 | CD4 Naive / T Central Memory | True | 0.431 | CD4 Naive / T Central Memory | 0.093 | 0.000 | CD4_naive_tcm | pass |
| vaccination_study_06 | T_NK_lineage | 4 | 2,854 | CD4 Naive / T Central Memory | True | 1.480 | CD4 Naive / T Central Memory | 0.116 | 0.000 | CD4_naive_tcm | pass |
| vaccination_study_06 | T_NK_lineage | 5 | 2,812 | NK Cell | True | 2.456 | NK Cell | 0.011 | 0.000 | not_applicable | pass |
| vaccination_study_06 | T_NK_lineage | 6 | 2,655 | NK Cell | True | 2.214 | NK Cell | 0.018 | 0.000 | not_applicable | pass |
| vaccination_study_06 | T_NK_lineage | 7 | 2,424 | CD8 Cytotoxic / T Effector Memory | True | 1.434 | CD4 Naive / T Central Memory | 0.029 | 0.000 | not_applicable | pass |
| vaccination_study_06 | T_NK_lineage | 8 | 2,204 | CD4 Naive / T Central Memory | True | 1.018 | CD4 Naive / T Central Memory | 0.216 | 0.000 | CD4_naive_tcm | pass |
| vaccination_study_06 | T_NK_lineage | 9 | 2,063 | CD4 Naive / T Central Memory | True | 1.578 | CD4 Naive / T Central Memory | 0.180 | 0.000 | CD4_naive_tcm | pass |
| vaccination_study_06 | T_NK_lineage | 10 | 2,054 | CD4 Naive / T Central Memory | True | 1.748 | CD4 Naive / T Central Memory | 0.132 | 0.000 | CD4_naive_tcm | pass |
| vaccination_study_06 | T_NK_lineage | 11 | 1,975 | CD4 Naive / T Central Memory | True | 1.455 | CD4 Naive / T Central Memory | 0.154 | 0.000 | CD4_naive_tcm | pass |

## 出力ファイル

- Submission TSVs: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_clean_v17/vaccination_study_06/submissions/`
- cellxgene H5ADs: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_clean_v17/vaccination_study_06/cellxgene/`
- Marker availability table: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_clean_v17/vaccination_study_06/tables/marker_gene_availability.tsv`
- Marker availability alerts: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_clean_v17/vaccination_study_06/tables/marker_gene_availability_alerts.tsv`
- Subcluster evidence: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_clean_v17/vaccination_study_06/tables/lineage_subcluster_evidence.tsv.gz`
- Source disagreement summary: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_clean_v17/vaccination_study_06/tables/source_disagreement_summary.tsv`
- Diagnostics tables: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_clean_v17/vaccination_study_06/tables/`

