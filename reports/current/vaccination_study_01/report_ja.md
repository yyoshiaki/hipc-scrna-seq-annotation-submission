# HIPC データセットアノテーションレポート: vaccination_study_01

更新日: 2026-06-05 EDT

このレポートは `hipc-annotation` Codex workflow によって生成したデータセット別レビュー文書です。固定 method は repository README に置き、このレポートでは実際の evidence、弱い箇所、レビュー優先度、UMAP / dotplot を確認します。

## データセット概要

| study | cells | analysis_X_genes | pre_hvg_genes | counts_layer_genes | labels | parent_or_blood_fraction | Blood Cell | Doublet | artifact_like | median_confidence | low_confidence | source_disagreement | invalid_labels |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| vaccination_study_01 | 307,194 | 10,528 | 10,528 | 10,528 | 4 | 1.000 | 83,760 | 0 | 0 | 0.437 | 307,194 | 0 (0.000) | none |

## 実行概要

- 実行単位: one dataset in, one annotated dataset out。
- 実行経路: Codex skill `hipc-annotation` -> bundled helper `run_one.sh` -> annotation CLI -> validator -> report inspection。
- 検証: submission row count、H5AD observation count、official label validity、H5AD/submission agreement、confidence column、report image link を確認する。
- このレポートは workflow の再掲ではなく、このデータセットの marker 欠損、UMAP、label 構成、review concern を読むためのもの。

## データセット固有の解釈

- `vaccination_study_01`: 307,194 cells、analysis X/var 10,528 genes、pre-HVG slot 10,528 genes、submitted label 4 種、parent/Blood residual fraction 1.000、median confidence 0.437。
  - 307,194 cells は low confidence。QC / confidence UMAP 上で局在を確認する。
  - 83,760 cells は `Blood Cell` として残存。これは filter-out ではなく、曖昧な細胞を公式 parent label で残したもの。
  - Marker gene 欠損アラート: Treg。該当 marker set に依存する fine label は慎重に見る。

## データセット固有の評価

- 全体像: 307,194 cells / analysis X/var 10,528 genes / pre-HVG slot 10,528 genes。parent/Blood residual は 1.000、low-confidence は 307,194 cells、source disagreement flag は 0 cells (0.000)。
- 優先確認: low-confidence 領域が QC UMAP と source-disagreement UMAP で同じ場所に集まるかを確認する。
- 優先確認: `Blood Cell` 残存が孤立 cluster なのか、複数 lineage に分散した曖昧領域なのかを UMAP で確認する。
- Marker gene 欠損: Treg は confidence cap 対象。該当 label は marker expression UMAP と dotplot で妥当性を確認する。

## Marker Gene 欠損アラート

| study | marker_set | alert | present_fraction | missing_critical_markers | missing_genes |
| --- | --- | --- | --- | --- | --- |
| vaccination_study_01 | Treg | critical | 0.143 | FOXP3;IL2RA;CTLA4 | FOXP3;IL2RA;CTLA4;TIGIT;TNFRSF18;CCR8 |

## ソース間不一致

| study | predicted_cell_type | cells | median_source_agreement | disagreement_cells | disagreement_fraction |
| --- | --- | --- | --- | --- | --- |
| vaccination_study_01 | B Cell | 40,449 | 0.000 | 0 | 0.000 |
| vaccination_study_01 | Blood Cell | 83,760 | 0.000 | 0 | 0.000 |
| vaccination_study_01 | Myeloid Cell | 86,258 | 0.000 | 0 | 0.000 |
| vaccination_study_01 | T Cell | 96,727 | 0.000 | 0 | 0.000 |

## アノテーションソース効果

この表は外部 ground truth に対する正解率ではありません。各 annotation source がどれだけの細胞で情報を持ち、final label とどれだけ一致したかを示す監査用統計です。`coverage` は source が `not_available` 以外を返した割合、`final_concordance` は informative cells の中で final label と一致した割合、`unique_support` はその source だけが final label と一致した細胞数です。

| study | source | informative_cells | coverage | final_concordance | high_conf_concordance | unique_support | discordant |
| --- | --- | --- | --- | --- | --- | --- | --- |
| vaccination_study_01 | Cluster marker assignment | 223,434 | 0.727 | 0.000 | 0.000 | 0 | 223,434 |
| vaccination_study_01 | CellTypist | 0 | 0.000 | 0.000 | 0.000 | 0 | 0 |
| vaccination_study_01 | Pan-human Azimuth | 0 | 0.000 | 0.000 | 0.000 | 0 | 0 |
| vaccination_study_01 | Cluster consensus | 0 | 0.000 | 0.000 | 0.000 | 0 | 0 |
| vaccination_study_01 | scRefMapping | 0 | 0.000 | 0.000 | 0.000 | 0 | 0 |

## レビュー優先事項

| study | concern | cells |
| --- | --- | --- |
| vaccination_study_01 | Large Blood Cell/ambiguous residual remains | 83,760 |
| vaccination_study_01 | Many low-confidence cells; QC or mixed-marker effects likely remain | 307,194 |

## ラベル構成

| study | predicted_cell_type | cells |
| --- | --- | --- |
| vaccination_study_01 | T Cell | 96,727 |
| vaccination_study_01 | Myeloid Cell | 86,258 |
| vaccination_study_01 | Blood Cell | 83,760 |
| vaccination_study_01 | B Cell | 40,449 |

## Inline Figures

### vaccination_study_01

![vaccination_study_01 final labels](assets/umap_vaccination_study_01_annotation_label.png)

![vaccination_study_01 lineage and annotation reason](assets/umap_vaccination_study_01_annotation_lineage_reason.png)

![vaccination_study_01 QC and confidence](assets/umap_vaccination_study_01_annotation_qc_confidence.png)

![vaccination_study_01 source agreement and disagreement](assets/umap_vaccination_study_01_annotation_source_disagreement.png)

![vaccination_study_01 annotation-source effectiveness](assets/figure_02_source_effectiveness.png)

![vaccination_study_01 marker expression UMAPs](assets/umap_vaccination_study_01_annotation_marker_expression.png)

![vaccination_study_01 submitted-label marker dotplot](assets/dotplot_vaccination_study_01_annotation_marker_dotplot.png)

#### vaccination_study_01 B_lineage true subcluster UMAP

![vaccination_study_01 B_lineage true subcluster labels](assets/umap_vaccination_study_01_B_lineage_true_subcluster_label.png)

![vaccination_study_01 B_lineage true subcluster source labels](assets/umap_vaccination_study_01_B_lineage_true_subcluster_source_labels.png)

![vaccination_study_01 B_lineage true subcluster QC](assets/umap_vaccination_study_01_B_lineage_true_subcluster_qc.png)

![vaccination_study_01 B_lineage true subcluster marker scores](assets/umap_vaccination_study_01_B_lineage_true_subcluster_marker_scores.png)

![vaccination_study_01 B_lineage true subcluster marker expression](assets/umap_vaccination_study_01_B_lineage_true_subcluster_marker_expression.png)

![vaccination_study_01 B_lineage subcluster marker score heatmap](assets/subcluster_marker_score_heatmap_vaccination_study_01_B_lineage.png)

![vaccination_study_01 B_lineage subcluster marker dotplot](assets/dotplot_vaccination_study_01_B_lineage_true_subcluster_marker_dotplot.png)

Tables: `tables/vaccination_study_01_B_lineage_true_subcluster_umap.tsv.gz`, `tables/vaccination_study_01_B_lineage_subcluster_candidate_scores.tsv`.

#### vaccination_study_01 T_NK_lineage true subcluster UMAP

![vaccination_study_01 T_NK_lineage true subcluster labels](assets/umap_vaccination_study_01_T_NK_lineage_true_subcluster_label.png)

![vaccination_study_01 T_NK_lineage true subcluster source labels](assets/umap_vaccination_study_01_T_NK_lineage_true_subcluster_source_labels.png)

![vaccination_study_01 T_NK_lineage true subcluster QC](assets/umap_vaccination_study_01_T_NK_lineage_true_subcluster_qc.png)

![vaccination_study_01 T_NK_lineage true subcluster marker scores](assets/umap_vaccination_study_01_T_NK_lineage_true_subcluster_marker_scores.png)

![vaccination_study_01 T_NK_lineage true subcluster marker expression](assets/umap_vaccination_study_01_T_NK_lineage_true_subcluster_marker_expression.png)

![vaccination_study_01 T_NK_lineage subcluster marker score heatmap](assets/subcluster_marker_score_heatmap_vaccination_study_01_T_NK_lineage.png)

![vaccination_study_01 T_NK_lineage subcluster marker dotplot](assets/dotplot_vaccination_study_01_T_NK_lineage_true_subcluster_marker_dotplot.png)

Tables: `tables/vaccination_study_01_T_NK_lineage_true_subcluster_umap.tsv.gz`, `tables/vaccination_study_01_T_NK_lineage_subcluster_candidate_scores.tsv`.

#### vaccination_study_01 Myeloid_lineage true subcluster UMAP

![vaccination_study_01 Myeloid_lineage true subcluster labels](assets/umap_vaccination_study_01_Myeloid_lineage_true_subcluster_label.png)

![vaccination_study_01 Myeloid_lineage true subcluster source labels](assets/umap_vaccination_study_01_Myeloid_lineage_true_subcluster_source_labels.png)

![vaccination_study_01 Myeloid_lineage true subcluster QC](assets/umap_vaccination_study_01_Myeloid_lineage_true_subcluster_qc.png)

![vaccination_study_01 Myeloid_lineage true subcluster marker scores](assets/umap_vaccination_study_01_Myeloid_lineage_true_subcluster_marker_scores.png)

![vaccination_study_01 Myeloid_lineage true subcluster marker expression](assets/umap_vaccination_study_01_Myeloid_lineage_true_subcluster_marker_expression.png)

![vaccination_study_01 Myeloid_lineage subcluster marker score heatmap](assets/subcluster_marker_score_heatmap_vaccination_study_01_Myeloid_lineage.png)

![vaccination_study_01 Myeloid_lineage subcluster marker dotplot](assets/dotplot_vaccination_study_01_Myeloid_lineage_true_subcluster_marker_dotplot.png)

Tables: `tables/vaccination_study_01_Myeloid_lineage_true_subcluster_umap.tsv.gz`, `tables/vaccination_study_01_Myeloid_lineage_subcluster_candidate_scores.tsv`.


## Subcluster Marker Score Review

上の lineage-specific panel は、各 lineage subset で HVG 選択、PCA、neighbors、Leiden、UMAP を再計算した true local subcluster analysis から生成しています。Marker gene による fine label の確認は global UMAP だけではなく、この local UMAP、CellTypist/Azimuth/Pan-human/cluster-level marker gene assignment overlay、cluster marker gate score UMAP、marker-expression UMAP、dotplot を主に見ます。Treg など sparse marker label は cell-wise marker winner ではなく、local cluster の FOXP3/IL2RA/CTLA4 など key-marker support と reference support で判定します。

## Marker Assignment Feedback

Marker gene assignment は final label を強制的に上書きするものではなく、cluster-level の自己点検です。`raw_marker_winner` は marker score だけの勝者、`marker_assignment` は conservative policy と source-supported tie-break を通した marker-based assignment です。この表は marker assignment と final/reference-driven label がずれる cluster、marker specificity が弱い cluster、scRefMap が期待される lineage で欠落する cluster を示します。`marker_score` は raw marker base score から negative/confound marker penalty を差し引いた cluster-level marker gate score です。

| study | lineage | cluster | cells | chosen_label | marker_assignment | raw_marker_winner | assignment_reason | marker_score | base_score | penalty | flags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| vaccination_study_01 | Myeloid_lineage | 6 | 15,978 | Myeloid Cell | Neutrophil | Neutrophil | raw_marker_winner | 0.517 | 1.000 | 0.483 | marker_final_disagreement |
| vaccination_study_01 | T_NK_lineage | 9 | 15,623 | T Cell | CD4 Naive / T Central Memory | CD4 Naive / T Central Memory | raw_marker_winner | 0.820 | 1.000 | 0.180 | marker_final_disagreement;screfmapping_missing_for_scope |
| vaccination_study_01 | T_NK_lineage | 1 | 12,921 | T Cell | NKT Cell | NKT Cell | raw_marker_winner | 0.859 | 1.000 | 0.141 | marker_final_disagreement;screfmapping_missing_for_scope |
| vaccination_study_01 | Myeloid_lineage | 2 | 12,493 | Myeloid Cell | Neutrophil | Neutrophil | raw_marker_winner | 0.401 | 1.000 | 0.599 | marker_final_disagreement |
| vaccination_study_01 | T_NK_lineage | 2 | 11,418 | T Cell | CD4 Naive / T Central Memory | CD4 Naive / T Central Memory | raw_marker_winner | 0.787 | 1.000 | 0.213 | marker_final_disagreement;screfmapping_missing_for_scope |
| vaccination_study_01 | T_NK_lineage | 4 | 10,671 | T Cell | NKT Cell | NKT Cell | raw_marker_winner | 0.863 | 1.000 | 0.137 | marker_final_disagreement;screfmapping_missing_for_scope |
| vaccination_study_01 | Myeloid_lineage | 1 | 10,592 | Myeloid Cell | Intermediate Monocyte | Intermediate Monocyte | raw_marker_winner | 0.541 | 1.000 | 0.459 | marker_final_disagreement |
| vaccination_study_01 | Myeloid_lineage | 4 | 10,097 | Myeloid Cell | Neutrophil | Neutrophil | raw_marker_winner | 0.525 | 1.000 | 0.475 | marker_final_disagreement |
| vaccination_study_01 | T_NK_lineage | 3 | 8,863 | T Cell | CD4 Naive / T Central Memory | CD4 Naive / T Central Memory | raw_marker_winner | 0.866 | 1.000 | 0.134 | marker_final_disagreement;screfmapping_missing_for_scope |
| vaccination_study_01 | Myeloid_lineage | 9 | 8,774 | Myeloid Cell | Neutrophil | Neutrophil | raw_marker_winner | 0.514 | 1.000 | 0.486 | marker_final_disagreement |
| vaccination_study_01 | T_NK_lineage | 6 | 8,557 | T Cell | NKT Cell | NKT Cell | raw_marker_winner | 0.865 | 1.000 | 0.135 | marker_final_disagreement;screfmapping_missing_for_scope |
| vaccination_study_01 | Myeloid_lineage | 0 | 8,459 | Myeloid Cell | Intermediate Monocyte | Intermediate Monocyte | raw_marker_winner | 0.488 | 1.000 | 0.512 | marker_final_disagreement |
| vaccination_study_01 | T_NK_lineage | 5 | 8,136 | T Cell | NKT Cell | NKT Cell | raw_marker_winner | 0.627 | 1.000 | 0.373 | marker_final_disagreement;screfmapping_missing_for_scope |
| vaccination_study_01 | Myeloid_lineage | 7 | 8,095 | Myeloid Cell | Neutrophil | Neutrophil | raw_marker_winner | 0.524 | 1.000 | 0.476 | marker_final_disagreement |
| vaccination_study_01 | T_NK_lineage | 8 | 7,908 | T Cell | NKT Cell | NKT Cell | raw_marker_winner | 0.773 | 0.986 | 0.212 | marker_final_disagreement;screfmapping_missing_for_scope |
| vaccination_study_01 | T_NK_lineage | 0 | 7,276 | T Cell | NKT Cell | NKT Cell | raw_marker_winner | 0.725 | 0.973 | 0.249 | marker_final_disagreement;screfmapping_missing_for_scope |
| vaccination_study_01 | Myeloid_lineage | 5 | 6,264 | Myeloid Cell | Neutrophil | Neutrophil | raw_marker_winner | 0.508 | 0.978 | 0.470 | marker_final_disagreement |
| vaccination_study_01 | T_NK_lineage | 7 | 5,354 | T Cell | NKT Cell | NKT Cell | raw_marker_winner | 0.606 | 1.000 | 0.394 | marker_final_disagreement;screfmapping_missing_for_scope |
| vaccination_study_01 | Myeloid_lineage | 3 | 3,977 | Myeloid Cell | Neutrophil | Neutrophil | raw_marker_winner | 0.526 | 1.000 | 0.474 | marker_final_disagreement |
| vaccination_study_01 | B_lineage | 0 | 3,653 | B Cell | Plasmablast | Plasmablast | raw_marker_winner | 0.423 | 0.733 | 0.310 | marker_final_disagreement;screfmapping_missing_for_scope |

## LLM Review Queue

この表は Codex/LLM が読むための subcluster-level review queue です。LLM はこの evidence を読んで、final label が妥当か、ontology にちょうどよい label がないのか、registry / conservative policy を一般ルールとして更新すべきかを提案します。LLM の出力で per-cell label を直接書き換えず、採用する場合は registry/config を更新して deterministic pipeline を再実行します。

| study | lineage | cluster | cells | priority | reasons | suggested_action | final_label | marker_assignment | raw_marker_winner | score_margin |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| vaccination_study_01 | T_NK_lineage | 5 | 8,136 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | T Cell | NKT Cell | NKT Cell | 0.126 |
| vaccination_study_01 | T_NK_lineage | 8 | 7,908 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | T Cell | NKT Cell | NKT Cell | 0.022 |
| vaccination_study_01 | T_NK_lineage | 0 | 7,276 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | T Cell | NKT Cell | NKT Cell | 0.060 |
| vaccination_study_01 | T_NK_lineage | 7 | 5,354 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | T Cell | NKT Cell | NKT Cell | 0.071 |
| vaccination_study_01 | B_lineage | 0 | 3,653 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | B Cell | Plasmablast | Plasmablast | 0.055 |
| vaccination_study_01 | B_lineage | 1 | 3,060 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | B Cell | Plasma Cell | Plasma Cell | 0.046 |
| vaccination_study_01 | B_lineage | 2 | 2,269 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | B Cell | Plasmablast | Plasmablast | 0.078 |
| vaccination_study_01 | B_lineage | 9 | 1,661 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | B Cell | Plasma Cell | Plasma Cell | 0.039 |
| vaccination_study_01 | B_lineage | 12 | 1,290 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | B Cell | Plasmablast | Plasmablast | 0.028 |
| vaccination_study_01 | B_lineage | 17 | 1,015 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | B Cell | Plasma Cell | Plasma Cell | 0.026 |
| vaccination_study_01 | B_lineage | 24 | 580 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | B Cell | Plasma Cell | Plasma Cell | 0.000 |
| vaccination_study_01 | B_lineage | 25 | 549 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | B Cell | Plasmablast | Plasmablast | 0.159 |
| vaccination_study_01 | B_lineage | 27 | 530 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | B Cell | Plasma Cell | Plasma Cell | 0.079 |
| vaccination_study_01 | B_lineage | 28 | 424 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | B Cell | Plasma Cell | Plasma Cell | 0.074 |
| vaccination_study_01 | B_lineage | 29 | 402 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | B Cell | Plasma Cell | Plasma Cell | 0.000 |
| vaccination_study_01 | B_lineage | 30 | 337 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | B Cell | Plasmablast | Plasmablast | 0.047 |
| vaccination_study_01 | Myeloid_lineage | 6 | 15,978 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | Myeloid Cell | Neutrophil | Neutrophil | 0.043 |
| vaccination_study_01 | T_NK_lineage | 9 | 15,623 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | T Cell | CD4 Naive / T Central Memory | CD4 Naive / T Central Memory | 0.022 |
| vaccination_study_01 | T_NK_lineage | 1 | 12,921 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available | check_if_finer_official_label_is_supported | T Cell | NKT Cell | NKT Cell | 0.193 |
| vaccination_study_01 | Myeloid_lineage | 2 | 12,493 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | Myeloid Cell | Neutrophil | Neutrophil | 0.001 |

## Cluster Consensus Evidence

| study | lineage | cluster | cells | chosen_label | accepted | score_margin | cluster_marker_assignment | treg_key_any | treg_key_bonus | marker_set | marker_alert |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| vaccination_study_01 | B_lineage | 0 | 3,653 | B Cell | False | 0.055 | Plasmablast | nan | nan | registry__plasmablast | pass |
| vaccination_study_01 | B_lineage | 1 | 3,060 | B Cell | False | 0.046 | Plasma Cell | nan | nan | registry__plasma_cell | pass |
| vaccination_study_01 | B_lineage | 2 | 2,269 | B Cell | False | 0.078 | Plasmablast | nan | nan | registry__plasmablast | pass |
| vaccination_study_01 | B_lineage | 3 | 2,072 | B Cell | False | 0.699 | Naive B Cell | nan | nan | registry__naive_b_cell | pass |
| vaccination_study_01 | B_lineage | 4 | 1,953 | B Cell | False | 0.550 | Memory B Cell | nan | nan | registry__memory_b_cell | pass |
| vaccination_study_01 | B_lineage | 5 | 1,941 | B Cell | False | 0.800 | Naive B Cell | nan | nan | registry__naive_b_cell | pass |
| vaccination_study_01 | B_lineage | 6 | 1,828 | B Cell | False | 0.296 | Naive B Cell | nan | nan | registry__naive_b_cell | pass |
| vaccination_study_01 | B_lineage | 7 | 1,820 | B Cell | False | 0.068 | Naive B Cell | nan | nan | registry__naive_b_cell | pass |
| vaccination_study_01 | B_lineage | 8 | 1,669 | B Cell | False | 0.051 | Memory B Cell | nan | nan | registry__memory_b_cell | pass |
| vaccination_study_01 | B_lineage | 9 | 1,661 | B Cell | False | 0.039 | Plasma Cell | nan | nan | registry__plasma_cell | pass |
| vaccination_study_01 | B_lineage | 10 | 1,609 | B Cell | False | 0.720 | Naive B Cell | nan | nan | registry__naive_b_cell | pass |
| vaccination_study_01 | B_lineage | 11 | 1,305 | B Cell | False | 0.139 | Memory B Cell | nan | nan | registry__memory_b_cell | pass |
| vaccination_study_01 | B_lineage | 12 | 1,290 | B Cell | False | 0.028 | Plasmablast | nan | nan | registry__plasmablast | pass |
| vaccination_study_01 | B_lineage | 13 | 1,268 | B Cell | False | 0.032 | Naive B Cell | nan | nan | registry__naive_b_cell | pass |
| vaccination_study_01 | B_lineage | 14 | 1,254 | B Cell | False | 0.690 | Naive B Cell | nan | nan | registry__naive_b_cell | pass |
| vaccination_study_01 | B_lineage | 15 | 1,153 | B Cell | False | 0.246 | Memory B Cell | nan | nan | registry__memory_b_cell | pass |
| vaccination_study_01 | B_lineage | 16 | 1,060 | B Cell | False | 0.662 | Naive B Cell | nan | nan | registry__naive_b_cell | pass |
| vaccination_study_01 | B_lineage | 17 | 1,015 | B Cell | False | 0.026 | Plasma Cell | nan | nan | registry__plasma_cell | pass |
| vaccination_study_01 | B_lineage | 18 | 999 | B Cell | False | 0.007 | Naive B Cell | nan | nan | registry__naive_b_cell | pass |
| vaccination_study_01 | B_lineage | 19 | 831 | B Cell | False | 0.338 | Memory B Cell | nan | nan | registry__memory_b_cell | pass |
| vaccination_study_01 | B_lineage | 20 | 706 | B Cell | False | 0.068 | Memory B Cell | nan | nan | registry__memory_b_cell | pass |
| vaccination_study_01 | B_lineage | 21 | 678 | B Cell | False | 0.101 | Memory B Cell | nan | nan | registry__memory_b_cell | pass |
| vaccination_study_01 | B_lineage | 22 | 632 | B Cell | False | 0.132 | Memory B Cell | nan | nan | registry__memory_b_cell | pass |
| vaccination_study_01 | B_lineage | 23 | 605 | B Cell | False | 0.832 | Naive B Cell | nan | nan | registry__naive_b_cell | pass |
| vaccination_study_01 | B_lineage | 24 | 580 | B Cell | False | 0.000 | Plasma Cell | nan | nan | registry__plasma_cell | pass |
| vaccination_study_01 | B_lineage | 25 | 549 | B Cell | False | 0.159 | Plasmablast | nan | nan | registry__plasmablast | pass |
| vaccination_study_01 | B_lineage | 26 | 546 | B Cell | False | 0.032 | Naive B Cell | nan | nan | registry__naive_b_cell | pass |
| vaccination_study_01 | B_lineage | 27 | 530 | B Cell | False | 0.079 | Plasma Cell | nan | nan | registry__plasma_cell | pass |
| vaccination_study_01 | B_lineage | 28 | 424 | B Cell | False | 0.074 | Plasma Cell | nan | nan | registry__plasma_cell | pass |
| vaccination_study_01 | B_lineage | 29 | 402 | B Cell | False | 0.000 | Plasma Cell | nan | nan | registry__plasma_cell | pass |

## 出力ファイル

- Submission TSVs: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_final_v22/vaccination_study_01/submissions/`
- cellxgene H5ADs: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_final_v22/vaccination_study_01/cellxgene/`
- Marker availability table: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_final_v22/vaccination_study_01/tables/marker_gene_availability.tsv`
- Marker availability alerts: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_final_v22/vaccination_study_01/tables/marker_gene_availability_alerts.tsv`
- Subcluster evidence: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_final_v22/vaccination_study_01/tables/lineage_subcluster_evidence.tsv.gz`
- Source disagreement summary: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_final_v22/vaccination_study_01/tables/source_disagreement_summary.tsv`
- Source effectiveness summary: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_final_v22/vaccination_study_01/tables/source_effectiveness_summary.tsv`
- Diagnostics tables: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_final_v22/vaccination_study_01/tables/`

