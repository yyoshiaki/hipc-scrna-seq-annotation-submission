# HIPC データセットアノテーションレポート: infection_study_06

更新日: 2026-06-12 EDT

このレポートは `hipc-annotation` Codex workflow によって生成したデータセット別レビュー文書です。固定 method は repository README に置き、このレポートでは実際の evidence、弱い箇所、レビュー優先度、UMAP / dotplot を確認します。

## 2026-06-12 提出候補メモ

- 現行の緊急提出候補では、この dataset は v23 aggressive marker-rescue output を採用しています。
- `feature_name` 由来の gene symbol 修正により marker gene は見えるようになりましたが、parent/Blood residual fraction は 0.8234 と高く、まだ fine annotation は不十分です。
- reference-transfer evidence が弱く、marker-only rescue に寄っているため、NKT などの一部 label は過剰割り当ての可能性があります。
- 次に改善するなら、Harmony などで batch/sample structure を補正した embedding を作り、cluster-level assignment をやり直す必要があります。

## データセット概要

| study | cells | analysis_X_genes | pre_hvg_genes | counts_layer_genes | labels | parent_or_blood_fraction | Blood Cell | Doublet | artifact_like | median_confidence | low_confidence | source_disagreement | invalid_labels |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| infection_study_06 | 827,389 | 37,298 | 37,298 | 37,298 | 9 | 0.823 | 235,558 | 0 | 0 | 0.450 | 827,389 | 0 (0.000) | none |

## 実行概要

- 実行単位: one dataset in, one annotated dataset out。
- 実行経路: Codex skill `hipc-annotation` -> bundled helper `run_one.sh` -> annotation CLI -> validator -> report inspection。
- 検証: submission row count、H5AD observation count、official label validity、H5AD/submission agreement、confidence column、report image link を確認する。
- このレポートは workflow の再掲ではなく、このデータセットの marker 欠損、UMAP、label 構成、review concern を読むためのもの。

## データセット固有の解釈

- `infection_study_06`: 827,389 cells、analysis X/var 37,298 genes、pre-HVG slot 37,298 genes、submitted label 9 種、parent/Blood residual fraction 0.823、median confidence 0.450。
  - 827,389 cells は low confidence。QC / confidence UMAP 上で局在を確認する。
  - 235,558 cells は `Blood Cell` として残存。これは filter-out ではなく、曖昧な細胞を公式 parent label で残したもの。

## データセット固有の評価

- 全体像: 827,389 cells / analysis X/var 37,298 genes / pre-HVG slot 37,298 genes。parent/Blood residual は 0.823、low-confidence は 827,389 cells、source disagreement flag は 0 cells (0.000)。
- 優先確認: low-confidence 領域が QC UMAP と source-disagreement UMAP で同じ場所に集まるかを確認する。
- 優先確認: `Blood Cell` 残存が孤立 cluster なのか、複数 lineage に分散した曖昧領域なのかを UMAP で確認する。

## Marker Gene 欠損アラート

なし。

## ソース間不一致

| study | predicted_cell_type | cells | median_source_agreement | disagreement_cells | disagreement_fraction |
| --- | --- | --- | --- | --- | --- |
| infection_study_06 | B Cell | 73,729 | 0.000 | 0 | 0.000 |
| infection_study_06 | Blood Cell | 235,558 | 0.000 | 0 | 0.000 |
| infection_study_06 | CD8 Naive / T Central Memory | 19,442 | 0.000 | 0 | 0.000 |
| infection_study_06 | Classical Monocyte | 21,846 | 0.000 | 0 | 0.000 |
| infection_study_06 | Myeloid Cell | 197,279 | 0.000 | 0 | 0.000 |
| infection_study_06 | NKT Cell | 83,080 | 0.000 | 0 | 0.000 |
| infection_study_06 | Naive B Cell | 18,040 | 0.000 | 0 | 0.000 |
| infection_study_06 | Neutrophil | 3,723 | 0.000 | 0 | 0.000 |
| infection_study_06 | T Cell | 174,692 | 0.000 | 0 | 0.000 |

## アノテーションソース効果

この表は外部 ground truth に対する正解率ではありません。各 annotation source がどれだけの細胞で情報を持ち、final label とどれだけ一致したかを示す監査用統計です。`coverage` は source が `not_available` 以外を返した割合、`final_concordance` は informative cells の中で final label と一致した割合、`unique_support` はその source だけが final label と一致した細胞数です。

| study | source | informative_cells | coverage | final_concordance | high_conf_concordance | unique_support | discordant |
| --- | --- | --- | --- | --- | --- | --- | --- |
| infection_study_06 | Cluster marker assignment | 591,831 | 0.715 | 0.247 | 0.000 | 146,131 | 445,700 |
| infection_study_06 | CellTypist | 0 | 0.000 | 0.000 | 0.000 | 0 | 0 |
| infection_study_06 | Pan-human Azimuth | 0 | 0.000 | 0.000 | 0.000 | 0 | 0 |
| infection_study_06 | Cluster consensus | 0 | 0.000 | 0.000 | 0.000 | 0 | 0 |
| infection_study_06 | scRefMapping | 0 | 0.000 | 0.000 | 0.000 | 0 | 0 |

## レビュー優先事項

| study | concern | cells |
| --- | --- | --- |
| infection_study_06 | Large Blood Cell/ambiguous residual remains | 235,558 |
| infection_study_06 | Many low-confidence cells; QC or mixed-marker effects likely remain | 827,389 |

## ラベル構成

| study | predicted_cell_type | cells |
| --- | --- | --- |
| infection_study_06 | Blood Cell | 235,558 |
| infection_study_06 | Myeloid Cell | 197,279 |
| infection_study_06 | T Cell | 174,692 |
| infection_study_06 | NKT Cell | 83,080 |
| infection_study_06 | B Cell | 73,729 |
| infection_study_06 | Classical Monocyte | 21,846 |
| infection_study_06 | CD8 Naive / T Central Memory | 19,442 |
| infection_study_06 | Naive B Cell | 18,040 |
| infection_study_06 | Neutrophil | 3,723 |

## Inline Figures

### infection_study_06

![infection_study_06 final labels](assets/umap_infection_study_06_annotation_label.png)

![infection_study_06 lineage and annotation reason](assets/umap_infection_study_06_annotation_lineage_reason.png)

![infection_study_06 QC and confidence](assets/umap_infection_study_06_annotation_qc_confidence.png)

![infection_study_06 source agreement and disagreement](assets/umap_infection_study_06_annotation_source_disagreement.png)

![infection_study_06 annotation-source effectiveness](assets/figure_02_source_effectiveness.png)

![infection_study_06 marker expression UMAPs](assets/umap_infection_study_06_annotation_marker_expression.png)

![infection_study_06 submitted-label marker dotplot](assets/dotplot_infection_study_06_annotation_marker_dotplot.png)

#### infection_study_06 B_lineage true subcluster UMAP

![infection_study_06 B_lineage true subcluster labels](assets/umap_infection_study_06_B_lineage_true_subcluster_label.png)

![infection_study_06 B_lineage true subcluster source labels](assets/umap_infection_study_06_B_lineage_true_subcluster_source_labels.png)

![infection_study_06 B_lineage true subcluster QC](assets/umap_infection_study_06_B_lineage_true_subcluster_qc.png)

![infection_study_06 B_lineage true subcluster marker scores](assets/umap_infection_study_06_B_lineage_true_subcluster_marker_scores.png)

![infection_study_06 B_lineage true subcluster marker expression](assets/umap_infection_study_06_B_lineage_true_subcluster_marker_expression.png)

![infection_study_06 B_lineage subcluster marker score heatmap](assets/subcluster_marker_score_heatmap_infection_study_06_B_lineage.png)

![infection_study_06 B_lineage subcluster marker dotplot](assets/dotplot_infection_study_06_B_lineage_true_subcluster_marker_dotplot.png)

Tables: `tables/infection_study_06_B_lineage_true_subcluster_umap.tsv.gz`, `tables/infection_study_06_B_lineage_subcluster_candidate_scores.tsv`.

#### infection_study_06 T_NK_lineage true subcluster UMAP

![infection_study_06 T_NK_lineage true subcluster labels](assets/umap_infection_study_06_T_NK_lineage_true_subcluster_label.png)

![infection_study_06 T_NK_lineage true subcluster source labels](assets/umap_infection_study_06_T_NK_lineage_true_subcluster_source_labels.png)

![infection_study_06 T_NK_lineage true subcluster QC](assets/umap_infection_study_06_T_NK_lineage_true_subcluster_qc.png)

![infection_study_06 T_NK_lineage true subcluster marker scores](assets/umap_infection_study_06_T_NK_lineage_true_subcluster_marker_scores.png)

![infection_study_06 T_NK_lineage true subcluster marker expression](assets/umap_infection_study_06_T_NK_lineage_true_subcluster_marker_expression.png)

![infection_study_06 T_NK_lineage subcluster marker score heatmap](assets/subcluster_marker_score_heatmap_infection_study_06_T_NK_lineage.png)

![infection_study_06 T_NK_lineage subcluster marker dotplot](assets/dotplot_infection_study_06_T_NK_lineage_true_subcluster_marker_dotplot.png)

Tables: `tables/infection_study_06_T_NK_lineage_true_subcluster_umap.tsv.gz`, `tables/infection_study_06_T_NK_lineage_subcluster_candidate_scores.tsv`.

#### infection_study_06 Myeloid_lineage true subcluster UMAP

![infection_study_06 Myeloid_lineage true subcluster labels](assets/umap_infection_study_06_Myeloid_lineage_true_subcluster_label.png)

![infection_study_06 Myeloid_lineage true subcluster source labels](assets/umap_infection_study_06_Myeloid_lineage_true_subcluster_source_labels.png)

![infection_study_06 Myeloid_lineage true subcluster QC](assets/umap_infection_study_06_Myeloid_lineage_true_subcluster_qc.png)

![infection_study_06 Myeloid_lineage true subcluster marker scores](assets/umap_infection_study_06_Myeloid_lineage_true_subcluster_marker_scores.png)

![infection_study_06 Myeloid_lineage true subcluster marker expression](assets/umap_infection_study_06_Myeloid_lineage_true_subcluster_marker_expression.png)

![infection_study_06 Myeloid_lineage subcluster marker score heatmap](assets/subcluster_marker_score_heatmap_infection_study_06_Myeloid_lineage.png)

![infection_study_06 Myeloid_lineage subcluster marker dotplot](assets/dotplot_infection_study_06_Myeloid_lineage_true_subcluster_marker_dotplot.png)

Tables: `tables/infection_study_06_Myeloid_lineage_true_subcluster_umap.tsv.gz`, `tables/infection_study_06_Myeloid_lineage_subcluster_candidate_scores.tsv`.


## Subcluster Marker Score Review

上の lineage-specific panel は、各 lineage subset で HVG 選択、PCA、neighbors、Leiden、UMAP を再計算した true local subcluster analysis から生成しています。Marker gene による fine label の確認は global UMAP だけではなく、この local UMAP、CellTypist/Azimuth/Pan-human/cluster-level marker gene assignment overlay、cluster marker gate score UMAP、marker-expression UMAP、dotplot を主に見ます。Treg など sparse marker label は cell-wise marker winner ではなく、local cluster の FOXP3/IL2RA/CTLA4 など key-marker support と reference support で判定します。

## Marker Assignment Feedback

Marker gene assignment は final label を強制的に上書きするものではなく、cluster-level の自己点検です。`raw_marker_winner` は marker score だけの勝者、`marker_assignment` は conservative policy と source-supported tie-break を通した marker-based assignment です。この表は marker assignment と final/reference-driven label がずれる cluster、marker specificity が弱い cluster、scRefMap が期待される lineage で欠落する cluster を示します。`marker_score` は raw marker base score から negative/confound marker penalty を差し引いた cluster-level marker gate score です。

| study | lineage | cluster | cells | chosen_label | marker_assignment | raw_marker_winner | assignment_reason | marker_score | base_score | penalty | flags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| infection_study_06 | T_NK_lineage | 3 | 31,206 | NKT Cell | NKT Cell | NKT Cell | raw_marker_winner | 0.853 | 1.000 | 0.147 | screfmapping_missing_for_scope |
| infection_study_06 | T_NK_lineage | 16 | 29,148 | T Cell | NKT Cell | NKT Cell | raw_marker_winner | 0.912 | 0.980 | 0.068 | marker_final_disagreement;screfmapping_missing_for_scope |
| infection_study_06 | T_NK_lineage | 10 | 25,617 | T Cell | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | raw_marker_winner | 0.554 | 1.000 | 0.446 | marker_final_disagreement;screfmapping_missing_for_scope |
| infection_study_06 | Myeloid_lineage | 5 | 23,886 | Myeloid Cell | Classical Monocyte | Classical Monocyte | raw_marker_winner | 0.598 | 1.000 | 0.402 | marker_final_disagreement |
| infection_study_06 | Myeloid_lineage | 0 | 23,556 | Myeloid Cell | Eosinophil | Eosinophil | raw_marker_winner | 0.543 | 1.000 | 0.457 | marker_final_disagreement |
| infection_study_06 | B_lineage | 0 | 22,889 | B Cell | Naive B Cell | Naive B Cell | raw_marker_winner | 0.538 | 0.924 | 0.385 | marker_final_disagreement;screfmapping_missing_for_scope |
| infection_study_06 | Myeloid_lineage | 6 | 22,627 | Myeloid Cell | Classical Monocyte | Classical Monocyte | raw_marker_winner | 0.576 | 1.000 | 0.424 | marker_final_disagreement |
| infection_study_06 | T_NK_lineage | 1 | 21,851 | T Cell | NKT Cell | NKT Cell | raw_marker_winner | 0.893 | 0.974 | 0.081 | marker_final_disagreement;screfmapping_missing_for_scope |
| infection_study_06 | Myeloid_lineage | 12 | 20,816 | Myeloid Cell | Neutrophil | Neutrophil | raw_marker_winner | 0.527 | 1.000 | 0.473 | marker_final_disagreement |
| infection_study_06 | Myeloid_lineage | 3 | 20,611 | Myeloid Cell | Neutrophil | Neutrophil | raw_marker_winner | 0.510 | 1.000 | 0.490 | marker_final_disagreement |
| infection_study_06 | B_lineage | 2 | 20,528 | B Cell | Plasma Cell | Plasma Cell | raw_marker_winner | 0.589 | 1.000 | 0.411 | marker_final_disagreement;screfmapping_missing_for_scope |
| infection_study_06 | T_NK_lineage | 5 | 19,442 | CD8 Naive / T Central Memory | CD8 Naive / T Central Memory | CD8 Naive / T Central Memory | raw_marker_winner | 0.796 | 1.000 | 0.204 | screfmapping_missing_for_scope |
| infection_study_06 | T_NK_lineage | 14 | 18,554 | T Cell | NKT Cell | NKT Cell | raw_marker_winner | 0.859 | 0.988 | 0.129 | marker_final_disagreement;screfmapping_missing_for_scope |
| infection_study_06 | B_lineage | 6 | 18,040 | Naive B Cell | Naive B Cell | Naive B Cell | raw_marker_winner | 0.590 | 1.000 | 0.410 | screfmapping_missing_for_scope |
| infection_study_06 | Myeloid_lineage | 8 | 17,621 | Myeloid Cell | Neutrophil | Neutrophil | raw_marker_winner | 0.507 | 1.000 | 0.493 | marker_final_disagreement |
| infection_study_06 | Myeloid_lineage | 10 | 17,477 | Myeloid Cell | Neutrophil | Neutrophil | raw_marker_winner | 0.525 | 1.000 | 0.475 | marker_final_disagreement |
| infection_study_06 | T_NK_lineage | 4 | 17,442 | NKT Cell | NKT Cell | NKT Cell | raw_marker_winner | 0.780 | 1.000 | 0.220 | screfmapping_missing_for_scope |
| infection_study_06 | Myeloid_lineage | 4 | 16,475 | Myeloid Cell | Neutrophil | Neutrophil | raw_marker_winner | 0.509 | 1.000 | 0.491 | marker_final_disagreement |
| infection_study_06 | T_NK_lineage | 2 | 16,267 | T Cell | NKT Cell | NKT Cell | raw_marker_winner | 0.721 | 1.000 | 0.279 | marker_final_disagreement;screfmapping_missing_for_scope |
| infection_study_06 | T_NK_lineage | 17 | 15,470 | NKT Cell | NKT Cell | NKT Cell | raw_marker_winner | 0.812 | 0.987 | 0.175 | screfmapping_missing_for_scope |

## LLM Review Queue

この表は Codex/LLM が読むための subcluster-level review queue です。LLM はこの evidence を読んで、final label が妥当か、ontology にちょうどよい label がないのか、registry / conservative policy を一般ルールとして更新すべきかを提案します。LLM の出力で per-cell label を直接書き換えず、採用する場合は registry/config を更新して deterministic pipeline を再実行します。

| study | lineage | cluster | cells | priority | reasons | suggested_action | final_label | marker_assignment | raw_marker_winner | score_margin |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| infection_study_06 | T_NK_lineage | 16 | 29,148 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | T Cell | NKT Cell | NKT Cell | 0.077 |
| infection_study_06 | T_NK_lineage | 1 | 21,851 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | T Cell | NKT Cell | NKT Cell | 0.078 |
| infection_study_06 | B_lineage | 2 | 20,528 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | B Cell | Plasma Cell | Plasma Cell | 0.092 |
| infection_study_06 | T_NK_lineage | 2 | 16,267 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | T Cell | NKT Cell | NKT Cell | 0.103 |
| infection_study_06 | T_NK_lineage | 11 | 13,270 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | T Cell | NKT Cell | NKT Cell | 0.055 |
| infection_study_06 | T_NK_lineage | 8 | 11,374 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | T Cell | NKT Cell | NKT Cell | 0.097 |
| infection_study_06 | T_NK_lineage | 12 | 10,807 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | T Cell | NKT Cell | NKT Cell | 0.139 |
| infection_study_06 | B_lineage | 4 | 6,221 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | B Cell | Plasmablast | Plasmablast | 0.113 |
| infection_study_06 | B_lineage | 3 | 6,079 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | B Cell | Plasmablast | Plasmablast | 0.018 |
| infection_study_06 | T_NK_lineage | 15 | 5,348 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | T Cell | NKT Cell | NKT Cell | 0.045 |
| infection_study_06 | B_lineage | 1 | 4,854 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | B Cell | Plasmablast | Plasmablast | 0.009 |
| infection_study_06 | B_lineage | 9 | 3,761 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | B Cell | Plasma Cell | Plasma Cell | 0.094 |
| infection_study_06 | B_lineage | 8 | 3,685 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | B Cell | Plasmablast | Plasmablast | 0.122 |
| infection_study_06 | T_NK_lineage | 10 | 25,617 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | T Cell | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | 0.026 |
| infection_study_06 | Myeloid_lineage | 5 | 23,886 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | Myeloid Cell | Classical Monocyte | Classical Monocyte | 0.067 |
| infection_study_06 | Myeloid_lineage | 0 | 23,556 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | Myeloid Cell | Eosinophil | Eosinophil | 0.020 |
| infection_study_06 | B_lineage | 0 | 22,889 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | B Cell | Naive B Cell | Naive B Cell | 0.508 |
| infection_study_06 | Myeloid_lineage | 6 | 22,627 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | Myeloid Cell | Classical Monocyte | Classical Monocyte | 0.040 |
| infection_study_06 | Myeloid_lineage | 12 | 20,816 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | Myeloid Cell | Neutrophil | Neutrophil | 0.000 |
| infection_study_06 | Myeloid_lineage | 3 | 20,611 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | Myeloid Cell | Neutrophil | Neutrophil | 0.008 |

## Cluster Consensus Evidence

| study | lineage | cluster | cells | chosen_label | accepted | score_margin | cluster_marker_assignment | treg_key_any | treg_key_bonus | marker_set | marker_alert |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| infection_study_06 | B_lineage | 0 | 22,889 | B Cell | False | 0.508 | Naive B Cell | nan | nan | registry__naive_b_cell | pass |
| infection_study_06 | B_lineage | 2 | 20,528 | B Cell | False | 0.092 | Plasma Cell | nan | nan | registry__plasma_cell | pass |
| infection_study_06 | B_lineage | 6 | 18,040 | Naive B Cell | True | 0.415 | Naive B Cell | nan | nan | registry__naive_b_cell | pass |
| infection_study_06 | B_lineage | 4 | 6,221 | B Cell | False | 0.113 | Plasmablast | nan | nan | registry__plasmablast | pass |
| infection_study_06 | B_lineage | 3 | 6,079 | B Cell | False | 0.018 | Plasmablast | nan | nan | registry__plasmablast | pass |
| infection_study_06 | B_lineage | 1 | 4,854 | B Cell | False | 0.009 | Plasmablast | nan | nan | registry__plasmablast | pass |
| infection_study_06 | B_lineage | 7 | 4,346 | B Cell | False | 0.007 | Memory B Cell | nan | nan | registry__memory_b_cell | pass |
| infection_study_06 | B_lineage | 9 | 3,761 | B Cell | False | 0.094 | Plasma Cell | nan | nan | registry__plasma_cell | pass |
| infection_study_06 | B_lineage | 8 | 3,685 | B Cell | False | 0.122 | Plasmablast | nan | nan | registry__plasmablast | pass |
| infection_study_06 | B_lineage | 5 | 1,366 | B Cell | False | 0.085 | Naive B Cell | nan | nan | registry__naive_b_cell | pass |
| infection_study_06 | Myeloid_lineage | 5 | 23,886 | Myeloid Cell | False | 0.067 | Classical Monocyte | nan | nan | registry__classical_monocyte | pass |
| infection_study_06 | Myeloid_lineage | 0 | 23,556 | Myeloid Cell | False | 0.020 | Eosinophil | nan | nan | registry__eosinophil | pass |
| infection_study_06 | Myeloid_lineage | 6 | 22,627 | Myeloid Cell | False | 0.040 | Classical Monocyte | nan | nan | registry__classical_monocyte | pass |
| infection_study_06 | Myeloid_lineage | 13 | 21,846 | Classical Monocyte | True | 0.209 | Classical Monocyte | nan | nan | registry__classical_monocyte | pass |
| infection_study_06 | Myeloid_lineage | 12 | 20,816 | Myeloid Cell | False | 0.000 | Neutrophil | nan | nan | registry__neutrophil | pass |
| infection_study_06 | Myeloid_lineage | 3 | 20,611 | Myeloid Cell | False | 0.008 | Neutrophil | nan | nan | registry__neutrophil | pass |
| infection_study_06 | Myeloid_lineage | 8 | 17,621 | Myeloid Cell | False | 0.066 | Neutrophil | nan | nan | registry__neutrophil | pass |
| infection_study_06 | Myeloid_lineage | 10 | 17,477 | Myeloid Cell | False | 0.063 | Neutrophil | nan | nan | registry__neutrophil | pass |
| infection_study_06 | Myeloid_lineage | 4 | 16,475 | Myeloid Cell | False | 0.013 | Neutrophil | nan | nan | registry__neutrophil | pass |
| infection_study_06 | Myeloid_lineage | 11 | 13,225 | Myeloid Cell | False | 0.094 | Neutrophil | nan | nan | registry__neutrophil | pass |
| infection_study_06 | Myeloid_lineage | 1 | 11,335 | Myeloid Cell | False | 0.089 | Neutrophil | nan | nan | registry__neutrophil | pass |
| infection_study_06 | Myeloid_lineage | 7 | 6,509 | Myeloid Cell | False | 0.082 | Neutrophil | nan | nan | registry__neutrophil | pass |
| infection_study_06 | Myeloid_lineage | 9 | 3,723 | Neutrophil | True | 0.287 | Neutrophil | nan | nan | registry__neutrophil | pass |
| infection_study_06 | Myeloid_lineage | 2 | 3,141 | Myeloid Cell | False | 0.103 | Intermediate Monocyte | nan | nan | registry__intermediate_monocyte | pass |
| infection_study_06 | T_NK_lineage | 3 | 31,206 | NKT Cell | True | 0.238 | NKT Cell | 0.010 | 0.000 | registry__nkt_cell | pass |
| infection_study_06 | T_NK_lineage | 16 | 29,148 | T Cell | False | 0.077 | NKT Cell | 0.107 | 0.000 | registry__nkt_cell | pass |
| infection_study_06 | T_NK_lineage | 10 | 25,617 | T Cell | False | 0.026 | CD8 Cytotoxic / T Effector Memory | 0.032 | 0.000 | registry__cd8_cytotoxic_t_effector_memory | pass |
| infection_study_06 | T_NK_lineage | 1 | 21,851 | T Cell | False | 0.078 | NKT Cell | 0.147 | 0.000 | registry__nkt_cell | pass |
| infection_study_06 | T_NK_lineage | 5 | 19,442 | CD8 Naive / T Central Memory | True | 0.314 | CD8 Naive / T Central Memory | 0.033 | 0.000 | registry__cd8_naive_t_central_memory | pass |
| infection_study_06 | T_NK_lineage | 14 | 18,554 | T Cell | False | 0.105 | NKT Cell | 0.204 | 0.000 | registry__nkt_cell | pass |

## 出力ファイル

- Submission TSVs: `outputs/submission_v23_marker_rescue_scavenge/infection_study_06/submissions/`
- cellxgene H5ADs: `outputs/submission_v23_marker_rescue_scavenge/infection_study_06/cellxgene/`
- Marker availability table: `outputs/submission_v23_marker_rescue_scavenge/infection_study_06/tables/marker_gene_availability.tsv`
- Marker availability alerts: `outputs/submission_v23_marker_rescue_scavenge/infection_study_06/tables/marker_gene_availability_alerts.tsv`
- Subcluster evidence: `outputs/submission_v23_marker_rescue_scavenge/infection_study_06/tables/lineage_subcluster_evidence.tsv.gz`
- Source disagreement summary: `outputs/submission_v23_marker_rescue_scavenge/infection_study_06/tables/source_disagreement_summary.tsv`
- Source effectiveness summary: `outputs/submission_v23_marker_rescue_scavenge/infection_study_06/tables/source_effectiveness_summary.tsv`
- Diagnostics tables: `outputs/submission_v23_marker_rescue_scavenge/infection_study_06/tables/`
