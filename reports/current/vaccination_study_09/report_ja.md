# HIPC データセットアノテーションレポート: vaccination_study_09

更新日: 2026-06-15 EDT

このレポートは `hipc-annotation` Codex workflow によって生成したデータセット別レビュー文書です。固定 method は repository README に置き、このレポートでは実際の evidence、弱い箇所、レビュー優先度、UMAP / dotplot を確認します。

## データセット概要

| study | cells | analysis_X_genes | pre_hvg_genes | counts_layer_genes | labels | parent_or_blood_fraction | Blood Cell | Doublet | artifact_like | median_confidence | low_confidence | source_disagreement | invalid_labels |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| vaccination_study_09 | 139,960 | 19,141 | 19,141 | 19,141 | 18 | 0.009 | 1,238 | 579 | 121 | 0.788 | 1,837 | 20,296 (0.145) | none |

## 実行概要

- 実行単位: one dataset in, one annotated dataset out。
- 実行経路: Codex skill `hipc-annotation` -> bundled helper `run_one.sh` -> annotation CLI -> validator -> report inspection。
- 検証: submission row count、H5AD observation count、official label validity、H5AD/submission agreement、confidence column、report image link を確認する。
- このレポートは workflow の再掲ではなく、このデータセットの marker 欠損、UMAP、label 構成、review concern を読むためのもの。

## データセット固有の解釈

- `vaccination_study_09`: 139,960 cells、analysis X/var 19,141 genes、pre-HVG slot 19,141 genes、submitted label 18 種、parent/Blood residual fraction 0.009、median confidence 0.788。
  - 1,837 cells は low confidence。QC / confidence UMAP 上で局在を確認する。
  - 579 cells は `Doublet` として提出。mixed-lineage marker expression と scrublet support を確認する。
  - 1,238 cells は `Blood Cell` として残存。これは filter-out ではなく、曖昧な細胞を公式 parent label で残したもの。
  - Marker gene 欠損アラート: gdT, Plasma_ASC。該当 marker set に依存する fine label は慎重に見る。

## データセット固有の評価

- 全体像: 139,960 cells / analysis X/var 19,141 genes / pre-HVG slot 19,141 genes。parent/Blood residual は 0.009、low-confidence は 1,837 cells、source disagreement flag は 20,296 cells (0.145)。
- 優先確認: low-confidence 領域が QC UMAP と source-disagreement UMAP で同じ場所に集まるかを確認する。
- 優先確認: `Blood Cell` 残存が孤立 cluster なのか、複数 lineage に分散した曖昧領域なのかを UMAP で確認する。
- Marker gene 欠損: gdT, Plasma_ASC は confidence cap 対象。該当 label は marker expression UMAP と dotplot で妥当性を確認する。

## Marker Gene 欠損アラート

| study | marker_set | alert | present_fraction | missing_critical_markers | missing_genes |
| --- | --- | --- | --- | --- | --- |
| vaccination_study_09 | gdT | warning | 0.333 | TRDC;TRGC1;TRGC2 | TRDC;TRGC1;TRGC2;TRDV2 |
| vaccination_study_09 | Plasma_ASC | warning | 0.667 | JCHAIN | JCHAIN;IGHG1;IGHA1 |

## ソース間不一致

| study | predicted_cell_type | cells | median_source_agreement | disagreement_cells | disagreement_fraction |
| --- | --- | --- | --- | --- | --- |
| vaccination_study_09 | Doublet | 579 | 0.000 | 579 | 1.000 |
| vaccination_study_09 | B Cell | 20 | 0.000 | 20 | 1.000 |
| vaccination_study_09 | Plasma Cell | 425 | 0.200 | 267 | 0.628 |
| vaccination_study_09 | MAIT Cell | 6,316 | 0.500 | 2,466 | 0.390 |
| vaccination_study_09 | Blood Cell | 1,238 | 0.750 | 374 | 0.302 |
| vaccination_study_09 | CD8 Naive / T Central Memory | 11,778 | 0.500 | 3,488 | 0.296 |
| vaccination_study_09 | Classical Monocyte | 26,133 | 0.750 | 5,456 | 0.209 |
| vaccination_study_09 | CD8 Cytotoxic / T Effector Memory | 13,732 | 0.750 | 2,298 | 0.167 |
| vaccination_study_09 | Conventional DC 2 | 1,676 | 0.750 | 253 | 0.151 |
| vaccination_study_09 | Naive B Cell | 11,350 | 0.800 | 1,370 | 0.121 |
| vaccination_study_09 | Memory B Cell | 4,173 | 0.800 | 442 | 0.106 |
| vaccination_study_09 | Conventional DC 1 | 52 | 0.750 | 4 | 0.077 |

## アノテーションソース効果

この表は外部 ground truth に対する正解率ではありません。各 annotation source がどれだけの細胞で情報を持ち、final label とどれだけ一致したかを示す監査用統計です。`coverage` は source が `not_available` 以外を返した割合、`final_concordance` は informative cells の中で final label と一致した割合、`unique_support` はその source だけが final label と一致した細胞数です。

| study | source | informative_cells | coverage | final_concordance | high_conf_concordance | unique_support | discordant |
| --- | --- | --- | --- | --- | --- | --- | --- |
| vaccination_study_09 | Cluster consensus | 139,960 | 1.000 | 0.874 | 0.916 | 1,411 | 17,600 |
| vaccination_study_09 | CellTypist | 139,960 | 1.000 | 0.764 | 0.843 | 564 | 32,964 |
| vaccination_study_09 | Pan-human Azimuth | 139,960 | 1.000 | 0.726 | 0.830 | 312 | 38,301 |
| vaccination_study_09 | Azimuth PBMC L2 | 139,960 | 1.000 | 0.540 | 0.609 | 149 | 64,421 |
| vaccination_study_09 | Azimuth PBMC L3 | 139,960 | 1.000 | 0.200 | 0.181 | 10 | 111,959 |
| vaccination_study_09 | Cluster marker assignment | 137,977 | 0.986 | 0.838 | 0.837 | 2,673 | 22,361 |
| vaccination_study_09 | scRefMapping | 56,028 | 0.400 | 0.839 | 0.897 | 7 | 9,023 |

## レビュー優先事項

| study | concern | cells |
| --- | --- | --- |
| vaccination_study_09 | High source disagreement for B Cell | 20 |
| vaccination_study_09 | High source disagreement for Doublet | 579 |
| vaccination_study_09 | High source disagreement for Plasma Cell | 267 |
| vaccination_study_09 | warning marker availability for Plasma_ASC | 425 |
| vaccination_study_09 | Large Blood Cell/ambiguous residual remains | 1,238 |

## ラベル構成

| study | predicted_cell_type | cells |
| --- | --- | --- |
| vaccination_study_09 | CD4 Naive / T Central Memory | 49,118 |
| vaccination_study_09 | Classical Monocyte | 26,133 |
| vaccination_study_09 | CD8 Cytotoxic / T Effector Memory | 13,732 |
| vaccination_study_09 | CD8 Naive / T Central Memory | 11,778 |
| vaccination_study_09 | Naive B Cell | 11,350 |
| vaccination_study_09 | NK Cell | 9,374 |
| vaccination_study_09 | MAIT Cell | 6,316 |
| vaccination_study_09 | Memory B Cell | 4,173 |
| vaccination_study_09 | Non-Classical Monocyte | 3,072 |
| vaccination_study_09 | Conventional DC 2 | 1,676 |
| vaccination_study_09 | Blood Cell | 1,238 |
| vaccination_study_09 | Plasmacytoid DC | 803 |
| vaccination_study_09 | Doublet | 579 |
| vaccination_study_09 | Plasma Cell | 425 |
| vaccination_study_09 | Platelet | 84 |
| vaccination_study_09 | Conventional DC 1 | 52 |
| vaccination_study_09 | HSC | 37 |
| vaccination_study_09 | B Cell | 20 |

## Inline Figures

### vaccination_study_09

![vaccination_study_09 final labels](assets/umap_vaccination_study_09_annotation_label.png)

![vaccination_study_09 lineage and annotation reason](assets/umap_vaccination_study_09_annotation_lineage_reason.png)

![vaccination_study_09 QC and confidence](assets/umap_vaccination_study_09_annotation_qc_confidence.png)

![vaccination_study_09 source agreement and disagreement](assets/umap_vaccination_study_09_annotation_source_disagreement.png)

![vaccination_study_09 annotation-source effectiveness](assets/figure_02_source_effectiveness.png)

![vaccination_study_09 marker expression UMAPs](assets/umap_vaccination_study_09_annotation_marker_expression.png)

![vaccination_study_09 submitted-label marker dotplot](assets/dotplot_vaccination_study_09_annotation_marker_dotplot.png)

#### vaccination_study_09 B_lineage true subcluster UMAP

![vaccination_study_09 B_lineage true subcluster labels](assets/umap_vaccination_study_09_B_lineage_true_subcluster_label.png)

![vaccination_study_09 B_lineage true subcluster source labels](assets/umap_vaccination_study_09_B_lineage_true_subcluster_source_labels.png)

![vaccination_study_09 B_lineage true subcluster QC](assets/umap_vaccination_study_09_B_lineage_true_subcluster_qc.png)

![vaccination_study_09 B_lineage true subcluster marker scores](assets/umap_vaccination_study_09_B_lineage_true_subcluster_marker_scores.png)

![vaccination_study_09 B_lineage true subcluster marker expression](assets/umap_vaccination_study_09_B_lineage_true_subcluster_marker_expression.png)

![vaccination_study_09 B_lineage subcluster marker score heatmap](assets/subcluster_marker_score_heatmap_vaccination_study_09_B_lineage.png)

![vaccination_study_09 B_lineage subcluster marker dotplot](assets/dotplot_vaccination_study_09_B_lineage_true_subcluster_marker_dotplot.png)

Tables: `tables/vaccination_study_09_B_lineage_true_subcluster_umap.tsv.gz`, `tables/vaccination_study_09_B_lineage_subcluster_candidate_scores.tsv`.

#### vaccination_study_09 T_NK_lineage true subcluster UMAP

![vaccination_study_09 T_NK_lineage true subcluster labels](assets/umap_vaccination_study_09_T_NK_lineage_true_subcluster_label.png)

![vaccination_study_09 T_NK_lineage true subcluster source labels](assets/umap_vaccination_study_09_T_NK_lineage_true_subcluster_source_labels.png)

![vaccination_study_09 T_NK_lineage true subcluster QC](assets/umap_vaccination_study_09_T_NK_lineage_true_subcluster_qc.png)

![vaccination_study_09 T_NK_lineage true subcluster marker scores](assets/umap_vaccination_study_09_T_NK_lineage_true_subcluster_marker_scores.png)

![vaccination_study_09 T_NK_lineage true subcluster marker expression](assets/umap_vaccination_study_09_T_NK_lineage_true_subcluster_marker_expression.png)

![vaccination_study_09 T_NK_lineage subcluster marker score heatmap](assets/subcluster_marker_score_heatmap_vaccination_study_09_T_NK_lineage.png)

![vaccination_study_09 T_NK_lineage subcluster marker dotplot](assets/dotplot_vaccination_study_09_T_NK_lineage_true_subcluster_marker_dotplot.png)

Tables: `tables/vaccination_study_09_T_NK_lineage_true_subcluster_umap.tsv.gz`, `tables/vaccination_study_09_T_NK_lineage_subcluster_candidate_scores.tsv`.

#### vaccination_study_09 Myeloid_lineage true subcluster UMAP

![vaccination_study_09 Myeloid_lineage true subcluster labels](assets/umap_vaccination_study_09_Myeloid_lineage_true_subcluster_label.png)

![vaccination_study_09 Myeloid_lineage true subcluster source labels](assets/umap_vaccination_study_09_Myeloid_lineage_true_subcluster_source_labels.png)

![vaccination_study_09 Myeloid_lineage true subcluster QC](assets/umap_vaccination_study_09_Myeloid_lineage_true_subcluster_qc.png)

![vaccination_study_09 Myeloid_lineage true subcluster marker scores](assets/umap_vaccination_study_09_Myeloid_lineage_true_subcluster_marker_scores.png)

![vaccination_study_09 Myeloid_lineage true subcluster marker expression](assets/umap_vaccination_study_09_Myeloid_lineage_true_subcluster_marker_expression.png)

![vaccination_study_09 Myeloid_lineage subcluster marker score heatmap](assets/subcluster_marker_score_heatmap_vaccination_study_09_Myeloid_lineage.png)

![vaccination_study_09 Myeloid_lineage subcluster marker dotplot](assets/dotplot_vaccination_study_09_Myeloid_lineage_true_subcluster_marker_dotplot.png)

Tables: `tables/vaccination_study_09_Myeloid_lineage_true_subcluster_umap.tsv.gz`, `tables/vaccination_study_09_Myeloid_lineage_subcluster_candidate_scores.tsv`.


## Subcluster Marker Score Review

上の lineage-specific panel は、各 lineage subset で HVG 選択、PCA、neighbors、Leiden、UMAP を再計算した true local subcluster analysis から生成しています。Marker gene による fine label の確認は global UMAP だけではなく、この local UMAP、CellTypist/Azimuth/Pan-human/cluster-level marker gene assignment overlay、cluster marker gate score UMAP、marker-expression UMAP、dotplot を主に見ます。Treg など sparse marker label は cell-wise marker winner ではなく、local cluster の FOXP3/IL2RA/CTLA4 など key-marker support と reference support で判定します。

## Marker Assignment Feedback

Marker gene assignment は final label を強制的に上書きするものではなく、cluster-level の自己点検です。`raw_marker_winner` は marker score だけの勝者、`marker_assignment` は conservative policy と source-supported tie-break を通した marker-based assignment です。この表は marker assignment と final/reference-driven label がずれる cluster、marker specificity が弱い cluster、scRefMap が期待される lineage で欠落する cluster を示します。`marker_score` は raw marker base score から negative/confound marker penalty を差し引いた cluster-level marker gate score です。

| study | lineage | cluster | cells | chosen_label | marker_assignment | raw_marker_winner | assignment_reason | marker_score | base_score | penalty | flags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| vaccination_study_09 | T_NK_lineage | 4 | 13,847 | CD4 Naive / T Central Memory | NKT Cell | NKT Cell | raw_marker_winner | 0.723 | 0.809 | 0.086 | marker_final_disagreement |
| vaccination_study_09 | T_NK_lineage | 3 | 11,776 | CD8 Naive / T Central Memory | CD8 Naive / T Central Memory | CD8 Naive / T Central Memory | raw_marker_winner | 0.904 | 0.995 | 0.091 | screfmapping_missing_for_scope |
| vaccination_study_09 | T_NK_lineage | 2 | 6,316 | MAIT Cell | NKT Cell | NKT Cell | raw_marker_winner | 0.807 | 1.000 | 0.193 | marker_final_disagreement;screfmapping_missing_for_scope |
| vaccination_study_09 | T_NK_lineage | 9 | 6,222 | NK Cell | NK Cell | NKT Cell | source_supported_marker_tiebreak | 0.921 | 1.000 | 0.079 | screfmapping_missing_for_scope |
| vaccination_study_09 | T_NK_lineage | 8 | 5,821 | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | NKT Cell | source_supported_marker_tiebreak | 0.785 | 1.000 | 0.215 | screfmapping_missing_for_scope |
| vaccination_study_09 | T_NK_lineage | 7 | 4,607 | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | raw_marker_winner | 0.714 | 0.997 | 0.283 | screfmapping_missing_for_scope |
| vaccination_study_09 | T_NK_lineage | 0 | 3,302 | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | NKT Cell | source_supported_marker_tiebreak | 0.800 | 1.000 | 0.200 | screfmapping_missing_for_scope |
| vaccination_study_09 | T_NK_lineage | 5 | 3,152 | NK Cell | NK Cell | NKT Cell | source_supported_marker_tiebreak | 0.917 | 1.000 | 0.083 | screfmapping_missing_for_scope |
| vaccination_study_09 | Myeloid_lineage | 9 | 1,701 | Classical Monocyte | Intermediate Monocyte | Intermediate Monocyte | raw_marker_winner | 0.657 | 1.000 | 0.343 | marker_final_disagreement |
| vaccination_study_09 | B_lineage | 18 | 266 | Plasma Cell | Memory B Cell | Memory B Cell | raw_marker_winner | 0.012 | 0.023 | 0.011 | marker_final_disagreement;weak_marker_specificity |
| vaccination_study_09 | B_lineage | 20 | 159 | Plasma Cell | Plasmablast | Plasmablast | raw_marker_winner | 0.667 | 1.000 | 0.333 | marker_final_disagreement |
| vaccination_study_09 | Myeloid_lineage | 22 | 52 | Conventional DC 1 | Intermediate Monocyte | Intermediate Monocyte | raw_marker_winner | 0.857 | 1.000 | 0.143 | marker_final_disagreement |
| vaccination_study_09 | B_lineage | 26 | 20 | B Cell | Plasmablast | Plasmablast | raw_marker_winner | 0.667 | 1.000 | 0.333 | marker_final_disagreement;screfmapping_missing_for_scope |

## LLM Review Queue

この表は Codex/LLM が読むための subcluster-level review queue です。LLM はこの evidence を読んで、final label が妥当か、ontology にちょうどよい label がないのか、registry / conservative policy を一般ルールとして更新すべきかを提案します。LLM の出力で per-cell label を直接書き換えず、採用する場合は registry/config を更新して deterministic pipeline を再実行します。

| study | lineage | cluster | cells | priority | reasons | suggested_action | final_label | marker_assignment | raw_marker_winner | score_margin |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| vaccination_study_09 | B_lineage | 26 | 20 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | B Cell | Plasmablast | Plasmablast | 0.015 |
| vaccination_study_09 | T_NK_lineage | 2 | 6,316 | high | marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | MAIT Cell | NKT Cell | NKT Cell | 0.710 |
| vaccination_study_09 | T_NK_lineage | 4 | 13,847 | medium | marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate | evaluate_ontology_gap_or_conservative_policy | CD4 Naive / T Central Memory | NKT Cell | NKT Cell | 2.156 |
| vaccination_study_09 | T_NK_lineage | 9 | 6,222 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | NK Cell | NK Cell | NKT Cell | 2.515 |
| vaccination_study_09 | T_NK_lineage | 8 | 5,821 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | NKT Cell | 1.445 |
| vaccination_study_09 | T_NK_lineage | 0 | 3,302 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | NKT Cell | 0.763 |
| vaccination_study_09 | T_NK_lineage | 5 | 3,152 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | NK Cell | NK Cell | NKT Cell | 2.125 |
| vaccination_study_09 | Myeloid_lineage | 9 | 1,701 | medium | marker_assignment_disagrees_with_final;screfmapping_not_available | review_marker_vs_reference_disagreement | Classical Monocyte | Intermediate Monocyte | Intermediate Monocyte | 2.273 |
| vaccination_study_09 | B_lineage | 20 | 159 | medium | marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate | evaluate_ontology_gap_or_conservative_policy | Plasma Cell | Plasmablast | Plasmablast | 1.908 |
| vaccination_study_09 | T_NK_lineage | 3 | 11,776 | low | screfmapping_not_available | accept | CD8 Naive / T Central Memory | CD8 Naive / T Central Memory | CD8 Naive / T Central Memory | 0.451 |
| vaccination_study_09 | T_NK_lineage | 7 | 4,607 | low | screfmapping_not_available | accept | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | 1.887 |
| vaccination_study_09 | Myeloid_lineage | 22 | 52 | low | marker_assignment_disagrees_with_final;screfmapping_not_available | review_marker_vs_reference_disagreement | Conventional DC 1 | Intermediate Monocyte | Intermediate Monocyte | 1.292 |
| vaccination_study_09 | B_lineage | 18 | 266 | low | marker_assignment_disagrees_with_final | review_marker_vs_reference_disagreement | Plasma Cell | Memory B Cell | Memory B Cell | 1.296 |

## Cluster Consensus Evidence

| study | lineage | cluster | cells | chosen_label | accepted | score_margin | cluster_marker_assignment | treg_key_any | treg_key_bonus | marker_set | marker_alert |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| vaccination_study_09 | B_lineage | 0 | 1,607 | Naive B Cell | True | 4.115 | Naive B Cell | nan | nan | B_naive | pass |
| vaccination_study_09 | B_lineage | 1 | 1,227 | Memory B Cell | True | 3.198 | Memory B Cell | nan | nan | B_memory_ABC | pass |
| vaccination_study_09 | B_lineage | 2 | 1,135 | Naive B Cell | True | 3.944 | Naive B Cell | nan | nan | B_naive | pass |
| vaccination_study_09 | B_lineage | 3 | 1,110 | Naive B Cell | True | 3.705 | Naive B Cell | nan | nan | B_naive | pass |
| vaccination_study_09 | B_lineage | 4 | 1,100 | Naive B Cell | True | 3.668 | Naive B Cell | nan | nan | B_naive | pass |
| vaccination_study_09 | B_lineage | 5 | 957 | Naive B Cell | True | 3.823 | Naive B Cell | nan | nan | B_naive | pass |
| vaccination_study_09 | B_lineage | 6 | 941 | Naive B Cell | True | 3.978 | Naive B Cell | nan | nan | B_naive | pass |
| vaccination_study_09 | B_lineage | 7 | 844 | Naive B Cell | True | 3.848 | Naive B Cell | nan | nan | B_naive | pass |
| vaccination_study_09 | B_lineage | 8 | 804 | Memory B Cell | True | 3.541 | Memory B Cell | nan | nan | B_memory_ABC | pass |
| vaccination_study_09 | B_lineage | 9 | 766 | Naive B Cell | True | 4.156 | Naive B Cell | nan | nan | B_naive | pass |
| vaccination_study_09 | B_lineage | 10 | 728 | Naive B Cell | True | 3.903 | Naive B Cell | nan | nan | B_naive | pass |
| vaccination_study_09 | B_lineage | 11 | 640 | Memory B Cell | True | 3.289 | Memory B Cell | nan | nan | B_memory_ABC | pass |
| vaccination_study_09 | B_lineage | 12 | 552 | Naive B Cell | True | 3.384 | Naive B Cell | nan | nan | B_naive | pass |
| vaccination_study_09 | B_lineage | 13 | 549 | Memory B Cell | True | 3.893 | Memory B Cell | nan | nan | B_memory_ABC | pass |
| vaccination_study_09 | B_lineage | 14 | 503 | Memory B Cell | True | 3.579 | Memory B Cell | nan | nan | B_memory_ABC | pass |
| vaccination_study_09 | B_lineage | 15 | 483 | Naive B Cell | True | 3.709 | Naive B Cell | nan | nan | B_naive | pass |
| vaccination_study_09 | B_lineage | 16 | 452 | Naive B Cell | True | 3.197 | Naive B Cell | nan | nan | B_naive | pass |
| vaccination_study_09 | B_lineage | 17 | 381 | Memory B Cell | True | 3.498 | Memory B Cell | nan | nan | B_memory_ABC | pass |
| vaccination_study_09 | B_lineage | 18 | 266 | Plasma Cell | True | 1.296 | Memory B Cell | nan | nan | Plasma_ASC | warning |
| vaccination_study_09 | B_lineage | 19 | 260 | Naive B Cell | True | 3.651 | Naive B Cell | nan | nan | B_naive | pass |
| vaccination_study_09 | B_lineage | 20 | 159 | Plasma Cell | True | 1.908 | Plasmablast | nan | nan | Plasma_ASC | warning |
| vaccination_study_09 | B_lineage | 21 | 147 | Naive B Cell | True | 0.532 | Naive B Cell | nan | nan | B_naive | pass |
| vaccination_study_09 | B_lineage | 22 | 112 | Naive B Cell | True | 3.732 | Naive B Cell | nan | nan | B_naive | pass |
| vaccination_study_09 | B_lineage | 23 | 75 | Naive B Cell | True | 1.285 | Naive B Cell | nan | nan | B_naive | pass |
| vaccination_study_09 | B_lineage | 24 | 69 | Memory B Cell | True | 1.911 | Memory B Cell | nan | nan | B_memory_ABC | pass |
| vaccination_study_09 | B_lineage | 25 | 64 | Naive B Cell | True | 4.087 | Naive B Cell | nan | nan | B_naive | pass |
| vaccination_study_09 | B_lineage | 26 | 20 | B Cell | False | 0.015 | Plasmablast | nan | nan | Plasma_ASC | warning |
| vaccination_study_09 | B_lineage | 27 | 17 | Naive B Cell | True | 1.985 | Naive B Cell | nan | nan | B_naive | pass |
| vaccination_study_09 | Myeloid_lineage | 0 | 2,756 | Non-Classical Monocyte | True | 1.669 | Non-Classical Monocyte | nan | nan | registry__non_classical_monocyte | pass |
| vaccination_study_09 | Myeloid_lineage | 1 | 2,708 | Classical Monocyte | True | 2.217 | Classical Monocyte | nan | nan | registry__classical_monocyte | pass |

## 出力ファイル

- Submission TSVs: `outputs/submission_v25_harmony_reference_rescue/vaccination_study_09/submissions/`
- cellxgene H5ADs: `outputs/submission_v25_harmony_reference_rescue/vaccination_study_09/cellxgene/`
- Marker availability table: `outputs/submission_v25_harmony_reference_rescue/vaccination_study_09/tables/marker_gene_availability.tsv`
- Marker availability alerts: `outputs/submission_v25_harmony_reference_rescue/vaccination_study_09/tables/marker_gene_availability_alerts.tsv`
- Subcluster evidence: `outputs/submission_v25_harmony_reference_rescue/vaccination_study_09/tables/lineage_subcluster_evidence.tsv.gz`
- Source disagreement summary: `outputs/submission_v25_harmony_reference_rescue/vaccination_study_09/tables/source_disagreement_summary.tsv`
- Source effectiveness summary: `outputs/submission_v25_harmony_reference_rescue/vaccination_study_09/tables/source_effectiveness_summary.tsv`
- Diagnostics tables: `outputs/submission_v25_harmony_reference_rescue/vaccination_study_09/tables/`

