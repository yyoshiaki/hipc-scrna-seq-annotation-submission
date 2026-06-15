# HIPC データセットアノテーションレポート: infection_study_01

更新日: 2026-06-15 EDT

このレポートは `hipc-annotation` Codex workflow によって生成したデータセット別レビュー文書です。固定 method は repository README に置き、このレポートでは実際の evidence、弱い箇所、レビュー優先度、UMAP / dotplot を確認します。

## データセット概要

| study | cells | analysis_X_genes | pre_hvg_genes | counts_layer_genes | labels | parent_or_blood_fraction | Blood Cell | Doublet | artifact_like | median_confidence | low_confidence | source_disagreement | invalid_labels |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| infection_study_01 | 54,924 | 33,538 | 33,538 | 33,538 | 21 | 0.004 | 197 | 1,278 | 1,356 | 0.777 | 2,895 | 7,814 (0.142) | none |

## 実行概要

- 実行単位: one dataset in, one annotated dataset out。
- 実行経路: Codex skill `hipc-annotation` -> bundled helper `run_one.sh` -> annotation CLI -> validator -> report inspection。
- 検証: submission row count、H5AD observation count、official label validity、H5AD/submission agreement、confidence column、report image link を確認する。
- このレポートは workflow の再掲ではなく、このデータセットの marker 欠損、UMAP、label 構成、review concern を読むためのもの。

## データセット固有の解釈

- `infection_study_01`: 54,924 cells、analysis X/var 33,538 genes、pre-HVG slot 33,538 genes、submitted label 21 種、parent/Blood residual fraction 0.004、median confidence 0.777。
  - 2,895 cells は low confidence。QC / confidence UMAP 上で局在を確認する。
  - 1,278 cells は `Doublet` として提出。mixed-lineage marker expression と scrublet support を確認する。
  - 197 cells は `Blood Cell` として残存。これは filter-out ではなく、曖昧な細胞を公式 parent label で残したもの。

## データセット固有の評価

- 全体像: 54,924 cells / analysis X/var 33,538 genes / pre-HVG slot 33,538 genes。parent/Blood residual は 0.004、low-confidence は 2,895 cells、source disagreement flag は 7,814 cells (0.142)。
- 優先確認: low-confidence 領域が QC UMAP と source-disagreement UMAP で同じ場所に集まるかを確認する。
- 優先確認: `Blood Cell` 残存が孤立 cluster なのか、複数 lineage に分散した曖昧領域なのかを UMAP で確認する。

## Marker Gene 欠損アラート

なし。

## ソース間不一致

| study | predicted_cell_type | cells | median_source_agreement | disagreement_cells | disagreement_fraction |
| --- | --- | --- | --- | --- | --- |
| infection_study_01 | Doublet | 1,278 | 0.000 | 1,278 | 1.000 |
| infection_study_01 | Plasmablast | 41 | 0.200 | 41 | 1.000 |
| infection_study_01 | Neutrophil | 14 | 0.250 | 14 | 1.000 |
| infection_study_01 | CD4 T Effector Memory | 1,628 | 0.400 | 824 | 0.506 |
| infection_study_01 | MAIT Cell | 958 | 0.500 | 466 | 0.486 |
| infection_study_01 | CD4 Naive / T Central Memory | 4,590 | 0.600 | 1,916 | 0.417 |
| infection_study_01 | Plasma Cell | 130 | 0.800 | 47 | 0.362 |
| infection_study_01 | Blood Cell | 197 | 0.750 | 70 | 0.355 |
| infection_study_01 | Memory B Cell | 2,118 | 0.600 | 531 | 0.251 |
| infection_study_01 | Plasmacytoid DC | 105 | 0.750 | 15 | 0.143 |
| infection_study_01 | CD8 Naive / T Central Memory | 360 | 0.750 | 40 | 0.111 |
| infection_study_01 | CD8 Cytotoxic / T Effector Memory | 8,723 | 1.000 | 848 | 0.097 |

## アノテーションソース効果

この表は外部 ground truth に対する正解率ではありません。各 annotation source がどれだけの細胞で情報を持ち、final label とどれだけ一致したかを示す監査用統計です。`coverage` は source が `not_available` 以外を返した割合、`final_concordance` は informative cells の中で final label と一致した割合、`unique_support` はその source だけが final label と一致した細胞数です。

| study | source | informative_cells | coverage | final_concordance | high_conf_concordance | unique_support | discordant |
| --- | --- | --- | --- | --- | --- | --- | --- |
| infection_study_01 | Cluster consensus | 54,924 | 1.000 | 0.829 | 0.905 | 617 | 9,376 |
| infection_study_01 | CellTypist | 54,924 | 1.000 | 0.823 | 0.919 | 136 | 9,716 |
| infection_study_01 | Azimuth PBMC L2 | 54,924 | 1.000 | 0.817 | 0.925 | 85 | 10,047 |
| infection_study_01 | Pan-human Azimuth | 54,924 | 1.000 | 0.743 | 0.830 | 114 | 14,135 |
| infection_study_01 | Azimuth PBMC L3 | 54,924 | 1.000 | 0.401 | 0.519 | 6 | 32,919 |
| infection_study_01 | Cluster marker assignment | 52,091 | 0.948 | 0.858 | 0.853 | 1,415 | 7,373 |
| infection_study_01 | scRefMapping | 12,525 | 0.228 | 0.804 | 0.959 | 4 | 2,453 |

## レビュー優先事項

| study | concern | cells |
| --- | --- | --- |
| infection_study_01 | High source disagreement for CD4 T Effector Memory | 824 |
| infection_study_01 | High source disagreement for Doublet | 1,278 |
| infection_study_01 | High source disagreement for Neutrophil | 14 |
| infection_study_01 | High source disagreement for Plasmablast | 41 |

## ラベル構成

| study | predicted_cell_type | cells |
| --- | --- | --- |
| infection_study_01 | Classical Monocyte | 17,074 |
| infection_study_01 | NK Cell | 9,393 |
| infection_study_01 | CD8 Cytotoxic / T Effector Memory | 8,723 |
| infection_study_01 | CD4 Naive / T Central Memory | 4,590 |
| infection_study_01 | Naive B Cell | 4,252 |
| infection_study_01 | Non-Classical Monocyte | 2,219 |
| infection_study_01 | Memory B Cell | 2,118 |
| infection_study_01 | CD4 T Effector Memory | 1,628 |
| infection_study_01 | Platelet | 1,343 |
| infection_study_01 | Doublet | 1,278 |
| infection_study_01 | MAIT Cell | 958 |
| infection_study_01 | Conventional DC 2 | 455 |
| infection_study_01 | CD8 Naive / T Central Memory | 360 |
| infection_study_01 | Blood Cell | 197 |
| infection_study_01 | Plasma Cell | 130 |
| infection_study_01 | Plasmacytoid DC | 105 |
| infection_study_01 | Plasmablast | 41 |
| infection_study_01 | Conventional DC 1 | 33 |
| infection_study_01 | Neutrophil | 14 |
| infection_study_01 | HSC | 12 |
| infection_study_01 | RBC | 1 |

## Inline Figures

### infection_study_01

![infection_study_01 final labels](assets/umap_infection_study_01_annotation_label.png)

![infection_study_01 lineage and annotation reason](assets/umap_infection_study_01_annotation_lineage_reason.png)

![infection_study_01 QC and confidence](assets/umap_infection_study_01_annotation_qc_confidence.png)

![infection_study_01 source agreement and disagreement](assets/umap_infection_study_01_annotation_source_disagreement.png)

![infection_study_01 annotation-source effectiveness](assets/figure_02_source_effectiveness.png)

![infection_study_01 marker expression UMAPs](assets/umap_infection_study_01_annotation_marker_expression.png)

![infection_study_01 submitted-label marker dotplot](assets/dotplot_infection_study_01_annotation_marker_dotplot.png)

#### infection_study_01 B_lineage true subcluster UMAP

![infection_study_01 B_lineage true subcluster labels](assets/umap_infection_study_01_B_lineage_true_subcluster_label.png)

![infection_study_01 B_lineage true subcluster source labels](assets/umap_infection_study_01_B_lineage_true_subcluster_source_labels.png)

![infection_study_01 B_lineage true subcluster QC](assets/umap_infection_study_01_B_lineage_true_subcluster_qc.png)

![infection_study_01 B_lineage true subcluster marker scores](assets/umap_infection_study_01_B_lineage_true_subcluster_marker_scores.png)

![infection_study_01 B_lineage true subcluster marker expression](assets/umap_infection_study_01_B_lineage_true_subcluster_marker_expression.png)

![infection_study_01 B_lineage subcluster marker score heatmap](assets/subcluster_marker_score_heatmap_infection_study_01_B_lineage.png)

![infection_study_01 B_lineage subcluster marker dotplot](assets/dotplot_infection_study_01_B_lineage_true_subcluster_marker_dotplot.png)

Tables: `tables/infection_study_01_B_lineage_true_subcluster_umap.tsv.gz`, `tables/infection_study_01_B_lineage_subcluster_candidate_scores.tsv`.

#### infection_study_01 T_NK_lineage true subcluster UMAP

![infection_study_01 T_NK_lineage true subcluster labels](assets/umap_infection_study_01_T_NK_lineage_true_subcluster_label.png)

![infection_study_01 T_NK_lineage true subcluster source labels](assets/umap_infection_study_01_T_NK_lineage_true_subcluster_source_labels.png)

![infection_study_01 T_NK_lineage true subcluster QC](assets/umap_infection_study_01_T_NK_lineage_true_subcluster_qc.png)

![infection_study_01 T_NK_lineage true subcluster marker scores](assets/umap_infection_study_01_T_NK_lineage_true_subcluster_marker_scores.png)

![infection_study_01 T_NK_lineage true subcluster marker expression](assets/umap_infection_study_01_T_NK_lineage_true_subcluster_marker_expression.png)

![infection_study_01 T_NK_lineage subcluster marker score heatmap](assets/subcluster_marker_score_heatmap_infection_study_01_T_NK_lineage.png)

![infection_study_01 T_NK_lineage subcluster marker dotplot](assets/dotplot_infection_study_01_T_NK_lineage_true_subcluster_marker_dotplot.png)

Tables: `tables/infection_study_01_T_NK_lineage_true_subcluster_umap.tsv.gz`, `tables/infection_study_01_T_NK_lineage_subcluster_candidate_scores.tsv`.

#### infection_study_01 Myeloid_lineage true subcluster UMAP

![infection_study_01 Myeloid_lineage true subcluster labels](assets/umap_infection_study_01_Myeloid_lineage_true_subcluster_label.png)

![infection_study_01 Myeloid_lineage true subcluster source labels](assets/umap_infection_study_01_Myeloid_lineage_true_subcluster_source_labels.png)

![infection_study_01 Myeloid_lineage true subcluster QC](assets/umap_infection_study_01_Myeloid_lineage_true_subcluster_qc.png)

![infection_study_01 Myeloid_lineage true subcluster marker scores](assets/umap_infection_study_01_Myeloid_lineage_true_subcluster_marker_scores.png)

![infection_study_01 Myeloid_lineage true subcluster marker expression](assets/umap_infection_study_01_Myeloid_lineage_true_subcluster_marker_expression.png)

![infection_study_01 Myeloid_lineage subcluster marker score heatmap](assets/subcluster_marker_score_heatmap_infection_study_01_Myeloid_lineage.png)

![infection_study_01 Myeloid_lineage subcluster marker dotplot](assets/dotplot_infection_study_01_Myeloid_lineage_true_subcluster_marker_dotplot.png)

Tables: `tables/infection_study_01_Myeloid_lineage_true_subcluster_umap.tsv.gz`, `tables/infection_study_01_Myeloid_lineage_subcluster_candidate_scores.tsv`.


## Subcluster Marker Score Review

上の lineage-specific panel は、各 lineage subset で HVG 選択、PCA、neighbors、Leiden、UMAP を再計算した true local subcluster analysis から生成しています。Marker gene による fine label の確認は global UMAP だけではなく、この local UMAP、CellTypist/Azimuth/Pan-human/cluster-level marker gene assignment overlay、cluster marker gate score UMAP、marker-expression UMAP、dotplot を主に見ます。Treg など sparse marker label は cell-wise marker winner ではなく、local cluster の FOXP3/IL2RA/CTLA4 など key-marker support と reference support で判定します。

## Marker Assignment Feedback

Marker gene assignment は final label を強制的に上書きするものではなく、cluster-level の自己点検です。`raw_marker_winner` は marker score だけの勝者、`marker_assignment` は conservative policy と source-supported tie-break を通した marker-based assignment です。この表は marker assignment と final/reference-driven label がずれる cluster、marker specificity が弱い cluster、scRefMap が期待される lineage で欠落する cluster を示します。`marker_score` は raw marker base score から negative/confound marker penalty を差し引いた cluster-level marker gate score です。

| study | lineage | cluster | cells | chosen_label | marker_assignment | raw_marker_winner | assignment_reason | marker_score | base_score | penalty | flags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| infection_study_01 | T_NK_lineage | 0 | 1,329 | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | raw_marker_winner | 0.540 | 1.000 | 0.460 | screfmapping_missing_for_scope |
| infection_study_01 | T_NK_lineage | 1 | 1,307 | NK Cell | NKT Cell | NKT Cell | raw_marker_winner | 0.864 | 1.000 | 0.136 | marker_final_disagreement;screfmapping_missing_for_scope |
| infection_study_01 | T_NK_lineage | 4 | 1,015 | NK Cell | NKT Cell | NKT Cell | raw_marker_winner | 0.918 | 1.000 | 0.082 | marker_final_disagreement;screfmapping_missing_for_scope |
| infection_study_01 | T_NK_lineage | 5 | 990 | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | NKT Cell | source_supported_marker_tiebreak | 0.578 | 1.000 | 0.422 | screfmapping_missing_for_scope |
| infection_study_01 | T_NK_lineage | 6 | 960 | NK Cell | NK Cell | NKT Cell | source_supported_marker_tiebreak | 0.822 | 1.000 | 0.178 | screfmapping_missing_for_scope |
| infection_study_01 | T_NK_lineage | 7 | 876 | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | NKT Cell | source_supported_marker_tiebreak | 0.890 | 1.000 | 0.110 | screfmapping_missing_for_scope |
| infection_study_01 | T_NK_lineage | 9 | 808 | NK Cell | NK Cell | NKT Cell | source_supported_marker_tiebreak | 0.829 | 1.000 | 0.171 | screfmapping_missing_for_scope |
| infection_study_01 | T_NK_lineage | 11 | 767 | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | NKT Cell | source_supported_marker_tiebreak | 0.526 | 1.000 | 0.474 | screfmapping_missing_for_scope |
| infection_study_01 | T_NK_lineage | 13 | 717 | NK Cell | NKT Cell | NKT Cell | raw_marker_winner | 0.891 | 1.000 | 0.109 | marker_final_disagreement;screfmapping_missing_for_scope |
| infection_study_01 | T_NK_lineage | 14 | 708 | MAIT Cell | NKT Cell | NKT Cell | raw_marker_winner | 0.838 | 1.000 | 0.162 | marker_final_disagreement;screfmapping_missing_for_scope |
| infection_study_01 | T_NK_lineage | 16 | 616 | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | NKT Cell | source_supported_marker_tiebreak | 0.541 | 1.000 | 0.459 | screfmapping_missing_for_scope |
| infection_study_01 | T_NK_lineage | 17 | 610 | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | NKT Cell | source_supported_marker_tiebreak | 0.525 | 1.000 | 0.475 | screfmapping_missing_for_scope |
| infection_study_01 | T_NK_lineage | 18 | 589 | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | NKT Cell | source_supported_marker_tiebreak | 0.565 | 1.000 | 0.435 | screfmapping_missing_for_scope |
| infection_study_01 | T_NK_lineage | 19 | 534 | NK Cell | NK Cell | NKT Cell | source_supported_marker_tiebreak | 0.841 | 1.000 | 0.159 | screfmapping_missing_for_scope |
| infection_study_01 | T_NK_lineage | 21 | 529 | NK Cell | NK Cell | NKT Cell | source_supported_marker_tiebreak | 0.582 | 1.000 | 0.418 | screfmapping_missing_for_scope |
| infection_study_01 | T_NK_lineage | 22 | 498 | NK Cell | NK Cell | NKT Cell | source_supported_marker_tiebreak | 0.884 | 0.996 | 0.112 | screfmapping_missing_for_scope |
| infection_study_01 | T_NK_lineage | 23 | 460 | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | raw_marker_winner | 0.507 | 1.000 | 0.493 | screfmapping_missing_for_scope |
| infection_study_01 | T_NK_lineage | 24 | 427 | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | NKT Cell | source_supported_marker_tiebreak | 0.737 | 1.000 | 0.263 | screfmapping_missing_for_scope |
| infection_study_01 | T_NK_lineage | 25 | 425 | NK Cell | NK Cell | NKT Cell | source_supported_marker_tiebreak | 0.853 | 0.996 | 0.144 | screfmapping_missing_for_scope |
| infection_study_01 | B_lineage | 2 | 408 | Memory B Cell | Naive B Cell | Naive B Cell | raw_marker_winner | 0.537 | 0.990 | 0.453 | marker_final_disagreement |

## LLM Review Queue

この表は Codex/LLM が読むための subcluster-level review queue です。LLM はこの evidence を読んで、final label が妥当か、ontology にちょうどよい label がないのか、registry / conservative policy を一般ルールとして更新すべきかを提案します。LLM の出力で per-cell label を直接書き換えず、採用する場合は registry/config を更新して deterministic pipeline を再実行します。

| study | lineage | cluster | cells | priority | reasons | suggested_action | final_label | marker_assignment | raw_marker_winner | score_margin |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| infection_study_01 | T_NK_lineage | 1 | 1,307 | high | marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | NK Cell | NKT Cell | NKT Cell | 1.779 |
| infection_study_01 | T_NK_lineage | 4 | 1,015 | high | marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | NK Cell | NKT Cell | NKT Cell | 2.237 |
| infection_study_01 | T_NK_lineage | 43 | 91 | high | marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available;low_total_score_or_margin | evaluate_ontology_gap_or_conservative_policy | CD8 Cytotoxic / T Effector Memory | NKT Cell | NKT Cell | 0.077 |
| infection_study_01 | T_NK_lineage | 13 | 717 | medium | marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | NK Cell | NKT Cell | NKT Cell | 2.179 |
| infection_study_01 | T_NK_lineage | 14 | 708 | medium | marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | MAIT Cell | NKT Cell | NKT Cell | 0.383 |
| infection_study_01 | T_NK_lineage | 26 | 408 | medium | marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | CD8 Cytotoxic / T Effector Memory | NKT Cell | NKT Cell | 1.239 |
| infection_study_01 | T_NK_lineage | 28 | 392 | medium | marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | NK Cell | NKT Cell | NKT Cell | 0.157 |
| infection_study_01 | T_NK_lineage | 30 | 376 | medium | marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | NK Cell | NKT Cell | NKT Cell | 1.744 |
| infection_study_01 | T_NK_lineage | 33 | 341 | medium | marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | CD8 Cytotoxic / T Effector Memory | NKT Cell | NKT Cell | 0.312 |
| infection_study_01 | T_NK_lineage | 5 | 990 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | NKT Cell | 2.481 |
| infection_study_01 | T_NK_lineage | 6 | 960 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | NK Cell | NK Cell | NKT Cell | 2.513 |
| infection_study_01 | T_NK_lineage | 7 | 876 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | NKT Cell | 1.840 |
| infection_study_01 | T_NK_lineage | 9 | 808 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | NK Cell | NK Cell | NKT Cell | 2.536 |
| infection_study_01 | T_NK_lineage | 11 | 767 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | NKT Cell | 2.541 |
| infection_study_01 | T_NK_lineage | 16 | 616 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | NKT Cell | 2.358 |
| infection_study_01 | T_NK_lineage | 17 | 610 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | NKT Cell | 2.131 |
| infection_study_01 | T_NK_lineage | 18 | 589 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | NKT Cell | 2.466 |
| infection_study_01 | T_NK_lineage | 19 | 534 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | NK Cell | NK Cell | NKT Cell | 2.370 |
| infection_study_01 | T_NK_lineage | 21 | 529 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | NK Cell | NK Cell | NKT Cell | 1.706 |
| infection_study_01 | T_NK_lineage | 22 | 498 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | NK Cell | NK Cell | NKT Cell | 2.340 |

## Cluster Consensus Evidence

| study | lineage | cluster | cells | chosen_label | accepted | score_margin | cluster_marker_assignment | treg_key_any | treg_key_bonus | marker_set | marker_alert |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| infection_study_01 | B_lineage | 0 | 452 | Memory B Cell | True | 4.192 | Memory B Cell | nan | nan | B_memory_ABC | pass |
| infection_study_01 | B_lineage | 1 | 449 | Naive B Cell | True | 4.470 | Naive B Cell | nan | nan | B_naive | pass |
| infection_study_01 | B_lineage | 2 | 408 | Memory B Cell | True | 3.307 | Naive B Cell | nan | nan | B_memory_ABC | pass |
| infection_study_01 | B_lineage | 3 | 402 | Memory B Cell | True | 2.879 | Naive B Cell | nan | nan | B_memory_ABC | pass |
| infection_study_01 | B_lineage | 4 | 398 | Naive B Cell | True | 4.499 | Naive B Cell | nan | nan | B_naive | pass |
| infection_study_01 | B_lineage | 5 | 394 | Naive B Cell | True | 4.152 | Naive B Cell | nan | nan | B_naive | pass |
| infection_study_01 | B_lineage | 6 | 366 | Naive B Cell | True | 4.375 | Naive B Cell | nan | nan | B_naive | pass |
| infection_study_01 | B_lineage | 7 | 322 | Naive B Cell | True | 3.997 | Naive B Cell | nan | nan | B_naive | pass |
| infection_study_01 | B_lineage | 8 | 316 | Memory B Cell | True | 3.292 | Memory B Cell | nan | nan | B_memory_ABC | pass |
| infection_study_01 | B_lineage | 9 | 314 | Naive B Cell | True | 4.067 | Naive B Cell | nan | nan | B_naive | pass |
| infection_study_01 | B_lineage | 10 | 313 | Naive B Cell | True | 3.879 | Naive B Cell | nan | nan | B_naive | pass |
| infection_study_01 | B_lineage | 11 | 283 | Naive B Cell | True | 4.286 | Naive B Cell | nan | nan | B_naive | pass |
| infection_study_01 | B_lineage | 12 | 241 | Memory B Cell | True | 3.716 | Memory B Cell | nan | nan | B_memory_ABC | pass |
| infection_study_01 | B_lineage | 13 | 232 | Naive B Cell | True | 4.245 | Naive B Cell | nan | nan | B_naive | pass |
| infection_study_01 | B_lineage | 14 | 218 | Naive B Cell | True | 2.989 | Naive B Cell | nan | nan | B_naive | pass |
| infection_study_01 | B_lineage | 15 | 215 | Naive B Cell | True | 1.676 | Naive B Cell | nan | nan | B_naive | pass |
| infection_study_01 | B_lineage | 16 | 190 | Memory B Cell | True | 3.704 | Memory B Cell | nan | nan | B_memory_ABC | pass |
| infection_study_01 | B_lineage | 17 | 178 | Naive B Cell | True | 4.229 | Naive B Cell | nan | nan | B_naive | pass |
| infection_study_01 | B_lineage | 18 | 152 | Naive B Cell | True | 4.111 | Naive B Cell | nan | nan | B_naive | pass |
| infection_study_01 | B_lineage | 19 | 148 | Naive B Cell | True | 4.160 | Naive B Cell | nan | nan | B_naive | pass |
| infection_study_01 | B_lineage | 20 | 131 | Naive B Cell | True | 3.033 | Naive B Cell | nan | nan | B_naive | pass |
| infection_study_01 | B_lineage | 21 | 100 | Naive B Cell | True | 0.570 | Naive B Cell | nan | nan | B_naive | pass |
| infection_study_01 | B_lineage | 22 | 85 | Plasma Cell | True | 1.726 | Plasmablast | nan | nan | Plasma_ASC | pass |
| infection_study_01 | B_lineage | 23 | 80 | Memory B Cell | True | 3.892 | Memory B Cell | nan | nan | B_memory_ABC | pass |
| infection_study_01 | B_lineage | 24 | 45 | Plasma Cell | True | 0.681 | Plasma Cell | nan | nan | Plasma_ASC | pass |
| infection_study_01 | B_lineage | 25 | 41 | Plasmablast | True | 0.636 | Plasmablast | nan | nan | Plasma_ASC | pass |
| infection_study_01 | B_lineage | 26 | 39 | Naive B Cell | True | 1.354 | Naive B Cell | nan | nan | B_naive | pass |
| infection_study_01 | B_lineage | 27 | 29 | Memory B Cell | True | 3.443 | Memory B Cell | nan | nan | B_memory_ABC | pass |
| infection_study_01 | Myeloid_lineage | 0 | 1,533 | Classical Monocyte | True | 2.056 | Classical Monocyte | nan | nan | registry__classical_monocyte | pass |
| infection_study_01 | Myeloid_lineage | 1 | 1,505 | Classical Monocyte | True | 2.408 | Classical Monocyte | nan | nan | registry__classical_monocyte | pass |

## 出力ファイル

- Submission TSVs: `outputs/submission_v25_harmony_reference_rescue/infection_study_01/submissions/`
- cellxgene H5ADs: `outputs/submission_v25_harmony_reference_rescue/infection_study_01/cellxgene/`
- Marker availability table: `outputs/submission_v25_harmony_reference_rescue/infection_study_01/tables/marker_gene_availability.tsv`
- Marker availability alerts: `outputs/submission_v25_harmony_reference_rescue/infection_study_01/tables/marker_gene_availability_alerts.tsv`
- Subcluster evidence: `outputs/submission_v25_harmony_reference_rescue/infection_study_01/tables/lineage_subcluster_evidence.tsv.gz`
- Source disagreement summary: `outputs/submission_v25_harmony_reference_rescue/infection_study_01/tables/source_disagreement_summary.tsv`
- Source effectiveness summary: `outputs/submission_v25_harmony_reference_rescue/infection_study_01/tables/source_effectiveness_summary.tsv`
- Diagnostics tables: `outputs/submission_v25_harmony_reference_rescue/infection_study_01/tables/`

