# HIPC データセットアノテーションレポート: vaccination_study_06

更新日: 2026-06-12 EDT

## 現行提出用サマリー

| 項目 | 内容 |
| --- | --- |
| 提出候補 package | v24 pragmatic package |
| 採用 source | `outputs/submission_final_v22/vaccination_study_06/submissions/vaccination_study_06_annotation.tsv` |
| 細胞数 | 57,419 |
| label 数 | 12 |
| parent/Blood residual | 1,215 cells (0.0212) |
| median confidence | 0.7724 |
| 上位 label | CD4 Naive / T Central Memory: 29,818; CD8 Cytotoxic / T Effector Memory: 10,013; NK Cell: 9,877; Memory B Cell: 2,547; Doublet: 2,162; MAIT Cell: 1,538; Blood Cell: 746; Myeloid Cell: 468 |
| 現状判断 | 提出候補として概ね良好。T/NK dominant dataset として、T subset の粗さと doublet marker を個別 UMAP で確認する。 |

このレポートは `hipc-annotation` Codex workflow によって生成したデータセット別レビュー文書です。固定 method は repository README に置き、このレポートでは実際の evidence、弱い箇所、レビュー優先度、UMAP / dotplot を確認します。

## データセット概要

| study | cells | analysis_X_genes | pre_hvg_genes | counts_layer_genes | labels | parent_or_blood_fraction | Blood Cell | Doublet | artifact_like | median_confidence | low_confidence | source_disagreement | invalid_labels |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| vaccination_study_06 | 57,419 | 11,878 | 11,878 | 11,878 | 12 | 0.021 | 746 | 2,162 | 0 | 0.772 | 3,430 | 14,569 (0.254) | none |

## 実行概要

- 実行単位: one dataset in, one annotated dataset out。
- 実行経路: Codex skill `hipc-annotation` -> bundled helper `run_one.sh` -> annotation CLI -> validator -> report inspection。
- 検証: submission row count、H5AD observation count、official label validity、H5AD/submission agreement、confidence column、report image link を確認する。
- このレポートは workflow の再掲ではなく、このデータセットの marker 欠損、UMAP、label 構成、review concern を読むためのもの。

## データセット固有の解釈

- `vaccination_study_06`: 57,419 cells、analysis X/var 11,878 genes、pre-HVG slot 11,878 genes、submitted label 12 種、parent/Blood residual fraction 0.021、median confidence 0.772。
  - 3,430 cells は low confidence。QC / confidence UMAP 上で局在を確認する。
  - 2,162 cells は `Doublet` として提出。mixed-lineage marker expression と scrublet support を確認する。
  - 746 cells は `Blood Cell` として残存。これは filter-out ではなく、曖昧な細胞を公式 parent label で残したもの。
  - Marker gene 欠損アラート: Treg, Plasma_ASC。該当 marker set に依存する fine label は慎重に見る。

## データセット固有の評価

- 全体像: 57,419 cells / analysis X/var 11,878 genes / pre-HVG slot 11,878 genes。parent/Blood residual は 0.021、low-confidence は 3,430 cells、source disagreement flag は 14,569 cells (0.254)。
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
| vaccination_study_06 | Doublet | 2,162 | 0.000 | 2,162 | 1.000 |
| vaccination_study_06 | Blood Cell | 746 | 0.000 | 746 | 1.000 |
| vaccination_study_06 | Myeloid Cell | 468 | 0.000 | 468 | 1.000 |
| vaccination_study_06 | Non-Classical Monocyte | 54 | 0.000 | 54 | 1.000 |
| vaccination_study_06 | Intermediate Monocyte | 20 | 0.333 | 20 | 1.000 |
| vaccination_study_06 | Naive B Cell | 175 | 0.250 | 116 | 0.663 |
| vaccination_study_06 | Memory B Cell | 2,547 | 0.500 | 1,059 | 0.416 |
| vaccination_study_06 | CD8 Cytotoxic / T Effector Memory | 10,013 | 0.667 | 3,381 | 0.338 |
| vaccination_study_06 | MAIT Cell | 1,538 | 0.667 | 475 | 0.309 |
| vaccination_study_06 | CD4 Naive / T Central Memory | 29,818 | 0.750 | 5,073 | 0.170 |
| vaccination_study_06 | NK Cell | 9,877 | 1.000 | 1,015 | 0.103 |
| vaccination_study_06 | B Cell | 1 | 0.750 | 0 | 0.000 |

## アノテーションソース効果

この表は外部 ground truth に対する正解率ではありません。各 annotation source がどれだけの細胞で情報を持ち、final label とどれだけ一致したかを示す監査用統計です。`coverage` は source が `not_available` 以外を返した割合、`final_concordance` は informative cells の中で final label と一致した割合、`unique_support` はその source だけが final label と一致した細胞数です。

| study | source | informative_cells | coverage | final_concordance | high_conf_concordance | unique_support | discordant |
| --- | --- | --- | --- | --- | --- | --- | --- |
| vaccination_study_06 | Cluster consensus | 57,419 | 1.000 | 0.720 | 0.792 | 99 | 16,100 |
| vaccination_study_06 | CellTypist | 57,419 | 1.000 | 0.687 | 0.773 | 54 | 17,999 |
| vaccination_study_06 | Pan-human Azimuth | 57,419 | 1.000 | 0.412 | 0.401 | 1,093 | 33,768 |
| vaccination_study_06 | Cluster marker assignment | 54,408 | 0.948 | 0.949 | 1.000 | 4,536 | 2,768 |
| vaccination_study_06 | scRefMapping | 30,889 | 0.538 | 0.777 | 0.914 | 9 | 6,879 |

## レビュー優先事項

| study | concern | cells |
| --- | --- | --- |
| vaccination_study_06 | High source disagreement for Blood Cell | 746 |
| vaccination_study_06 | High source disagreement for Doublet | 2,162 |
| vaccination_study_06 | High source disagreement for Intermediate Monocyte | 20 |
| vaccination_study_06 | High source disagreement for Myeloid Cell | 468 |
| vaccination_study_06 | High source disagreement for Naive B Cell | 116 |
| vaccination_study_06 | High source disagreement for Non-Classical Monocyte | 54 |
| vaccination_study_06 | High dataset-level source disagreement | 14,569 |

## ラベル構成

| study | predicted_cell_type | cells |
| --- | --- | --- |
| vaccination_study_06 | CD4 Naive / T Central Memory | 29,818 |
| vaccination_study_06 | CD8 Cytotoxic / T Effector Memory | 10,013 |
| vaccination_study_06 | NK Cell | 9,877 |
| vaccination_study_06 | Memory B Cell | 2,547 |
| vaccination_study_06 | Doublet | 2,162 |
| vaccination_study_06 | MAIT Cell | 1,538 |
| vaccination_study_06 | Blood Cell | 746 |
| vaccination_study_06 | Myeloid Cell | 468 |
| vaccination_study_06 | Naive B Cell | 175 |
| vaccination_study_06 | Non-Classical Monocyte | 54 |
| vaccination_study_06 | Intermediate Monocyte | 20 |
| vaccination_study_06 | B Cell | 1 |

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
| vaccination_study_06 | T_NK_lineage | 2 | 3,407 | CD4 Naive / T Central Memory | CD4 Naive / T Central Memory | NKT Cell | conservative_policy_blocks_raw_marker_winner | 0.314 | 0.358 | 0.044 | weak_marker_specificity |
| vaccination_study_06 | T_NK_lineage | 3 | 3,230 | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | NKT Cell | conservative_policy_blocks_raw_marker_winner | 0.664 | 1.000 | 0.336 | screfmapping_missing_for_scope |
| vaccination_study_06 | T_NK_lineage | 5 | 3,181 | NK Cell | NK Cell | NKT Cell | conservative_policy_blocks_raw_marker_winner | 0.921 | 1.000 | 0.079 | screfmapping_missing_for_scope |
| vaccination_study_06 | T_NK_lineage | 6 | 2,915 | NK Cell | NK Cell | NKT Cell | conservative_policy_blocks_raw_marker_winner | 0.860 | 0.907 | 0.047 | screfmapping_missing_for_scope |
| vaccination_study_06 | T_NK_lineage | 7 | 2,893 | CD4 Naive / T Central Memory | CD4 Naive / T Central Memory | NKT Cell | conservative_policy_blocks_raw_marker_winner | 0.319 | 0.377 | 0.057 | weak_marker_specificity |
| vaccination_study_06 | T_NK_lineage | 14 | 2,123 | NK Cell | NK Cell | NKT Cell | conservative_policy_blocks_raw_marker_winner | 0.916 | 1.000 | 0.084 | screfmapping_missing_for_scope |
| vaccination_study_06 | T_NK_lineage | 15 | 1,538 | MAIT Cell | MAIT Cell | NKT Cell | conservative_policy_blocks_raw_marker_winner | 0.778 | 1.000 | 0.222 | screfmapping_missing_for_scope |
| vaccination_study_06 | T_NK_lineage | 16 | 1,460 | NK Cell | NK Cell | NKT Cell | conservative_policy_blocks_raw_marker_winner | 0.848 | 0.918 | 0.070 | screfmapping_missing_for_scope |
| vaccination_study_06 | T_NK_lineage | 18 | 894 | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | NKT Cell | conservative_policy_blocks_raw_marker_winner | 0.582 | 1.000 | 0.418 | screfmapping_missing_for_scope |
| vaccination_study_06 | T_NK_lineage | 19 | 270 | CD4 Naive / T Central Memory | Treg | Treg | raw_marker_winner | 0.519 | 1.000 | 0.481 | marker_final_disagreement |
| vaccination_study_06 | B_lineage | 0 | 219 | Memory B Cell | Memory B Cell | Memory B Cell | raw_marker_winner | 0.348 | 0.533 | 0.185 | weak_marker_specificity |
| vaccination_study_06 | B_lineage | 1 | 211 | Memory B Cell | Naive B Cell | Naive B Cell | raw_marker_winner | 0.769 | 0.942 | 0.174 | marker_final_disagreement |
| vaccination_study_06 | B_lineage | 2 | 179 | Memory B Cell | Naive B Cell | Naive B Cell | raw_marker_winner | 0.163 | 0.201 | 0.038 | marker_final_disagreement;weak_marker_specificity |
| vaccination_study_06 | B_lineage | 5 | 173 | Memory B Cell | Naive B Cell | Naive B Cell | raw_marker_winner | 0.218 | 0.318 | 0.099 | marker_final_disagreement;weak_marker_specificity |
| vaccination_study_06 | B_lineage | 6 | 165 | Memory B Cell | Naive B Cell | Naive B Cell | raw_marker_winner | 0.084 | 0.139 | 0.055 | marker_final_disagreement;weak_marker_specificity |
| vaccination_study_06 | T_NK_lineage | 20 | 160 | NK Cell | NK Cell | NKT Cell | conservative_policy_blocks_raw_marker_winner | 0.952 | 1.000 | 0.048 | screfmapping_missing_for_scope |
| vaccination_study_06 | B_lineage | 7 | 144 | Memory B Cell | Naive B Cell | Naive B Cell | raw_marker_winner | 0.129 | 0.194 | 0.066 | marker_final_disagreement;weak_marker_specificity |
| vaccination_study_06 | B_lineage | 8 | 141 | Memory B Cell | Naive B Cell | Naive B Cell | raw_marker_winner | 0.293 | 0.355 | 0.062 | marker_final_disagreement;weak_marker_specificity |
| vaccination_study_06 | B_lineage | 9 | 135 | Memory B Cell | Naive B Cell | Naive B Cell | raw_marker_winner | 0.114 | 0.163 | 0.049 | marker_final_disagreement;weak_marker_specificity |
| vaccination_study_06 | B_lineage | 10 | 133 | Memory B Cell | Naive B Cell | Naive B Cell | raw_marker_winner | 0.086 | 0.263 | 0.177 | marker_final_disagreement;weak_marker_specificity |

## LLM Review Queue

この表は Codex/LLM が読むための subcluster-level review queue です。LLM はこの evidence を読んで、final label が妥当か、ontology にちょうどよい label がないのか、registry / conservative policy を一般ルールとして更新すべきかを提案します。LLM の出力で per-cell label を直接書き換えず、採用する場合は registry/config を更新して deterministic pipeline を再実行します。

| study | lineage | cluster | cells | priority | reasons | suggested_action | final_label | marker_assignment | raw_marker_winner | score_margin |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| vaccination_study_06 | Myeloid_lineage | 1 | 58 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;low_total_score_or_margin | check_if_finer_official_label_is_supported | Myeloid Cell | Intermediate Monocyte | Intermediate Monocyte | 0.049 |
| vaccination_study_06 | Myeloid_lineage | 6 | 45 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;low_total_score_or_margin | check_if_finer_official_label_is_supported | Myeloid Cell | Intermediate Monocyte | Intermediate Monocyte | 0.116 |
| vaccination_study_06 | T_NK_lineage | 3 | 3,230 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | NKT Cell | 2.223 |
| vaccination_study_06 | T_NK_lineage | 5 | 3,181 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | NK Cell | NK Cell | NKT Cell | 2.443 |
| vaccination_study_06 | T_NK_lineage | 6 | 2,915 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | NK Cell | NK Cell | NKT Cell | 2.099 |
| vaccination_study_06 | T_NK_lineage | 14 | 2,123 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | NK Cell | NK Cell | NKT Cell | 1.656 |
| vaccination_study_06 | T_NK_lineage | 15 | 1,538 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | MAIT Cell | MAIT Cell | NKT Cell | 1.387 |
| vaccination_study_06 | T_NK_lineage | 16 | 1,460 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | NK Cell | NK Cell | NKT Cell | 1.683 |
| vaccination_study_06 | Myeloid_lineage | 7 | 39 | medium | parent_or_broad_final_label;marker_assignment_disagrees_with_final;screfmapping_not_available | check_if_finer_official_label_is_supported | Myeloid Cell | Intermediate Monocyte | Intermediate Monocyte | 0.231 |
| vaccination_study_06 | Myeloid_lineage | 9 | 35 | medium | parent_or_broad_final_label;marker_assignment_disagrees_with_final;screfmapping_not_available | check_if_finer_official_label_is_supported | Myeloid Cell | Conventional DC 2 | Conventional DC 2 | 0.378 |
| vaccination_study_06 | T_NK_lineage | 2 | 3,407 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate | evaluate_ontology_gap_or_conservative_policy | CD4 Naive / T Central Memory | CD4 Naive / T Central Memory | NKT Cell | 2.947 |
| vaccination_study_06 | T_NK_lineage | 7 | 2,893 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate | evaluate_ontology_gap_or_conservative_policy | CD4 Naive / T Central Memory | CD4 Naive / T Central Memory | NKT Cell | 2.577 |
| vaccination_study_06 | T_NK_lineage | 18 | 894 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | NKT Cell | 2.496 |
| vaccination_study_06 | Myeloid_lineage | 0 | 83 | medium | parent_or_broad_final_label;marker_assignment_disagrees_with_final | check_if_finer_official_label_is_supported | Myeloid Cell | Intermediate Monocyte | Intermediate Monocyte | 0.276 |
| vaccination_study_06 | Myeloid_lineage | 2 | 57 | medium | parent_or_broad_final_label;marker_assignment_disagrees_with_final | check_if_finer_official_label_is_supported | Myeloid Cell | Intermediate Monocyte | Intermediate Monocyte | 0.113 |
| vaccination_study_06 | Myeloid_lineage | 3 | 55 | medium | parent_or_broad_final_label;marker_assignment_disagrees_with_final | check_if_finer_official_label_is_supported | Myeloid Cell | Intermediate Monocyte | Intermediate Monocyte | 0.159 |
| vaccination_study_06 | Myeloid_lineage | 5 | 47 | medium | parent_or_broad_final_label;marker_assignment_disagrees_with_final | check_if_finer_official_label_is_supported | Myeloid Cell | Intermediate Monocyte | Intermediate Monocyte | 0.148 |
| vaccination_study_06 | Myeloid_lineage | 8 | 38 | medium | parent_or_broad_final_label;marker_assignment_disagrees_with_final | check_if_finer_official_label_is_supported | Myeloid Cell | Intermediate Monocyte | Intermediate Monocyte | 0.306 |
| vaccination_study_06 | Myeloid_lineage | 11 | 11 | medium | parent_or_broad_final_label;marker_assignment_disagrees_with_final | check_if_finer_official_label_is_supported | Myeloid Cell | Intermediate Monocyte | Intermediate Monocyte | 0.466 |
| vaccination_study_06 | T_NK_lineage | 19 | 270 | medium | marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate | evaluate_ontology_gap_or_conservative_policy | CD4 Naive / T Central Memory | Treg | Treg | 1.081 |

## Cluster Consensus Evidence

| study | lineage | cluster | cells | chosen_label | accepted | score_margin | cluster_marker_assignment | treg_key_any | treg_key_bonus | marker_set | marker_alert |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| vaccination_study_06 | B_lineage | 0 | 219 | Memory B Cell | True | 3.144 | Memory B Cell | nan | nan | registry__memory_b_cell | pass |
| vaccination_study_06 | B_lineage | 1 | 211 | Memory B Cell | True | 1.527 | Naive B Cell | nan | nan | registry__memory_b_cell | pass |
| vaccination_study_06 | B_lineage | 2 | 179 | Memory B Cell | True | 1.533 | Naive B Cell | nan | nan | registry__memory_b_cell | pass |
| vaccination_study_06 | B_lineage | 3 | 178 | Memory B Cell | True | 2.647 | Memory B Cell | nan | nan | registry__memory_b_cell | pass |
| vaccination_study_06 | B_lineage | 4 | 175 | Naive B Cell | True | 0.141 | Naive B Cell | nan | nan | registry__naive_b_cell | pass |
| vaccination_study_06 | B_lineage | 5 | 173 | Memory B Cell | True | 2.407 | Naive B Cell | nan | nan | registry__memory_b_cell | pass |
| vaccination_study_06 | B_lineage | 6 | 165 | Memory B Cell | True | 1.647 | Naive B Cell | nan | nan | registry__memory_b_cell | pass |
| vaccination_study_06 | B_lineage | 7 | 144 | Memory B Cell | True | 2.082 | Naive B Cell | nan | nan | registry__memory_b_cell | pass |
| vaccination_study_06 | B_lineage | 8 | 141 | Memory B Cell | True | 1.422 | Naive B Cell | nan | nan | registry__memory_b_cell | pass |
| vaccination_study_06 | B_lineage | 9 | 135 | Memory B Cell | True | 1.948 | Naive B Cell | nan | nan | registry__memory_b_cell | pass |
| vaccination_study_06 | B_lineage | 10 | 133 | Memory B Cell | True | 2.103 | Naive B Cell | nan | nan | registry__memory_b_cell | pass |
| vaccination_study_06 | B_lineage | 11 | 133 | Memory B Cell | True | 0.812 | Naive B Cell | nan | nan | registry__memory_b_cell | pass |
| vaccination_study_06 | B_lineage | 12 | 117 | Memory B Cell | True | 1.832 | Naive B Cell | nan | nan | registry__memory_b_cell | pass |
| vaccination_study_06 | B_lineage | 13 | 90 | Memory B Cell | True | 2.628 | Naive B Cell | nan | nan | registry__memory_b_cell | pass |
| vaccination_study_06 | B_lineage | 14 | 84 | Memory B Cell | True | 3.019 | Memory B Cell | nan | nan | registry__memory_b_cell | pass |
| vaccination_study_06 | B_lineage | 15 | 78 | Memory B Cell | True | 2.279 | Naive B Cell | nan | nan | registry__memory_b_cell | pass |
| vaccination_study_06 | B_lineage | 16 | 76 | Memory B Cell | True | 2.328 | Naive B Cell | nan | nan | registry__memory_b_cell | pass |
| vaccination_study_06 | B_lineage | 17 | 69 | Memory B Cell | True | 1.454 | Naive B Cell | nan | nan | registry__memory_b_cell | pass |
| vaccination_study_06 | B_lineage | 18 | 63 | Memory B Cell | True | 2.565 | Naive B Cell | nan | nan | registry__memory_b_cell | pass |
| vaccination_study_06 | B_lineage | 19 | 53 | Memory B Cell | True | 1.860 | Naive B Cell | nan | nan | registry__memory_b_cell | pass |
| vaccination_study_06 | B_lineage | 20 | 42 | Memory B Cell | True | 2.037 | Naive B Cell | nan | nan | registry__memory_b_cell | pass |
| vaccination_study_06 | B_lineage | 21 | 28 | Memory B Cell | True | 1.930 | Naive B Cell | nan | nan | registry__memory_b_cell | pass |
| vaccination_study_06 | Myeloid_lineage | 0 | 83 | Myeloid Cell | False | 0.276 | Intermediate Monocyte | nan | nan | registry__intermediate_monocyte | pass |
| vaccination_study_06 | Myeloid_lineage | 1 | 58 | Myeloid Cell | False | 0.049 | Intermediate Monocyte | nan | nan | registry__intermediate_monocyte | pass |
| vaccination_study_06 | Myeloid_lineage | 2 | 57 | Myeloid Cell | False | 0.113 | Intermediate Monocyte | nan | nan | registry__intermediate_monocyte | pass |
| vaccination_study_06 | Myeloid_lineage | 3 | 55 | Myeloid Cell | False | 0.159 | Intermediate Monocyte | nan | nan | registry__intermediate_monocyte | pass |
| vaccination_study_06 | Myeloid_lineage | 4 | 54 | Non-Classical Monocyte | True | 0.604 | Non-Classical Monocyte | nan | nan | registry__non_classical_monocyte | pass |
| vaccination_study_06 | Myeloid_lineage | 5 | 47 | Myeloid Cell | False | 0.148 | Intermediate Monocyte | nan | nan | registry__intermediate_monocyte | pass |
| vaccination_study_06 | Myeloid_lineage | 6 | 45 | Myeloid Cell | False | 0.116 | Intermediate Monocyte | nan | nan | registry__intermediate_monocyte | pass |
| vaccination_study_06 | Myeloid_lineage | 7 | 39 | Myeloid Cell | False | 0.231 | Intermediate Monocyte | nan | nan | registry__intermediate_monocyte | pass |

## 出力ファイル

- Submission TSVs: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_final_v22/vaccination_study_06/submissions/`
- cellxgene H5ADs: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_final_v22/vaccination_study_06/cellxgene/`
- Marker availability table: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_final_v22/vaccination_study_06/tables/marker_gene_availability.tsv`
- Marker availability alerts: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_final_v22/vaccination_study_06/tables/marker_gene_availability_alerts.tsv`
- Subcluster evidence: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_final_v22/vaccination_study_06/tables/lineage_subcluster_evidence.tsv.gz`
- Source disagreement summary: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_final_v22/vaccination_study_06/tables/source_disagreement_summary.tsv`
- Source effectiveness summary: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_final_v22/vaccination_study_06/tables/source_effectiveness_summary.tsv`
- Diagnostics tables: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_final_v22/vaccination_study_06/tables/`
