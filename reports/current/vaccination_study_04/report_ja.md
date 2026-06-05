# HIPC データセットアノテーションレポート: vaccination_study_04

更新日: 2026-06-05 EDT

このレポートは `hipc-annotation` Codex workflow によって生成したデータセット別レビュー文書です。固定 method は repository README に置き、このレポートでは実際の evidence、弱い箇所、レビュー優先度、UMAP / dotplot を確認します。

## データセット概要

| study | cells | analysis_X_genes | pre_hvg_genes | counts_layer_genes | labels | parent_or_blood_fraction | Blood Cell | Doublet | artifact_like | median_confidence | low_confidence | source_disagreement | invalid_labels |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| vaccination_study_04 | 66,065 | 16,983 | 16,983 | 16,983 | 11 | 0.011 | 718 | 647 | 217 | 0.777 | 1,423 | 2,900 (0.044) | none |

## 実行概要

- 実行単位: one dataset in, one annotated dataset out。
- 実行経路: Codex skill `hipc-annotation` -> bundled helper `run_one.sh` -> annotation CLI -> validator -> report inspection。
- 検証: submission row count、H5AD observation count、official label validity、H5AD/submission agreement、confidence column、report image link を確認する。
- このレポートは workflow の再掲ではなく、このデータセットの marker 欠損、UMAP、label 構成、review concern を読むためのもの。

## データセット固有の解釈

- `vaccination_study_04`: 66,065 cells、analysis X/var 16,983 genes、pre-HVG slot 16,983 genes、submitted label 11 種、parent/Blood residual fraction 0.011、median confidence 0.777。
  - 1,423 cells は low confidence。QC / confidence UMAP 上で局在を確認する。
  - 647 cells は `Doublet` として提出。mixed-lineage marker expression と scrublet support を確認する。
  - 718 cells は `Blood Cell` として残存。これは filter-out ではなく、曖昧な細胞を公式 parent label で残したもの。
  - Marker gene 欠損アラート: Treg, gdT。該当 marker set に依存する fine label は慎重に見る。

## データセット固有の評価

- 全体像: 66,065 cells / analysis X/var 16,983 genes / pre-HVG slot 16,983 genes。parent/Blood residual は 0.011、low-confidence は 1,423 cells、source disagreement flag は 2,900 cells (0.044)。
- 優先確認: low-confidence 領域が QC UMAP と source-disagreement UMAP で同じ場所に集まるかを確認する。
- 優先確認: `Blood Cell` 残存が孤立 cluster なのか、複数 lineage に分散した曖昧領域なのかを UMAP で確認する。
- Marker gene 欠損: Treg, gdT は confidence cap 対象。該当 label は marker expression UMAP と dotplot で妥当性を確認する。

## Marker Gene 欠損アラート

| study | marker_set | alert | present_fraction | missing_critical_markers | missing_genes |
| --- | --- | --- | --- | --- | --- |
| vaccination_study_04 | Treg | critical | 0.286 | FOXP3;IL2RA | FOXP3;IL2RA;TIGIT;TNFRSF18;CCR8 |
| vaccination_study_04 | gdT | critical | 0.167 | TRDC;TRGC1;TRGC2 | CD3D;TRDC;TRGC1;TRGC2;TRDV2 |

## ソース間不一致

| study | predicted_cell_type | cells | median_source_agreement | disagreement_cells | disagreement_fraction |
| --- | --- | --- | --- | --- | --- |
| vaccination_study_04 | Doublet | 647 | 0.000 | 647 | 1.000 |
| vaccination_study_04 | CD4 Naive / T Central Memory | 29 | 0.500 | 11 | 0.379 |
| vaccination_study_04 | NK Cell | 234 | 1.000 | 46 | 0.197 |
| vaccination_study_04 | Conventional DC 2 | 7,930 | 1.000 | 1,023 | 0.129 |
| vaccination_study_04 | Plasma Cell | 109 | 0.750 | 12 | 0.110 |
| vaccination_study_04 | Blood Cell | 718 | 1.000 | 37 | 0.052 |
| vaccination_study_04 | Conventional DC 1 | 1,110 | 1.000 | 33 | 0.030 |
| vaccination_study_04 | Classical Monocyte | 34,011 | 1.000 | 922 | 0.027 |
| vaccination_study_04 | Plasmacytoid DC | 5,506 | 1.000 | 55 | 0.010 |
| vaccination_study_04 | Non-Classical Monocyte | 15,554 | 1.000 | 114 | 0.007 |
| vaccination_study_04 | HSC | 217 | 0.667 | 0 | 0.000 |

## レビュー優先事項

| study | concern | cells |
| --- | --- | --- |
| vaccination_study_04 | High source disagreement for Doublet | 647 |

## ラベル構成

| study | predicted_cell_type | cells |
| --- | --- | --- |
| vaccination_study_04 | Classical Monocyte | 34,011 |
| vaccination_study_04 | Non-Classical Monocyte | 15,554 |
| vaccination_study_04 | Conventional DC 2 | 7,930 |
| vaccination_study_04 | Plasmacytoid DC | 5,506 |
| vaccination_study_04 | Conventional DC 1 | 1,110 |
| vaccination_study_04 | Blood Cell | 718 |
| vaccination_study_04 | Doublet | 647 |
| vaccination_study_04 | NK Cell | 234 |
| vaccination_study_04 | HSC | 217 |
| vaccination_study_04 | Plasma Cell | 109 |
| vaccination_study_04 | CD4 Naive / T Central Memory | 29 |

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

![vaccination_study_04 B_lineage true subcluster source labels](assets/umap_vaccination_study_04_B_lineage_true_subcluster_source_labels.png)

![vaccination_study_04 B_lineage true subcluster QC](assets/umap_vaccination_study_04_B_lineage_true_subcluster_qc.png)

![vaccination_study_04 B_lineage true subcluster marker scores](assets/umap_vaccination_study_04_B_lineage_true_subcluster_marker_scores.png)

![vaccination_study_04 B_lineage true subcluster marker expression](assets/umap_vaccination_study_04_B_lineage_true_subcluster_marker_expression.png)

![vaccination_study_04 B_lineage subcluster marker score heatmap](assets/subcluster_marker_score_heatmap_vaccination_study_04_B_lineage.png)

![vaccination_study_04 B_lineage subcluster marker dotplot](assets/dotplot_vaccination_study_04_B_lineage_true_subcluster_marker_dotplot.png)

Tables: `tables/vaccination_study_04_B_lineage_true_subcluster_umap.tsv.gz`, `tables/vaccination_study_04_B_lineage_subcluster_candidate_scores.tsv`.

#### vaccination_study_04 T_NK_lineage true subcluster UMAP

![vaccination_study_04 T_NK_lineage true subcluster labels](assets/umap_vaccination_study_04_T_NK_lineage_true_subcluster_label.png)

![vaccination_study_04 T_NK_lineage true subcluster source labels](assets/umap_vaccination_study_04_T_NK_lineage_true_subcluster_source_labels.png)

![vaccination_study_04 T_NK_lineage true subcluster QC](assets/umap_vaccination_study_04_T_NK_lineage_true_subcluster_qc.png)

![vaccination_study_04 T_NK_lineage true subcluster marker scores](assets/umap_vaccination_study_04_T_NK_lineage_true_subcluster_marker_scores.png)

![vaccination_study_04 T_NK_lineage true subcluster marker expression](assets/umap_vaccination_study_04_T_NK_lineage_true_subcluster_marker_expression.png)

![vaccination_study_04 T_NK_lineage subcluster marker score heatmap](assets/subcluster_marker_score_heatmap_vaccination_study_04_T_NK_lineage.png)

![vaccination_study_04 T_NK_lineage subcluster marker dotplot](assets/dotplot_vaccination_study_04_T_NK_lineage_true_subcluster_marker_dotplot.png)

Tables: `tables/vaccination_study_04_T_NK_lineage_true_subcluster_umap.tsv.gz`, `tables/vaccination_study_04_T_NK_lineage_subcluster_candidate_scores.tsv`.

#### vaccination_study_04 Myeloid_lineage true subcluster UMAP

![vaccination_study_04 Myeloid_lineage true subcluster labels](assets/umap_vaccination_study_04_Myeloid_lineage_true_subcluster_label.png)

![vaccination_study_04 Myeloid_lineage true subcluster source labels](assets/umap_vaccination_study_04_Myeloid_lineage_true_subcluster_source_labels.png)

![vaccination_study_04 Myeloid_lineage true subcluster QC](assets/umap_vaccination_study_04_Myeloid_lineage_true_subcluster_qc.png)

![vaccination_study_04 Myeloid_lineage true subcluster marker scores](assets/umap_vaccination_study_04_Myeloid_lineage_true_subcluster_marker_scores.png)

![vaccination_study_04 Myeloid_lineage true subcluster marker expression](assets/umap_vaccination_study_04_Myeloid_lineage_true_subcluster_marker_expression.png)

![vaccination_study_04 Myeloid_lineage subcluster marker score heatmap](assets/subcluster_marker_score_heatmap_vaccination_study_04_Myeloid_lineage.png)

![vaccination_study_04 Myeloid_lineage subcluster marker dotplot](assets/dotplot_vaccination_study_04_Myeloid_lineage_true_subcluster_marker_dotplot.png)

Tables: `tables/vaccination_study_04_Myeloid_lineage_true_subcluster_umap.tsv.gz`, `tables/vaccination_study_04_Myeloid_lineage_subcluster_candidate_scores.tsv`.


## Subcluster Marker Score Review

上の lineage-specific panel は、各 lineage subset で HVG 選択、PCA、neighbors、Leiden、UMAP を再計算した true local subcluster analysis から生成しています。Marker gene による fine label の確認は global UMAP だけではなく、この local UMAP、CellTypist/Azimuth/Pan-human/cluster-level marker gene assignment overlay、cluster marker gate score UMAP、marker-expression UMAP、dotplot を主に見ます。Treg など sparse marker label は cell-wise marker winner ではなく、local cluster の FOXP3/IL2RA/CTLA4 など key-marker support と reference support で判定します。

## Marker Assignment Feedback

Marker gene assignment は final label を強制的に上書きするものではなく、cluster-level の自己点検です。`raw_marker_winner` は marker score だけの勝者、`marker_assignment` は conservative policy と source-supported tie-break を通した marker-based assignment です。この表は marker assignment と final/reference-driven label がずれる cluster、marker specificity が弱い cluster、scRefMap が期待される lineage で欠落する cluster を示します。`marker_score` は raw marker base score から negative/confound marker penalty を差し引いた cluster-level marker gate score です。

| study | lineage | cluster | cells | chosen_label | marker_assignment | raw_marker_winner | assignment_reason | marker_score | base_score | penalty | flags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| vaccination_study_04 | Myeloid_lineage | 25 | 701 | Conventional DC 1 | Intermediate Monocyte | Intermediate Monocyte | raw_marker_winner | 0.816 | 1.000 | 0.184 | marker_final_disagreement |
| vaccination_study_04 | Myeloid_lineage | 26 | 664 | Non-Classical Monocyte | Intermediate Monocyte | Intermediate Monocyte | raw_marker_winner | 0.764 | 1.000 | 0.236 | marker_final_disagreement |
| vaccination_study_04 | Myeloid_lineage | 28 | 439 | Classical Monocyte | Intermediate Monocyte | Intermediate Monocyte | raw_marker_winner | 0.689 | 1.000 | 0.311 | marker_final_disagreement |
| vaccination_study_04 | Myeloid_lineage | 30 | 409 | Conventional DC 1 | Intermediate Monocyte | Intermediate Monocyte | raw_marker_winner | 0.827 | 0.995 | 0.168 | marker_final_disagreement |
| vaccination_study_04 | T_NK_lineage | 0 | 32 | NK Cell | NK Cell | NKT Cell | conservative_policy_blocks_raw_marker_winner | 0.925 | 1.000 | 0.075 | screfmapping_missing_for_scope |
| vaccination_study_04 | T_NK_lineage | 1 | 29 | NK Cell | NK Cell | NKT Cell | conservative_policy_blocks_raw_marker_winner | 0.876 | 1.000 | 0.124 | screfmapping_missing_for_scope |
| vaccination_study_04 | T_NK_lineage | 3 | 26 | NK Cell | NK Cell | NKT Cell | conservative_policy_blocks_raw_marker_winner | 0.908 | 1.000 | 0.092 | screfmapping_missing_for_scope |
| vaccination_study_04 | T_NK_lineage | 4 | 24 | NK Cell | NK Cell | NKT Cell | conservative_policy_blocks_raw_marker_winner | 1.000 | 1.000 | 0.000 | screfmapping_missing_for_scope |
| vaccination_study_04 | T_NK_lineage | 6 | 18 | NK Cell | NK Cell | NKT Cell | conservative_policy_blocks_raw_marker_winner | 0.867 | 1.000 | 0.133 | screfmapping_missing_for_scope |
| vaccination_study_04 | T_NK_lineage | 7 | 17 | NK Cell | NK Cell | NKT Cell | conservative_policy_blocks_raw_marker_winner | 0.929 | 1.000 | 0.071 | screfmapping_missing_for_scope |
| vaccination_study_04 | T_NK_lineage | 8 | 16 | NK Cell | NK Cell | NKT Cell | conservative_policy_blocks_raw_marker_winner | 0.963 | 1.000 | 0.037 | screfmapping_missing_for_scope |
| vaccination_study_04 | T_NK_lineage | 9 | 16 | NK Cell | NK Cell | NK Cell | raw_marker_winner | 0.969 | 1.000 | 0.031 | screfmapping_missing_for_scope |
| vaccination_study_04 | B_lineage | 1 | 11 | Plasma Cell | Memory B Cell | Memory B Cell | raw_marker_winner | 0.660 | 1.000 | 0.340 | marker_final_disagreement |
| vaccination_study_04 | B_lineage | 2 | 11 | Plasma Cell | Plasmablast | Plasmablast | raw_marker_winner | 0.732 | 1.000 | 0.268 | marker_final_disagreement |
| vaccination_study_04 | T_NK_lineage | 13 | 8 | NK Cell | NK Cell | NK Cell | raw_marker_winner | 0.877 | 1.000 | 0.122 | screfmapping_missing_for_scope |
| vaccination_study_04 | T_NK_lineage | 12 | 8 | NK Cell | NK Cell | NKT Cell | conservative_policy_blocks_raw_marker_winner | 1.000 | 1.000 | 0.000 | screfmapping_missing_for_scope |

## Cluster Consensus Evidence

| study | lineage | cluster | cells | chosen_label | accepted | score_margin | cluster_marker_assignment | treg_key_any | treg_key_bonus | marker_set | marker_alert |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| vaccination_study_04 | B_lineage | 0 | 12 | Plasma Cell | True | 1.683 | Plasma Cell | nan | nan | Plasma_ASC | pass |
| vaccination_study_04 | B_lineage | 1 | 11 | Plasma Cell | True | 0.268 | Memory B Cell | nan | nan | Plasma_ASC | pass |
| vaccination_study_04 | B_lineage | 2 | 11 | Plasma Cell | True | 0.923 | Plasmablast | nan | nan | Plasma_ASC | pass |
| vaccination_study_04 | B_lineage | 3 | 10 | Plasma Cell | True | 2.715 | Plasma Cell | nan | nan | Plasma_ASC | pass |
| vaccination_study_04 | B_lineage | 4 | 8 | Plasma Cell | True | 2.629 | Plasma Cell | nan | nan | Plasma_ASC | pass |
| vaccination_study_04 | B_lineage | 5 | 6 | Plasma Cell | True | 2.517 | Plasma Cell | nan | nan | Plasma_ASC | pass |
| vaccination_study_04 | B_lineage | 6 | 6 | Plasma Cell | True | 0.267 | Plasma Cell | nan | nan | Plasma_ASC | pass |
| vaccination_study_04 | B_lineage | 7 | 5 | Plasma Cell | True | 2.446 | Plasma Cell | nan | nan | Plasma_ASC | pass |
| vaccination_study_04 | B_lineage | 10 | 4 | Plasma Cell | True | 2.500 | Plasma Cell | nan | nan | Plasma_ASC | pass |
| vaccination_study_04 | B_lineage | 11 | 4 | Plasma Cell | True | 2.065 | Plasma Cell | nan | nan | Plasma_ASC | pass |
| vaccination_study_04 | B_lineage | 12 | 4 | Plasma Cell | True | 1.268 | Plasma Cell | nan | nan | Plasma_ASC | pass |
| vaccination_study_04 | B_lineage | 13 | 4 | Plasma Cell | True | 0.368 | Plasma Cell | nan | nan | Plasma_ASC | pass |
| vaccination_study_04 | B_lineage | 14 | 4 | Plasma Cell | True | 1.643 | Plasma Cell | nan | nan | Plasma_ASC | pass |
| vaccination_study_04 | B_lineage | 15 | 4 | Plasma Cell | True | 2.688 | Plasma Cell | nan | nan | Plasma_ASC | pass |
| vaccination_study_04 | B_lineage | 8 | 4 | Plasma Cell | True | 2.186 | Plasma Cell | nan | nan | Plasma_ASC | pass |
| vaccination_study_04 | B_lineage | 9 | 4 | Plasma Cell | True | 1.868 | Plasma Cell | nan | nan | Plasma_ASC | pass |
| vaccination_study_04 | B_lineage | 16 | 2 | Plasma Cell | True | 1.986 | Plasma Cell | nan | nan | Plasma_ASC | pass |
| vaccination_study_04 | B_lineage | 17 | 2 | Plasma Cell | True | 1.800 | Plasma Cell | nan | nan | Plasma_ASC | pass |
| vaccination_study_04 | B_lineage | 18 | 2 | Plasma Cell | True | 1.800 | Plasma Cell | nan | nan | Plasma_ASC | pass |
| vaccination_study_04 | B_lineage | 19 | 2 | Plasma Cell | True | 1.800 | Plasma Cell | nan | nan | Plasma_ASC | pass |
| vaccination_study_04 | Myeloid_lineage | 0 | 5,906 | Non-Classical Monocyte | True | 1.663 | Non-Classical Monocyte | nan | nan | not_applicable | pass |
| vaccination_study_04 | Myeloid_lineage | 1 | 4,352 | Classical Monocyte | True | 2.228 | Classical Monocyte | nan | nan | not_applicable | pass |
| vaccination_study_04 | Myeloid_lineage | 2 | 3,545 | Classical Monocyte | True | 2.396 | Classical Monocyte | nan | nan | not_applicable | pass |
| vaccination_study_04 | Myeloid_lineage | 3 | 3,507 | Classical Monocyte | True | 2.449 | Classical Monocyte | nan | nan | not_applicable | pass |
| vaccination_study_04 | Myeloid_lineage | 4 | 3,491 | Classical Monocyte | True | 2.296 | Classical Monocyte | nan | nan | not_applicable | pass |
| vaccination_study_04 | Myeloid_lineage | 5 | 3,482 | Classical Monocyte | True | 2.405 | Classical Monocyte | nan | nan | not_applicable | pass |
| vaccination_study_04 | Myeloid_lineage | 6 | 3,185 | Classical Monocyte | True | 2.432 | Classical Monocyte | nan | nan | not_applicable | pass |
| vaccination_study_04 | Myeloid_lineage | 7 | 2,934 | Classical Monocyte | True | 2.450 | Classical Monocyte | nan | nan | not_applicable | pass |
| vaccination_study_04 | Myeloid_lineage | 8 | 2,475 | Plasmacytoid DC | True | 2.580 | Plasmacytoid DC | nan | nan | not_applicable | pass |
| vaccination_study_04 | Myeloid_lineage | 9 | 2,442 | Classical Monocyte | True | 2.413 | Classical Monocyte | nan | nan | not_applicable | pass |

## 出力ファイル

- Submission TSVs: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_clean_v19/vaccination_study_04/submissions/`
- cellxgene H5ADs: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_clean_v19/vaccination_study_04/cellxgene/`
- Marker availability table: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_clean_v19/vaccination_study_04/tables/marker_gene_availability.tsv`
- Marker availability alerts: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_clean_v19/vaccination_study_04/tables/marker_gene_availability_alerts.tsv`
- Subcluster evidence: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_clean_v19/vaccination_study_04/tables/lineage_subcluster_evidence.tsv.gz`
- Source disagreement summary: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_clean_v19/vaccination_study_04/tables/source_disagreement_summary.tsv`
- Diagnostics tables: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_clean_v19/vaccination_study_04/tables/`

