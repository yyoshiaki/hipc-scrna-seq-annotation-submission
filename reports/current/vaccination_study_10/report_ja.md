# HIPC データセットアノテーションレポート: vaccination_study_10

更新日: 2026-06-05 EDT

このレポートは `hipc-annotation` Codex workflow によって生成したデータセット別レビュー文書です。固定 method は repository README に置き、このレポートでは実際の evidence、弱い箇所、レビュー優先度、UMAP / dotplot を確認します。

## データセット概要

| study | cells | analysis_X_genes | pre_hvg_genes | counts_layer_genes | labels | parent_or_blood_fraction | Blood Cell | Doublet | artifact_like | median_confidence | low_confidence | source_disagreement | invalid_labels |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| vaccination_study_10 | 47,511 | 1,271 | 14,969 | 1,271 | 4 | 1.000 | 17,608 | 0 | 0 | 0.450 | 47,511 | 0 (0.000) | none |

## 実行概要

- 実行単位: one dataset in, one annotated dataset out。
- 実行経路: Codex skill `hipc-annotation` -> bundled helper `run_one.sh` -> annotation CLI -> validator -> report inspection。
- 検証: submission row count、H5AD observation count、official label validity、H5AD/submission agreement、confidence column、report image link を確認する。
- このレポートは workflow の再掲ではなく、このデータセットの marker 欠損、UMAP、label 構成、review concern を読むためのもの。

## データセット固有の解釈

- `vaccination_study_10`: 47,511 cells、analysis X/var 1,271 genes、pre-HVG slot 14,969 genes、submitted label 4 種、parent/Blood residual fraction 1.000、median confidence 0.450。
  - 47,511 cells は low confidence。QC / confidence UMAP 上で局在を確認する。
  - 17,608 cells は `Blood Cell` として残存。これは filter-out ではなく、曖昧な細胞を公式 parent label で残したもの。
  - Marker gene 欠損アラート: CD4_naive_tcm, gdT, NKT, B_memory_ABC, Plasma_ASC。該当 marker set に依存する fine label は慎重に見る。

## データセット固有の評価

- 全体像: 47,511 cells / analysis X/var 1,271 genes / pre-HVG slot 14,969 genes。parent/Blood residual は 1.000、low-confidence は 47,511 cells、source disagreement flag は 0 cells (0.000)。
- 優先確認: low-confidence 領域が QC UMAP と source-disagreement UMAP で同じ場所に集まるかを確認する。
- 優先確認: `Blood Cell` 残存が孤立 cluster なのか、複数 lineage に分散した曖昧領域なのかを UMAP で確認する。
- Marker gene 欠損: CD4_naive_tcm, gdT, NKT, B_memory_ABC, Plasma_ASC は confidence cap 対象。該当 label は marker expression UMAP と dotplot で妥当性を確認する。

## Marker Gene 欠損アラート

| study | marker_set | alert | present_fraction | missing_critical_markers | missing_genes |
| --- | --- | --- | --- | --- | --- |
| vaccination_study_10 | CD4_naive_tcm | critical | 0.222 | none | CD3D;CD3E;CD4;CCR7;SELL;TCF7;LEF1 |
| vaccination_study_10 | gdT | critical | 0.000 | TRDC;TRGC1;TRGC2 | CD3D;CD3E;TRDC;TRGC1;TRGC2;TRDV2 |
| vaccination_study_10 | NKT | warning | 0.571 | CD3D | CD3D;CD3E;TRAC |
| vaccination_study_10 | B_memory_ABC | warning | 0.500 | CD27;ITGAX | CD27;ITGAX;AIM2;CD86 |
| vaccination_study_10 | Plasma_ASC | warning | 0.333 | JCHAIN;XBP1 | XBP1;JCHAIN;SDC1;IRF4;IGHG1;IGHA1 |

## ソース間不一致

| study | predicted_cell_type | cells | median_source_agreement | disagreement_cells | disagreement_fraction |
| --- | --- | --- | --- | --- | --- |
| vaccination_study_10 | B Cell | 5,637 | 0.000 | 0 | 0.000 |
| vaccination_study_10 | Blood Cell | 17,608 | 0.000 | 0 | 0.000 |
| vaccination_study_10 | Myeloid Cell | 9,624 | 0.000 | 0 | 0.000 |
| vaccination_study_10 | T Cell | 14,642 | 0.000 | 0 | 0.000 |

## アノテーションソース効果

この表は外部 ground truth に対する正解率ではありません。各 annotation source がどれだけの細胞で情報を持ち、final label とどれだけ一致したかを示す監査用統計です。`coverage` は source が `not_available` 以外を返した割合、`final_concordance` は informative cells の中で final label と一致した割合、`unique_support` はその source だけが final label と一致した細胞数です。

| study | source | informative_cells | coverage | final_concordance | high_conf_concordance | unique_support | discordant |
| --- | --- | --- | --- | --- | --- | --- | --- |
| vaccination_study_10 | Cluster marker assignment | 29,903 | 0.629 | 0.000 | 0.000 | 0 | 29,903 |
| vaccination_study_10 | CellTypist | 0 | 0.000 | 0.000 | 0.000 | 0 | 0 |
| vaccination_study_10 | Pan-human Azimuth | 0 | 0.000 | 0.000 | 0.000 | 0 | 0 |
| vaccination_study_10 | Cluster consensus | 0 | 0.000 | 0.000 | 0.000 | 0 | 0 |
| vaccination_study_10 | scRefMapping | 0 | 0.000 | 0.000 | 0.000 | 0 | 0 |

## レビュー優先事項

| study | concern | cells |
| --- | --- | --- |
| vaccination_study_10 | Large Blood Cell/ambiguous residual remains | 17,608 |
| vaccination_study_10 | Many low-confidence cells; QC or mixed-marker effects likely remain | 47,511 |

## ラベル構成

| study | predicted_cell_type | cells |
| --- | --- | --- |
| vaccination_study_10 | Blood Cell | 17,608 |
| vaccination_study_10 | T Cell | 14,642 |
| vaccination_study_10 | Myeloid Cell | 9,624 |
| vaccination_study_10 | B Cell | 5,637 |

## Inline Figures

### vaccination_study_10

![vaccination_study_10 final labels](assets/umap_vaccination_study_10_annotation_label.png)

![vaccination_study_10 lineage and annotation reason](assets/umap_vaccination_study_10_annotation_lineage_reason.png)

![vaccination_study_10 QC and confidence](assets/umap_vaccination_study_10_annotation_qc_confidence.png)

![vaccination_study_10 source agreement and disagreement](assets/umap_vaccination_study_10_annotation_source_disagreement.png)

![vaccination_study_10 annotation-source effectiveness](assets/figure_02_source_effectiveness.png)

![vaccination_study_10 marker expression UMAPs](assets/umap_vaccination_study_10_annotation_marker_expression.png)

![vaccination_study_10 submitted-label marker dotplot](assets/dotplot_vaccination_study_10_annotation_marker_dotplot.png)

#### vaccination_study_10 B_lineage true subcluster UMAP

![vaccination_study_10 B_lineage true subcluster labels](assets/umap_vaccination_study_10_B_lineage_true_subcluster_label.png)

![vaccination_study_10 B_lineage true subcluster source labels](assets/umap_vaccination_study_10_B_lineage_true_subcluster_source_labels.png)

![vaccination_study_10 B_lineage true subcluster QC](assets/umap_vaccination_study_10_B_lineage_true_subcluster_qc.png)

![vaccination_study_10 B_lineage true subcluster marker scores](assets/umap_vaccination_study_10_B_lineage_true_subcluster_marker_scores.png)

![vaccination_study_10 B_lineage true subcluster marker expression](assets/umap_vaccination_study_10_B_lineage_true_subcluster_marker_expression.png)

![vaccination_study_10 B_lineage subcluster marker score heatmap](assets/subcluster_marker_score_heatmap_vaccination_study_10_B_lineage.png)

![vaccination_study_10 B_lineage subcluster marker dotplot](assets/dotplot_vaccination_study_10_B_lineage_true_subcluster_marker_dotplot.png)

Tables: `tables/vaccination_study_10_B_lineage_true_subcluster_umap.tsv.gz`, `tables/vaccination_study_10_B_lineage_subcluster_candidate_scores.tsv`.

#### vaccination_study_10 T_NK_lineage true subcluster UMAP

![vaccination_study_10 T_NK_lineage true subcluster labels](assets/umap_vaccination_study_10_T_NK_lineage_true_subcluster_label.png)

![vaccination_study_10 T_NK_lineage true subcluster source labels](assets/umap_vaccination_study_10_T_NK_lineage_true_subcluster_source_labels.png)

![vaccination_study_10 T_NK_lineage true subcluster QC](assets/umap_vaccination_study_10_T_NK_lineage_true_subcluster_qc.png)

![vaccination_study_10 T_NK_lineage true subcluster marker scores](assets/umap_vaccination_study_10_T_NK_lineage_true_subcluster_marker_scores.png)

![vaccination_study_10 T_NK_lineage true subcluster marker expression](assets/umap_vaccination_study_10_T_NK_lineage_true_subcluster_marker_expression.png)

![vaccination_study_10 T_NK_lineage subcluster marker score heatmap](assets/subcluster_marker_score_heatmap_vaccination_study_10_T_NK_lineage.png)

![vaccination_study_10 T_NK_lineage subcluster marker dotplot](assets/dotplot_vaccination_study_10_T_NK_lineage_true_subcluster_marker_dotplot.png)

Tables: `tables/vaccination_study_10_T_NK_lineage_true_subcluster_umap.tsv.gz`, `tables/vaccination_study_10_T_NK_lineage_subcluster_candidate_scores.tsv`.

#### vaccination_study_10 Myeloid_lineage true subcluster UMAP

![vaccination_study_10 Myeloid_lineage true subcluster labels](assets/umap_vaccination_study_10_Myeloid_lineage_true_subcluster_label.png)

![vaccination_study_10 Myeloid_lineage true subcluster source labels](assets/umap_vaccination_study_10_Myeloid_lineage_true_subcluster_source_labels.png)

![vaccination_study_10 Myeloid_lineage true subcluster QC](assets/umap_vaccination_study_10_Myeloid_lineage_true_subcluster_qc.png)

![vaccination_study_10 Myeloid_lineage true subcluster marker scores](assets/umap_vaccination_study_10_Myeloid_lineage_true_subcluster_marker_scores.png)

![vaccination_study_10 Myeloid_lineage true subcluster marker expression](assets/umap_vaccination_study_10_Myeloid_lineage_true_subcluster_marker_expression.png)

![vaccination_study_10 Myeloid_lineage subcluster marker score heatmap](assets/subcluster_marker_score_heatmap_vaccination_study_10_Myeloid_lineage.png)

![vaccination_study_10 Myeloid_lineage subcluster marker dotplot](assets/dotplot_vaccination_study_10_Myeloid_lineage_true_subcluster_marker_dotplot.png)

Tables: `tables/vaccination_study_10_Myeloid_lineage_true_subcluster_umap.tsv.gz`, `tables/vaccination_study_10_Myeloid_lineage_subcluster_candidate_scores.tsv`.


## Subcluster Marker Score Review

上の lineage-specific panel は、各 lineage subset で HVG 選択、PCA、neighbors、Leiden、UMAP を再計算した true local subcluster analysis から生成しています。Marker gene による fine label の確認は global UMAP だけではなく、この local UMAP、CellTypist/Azimuth/Pan-human/cluster-level marker gene assignment overlay、cluster marker gate score UMAP、marker-expression UMAP、dotplot を主に見ます。Treg など sparse marker label は cell-wise marker winner ではなく、local cluster の FOXP3/IL2RA/CTLA4 など key-marker support と reference support で判定します。

## Marker Assignment Feedback

Marker gene assignment は final label を強制的に上書きするものではなく、cluster-level の自己点検です。`raw_marker_winner` は marker score だけの勝者、`marker_assignment` は conservative policy と source-supported tie-break を通した marker-based assignment です。この表は marker assignment と final/reference-driven label がずれる cluster、marker specificity が弱い cluster、scRefMap が期待される lineage で欠落する cluster を示します。`marker_score` は raw marker base score から negative/confound marker penalty を差し引いた cluster-level marker gate score です。

| study | lineage | cluster | cells | chosen_label | marker_assignment | raw_marker_winner | assignment_reason | marker_score | base_score | penalty | flags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| vaccination_study_10 | T_NK_lineage | 0 | 1,189 | T Cell | NK Cell | NK Cell | raw_marker_winner | 0.933 | 1.000 | 0.067 | marker_final_disagreement;screfmapping_missing_for_scope |
| vaccination_study_10 | T_NK_lineage | 1 | 1,124 | T Cell | NK Cell | NK Cell | raw_marker_winner | 0.859 | 1.000 | 0.141 | marker_final_disagreement;screfmapping_missing_for_scope |
| vaccination_study_10 | T_NK_lineage | 2 | 980 | T Cell | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | raw_marker_winner | 0.709 | 1.000 | 0.291 | marker_final_disagreement;screfmapping_missing_for_scope |
| vaccination_study_10 | T_NK_lineage | 3 | 949 | T Cell | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | raw_marker_winner | 0.933 | 1.000 | 0.067 | marker_final_disagreement;screfmapping_missing_for_scope |
| vaccination_study_10 | Myeloid_lineage | 0 | 859 | Myeloid Cell | Non-Classical Monocyte | Non-Classical Monocyte | raw_marker_winner | 0.832 | 1.000 | 0.168 | marker_final_disagreement |
| vaccination_study_10 | T_NK_lineage | 4 | 825 | T Cell | CD4 Naive / T Central Memory | CD4 Naive / T Central Memory | raw_marker_winner | 0.891 | 0.975 | 0.084 | marker_final_disagreement;screfmapping_missing_for_scope |
| vaccination_study_10 | T_NK_lineage | 5 | 821 | T Cell | CD4 Naive / T Central Memory | CD4 Naive / T Central Memory | raw_marker_winner | 0.870 | 0.966 | 0.095 | marker_final_disagreement;screfmapping_missing_for_scope |
| vaccination_study_10 | Myeloid_lineage | 1 | 819 | Myeloid Cell | Conventional DC 2 | Conventional DC 2 | raw_marker_winner | 0.604 | 1.000 | 0.396 | marker_final_disagreement |
| vaccination_study_10 | T_NK_lineage | 6 | 797 | T Cell | CD8 Naive / T Central Memory | CD8 Naive / T Central Memory | raw_marker_winner | 0.913 | 1.000 | 0.087 | marker_final_disagreement;screfmapping_missing_for_scope |
| vaccination_study_10 | T_NK_lineage | 7 | 763 | T Cell | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | raw_marker_winner | 0.871 | 1.000 | 0.129 | marker_final_disagreement;screfmapping_missing_for_scope |
| vaccination_study_10 | Myeloid_lineage | 2 | 742 | Myeloid Cell | Intermediate Monocyte | Intermediate Monocyte | raw_marker_winner | 0.529 | 1.000 | 0.471 | marker_final_disagreement |
| vaccination_study_10 | Myeloid_lineage | 3 | 664 | Myeloid Cell | Intermediate Monocyte | Intermediate Monocyte | raw_marker_winner | 0.475 | 1.000 | 0.525 | marker_final_disagreement |
| vaccination_study_10 | T_NK_lineage | 8 | 646 | T Cell | CD8 Naive / T Central Memory | CD8 Naive / T Central Memory | raw_marker_winner | 0.920 | 1.000 | 0.080 | marker_final_disagreement;screfmapping_missing_for_scope |
| vaccination_study_10 | T_NK_lineage | 9 | 634 | T Cell | NK Cell | NK Cell | raw_marker_winner | 0.922 | 1.000 | 0.078 | marker_final_disagreement;screfmapping_missing_for_scope |
| vaccination_study_10 | T_NK_lineage | 10 | 609 | T Cell | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | raw_marker_winner | 0.689 | 1.000 | 0.311 | marker_final_disagreement;screfmapping_missing_for_scope |
| vaccination_study_10 | Myeloid_lineage | 4 | 601 | Myeloid Cell | Conventional DC 2 | Conventional DC 2 | raw_marker_winner | 0.524 | 1.000 | 0.476 | marker_final_disagreement |
| vaccination_study_10 | T_NK_lineage | 11 | 579 | T Cell | CD8 Naive / T Central Memory | CD8 Naive / T Central Memory | raw_marker_winner | 0.919 | 1.000 | 0.081 | marker_final_disagreement;screfmapping_missing_for_scope |
| vaccination_study_10 | Myeloid_lineage | 5 | 565 | Myeloid Cell | Intermediate Monocyte | Intermediate Monocyte | raw_marker_winner | 0.573 | 1.000 | 0.427 | marker_final_disagreement |
| vaccination_study_10 | T_NK_lineage | 12 | 565 | T Cell | CD4 Naive / T Central Memory | CD4 Naive / T Central Memory | raw_marker_winner | 0.764 | 0.973 | 0.209 | marker_final_disagreement;screfmapping_missing_for_scope |
| vaccination_study_10 | Myeloid_lineage | 6 | 536 | Myeloid Cell | Intermediate Monocyte | Intermediate Monocyte | raw_marker_winner | 0.598 | 1.000 | 0.402 | marker_final_disagreement |

## LLM Review Queue

この表は Codex/LLM が読むための subcluster-level review queue です。LLM はこの evidence を読んで、final label が妥当か、ontology にちょうどよい label がないのか、registry / conservative policy を一般ルールとして更新すべきかを提案します。LLM の出力で per-cell label を直接書き換えず、採用する場合は registry/config を更新して deterministic pipeline を再実行します。

| study | lineage | cluster | cells | priority | reasons | suggested_action | final_label | marker_assignment | raw_marker_winner | score_margin |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| vaccination_study_10 | T_NK_lineage | 15 | 487 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | T Cell | NKT Cell | NKT Cell | 0.000 |
| vaccination_study_10 | T_NK_lineage | 0 | 1,189 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | T Cell | NK Cell | NK Cell | 0.000 |
| vaccination_study_10 | T_NK_lineage | 1 | 1,124 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | T Cell | NK Cell | NK Cell | 0.000 |
| vaccination_study_10 | B_lineage | 10 | 249 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | B Cell | Plasma Cell | Plasma Cell | 0.708 |
| vaccination_study_10 | B_lineage | 20 | 88 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | B Cell | Plasma Cell | Plasma Cell | 0.343 |
| vaccination_study_10 | B_lineage | 21 | 46 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | B Cell | Plasmablast | Plasmablast | 0.000 |
| vaccination_study_10 | T_NK_lineage | 25 | 38 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | T Cell | NKT Cell | NKT Cell | 0.000 |
| vaccination_study_10 | B_lineage | 23 | 17 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | B Cell | Plasmablast | Plasmablast | 0.019 |
| vaccination_study_10 | T_NK_lineage | 2 | 980 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | T Cell | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | 0.064 |
| vaccination_study_10 | Myeloid_lineage | 1 | 819 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | Myeloid Cell | Conventional DC 2 | Conventional DC 2 | 0.149 |
| vaccination_study_10 | Myeloid_lineage | 2 | 742 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | Myeloid Cell | Intermediate Monocyte | Intermediate Monocyte | 0.129 |
| vaccination_study_10 | Myeloid_lineage | 3 | 664 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | Myeloid Cell | Intermediate Monocyte | Intermediate Monocyte | 0.030 |
| vaccination_study_10 | T_NK_lineage | 9 | 634 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | T Cell | NK Cell | NK Cell | 0.000 |
| vaccination_study_10 | T_NK_lineage | 10 | 609 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | T Cell | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | 0.012 |
| vaccination_study_10 | Myeloid_lineage | 4 | 601 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | Myeloid Cell | Conventional DC 2 | Conventional DC 2 | 0.054 |
| vaccination_study_10 | T_NK_lineage | 12 | 565 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | T Cell | CD4 Naive / T Central Memory | CD4 Naive / T Central Memory | 0.072 |
| vaccination_study_10 | Myeloid_lineage | 5 | 565 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | Myeloid Cell | Intermediate Monocyte | Intermediate Monocyte | 0.173 |
| vaccination_study_10 | Myeloid_lineage | 6 | 536 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | Myeloid Cell | Intermediate Monocyte | Intermediate Monocyte | 0.198 |
| vaccination_study_10 | B_lineage | 0 | 525 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available | check_if_finer_official_label_is_supported | B Cell | Plasma Cell | Plasma Cell | 0.783 |
| vaccination_study_10 | Myeloid_lineage | 7 | 489 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | Myeloid Cell | Conventional DC 2 | Conventional DC 2 | 0.329 |

## Cluster Consensus Evidence

| study | lineage | cluster | cells | chosen_label | accepted | score_margin | cluster_marker_assignment | treg_key_any | treg_key_bonus | marker_set | marker_alert |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| vaccination_study_10 | B_lineage | 0 | 525 | B Cell | False | 0.783 | Plasma Cell | nan | nan | registry__plasma_cell | pass |
| vaccination_study_10 | B_lineage | 1 | 463 | B Cell | False | 0.903 | Naive B Cell | nan | nan | registry__naive_b_cell | pass |
| vaccination_study_10 | B_lineage | 2 | 417 | B Cell | False | 0.643 | Naive B Cell | nan | nan | registry__naive_b_cell | pass |
| vaccination_study_10 | B_lineage | 3 | 414 | B Cell | False | 0.422 | Memory B Cell | nan | nan | registry__memory_b_cell | pass |
| vaccination_study_10 | B_lineage | 4 | 355 | B Cell | False | 0.883 | Naive B Cell | nan | nan | registry__naive_b_cell | pass |
| vaccination_study_10 | B_lineage | 5 | 346 | B Cell | False | 0.890 | Naive B Cell | nan | nan | registry__naive_b_cell | pass |
| vaccination_study_10 | B_lineage | 6 | 334 | B Cell | False | 0.393 | Memory B Cell | nan | nan | registry__memory_b_cell | pass |
| vaccination_study_10 | B_lineage | 7 | 307 | B Cell | False | 0.912 | Naive B Cell | nan | nan | registry__naive_b_cell | pass |
| vaccination_study_10 | B_lineage | 8 | 285 | B Cell | False | 0.141 | Plasma Cell | nan | nan | registry__plasma_cell | pass |
| vaccination_study_10 | B_lineage | 9 | 260 | B Cell | False | 0.674 | Plasma Cell | nan | nan | registry__plasma_cell | pass |
| vaccination_study_10 | B_lineage | 10 | 249 | B Cell | False | 0.708 | Plasma Cell | nan | nan | registry__plasma_cell | pass |
| vaccination_study_10 | B_lineage | 11 | 238 | B Cell | False | 0.402 | Memory B Cell | nan | nan | registry__memory_b_cell | pass |
| vaccination_study_10 | B_lineage | 12 | 230 | B Cell | False | 0.421 | Naive B Cell | nan | nan | registry__naive_b_cell | pass |
| vaccination_study_10 | B_lineage | 13 | 194 | B Cell | False | 0.084 | Naive B Cell | nan | nan | registry__naive_b_cell | pass |
| vaccination_study_10 | B_lineage | 14 | 185 | B Cell | False | 0.357 | Plasma Cell | nan | nan | registry__plasma_cell | pass |
| vaccination_study_10 | B_lineage | 15 | 158 | B Cell | False | 0.736 | Plasma Cell | nan | nan | registry__plasma_cell | pass |
| vaccination_study_10 | B_lineage | 16 | 136 | B Cell | False | 0.421 | Memory B Cell | nan | nan | registry__memory_b_cell | pass |
| vaccination_study_10 | B_lineage | 17 | 127 | B Cell | False | 0.894 | Naive B Cell | nan | nan | registry__naive_b_cell | pass |
| vaccination_study_10 | B_lineage | 18 | 117 | B Cell | False | 0.766 | Plasma Cell | nan | nan | registry__plasma_cell | pass |
| vaccination_study_10 | B_lineage | 19 | 110 | B Cell | False | 0.743 | Memory B Cell | nan | nan | registry__memory_b_cell | pass |
| vaccination_study_10 | B_lineage | 20 | 88 | B Cell | False | 0.343 | Plasma Cell | nan | nan | registry__plasma_cell | pass |
| vaccination_study_10 | B_lineage | 21 | 46 | B Cell | False | 0.000 | Plasmablast | nan | nan | registry__plasma_cell | pass |
| vaccination_study_10 | B_lineage | 22 | 36 | B Cell | False | 0.052 | Memory B Cell | nan | nan | registry__memory_b_cell | pass |
| vaccination_study_10 | B_lineage | 23 | 17 | B Cell | False | 0.019 | Plasmablast | nan | nan | registry__plasmablast | pass |
| vaccination_study_10 | Myeloid_lineage | 0 | 859 | Myeloid Cell | False | 0.321 | Non-Classical Monocyte | nan | nan | registry__non_classical_monocyte | pass |
| vaccination_study_10 | Myeloid_lineage | 1 | 819 | Myeloid Cell | False | 0.149 | Conventional DC 2 | nan | nan | registry__conventional_dc_2 | pass |
| vaccination_study_10 | Myeloid_lineage | 2 | 742 | Myeloid Cell | False | 0.129 | Intermediate Monocyte | nan | nan | registry__intermediate_monocyte | pass |
| vaccination_study_10 | Myeloid_lineage | 3 | 664 | Myeloid Cell | False | 0.030 | Intermediate Monocyte | nan | nan | registry__intermediate_monocyte | pass |
| vaccination_study_10 | Myeloid_lineage | 4 | 601 | Myeloid Cell | False | 0.054 | Conventional DC 2 | nan | nan | registry__conventional_dc_2 | pass |
| vaccination_study_10 | Myeloid_lineage | 5 | 565 | Myeloid Cell | False | 0.173 | Intermediate Monocyte | nan | nan | registry__intermediate_monocyte | pass |

## 出力ファイル

- Submission TSVs: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_final_v22/vaccination_study_10/submissions/`
- cellxgene H5ADs: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_final_v22/vaccination_study_10/cellxgene/`
- Marker availability table: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_final_v22/vaccination_study_10/tables/marker_gene_availability.tsv`
- Marker availability alerts: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_final_v22/vaccination_study_10/tables/marker_gene_availability_alerts.tsv`
- Subcluster evidence: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_final_v22/vaccination_study_10/tables/lineage_subcluster_evidence.tsv.gz`
- Source disagreement summary: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_final_v22/vaccination_study_10/tables/source_disagreement_summary.tsv`
- Source effectiveness summary: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_final_v22/vaccination_study_10/tables/source_effectiveness_summary.tsv`
- Diagnostics tables: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_final_v22/vaccination_study_10/tables/`

