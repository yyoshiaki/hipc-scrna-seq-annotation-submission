# HIPC データセットアノテーションレポート: vaccination_study_06

更新日: 2026-06-15 EDT

このレポートは `hipc-annotation` Codex workflow によって生成したデータセット別レビュー文書です。固定 method は repository README に置き、このレポートでは実際の evidence、弱い箇所、レビュー優先度、UMAP / dotplot を確認します。

## データセット概要

| study | cells | analysis_X_genes | pre_hvg_genes | counts_layer_genes | labels | parent_or_blood_fraction | Blood Cell | Doublet | artifact_like | median_confidence | low_confidence | source_disagreement | invalid_labels |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| vaccination_study_06 | 57,419 | 11,878 | 11,878 | 11,878 | 14 | 0.023 | 821 | 1,502 | 0 | 0.785 | 12,276 | 18,710 (0.326) | none |

## 実行概要

- 実行単位: one dataset in, one annotated dataset out。
- 実行経路: Codex skill `hipc-annotation` -> bundled helper `run_one.sh` -> annotation CLI -> validator -> report inspection。
- 検証: submission row count、H5AD observation count、official label validity、H5AD/submission agreement、confidence column、report image link を確認する。
- このレポートは workflow の再掲ではなく、このデータセットの marker 欠損、UMAP、label 構成、review concern を読むためのもの。

## データセット固有の解釈

- `vaccination_study_06`: 57,419 cells、analysis X/var 11,878 genes、pre-HVG slot 11,878 genes、submitted label 14 種、parent/Blood residual fraction 0.023、median confidence 0.785。
  - 12,276 cells は low confidence。QC / confidence UMAP 上で局在を確認する。
  - 1,502 cells は `Doublet` として提出。mixed-lineage marker expression と scrublet support を確認する。
  - 821 cells は `Blood Cell` として残存。これは filter-out ではなく、曖昧な細胞を公式 parent label で残したもの。
  - Marker gene 欠損アラート: Treg, Plasma_ASC。該当 marker set に依存する fine label は慎重に見る。

## データセット固有の評価

- 全体像: 57,419 cells / analysis X/var 11,878 genes / pre-HVG slot 11,878 genes。parent/Blood residual は 0.023、low-confidence は 12,276 cells、source disagreement flag は 18,710 cells (0.326)。
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
| vaccination_study_06 | Myeloid Cell | 256 | 0.000 | 256 | 1.000 |
| vaccination_study_06 | Intermediate Monocyte | 48 | 0.000 | 48 | 1.000 |
| vaccination_study_06 | Conventional DC 2 | 77 | 0.000 | 74 | 0.961 |
| vaccination_study_06 | Classical Monocyte | 23 | 0.250 | 22 | 0.957 |
| vaccination_study_06 | Naive B Cell | 840 | 0.200 | 770 | 0.917 |
| vaccination_study_06 | B Cell | 221 | 0.000 | 196 | 0.887 |
| vaccination_study_06 | Memory B Cell | 2,801 | 0.400 | 2,335 | 0.834 |
| vaccination_study_06 | Blood Cell | 821 | 0.250 | 648 | 0.789 |
| vaccination_study_06 | MAIT Cell | 2,455 | 0.000 | 1,551 | 0.632 |
| vaccination_study_06 | CD4 Naive / T Central Memory | 33,258 | 0.600 | 8,075 | 0.243 |
| vaccination_study_06 | NK Cell | 11,640 | 0.750 | 2,647 | 0.227 |

## アノテーションソース効果

この表は外部 ground truth に対する正解率ではありません。各 annotation source がどれだけの細胞で情報を持ち、final label とどれだけ一致したかを示す監査用統計です。`coverage` は source が `not_available` 以外を返した割合、`final_concordance` は informative cells の中で final label と一致した割合、`unique_support` はその source だけが final label と一致した細胞数です。

| study | source | informative_cells | coverage | final_concordance | high_conf_concordance | unique_support | discordant |
| --- | --- | --- | --- | --- | --- | --- | --- |
| vaccination_study_06 | Cluster consensus | 57,419 | 1.000 | 0.726 | 0.907 | 558 | 15,745 |
| vaccination_study_06 | CellTypist | 57,419 | 1.000 | 0.600 | 0.745 | 421 | 22,983 |
| vaccination_study_06 | Azimuth PBMC L2 | 57,419 | 1.000 | 0.525 | 0.657 | 229 | 27,284 |
| vaccination_study_06 | Pan-human Azimuth | 57,419 | 1.000 | 0.385 | 0.445 | 897 | 35,337 |
| vaccination_study_06 | Azimuth PBMC L3 | 57,419 | 1.000 | 0.098 | 0.124 | 131 | 51,812 |
| vaccination_study_06 | Cluster marker assignment | 54,858 | 0.955 | 0.828 | 1.000 | 3,968 | 9,423 |
| vaccination_study_06 | scRefMapping | 32,412 | 0.564 | 0.807 | 0.932 | 79 | 6,260 |

## レビュー優先事項

| study | concern | cells |
| --- | --- | --- |
| vaccination_study_06 | High source disagreement for B Cell | 196 |
| vaccination_study_06 | High source disagreement for Blood Cell | 648 |
| vaccination_study_06 | High source disagreement for Classical Monocyte | 22 |
| vaccination_study_06 | High source disagreement for Conventional DC 2 | 74 |
| vaccination_study_06 | High source disagreement for Doublet | 1,502 |
| vaccination_study_06 | High source disagreement for Intermediate Monocyte | 48 |
| vaccination_study_06 | High source disagreement for MAIT Cell | 1,551 |
| vaccination_study_06 | High source disagreement for Memory B Cell | 2,335 |
| vaccination_study_06 | High source disagreement for Myeloid Cell | 256 |
| vaccination_study_06 | High source disagreement for Naive B Cell | 770 |
| vaccination_study_06 | High dataset-level source disagreement | 18,710 |
| vaccination_study_06 | Many low-confidence cells; QC or mixed-marker effects likely remain | 12,276 |

## ラベル構成

| study | predicted_cell_type | cells |
| --- | --- | --- |
| vaccination_study_06 | CD4 Naive / T Central Memory | 33,258 |
| vaccination_study_06 | NK Cell | 11,640 |
| vaccination_study_06 | CD8 Cytotoxic / T Effector Memory | 3,476 |
| vaccination_study_06 | Memory B Cell | 2,801 |
| vaccination_study_06 | MAIT Cell | 2,455 |
| vaccination_study_06 | Doublet | 1,502 |
| vaccination_study_06 | Naive B Cell | 840 |
| vaccination_study_06 | Blood Cell | 821 |
| vaccination_study_06 | Myeloid Cell | 256 |
| vaccination_study_06 | B Cell | 221 |
| vaccination_study_06 | Conventional DC 2 | 77 |
| vaccination_study_06 | Intermediate Monocyte | 48 |
| vaccination_study_06 | Classical Monocyte | 23 |
| vaccination_study_06 | CD8 Naive / T Central Memory | 1 |

## Inline Figures

### vaccination_study_06

![vaccination_study_06 final labels](assets/umap_vaccination_study_06_annotation_label.png)

![vaccination_study_06 lineage and annotation reason](assets/umap_vaccination_study_06_annotation_lineage_reason.png)

![vaccination_study_06 QC and confidence](assets/umap_vaccination_study_06_annotation_qc_confidence.png)

![vaccination_study_06 source agreement and disagreement](assets/umap_vaccination_study_06_annotation_source_disagreement.png)

![vaccination_study_06 annotation-source effectiveness](assets/figure_02_source_effectiveness.png)

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

![vaccination_study_06 Myeloid_lineage true subcluster labels](assets/umap_vaccination_study_06_Myeloid_lineage_true_subcluster_label.png)

![vaccination_study_06 Myeloid_lineage true subcluster source labels](assets/umap_vaccination_study_06_Myeloid_lineage_true_subcluster_source_labels.png)

![vaccination_study_06 Myeloid_lineage true subcluster QC](assets/umap_vaccination_study_06_Myeloid_lineage_true_subcluster_qc.png)

![vaccination_study_06 Myeloid_lineage true subcluster marker scores](assets/umap_vaccination_study_06_Myeloid_lineage_true_subcluster_marker_scores.png)

![vaccination_study_06 Myeloid_lineage true subcluster marker expression](assets/umap_vaccination_study_06_Myeloid_lineage_true_subcluster_marker_expression.png)

![vaccination_study_06 Myeloid_lineage subcluster marker score heatmap](assets/subcluster_marker_score_heatmap_vaccination_study_06_Myeloid_lineage.png)

![vaccination_study_06 Myeloid_lineage subcluster marker dotplot](assets/dotplot_vaccination_study_06_Myeloid_lineage_true_subcluster_marker_dotplot.png)

Tables: `tables/vaccination_study_06_Myeloid_lineage_true_subcluster_umap.tsv.gz`, `tables/vaccination_study_06_Myeloid_lineage_subcluster_candidate_scores.tsv`.


## Subcluster Marker Score Review

上の lineage-specific panel は、各 lineage subset で HVG 選択、PCA、neighbors、Leiden、UMAP を再計算した true local subcluster analysis から生成しています。Marker gene による fine label の確認は global UMAP だけではなく、この local UMAP、CellTypist/Azimuth/Pan-human/cluster-level marker gene assignment overlay、cluster marker gate score UMAP、marker-expression UMAP、dotplot を主に見ます。Treg など sparse marker label は cell-wise marker winner ではなく、local cluster の FOXP3/IL2RA/CTLA4 など key-marker support と reference support で判定します。

## Marker Assignment Feedback

Marker gene assignment は final label を強制的に上書きするものではなく、cluster-level の自己点検です。`raw_marker_winner` は marker score だけの勝者、`marker_assignment` は conservative policy と source-supported tie-break を通した marker-based assignment です。この表は marker assignment と final/reference-driven label がずれる cluster、marker specificity が弱い cluster、scRefMap が期待される lineage で欠落する cluster を示します。`marker_score` は raw marker base score から negative/confound marker penalty を差し引いた cluster-level marker gate score です。

| study | lineage | cluster | cells | chosen_label | marker_assignment | raw_marker_winner | assignment_reason | marker_score | base_score | penalty | flags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| vaccination_study_06 | T_NK_lineage | 7 | 6,539 | CD4 Naive / T Central Memory | NKT Cell | NKT Cell | raw_marker_winner | 0.420 | 0.525 | 0.105 | marker_final_disagreement |
| vaccination_study_06 | T_NK_lineage | 0 | 5,886 | NK Cell | NK Cell | NKT Cell | source_supported_marker_tiebreak | 0.818 | 0.911 | 0.093 | screfmapping_missing_for_scope |
| vaccination_study_06 | T_NK_lineage | 5 | 3,451 | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | NKT Cell | source_supported_marker_tiebreak | 0.678 | 1.000 | 0.322 | screfmapping_missing_for_scope |
| vaccination_study_06 | T_NK_lineage | 9 | 3,279 | NK Cell | NK Cell | NKT Cell | source_supported_marker_tiebreak | 0.921 | 1.000 | 0.079 | screfmapping_missing_for_scope |
| vaccination_study_06 | T_NK_lineage | 3 | 2,454 | MAIT Cell | MAIT Cell | NKT Cell | source_supported_marker_tiebreak | 0.737 | 1.000 | 0.263 | screfmapping_missing_for_scope |
| vaccination_study_06 | T_NK_lineage | 4 | 2,325 | NK Cell | NK Cell | NKT Cell | source_supported_marker_tiebreak | 0.893 | 1.000 | 0.107 | screfmapping_missing_for_scope |
| vaccination_study_06 | B_lineage | 0 | 325 | Memory B Cell | Naive B Cell | Naive B Cell | raw_marker_winner | 0.168 | 0.277 | 0.109 | marker_final_disagreement;weak_marker_specificity |
| vaccination_study_06 | B_lineage | 1 | 291 | Memory B Cell | Naive B Cell | Naive B Cell | raw_marker_winner | 0.237 | 0.299 | 0.062 | marker_final_disagreement;weak_marker_specificity |
| vaccination_study_06 | B_lineage | 2 | 286 | Memory B Cell | Naive B Cell | Naive B Cell | raw_marker_winner | 0.863 | 1.000 | 0.137 | marker_final_disagreement |
| vaccination_study_06 | B_lineage | 4 | 268 | Memory B Cell | Naive B Cell | Naive B Cell | raw_marker_winner | 0.578 | 0.829 | 0.251 | marker_final_disagreement |
| vaccination_study_06 | B_lineage | 5 | 265 | Naive B Cell | Naive B Cell | Naive B Cell | raw_marker_winner | 0.181 | 0.208 | 0.027 | weak_marker_specificity |
| vaccination_study_06 | B_lineage | 6 | 240 | Memory B Cell | Plasmablast | Plasmablast | raw_marker_winner | 0.155 | 0.747 | 0.592 | marker_final_disagreement;weak_marker_specificity |
| vaccination_study_06 | B_lineage | 7 | 236 | Memory B Cell | Naive B Cell | Naive B Cell | raw_marker_winner | 0.105 | 0.165 | 0.060 | marker_final_disagreement;weak_marker_specificity |
| vaccination_study_06 | B_lineage | 8 | 218 | B Cell | Plasma Cell | Plasma Cell | raw_marker_winner | 0.612 | 0.925 | 0.313 | marker_final_disagreement |
| vaccination_study_06 | B_lineage | 10 | 195 | Memory B Cell | Plasma Cell | Plasma Cell | raw_marker_winner | 0.000 | 0.415 | 0.526 | marker_final_disagreement;weak_marker_specificity |
| vaccination_study_06 | B_lineage | 11 | 174 | Memory B Cell | Naive B Cell | Naive B Cell | raw_marker_winner | 0.104 | 0.138 | 0.034 | marker_final_disagreement;weak_marker_specificity |
| vaccination_study_06 | B_lineage | 12 | 174 | Memory B Cell | Memory B Cell | Memory B Cell | raw_marker_winner | 0.283 | 0.452 | 0.169 | weak_marker_specificity |
| vaccination_study_06 | B_lineage | 13 | 172 | Memory B Cell | Memory B Cell | Memory B Cell | raw_marker_winner | 0.349 | 0.564 | 0.215 | weak_marker_specificity |
| vaccination_study_06 | B_lineage | 15 | 136 | Memory B Cell | Naive B Cell | Naive B Cell | raw_marker_winner | 0.149 | 0.228 | 0.079 | marker_final_disagreement;weak_marker_specificity |
| vaccination_study_06 | B_lineage | 16 | 103 | Memory B Cell | Plasmablast | Plasmablast | raw_marker_winner | 0.163 | 0.408 | 0.244 | marker_final_disagreement;weak_marker_specificity |

## LLM Review Queue

この表は Codex/LLM が読むための subcluster-level review queue です。LLM はこの evidence を読んで、final label が妥当か、ontology にちょうどよい label がないのか、registry / conservative policy を一般ルールとして更新すべきかを提案します。LLM の出力で per-cell label を直接書き換えず、採用する場合は registry/config を更新して deterministic pipeline を再実行します。

| study | lineage | cluster | cells | priority | reasons | suggested_action | final_label | marker_assignment | raw_marker_winner | score_margin |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| vaccination_study_06 | T_NK_lineage | 3 | 2,454 | high | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available;low_total_score_or_margin | evaluate_ontology_gap_or_conservative_policy | MAIT Cell | MAIT Cell | NKT Cell | 0.020 |
| vaccination_study_06 | B_lineage | 8 | 218 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available | check_if_finer_official_label_is_supported | B Cell | Plasma Cell | Plasma Cell | 0.766 |
| vaccination_study_06 | Myeloid_lineage | 0 | 57 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | Myeloid Cell | Conventional DC 2 | Conventional DC 2 | 0.247 |
| vaccination_study_06 | Myeloid_lineage | 1 | 54 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | Myeloid Cell | Conventional DC 2 | Conventional DC 2 | 0.329 |
| vaccination_study_06 | Myeloid_lineage | 4 | 35 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | Myeloid Cell | Intermediate Monocyte | Intermediate Monocyte | 0.079 |
| vaccination_study_06 | Myeloid_lineage | 10 | 17 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | Myeloid Cell | Conventional DC 2 | Conventional DC 2 | 0.459 |
| vaccination_study_06 | Myeloid_lineage | 11 | 9 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | Myeloid Cell | Conventional DC 2 | Conventional DC 2 | 0.011 |
| vaccination_study_06 | Myeloid_lineage | 12 | 3 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | Myeloid Cell | Conventional DC 2 | Conventional DC 2 | 0.092 |
| vaccination_study_06 | T_NK_lineage | 7 | 6,539 | high | marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | CD4 Naive / T Central Memory | NKT Cell | NKT Cell | 0.502 |
| vaccination_study_06 | Myeloid_lineage | 9 | 22 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;low_total_score_or_margin | check_if_finer_official_label_is_supported | Myeloid Cell | Conventional DC 2 | Conventional DC 2 | 0.036 |
| vaccination_study_06 | T_NK_lineage | 0 | 5,886 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | NK Cell | NK Cell | NKT Cell | 0.772 |
| vaccination_study_06 | T_NK_lineage | 5 | 3,451 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | NKT Cell | 1.611 |
| vaccination_study_06 | T_NK_lineage | 9 | 3,279 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | NK Cell | NK Cell | NKT Cell | 2.374 |
| vaccination_study_06 | T_NK_lineage | 4 | 2,325 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | NK Cell | NK Cell | NKT Cell | 2.057 |
| vaccination_study_06 | Myeloid_lineage | 5 | 30 | medium | parent_or_broad_final_label;marker_assignment_disagrees_with_final;screfmapping_not_available | check_if_finer_official_label_is_supported | Myeloid Cell | Intermediate Monocyte | Intermediate Monocyte | 0.111 |
| vaccination_study_06 | Myeloid_lineage | 7 | 29 | medium | parent_or_broad_final_label;marker_assignment_disagrees_with_final;screfmapping_not_available | check_if_finer_official_label_is_supported | Myeloid Cell | Intermediate Monocyte | Intermediate Monocyte | 0.112 |
| vaccination_study_06 | B_lineage | 16 | 103 | medium | marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | Memory B Cell | Plasmablast | Plasmablast | 0.450 |
| vaccination_study_06 | B_lineage | 6 | 240 | medium | marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate | evaluate_ontology_gap_or_conservative_policy | Memory B Cell | Plasmablast | Plasmablast | 2.794 |
| vaccination_study_06 | B_lineage | 10 | 195 | medium | marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate | evaluate_ontology_gap_or_conservative_policy | Memory B Cell | Plasma Cell | Plasma Cell | 2.195 |
| vaccination_study_06 | B_lineage | 0 | 325 | low | marker_assignment_disagrees_with_final | review_marker_vs_reference_disagreement | Memory B Cell | Naive B Cell | Naive B Cell | 1.180 |

## Cluster Consensus Evidence

| study | lineage | cluster | cells | chosen_label | accepted | score_margin | cluster_marker_assignment | treg_key_any | treg_key_bonus | marker_set | marker_alert |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| vaccination_study_06 | B_lineage | 0 | 325 | Memory B Cell | True | 1.180 | Naive B Cell | nan | nan | B_memory_ABC | pass |
| vaccination_study_06 | B_lineage | 1 | 291 | Memory B Cell | True | 2.681 | Naive B Cell | nan | nan | B_memory_ABC | pass |
| vaccination_study_06 | B_lineage | 2 | 286 | Memory B Cell | True | 0.381 | Naive B Cell | nan | nan | B_memory_ABC | pass |
| vaccination_study_06 | B_lineage | 3 | 284 | Naive B Cell | True | 0.191 | Naive B Cell | nan | nan | B_naive | pass |
| vaccination_study_06 | B_lineage | 4 | 268 | Memory B Cell | True | 1.126 | Naive B Cell | nan | nan | B_memory_ABC | pass |
| vaccination_study_06 | B_lineage | 5 | 265 | Naive B Cell | True | 0.118 | Naive B Cell | nan | nan | B_naive | pass |
| vaccination_study_06 | B_lineage | 6 | 240 | Memory B Cell | True | 2.794 | Plasmablast | nan | nan | B_memory_ABC | pass |
| vaccination_study_06 | B_lineage | 7 | 236 | Memory B Cell | True | 2.876 | Naive B Cell | nan | nan | B_memory_ABC | pass |
| vaccination_study_06 | B_lineage | 8 | 218 | B Cell | False | 0.766 | Plasma Cell | nan | nan | Plasma_ASC | warning |
| vaccination_study_06 | B_lineage | 9 | 207 | Naive B Cell | True | 1.411 | Naive B Cell | nan | nan | B_naive | pass |
| vaccination_study_06 | B_lineage | 10 | 195 | Memory B Cell | True | 2.195 | Plasma Cell | nan | nan | B_memory_ABC | pass |
| vaccination_study_06 | B_lineage | 11 | 174 | Memory B Cell | True | 2.054 | Naive B Cell | nan | nan | B_memory_ABC | pass |
| vaccination_study_06 | B_lineage | 12 | 174 | Memory B Cell | True | 2.566 | Memory B Cell | nan | nan | B_memory_ABC | pass |
| vaccination_study_06 | B_lineage | 13 | 172 | Memory B Cell | True | 3.247 | Memory B Cell | nan | nan | B_memory_ABC | pass |
| vaccination_study_06 | B_lineage | 14 | 144 | Memory B Cell | True | 2.176 | Memory B Cell | nan | nan | B_memory_ABC | pass |
| vaccination_study_06 | B_lineage | 15 | 136 | Memory B Cell | True | 1.795 | Naive B Cell | nan | nan | B_memory_ABC | pass |
| vaccination_study_06 | B_lineage | 16 | 103 | Memory B Cell | True | 0.450 | Plasmablast | nan | nan | B_memory_ABC | pass |
| vaccination_study_06 | B_lineage | 17 | 84 | Naive B Cell | True | 0.623 | Naive B Cell | nan | nan | B_naive | pass |
| vaccination_study_06 | B_lineage | 18 | 56 | Memory B Cell | True | 2.818 | Naive B Cell | nan | nan | B_memory_ABC | pass |
| vaccination_study_06 | Myeloid_lineage | 0 | 57 | Myeloid Cell | False | 0.247 | Conventional DC 2 | nan | nan | registry__conventional_dc_2 | pass |
| vaccination_study_06 | Myeloid_lineage | 1 | 54 | Myeloid Cell | False | 0.329 | Conventional DC 2 | nan | nan | registry__conventional_dc_2 | pass |
| vaccination_study_06 | Myeloid_lineage | 2 | 48 | Intermediate Monocyte | True | 0.158 | Intermediate Monocyte | nan | nan | registry__intermediate_monocyte | pass |
| vaccination_study_06 | Myeloid_lineage | 3 | 47 | Conventional DC 2 | True | 0.656 | Intermediate Monocyte | nan | nan | registry__conventional_dc_2 | pass |
| vaccination_study_06 | Myeloid_lineage | 4 | 35 | Myeloid Cell | False | 0.079 | Intermediate Monocyte | nan | nan | registry__intermediate_monocyte | pass |
| vaccination_study_06 | Myeloid_lineage | 5 | 30 | Myeloid Cell | False | 0.111 | Intermediate Monocyte | nan | nan | registry__intermediate_monocyte | pass |
| vaccination_study_06 | Myeloid_lineage | 6 | 30 | Conventional DC 2 | True | 0.927 | Intermediate Monocyte | nan | nan | registry__conventional_dc_2 | pass |
| vaccination_study_06 | Myeloid_lineage | 7 | 29 | Myeloid Cell | False | 0.112 | Intermediate Monocyte | nan | nan | registry__intermediate_monocyte | pass |
| vaccination_study_06 | Myeloid_lineage | 8 | 23 | Classical Monocyte | True | 0.266 | Intermediate Monocyte | nan | nan | registry__classical_monocyte | pass |
| vaccination_study_06 | Myeloid_lineage | 9 | 22 | Myeloid Cell | False | 0.036 | Conventional DC 2 | nan | nan | registry__conventional_dc_2 | pass |
| vaccination_study_06 | Myeloid_lineage | 10 | 17 | Myeloid Cell | False | 0.459 | Conventional DC 2 | nan | nan | registry__conventional_dc_2 | pass |

## 出力ファイル

- Submission TSVs: `outputs/submission_v25_harmony_reference_rescue/vaccination_study_06/submissions/`
- cellxgene H5ADs: `outputs/submission_v25_harmony_reference_rescue/vaccination_study_06/cellxgene/`
- Marker availability table: `outputs/submission_v25_harmony_reference_rescue/vaccination_study_06/tables/marker_gene_availability.tsv`
- Marker availability alerts: `outputs/submission_v25_harmony_reference_rescue/vaccination_study_06/tables/marker_gene_availability_alerts.tsv`
- Subcluster evidence: `outputs/submission_v25_harmony_reference_rescue/vaccination_study_06/tables/lineage_subcluster_evidence.tsv.gz`
- Source disagreement summary: `outputs/submission_v25_harmony_reference_rescue/vaccination_study_06/tables/source_disagreement_summary.tsv`
- Source effectiveness summary: `outputs/submission_v25_harmony_reference_rescue/vaccination_study_06/tables/source_effectiveness_summary.tsv`
- Diagnostics tables: `outputs/submission_v25_harmony_reference_rescue/vaccination_study_06/tables/`

