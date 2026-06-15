# HIPC データセットアノテーションレポート: vaccination_study_04

更新日: 2026-06-15 EDT

このレポートは `hipc-annotation` Codex workflow によって生成したデータセット別レビュー文書です。固定 method は repository README に置き、このレポートでは実際の evidence、弱い箇所、レビュー優先度、UMAP / dotplot を確認します。

## データセット概要

| study | cells | analysis_X_genes | pre_hvg_genes | counts_layer_genes | labels | parent_or_blood_fraction | Blood Cell | Doublet | artifact_like | median_confidence | low_confidence | source_disagreement | invalid_labels |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| vaccination_study_04 | 66,065 | 16,983 | 16,983 | 16,983 | 15 | 0.006 | 256 | 647 | 350 | 0.777 | 1,123 | 2,561 (0.039) | none |

## 実行概要

- 実行単位: one dataset in, one annotated dataset out。
- 実行経路: Codex skill `hipc-annotation` -> bundled helper `run_one.sh` -> annotation CLI -> validator -> report inspection。
- 検証: submission row count、H5AD observation count、official label validity、H5AD/submission agreement、confidence column、report image link を確認する。
- このレポートは workflow の再掲ではなく、このデータセットの marker 欠損、UMAP、label 構成、review concern を読むためのもの。

## データセット固有の解釈

- `vaccination_study_04`: 66,065 cells、analysis X/var 16,983 genes、pre-HVG slot 16,983 genes、submitted label 15 種、parent/Blood residual fraction 0.006、median confidence 0.777。
  - 1,123 cells は low confidence。QC / confidence UMAP 上で局在を確認する。
  - 647 cells は `Doublet` として提出。mixed-lineage marker expression と scrublet support を確認する。
  - 256 cells は `Blood Cell` として残存。これは filter-out ではなく、曖昧な細胞を公式 parent label で残したもの。
  - Marker gene 欠損アラート: Treg, gdT。該当 marker set に依存する fine label は慎重に見る。

## データセット固有の評価

- 全体像: 66,065 cells / analysis X/var 16,983 genes / pre-HVG slot 16,983 genes。parent/Blood residual は 0.006、low-confidence は 1,123 cells、source disagreement flag は 2,561 cells (0.039)。
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
| vaccination_study_04 | T Cell | 77 | 0.000 | 77 | 1.000 |
| vaccination_study_04 | B Cell | 33 | 0.000 | 33 | 1.000 |
| vaccination_study_04 | CD4 T Effector Memory | 2 | 0.200 | 2 | 1.000 |
| vaccination_study_04 | CD4 Naive / T Central Memory | 28 | 0.600 | 11 | 0.393 |
| vaccination_study_04 | NK Cell | 298 | 0.750 | 86 | 0.289 |
| vaccination_study_04 | Plasma Cell | 115 | 0.600 | 24 | 0.209 |
| vaccination_study_04 | Conventional DC 2 | 7,981 | 1.000 | 1,089 | 0.136 |
| vaccination_study_04 | Blood Cell | 256 | 0.750 | 27 | 0.105 |
| vaccination_study_04 | Conventional DC 1 | 1,089 | 1.000 | 20 | 0.018 |
| vaccination_study_04 | Classical Monocyte | 33,893 | 1.000 | 380 | 0.011 |
| vaccination_study_04 | Non-Classical Monocyte | 15,993 | 1.000 | 164 | 0.010 |

## アノテーションソース効果

この表は外部 ground truth に対する正解率ではありません。各 annotation source がどれだけの細胞で情報を持ち、final label とどれだけ一致したかを示す監査用統計です。`coverage` は source が `not_available` 以外を返した割合、`final_concordance` は informative cells の中で final label と一致した割合、`unique_support` はその source だけが final label と一致した細胞数です。

| study | source | informative_cells | coverage | final_concordance | high_conf_concordance | unique_support | discordant |
| --- | --- | --- | --- | --- | --- | --- | --- |
| vaccination_study_04 | Cluster consensus | 66,065 | 1.000 | 0.949 | 0.971 | 22 | 3,370 |
| vaccination_study_04 | CellTypist | 66,065 | 1.000 | 0.934 | 0.982 | 4 | 4,389 |
| vaccination_study_04 | Azimuth PBMC L2 | 66,065 | 1.000 | 0.932 | 0.975 | 0 | 4,482 |
| vaccination_study_04 | Pan-human Azimuth | 66,065 | 1.000 | 0.906 | 0.931 | 24 | 6,193 |
| vaccination_study_04 | Azimuth PBMC L3 | 66,065 | 1.000 | 0.840 | 0.901 | 1 | 10,599 |
| vaccination_study_04 | Cluster marker assignment | 64,647 | 0.979 | 0.979 | 0.981 | 610 | 1,386 |
| vaccination_study_04 | scRefMapping | 170 | 0.003 | 0.300 | 0.736 | 0 | 119 |

## レビュー優先事項

| study | concern | cells |
| --- | --- | --- |
| vaccination_study_04 | High source disagreement for B Cell | 33 |
| vaccination_study_04 | High source disagreement for CD4 T Effector Memory | 2 |
| vaccination_study_04 | High source disagreement for Doublet | 647 |
| vaccination_study_04 | High source disagreement for T Cell | 77 |

## ラベル構成

| study | predicted_cell_type | cells |
| --- | --- | --- |
| vaccination_study_04 | Classical Monocyte | 33,893 |
| vaccination_study_04 | Non-Classical Monocyte | 15,993 |
| vaccination_study_04 | Conventional DC 2 | 7,981 |
| vaccination_study_04 | Plasmacytoid DC | 5,303 |
| vaccination_study_04 | Conventional DC 1 | 1,089 |
| vaccination_study_04 | Doublet | 647 |
| vaccination_study_04 | HSC | 346 |
| vaccination_study_04 | NK Cell | 298 |
| vaccination_study_04 | Blood Cell | 256 |
| vaccination_study_04 | Plasma Cell | 115 |
| vaccination_study_04 | T Cell | 77 |
| vaccination_study_04 | B Cell | 33 |
| vaccination_study_04 | CD4 Naive / T Central Memory | 28 |
| vaccination_study_04 | Platelet | 4 |
| vaccination_study_04 | CD4 T Effector Memory | 2 |

## Inline Figures

### vaccination_study_04

![vaccination_study_04 final labels](assets/umap_vaccination_study_04_annotation_label.png)

![vaccination_study_04 lineage and annotation reason](assets/umap_vaccination_study_04_annotation_lineage_reason.png)

![vaccination_study_04 QC and confidence](assets/umap_vaccination_study_04_annotation_qc_confidence.png)

![vaccination_study_04 source agreement and disagreement](assets/umap_vaccination_study_04_annotation_source_disagreement.png)

![vaccination_study_04 annotation-source effectiveness](assets/figure_02_source_effectiveness.png)

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
| vaccination_study_04 | Myeloid_lineage | 6 | 1,089 | Conventional DC 1 | Intermediate Monocyte | Intermediate Monocyte | raw_marker_winner | 0.828 | 0.998 | 0.170 | marker_final_disagreement |
| vaccination_study_04 | T_NK_lineage | 0 | 38 | T Cell | gdT Cell | gdT Cell | raw_marker_winner | 0.775 | 1.000 | 0.225 | marker_final_disagreement;screfmapping_missing_for_scope |
| vaccination_study_04 | T_NK_lineage | 1 | 37 | NK Cell | NK Cell | NK Cell | raw_marker_winner | 0.487 | 0.973 | 0.486 | screfmapping_missing_for_scope |
| vaccination_study_04 | T_NK_lineage | 2 | 35 | NK Cell | CD8 Naive / T Central Memory | CD8 Naive / T Central Memory | raw_marker_winner | 0.670 | 0.857 | 0.188 | marker_final_disagreement |
| vaccination_study_04 | T_NK_lineage | 3 | 33 | NK Cell | NK Cell | NKT Cell | source_supported_marker_tiebreak | 0.909 | 1.000 | 0.091 | screfmapping_missing_for_scope |
| vaccination_study_04 | T_NK_lineage | 5 | 33 | NK Cell | NK Cell | NKT Cell | source_supported_marker_tiebreak | 0.964 | 1.000 | 0.036 | screfmapping_missing_for_scope |
| vaccination_study_04 | T_NK_lineage | 4 | 33 | NK Cell | NK Cell | NKT Cell | source_supported_marker_tiebreak | 1.000 | 1.000 | 0.000 | screfmapping_missing_for_scope |
| vaccination_study_04 | B_lineage | 0 | 31 | B Cell | Plasmablast | Plasmablast | raw_marker_winner | 0.590 | 1.000 | 0.410 | marker_final_disagreement;screfmapping_missing_for_scope |
| vaccination_study_04 | T_NK_lineage | 6 | 31 | NK Cell | NKT Cell | NKT Cell | raw_marker_winner | 0.923 | 1.000 | 0.077 | marker_final_disagreement;screfmapping_missing_for_scope |
| vaccination_study_04 | T_NK_lineage | 7 | 28 | NK Cell | NKT Cell | NKT Cell | raw_marker_winner | 0.871 | 1.000 | 0.129 | marker_final_disagreement;screfmapping_missing_for_scope |
| vaccination_study_04 | T_NK_lineage | 9 | 26 | T Cell | gdT Cell | gdT Cell | raw_marker_winner | 0.729 | 1.000 | 0.271 | marker_final_disagreement;screfmapping_missing_for_scope |
| vaccination_study_04 | T_NK_lineage | 10 | 24 | NK Cell | NK Cell | NKT Cell | source_supported_marker_tiebreak | 0.925 | 1.000 | 0.075 | screfmapping_missing_for_scope |
| vaccination_study_04 | B_lineage | 1 | 22 | Plasma Cell | Plasmablast | Plasmablast | raw_marker_winner | 0.936 | 1.000 | 0.064 | marker_final_disagreement |
| vaccination_study_04 | T_NK_lineage | 12 | 20 | NK Cell | NK Cell | NKT Cell | source_supported_marker_tiebreak | 0.910 | 1.000 | 0.090 | screfmapping_missing_for_scope |
| vaccination_study_04 | B_lineage | 3 | 19 | Plasma Cell | Plasmablast | Plasmablast | raw_marker_winner | 0.784 | 1.000 | 0.216 | marker_final_disagreement |
| vaccination_study_04 | B_lineage | 2 | 19 | Plasma Cell | Plasmablast | Plasmablast | raw_marker_winner | 0.789 | 1.000 | 0.211 | marker_final_disagreement |
| vaccination_study_04 | B_lineage | 4 | 16 | Plasma Cell | Plasmablast | Plasmablast | raw_marker_winner | 0.672 | 1.000 | 0.328 | marker_final_disagreement |
| vaccination_study_04 | T_NK_lineage | 13 | 13 | T Cell | CD8 Naive / T Central Memory | CD8 Naive / T Central Memory | raw_marker_winner | 0.992 | 0.992 | 0.000 | marker_final_disagreement;screfmapping_missing_for_scope |
| vaccination_study_04 | B_lineage | 6 | 12 | Plasma Cell | Plasmablast | Plasmablast | raw_marker_winner | 0.804 | 1.000 | 0.196 | marker_final_disagreement |
| vaccination_study_04 | B_lineage | 8 | 5 | Plasma Cell | Plasmablast | Plasmablast | raw_marker_winner | 0.860 | 1.000 | 0.140 | marker_final_disagreement |

## LLM Review Queue

この表は Codex/LLM が読むための subcluster-level review queue です。LLM はこの evidence を読んで、final label が妥当か、ontology にちょうどよい label がないのか、registry / conservative policy を一般ルールとして更新すべきかを提案します。LLM の出力で per-cell label を直接書き換えず、採用する場合は registry/config を更新して deterministic pipeline を再実行します。

| study | lineage | cluster | cells | priority | reasons | suggested_action | final_label | marker_assignment | raw_marker_winner | score_margin |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| vaccination_study_04 | T_NK_lineage | 9 | 26 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | T Cell | gdT Cell | gdT Cell | 0.185 |
| vaccination_study_04 | T_NK_lineage | 0 | 38 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available | check_if_finer_official_label_is_supported | T Cell | gdT Cell | gdT Cell | 0.236 |
| vaccination_study_04 | B_lineage | 0 | 31 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available | check_if_finer_official_label_is_supported | B Cell | Plasmablast | Plasmablast | 0.328 |
| vaccination_study_04 | B_lineage | 9 | 2 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | B Cell | Naive B Cell | Naive B Cell | 0.110 |
| vaccination_study_04 | T_NK_lineage | 13 | 13 | medium | parent_or_broad_final_label;marker_assignment_disagrees_with_final;screfmapping_not_available | check_if_finer_official_label_is_supported | T Cell | CD8 Naive / T Central Memory | CD8 Naive / T Central Memory | 0.141 |
| vaccination_study_04 | Myeloid_lineage | 6 | 1,089 | medium | marker_assignment_disagrees_with_final;screfmapping_not_available | review_marker_vs_reference_disagreement | Conventional DC 1 | Intermediate Monocyte | Intermediate Monocyte | 2.135 |
| vaccination_study_04 | T_NK_lineage | 6 | 31 | medium | marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | NK Cell | NKT Cell | NKT Cell | 1.768 |
| vaccination_study_04 | T_NK_lineage | 7 | 28 | medium | marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | NK Cell | NKT Cell | NKT Cell | 2.349 |
| vaccination_study_04 | T_NK_lineage | 3 | 33 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | NK Cell | NK Cell | NKT Cell | 2.495 |
| vaccination_study_04 | T_NK_lineage | 4 | 33 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | NK Cell | NK Cell | NKT Cell | 2.451 |
| vaccination_study_04 | T_NK_lineage | 5 | 33 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | NK Cell | NK Cell | NKT Cell | 2.503 |
| vaccination_study_04 | T_NK_lineage | 10 | 24 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | NK Cell | NK Cell | NKT Cell | 2.385 |
| vaccination_study_04 | B_lineage | 1 | 22 | medium | marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate | evaluate_ontology_gap_or_conservative_policy | Plasma Cell | Plasmablast | Plasmablast | 0.573 |
| vaccination_study_04 | T_NK_lineage | 12 | 20 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | NK Cell | NK Cell | NKT Cell | 2.385 |
| vaccination_study_04 | B_lineage | 2 | 19 | medium | marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate | evaluate_ontology_gap_or_conservative_policy | Plasma Cell | Plasmablast | Plasmablast | 0.737 |
| vaccination_study_04 | B_lineage | 3 | 19 | medium | marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate | evaluate_ontology_gap_or_conservative_policy | Plasma Cell | Plasmablast | Plasmablast | 0.837 |
| vaccination_study_04 | B_lineage | 4 | 16 | medium | marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate | evaluate_ontology_gap_or_conservative_policy | Plasma Cell | Plasmablast | Plasmablast | 1.028 |
| vaccination_study_04 | B_lineage | 6 | 12 | medium | marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate | evaluate_ontology_gap_or_conservative_policy | Plasma Cell | Plasmablast | Plasmablast | 0.863 |
| vaccination_study_04 | B_lineage | 8 | 5 | medium | marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate | evaluate_ontology_gap_or_conservative_policy | Plasma Cell | Plasmablast | Plasmablast | 0.340 |
| vaccination_study_04 | T_NK_lineage | 2 | 35 | low | marker_assignment_disagrees_with_final;screfmapping_not_available | review_marker_vs_reference_disagreement | NK Cell | CD8 Naive / T Central Memory | CD8 Naive / T Central Memory | 0.395 |

## Cluster Consensus Evidence

| study | lineage | cluster | cells | chosen_label | accepted | score_margin | cluster_marker_assignment | treg_key_any | treg_key_bonus | marker_set | marker_alert |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| vaccination_study_04 | B_lineage | 0 | 31 | B Cell | False | 0.328 | Plasmablast | nan | nan | B_naive | pass |
| vaccination_study_04 | B_lineage | 1 | 22 | Plasma Cell | True | 0.573 | Plasmablast | nan | nan | Plasma_ASC | pass |
| vaccination_study_04 | B_lineage | 2 | 19 | Plasma Cell | True | 0.737 | Plasmablast | nan | nan | Plasma_ASC | pass |
| vaccination_study_04 | B_lineage | 3 | 19 | Plasma Cell | True | 0.837 | Plasmablast | nan | nan | Plasma_ASC | pass |
| vaccination_study_04 | B_lineage | 4 | 16 | Plasma Cell | True | 1.028 | Plasmablast | nan | nan | Plasma_ASC | pass |
| vaccination_study_04 | B_lineage | 5 | 14 | Plasma Cell | True | 0.040 | Plasma Cell | nan | nan | Plasma_ASC | pass |
| vaccination_study_04 | B_lineage | 6 | 12 | Plasma Cell | True | 0.863 | Plasmablast | nan | nan | Plasma_ASC | pass |
| vaccination_study_04 | B_lineage | 7 | 8 | Plasma Cell | True | 1.175 | Plasma Cell | nan | nan | Plasma_ASC | pass |
| vaccination_study_04 | B_lineage | 8 | 5 | Plasma Cell | True | 0.340 | Plasmablast | nan | nan | Plasma_ASC | pass |
| vaccination_study_04 | B_lineage | 9 | 2 | B Cell | False | 0.110 | Naive B Cell | nan | nan | B_naive | pass |
| vaccination_study_04 | Myeloid_lineage | 4 | 15,213 | Classical Monocyte | True | 2.435 | Classical Monocyte | nan | nan | registry__classical_monocyte | pass |
| vaccination_study_04 | Myeloid_lineage | 2 | 13,129 | Classical Monocyte | True | 2.421 | Classical Monocyte | nan | nan | registry__classical_monocyte | pass |
| vaccination_study_04 | Myeloid_lineage | 1 | 8,275 | Non-Classical Monocyte | True | 1.609 | Non-Classical Monocyte | nan | nan | registry__non_classical_monocyte | pass |
| vaccination_study_04 | Myeloid_lineage | 5 | 7,713 | Non-Classical Monocyte | True | 1.613 | Non-Classical Monocyte | nan | nan | registry__non_classical_monocyte | pass |
| vaccination_study_04 | Myeloid_lineage | 7 | 5,515 | Classical Monocyte | True | 2.251 | Classical Monocyte | nan | nan | registry__classical_monocyte | pass |
| vaccination_study_04 | Myeloid_lineage | 8 | 4,633 | Conventional DC 2 | True | 2.410 | Conventional DC 2 | nan | nan | registry__conventional_dc_2 | pass |
| vaccination_study_04 | Myeloid_lineage | 0 | 3,346 | Conventional DC 2 | True | 0.506 | Conventional DC 2 | nan | nan | registry__conventional_dc_2 | pass |
| vaccination_study_04 | Myeloid_lineage | 3 | 2,756 | Plasmacytoid DC | True | 2.625 | Plasmacytoid DC | nan | nan | registry__plasmacytoid_dc | pass |
| vaccination_study_04 | Myeloid_lineage | 9 | 2,425 | Plasmacytoid DC | True | 2.594 | Plasmacytoid DC | nan | nan | registry__plasmacytoid_dc | pass |
| vaccination_study_04 | Myeloid_lineage | 6 | 1,089 | Conventional DC 1 | True | 2.135 | Intermediate Monocyte | nan | nan | registry__conventional_dc_1 | pass |
| vaccination_study_04 | T_NK_lineage | 0 | 38 | T Cell | False | 0.236 | gdT Cell | 0.000 | 0.000 | gdT | critical |
| vaccination_study_04 | T_NK_lineage | 1 | 37 | NK Cell | True | 0.845 | NK Cell | 0.000 | 0.000 | registry__nk_cell | pass |
| vaccination_study_04 | T_NK_lineage | 2 | 35 | NK Cell | True | 0.395 | CD8 Naive / T Central Memory | 0.000 | 0.000 | registry__nk_cell | pass |
| vaccination_study_04 | T_NK_lineage | 3 | 33 | NK Cell | True | 2.495 | NK Cell | 0.000 | 0.000 | registry__nk_cell | pass |
| vaccination_study_04 | T_NK_lineage | 4 | 33 | NK Cell | True | 2.451 | NK Cell | 0.000 | 0.000 | registry__nk_cell | pass |
| vaccination_study_04 | T_NK_lineage | 5 | 33 | NK Cell | True | 2.503 | NK Cell | 0.000 | 0.000 | registry__nk_cell | pass |
| vaccination_study_04 | T_NK_lineage | 6 | 31 | NK Cell | True | 1.768 | NKT Cell | 0.000 | 0.000 | registry__nk_cell | pass |
| vaccination_study_04 | T_NK_lineage | 7 | 28 | NK Cell | True | 2.349 | NKT Cell | 0.000 | 0.000 | registry__nk_cell | pass |
| vaccination_study_04 | T_NK_lineage | 8 | 28 | CD4 Naive / T Central Memory | True | 2.218 | CD4 Naive / T Central Memory | 0.036 | 0.000 | CD4_naive_tcm | pass |
| vaccination_study_04 | T_NK_lineage | 9 | 26 | T Cell | False | 0.185 | gdT Cell | 0.000 | 0.000 | gdT | critical |

## 出力ファイル

- Submission TSVs: `outputs/submission_v25_harmony_reference_rescue/vaccination_study_04/submissions/`
- cellxgene H5ADs: `outputs/submission_v25_harmony_reference_rescue/vaccination_study_04/cellxgene/`
- Marker availability table: `outputs/submission_v25_harmony_reference_rescue/vaccination_study_04/tables/marker_gene_availability.tsv`
- Marker availability alerts: `outputs/submission_v25_harmony_reference_rescue/vaccination_study_04/tables/marker_gene_availability_alerts.tsv`
- Subcluster evidence: `outputs/submission_v25_harmony_reference_rescue/vaccination_study_04/tables/lineage_subcluster_evidence.tsv.gz`
- Source disagreement summary: `outputs/submission_v25_harmony_reference_rescue/vaccination_study_04/tables/source_disagreement_summary.tsv`
- Source effectiveness summary: `outputs/submission_v25_harmony_reference_rescue/vaccination_study_04/tables/source_effectiveness_summary.tsv`
- Diagnostics tables: `outputs/submission_v25_harmony_reference_rescue/vaccination_study_04/tables/`

