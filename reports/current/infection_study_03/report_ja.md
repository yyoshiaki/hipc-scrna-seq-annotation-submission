# HIPC データセットアノテーションレポート: infection_study_03

更新日: 2026-06-15 EDT

このレポートは `hipc-annotation` Codex workflow によって生成したデータセット別レビュー文書です。固定 method は repository README に置き、このレポートでは実際の evidence、弱い箇所、レビュー優先度、UMAP / dotplot を確認します。

## データセット概要

| study | cells | analysis_X_genes | pre_hvg_genes | counts_layer_genes | labels | parent_or_blood_fraction | Blood Cell | Doublet | artifact_like | median_confidence | low_confidence | source_disagreement | invalid_labels |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| infection_study_03 | 646,739 | 24,929 | 24,929 | 24,929 | 14 | 0.004 | 2,324 | 0 | 14,448 | 0.818 | 2,324 | 134,542 (0.208) | none |

## 実行概要

- 実行単位: one dataset in, one annotated dataset out。
- 実行経路: Codex skill `hipc-annotation` -> bundled helper `run_one.sh` -> annotation CLI -> validator -> report inspection。
- 検証: submission row count、H5AD observation count、official label validity、H5AD/submission agreement、confidence column、report image link を確認する。
- このレポートは workflow の再掲ではなく、このデータセットの marker 欠損、UMAP、label 構成、review concern を読むためのもの。

## データセット固有の解釈

- `infection_study_03`: 646,739 cells、analysis X/var 24,929 genes、pre-HVG slot 24,929 genes、submitted label 14 種、parent/Blood residual fraction 0.004、median confidence 0.818。
  - 2,324 cells は low confidence。QC / confidence UMAP 上で局在を確認する。
  - 2,324 cells は `Blood Cell` として残存。これは filter-out ではなく、曖昧な細胞を公式 parent label で残したもの。

## データセット固有の評価

- 全体像: 646,739 cells / analysis X/var 24,929 genes / pre-HVG slot 24,929 genes。parent/Blood residual は 0.004、low-confidence は 2,324 cells、source disagreement flag は 134,542 cells (0.208)。
- 優先確認: low-confidence 領域が QC UMAP と source-disagreement UMAP で同じ場所に集まるかを確認する。
- 優先確認: `Blood Cell` 残存が孤立 cluster なのか、複数 lineage に分散した曖昧領域なのかを UMAP で確認する。

## Marker Gene 欠損アラート

なし。

## ソース間不一致

| study | predicted_cell_type | cells | median_source_agreement | disagreement_cells | disagreement_fraction |
| --- | --- | --- | --- | --- | --- |
| infection_study_03 | Blood Cell | 2,324 | 0.333 | 1,965 | 0.846 |
| infection_study_03 | Conventional DC 2 | 8,329 | 0.667 | 4,077 | 0.489 |
| infection_study_03 | Plasma Cell | 8,842 | 0.667 | 3,927 | 0.444 |
| infection_study_03 | CD8 Naive / T Central Memory | 9,049 | 0.667 | 3,489 | 0.386 |
| infection_study_03 | Memory B Cell | 6,291 | 0.667 | 2,419 | 0.385 |
| infection_study_03 | Naive B Cell | 61,829 | 1.000 | 22,408 | 0.362 |
| infection_study_03 | CD4 Naive / T Central Memory | 184,676 | 0.667 | 50,686 | 0.274 |
| infection_study_03 | CD8 Cytotoxic / T Effector Memory | 102,353 | 1.000 | 26,323 | 0.257 |
| infection_study_03 | Non-Classical Monocyte | 10,769 | 0.667 | 1,663 | 0.154 |
| infection_study_03 | Classical Monocyte | 130,556 | 0.667 | 14,140 | 0.108 |
| infection_study_03 | NK Cell | 102,938 | 1.000 | 3,414 | 0.033 |
| infection_study_03 | Plasmacytoid DC | 4,335 | 1.000 | 31 | 0.007 |

## アノテーションソース効果

この表は外部 ground truth に対する正解率ではありません。各 annotation source がどれだけの細胞で情報を持ち、final label とどれだけ一致したかを示す監査用統計です。`coverage` は source が `not_available` 以外を返した割合、`final_concordance` は informative cells の中で final label と一致した割合、`unique_support` はその source だけが final label と一致した細胞数です。

| study | source | informative_cells | coverage | final_concordance | high_conf_concordance | unique_support | discordant |
| --- | --- | --- | --- | --- | --- | --- | --- |
| infection_study_03 | CellTypist | 646,739 | 1.000 | 0.813 | 0.826 | 450 | 120,692 |
| infection_study_03 | Azimuth PBMC L2 | 646,739 | 1.000 | 0.708 | 0.723 | 71 | 188,739 |
| infection_study_03 | Azimuth PBMC L3 | 646,739 | 1.000 | 0.211 | 0.194 | 518 | 509,990 |
| infection_study_03 | Cluster marker assignment | 629,964 | 0.974 | 0.969 | 0.983 | 70,433 | 19,238 |
| infection_study_03 | Pan-human Azimuth | 609,674 | 0.943 | 0.700 | 0.693 | 3,908 | 183,179 |
| infection_study_03 | Cluster consensus | 0 | 0.000 | 0.000 | 0.000 | 0 | 0 |
| infection_study_03 | scRefMapping | 0 | 0.000 | 0.000 | 0.000 | 0 | 0 |

## レビュー優先事項

| study | concern | cells |
| --- | --- | --- |
| infection_study_03 | High source disagreement for Blood Cell | 1,965 |
| infection_study_03 | High dataset-level source disagreement | 134,542 |
| infection_study_03 | Large Blood Cell/ambiguous residual remains | 2,324 |

## ラベル構成

| study | predicted_cell_type | cells |
| --- | --- | --- |
| infection_study_03 | CD4 Naive / T Central Memory | 184,676 |
| infection_study_03 | Classical Monocyte | 130,556 |
| infection_study_03 | NK Cell | 102,938 |
| infection_study_03 | CD8 Cytotoxic / T Effector Memory | 102,353 |
| infection_study_03 | Naive B Cell | 61,829 |
| infection_study_03 | Platelet | 11,371 |
| infection_study_03 | Non-Classical Monocyte | 10,769 |
| infection_study_03 | CD8 Naive / T Central Memory | 9,049 |
| infection_study_03 | Plasma Cell | 8,842 |
| infection_study_03 | Conventional DC 2 | 8,329 |
| infection_study_03 | Memory B Cell | 6,291 |
| infection_study_03 | Plasmacytoid DC | 4,335 |
| infection_study_03 | HSC | 3,077 |
| infection_study_03 | Blood Cell | 2,324 |

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
| infection_study_03 | T_NK_lineage | 9 | 27,705 | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | NKT Cell | source_supported_marker_tiebreak | 0.655 | 1.000 | 0.345 | screfmapping_missing_for_scope |
| infection_study_03 | T_NK_lineage | 15 | 26,606 | CD4 Naive / T Central Memory | CD4 Naive / T Central Memory | CD4 Naive / T Central Memory | raw_marker_winner | 0.691 | 0.863 | 0.172 | screfmapping_missing_for_scope |
| infection_study_03 | T_NK_lineage | 25 | 25,842 | NK Cell | NK Cell | NKT Cell | source_supported_marker_tiebreak | 0.910 | 1.000 | 0.090 | screfmapping_missing_for_scope |
| infection_study_03 | T_NK_lineage | 11 | 24,421 | CD4 Naive / T Central Memory | CD4 Naive / T Central Memory | NKT Cell | source_supported_marker_tiebreak | 0.517 | 0.625 | 0.108 | screfmapping_missing_for_scope |
| infection_study_03 | T_NK_lineage | 4 | 20,786 | NK Cell | NK Cell | NKT Cell | source_supported_marker_tiebreak | 0.925 | 1.000 | 0.075 | screfmapping_missing_for_scope |
| infection_study_03 | T_NK_lineage | 20 | 20,390 | CD4 Naive / T Central Memory | CD4 Naive / T Central Memory | CD8 Naive / T Central Memory | source_supported_marker_tiebreak | 0.783 | 1.000 | 0.217 | screfmapping_missing_for_scope |
| infection_study_03 | T_NK_lineage | 12 | 20,022 | NK Cell | NK Cell | NKT Cell | source_supported_marker_tiebreak | 0.869 | 1.000 | 0.131 | screfmapping_missing_for_scope |
| infection_study_03 | T_NK_lineage | 7 | 19,134 | CD4 Naive / T Central Memory | CD4 Naive / T Central Memory | CD4 Naive / T Central Memory | raw_marker_winner | 0.815 | 1.000 | 0.185 | screfmapping_missing_for_scope |
| infection_study_03 | T_NK_lineage | 21 | 18,558 | CD4 Naive / T Central Memory | CD4 Naive / T Central Memory | NKT Cell | source_supported_marker_tiebreak | 0.715 | 0.844 | 0.129 | screfmapping_missing_for_scope |
| infection_study_03 | T_NK_lineage | 24 | 17,797 | CD4 Naive / T Central Memory | CD4 Naive / T Central Memory | CD4 Naive / T Central Memory | raw_marker_winner | 0.811 | 1.000 | 0.189 | screfmapping_missing_for_scope |
| infection_study_03 | T_NK_lineage | 14 | 16,189 | CD4 Naive / T Central Memory | CD4 Naive / T Central Memory | NKT Cell | source_supported_marker_tiebreak | 0.666 | 0.786 | 0.120 | screfmapping_missing_for_scope |
| infection_study_03 | B_lineage | 4 | 15,404 | Naive B Cell | Naive B Cell | Naive B Cell | raw_marker_winner | 0.687 | 0.943 | 0.256 | screfmapping_missing_for_scope |
| infection_study_03 | T_NK_lineage | 3 | 14,533 | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | NKT Cell | source_supported_marker_tiebreak | 0.762 | 1.000 | 0.238 | screfmapping_missing_for_scope |
| infection_study_03 | T_NK_lineage | 2 | 14,502 | CD4 Naive / T Central Memory | CD4 Naive / T Central Memory | NKT Cell | source_supported_marker_tiebreak | 0.736 | 0.892 | 0.156 | screfmapping_missing_for_scope |
| infection_study_03 | T_NK_lineage | 5 | 14,190 | CD4 Naive / T Central Memory | CD4 Naive / T Central Memory | NKT Cell | source_supported_marker_tiebreak | 0.773 | 0.913 | 0.140 | screfmapping_missing_for_scope |
| infection_study_03 | T_NK_lineage | 19 | 14,063 | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | NKT Cell | source_supported_marker_tiebreak | 0.642 | 1.000 | 0.358 | screfmapping_missing_for_scope |
| infection_study_03 | T_NK_lineage | 23 | 13,542 | NK Cell | NK Cell | NKT Cell | source_supported_marker_tiebreak | 0.871 | 1.000 | 0.129 | screfmapping_missing_for_scope |
| infection_study_03 | T_NK_lineage | 1 | 13,323 | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | raw_marker_winner | 0.684 | 1.000 | 0.316 | screfmapping_missing_for_scope |
| infection_study_03 | T_NK_lineage | 10 | 12,888 | CD4 Naive / T Central Memory | CD4 Naive / T Central Memory | NKT Cell | source_supported_marker_tiebreak | 0.743 | 0.924 | 0.181 | screfmapping_missing_for_scope |
| infection_study_03 | T_NK_lineage | 8 | 12,348 | NK Cell | NK Cell | NKT Cell | source_supported_marker_tiebreak | 0.880 | 1.000 | 0.120 | screfmapping_missing_for_scope |

## LLM Review Queue

この表は Codex/LLM が読むための subcluster-level review queue です。LLM はこの evidence を読んで、final label が妥当か、ontology にちょうどよい label がないのか、registry / conservative policy を一般ルールとして更新すべきかを提案します。LLM の出力で per-cell label を直接書き換えず、採用する場合は registry/config を更新して deterministic pipeline を再実行します。

| study | lineage | cluster | cells | priority | reasons | suggested_action | final_label | marker_assignment | raw_marker_winner | score_margin |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| infection_study_03 | T_NK_lineage | 18 | 8,386 | high | marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | NK Cell | NKT Cell | NKT Cell | 2.287 |
| infection_study_03 | B_lineage | 6 | 4,762 | high | marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | Plasma Cell | Plasmablast | Plasmablast | 0.220 |
| infection_study_03 | B_lineage | 1 | 4,080 | high | marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | Plasma Cell | Plasmablast | Plasmablast | 0.377 |
| infection_study_03 | T_NK_lineage | 17 | 2,010 | high | marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | NK Cell | NKT Cell | NKT Cell | 1.683 |
| infection_study_03 | T_NK_lineage | 9 | 27,705 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | NKT Cell | 2.374 |
| infection_study_03 | T_NK_lineage | 25 | 25,842 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | NK Cell | NK Cell | NKT Cell | 2.434 |
| infection_study_03 | T_NK_lineage | 11 | 24,421 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | CD4 Naive / T Central Memory | CD4 Naive / T Central Memory | NKT Cell | 2.042 |
| infection_study_03 | T_NK_lineage | 4 | 20,786 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | NK Cell | NK Cell | NKT Cell | 2.419 |
| infection_study_03 | T_NK_lineage | 12 | 20,022 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | NK Cell | NK Cell | NKT Cell | 2.425 |
| infection_study_03 | T_NK_lineage | 21 | 18,558 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | CD4 Naive / T Central Memory | CD4 Naive / T Central Memory | NKT Cell | 2.252 |
| infection_study_03 | T_NK_lineage | 14 | 16,189 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | CD4 Naive / T Central Memory | CD4 Naive / T Central Memory | NKT Cell | 1.662 |
| infection_study_03 | T_NK_lineage | 3 | 14,533 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | NKT Cell | 1.055 |
| infection_study_03 | T_NK_lineage | 2 | 14,502 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | CD4 Naive / T Central Memory | CD4 Naive / T Central Memory | NKT Cell | 0.500 |
| infection_study_03 | T_NK_lineage | 5 | 14,190 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | CD4 Naive / T Central Memory | CD4 Naive / T Central Memory | NKT Cell | 1.575 |
| infection_study_03 | T_NK_lineage | 19 | 14,063 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | NKT Cell | 2.471 |
| infection_study_03 | T_NK_lineage | 23 | 13,542 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | NK Cell | NK Cell | NKT Cell | 2.383 |
| infection_study_03 | T_NK_lineage | 10 | 12,888 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | CD4 Naive / T Central Memory | CD4 Naive / T Central Memory | NKT Cell | 1.349 |
| infection_study_03 | T_NK_lineage | 8 | 12,348 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | NK Cell | NK Cell | NKT Cell | 2.344 |
| infection_study_03 | T_NK_lineage | 16 | 10,318 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | NKT Cell | 1.957 |
| infection_study_03 | T_NK_lineage | 0 | 8,552 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | NKT Cell | 2.035 |

## Cluster Consensus Evidence

| study | lineage | cluster | cells | chosen_label | accepted | score_margin | cluster_marker_assignment | treg_key_any | treg_key_bonus | marker_set | marker_alert |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| infection_study_03 | B_lineage | 4 | 15,404 | Naive B Cell | True | 1.555 | Naive B Cell | nan | nan | B_naive | pass |
| infection_study_03 | B_lineage | 3 | 11,601 | Naive B Cell | True | 2.330 | Naive B Cell | nan | nan | B_naive | pass |
| infection_study_03 | B_lineage | 8 | 9,718 | Naive B Cell | True | 1.391 | Naive B Cell | nan | nan | B_naive | pass |
| infection_study_03 | B_lineage | 0 | 8,713 | Naive B Cell | True | 0.333 | Naive B Cell | nan | nan | B_naive | pass |
| infection_study_03 | B_lineage | 9 | 7,975 | Naive B Cell | True | 0.973 | Naive B Cell | nan | nan | B_naive | pass |
| infection_study_03 | B_lineage | 5 | 6,968 | Naive B Cell | True | 1.797 | Naive B Cell | nan | nan | B_naive | pass |
| infection_study_03 | B_lineage | 7 | 6,291 | Memory B Cell | True | 2.088 | Memory B Cell | nan | nan | B_memory_ABC | pass |
| infection_study_03 | B_lineage | 6 | 4,762 | Plasma Cell | True | 0.220 | Plasmablast | nan | nan | Plasma_ASC | pass |
| infection_study_03 | B_lineage | 1 | 4,080 | Plasma Cell | True | 0.377 | Plasmablast | nan | nan | Plasma_ASC | pass |
| infection_study_03 | B_lineage | 2 | 1,450 | Naive B Cell | True | 1.610 | Naive B Cell | nan | nan | B_naive | pass |
| infection_study_03 | Myeloid_lineage | 8 | 32,457 | Classical Monocyte | True | 2.611 | Classical Monocyte | nan | nan | registry__classical_monocyte | pass |
| infection_study_03 | Myeloid_lineage | 0 | 22,375 | Classical Monocyte | True | 2.527 | Classical Monocyte | nan | nan | registry__classical_monocyte | pass |
| infection_study_03 | Myeloid_lineage | 4 | 20,442 | Classical Monocyte | True | 2.396 | Classical Monocyte | nan | nan | registry__classical_monocyte | pass |
| infection_study_03 | Myeloid_lineage | 7 | 19,007 | Classical Monocyte | True | 1.245 | Classical Monocyte | nan | nan | registry__classical_monocyte | pass |
| infection_study_03 | Myeloid_lineage | 3 | 16,782 | Classical Monocyte | True | 2.203 | Classical Monocyte | nan | nan | registry__classical_monocyte | pass |
| infection_study_03 | Myeloid_lineage | 2 | 11,850 | Classical Monocyte | True | 2.165 | Classical Monocyte | nan | nan | registry__classical_monocyte | pass |
| infection_study_03 | Myeloid_lineage | 1 | 10,769 | Non-Classical Monocyte | True | 1.268 | Non-Classical Monocyte | nan | nan | registry__non_classical_monocyte | pass |
| infection_study_03 | Myeloid_lineage | 9 | 8,329 | Conventional DC 2 | True | 0.426 | Conventional DC 2 | nan | nan | registry__conventional_dc_2 | pass |
| infection_study_03 | Myeloid_lineage | 6 | 7,643 | Classical Monocyte | True | 2.232 | Classical Monocyte | nan | nan | registry__classical_monocyte | pass |
| infection_study_03 | Myeloid_lineage | 5 | 4,335 | Plasmacytoid DC | True | 2.505 | Plasmacytoid DC | nan | nan | registry__plasmacytoid_dc | pass |
| infection_study_03 | T_NK_lineage | 9 | 27,705 | CD8 Cytotoxic / T Effector Memory | True | 2.374 | CD8 Cytotoxic / T Effector Memory | 0.022 | 0.000 | registry__cd8_cytotoxic_t_effector_memory | pass |
| infection_study_03 | T_NK_lineage | 15 | 26,606 | CD4 Naive / T Central Memory | True | 1.959 | CD4 Naive / T Central Memory | 0.097 | 0.000 | CD4_naive_tcm | pass |
| infection_study_03 | T_NK_lineage | 25 | 25,842 | NK Cell | True | 2.434 | NK Cell | 0.005 | 0.000 | registry__nk_cell | pass |
| infection_study_03 | T_NK_lineage | 11 | 24,421 | CD4 Naive / T Central Memory | True | 2.042 | CD4 Naive / T Central Memory | 0.073 | 0.000 | CD4_naive_tcm | pass |
| infection_study_03 | T_NK_lineage | 4 | 20,786 | NK Cell | True | 2.419 | NK Cell | 0.004 | 0.000 | registry__nk_cell | pass |
| infection_study_03 | T_NK_lineage | 20 | 20,390 | CD4 Naive / T Central Memory | True | 1.106 | CD4 Naive / T Central Memory | 0.087 | 0.000 | CD4_naive_tcm | pass |
| infection_study_03 | T_NK_lineage | 12 | 20,022 | NK Cell | True | 2.425 | NK Cell | 0.007 | 0.000 | registry__nk_cell | pass |
| infection_study_03 | T_NK_lineage | 7 | 19,134 | CD4 Naive / T Central Memory | True | 2.531 | CD4 Naive / T Central Memory | 0.118 | 0.000 | CD4_naive_tcm | pass |
| infection_study_03 | T_NK_lineage | 21 | 18,558 | CD4 Naive / T Central Memory | True | 2.252 | CD4 Naive / T Central Memory | 0.108 | 0.000 | CD4_naive_tcm | pass |
| infection_study_03 | T_NK_lineage | 24 | 17,797 | CD4 Naive / T Central Memory | True | 1.880 | CD4 Naive / T Central Memory | 0.143 | 0.000 | CD4_naive_tcm | pass |

## 出力ファイル

- Submission TSVs: `outputs/submission_v25_harmony_reference_rescue/infection_study_03/submissions/`
- cellxgene H5ADs: `outputs/submission_v25_harmony_reference_rescue/infection_study_03/cellxgene/`
- Marker availability table: `outputs/submission_v25_harmony_reference_rescue/infection_study_03/tables/marker_gene_availability.tsv`
- Marker availability alerts: `outputs/submission_v25_harmony_reference_rescue/infection_study_03/tables/marker_gene_availability_alerts.tsv`
- Subcluster evidence: `outputs/submission_v25_harmony_reference_rescue/infection_study_03/tables/lineage_subcluster_evidence.tsv.gz`
- Source disagreement summary: `outputs/submission_v25_harmony_reference_rescue/infection_study_03/tables/source_disagreement_summary.tsv`
- Source effectiveness summary: `outputs/submission_v25_harmony_reference_rescue/infection_study_03/tables/source_effectiveness_summary.tsv`
- Diagnostics tables: `outputs/submission_v25_harmony_reference_rescue/infection_study_03/tables/`
