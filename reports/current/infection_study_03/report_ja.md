# HIPC データセットアノテーションレポート: infection_study_03

更新日: 2026-06-05 EDT

このレポートは `hipc-annotation` Codex workflow によって生成したデータセット別レビュー文書です。固定 method は repository README に置き、このレポートでは実際の evidence、弱い箇所、レビュー優先度、UMAP / dotplot を確認します。

## データセット概要

| study | cells | analysis_X_genes | pre_hvg_genes | counts_layer_genes | labels | parent_or_blood_fraction | Blood Cell | Doublet | artifact_like | median_confidence | low_confidence | source_disagreement | invalid_labels |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| infection_study_03 | 646,739 | 24,929 | 24,929 | 24,929 | 4 | 1.000 | 215,411 | 0 | 0 | 0.444 | 646,739 | 0 (0.000) | none |

## 実行概要

- 実行単位: one dataset in, one annotated dataset out。
- 実行経路: Codex skill `hipc-annotation` -> bundled helper `run_one.sh` -> annotation CLI -> validator -> report inspection。
- 検証: submission row count、H5AD observation count、official label validity、H5AD/submission agreement、confidence column、report image link を確認する。
- このレポートは workflow の再掲ではなく、このデータセットの marker 欠損、UMAP、label 構成、review concern を読むためのもの。

## データセット固有の解釈

- `infection_study_03`: 646,739 cells、analysis X/var 24,929 genes、pre-HVG slot 24,929 genes、submitted label 4 種、parent/Blood residual fraction 1.000、median confidence 0.444。
  - 646,739 cells は low confidence。QC / confidence UMAP 上で局在を確認する。
  - 215,411 cells は `Blood Cell` として残存。これは filter-out ではなく、曖昧な細胞を公式 parent label で残したもの。

## データセット固有の評価

- 全体像: 646,739 cells / analysis X/var 24,929 genes / pre-HVG slot 24,929 genes。parent/Blood residual は 1.000、low-confidence は 646,739 cells、source disagreement flag は 0 cells (0.000)。
- 優先確認: low-confidence 領域が QC UMAP と source-disagreement UMAP で同じ場所に集まるかを確認する。
- 優先確認: `Blood Cell` 残存が孤立 cluster なのか、複数 lineage に分散した曖昧領域なのかを UMAP で確認する。

## Marker Gene 欠損アラート

なし。

## ソース間不一致

| study | predicted_cell_type | cells | median_source_agreement | disagreement_cells | disagreement_fraction |
| --- | --- | --- | --- | --- | --- |
| infection_study_03 | B Cell | 93,274 | 0.000 | 0 | 0.000 |
| infection_study_03 | Blood Cell | 215,411 | 0.000 | 0 | 0.000 |
| infection_study_03 | Myeloid Cell | 137,478 | 0.000 | 0 | 0.000 |
| infection_study_03 | T Cell | 200,576 | 0.000 | 0 | 0.000 |

## アノテーションソース効果

この表は外部 ground truth に対する正解率ではありません。各 annotation source がどれだけの細胞で情報を持ち、final label とどれだけ一致したかを示す監査用統計です。`coverage` は source が `not_available` 以外を返した割合、`final_concordance` は informative cells の中で final label と一致した割合、`unique_support` はその source だけが final label と一致した細胞数です。

| study | source | informative_cells | coverage | final_concordance | high_conf_concordance | unique_support | discordant |
| --- | --- | --- | --- | --- | --- | --- | --- |
| infection_study_03 | Cluster marker assignment | 431,328 | 0.667 | 0.000 | 0.000 | 0 | 431,328 |
| infection_study_03 | CellTypist | 0 | 0.000 | 0.000 | 0.000 | 0 | 0 |
| infection_study_03 | Pan-human Azimuth | 0 | 0.000 | 0.000 | 0.000 | 0 | 0 |
| infection_study_03 | Cluster consensus | 0 | 0.000 | 0.000 | 0.000 | 0 | 0 |
| infection_study_03 | scRefMapping | 0 | 0.000 | 0.000 | 0.000 | 0 | 0 |

## レビュー優先事項

| study | concern | cells |
| --- | --- | --- |
| infection_study_03 | Large Blood Cell/ambiguous residual remains | 215,411 |
| infection_study_03 | Many low-confidence cells; QC or mixed-marker effects likely remain | 646,739 |

## ラベル構成

| study | predicted_cell_type | cells |
| --- | --- | --- |
| infection_study_03 | Blood Cell | 215,411 |
| infection_study_03 | T Cell | 200,576 |
| infection_study_03 | Myeloid Cell | 137,478 |
| infection_study_03 | B Cell | 93,274 |

## Inline Figures

### infection_study_03

![infection_study_03 final labels](assets/umap_infection_study_03_annotation_label.png)

![infection_study_03 lineage and annotation reason](assets/umap_infection_study_03_annotation_lineage_reason.png)

![infection_study_03 QC and confidence](assets/umap_infection_study_03_annotation_qc_confidence.png)

![infection_study_03 source agreement and disagreement](assets/umap_infection_study_03_annotation_source_disagreement.png)

![infection_study_03 annotation-source effectiveness](assets/figure_02_source_effectiveness.png)

![infection_study_03 marker expression UMAPs](assets/umap_infection_study_03_annotation_marker_expression.png)

![infection_study_03 submitted-label marker dotplot](assets/dotplot_infection_study_03_annotation_marker_dotplot.png)

#### infection_study_03 B_lineage true subcluster UMAP

![infection_study_03 B_lineage true subcluster labels](assets/umap_infection_study_03_B_lineage_true_subcluster_label.png)

![infection_study_03 B_lineage true subcluster source labels](assets/umap_infection_study_03_B_lineage_true_subcluster_source_labels.png)

![infection_study_03 B_lineage true subcluster QC](assets/umap_infection_study_03_B_lineage_true_subcluster_qc.png)

![infection_study_03 B_lineage true subcluster marker scores](assets/umap_infection_study_03_B_lineage_true_subcluster_marker_scores.png)

![infection_study_03 B_lineage true subcluster marker expression](assets/umap_infection_study_03_B_lineage_true_subcluster_marker_expression.png)

![infection_study_03 B_lineage subcluster marker score heatmap](assets/subcluster_marker_score_heatmap_infection_study_03_B_lineage.png)

![infection_study_03 B_lineage subcluster marker dotplot](assets/dotplot_infection_study_03_B_lineage_true_subcluster_marker_dotplot.png)

Tables: `tables/infection_study_03_B_lineage_true_subcluster_umap.tsv.gz`, `tables/infection_study_03_B_lineage_subcluster_candidate_scores.tsv`.

#### infection_study_03 T_NK_lineage true subcluster UMAP

![infection_study_03 T_NK_lineage true subcluster labels](assets/umap_infection_study_03_T_NK_lineage_true_subcluster_label.png)

![infection_study_03 T_NK_lineage true subcluster source labels](assets/umap_infection_study_03_T_NK_lineage_true_subcluster_source_labels.png)

![infection_study_03 T_NK_lineage true subcluster QC](assets/umap_infection_study_03_T_NK_lineage_true_subcluster_qc.png)

![infection_study_03 T_NK_lineage true subcluster marker scores](assets/umap_infection_study_03_T_NK_lineage_true_subcluster_marker_scores.png)

![infection_study_03 T_NK_lineage true subcluster marker expression](assets/umap_infection_study_03_T_NK_lineage_true_subcluster_marker_expression.png)

![infection_study_03 T_NK_lineage subcluster marker score heatmap](assets/subcluster_marker_score_heatmap_infection_study_03_T_NK_lineage.png)

![infection_study_03 T_NK_lineage subcluster marker dotplot](assets/dotplot_infection_study_03_T_NK_lineage_true_subcluster_marker_dotplot.png)

Tables: `tables/infection_study_03_T_NK_lineage_true_subcluster_umap.tsv.gz`, `tables/infection_study_03_T_NK_lineage_subcluster_candidate_scores.tsv`.

#### infection_study_03 Myeloid_lineage true subcluster UMAP

![infection_study_03 Myeloid_lineage true subcluster labels](assets/umap_infection_study_03_Myeloid_lineage_true_subcluster_label.png)

![infection_study_03 Myeloid_lineage true subcluster source labels](assets/umap_infection_study_03_Myeloid_lineage_true_subcluster_source_labels.png)

![infection_study_03 Myeloid_lineage true subcluster QC](assets/umap_infection_study_03_Myeloid_lineage_true_subcluster_qc.png)

![infection_study_03 Myeloid_lineage true subcluster marker scores](assets/umap_infection_study_03_Myeloid_lineage_true_subcluster_marker_scores.png)

![infection_study_03 Myeloid_lineage true subcluster marker expression](assets/umap_infection_study_03_Myeloid_lineage_true_subcluster_marker_expression.png)

![infection_study_03 Myeloid_lineage subcluster marker score heatmap](assets/subcluster_marker_score_heatmap_infection_study_03_Myeloid_lineage.png)

![infection_study_03 Myeloid_lineage subcluster marker dotplot](assets/dotplot_infection_study_03_Myeloid_lineage_true_subcluster_marker_dotplot.png)

Tables: `tables/infection_study_03_Myeloid_lineage_true_subcluster_umap.tsv.gz`, `tables/infection_study_03_Myeloid_lineage_subcluster_candidate_scores.tsv`.


## Subcluster Marker Score Review

上の lineage-specific panel は、各 lineage subset で HVG 選択、PCA、neighbors、Leiden、UMAP を再計算した true local subcluster analysis から生成しています。Marker gene による fine label の確認は global UMAP だけではなく、この local UMAP、CellTypist/Azimuth/Pan-human/cluster-level marker gene assignment overlay、cluster marker gate score UMAP、marker-expression UMAP、dotplot を主に見ます。Treg など sparse marker label は cell-wise marker winner ではなく、local cluster の FOXP3/IL2RA/CTLA4 など key-marker support と reference support で判定します。

## Marker Assignment Feedback

Marker gene assignment は final label を強制的に上書きするものではなく、cluster-level の自己点検です。`raw_marker_winner` は marker score だけの勝者、`marker_assignment` は conservative policy と source-supported tie-break を通した marker-based assignment です。この表は marker assignment と final/reference-driven label がずれる cluster、marker specificity が弱い cluster、scRefMap が期待される lineage で欠落する cluster を示します。`marker_score` は raw marker base score から negative/confound marker penalty を差し引いた cluster-level marker gate score です。

| study | lineage | cluster | cells | chosen_label | marker_assignment | raw_marker_winner | assignment_reason | marker_score | base_score | penalty | flags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| infection_study_03 | Myeloid_lineage | 6 | 40,314 | Myeloid Cell | Neutrophil | Neutrophil | raw_marker_winner | 0.562 | 1.000 | 0.438 | marker_final_disagreement |
| infection_study_03 | T_NK_lineage | 3 | 28,787 | T Cell | CD8 Naive / T Central Memory | CD8 Naive / T Central Memory | raw_marker_winner | 0.775 | 1.000 | 0.225 | marker_final_disagreement;screfmapping_missing_for_scope |
| infection_study_03 | Myeloid_lineage | 5 | 24,497 | Myeloid Cell | Eosinophil | Eosinophil | raw_marker_winner | 0.546 | 1.000 | 0.454 | marker_final_disagreement |
| infection_study_03 | T_NK_lineage | 5 | 23,985 | T Cell | NKT Cell | NKT Cell | raw_marker_winner | 0.875 | 1.000 | 0.125 | marker_final_disagreement;screfmapping_missing_for_scope |
| infection_study_03 | T_NK_lineage | 2 | 21,707 | T Cell | NKT Cell | NKT Cell | raw_marker_winner | 0.633 | 1.000 | 0.367 | marker_final_disagreement;screfmapping_missing_for_scope |
| infection_study_03 | Myeloid_lineage | 0 | 21,549 | Myeloid Cell | Neutrophil | Neutrophil | raw_marker_winner | 0.543 | 1.000 | 0.457 | marker_final_disagreement |
| infection_study_03 | B_lineage | 3 | 19,057 | B Cell | Naive B Cell | Naive B Cell | raw_marker_winner | 0.705 | 1.000 | 0.295 | marker_final_disagreement;screfmapping_missing_for_scope |
| infection_study_03 | T_NK_lineage | 7 | 18,018 | T Cell | NKT Cell | NKT Cell | raw_marker_winner | 0.757 | 0.959 | 0.202 | marker_final_disagreement;screfmapping_missing_for_scope |
| infection_study_03 | T_NK_lineage | 10 | 16,556 | T Cell | NKT Cell | NKT Cell | raw_marker_winner | 0.700 | 1.000 | 0.300 | marker_final_disagreement;screfmapping_missing_for_scope |
| infection_study_03 | T_NK_lineage | 4 | 16,280 | T Cell | NKT Cell | NKT Cell | raw_marker_winner | 0.816 | 0.965 | 0.149 | marker_final_disagreement;screfmapping_missing_for_scope |
| infection_study_03 | T_NK_lineage | 9 | 14,768 | T Cell | NKT Cell | NKT Cell | raw_marker_winner | 0.838 | 0.956 | 0.118 | marker_final_disagreement;screfmapping_missing_for_scope |
| infection_study_03 | T_NK_lineage | 6 | 14,672 | T Cell | NKT Cell | NKT Cell | raw_marker_winner | 0.708 | 0.977 | 0.269 | marker_final_disagreement;screfmapping_missing_for_scope |
| infection_study_03 | Myeloid_lineage | 3 | 14,243 | Myeloid Cell | Neutrophil | Neutrophil | raw_marker_winner | 0.537 | 1.000 | 0.463 | marker_final_disagreement |
| infection_study_03 | Myeloid_lineage | 1 | 13,138 | Myeloid Cell | Neutrophil | Neutrophil | raw_marker_winner | 0.530 | 1.000 | 0.470 | marker_final_disagreement |
| infection_study_03 | B_lineage | 8 | 13,111 | B Cell | Naive B Cell | Naive B Cell | raw_marker_winner | 0.612 | 0.881 | 0.269 | marker_final_disagreement;screfmapping_missing_for_scope |
| infection_study_03 | T_NK_lineage | 12 | 12,839 | T Cell | NKT Cell | NKT Cell | raw_marker_winner | 0.643 | 1.000 | 0.357 | marker_final_disagreement;screfmapping_missing_for_scope |
| infection_study_03 | B_lineage | 5 | 11,816 | B Cell | Naive B Cell | Naive B Cell | raw_marker_winner | 0.660 | 1.000 | 0.340 | marker_final_disagreement;screfmapping_missing_for_scope |
| infection_study_03 | B_lineage | 9 | 11,192 | B Cell | Naive B Cell | Naive B Cell | raw_marker_winner | 0.641 | 1.000 | 0.359 | marker_final_disagreement;screfmapping_missing_for_scope |
| infection_study_03 | T_NK_lineage | 11 | 10,820 | T Cell | NKT Cell | NKT Cell | raw_marker_winner | 0.621 | 1.000 | 0.379 | marker_final_disagreement;screfmapping_missing_for_scope |
| infection_study_03 | T_NK_lineage | 1 | 9,724 | T Cell | NKT Cell | NKT Cell | raw_marker_winner | 0.620 | 1.000 | 0.380 | marker_final_disagreement;screfmapping_missing_for_scope |

## LLM Review Queue

この表は Codex/LLM が読むための subcluster-level review queue です。LLM はこの evidence を読んで、final label が妥当か、ontology にちょうどよい label がないのか、registry / conservative policy を一般ルールとして更新すべきかを提案します。LLM の出力で per-cell label を直接書き換えず、採用する場合は registry/config を更新して deterministic pipeline を再実行します。

| study | lineage | cluster | cells | priority | reasons | suggested_action | final_label | marker_assignment | raw_marker_winner | score_margin |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| infection_study_03 | T_NK_lineage | 2 | 21,707 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | T Cell | NKT Cell | NKT Cell | 0.039 |
| infection_study_03 | T_NK_lineage | 7 | 18,018 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | T Cell | NKT Cell | NKT Cell | 0.044 |
| infection_study_03 | T_NK_lineage | 10 | 16,556 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | T Cell | NKT Cell | NKT Cell | 0.046 |
| infection_study_03 | T_NK_lineage | 4 | 16,280 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | T Cell | NKT Cell | NKT Cell | 0.064 |
| infection_study_03 | T_NK_lineage | 9 | 14,768 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | T Cell | NKT Cell | NKT Cell | 0.056 |
| infection_study_03 | T_NK_lineage | 6 | 14,672 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | T Cell | NKT Cell | NKT Cell | 0.038 |
| infection_study_03 | T_NK_lineage | 12 | 12,839 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | T Cell | NKT Cell | NKT Cell | 0.066 |
| infection_study_03 | T_NK_lineage | 11 | 10,820 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | T Cell | NKT Cell | NKT Cell | 0.023 |
| infection_study_03 | T_NK_lineage | 1 | 9,724 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | T Cell | NKT Cell | NKT Cell | 0.066 |
| infection_study_03 | B_lineage | 4 | 9,714 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | B Cell | Plasmablast | Plasmablast | 0.010 |
| infection_study_03 | B_lineage | 2 | 9,073 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | B Cell | Plasmablast | Plasmablast | 0.175 |
| infection_study_03 | B_lineage | 1 | 5,017 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | B Cell | Plasma Cell | Plasma Cell | 0.009 |
| infection_study_03 | B_lineage | 0 | 4,685 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | B Cell | Plasma Cell | Plasma Cell | 0.006 |
| infection_study_03 | T_NK_lineage | 0 | 4,437 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | T Cell | NKT Cell | NKT Cell | 0.199 |
| infection_study_03 | Myeloid_lineage | 6 | 40,314 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | Myeloid Cell | Neutrophil | Neutrophil | 0.022 |
| infection_study_03 | T_NK_lineage | 3 | 28,787 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | T Cell | CD8 Naive / T Central Memory | CD8 Naive / T Central Memory | 0.011 |
| infection_study_03 | Myeloid_lineage | 5 | 24,497 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | Myeloid Cell | Eosinophil | Eosinophil | 0.002 |
| infection_study_03 | T_NK_lineage | 5 | 23,985 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available | check_if_finer_official_label_is_supported | T Cell | NKT Cell | NKT Cell | 0.256 |
| infection_study_03 | Myeloid_lineage | 0 | 21,549 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | Myeloid Cell | Neutrophil | Neutrophil | 0.055 |
| infection_study_03 | B_lineage | 3 | 19,057 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | B Cell | Naive B Cell | Naive B Cell | 0.705 |

## Cluster Consensus Evidence

| study | lineage | cluster | cells | chosen_label | accepted | score_margin | cluster_marker_assignment | treg_key_any | treg_key_bonus | marker_set | marker_alert |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| infection_study_03 | B_lineage | 3 | 19,057 | B Cell | False | 0.705 | Naive B Cell | nan | nan | registry__naive_b_cell | pass |
| infection_study_03 | B_lineage | 8 | 13,111 | B Cell | False | 0.594 | Naive B Cell | nan | nan | registry__naive_b_cell | pass |
| infection_study_03 | B_lineage | 5 | 11,816 | B Cell | False | 0.660 | Naive B Cell | nan | nan | registry__naive_b_cell | pass |
| infection_study_03 | B_lineage | 9 | 11,192 | B Cell | False | 0.630 | Naive B Cell | nan | nan | registry__naive_b_cell | pass |
| infection_study_03 | B_lineage | 4 | 9,714 | B Cell | False | 0.010 | Plasmablast | nan | nan | registry__plasmablast | pass |
| infection_study_03 | B_lineage | 2 | 9,073 | B Cell | False | 0.175 | Plasmablast | nan | nan | registry__plasmablast | pass |
| infection_study_03 | B_lineage | 6 | 8,399 | B Cell | False | 0.225 | Naive B Cell | nan | nan | registry__naive_b_cell | pass |
| infection_study_03 | B_lineage | 1 | 5,017 | B Cell | False | 0.009 | Plasma Cell | nan | nan | registry__plasma_cell | pass |
| infection_study_03 | B_lineage | 0 | 4,685 | B Cell | False | 0.006 | Plasma Cell | nan | nan | registry__plasma_cell | pass |
| infection_study_03 | B_lineage | 7 | 1,210 | B Cell | False | 0.487 | Naive B Cell | nan | nan | registry__naive_b_cell | pass |
| infection_study_03 | Myeloid_lineage | 6 | 40,314 | Myeloid Cell | False | 0.022 | Neutrophil | nan | nan | registry__neutrophil | pass |
| infection_study_03 | Myeloid_lineage | 5 | 24,497 | Myeloid Cell | False | 0.002 | Eosinophil | nan | nan | registry__eosinophil | pass |
| infection_study_03 | Myeloid_lineage | 0 | 21,549 | Myeloid Cell | False | 0.055 | Neutrophil | nan | nan | registry__neutrophil | pass |
| infection_study_03 | Myeloid_lineage | 3 | 14,243 | Myeloid Cell | False | 0.077 | Neutrophil | nan | nan | registry__neutrophil | pass |
| infection_study_03 | Myeloid_lineage | 1 | 13,138 | Myeloid Cell | False | 0.054 | Neutrophil | nan | nan | registry__neutrophil | pass |
| infection_study_03 | Myeloid_lineage | 2 | 8,728 | Myeloid Cell | False | 0.105 | Neutrophil | nan | nan | registry__neutrophil | pass |
| infection_study_03 | Myeloid_lineage | 4 | 6,666 | Myeloid Cell | False | 0.104 | Neutrophil | nan | nan | registry__neutrophil | pass |
| infection_study_03 | Myeloid_lineage | 8 | 3,424 | Myeloid Cell | False | 0.090 | Intermediate Monocyte | nan | nan | registry__intermediate_monocyte | pass |
| infection_study_03 | Myeloid_lineage | 9 | 2,629 | Myeloid Cell | False | 0.058 | Neutrophil | nan | nan | registry__neutrophil | pass |
| infection_study_03 | Myeloid_lineage | 7 | 2,290 | Myeloid Cell | False | 0.070 | Neutrophil | nan | nan | registry__neutrophil | pass |
| infection_study_03 | T_NK_lineage | 3 | 28,787 | T Cell | False | 0.011 | CD8 Naive / T Central Memory | 0.105 | 0.000 | registry__cd8_naive_t_central_memory | pass |
| infection_study_03 | T_NK_lineage | 5 | 23,985 | T Cell | False | 0.256 | NKT Cell | 0.007 | 0.000 | registry__nkt_cell | pass |
| infection_study_03 | T_NK_lineage | 2 | 21,707 | T Cell | False | 0.039 | NKT Cell | 0.025 | 0.000 | registry__nkt_cell | pass |
| infection_study_03 | T_NK_lineage | 7 | 18,018 | T Cell | False | 0.044 | NKT Cell | 0.150 | 0.000 | registry__nkt_cell | pass |
| infection_study_03 | T_NK_lineage | 10 | 16,556 | T Cell | False | 0.046 | NKT Cell | 0.021 | 0.000 | registry__nkt_cell | pass |
| infection_study_03 | T_NK_lineage | 4 | 16,280 | T Cell | False | 0.064 | NKT Cell | 0.131 | 0.000 | registry__nkt_cell | pass |
| infection_study_03 | T_NK_lineage | 9 | 14,768 | T Cell | False | 0.056 | NKT Cell | 0.130 | 0.000 | registry__nkt_cell | pass |
| infection_study_03 | T_NK_lineage | 6 | 14,672 | T Cell | False | 0.038 | NKT Cell | 0.110 | 0.000 | registry__nkt_cell | pass |
| infection_study_03 | T_NK_lineage | 12 | 12,839 | T Cell | False | 0.066 | NKT Cell | 0.031 | 0.000 | registry__nkt_cell | pass |
| infection_study_03 | T_NK_lineage | 11 | 10,820 | T Cell | False | 0.023 | NKT Cell | 0.028 | 0.000 | registry__nkt_cell | pass |

## 出力ファイル

- Submission TSVs: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_final_v22/infection_study_03/submissions/`
- cellxgene H5ADs: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_final_v22/infection_study_03/cellxgene/`
- Marker availability table: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_final_v22/infection_study_03/tables/marker_gene_availability.tsv`
- Marker availability alerts: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_final_v22/infection_study_03/tables/marker_gene_availability_alerts.tsv`
- Subcluster evidence: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_final_v22/infection_study_03/tables/lineage_subcluster_evidence.tsv.gz`
- Source disagreement summary: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_final_v22/infection_study_03/tables/source_disagreement_summary.tsv`
- Source effectiveness summary: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_final_v22/infection_study_03/tables/source_effectiveness_summary.tsv`
- Diagnostics tables: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_final_v22/infection_study_03/tables/`

