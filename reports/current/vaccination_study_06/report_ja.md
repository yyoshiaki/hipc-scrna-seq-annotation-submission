# HIPC データセットアノテーションレポート: vaccination_study_06

更新日: 2026-06-04 EDT

このレポートは `hipc-annotation` Codex workflow によって生成したデータセット別レビュー文書です。固定 method は repository README に置き、このレポートでは実際の evidence、弱い箇所、レビュー優先度、UMAP / dotplot を確認します。

## データセット概要

| study | cells | analysis_X_genes | pre_hvg_genes | counts_layer_genes | labels | parent_or_blood_fraction | Blood Cell | Doublet | artifact_like | median_confidence | low_confidence | source_disagreement | invalid_labels |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| vaccination_study_06 | 57,419 | 11,878 | 11,878 | 11,878 | 10 | 0.019 | 1,090 | 1,502 | 0 | 0.711 | 11,348 | 10,623 (0.185) | none |

## 実行概要

- 実行単位: one dataset in, one annotated dataset out。
- 実行経路: Codex skill `hipc-annotation` -> bundled helper `run_one.sh` -> annotation CLI -> validator -> report inspection。
- 検証: submission row count、H5AD observation count、official label validity、H5AD/submission agreement、confidence column、report image link を確認する。
- このレポートは workflow の再掲ではなく、このデータセットの marker 欠損、UMAP、label 構成、review concern を読むためのもの。

## データセット固有の解釈

- `vaccination_study_06`: 57,419 cells、analysis X/var 11,878 genes、pre-HVG slot 11,878 genes、submitted label 10 種、parent/Blood residual fraction 0.019、median confidence 0.711。
  - 11,348 cells は low confidence。QC / confidence UMAP 上で局在を確認する。
  - 1,502 cells は `Doublet` として提出。mixed-lineage marker expression と scrublet support を確認する。
  - 1,090 cells は `Blood Cell` として残存。これは filter-out ではなく、曖昧な細胞を公式 parent label で残したもの。
  - Marker gene 欠損アラート: Treg, Plasma_ASC。該当 marker set に依存する fine label は慎重に見る。

## データセット固有の評価

- 全体像: 57,419 cells / analysis X/var 11,878 genes / pre-HVG slot 11,878 genes。parent/Blood residual は 0.019、low-confidence は 11,348 cells、source disagreement flag は 10,623 cells (0.185)。
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
| vaccination_study_06 | Plasma Cell | 204 | 0.333 | 203 | 0.995 |
| vaccination_study_06 | Naive B Cell | 630 | 0.250 | 383 | 0.608 |
| vaccination_study_06 | Memory B Cell | 3,189 | 0.500 | 1,454 | 0.456 |
| vaccination_study_06 | MAIT Cell | 1,383 | 0.667 | 368 | 0.266 |
| vaccination_study_06 | CD8 Cytotoxic / T Effector Memory | 9,155 | 0.667 | 2,074 | 0.227 |
| vaccination_study_06 | CD8 Naive / T Central Memory | 878 | 0.667 | 130 | 0.148 |
| vaccination_study_06 | NK Cell | 10,329 | 0.667 | 1,264 | 0.122 |
| vaccination_study_06 | Blood Cell | 1,090 | 0.667 | 125 | 0.115 |
| vaccination_study_06 | CD4 Naive / T Central Memory | 29,059 | 0.750 | 3,120 | 0.107 |

## レビュー優先事項

| study | concern | cells |
| --- | --- | --- |
| vaccination_study_06 | High source disagreement for Doublet | 1,502 |
| vaccination_study_06 | High source disagreement for Naive B Cell | 383 |
| vaccination_study_06 | High source disagreement for Plasma Cell | 203 |
| vaccination_study_06 | warning marker availability for Plasma_ASC | 204 |
| vaccination_study_06 | Large Blood Cell/ambiguous residual remains | 1,090 |
| vaccination_study_06 | Many low-confidence cells; QC or mixed-marker effects likely remain | 11,348 |

## ラベル構成

| study | predicted_cell_type | cells |
| --- | --- | --- |
| vaccination_study_06 | CD4 Naive / T Central Memory | 29,059 |
| vaccination_study_06 | NK Cell | 10,329 |
| vaccination_study_06 | CD8 Cytotoxic / T Effector Memory | 9,155 |
| vaccination_study_06 | Memory B Cell | 3,189 |
| vaccination_study_06 | Doublet | 1,502 |
| vaccination_study_06 | MAIT Cell | 1,383 |
| vaccination_study_06 | Blood Cell | 1,090 |
| vaccination_study_06 | CD8 Naive / T Central Memory | 878 |
| vaccination_study_06 | Naive B Cell | 630 |
| vaccination_study_06 | Plasma Cell | 204 |

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

Skipped: fewer than 50 cells assigned to this broad lineage (`n_cells=46`).

Tables: `tables/vaccination_study_06_Myeloid_lineage_true_subcluster_umap.tsv.gz`, `tables/vaccination_study_06_Myeloid_lineage_subcluster_candidate_scores.tsv`.


## Subcluster Marker Score Review

上の lineage-specific panel は、各 lineage subset で HVG 選択、PCA、neighbors、Leiden、UMAP を再計算した true local subcluster analysis から生成しています。Marker gene による fine label の確認は global UMAP だけではなく、この local UMAP、CellTypist/Azimuth/Pan-human/cluster-level marker gene assignment overlay、cluster marker gate score UMAP、marker-expression UMAP、dotplot を主に見ます。Treg など sparse marker label は cell-wise marker winner ではなく、local cluster の FOXP3/IL2RA/CTLA4 など key-marker support と reference support で判定します。

## Marker Assignment Feedback

Marker gene assignment は final label を強制的に上書きするものではなく、cluster-level の自己点検です。この表は marker-only assignment と final/reference-driven label がずれる cluster、marker specificity が弱い cluster、scRefMap が期待される lineage で欠落する cluster を示します。`marker_score` は raw marker base score から negative/confound marker penalty を差し引いた cluster-level marker gate score です。

| study | lineage | cluster | cells | chosen_label | marker_assignment | marker_score | base_score | penalty | flags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| vaccination_study_06 | T_NK_lineage | 1 | 3,202 | CD4 Naive / T Central Memory | CD8 Naive / T Central Memory | 0.266 | 0.496 | 0.230 | marker_final_disagreement;weak_marker_specificity |
| vaccination_study_06 | T_NK_lineage | 2 | 3,197 | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | 0.597 | 1.000 | 0.403 | screfmapping_missing_for_scope |
| vaccination_study_06 | T_NK_lineage | 3 | 2,956 | NK Cell | NK Cell | 0.799 | 1.000 | 0.201 | screfmapping_missing_for_scope |
| vaccination_study_06 | T_NK_lineage | 5 | 2,655 | NK Cell | NK Cell | 0.856 | 1.000 | 0.144 | screfmapping_missing_for_scope |
| vaccination_study_06 | T_NK_lineage | 7 | 2,496 | CD4 Naive / T Central Memory | CD4 Naive / T Central Memory | 0.328 | 0.561 | 0.233 | weak_marker_specificity |
| vaccination_study_06 | T_NK_lineage | 8 | 2,424 | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | 0.468 | 1.000 | 0.532 | screfmapping_missing_for_scope |
| vaccination_study_06 | T_NK_lineage | 13 | 1,966 | CD4 Naive / T Central Memory | CD8 Naive / T Central Memory | 0.732 | 1.000 | 0.268 | marker_final_disagreement |
| vaccination_study_06 | T_NK_lineage | 15 | 1,632 | NK Cell | NK Cell | 0.767 | 1.000 | 0.233 | screfmapping_missing_for_scope |
| vaccination_study_06 | T_NK_lineage | 16 | 1,440 | CD8 Cytotoxic / T Effector Memory | MAIT Cell | 0.509 | 0.783 | 0.274 | marker_final_disagreement |
| vaccination_study_06 | T_NK_lineage | 17 | 1,383 | MAIT Cell | MAIT Cell | 0.588 | 1.000 | 0.412 | screfmapping_missing_for_scope |
| vaccination_study_06 | T_NK_lineage | 18 | 1,292 | NK Cell | NK Cell | 0.826 | 1.000 | 0.174 | screfmapping_missing_for_scope |
| vaccination_study_06 | T_NK_lineage | 19 | 1,017 | CD4 Naive / T Central Memory | CD8 Naive / T Central Memory | 0.777 | 1.000 | 0.223 | marker_final_disagreement |
| vaccination_study_06 | T_NK_lineage | 20 | 967 | CD8 Cytotoxic / T Effector Memory | CD8 Naive / T Central Memory | 0.484 | 0.990 | 0.506 | marker_final_disagreement;screfmapping_missing_for_scope |
| vaccination_study_06 | T_NK_lineage | 22 | 859 | NK Cell | MAIT Cell | 0.562 | 1.000 | 0.438 | marker_final_disagreement;screfmapping_missing_for_scope |
| vaccination_study_06 | T_NK_lineage | 24 | 698 | CD8 Cytotoxic / T Effector Memory | CD8 Naive / T Central Memory | 0.494 | 1.000 | 0.506 | marker_final_disagreement;screfmapping_missing_for_scope |
| vaccination_study_06 | T_NK_lineage | 25 | 596 | NK Cell | NK Cell | 0.552 | 1.000 | 0.448 | screfmapping_missing_for_scope |
| vaccination_study_06 | T_NK_lineage | 26 | 429 | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | 0.597 | 1.000 | 0.403 | screfmapping_missing_for_scope |
| vaccination_study_06 | T_NK_lineage | 27 | 363 | CD4 Naive / T Central Memory | NK Cell | 0.563 | 1.000 | 0.437 | marker_final_disagreement |
| vaccination_study_06 | B_lineage | 1 | 334 | Memory B Cell | Naive B Cell | 0.171 | 0.278 | 0.107 | marker_final_disagreement;weak_marker_specificity |
| vaccination_study_06 | B_lineage | 2 | 318 | Memory B Cell | Naive B Cell | 0.864 | 1.000 | 0.136 | marker_final_disagreement |

## Cluster Consensus Evidence

| study | lineage | cluster | cells | chosen_label | accepted | score_margin | cluster_marker_assignment | treg_key_any | treg_key_bonus | marker_set | marker_alert |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| vaccination_study_06 | B_lineage | 0 | 365 | Naive B Cell | True | 0.610 | Naive B Cell | nan | nan | B_naive | pass |
| vaccination_study_06 | B_lineage | 1 | 334 | Memory B Cell | True | 1.131 | Naive B Cell | nan | nan | B_memory_ABC | pass |
| vaccination_study_06 | B_lineage | 2 | 318 | Memory B Cell | True | 0.331 | Naive B Cell | nan | nan | B_memory_ABC | pass |
| vaccination_study_06 | B_lineage | 3 | 296 | Memory B Cell | True | 1.249 | Naive B Cell | nan | nan | B_memory_ABC | pass |
| vaccination_study_06 | B_lineage | 4 | 294 | Memory B Cell | True | 2.636 | Naive B Cell | nan | nan | B_memory_ABC | pass |
| vaccination_study_06 | B_lineage | 5 | 278 | Memory B Cell | True | 2.761 | Plasma Cell | nan | nan | B_memory_ABC | pass |
| vaccination_study_06 | B_lineage | 6 | 269 | Memory B Cell | True | 2.141 | Naive B Cell | nan | nan | B_memory_ABC | pass |
| vaccination_study_06 | B_lineage | 7 | 265 | Naive B Cell | True | 0.027 | Naive B Cell | nan | nan | B_naive | pass |
| vaccination_study_06 | B_lineage | 8 | 251 | Memory B Cell | True | 2.825 | Naive B Cell | nan | nan | B_memory_ABC | pass |
| vaccination_study_06 | B_lineage | 9 | 209 | Memory B Cell | True | 1.442 | Naive B Cell | nan | nan | B_memory_ABC | pass |
| vaccination_study_06 | B_lineage | 10 | 204 | Plasma Cell | True | 1.676 | Plasma Cell | nan | nan | Plasma_ASC | warning |
| vaccination_study_06 | B_lineage | 11 | 199 | Memory B Cell | True | 2.197 | Memory B Cell | nan | nan | B_memory_ABC | pass |
| vaccination_study_06 | B_lineage | 12 | 173 | Memory B Cell | True | 0.191 | Naive B Cell | nan | nan | B_memory_ABC | pass |
| vaccination_study_06 | B_lineage | 13 | 169 | Memory B Cell | True | 3.235 | Naive B Cell | nan | nan | B_memory_ABC | pass |
| vaccination_study_06 | B_lineage | 14 | 131 | Memory B Cell | True | 1.832 | Naive B Cell | nan | nan | B_memory_ABC | pass |
| vaccination_study_06 | B_lineage | 15 | 98 | Memory B Cell | True | 1.998 | Naive B Cell | nan | nan | B_memory_ABC | pass |
| vaccination_study_06 | B_lineage | 16 | 86 | Memory B Cell | True | 2.556 | Naive B Cell | nan | nan | B_memory_ABC | pass |
| vaccination_study_06 | B_lineage | 17 | 84 | Memory B Cell | True | 0.939 | Memory B Cell | nan | nan | B_memory_ABC | pass |
| vaccination_study_06 | T_NK_lineage | 0 | 3,691 | CD4 Naive / T Central Memory | True | 2.615 | CD4 Naive / T Central Memory | 0.148 | 0.000 | CD4_naive_tcm | pass |
| vaccination_study_06 | T_NK_lineage | 1 | 3,202 | CD4 Naive / T Central Memory | True | 1.665 | CD8 Naive / T Central Memory | 0.156 | 0.000 | CD4_naive_tcm | pass |
| vaccination_study_06 | T_NK_lineage | 2 | 3,197 | CD8 Cytotoxic / T Effector Memory | True | 1.403 | CD8 Cytotoxic / T Effector Memory | 0.020 | 0.000 | not_applicable | pass |
| vaccination_study_06 | T_NK_lineage | 3 | 2,956 | NK Cell | True | 2.820 | NK Cell | 0.014 | 0.000 | not_applicable | pass |
| vaccination_study_06 | T_NK_lineage | 4 | 2,879 | CD4 Naive / T Central Memory | True | 2.853 | CD4 Naive / T Central Memory | 0.146 | 0.000 | CD4_naive_tcm | pass |
| vaccination_study_06 | T_NK_lineage | 5 | 2,655 | NK Cell | True | 2.557 | NK Cell | 0.019 | 0.000 | not_applicable | pass |
| vaccination_study_06 | T_NK_lineage | 6 | 2,549 | CD4 Naive / T Central Memory | True | 2.531 | CD4 Naive / T Central Memory | 0.168 | 0.000 | CD4_naive_tcm | pass |
| vaccination_study_06 | T_NK_lineage | 7 | 2,496 | CD4 Naive / T Central Memory | True | 2.054 | CD4 Naive / T Central Memory | 0.129 | 0.000 | CD4_naive_tcm | pass |
| vaccination_study_06 | T_NK_lineage | 8 | 2,424 | CD8 Cytotoxic / T Effector Memory | True | 1.510 | CD8 Cytotoxic / T Effector Memory | 0.031 | 0.000 | not_applicable | pass |
| vaccination_study_06 | T_NK_lineage | 9 | 2,258 | CD4 Naive / T Central Memory | True | 2.840 | CD4 Naive / T Central Memory | 0.167 | 0.000 | CD4_naive_tcm | pass |
| vaccination_study_06 | T_NK_lineage | 10 | 2,037 | CD4 Naive / T Central Memory | True | 2.576 | CD4 Naive / T Central Memory | 0.224 | 0.000 | CD4_naive_tcm | pass |
| vaccination_study_06 | T_NK_lineage | 11 | 2,030 | CD4 Naive / T Central Memory | True | 1.329 | CD4 Naive / T Central Memory | 0.100 | 0.000 | CD4_naive_tcm | pass |

## 出力ファイル

- Submission TSVs: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_clean_v18_obsfix/vaccination_study_06/submissions/`
- cellxgene H5ADs: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_clean_v18_obsfix/vaccination_study_06/cellxgene/`
- Marker availability table: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_clean_v18_obsfix/vaccination_study_06/tables/marker_gene_availability.tsv`
- Marker availability alerts: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_clean_v18_obsfix/vaccination_study_06/tables/marker_gene_availability_alerts.tsv`
- Subcluster evidence: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_clean_v18_obsfix/vaccination_study_06/tables/lineage_subcluster_evidence.tsv.gz`
- Source disagreement summary: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_clean_v18_obsfix/vaccination_study_06/tables/source_disagreement_summary.tsv`
- Diagnostics tables: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_clean_v18_obsfix/vaccination_study_06/tables/`

