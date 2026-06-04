# HIPC データセットアノテーションレポート: infection_study_01

更新日: 2026-06-04 EDT

このレポートは `hipc-annotation` Codex workflow によって生成したデータセット別レビュー文書です。固定 method は repository README に置き、このレポートでは実際の evidence、弱い箇所、レビュー優先度、UMAP / dotplot を確認します。

## データセット概要

| study | cells | analysis_X_genes | pre_hvg_genes | counts_layer_genes | labels | parent_or_blood_fraction | Blood Cell | Doublet | artifact_like | median_confidence | low_confidence | source_disagreement | invalid_labels |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| infection_study_01 | 54,924 | 33,538 | 33,538 | 33,538 | 19 | 0.006 | 326 | 1,278 | 1,350 | 0.850 | 3,691 | 7,485 (0.136) | none |

## 実行概要

- 実行単位: one dataset in, one annotated dataset out。
- 実行経路: Codex skill `hipc-annotation` -> bundled helper `run_one.sh` -> annotation CLI -> validator -> report inspection。
- 検証: submission row count、H5AD observation count、official label validity、H5AD/submission agreement、confidence column、report image link を確認する。
- このレポートは workflow の再掲ではなく、このデータセットの marker 欠損、UMAP、label 構成、review concern を読むためのもの。

## データセット固有の解釈

- `infection_study_01`: 54,924 cells、analysis X/var 33,538 genes、pre-HVG slot 33,538 genes、submitted label 19 種、parent/Blood residual fraction 0.006、median confidence 0.850。
  - 3,691 cells は low confidence。QC / confidence UMAP 上で局在を確認する。
  - 1,278 cells は `Doublet` として提出。mixed-lineage marker expression と scrublet support を確認する。
  - 326 cells は `Blood Cell` として残存。これは filter-out ではなく、曖昧な細胞を公式 parent label で残したもの。

## データセット固有の評価

- 全体像: 54,924 cells / analysis X/var 33,538 genes / pre-HVG slot 33,538 genes。parent/Blood residual は 0.006、low-confidence は 3,691 cells、source disagreement flag は 7,485 cells (0.136)。
- 優先確認: low-confidence 領域が QC UMAP と source-disagreement UMAP で同じ場所に集まるかを確認する。
- 優先確認: `Blood Cell` 残存が孤立 cluster なのか、複数 lineage に分散した曖昧領域なのかを UMAP で確認する。

## Marker Gene 欠損アラート

なし。

## ソース間不一致

| study | predicted_cell_type | cells | median_source_agreement | disagreement_cells | disagreement_fraction |
| --- | --- | --- | --- | --- | --- |
| infection_study_01 | Doublet | 1,278 | 0.000 | 1,278 | 1.000 |
| infection_study_01 | Treg | 718 | 0.000 | 493 | 0.687 |
| infection_study_01 | MAIT Cell | 976 | 0.250 | 501 | 0.513 |
| infection_study_01 | Blood Cell | 326 | 0.250 | 167 | 0.512 |
| infection_study_01 | Plasma Cell | 183 | 0.500 | 76 | 0.415 |
| infection_study_01 | Memory B Cell | 2,114 | 0.500 | 408 | 0.193 |
| infection_study_01 | CD4 T Effector Memory | 2,985 | 0.500 | 550 | 0.184 |
| infection_study_01 | Plasmacytoid DC | 107 | 0.750 | 19 | 0.178 |
| infection_study_01 | CD4 Naive / T Central Memory | 2,240 | 0.750 | 367 | 0.164 |
| infection_study_01 | NK Cell | 9,487 | 0.750 | 1,376 | 0.145 |
| infection_study_01 | CD8 Cytotoxic / T Effector Memory | 9,195 | 0.750 | 934 | 0.102 |
| infection_study_01 | Non-Classical Monocyte | 2,036 | 1.000 | 159 | 0.078 |

## レビュー優先事項

| study | concern | cells |
| --- | --- | --- |
| infection_study_01 | High source disagreement for Blood Cell | 167 |
| infection_study_01 | High source disagreement for Doublet | 1,278 |
| infection_study_01 | High source disagreement for MAIT Cell | 501 |
| infection_study_01 | High source disagreement for Treg | 493 |

## ラベル構成

| study | predicted_cell_type | cells |
| --- | --- | --- |
| infection_study_01 | Classical Monocyte | 17,218 |
| infection_study_01 | NK Cell | 9,487 |
| infection_study_01 | CD8 Cytotoxic / T Effector Memory | 9,195 |
| infection_study_01 | Naive B Cell | 4,235 |
| infection_study_01 | CD4 T Effector Memory | 2,985 |
| infection_study_01 | CD4 Naive / T Central Memory | 2,240 |
| infection_study_01 | Memory B Cell | 2,114 |
| infection_study_01 | Non-Classical Monocyte | 2,036 |
| infection_study_01 | Platelet | 1,336 |
| infection_study_01 | Doublet | 1,278 |
| infection_study_01 | MAIT Cell | 976 |
| infection_study_01 | Treg | 718 |
| infection_study_01 | Conventional DC 2 | 442 |
| infection_study_01 | Blood Cell | 326 |
| infection_study_01 | Plasma Cell | 183 |
| infection_study_01 | Plasmacytoid DC | 107 |
| infection_study_01 | Conventional DC 1 | 34 |
| infection_study_01 | HSC | 13 |
| infection_study_01 | RBC | 1 |

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

## Cluster Consensus Evidence

| study | lineage | cluster | cells | chosen_label | accepted | score_margin | cluster_marker_assignment | treg_key_any | treg_key_bonus | marker_set | marker_alert |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| infection_study_01 | B_lineage | 0 | 491 | Naive B Cell | True | 3.047 | Naive B Cell | nan | nan | B_naive | pass |
| infection_study_01 | B_lineage | 1 | 464 | Naive B Cell | True | 3.184 | Naive B Cell | nan | nan | B_naive | pass |
| infection_study_01 | B_lineage | 2 | 431 | Naive B Cell | True | 3.039 | Naive B Cell | nan | nan | B_naive | pass |
| infection_study_01 | B_lineage | 3 | 396 | Naive B Cell | True | 3.065 | Naive B Cell | nan | nan | B_naive | pass |
| infection_study_01 | B_lineage | 4 | 351 | Memory B Cell | True | 1.526 | Naive B Cell | nan | nan | B_memory_ABC | pass |
| infection_study_01 | B_lineage | 5 | 342 | Naive B Cell | True | 2.887 | Naive B Cell | nan | nan | B_naive | pass |
| infection_study_01 | B_lineage | 6 | 321 | Memory B Cell | True | 2.526 | Naive B Cell | nan | nan | B_memory_ABC | pass |
| infection_study_01 | B_lineage | 7 | 317 | Memory B Cell | True | 1.854 | Naive B Cell | nan | nan | B_memory_ABC | pass |
| infection_study_01 | B_lineage | 8 | 309 | Memory B Cell | True | 2.047 | Naive B Cell | nan | nan | B_memory_ABC | pass |
| infection_study_01 | B_lineage | 9 | 306 | Memory B Cell | True | 2.311 | Naive B Cell | nan | nan | B_memory_ABC | pass |
| infection_study_01 | B_lineage | 10 | 286 | Naive B Cell | True | 2.717 | Naive B Cell | nan | nan | B_naive | pass |
| infection_study_01 | B_lineage | 11 | 277 | Naive B Cell | True | 2.709 | Naive B Cell | nan | nan | B_naive | pass |
| infection_study_01 | B_lineage | 12 | 275 | Naive B Cell | True | 3.072 | Naive B Cell | nan | nan | B_naive | pass |
| infection_study_01 | B_lineage | 13 | 236 | Naive B Cell | True | 1.778 | Naive B Cell | nan | nan | B_naive | pass |
| infection_study_01 | B_lineage | 14 | 229 | Naive B Cell | True | 1.941 | Naive B Cell | nan | nan | B_naive | pass |
| infection_study_01 | B_lineage | 15 | 221 | Memory B Cell | True | 2.378 | Naive B Cell | nan | nan | B_memory_ABC | pass |
| infection_study_01 | B_lineage | 16 | 221 | Naive B Cell | True | 3.093 | Naive B Cell | nan | nan | B_naive | pass |
| infection_study_01 | B_lineage | 17 | 208 | Memory B Cell | True | 2.197 | Naive B Cell | nan | nan | B_memory_ABC | pass |
| infection_study_01 | B_lineage | 18 | 172 | Naive B Cell | True | 2.436 | Naive B Cell | nan | nan | B_naive | pass |
| infection_study_01 | B_lineage | 19 | 165 | Naive B Cell | True | 2.938 | Naive B Cell | nan | nan | B_naive | pass |
| infection_study_01 | B_lineage | 20 | 118 | Naive B Cell | True | 0.024 | Naive B Cell | nan | nan | B_naive | pass |
| infection_study_01 | B_lineage | 21 | 95 | Naive B Cell | True | 2.975 | Naive B Cell | nan | nan | B_naive | pass |
| infection_study_01 | B_lineage | 22 | 85 | Plasma Cell | True | 2.612 | Plasma Cell | nan | nan | Plasma_ASC | pass |
| infection_study_01 | B_lineage | 23 | 81 | Memory B Cell | True | 2.330 | Naive B Cell | nan | nan | B_memory_ABC | pass |
| infection_study_01 | B_lineage | 24 | 56 | Plasma Cell | True | 2.101 | Plasma Cell | nan | nan | Plasma_ASC | pass |
| infection_study_01 | B_lineage | 25 | 42 | Plasma Cell | True | 2.729 | Plasma Cell | nan | nan | Plasma_ASC | pass |
| infection_study_01 | B_lineage | 26 | 37 | Naive B Cell | True | 0.962 | Naive B Cell | nan | nan | B_naive | pass |
| infection_study_01 | Myeloid_lineage | 0 | 1,504 | Classical Monocyte | True | 2.551 | Classical Monocyte | nan | nan | not_applicable | pass |
| infection_study_01 | Myeloid_lineage | 1 | 1,418 | Classical Monocyte | True | 1.907 | Classical Monocyte | nan | nan | not_applicable | pass |
| infection_study_01 | Myeloid_lineage | 2 | 1,344 | Non-Classical Monocyte | True | 1.493 | Non-Classical Monocyte | nan | nan | not_applicable | pass |

## 出力ファイル

- Submission TSVs: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_clean_v17/infection_study_01/submissions/`
- cellxgene H5ADs: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_clean_v17/infection_study_01/cellxgene/`
- Marker availability table: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_clean_v17/infection_study_01/tables/marker_gene_availability.tsv`
- Marker availability alerts: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_clean_v17/infection_study_01/tables/marker_gene_availability_alerts.tsv`
- Subcluster evidence: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_clean_v17/infection_study_01/tables/lineage_subcluster_evidence.tsv.gz`
- Source disagreement summary: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_clean_v17/infection_study_01/tables/source_disagreement_summary.tsv`
- Diagnostics tables: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_clean_v17/infection_study_01/tables/`

