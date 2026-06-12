# HIPC データセットアノテーションレポート: infection_study_04

更新日: 2026-06-05 EDT

このレポートは `hipc-annotation` Codex workflow によって生成したデータセット別レビュー文書です。固定 method は repository README に置き、このレポートでは実際の evidence、弱い箇所、レビュー優先度、UMAP / dotplot を確認します。

## データセット概要

| study | cells | analysis_X_genes | pre_hvg_genes | counts_layer_genes | labels | parent_or_blood_fraction | Blood Cell | Doublet | artifact_like | median_confidence | low_confidence | source_disagreement | invalid_labels |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| infection_study_04 | 43,767 | 3,933 | 8,000 | 3,933 | 15 | 0.010 | 436 | 61 | 166 | 0.776 | 497 | 9,576 (0.219) | none |

## 実行概要

- 実行単位: one dataset in, one annotated dataset out。
- 実行経路: Codex skill `hipc-annotation` -> bundled helper `run_one.sh` -> annotation CLI -> validator -> report inspection。
- 検証: submission row count、H5AD observation count、official label validity、H5AD/submission agreement、confidence column、report image link を確認する。
- このレポートは workflow の再掲ではなく、このデータセットの marker 欠損、UMAP、label 構成、review concern を読むためのもの。

## データセット固有の解釈

- `infection_study_04`: 43,767 cells、analysis X/var 3,933 genes、pre-HVG slot 8,000 genes、submitted label 15 種、parent/Blood residual fraction 0.010、median confidence 0.776。
  - 497 cells は low confidence。QC / confidence UMAP 上で局在を確認する。
  - 61 cells は `Doublet` として提出。mixed-lineage marker expression と scrublet support を確認する。
  - 436 cells は `Blood Cell` として残存。これは filter-out ではなく、曖昧な細胞を公式 parent label で残したもの。
  - Marker gene 欠損アラート: Treg, Plasma_ASC。該当 marker set に依存する fine label は慎重に見る。

## データセット固有の評価

- 全体像: 43,767 cells / analysis X/var 3,933 genes / pre-HVG slot 8,000 genes。parent/Blood residual は 0.010、low-confidence は 497 cells、source disagreement flag は 9,576 cells (0.219)。
- 優先確認: low-confidence 領域が QC UMAP と source-disagreement UMAP で同じ場所に集まるかを確認する。
- 優先確認: `Blood Cell` 残存が孤立 cluster なのか、複数 lineage に分散した曖昧領域なのかを UMAP で確認する。
- Marker gene 欠損: Treg, Plasma_ASC は confidence cap 対象。該当 label は marker expression UMAP と dotplot で妥当性を確認する。

## Marker Gene 欠損アラート

| study | marker_set | alert | present_fraction | missing_critical_markers | missing_genes |
| --- | --- | --- | --- | --- | --- |
| infection_study_04 | Treg | critical | 0.286 | FOXP3;IL2RA;CTLA4 | FOXP3;IL2RA;CTLA4;TNFRSF18;CCR8 |
| infection_study_04 | Plasma_ASC | warning | 0.667 | JCHAIN | JCHAIN;SDC1;TNFRSF17 |

## ソース間不一致

| study | predicted_cell_type | cells | median_source_agreement | disagreement_cells | disagreement_fraction |
| --- | --- | --- | --- | --- | --- |
| infection_study_04 | Blood Cell | 436 | 0.000 | 436 | 1.000 |
| infection_study_04 | Neutrophil | 195 | 0.333 | 195 | 1.000 |
| infection_study_04 | Doublet | 61 | 0.000 | 61 | 1.000 |
| infection_study_04 | Memory B Cell | 1,344 | 0.500 | 452 | 0.336 |
| infection_study_04 | CD8 Cytotoxic / T Effector Memory | 7,788 | 0.667 | 2,322 | 0.298 |
| infection_study_04 | CD4 Naive / T Central Memory | 8,829 | 0.750 | 2,420 | 0.274 |
| infection_study_04 | Naive B Cell | 2,126 | 0.750 | 507 | 0.238 |
| infection_study_04 | NK Cell | 6,433 | 1.000 | 1,138 | 0.177 |
| infection_study_04 | Classical Monocyte | 11,458 | 1.000 | 1,755 | 0.153 |
| infection_study_04 | Conventional DC 2 | 338 | 1.000 | 51 | 0.151 |
| infection_study_04 | Non-Classical Monocyte | 1,214 | 1.000 | 158 | 0.130 |
| infection_study_04 | Plasmacytoid DC | 229 | 1.000 | 8 | 0.035 |

## アノテーションソース効果

この表は外部 ground truth に対する正解率ではありません。各 annotation source がどれだけの細胞で情報を持ち、final label とどれだけ一致したかを示す監査用統計です。`coverage` は source が `not_available` 以外を返した割合、`final_concordance` は informative cells の中で final label と一致した割合、`unique_support` はその source だけが final label と一致した細胞数です。

| study | source | informative_cells | coverage | final_concordance | high_conf_concordance | unique_support | discordant |
| --- | --- | --- | --- | --- | --- | --- | --- |
| infection_study_04 | CellTypist | 43,767 | 1.000 | 0.779 | 0.811 | 58 | 9,682 |
| infection_study_04 | Cluster consensus | 43,767 | 1.000 | 0.671 | 0.668 | 1 | 14,404 |
| infection_study_04 | Pan-human Azimuth | 43,767 | 1.000 | 0.656 | 0.704 | 311 | 15,062 |
| infection_study_04 | Cluster marker assignment | 43,098 | 0.985 | 0.969 | 0.961 | 4,183 | 1,327 |
| infection_study_04 | scRefMapping | 14,878 | 0.340 | 0.728 | 0.841 | 38 | 4,042 |

## レビュー優先事項

| study | concern | cells |
| --- | --- | --- |
| infection_study_04 | High source disagreement for Blood Cell | 436 |
| infection_study_04 | High source disagreement for Doublet | 61 |
| infection_study_04 | High source disagreement for Neutrophil | 195 |
| infection_study_04 | High dataset-level source disagreement | 9,576 |
| infection_study_04 | warning marker availability for Plasma_ASC | 3,150 |

## ラベル構成

| study | predicted_cell_type | cells |
| --- | --- | --- |
| infection_study_04 | Classical Monocyte | 11,458 |
| infection_study_04 | CD4 Naive / T Central Memory | 8,829 |
| infection_study_04 | CD8 Cytotoxic / T Effector Memory | 7,788 |
| infection_study_04 | NK Cell | 6,433 |
| infection_study_04 | Plasma Cell | 3,150 |
| infection_study_04 | Naive B Cell | 2,126 |
| infection_study_04 | Memory B Cell | 1,344 |
| infection_study_04 | Non-Classical Monocyte | 1,214 |
| infection_study_04 | Blood Cell | 436 |
| infection_study_04 | Conventional DC 2 | 338 |
| infection_study_04 | Plasmacytoid DC | 229 |
| infection_study_04 | Neutrophil | 195 |
| infection_study_04 | Platelet | 86 |
| infection_study_04 | HSC | 80 |
| infection_study_04 | Doublet | 61 |

## Inline Figures

### infection_study_04

![infection_study_04 final labels](assets/umap_infection_study_04_annotation_label.png)

![infection_study_04 lineage and annotation reason](assets/umap_infection_study_04_annotation_lineage_reason.png)

![infection_study_04 QC and confidence](assets/umap_infection_study_04_annotation_qc_confidence.png)

![infection_study_04 source agreement and disagreement](assets/umap_infection_study_04_annotation_source_disagreement.png)

![infection_study_04 annotation-source effectiveness](assets/figure_02_source_effectiveness.png)

![infection_study_04 marker expression UMAPs](assets/umap_infection_study_04_annotation_marker_expression.png)

![infection_study_04 submitted-label marker dotplot](assets/dotplot_infection_study_04_annotation_marker_dotplot.png)

#### infection_study_04 B_lineage true subcluster UMAP

![infection_study_04 B_lineage true subcluster labels](assets/umap_infection_study_04_B_lineage_true_subcluster_label.png)

![infection_study_04 B_lineage true subcluster source labels](assets/umap_infection_study_04_B_lineage_true_subcluster_source_labels.png)

![infection_study_04 B_lineage true subcluster QC](assets/umap_infection_study_04_B_lineage_true_subcluster_qc.png)

![infection_study_04 B_lineage true subcluster marker scores](assets/umap_infection_study_04_B_lineage_true_subcluster_marker_scores.png)

![infection_study_04 B_lineage true subcluster marker expression](assets/umap_infection_study_04_B_lineage_true_subcluster_marker_expression.png)

![infection_study_04 B_lineage subcluster marker score heatmap](assets/subcluster_marker_score_heatmap_infection_study_04_B_lineage.png)

![infection_study_04 B_lineage subcluster marker dotplot](assets/dotplot_infection_study_04_B_lineage_true_subcluster_marker_dotplot.png)

Tables: `tables/infection_study_04_B_lineage_true_subcluster_umap.tsv.gz`, `tables/infection_study_04_B_lineage_subcluster_candidate_scores.tsv`.

#### infection_study_04 T_NK_lineage true subcluster UMAP

![infection_study_04 T_NK_lineage true subcluster labels](assets/umap_infection_study_04_T_NK_lineage_true_subcluster_label.png)

![infection_study_04 T_NK_lineage true subcluster source labels](assets/umap_infection_study_04_T_NK_lineage_true_subcluster_source_labels.png)

![infection_study_04 T_NK_lineage true subcluster QC](assets/umap_infection_study_04_T_NK_lineage_true_subcluster_qc.png)

![infection_study_04 T_NK_lineage true subcluster marker scores](assets/umap_infection_study_04_T_NK_lineage_true_subcluster_marker_scores.png)

![infection_study_04 T_NK_lineage true subcluster marker expression](assets/umap_infection_study_04_T_NK_lineage_true_subcluster_marker_expression.png)

![infection_study_04 T_NK_lineage subcluster marker score heatmap](assets/subcluster_marker_score_heatmap_infection_study_04_T_NK_lineage.png)

![infection_study_04 T_NK_lineage subcluster marker dotplot](assets/dotplot_infection_study_04_T_NK_lineage_true_subcluster_marker_dotplot.png)

Tables: `tables/infection_study_04_T_NK_lineage_true_subcluster_umap.tsv.gz`, `tables/infection_study_04_T_NK_lineage_subcluster_candidate_scores.tsv`.

#### infection_study_04 Myeloid_lineage true subcluster UMAP

![infection_study_04 Myeloid_lineage true subcluster labels](assets/umap_infection_study_04_Myeloid_lineage_true_subcluster_label.png)

![infection_study_04 Myeloid_lineage true subcluster source labels](assets/umap_infection_study_04_Myeloid_lineage_true_subcluster_source_labels.png)

![infection_study_04 Myeloid_lineage true subcluster QC](assets/umap_infection_study_04_Myeloid_lineage_true_subcluster_qc.png)

![infection_study_04 Myeloid_lineage true subcluster marker scores](assets/umap_infection_study_04_Myeloid_lineage_true_subcluster_marker_scores.png)

![infection_study_04 Myeloid_lineage true subcluster marker expression](assets/umap_infection_study_04_Myeloid_lineage_true_subcluster_marker_expression.png)

![infection_study_04 Myeloid_lineage subcluster marker score heatmap](assets/subcluster_marker_score_heatmap_infection_study_04_Myeloid_lineage.png)

![infection_study_04 Myeloid_lineage subcluster marker dotplot](assets/dotplot_infection_study_04_Myeloid_lineage_true_subcluster_marker_dotplot.png)

Tables: `tables/infection_study_04_Myeloid_lineage_true_subcluster_umap.tsv.gz`, `tables/infection_study_04_Myeloid_lineage_subcluster_candidate_scores.tsv`.


## Subcluster Marker Score Review

上の lineage-specific panel は、各 lineage subset で HVG 選択、PCA、neighbors、Leiden、UMAP を再計算した true local subcluster analysis から生成しています。Marker gene による fine label の確認は global UMAP だけではなく、この local UMAP、CellTypist/Azimuth/Pan-human/cluster-level marker gene assignment overlay、cluster marker gate score UMAP、marker-expression UMAP、dotplot を主に見ます。Treg など sparse marker label は cell-wise marker winner ではなく、local cluster の FOXP3/IL2RA/CTLA4 など key-marker support と reference support で判定します。

## Marker Assignment Feedback

Marker gene assignment は final label を強制的に上書きするものではなく、cluster-level の自己点検です。`raw_marker_winner` は marker score だけの勝者、`marker_assignment` は conservative policy と source-supported tie-break を通した marker-based assignment です。この表は marker assignment と final/reference-driven label がずれる cluster、marker specificity が弱い cluster、scRefMap が期待される lineage で欠落する cluster を示します。`marker_score` は raw marker base score から negative/confound marker penalty を差し引いた cluster-level marker gate score です。

| study | lineage | cluster | cells | chosen_label | marker_assignment | raw_marker_winner | assignment_reason | marker_score | base_score | penalty | flags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| infection_study_04 | T_NK_lineage | 0 | 1,706 | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | raw_marker_winner | 0.729 | 1.000 | 0.271 | screfmapping_missing_for_scope |
| infection_study_04 | T_NK_lineage | 1 | 1,554 | NK Cell | NK Cell | NK Cell | raw_marker_winner | 0.828 | 1.000 | 0.172 | screfmapping_missing_for_scope |
| infection_study_04 | T_NK_lineage | 2 | 1,496 | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | NKT Cell | conservative_policy_blocks_raw_marker_winner | 0.666 | 0.946 | 0.280 | screfmapping_missing_for_scope |
| infection_study_04 | T_NK_lineage | 4 | 1,144 | NK Cell | NK Cell | NK Cell | raw_marker_winner | 0.884 | 1.000 | 0.116 | screfmapping_missing_for_scope |
| infection_study_04 | T_NK_lineage | 5 | 1,138 | NK Cell | NK Cell | NK Cell | raw_marker_winner | 0.715 | 1.000 | 0.285 | screfmapping_missing_for_scope |
| infection_study_04 | T_NK_lineage | 11 | 1,064 | NK Cell | NK Cell | NKT Cell | conservative_policy_blocks_raw_marker_winner | 0.650 | 0.790 | 0.140 | screfmapping_missing_for_scope |
| infection_study_04 | T_NK_lineage | 12 | 1,033 | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | raw_marker_winner | 0.643 | 1.000 | 0.357 | screfmapping_missing_for_scope |
| infection_study_04 | T_NK_lineage | 13 | 943 | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | NKT Cell | conservative_policy_blocks_raw_marker_winner | 0.707 | 0.987 | 0.280 | screfmapping_missing_for_scope |
| infection_study_04 | T_NK_lineage | 16 | 816 | NK Cell | NK Cell | NKT Cell | conservative_policy_blocks_raw_marker_winner | 0.845 | 0.950 | 0.105 | screfmapping_missing_for_scope |
| infection_study_04 | B_lineage | 1 | 572 | Memory B Cell | Naive B Cell | Naive B Cell | raw_marker_winner | 0.369 | 0.726 | 0.357 | marker_final_disagreement |
| infection_study_04 | T_NK_lineage | 18 | 521 | NK Cell | NK Cell | NK Cell | raw_marker_winner | 0.803 | 1.000 | 0.197 | screfmapping_missing_for_scope |
| infection_study_04 | T_NK_lineage | 20 | 493 | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | raw_marker_winner | 0.645 | 1.000 | 0.355 | screfmapping_missing_for_scope |
| infection_study_04 | B_lineage | 7 | 417 | Memory B Cell | Naive B Cell | Naive B Cell | raw_marker_winner | 0.472 | 0.688 | 0.216 | marker_final_disagreement |
| infection_study_04 | Myeloid_lineage | 16 | 338 | Conventional DC 2 | Intermediate Monocyte | Intermediate Monocyte | raw_marker_winner | 0.771 | 1.000 | 0.229 | marker_final_disagreement |
| infection_study_04 | B_lineage | 14 | 198 | Naive B Cell | Naive B Cell | Naive B Cell | raw_marker_winner | 0.329 | 0.724 | 0.395 | weak_marker_specificity |
| infection_study_04 | T_NK_lineage | 24 | 195 | NK Cell | NK Cell | CD8 Cytotoxic / T Effector Memory | source_supported_marker_tiebreak | 0.400 | 1.000 | 0.600 | screfmapping_missing_for_scope |
| infection_study_04 | T_NK_lineage | 25 | 163 | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | NKT Cell | conservative_policy_blocks_raw_marker_winner | 0.370 | 0.613 | 0.243 | screfmapping_missing_for_scope |
| infection_study_04 | B_lineage | 17 | 44 | Naive B Cell | Naive B Cell | Naive B Cell | raw_marker_winner | 0.294 | 0.591 | 0.297 | weak_marker_specificity |

## LLM Review Queue

この表は Codex/LLM が読むための subcluster-level review queue です。LLM はこの evidence を読んで、final label が妥当か、ontology にちょうどよい label がないのか、registry / conservative policy を一般ルールとして更新すべきかを提案します。LLM の出力で per-cell label を直接書き換えず、採用する場合は registry/config を更新して deterministic pipeline を再実行します。

| study | lineage | cluster | cells | priority | reasons | suggested_action | final_label | marker_assignment | raw_marker_winner | score_margin |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| infection_study_04 | T_NK_lineage | 2 | 1,496 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | NKT Cell | 2.380 |
| infection_study_04 | T_NK_lineage | 11 | 1,064 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | NK Cell | NK Cell | NKT Cell | 0.201 |
| infection_study_04 | T_NK_lineage | 13 | 943 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | NKT Cell | 0.588 |
| infection_study_04 | T_NK_lineage | 16 | 816 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | NK Cell | NK Cell | NKT Cell | 2.486 |
| infection_study_04 | Myeloid_lineage | 16 | 338 | medium | marker_assignment_disagrees_with_final;screfmapping_not_available | review_marker_vs_reference_disagreement | Conventional DC 2 | Intermediate Monocyte | Intermediate Monocyte | 1.847 |
| infection_study_04 | T_NK_lineage | 25 | 163 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | NKT Cell | 2.132 |
| infection_study_04 | T_NK_lineage | 0 | 1,706 | low | screfmapping_not_available | accept | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | 2.335 |
| infection_study_04 | T_NK_lineage | 1 | 1,554 | low | screfmapping_not_available | accept | NK Cell | NK Cell | NK Cell | 1.915 |
| infection_study_04 | T_NK_lineage | 4 | 1,144 | low | screfmapping_not_available | accept | NK Cell | NK Cell | NK Cell | 2.765 |
| infection_study_04 | T_NK_lineage | 5 | 1,138 | low | screfmapping_not_available | accept | NK Cell | NK Cell | NK Cell | 1.693 |
| infection_study_04 | T_NK_lineage | 12 | 1,033 | low | screfmapping_not_available | accept | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | 1.791 |
| infection_study_04 | B_lineage | 1 | 572 | low | marker_assignment_disagrees_with_final | review_marker_vs_reference_disagreement | Memory B Cell | Naive B Cell | Naive B Cell | 1.815 |
| infection_study_04 | B_lineage | 7 | 417 | low | marker_assignment_disagrees_with_final | review_marker_vs_reference_disagreement | Memory B Cell | Naive B Cell | Naive B Cell | 0.283 |
| infection_study_04 | T_NK_lineage | 18 | 521 | low | screfmapping_not_available | accept | NK Cell | NK Cell | NK Cell | 2.577 |
| infection_study_04 | T_NK_lineage | 20 | 493 | low | screfmapping_not_available | accept | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | 2.111 |
| infection_study_04 | T_NK_lineage | 24 | 195 | low | raw_marker_winner_changed_by_policy;screfmapping_not_available | accept | NK Cell | NK Cell | CD8 Cytotoxic / T Effector Memory | 0.885 |
| infection_study_04 | B_lineage | 14 | 198 | low | screfmapping_not_available | accept | Naive B Cell | Naive B Cell | Naive B Cell | 0.750 |
| infection_study_04 | B_lineage | 17 | 44 | low | spot_check | accept | Naive B Cell | Naive B Cell | Naive B Cell | 0.280 |

## Cluster Consensus Evidence

| study | lineage | cluster | cells | chosen_label | accepted | score_margin | cluster_marker_assignment | treg_key_any | treg_key_bonus | marker_set | marker_alert |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| infection_study_04 | B_lineage | 0 | 634 | Naive B Cell | True | 4.299 | Naive B Cell | nan | nan | registry__naive_b_cell | pass |
| infection_study_04 | B_lineage | 1 | 572 | Memory B Cell | True | 1.815 | Naive B Cell | nan | nan | registry__memory_b_cell | pass |
| infection_study_04 | B_lineage | 2 | 499 | Plasma Cell | True | 1.397 | Plasma Cell | nan | nan | registry__plasma_cell | pass |
| infection_study_04 | B_lineage | 3 | 496 | Plasma Cell | True | 2.255 | Plasma Cell | nan | nan | registry__plasma_cell | pass |
| infection_study_04 | B_lineage | 4 | 487 | Plasma Cell | True | 3.286 | Plasma Cell | nan | nan | registry__plasma_cell | pass |
| infection_study_04 | B_lineage | 5 | 456 | Plasma Cell | True | 3.353 | Plasma Cell | nan | nan | registry__plasma_cell | pass |
| infection_study_04 | B_lineage | 6 | 436 | Naive B Cell | True | 4.296 | Naive B Cell | nan | nan | registry__naive_b_cell | pass |
| infection_study_04 | B_lineage | 7 | 417 | Memory B Cell | True | 0.283 | Naive B Cell | nan | nan | registry__memory_b_cell | pass |
| infection_study_04 | B_lineage | 8 | 411 | Plasma Cell | True | 0.969 | Plasma Cell | nan | nan | registry__plasma_cell | pass |
| infection_study_04 | B_lineage | 9 | 394 | Naive B Cell | True | 2.259 | Naive B Cell | nan | nan | registry__naive_b_cell | pass |
| infection_study_04 | B_lineage | 10 | 355 | Memory B Cell | True | 2.369 | Memory B Cell | nan | nan | registry__memory_b_cell | pass |
| infection_study_04 | B_lineage | 11 | 334 | Plasma Cell | True | 2.610 | Plasma Cell | nan | nan | registry__plasma_cell | pass |
| infection_study_04 | B_lineage | 12 | 317 | Plasma Cell | True | 3.196 | Plasma Cell | nan | nan | registry__plasma_cell | pass |
| infection_study_04 | B_lineage | 13 | 288 | Naive B Cell | True | 2.688 | Naive B Cell | nan | nan | registry__naive_b_cell | pass |
| infection_study_04 | B_lineage | 14 | 198 | Naive B Cell | True | 0.750 | Naive B Cell | nan | nan | registry__naive_b_cell | pass |
| infection_study_04 | B_lineage | 15 | 147 | Plasma Cell | True | 2.509 | Plasma Cell | nan | nan | registry__plasma_cell | pass |
| infection_study_04 | B_lineage | 16 | 132 | Naive B Cell | True | 1.625 | Naive B Cell | nan | nan | registry__naive_b_cell | pass |
| infection_study_04 | B_lineage | 17 | 44 | Naive B Cell | True | 0.280 | Naive B Cell | nan | nan | registry__naive_b_cell | pass |
| infection_study_04 | Myeloid_lineage | 0 | 1,257 | Classical Monocyte | True | 2.459 | Classical Monocyte | nan | nan | registry__classical_monocyte | pass |
| infection_study_04 | Myeloid_lineage | 1 | 1,209 | Classical Monocyte | True | 2.606 | Classical Monocyte | nan | nan | registry__classical_monocyte | pass |
| infection_study_04 | Myeloid_lineage | 2 | 1,060 | Classical Monocyte | True | 2.491 | Classical Monocyte | nan | nan | registry__classical_monocyte | pass |
| infection_study_04 | Myeloid_lineage | 3 | 874 | Classical Monocyte | True | 1.904 | Classical Monocyte | nan | nan | registry__classical_monocyte | pass |
| infection_study_04 | Myeloid_lineage | 4 | 860 | Classical Monocyte | True | 2.359 | Classical Monocyte | nan | nan | registry__classical_monocyte | pass |
| infection_study_04 | Myeloid_lineage | 5 | 812 | Classical Monocyte | True | 2.375 | Classical Monocyte | nan | nan | registry__classical_monocyte | pass |
| infection_study_04 | Myeloid_lineage | 6 | 764 | Classical Monocyte | True | 2.210 | Classical Monocyte | nan | nan | registry__classical_monocyte | pass |
| infection_study_04 | Myeloid_lineage | 7 | 682 | Classical Monocyte | True | 2.062 | Classical Monocyte | nan | nan | registry__classical_monocyte | pass |
| infection_study_04 | Myeloid_lineage | 8 | 680 | Non-Classical Monocyte | True | 2.041 | Non-Classical Monocyte | nan | nan | registry__non_classical_monocyte | pass |
| infection_study_04 | Myeloid_lineage | 9 | 670 | Classical Monocyte | True | 2.630 | Classical Monocyte | nan | nan | registry__classical_monocyte | pass |
| infection_study_04 | Myeloid_lineage | 10 | 628 | Classical Monocyte | True | 2.287 | Classical Monocyte | nan | nan | registry__classical_monocyte | pass |
| infection_study_04 | Myeloid_lineage | 11 | 548 | Classical Monocyte | True | 2.139 | Classical Monocyte | nan | nan | registry__classical_monocyte | pass |

## 出力ファイル

- Submission TSVs: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_final_v22/infection_study_04/submissions/`
- cellxgene H5ADs: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_final_v22/infection_study_04/cellxgene/`
- Marker availability table: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_final_v22/infection_study_04/tables/marker_gene_availability.tsv`
- Marker availability alerts: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_final_v22/infection_study_04/tables/marker_gene_availability_alerts.tsv`
- Subcluster evidence: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_final_v22/infection_study_04/tables/lineage_subcluster_evidence.tsv.gz`
- Source disagreement summary: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_final_v22/infection_study_04/tables/source_disagreement_summary.tsv`
- Source effectiveness summary: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_final_v22/infection_study_04/tables/source_effectiveness_summary.tsv`
- Diagnostics tables: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_final_v22/infection_study_04/tables/`

