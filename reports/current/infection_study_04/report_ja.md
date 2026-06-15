# HIPC データセットアノテーションレポート: infection_study_04

更新日: 2026-06-15 EDT

このレポートは `hipc-annotation` Codex workflow によって生成したデータセット別レビュー文書です。固定 method は repository README に置き、このレポートでは実際の evidence、弱い箇所、レビュー優先度、UMAP / dotplot を確認します。

## データセット概要

| study | cells | analysis_X_genes | pre_hvg_genes | counts_layer_genes | labels | parent_or_blood_fraction | Blood Cell | Doublet | artifact_like | median_confidence | low_confidence | source_disagreement | invalid_labels |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| infection_study_04 | 43,767 | 26,361 | 26,361 | 26,361 | 18 | 0.017 | 746 | 132 | 294 | 0.762 | 2,607 | 7,836 (0.179) | none |

## 実行概要

- 実行単位: one dataset in, one annotated dataset out。
- 実行経路: Codex skill `hipc-annotation` -> bundled helper `run_one.sh` -> annotation CLI -> validator -> report inspection。
- 検証: submission row count、H5AD observation count、official label validity、H5AD/submission agreement、confidence column、report image link を確認する。
- このレポートは workflow の再掲ではなく、このデータセットの marker 欠損、UMAP、label 構成、review concern を読むためのもの。

## データセット固有の解釈

- `infection_study_04`: 43,767 cells、analysis X/var 26,361 genes、pre-HVG slot 26,361 genes、submitted label 18 種、parent/Blood residual fraction 0.017、median confidence 0.762。
  - 2,607 cells は low confidence。QC / confidence UMAP 上で局在を確認する。
  - 132 cells は `Doublet` として提出。mixed-lineage marker expression と scrublet support を確認する。
  - 746 cells は `Blood Cell` として残存。これは filter-out ではなく、曖昧な細胞を公式 parent label で残したもの。
  - Marker gene 欠損アラート: Plasma_ASC。該当 marker set に依存する fine label は慎重に見る。

## データセット固有の評価

- 全体像: 43,767 cells / analysis X/var 26,361 genes / pre-HVG slot 26,361 genes。parent/Blood residual は 0.017、low-confidence は 2,607 cells、source disagreement flag は 7,836 cells (0.179)。
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
| infection_study_04 | Neutrophil | 132 | 0.250 | 132 | 1.000 |
| infection_study_04 | Memory B Cell | 1,674 | 0.400 | 1,365 | 0.815 |
| infection_study_04 | Blood Cell | 746 | 0.250 | 479 | 0.642 |
| infection_study_04 | MAIT Cell | 392 | 0.500 | 181 | 0.462 |
| infection_study_04 | Naive B Cell | 1,790 | 0.600 | 690 | 0.385 |
| infection_study_04 | Treg | 484 | 0.600 | 131 | 0.271 |
| infection_study_04 | Plasma Cell | 3,272 | 0.600 | 685 | 0.209 |
| infection_study_04 | CD8 Cytotoxic / T Effector Memory | 6,980 | 0.750 | 1,417 | 0.203 |
| infection_study_04 | Conventional DC 2 | 420 | 0.750 | 69 | 0.164 |
| infection_study_04 | NK Cell | 6,812 | 1.000 | 813 | 0.119 |
| infection_study_04 | CD4 Naive / T Central Memory | 8,282 | 0.800 | 969 | 0.117 |

## アノテーションソース効果

この表は外部 ground truth に対する正解率ではありません。各 annotation source がどれだけの細胞で情報を持ち、final label とどれだけ一致したかを示す監査用統計です。`coverage` は source が `not_available` 以外を返した割合、`final_concordance` は informative cells の中で final label と一致した割合、`unique_support` はその source だけが final label と一致した細胞数です。

| study | source | informative_cells | coverage | final_concordance | high_conf_concordance | unique_support | discordant |
| --- | --- | --- | --- | --- | --- | --- | --- |
| infection_study_04 | Cluster consensus | 43,767 | 1.000 | 0.800 | 0.835 | 356 | 8,732 |
| infection_study_04 | Azimuth PBMC L2 | 43,767 | 1.000 | 0.724 | 0.756 | 59 | 12,074 |
| infection_study_04 | Pan-human Azimuth | 43,767 | 1.000 | 0.702 | 0.774 | 464 | 13,044 |
| infection_study_04 | CellTypist | 43,767 | 1.000 | 0.700 | 0.800 | 121 | 13,133 |
| infection_study_04 | Azimuth PBMC L3 | 43,767 | 1.000 | 0.386 | 0.535 | 20 | 26,863 |
| infection_study_04 | Cluster marker assignment | 42,578 | 0.973 | 0.922 | 0.979 | 1,625 | 3,332 |
| infection_study_04 | scRefMapping | 14,670 | 0.335 | 0.756 | 0.855 | 86 | 3,586 |

## レビュー優先事項

| study | concern | cells |
| --- | --- | --- |
| infection_study_04 | High source disagreement for Blood Cell | 479 |
| infection_study_04 | High source disagreement for Doublet | 132 |
| infection_study_04 | High source disagreement for Memory B Cell | 1,365 |
| infection_study_04 | High source disagreement for Neutrophil | 132 |
| infection_study_04 | warning marker availability for Plasma_ASC | 3,272 |

## ラベル構成

| study | predicted_cell_type | cells |
| --- | --- | --- |
| infection_study_04 | Classical Monocyte | 10,603 |
| infection_study_04 | CD4 Naive / T Central Memory | 8,282 |
| infection_study_04 | CD8 Cytotoxic / T Effector Memory | 6,980 |
| infection_study_04 | NK Cell | 6,812 |
| infection_study_04 | Plasma Cell | 3,272 |
| infection_study_04 | Naive B Cell | 1,790 |
| infection_study_04 | Memory B Cell | 1,674 |
| infection_study_04 | Non-Classical Monocyte | 1,502 |
| infection_study_04 | Blood Cell | 746 |
| infection_study_04 | Treg | 484 |
| infection_study_04 | Conventional DC 2 | 420 |
| infection_study_04 | MAIT Cell | 392 |
| infection_study_04 | Plasmacytoid DC | 229 |
| infection_study_04 | Platelet | 172 |
| infection_study_04 | Neutrophil | 132 |
| infection_study_04 | Doublet | 132 |
| infection_study_04 | HSC | 122 |
| infection_study_04 | Conventional DC 1 | 23 |

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
| infection_study_04 | T_NK_lineage | 1 | 1,362 | NK Cell | NK Cell | NK Cell | raw_marker_winner | 0.866 | 1.000 | 0.134 | screfmapping_missing_for_scope |
| infection_study_04 | T_NK_lineage | 2 | 1,353 | NK Cell | NK Cell | NK Cell | raw_marker_winner | 0.885 | 1.000 | 0.115 | screfmapping_missing_for_scope |
| infection_study_04 | T_NK_lineage | 3 | 1,174 | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | raw_marker_winner | 0.631 | 1.000 | 0.369 | screfmapping_missing_for_scope |
| infection_study_04 | T_NK_lineage | 5 | 1,163 | NK Cell | NK Cell | NK Cell | raw_marker_winner | 0.760 | 1.000 | 0.240 | screfmapping_missing_for_scope |
| infection_study_04 | T_NK_lineage | 6 | 1,129 | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | NKT Cell | source_supported_marker_tiebreak | 0.635 | 1.000 | 0.365 | screfmapping_missing_for_scope |
| infection_study_04 | T_NK_lineage | 7 | 992 | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | raw_marker_winner | 0.736 | 1.000 | 0.264 | screfmapping_missing_for_scope |
| infection_study_04 | T_NK_lineage | 11 | 847 | NK Cell | NK Cell | NK Cell | raw_marker_winner | 0.757 | 1.000 | 0.243 | screfmapping_missing_for_scope |
| infection_study_04 | T_NK_lineage | 12 | 757 | NK Cell | NK Cell | NKT Cell | source_supported_marker_tiebreak | 0.659 | 0.839 | 0.180 | screfmapping_missing_for_scope |
| infection_study_04 | T_NK_lineage | 13 | 751 | CD8 Cytotoxic / T Effector Memory | NKT Cell | NKT Cell | raw_marker_winner | 0.681 | 0.909 | 0.228 | marker_final_disagreement;screfmapping_missing_for_scope |
| infection_study_04 | T_NK_lineage | 14 | 740 | CD4 Naive / T Central Memory | CD8 Naive / T Central Memory | CD8 Naive / T Central Memory | raw_marker_winner | 0.949 | 1.000 | 0.051 | marker_final_disagreement |
| infection_study_04 | T_NK_lineage | 15 | 736 | NK Cell | NK Cell | NKT Cell | source_supported_marker_tiebreak | 0.676 | 0.816 | 0.140 | screfmapping_missing_for_scope |
| infection_study_04 | T_NK_lineage | 18 | 680 | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | raw_marker_winner | 0.692 | 1.000 | 0.308 | screfmapping_missing_for_scope |
| infection_study_04 | T_NK_lineage | 19 | 593 | NK Cell | NK Cell | NK Cell | raw_marker_winner | 0.836 | 1.000 | 0.164 | screfmapping_missing_for_scope |
| infection_study_04 | T_NK_lineage | 20 | 567 | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | NKT Cell | source_supported_marker_tiebreak | 0.790 | 0.875 | 0.085 | screfmapping_missing_for_scope |
| infection_study_04 | B_lineage | 2 | 549 | Memory B Cell | Naive B Cell | Naive B Cell | raw_marker_winner | 0.516 | 0.707 | 0.190 | marker_final_disagreement |
| infection_study_04 | B_lineage | 4 | 470 | Memory B Cell | Naive B Cell | Naive B Cell | raw_marker_winner | 0.456 | 0.738 | 0.282 | marker_final_disagreement |
| infection_study_04 | T_NK_lineage | 22 | 463 | CD4 Naive / T Central Memory | NKT Cell | NKT Cell | raw_marker_winner | 0.351 | 0.577 | 0.226 | marker_final_disagreement |
| infection_study_04 | T_NK_lineage | 23 | 438 | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | raw_marker_winner | 0.719 | 1.000 | 0.281 | screfmapping_missing_for_scope |
| infection_study_04 | T_NK_lineage | 26 | 336 | CD4 Naive / T Central Memory | NKT Cell | NKT Cell | raw_marker_winner | 0.537 | 0.676 | 0.138 | marker_final_disagreement |
| infection_study_04 | B_lineage | 13 | 257 | Memory B Cell | Memory B Cell | Memory B Cell | raw_marker_winner | 0.299 | 0.501 | 0.202 | weak_marker_specificity |

## LLM Review Queue

この表は Codex/LLM が読むための subcluster-level review queue です。LLM はこの evidence を読んで、final label が妥当か、ontology にちょうどよい label がないのか、registry / conservative policy を一般ルールとして更新すべきかを提案します。LLM の出力で per-cell label を直接書き換えず、採用する場合は registry/config を更新して deterministic pipeline を再実行します。

| study | lineage | cluster | cells | priority | reasons | suggested_action | final_label | marker_assignment | raw_marker_winner | score_margin |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| infection_study_04 | T_NK_lineage | 6 | 1,129 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | NKT Cell | 2.323 |
| infection_study_04 | T_NK_lineage | 13 | 751 | medium | marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | CD8 Cytotoxic / T Effector Memory | NKT Cell | NKT Cell | 0.837 |
| infection_study_04 | T_NK_lineage | 22 | 463 | medium | marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | CD4 Naive / T Central Memory | NKT Cell | NKT Cell | 0.255 |
| infection_study_04 | T_NK_lineage | 26 | 336 | medium | marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | CD4 Naive / T Central Memory | NKT Cell | NKT Cell | 1.009 |
| infection_study_04 | T_NK_lineage | 12 | 757 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | NK Cell | NK Cell | NKT Cell | 1.800 |
| infection_study_04 | T_NK_lineage | 15 | 736 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | NK Cell | NK Cell | NKT Cell | 1.401 |
| infection_study_04 | T_NK_lineage | 20 | 567 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | NKT Cell | 0.186 |
| infection_study_04 | B_lineage | 2 | 549 | medium | marker_assignment_disagrees_with_final;low_total_score_or_margin | review_marker_vs_reference_disagreement | Memory B Cell | Naive B Cell | Naive B Cell | 0.030 |
| infection_study_04 | T_NK_lineage | 14 | 740 | medium | marker_assignment_disagrees_with_final;screfmapping_not_available | review_marker_vs_reference_disagreement | CD4 Naive / T Central Memory | CD8 Naive / T Central Memory | CD8 Naive / T Central Memory | 0.471 |
| infection_study_04 | T_NK_lineage | 29 | 219 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | NKT Cell | 1.307 |
| infection_study_04 | T_NK_lineage | 1 | 1,362 | low | screfmapping_not_available | accept | NK Cell | NK Cell | NK Cell | 2.683 |
| infection_study_04 | T_NK_lineage | 2 | 1,353 | low | screfmapping_not_available | accept | NK Cell | NK Cell | NK Cell | 2.486 |
| infection_study_04 | T_NK_lineage | 3 | 1,174 | low | screfmapping_not_available | accept | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | 2.471 |
| infection_study_04 | T_NK_lineage | 5 | 1,163 | low | screfmapping_not_available | accept | NK Cell | NK Cell | NK Cell | 1.648 |
| infection_study_04 | B_lineage | 4 | 470 | low | marker_assignment_disagrees_with_final | review_marker_vs_reference_disagreement | Memory B Cell | Naive B Cell | Naive B Cell | 1.655 |
| infection_study_04 | Myeloid_lineage | 26 | 23 | low | marker_assignment_disagrees_with_final;screfmapping_not_available | review_marker_vs_reference_disagreement | Conventional DC 1 | Intermediate Monocyte | Intermediate Monocyte | 1.406 |
| infection_study_04 | T_NK_lineage | 7 | 992 | low | screfmapping_not_available | accept | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | 2.261 |
| infection_study_04 | T_NK_lineage | 11 | 847 | low | screfmapping_not_available | accept | NK Cell | NK Cell | NK Cell | 2.237 |
| infection_study_04 | T_NK_lineage | 18 | 680 | low | screfmapping_not_available | accept | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | 1.206 |
| infection_study_04 | T_NK_lineage | 19 | 593 | low | screfmapping_not_available | accept | NK Cell | NK Cell | NK Cell | 2.649 |

## Cluster Consensus Evidence

| study | lineage | cluster | cells | chosen_label | accepted | score_margin | cluster_marker_assignment | treg_key_any | treg_key_bonus | marker_set | marker_alert |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| infection_study_04 | B_lineage | 0 | 774 | Naive B Cell | True | 4.406 | Naive B Cell | nan | nan | B_naive | pass |
| infection_study_04 | B_lineage | 1 | 556 | Plasma Cell | True | 1.807 | Plasma Cell | nan | nan | Plasma_ASC | warning |
| infection_study_04 | B_lineage | 2 | 549 | Memory B Cell | True | 0.030 | Naive B Cell | nan | nan | B_memory_ABC | pass |
| infection_study_04 | B_lineage | 3 | 472 | Plasma Cell | True | 1.859 | Plasma Cell | nan | nan | Plasma_ASC | warning |
| infection_study_04 | B_lineage | 4 | 470 | Memory B Cell | True | 1.655 | Naive B Cell | nan | nan | B_memory_ABC | pass |
| infection_study_04 | B_lineage | 5 | 465 | Plasma Cell | True | 1.909 | Plasma Cell | nan | nan | Plasma_ASC | warning |
| infection_study_04 | B_lineage | 6 | 398 | Memory B Cell | True | 2.317 | Memory B Cell | nan | nan | B_memory_ABC | pass |
| infection_study_04 | B_lineage | 7 | 330 | Naive B Cell | True | 0.980 | Naive B Cell | nan | nan | B_naive | pass |
| infection_study_04 | B_lineage | 8 | 323 | Naive B Cell | True | 4.135 | Naive B Cell | nan | nan | B_naive | pass |
| infection_study_04 | B_lineage | 9 | 323 | Plasma Cell | True | 1.592 | Plasma Cell | nan | nan | Plasma_ASC | warning |
| infection_study_04 | B_lineage | 10 | 266 | Naive B Cell | True | 1.246 | Naive B Cell | nan | nan | B_naive | pass |
| infection_study_04 | B_lineage | 11 | 264 | Plasma Cell | True | 1.031 | Plasma Cell | nan | nan | Plasma_ASC | warning |
| infection_study_04 | B_lineage | 12 | 264 | Plasma Cell | True | 1.088 | Plasma Cell | nan | nan | Plasma_ASC | warning |
| infection_study_04 | B_lineage | 13 | 257 | Memory B Cell | True | 3.272 | Memory B Cell | nan | nan | B_memory_ABC | pass |
| infection_study_04 | B_lineage | 14 | 236 | Plasma Cell | True | 1.317 | Plasma Cell | nan | nan | Plasma_ASC | warning |
| infection_study_04 | B_lineage | 15 | 208 | Plasma Cell | True | 1.578 | Plasma Cell | nan | nan | Plasma_ASC | warning |
| infection_study_04 | B_lineage | 16 | 119 | Plasma Cell | True | 1.755 | Plasma Cell | nan | nan | Plasma_ASC | warning |
| infection_study_04 | B_lineage | 17 | 113 | Plasma Cell | True | 1.062 | Plasma Cell | nan | nan | Plasma_ASC | warning |
| infection_study_04 | B_lineage | 18 | 97 | Naive B Cell | True | 3.561 | Naive B Cell | nan | nan | B_naive | pass |
| infection_study_04 | B_lineage | 19 | 95 | Plasma Cell | True | 1.653 | Plasma Cell | nan | nan | Plasma_ASC | warning |
| infection_study_04 | B_lineage | 20 | 88 | Plasma Cell | True | 1.807 | Plasma Cell | nan | nan | Plasma_ASC | warning |
| infection_study_04 | B_lineage | 21 | 69 | Plasma Cell | True | 0.852 | Plasma Cell | nan | nan | Plasma_ASC | warning |
| infection_study_04 | Myeloid_lineage | 0 | 1,513 | Classical Monocyte | True | 2.223 | Classical Monocyte | nan | nan | registry__classical_monocyte | pass |
| infection_study_04 | Myeloid_lineage | 1 | 920 | Classical Monocyte | True | 2.291 | Classical Monocyte | nan | nan | registry__classical_monocyte | pass |
| infection_study_04 | Myeloid_lineage | 2 | 867 | Classical Monocyte | True | 2.535 | Classical Monocyte | nan | nan | registry__classical_monocyte | pass |
| infection_study_04 | Myeloid_lineage | 3 | 866 | Classical Monocyte | True | 2.655 | Classical Monocyte | nan | nan | registry__classical_monocyte | pass |
| infection_study_04 | Myeloid_lineage | 4 | 749 | Classical Monocyte | True | 2.154 | Classical Monocyte | nan | nan | registry__classical_monocyte | pass |
| infection_study_04 | Myeloid_lineage | 5 | 736 | Non-Classical Monocyte | True | 2.211 | Non-Classical Monocyte | nan | nan | registry__non_classical_monocyte | pass |
| infection_study_04 | Myeloid_lineage | 6 | 734 | Classical Monocyte | True | 2.435 | Classical Monocyte | nan | nan | registry__classical_monocyte | pass |
| infection_study_04 | Myeloid_lineage | 7 | 598 | Classical Monocyte | True | 2.381 | Classical Monocyte | nan | nan | registry__classical_monocyte | pass |

## 出力ファイル

- Submission TSVs: `outputs/submission_v25_harmony_reference_rescue/infection_study_04/submissions/`
- cellxgene H5ADs: `outputs/submission_v25_harmony_reference_rescue/infection_study_04/cellxgene/`
- Marker availability table: `outputs/submission_v25_harmony_reference_rescue/infection_study_04/tables/marker_gene_availability.tsv`
- Marker availability alerts: `outputs/submission_v25_harmony_reference_rescue/infection_study_04/tables/marker_gene_availability_alerts.tsv`
- Subcluster evidence: `outputs/submission_v25_harmony_reference_rescue/infection_study_04/tables/lineage_subcluster_evidence.tsv.gz`
- Source disagreement summary: `outputs/submission_v25_harmony_reference_rescue/infection_study_04/tables/source_disagreement_summary.tsv`
- Source effectiveness summary: `outputs/submission_v25_harmony_reference_rescue/infection_study_04/tables/source_effectiveness_summary.tsv`
- Diagnostics tables: `outputs/submission_v25_harmony_reference_rescue/infection_study_04/tables/`

