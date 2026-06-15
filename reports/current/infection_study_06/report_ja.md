# HIPC データセットアノテーションレポート: infection_study_06

更新日: 2026-06-15 EDT

このレポートは `hipc-annotation` Codex workflow によって生成したデータセット別レビュー文書です。固定 method は repository README に置き、このレポートでは実際の evidence、弱い箇所、レビュー優先度、UMAP / dotplot を確認します。

## データセット概要

| study | cells | analysis_X_genes | pre_hvg_genes | counts_layer_genes | labels | parent_or_blood_fraction | Blood Cell | Doublet | artifact_like | median_confidence | low_confidence | source_disagreement | invalid_labels |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| infection_study_06 | 827,389 | 37,298 | 37,298 | 37,298 | 16 | 0.002 | 1,794 | 0 | 3,400 | 0.807 | 25,705 | 140,313 (0.170) | none |

## 実行概要

- 実行単位: one dataset in, one annotated dataset out。
- 実行経路: Codex skill `hipc-annotation` -> bundled helper `run_one.sh` -> annotation CLI -> validator -> report inspection。
- 検証: submission row count、H5AD observation count、official label validity、H5AD/submission agreement、confidence column、report image link を確認する。
- このレポートは workflow の再掲ではなく、このデータセットの marker 欠損、UMAP、label 構成、review concern を読むためのもの。

## データセット固有の解釈

- `infection_study_06`: 827,389 cells、analysis X/var 37,298 genes、pre-HVG slot 37,298 genes、submitted label 16 種、parent/Blood residual fraction 0.002、median confidence 0.807。
  - 25,705 cells は low confidence。QC / confidence UMAP 上で局在を確認する。
  - 1,794 cells は `Blood Cell` として残存。これは filter-out ではなく、曖昧な細胞を公式 parent label で残したもの。

## データセット固有の評価

- 全体像: 827,389 cells / analysis X/var 37,298 genes / pre-HVG slot 37,298 genes。parent/Blood residual は 0.002、low-confidence は 25,705 cells、source disagreement flag は 140,313 cells (0.170)。
- 優先確認: low-confidence 領域が QC UMAP と source-disagreement UMAP で同じ場所に集まるかを確認する。
- 優先確認: `Blood Cell` 残存が孤立 cluster なのか、複数 lineage に分散した曖昧領域なのかを UMAP で確認する。

## Marker Gene 欠損アラート

なし。

## ソース間不一致

| study | predicted_cell_type | cells | median_source_agreement | disagreement_cells | disagreement_fraction |
| --- | --- | --- | --- | --- | --- |
| infection_study_06 | Blood Cell | 1,794 | 0.000 | 1,535 | 0.856 |
| infection_study_06 | Treg | 18,781 | 0.333 | 11,530 | 0.614 |
| infection_study_06 | Naive B Cell | 38,339 | 1.000 | 11,307 | 0.295 |
| infection_study_06 | CD4 T Effector Memory | 34,304 | 0.667 | 9,998 | 0.291 |
| infection_study_06 | Plasma Cell | 13,240 | 0.667 | 3,834 | 0.290 |
| infection_study_06 | Memory B Cell | 12,024 | 1.000 | 3,181 | 0.265 |
| infection_study_06 | CD4 Naive / T Central Memory | 226,620 | 1.000 | 57,575 | 0.254 |
| infection_study_06 | CD8 Cytotoxic / T Effector Memory | 102,955 | 1.000 | 20,200 | 0.196 |
| infection_study_06 | Conventional DC 2 | 5,848 | 1.000 | 821 | 0.140 |
| infection_study_06 | NK Cell | 75,888 | 1.000 | 7,017 | 0.092 |
| infection_study_06 | Non-Classical Monocyte | 23,278 | 1.000 | 1,171 | 0.050 |
| infection_study_06 | CD8 Naive / T Central Memory | 24,369 | 1.000 | 1,168 | 0.048 |

## アノテーションソース効果

この表は外部 ground truth に対する正解率ではありません。各 annotation source がどれだけの細胞で情報を持ち、final label とどれだけ一致したかを示す監査用統計です。`coverage` は source が `not_available` 以外を返した割合、`final_concordance` は informative cells の中で final label と一致した割合、`unique_support` はその source だけが final label と一致した細胞数です。

| study | source | informative_cells | coverage | final_concordance | high_conf_concordance | unique_support | discordant |
| --- | --- | --- | --- | --- | --- | --- | --- |
| infection_study_06 | CellTypist | 827,389 | 1.000 | 0.830 | 0.873 | 4,097 | 140,542 |
| infection_study_06 | Azimuth PBMC L2 | 827,389 | 1.000 | 0.824 | 0.871 | 584 | 145,761 |
| infection_study_06 | Azimuth PBMC L3 | 827,389 | 1.000 | 0.420 | 0.460 | 677 | 479,561 |
| infection_study_06 | Cluster marker assignment | 822,136 | 0.994 | 0.930 | 0.967 | 47,997 | 57,724 |
| infection_study_06 | Pan-human Azimuth | 803,559 | 0.971 | 0.766 | 0.806 | 7,632 | 188,253 |
| infection_study_06 | Cluster consensus | 0 | 0.000 | 0.000 | 0.000 | 0 | 0 |
| infection_study_06 | scRefMapping | 0 | 0.000 | 0.000 | 0.000 | 0 | 0 |

## レビュー優先事項

| study | concern | cells |
| --- | --- | --- |
| infection_study_06 | High source disagreement for Blood Cell | 1,535 |
| infection_study_06 | High source disagreement for Treg | 11,530 |
| infection_study_06 | Large Blood Cell/ambiguous residual remains | 1,794 |
| infection_study_06 | Many low-confidence cells; QC or mixed-marker effects likely remain | 25,705 |

## ラベル構成

| study | predicted_cell_type | cells |
| --- | --- | --- |
| infection_study_06 | Classical Monocyte | 243,884 |
| infection_study_06 | CD4 Naive / T Central Memory | 226,620 |
| infection_study_06 | CD8 Cytotoxic / T Effector Memory | 102,955 |
| infection_study_06 | NK Cell | 75,888 |
| infection_study_06 | Naive B Cell | 38,339 |
| infection_study_06 | CD4 T Effector Memory | 34,304 |
| infection_study_06 | CD8 Naive / T Central Memory | 24,369 |
| infection_study_06 | Non-Classical Monocyte | 23,278 |
| infection_study_06 | Treg | 18,781 |
| infection_study_06 | Plasma Cell | 13,240 |
| infection_study_06 | Memory B Cell | 12,024 |
| infection_study_06 | Conventional DC 2 | 5,848 |
| infection_study_06 | Plasmacytoid DC | 2,665 |
| infection_study_06 | HSC | 2,090 |
| infection_study_06 | Blood Cell | 1,794 |
| infection_study_06 | Platelet | 1,310 |

## Inline Figures

### infection_study_06

![infection_study_06 final labels](assets/umap_infection_study_06_annotation_label.png)

![infection_study_06 lineage and annotation reason](assets/umap_infection_study_06_annotation_lineage_reason.png)

![infection_study_06 QC and confidence](assets/umap_infection_study_06_annotation_qc_confidence.png)

![infection_study_06 source agreement and disagreement](assets/umap_infection_study_06_annotation_source_disagreement.png)

![infection_study_06 annotation-source effectiveness](assets/figure_02_source_effectiveness.png)

![infection_study_06 marker expression UMAPs](assets/umap_infection_study_06_annotation_marker_expression.png)

![infection_study_06 submitted-label marker dotplot](assets/dotplot_infection_study_06_annotation_marker_dotplot.png)

#### infection_study_06 B_lineage true subcluster UMAP

![infection_study_06 B_lineage true subcluster labels](assets/umap_infection_study_06_B_lineage_true_subcluster_label.png)

![infection_study_06 B_lineage true subcluster source labels](assets/umap_infection_study_06_B_lineage_true_subcluster_source_labels.png)

![infection_study_06 B_lineage true subcluster QC](assets/umap_infection_study_06_B_lineage_true_subcluster_qc.png)

![infection_study_06 B_lineage true subcluster marker scores](assets/umap_infection_study_06_B_lineage_true_subcluster_marker_scores.png)

![infection_study_06 B_lineage true subcluster marker expression](assets/umap_infection_study_06_B_lineage_true_subcluster_marker_expression.png)

![infection_study_06 B_lineage subcluster marker score heatmap](assets/subcluster_marker_score_heatmap_infection_study_06_B_lineage.png)

![infection_study_06 B_lineage subcluster marker dotplot](assets/dotplot_infection_study_06_B_lineage_true_subcluster_marker_dotplot.png)

Tables: `tables/infection_study_06_B_lineage_true_subcluster_umap.tsv.gz`, `tables/infection_study_06_B_lineage_subcluster_candidate_scores.tsv`.

#### infection_study_06 T_NK_lineage true subcluster UMAP

![infection_study_06 T_NK_lineage true subcluster labels](assets/umap_infection_study_06_T_NK_lineage_true_subcluster_label.png)

![infection_study_06 T_NK_lineage true subcluster source labels](assets/umap_infection_study_06_T_NK_lineage_true_subcluster_source_labels.png)

![infection_study_06 T_NK_lineage true subcluster QC](assets/umap_infection_study_06_T_NK_lineage_true_subcluster_qc.png)

![infection_study_06 T_NK_lineage true subcluster marker scores](assets/umap_infection_study_06_T_NK_lineage_true_subcluster_marker_scores.png)

![infection_study_06 T_NK_lineage true subcluster marker expression](assets/umap_infection_study_06_T_NK_lineage_true_subcluster_marker_expression.png)

![infection_study_06 T_NK_lineage subcluster marker score heatmap](assets/subcluster_marker_score_heatmap_infection_study_06_T_NK_lineage.png)

![infection_study_06 T_NK_lineage subcluster marker dotplot](assets/dotplot_infection_study_06_T_NK_lineage_true_subcluster_marker_dotplot.png)

Tables: `tables/infection_study_06_T_NK_lineage_true_subcluster_umap.tsv.gz`, `tables/infection_study_06_T_NK_lineage_subcluster_candidate_scores.tsv`.

#### infection_study_06 Myeloid_lineage true subcluster UMAP

![infection_study_06 Myeloid_lineage true subcluster labels](assets/umap_infection_study_06_Myeloid_lineage_true_subcluster_label.png)

![infection_study_06 Myeloid_lineage true subcluster source labels](assets/umap_infection_study_06_Myeloid_lineage_true_subcluster_source_labels.png)

![infection_study_06 Myeloid_lineage true subcluster QC](assets/umap_infection_study_06_Myeloid_lineage_true_subcluster_qc.png)

![infection_study_06 Myeloid_lineage true subcluster marker scores](assets/umap_infection_study_06_Myeloid_lineage_true_subcluster_marker_scores.png)

![infection_study_06 Myeloid_lineage true subcluster marker expression](assets/umap_infection_study_06_Myeloid_lineage_true_subcluster_marker_expression.png)

![infection_study_06 Myeloid_lineage subcluster marker score heatmap](assets/subcluster_marker_score_heatmap_infection_study_06_Myeloid_lineage.png)

![infection_study_06 Myeloid_lineage subcluster marker dotplot](assets/dotplot_infection_study_06_Myeloid_lineage_true_subcluster_marker_dotplot.png)

Tables: `tables/infection_study_06_Myeloid_lineage_true_subcluster_umap.tsv.gz`, `tables/infection_study_06_Myeloid_lineage_subcluster_candidate_scores.tsv`.


## Subcluster Marker Score Review

上の lineage-specific panel は、各 lineage subset で HVG 選択、PCA、neighbors、Leiden、UMAP を再計算した true local subcluster analysis から生成しています。Marker gene による fine label の確認は global UMAP だけではなく、この local UMAP、CellTypist/Azimuth/Pan-human/cluster-level marker gene assignment overlay、cluster marker gate score UMAP、marker-expression UMAP、dotplot を主に見ます。Treg など sparse marker label は cell-wise marker winner ではなく、local cluster の FOXP3/IL2RA/CTLA4 など key-marker support と reference support で判定します。

## Marker Assignment Feedback

Marker gene assignment は final label を強制的に上書きするものではなく、cluster-level の自己点検です。`raw_marker_winner` は marker score だけの勝者、`marker_assignment` は conservative policy と source-supported tie-break を通した marker-based assignment です。この表は marker assignment と final/reference-driven label がずれる cluster、marker specificity が弱い cluster、scRefMap が期待される lineage で欠落する cluster を示します。`marker_score` は raw marker base score から negative/confound marker penalty を差し引いた cluster-level marker gate score です。

| study | lineage | cluster | cells | chosen_label | marker_assignment | raw_marker_winner | assignment_reason | marker_score | base_score | penalty | flags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| infection_study_06 | T_NK_lineage | 15 | 40,632 | CD4 Naive / T Central Memory | CD4 Naive / T Central Memory | CD4 Naive / T Central Memory | raw_marker_winner | 0.835 | 1.000 | 0.165 | screfmapping_missing_for_scope |
| infection_study_06 | T_NK_lineage | 13 | 32,373 | CD4 Naive / T Central Memory | CD4 Naive / T Central Memory | CD4 Naive / T Central Memory | raw_marker_winner | 0.848 | 1.000 | 0.152 | screfmapping_missing_for_scope |
| infection_study_06 | T_NK_lineage | 28 | 28,775 | CD4 Naive / T Central Memory | CD4 Naive / T Central Memory | CD4 Naive / T Central Memory | raw_marker_winner | 0.830 | 1.000 | 0.170 | screfmapping_missing_for_scope |
| infection_study_06 | T_NK_lineage | 25 | 25,299 | CD4 Naive / T Central Memory | CD4 Naive / T Central Memory | NKT Cell | source_supported_marker_tiebreak | 0.816 | 0.930 | 0.114 | screfmapping_missing_for_scope |
| infection_study_06 | T_NK_lineage | 1 | 25,257 | CD4 Naive / T Central Memory | CD4 Naive / T Central Memory | CD4 Naive / T Central Memory | raw_marker_winner | 0.857 | 1.000 | 0.143 | screfmapping_missing_for_scope |
| infection_study_06 | T_NK_lineage | 12 | 24,369 | CD8 Naive / T Central Memory | CD8 Naive / T Central Memory | CD8 Naive / T Central Memory | raw_marker_winner | 0.793 | 1.000 | 0.207 | screfmapping_missing_for_scope |
| infection_study_06 | T_NK_lineage | 31 | 23,911 | CD4 T Effector Memory | NKT Cell | NKT Cell | raw_marker_winner | 0.776 | 0.921 | 0.145 | marker_final_disagreement;screfmapping_missing_for_scope |
| infection_study_06 | T_NK_lineage | 5 | 19,617 | CD4 Naive / T Central Memory | CD4 Naive / T Central Memory | CD4 Naive / T Central Memory | raw_marker_winner | 0.741 | 1.000 | 0.259 | screfmapping_missing_for_scope |
| infection_study_06 | T_NK_lineage | 30 | 16,930 | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | raw_marker_winner | 0.542 | 1.000 | 0.458 | screfmapping_missing_for_scope |
| infection_study_06 | T_NK_lineage | 27 | 16,472 | CD4 Naive / T Central Memory | CD4 Naive / T Central Memory | NKT Cell | source_supported_marker_tiebreak | 0.800 | 0.894 | 0.094 | screfmapping_missing_for_scope |
| infection_study_06 | T_NK_lineage | 23 | 16,156 | NK Cell | NK Cell | NKT Cell | source_supported_marker_tiebreak | 0.860 | 1.000 | 0.140 | screfmapping_missing_for_scope |
| infection_study_06 | T_NK_lineage | 21 | 15,319 | CD4 Naive / T Central Memory | CD4 Naive / T Central Memory | NKT Cell | source_supported_marker_tiebreak | 0.776 | 0.902 | 0.126 | screfmapping_missing_for_scope |
| infection_study_06 | T_NK_lineage | 18 | 15,014 | CD4 Naive / T Central Memory | CD4 Naive / T Central Memory | NKT Cell | source_supported_marker_tiebreak | 0.788 | 0.901 | 0.113 | screfmapping_missing_for_scope |
| infection_study_06 | T_NK_lineage | 29 | 14,776 | NK Cell | NK Cell | NKT Cell | source_supported_marker_tiebreak | 0.855 | 1.000 | 0.145 | screfmapping_missing_for_scope |
| infection_study_06 | T_NK_lineage | 0 | 14,466 | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | raw_marker_winner | 0.616 | 1.000 | 0.384 | screfmapping_missing_for_scope |
| infection_study_06 | T_NK_lineage | 4 | 13,775 | Treg | Treg | NKT Cell | source_supported_marker_tiebreak | 0.867 | 0.970 | 0.103 | screfmapping_missing_for_scope |
| infection_study_06 | T_NK_lineage | 24 | 12,997 | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | raw_marker_winner | 0.594 | 1.000 | 0.406 | screfmapping_missing_for_scope |
| infection_study_06 | T_NK_lineage | 19 | 12,958 | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | NKT Cell | source_supported_marker_tiebreak | 0.630 | 1.000 | 0.370 | screfmapping_missing_for_scope |
| infection_study_06 | T_NK_lineage | 9 | 12,264 | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | NKT Cell | source_supported_marker_tiebreak | 0.732 | 1.000 | 0.268 | screfmapping_missing_for_scope |
| infection_study_06 | B_lineage | 5 | 12,024 | Memory B Cell | Memory B Cell | Memory B Cell | raw_marker_winner | 0.297 | 0.652 | 0.355 | weak_marker_specificity;screfmapping_missing_for_scope |

## LLM Review Queue

この表は Codex/LLM が読むための subcluster-level review queue です。LLM はこの evidence を読んで、final label が妥当か、ontology にちょうどよい label がないのか、registry / conservative policy を一般ルールとして更新すべきかを提案します。LLM の出力で per-cell label を直接書き換えず、採用する場合は registry/config を更新して deterministic pipeline を再実行します。

| study | lineage | cluster | cells | priority | reasons | suggested_action | final_label | marker_assignment | raw_marker_winner | score_margin |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| infection_study_06 | T_NK_lineage | 31 | 23,911 | high | marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | CD4 T Effector Memory | NKT Cell | NKT Cell | 0.115 |
| infection_study_06 | T_NK_lineage | 14 | 11,232 | high | marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | NK Cell | NKT Cell | NKT Cell | 2.009 |
| infection_study_06 | T_NK_lineage | 8 | 10,393 | high | marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | CD4 T Effector Memory | NKT Cell | NKT Cell | 0.517 |
| infection_study_06 | T_NK_lineage | 22 | 7,183 | high | marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | NK Cell | NKT Cell | NKT Cell | 2.327 |
| infection_study_06 | T_NK_lineage | 20 | 5,005 | high | marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | Treg | NKT Cell | NKT Cell | 0.673 |
| infection_study_06 | T_NK_lineage | 25 | 25,299 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | CD4 Naive / T Central Memory | CD4 Naive / T Central Memory | NKT Cell | 0.278 |
| infection_study_06 | T_NK_lineage | 27 | 16,472 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | CD4 Naive / T Central Memory | CD4 Naive / T Central Memory | NKT Cell | 0.456 |
| infection_study_06 | T_NK_lineage | 23 | 16,156 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | NK Cell | NK Cell | NKT Cell | 2.445 |
| infection_study_06 | T_NK_lineage | 21 | 15,319 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | CD4 Naive / T Central Memory | CD4 Naive / T Central Memory | NKT Cell | 0.369 |
| infection_study_06 | T_NK_lineage | 18 | 15,014 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | CD4 Naive / T Central Memory | CD4 Naive / T Central Memory | NKT Cell | 2.021 |
| infection_study_06 | T_NK_lineage | 29 | 14,776 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | NK Cell | NK Cell | NKT Cell | 2.449 |
| infection_study_06 | T_NK_lineage | 4 | 13,775 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | Treg | Treg | NKT Cell | 0.714 |
| infection_study_06 | T_NK_lineage | 19 | 12,958 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | NKT Cell | 2.484 |
| infection_study_06 | T_NK_lineage | 9 | 12,264 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | NKT Cell | 2.140 |
| infection_study_06 | T_NK_lineage | 16 | 9,471 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | NKT Cell | 1.802 |
| infection_study_06 | B_lineage | 8 | 8,097 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | Naive B Cell | Naive B Cell | Plasmablast | 1.507 |
| infection_study_06 | T_NK_lineage | 2 | 8,041 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | NK Cell | NK Cell | NKT Cell | 2.408 |
| infection_study_06 | T_NK_lineage | 10 | 7,828 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | CD4 Naive / T Central Memory | CD4 Naive / T Central Memory | NKT Cell | 0.548 |
| infection_study_06 | T_NK_lineage | 3 | 7,493 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | NKT Cell | 2.527 |
| infection_study_06 | T_NK_lineage | 11 | 7,075 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | NK Cell | NK Cell | NKT Cell | 1.985 |

## Cluster Consensus Evidence

| study | lineage | cluster | cells | chosen_label | accepted | score_margin | cluster_marker_assignment | treg_key_any | treg_key_bonus | marker_set | marker_alert |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| infection_study_06 | B_lineage | 5 | 12,024 | Memory B Cell | True | 1.863 | Memory B Cell | nan | nan | B_memory_ABC | pass |
| infection_study_06 | B_lineage | 0 | 10,143 | Naive B Cell | True | 1.622 | Naive B Cell | nan | nan | B_naive | pass |
| infection_study_06 | B_lineage | 1 | 10,113 | Naive B Cell | True | 2.292 | Naive B Cell | nan | nan | B_naive | pass |
| infection_study_06 | B_lineage | 8 | 8,097 | Naive B Cell | True | 1.507 | Naive B Cell | nan | nan | B_naive | pass |
| infection_study_06 | B_lineage | 4 | 5,689 | Naive B Cell | True | 1.101 | Naive B Cell | nan | nan | B_naive | pass |
| infection_study_06 | B_lineage | 3 | 4,484 | Plasma Cell | True | 0.618 | Plasma Cell | nan | nan | Plasma_ASC | pass |
| infection_study_06 | B_lineage | 7 | 4,297 | Naive B Cell | True | 1.627 | Naive B Cell | nan | nan | B_naive | pass |
| infection_study_06 | B_lineage | 6 | 3,627 | Plasma Cell | True | 0.560 | Plasma Cell | nan | nan | Plasma_ASC | pass |
| infection_study_06 | B_lineage | 9 | 3,287 | Plasma Cell | True | 0.421 | Plasma Cell | nan | nan | Plasma_ASC | pass |
| infection_study_06 | B_lineage | 2 | 1,842 | Plasma Cell | True | 0.736 | Plasma Cell | nan | nan | Plasma_ASC | pass |
| infection_study_06 | Myeloid_lineage | 3 | 23,278 | Non-Classical Monocyte | True | 1.497 | Non-Classical Monocyte | nan | nan | registry__non_classical_monocyte | pass |
| infection_study_06 | Myeloid_lineage | 13 | 22,911 | Classical Monocyte | True | 2.841 | Classical Monocyte | nan | nan | registry__classical_monocyte | pass |
| infection_study_06 | Myeloid_lineage | 4 | 22,345 | Classical Monocyte | True | 2.641 | Classical Monocyte | nan | nan | registry__classical_monocyte | pass |
| infection_study_06 | Myeloid_lineage | 11 | 17,976 | Classical Monocyte | True | 2.373 | Classical Monocyte | nan | nan | registry__classical_monocyte | pass |
| infection_study_06 | Myeloid_lineage | 8 | 17,756 | Classical Monocyte | True | 2.487 | Classical Monocyte | nan | nan | registry__classical_monocyte | pass |
| infection_study_06 | Myeloid_lineage | 16 | 17,731 | Classical Monocyte | True | 2.680 | Classical Monocyte | nan | nan | registry__classical_monocyte | pass |
| infection_study_06 | Myeloid_lineage | 15 | 17,304 | Classical Monocyte | True | 2.439 | Classical Monocyte | nan | nan | registry__classical_monocyte | pass |
| infection_study_06 | Myeloid_lineage | 14 | 16,771 | Classical Monocyte | True | 2.533 | Classical Monocyte | nan | nan | registry__classical_monocyte | pass |
| infection_study_06 | Myeloid_lineage | 9 | 16,684 | Classical Monocyte | True | 2.620 | Classical Monocyte | nan | nan | registry__classical_monocyte | pass |
| infection_study_06 | Myeloid_lineage | 0 | 16,465 | Classical Monocyte | True | 2.715 | Classical Monocyte | nan | nan | registry__classical_monocyte | pass |
| infection_study_06 | Myeloid_lineage | 1 | 15,636 | Classical Monocyte | True | 1.048 | Classical Monocyte | nan | nan | registry__classical_monocyte | pass |
| infection_study_06 | Myeloid_lineage | 6 | 15,022 | Classical Monocyte | True | 2.404 | Classical Monocyte | nan | nan | registry__classical_monocyte | pass |
| infection_study_06 | Myeloid_lineage | 12 | 14,441 | Classical Monocyte | True | 1.551 | Classical Monocyte | nan | nan | registry__classical_monocyte | pass |
| infection_study_06 | Myeloid_lineage | 2 | 11,841 | Classical Monocyte | True | 2.490 | Classical Monocyte | nan | nan | registry__classical_monocyte | pass |
| infection_study_06 | Myeloid_lineage | 17 | 11,457 | Classical Monocyte | True | 2.332 | Classical Monocyte | nan | nan | registry__classical_monocyte | pass |
| infection_study_06 | Myeloid_lineage | 7 | 9,531 | Classical Monocyte | True | 2.756 | Classical Monocyte | nan | nan | registry__classical_monocyte | pass |
| infection_study_06 | Myeloid_lineage | 5 | 5,848 | Conventional DC 2 | True | 2.017 | Conventional DC 2 | nan | nan | registry__conventional_dc_2 | pass |
| infection_study_06 | Myeloid_lineage | 10 | 2,665 | Plasmacytoid DC | True | 2.493 | Plasmacytoid DC | nan | nan | registry__plasmacytoid_dc | pass |
| infection_study_06 | T_NK_lineage | 15 | 40,632 | CD4 Naive / T Central Memory | True | 2.516 | CD4 Naive / T Central Memory | 0.082 | 0.000 | CD4_naive_tcm | pass |
| infection_study_06 | T_NK_lineage | 13 | 32,373 | CD4 Naive / T Central Memory | True | 2.482 | CD4 Naive / T Central Memory | 0.118 | 0.000 | CD4_naive_tcm | pass |

## 出力ファイル

- Submission TSVs: `outputs/submission_v25_harmony_reference_rescue/infection_study_06/submissions/`
- cellxgene H5ADs: `outputs/submission_v25_harmony_reference_rescue/infection_study_06/cellxgene/`
- Marker availability table: `outputs/submission_v25_harmony_reference_rescue/infection_study_06/tables/marker_gene_availability.tsv`
- Marker availability alerts: `outputs/submission_v25_harmony_reference_rescue/infection_study_06/tables/marker_gene_availability_alerts.tsv`
- Subcluster evidence: `outputs/submission_v25_harmony_reference_rescue/infection_study_06/tables/lineage_subcluster_evidence.tsv.gz`
- Source disagreement summary: `outputs/submission_v25_harmony_reference_rescue/infection_study_06/tables/source_disagreement_summary.tsv`
- Source effectiveness summary: `outputs/submission_v25_harmony_reference_rescue/infection_study_06/tables/source_effectiveness_summary.tsv`
- Diagnostics tables: `outputs/submission_v25_harmony_reference_rescue/infection_study_06/tables/`

