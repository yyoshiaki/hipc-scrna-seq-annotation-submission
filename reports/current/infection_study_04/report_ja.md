# HIPC データセットアノテーションレポート: infection_study_04

更新日: 2026-06-05 EDT

このレポートは `hipc-annotation` Codex workflow によって生成したデータセット別レビュー文書です。固定 method は repository README に置き、このレポートでは実際の evidence、弱い箇所、レビュー優先度、UMAP / dotplot を確認します。

## データセット概要

| study | cells | analysis_X_genes | pre_hvg_genes | counts_layer_genes | labels | parent_or_blood_fraction | Blood Cell | Doublet | artifact_like | median_confidence | low_confidence | source_disagreement | invalid_labels |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| infection_study_04 | 43,767 | 26,361 | 26,361 | 26,361 | 17 | 0.038 | 1,660 | 132 | 324 | 0.740 | 5,261 | 8,229 (0.188) | none |

## 実行概要

- 実行単位: one dataset in, one annotated dataset out。
- 実行経路: Codex skill `hipc-annotation` -> bundled helper `run_one.sh` -> annotation CLI -> validator -> report inspection。
- 検証: submission row count、H5AD observation count、official label validity、H5AD/submission agreement、confidence column、report image link を確認する。
- このレポートは workflow の再掲ではなく、このデータセットの marker 欠損、UMAP、label 構成、review concern を読むためのもの。

## データセット固有の解釈

- `infection_study_04`: 43,767 cells、analysis X/var 26,361 genes、pre-HVG slot 26,361 genes、submitted label 17 種、parent/Blood residual fraction 0.038、median confidence 0.740。
  - 5,261 cells は low confidence。QC / confidence UMAP 上で局在を確認する。
  - 132 cells は `Doublet` として提出。mixed-lineage marker expression と scrublet support を確認する。
  - 1,660 cells は `Blood Cell` として残存。これは filter-out ではなく、曖昧な細胞を公式 parent label で残したもの。
  - Marker gene 欠損アラート: Plasma_ASC。該当 marker set に依存する fine label は慎重に見る。

## データセット固有の評価

- 全体像: 43,767 cells / analysis X/var 26,361 genes / pre-HVG slot 26,361 genes。parent/Blood residual は 0.038、low-confidence は 5,261 cells、source disagreement flag は 8,229 cells (0.188)。
- 優先確認: low-confidence 領域が QC UMAP と source-disagreement UMAP で同じ場所に集まるかを確認する。
- 優先確認: `Blood Cell` 残存が孤立 cluster なのか、複数 lineage に分散した曖昧領域なのかを UMAP で確認する。
- Marker gene 欠損: Plasma_ASC は confidence cap 対象。該当 label は marker expression UMAP と dotplot で妥当性を確認する。

## Marker Gene 欠損アラート

| study | marker_set | alert | present_fraction | missing_critical_markers | missing_genes |
| --- | --- | --- | --- | --- | --- |
| infection_study_04 | Plasma_ASC | warning | 0.889 | JCHAIN | JCHAIN |

## ソース間不一致

| study | predicted_cell_type | cells | median_source_agreement | disagreement_cells | disagreement_fraction |
| --- | --- | --- | --- | --- | --- |
| infection_study_04 | Doublet | 132 | 0.000 | 132 | 1.000 |
| infection_study_04 | Neutrophil | 78 | 0.333 | 78 | 1.000 |
| infection_study_04 | MAIT Cell | 716 | 0.333 | 481 | 0.672 |
| infection_study_04 | Blood Cell | 1,660 | 0.333 | 898 | 0.541 |
| infection_study_04 | Memory B Cell | 1,594 | 0.500 | 626 | 0.393 |
| infection_study_04 | CD8 Cytotoxic / T Effector Memory | 6,582 | 0.667 | 1,874 | 0.285 |
| infection_study_04 | NK Cell | 7,441 | 1.000 | 1,757 | 0.236 |
| infection_study_04 | Conventional DC 2 | 433 | 0.667 | 93 | 0.215 |
| infection_study_04 | Naive B Cell | 1,374 | 0.750 | 191 | 0.139 |
| infection_study_04 | Treg | 461 | 0.750 | 58 | 0.126 |
| infection_study_04 | Non-Classical Monocyte | 1,474 | 1.000 | 142 | 0.096 |
| infection_study_04 | Plasma Cell | 3,369 | 0.750 | 320 | 0.095 |

## レビュー優先事項

| study | concern | cells |
| --- | --- | --- |
| infection_study_04 | High source disagreement for Blood Cell | 898 |
| infection_study_04 | High source disagreement for Doublet | 132 |
| infection_study_04 | High source disagreement for MAIT Cell | 481 |
| infection_study_04 | High source disagreement for Neutrophil | 78 |
| infection_study_04 | warning marker availability for Plasma_ASC | 3,369 |
| infection_study_04 | Large Blood Cell/ambiguous residual remains | 1,660 |

## ラベル構成

| study | predicted_cell_type | cells |
| --- | --- | --- |
| infection_study_04 | Classical Monocyte | 10,273 |
| infection_study_04 | CD4 Naive / T Central Memory | 7,630 |
| infection_study_04 | NK Cell | 7,441 |
| infection_study_04 | CD8 Cytotoxic / T Effector Memory | 6,582 |
| infection_study_04 | Plasma Cell | 3,369 |
| infection_study_04 | Blood Cell | 1,660 |
| infection_study_04 | Memory B Cell | 1,594 |
| infection_study_04 | Non-Classical Monocyte | 1,474 |
| infection_study_04 | Naive B Cell | 1,374 |
| infection_study_04 | MAIT Cell | 716 |
| infection_study_04 | Treg | 461 |
| infection_study_04 | Conventional DC 2 | 433 |
| infection_study_04 | Plasmacytoid DC | 226 |
| infection_study_04 | Platelet | 200 |
| infection_study_04 | Doublet | 132 |
| infection_study_04 | HSC | 124 |
| infection_study_04 | Neutrophil | 78 |

## Inline Figures

### infection_study_04

![infection_study_04 final labels](assets/umap_infection_study_04_annotation_label.png)

![infection_study_04 lineage and annotation reason](assets/umap_infection_study_04_annotation_lineage_reason.png)

![infection_study_04 QC and confidence](assets/umap_infection_study_04_annotation_qc_confidence.png)

![infection_study_04 source agreement and disagreement](assets/umap_infection_study_04_annotation_source_disagreement.png)

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
| infection_study_04 | T_NK_lineage | 0 | 1,687 | NK Cell | NK Cell | NK Cell | raw_marker_winner | 0.892 | 1.000 | 0.108 | screfmapping_missing_for_scope |
| infection_study_04 | T_NK_lineage | 1 | 1,421 | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | NKT Cell | conservative_policy_blocks_raw_marker_winner | 0.648 | 1.000 | 0.352 | screfmapping_missing_for_scope |
| infection_study_04 | T_NK_lineage | 4 | 1,203 | NK Cell | NK Cell | NK Cell | raw_marker_winner | 0.768 | 1.000 | 0.232 | screfmapping_missing_for_scope |
| infection_study_04 | T_NK_lineage | 5 | 1,042 | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | NKT Cell | conservative_policy_blocks_raw_marker_winner | 0.689 | 0.817 | 0.128 | screfmapping_missing_for_scope |
| infection_study_04 | T_NK_lineage | 6 | 1,007 | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | raw_marker_winner | 0.646 | 1.000 | 0.354 | screfmapping_missing_for_scope |
| infection_study_04 | T_NK_lineage | 7 | 937 | NK Cell | NK Cell | NK Cell | raw_marker_winner | 0.865 | 1.000 | 0.135 | screfmapping_missing_for_scope |
| infection_study_04 | T_NK_lineage | 10 | 902 | NK Cell | NK Cell | NKT Cell | conservative_policy_blocks_raw_marker_winner | 0.765 | 0.841 | 0.076 | screfmapping_missing_for_scope |
| infection_study_04 | T_NK_lineage | 11 | 891 | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | raw_marker_winner | 0.723 | 0.987 | 0.264 | screfmapping_missing_for_scope |
| infection_study_04 | T_NK_lineage | 12 | 800 | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | CD8 Naive / T Central Memory | source_supported_marker_tiebreak | 0.625 | 0.963 | 0.338 | screfmapping_missing_for_scope |
| infection_study_04 | T_NK_lineage | 13 | 795 | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | NKT Cell | conservative_policy_blocks_raw_marker_winner | 0.686 | 0.902 | 0.216 | screfmapping_missing_for_scope |
| infection_study_04 | T_NK_lineage | 14 | 762 | NK Cell | NK Cell | NKT Cell | conservative_policy_blocks_raw_marker_winner | 0.686 | 0.828 | 0.142 | screfmapping_missing_for_scope |
| infection_study_04 | T_NK_lineage | 15 | 754 | NK Cell | NK Cell | NKT Cell | conservative_policy_blocks_raw_marker_winner | 0.666 | 0.841 | 0.175 | screfmapping_missing_for_scope |
| infection_study_04 | T_NK_lineage | 16 | 713 | CD4 Naive / T Central Memory | CD8 Naive / T Central Memory | CD8 Naive / T Central Memory | raw_marker_winner | 0.949 | 1.000 | 0.051 | marker_final_disagreement |
| infection_study_04 | T_NK_lineage | 19 | 511 | NK Cell | NK Cell | NK Cell | raw_marker_winner | 0.842 | 1.000 | 0.158 | screfmapping_missing_for_scope |
| infection_study_04 | B_lineage | 4 | 443 | Memory B Cell | Naive B Cell | Naive B Cell | raw_marker_winner | 0.482 | 0.693 | 0.211 | marker_final_disagreement |
| infection_study_04 | T_NK_lineage | 22 | 413 | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | raw_marker_winner | 0.722 | 1.000 | 0.278 | screfmapping_missing_for_scope |
| infection_study_04 | B_lineage | 6 | 404 | Memory B Cell | Memory B Cell | Memory B Cell | raw_marker_winner | 0.245 | 0.478 | 0.233 | weak_marker_specificity |
| infection_study_04 | T_NK_lineage | 23 | 388 | NK Cell | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | raw_marker_winner | 0.381 | 0.730 | 0.349 | marker_final_disagreement;screfmapping_missing_for_scope |
| infection_study_04 | B_lineage | 9 | 344 | Memory B Cell | Naive B Cell | Naive B Cell | raw_marker_winner | 0.606 | 0.860 | 0.255 | marker_final_disagreement |
| infection_study_04 | T_NK_lineage | 27 | 231 | MAIT Cell | MAIT Cell | NKT Cell | conservative_policy_blocks_raw_marker_winner | 0.854 | 0.927 | 0.074 | screfmapping_missing_for_scope |

## LLM Review Queue

この表は Codex/LLM が読むための subcluster-level review queue です。LLM はこの evidence を読んで、final label が妥当か、ontology にちょうどよい label がないのか、registry / conservative policy を一般ルールとして更新すべきかを提案します。LLM の出力で per-cell label を直接書き換えず、採用する場合は registry/config を更新して deterministic pipeline を再実行します。

| study | lineage | cluster | cells | priority | reasons | suggested_action | final_label | marker_assignment | raw_marker_winner | score_margin |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| infection_study_04 | T_NK_lineage | 5 | 1,042 | high | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available;low_total_score_or_margin | evaluate_ontology_gap_or_conservative_policy | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | NKT Cell | 0.086 |
| infection_study_04 | T_NK_lineage | 1 | 1,421 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | NKT Cell | 1.531 |
| infection_study_04 | T_NK_lineage | 10 | 902 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | NK Cell | NK Cell | NKT Cell | 2.218 |
| infection_study_04 | T_NK_lineage | 13 | 795 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | NKT Cell | 0.579 |
| infection_study_04 | T_NK_lineage | 14 | 762 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | NK Cell | NK Cell | NKT Cell | 1.666 |
| infection_study_04 | T_NK_lineage | 15 | 754 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | NK Cell | NK Cell | NKT Cell | 1.302 |
| infection_study_04 | T_NK_lineage | 16 | 713 | medium | marker_assignment_disagrees_with_final;screfmapping_not_available | review_marker_vs_reference_disagreement | CD4 Naive / T Central Memory | CD8 Naive / T Central Memory | CD8 Naive / T Central Memory | 0.865 |
| infection_study_04 | T_NK_lineage | 23 | 388 | medium | marker_assignment_disagrees_with_final;screfmapping_not_available | review_marker_vs_reference_disagreement | NK Cell | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | 0.186 |
| infection_study_04 | T_NK_lineage | 27 | 231 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | MAIT Cell | MAIT Cell | NKT Cell | 0.456 |
| infection_study_04 | T_NK_lineage | 30 | 213 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | NKT Cell | 0.633 |
| infection_study_04 | T_NK_lineage | 0 | 1,687 | low | screfmapping_not_available | accept | NK Cell | NK Cell | NK Cell | 2.794 |
| infection_study_04 | T_NK_lineage | 4 | 1,203 | low | screfmapping_not_available | accept | NK Cell | NK Cell | NK Cell | 1.846 |
| infection_study_04 | T_NK_lineage | 6 | 1,007 | low | screfmapping_not_available | accept | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | 1.579 |
| infection_study_04 | T_NK_lineage | 12 | 800 | low | raw_marker_winner_changed_by_policy;screfmapping_not_available | accept | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | CD8 Naive / T Central Memory | 1.370 |
| infection_study_04 | B_lineage | 4 | 443 | low | marker_assignment_disagrees_with_final | review_marker_vs_reference_disagreement | Memory B Cell | Naive B Cell | Naive B Cell | 0.510 |
| infection_study_04 | B_lineage | 9 | 344 | low | marker_assignment_disagrees_with_final | review_marker_vs_reference_disagreement | Memory B Cell | Naive B Cell | Naive B Cell | 0.758 |
| infection_study_04 | Myeloid_lineage | 25 | 78 | low | marker_assignment_disagrees_with_final;screfmapping_not_available | review_marker_vs_reference_disagreement | Neutrophil | Classical Monocyte | Classical Monocyte | 0.578 |
| infection_study_04 | T_NK_lineage | 7 | 937 | low | screfmapping_not_available | accept | NK Cell | NK Cell | NK Cell | 2.656 |
| infection_study_04 | T_NK_lineage | 11 | 891 | low | screfmapping_not_available | accept | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | 1.431 |
| infection_study_04 | T_NK_lineage | 19 | 511 | low | screfmapping_not_available | accept | NK Cell | NK Cell | NK Cell | 2.728 |

## Cluster Consensus Evidence

| study | lineage | cluster | cells | chosen_label | accepted | score_margin | cluster_marker_assignment | treg_key_any | treg_key_bonus | marker_set | marker_alert |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| infection_study_04 | B_lineage | 0 | 681 | Naive B Cell | True | 4.476 | Naive B Cell | nan | nan | registry__naive_b_cell | pass |
| infection_study_04 | B_lineage | 1 | 574 | Plasma Cell | True | 2.389 | Plasma Cell | nan | nan | registry__plasma_cell | pass |
| infection_study_04 | B_lineage | 2 | 469 | Naive B Cell | True | 4.341 | Naive B Cell | nan | nan | registry__naive_b_cell | pass |
| infection_study_04 | B_lineage | 3 | 446 | Plasma Cell | True | 3.458 | Plasma Cell | nan | nan | registry__plasma_cell | pass |
| infection_study_04 | B_lineage | 4 | 443 | Memory B Cell | True | 0.510 | Naive B Cell | nan | nan | registry__memory_b_cell | pass |
| infection_study_04 | B_lineage | 5 | 439 | Plasma Cell | True | 3.480 | Plasma Cell | nan | nan | registry__plasma_cell | pass |
| infection_study_04 | B_lineage | 6 | 404 | Memory B Cell | True | 2.985 | Memory B Cell | nan | nan | registry__memory_b_cell | pass |
| infection_study_04 | B_lineage | 7 | 403 | Memory B Cell | True | 2.372 | Memory B Cell | nan | nan | registry__memory_b_cell | pass |
| infection_study_04 | B_lineage | 8 | 360 | Plasma Cell | True | 2.998 | Plasma Cell | nan | nan | registry__plasma_cell | pass |
| infection_study_04 | B_lineage | 9 | 344 | Memory B Cell | True | 0.758 | Naive B Cell | nan | nan | registry__memory_b_cell | pass |
| infection_study_04 | B_lineage | 10 | 341 | Plasma Cell | True | 0.334 | Plasma Cell | nan | nan | registry__plasma_cell | pass |
| infection_study_04 | B_lineage | 11 | 268 | Plasma Cell | True | 2.158 | Plasma Cell | nan | nan | registry__plasma_cell | pass |
| infection_study_04 | B_lineage | 12 | 266 | Plasma Cell | True | 1.421 | Plasma Cell | nan | nan | registry__plasma_cell | pass |
| infection_study_04 | B_lineage | 13 | 251 | Plasma Cell | True | 1.299 | Plasma Cell | nan | nan | registry__plasma_cell | pass |
| infection_study_04 | B_lineage | 14 | 224 | Naive B Cell | True | 1.443 | Naive B Cell | nan | nan | registry__naive_b_cell | pass |
| infection_study_04 | B_lineage | 15 | 194 | Plasma Cell | True | 2.431 | Plasma Cell | nan | nan | registry__plasma_cell | pass |
| infection_study_04 | B_lineage | 16 | 102 | Plasma Cell | True | 1.943 | Plasma Cell | nan | nan | registry__plasma_cell | pass |
| infection_study_04 | B_lineage | 17 | 81 | Plasma Cell | True | 2.338 | Plasma Cell | nan | nan | registry__plasma_cell | pass |
| infection_study_04 | B_lineage | 18 | 47 | Plasma Cell | True | 0.699 | Plasma Cell | nan | nan | registry__plasma_cell | pass |
| infection_study_04 | Myeloid_lineage | 0 | 1,341 | Classical Monocyte | True | 2.334 | Classical Monocyte | nan | nan | registry__classical_monocyte | pass |
| infection_study_04 | Myeloid_lineage | 1 | 900 | Classical Monocyte | True | 2.674 | Classical Monocyte | nan | nan | registry__classical_monocyte | pass |
| infection_study_04 | Myeloid_lineage | 2 | 836 | Classical Monocyte | True | 2.382 | Classical Monocyte | nan | nan | registry__classical_monocyte | pass |
| infection_study_04 | Myeloid_lineage | 3 | 831 | Classical Monocyte | True | 2.467 | Classical Monocyte | nan | nan | registry__classical_monocyte | pass |
| infection_study_04 | Myeloid_lineage | 4 | 767 | Classical Monocyte | True | 2.581 | Classical Monocyte | nan | nan | registry__classical_monocyte | pass |
| infection_study_04 | Myeloid_lineage | 5 | 738 | Non-Classical Monocyte | True | 2.201 | Non-Classical Monocyte | nan | nan | registry__non_classical_monocyte | pass |
| infection_study_04 | Myeloid_lineage | 6 | 659 | Classical Monocyte | True | 2.683 | Classical Monocyte | nan | nan | registry__classical_monocyte | pass |
| infection_study_04 | Myeloid_lineage | 7 | 625 | Classical Monocyte | True | 2.282 | Classical Monocyte | nan | nan | registry__classical_monocyte | pass |
| infection_study_04 | Myeloid_lineage | 8 | 598 | Classical Monocyte | True | 2.211 | Classical Monocyte | nan | nan | registry__classical_monocyte | pass |
| infection_study_04 | Myeloid_lineage | 9 | 572 | Classical Monocyte | True | 2.558 | Classical Monocyte | nan | nan | registry__classical_monocyte | pass |
| infection_study_04 | Myeloid_lineage | 10 | 558 | Classical Monocyte | True | 2.609 | Classical Monocyte | nan | nan | registry__classical_monocyte | pass |

## 出力ファイル

- Submission TSVs: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_clean_v21/infection_study_04/submissions/`
- cellxgene H5ADs: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_clean_v21/infection_study_04/cellxgene/`
- Marker availability table: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_clean_v21/infection_study_04/tables/marker_gene_availability.tsv`
- Marker availability alerts: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_clean_v21/infection_study_04/tables/marker_gene_availability_alerts.tsv`
- Subcluster evidence: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_clean_v21/infection_study_04/tables/lineage_subcluster_evidence.tsv.gz`
- Source disagreement summary: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_clean_v21/infection_study_04/tables/source_disagreement_summary.tsv`
- Diagnostics tables: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_clean_v21/infection_study_04/tables/`

