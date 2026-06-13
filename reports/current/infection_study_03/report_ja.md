# HIPC データセットアノテーションレポート: infection_study_03

更新日: 2026-06-12 EDT

## 現行提出用サマリー

| 項目 | 内容 |
| --- | --- |
| 提出候補 package | v24 pragmatic package |
| 採用 source | `outputs/submission_v23_marker_rescue_scavenge/infection_study_03/submissions/infection_study_03_annotation.tsv` |
| 細胞数 | 646,739 |
| label 数 | 7 |
| parent/Blood residual | 541,914 cells (0.8379) |
| median confidence | 0.4449 |
| 上位 label | Blood Cell: 215,358; T Cell: 166,643; Myeloid Cell: 137,561; Naive B Cell: 64,711; NKT Cell: 33,326; B Cell: 22,352; Plasmablast: 6,788 |
| 現状判断 | 提出候補には含めるが低信頼。broad parent / Blood Cell が多く、Harmony などの batch-corrected clustering で再評価する必要がある。 |

このレポートは `hipc-annotation` Codex workflow によって生成したデータセット別レビュー文書です。固定 method は repository README に置き、このレポートでは実際の evidence、弱い箇所、レビュー優先度、UMAP / dotplot を確認します。

## 2026-06-12 提出候補メモ

- 現行の緊急提出候補では、この dataset は v23 aggressive marker-rescue output を採用しています。
- ただし結果はまだ悪く、parent/Blood residual fraction は 0.8379 と高いです。`Blood Cell`, `T Cell`, `Myeloid Cell`, `B Cell` が大量に残っており、fine annotation まで分解できていません。
- CellTypist / Pan-human Azimuth / scRefMapping の usable evidence がこの run ではほぼ欠落しているため、marker/subcluster evidence に依存しています。
- 次に改善するなら、Harmony などで batch-corrected embedding を作り直し、そこで neighbor graph / Leiden / UMAP / cluster-level marker evidence を再計算する必要があります。

## データセット概要

| study | cells | analysis_X_genes | pre_hvg_genes | counts_layer_genes | labels | parent_or_blood_fraction | Blood Cell | Doublet | artifact_like | median_confidence | low_confidence | source_disagreement | invalid_labels |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| infection_study_03 | 646,739 | 24,929 | 24,929 | 24,929 | 7 | 0.838 | 215,358 | 0 | 0 | 0.445 | 646,739 | 0 (0.000) | none |

## 実行概要

- 実行単位: one dataset in, one annotated dataset out。
- 実行経路: Codex skill `hipc-annotation` -> bundled helper `run_one.sh` -> annotation CLI -> validator -> report inspection。
- 検証: submission row count、H5AD observation count、official label validity、H5AD/submission agreement、confidence column、report image link を確認する。
- このレポートは workflow の再掲ではなく、このデータセットの marker 欠損、UMAP、label 構成、review concern を読むためのもの。

## データセット固有の解釈

- `infection_study_03`: 646,739 cells、analysis X/var 24,929 genes、pre-HVG slot 24,929 genes、submitted label 7 種、parent/Blood residual fraction 0.838、median confidence 0.445。
  - 646,739 cells は low confidence。QC / confidence UMAP 上で局在を確認する。
  - 215,358 cells は `Blood Cell` として残存。これは filter-out ではなく、曖昧な細胞を公式 parent label で残したもの。

## データセット固有の評価

- 全体像: 646,739 cells / analysis X/var 24,929 genes / pre-HVG slot 24,929 genes。parent/Blood residual は 0.838、low-confidence は 646,739 cells、source disagreement flag は 0 cells (0.000)。
- 優先確認: low-confidence 領域が QC UMAP と source-disagreement UMAP で同じ場所に集まるかを確認する。
- 優先確認: `Blood Cell` 残存が孤立 cluster なのか、複数 lineage に分散した曖昧領域なのかを UMAP で確認する。

## Marker Gene 欠損アラート

なし。

## ソース間不一致

| study | predicted_cell_type | cells | median_source_agreement | disagreement_cells | disagreement_fraction |
| --- | --- | --- | --- | --- | --- |
| infection_study_03 | B Cell | 22,352 | 0.000 | 0 | 0.000 |
| infection_study_03 | Blood Cell | 215,358 | 0.000 | 0 | 0.000 |
| infection_study_03 | Myeloid Cell | 137,561 | 0.000 | 0 | 0.000 |
| infection_study_03 | NKT Cell | 33,326 | 0.000 | 0 | 0.000 |
| infection_study_03 | Naive B Cell | 64,711 | 0.000 | 0 | 0.000 |
| infection_study_03 | Plasmablast | 6,788 | 0.000 | 0 | 0.000 |
| infection_study_03 | T Cell | 166,643 | 0.000 | 0 | 0.000 |

## アノテーションソース効果

この表は外部 ground truth に対する正解率ではありません。各 annotation source がどれだけの細胞で情報を持ち、final label とどれだけ一致したかを示す監査用統計です。`coverage` は source が `not_available` 以外を返した割合、`final_concordance` は informative cells の中で final label と一致した割合、`unique_support` はその source だけが final label と一致した細胞数です。

| study | source | informative_cells | coverage | final_concordance | high_conf_concordance | unique_support | discordant |
| --- | --- | --- | --- | --- | --- | --- | --- |
| infection_study_03 | Cluster marker assignment | 431,381 | 0.667 | 0.243 | 0.000 | 104,825 | 326,556 |
| infection_study_03 | CellTypist | 0 | 0.000 | 0.000 | 0.000 | 0 | 0 |
| infection_study_03 | Pan-human Azimuth | 0 | 0.000 | 0.000 | 0.000 | 0 | 0 |
| infection_study_03 | Cluster consensus | 0 | 0.000 | 0.000 | 0.000 | 0 | 0 |
| infection_study_03 | scRefMapping | 0 | 0.000 | 0.000 | 0.000 | 0 | 0 |

## レビュー優先事項

| study | concern | cells |
| --- | --- | --- |
| infection_study_03 | Large Blood Cell/ambiguous residual remains | 215,358 |
| infection_study_03 | Many low-confidence cells; QC or mixed-marker effects likely remain | 646,739 |

## ラベル構成

| study | predicted_cell_type | cells |
| --- | --- | --- |
| infection_study_03 | Blood Cell | 215,358 |
| infection_study_03 | T Cell | 166,643 |
| infection_study_03 | Myeloid Cell | 137,561 |
| infection_study_03 | Naive B Cell | 64,711 |
| infection_study_03 | NKT Cell | 33,326 |
| infection_study_03 | B Cell | 22,352 |
| infection_study_03 | Plasmablast | 6,788 |

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
| infection_study_03 | Myeloid_lineage | 7 | 33,932 | Myeloid Cell | Classical Monocyte | Classical Monocyte | raw_marker_winner | 0.596 | 1.000 | 0.404 | marker_final_disagreement |
| infection_study_03 | T_NK_lineage | 5 | 25,968 | T Cell | NKT Cell | NKT Cell | raw_marker_winner | 0.775 | 0.942 | 0.167 | marker_final_disagreement;screfmapping_missing_for_scope |
| infection_study_03 | B_lineage | 4 | 24,451 | Naive B Cell | Naive B Cell | Naive B Cell | raw_marker_winner | 0.728 | 1.000 | 0.272 | screfmapping_missing_for_scope |
| infection_study_03 | T_NK_lineage | 3 | 24,218 | T Cell | NKT Cell | NKT Cell | raw_marker_winner | 0.639 | 1.000 | 0.361 | marker_final_disagreement;screfmapping_missing_for_scope |
| infection_study_03 | Myeloid_lineage | 9 | 21,420 | Myeloid Cell | Eosinophil | Eosinophil | raw_marker_winner | 0.546 | 1.000 | 0.454 | marker_final_disagreement |
| infection_study_03 | T_NK_lineage | 2 | 21,324 | T Cell | NKT Cell | NKT Cell | raw_marker_winner | 0.745 | 0.956 | 0.210 | marker_final_disagreement;screfmapping_missing_for_scope |
| infection_study_03 | Myeloid_lineage | 0 | 19,475 | Myeloid Cell | Neutrophil | Neutrophil | raw_marker_winner | 0.544 | 1.000 | 0.456 | marker_final_disagreement |
| infection_study_03 | Myeloid_lineage | 5 | 17,535 | Myeloid Cell | Neutrophil | Neutrophil | raw_marker_winner | 0.546 | 1.000 | 0.454 | marker_final_disagreement |
| infection_study_03 | T_NK_lineage | 0 | 17,363 | T Cell | NKT Cell | NKT Cell | raw_marker_winner | 0.797 | 0.965 | 0.167 | marker_final_disagreement;screfmapping_missing_for_scope |
| infection_study_03 | T_NK_lineage | 12 | 16,459 | NKT Cell | NKT Cell | NKT Cell | raw_marker_winner | 0.894 | 1.000 | 0.106 | screfmapping_missing_for_scope |
| infection_study_03 | T_NK_lineage | 4 | 15,652 | NKT Cell | NKT Cell | NKT Cell | raw_marker_winner | 0.855 | 1.000 | 0.145 | screfmapping_missing_for_scope |
| infection_study_03 | T_NK_lineage | 10 | 15,033 | T Cell | NKT Cell | NKT Cell | raw_marker_winner | 0.731 | 0.978 | 0.247 | marker_final_disagreement;screfmapping_missing_for_scope |
| infection_study_03 | T_NK_lineage | 1 | 14,371 | T Cell | NKT Cell | NKT Cell | raw_marker_winner | 0.677 | 1.000 | 0.323 | marker_final_disagreement;screfmapping_missing_for_scope |
| infection_study_03 | B_lineage | 1 | 14,216 | Naive B Cell | Naive B Cell | Naive B Cell | raw_marker_winner | 0.652 | 1.000 | 0.348 | screfmapping_missing_for_scope |
| infection_study_03 | T_NK_lineage | 9 | 14,010 | T Cell | NKT Cell | NKT Cell | raw_marker_winner | 0.834 | 0.954 | 0.120 | marker_final_disagreement;screfmapping_missing_for_scope |
| infection_study_03 | B_lineage | 0 | 13,682 | Naive B Cell | Naive B Cell | Naive B Cell | raw_marker_winner | 0.627 | 1.000 | 0.373 | screfmapping_missing_for_scope |
| infection_study_03 | Myeloid_lineage | 2 | 13,119 | Myeloid Cell | Neutrophil | Neutrophil | raw_marker_winner | 0.555 | 1.000 | 0.445 | marker_final_disagreement |
| infection_study_03 | Myeloid_lineage | 3 | 12,903 | Myeloid Cell | Neutrophil | Neutrophil | raw_marker_winner | 0.528 | 1.000 | 0.472 | marker_final_disagreement |
| infection_study_03 | T_NK_lineage | 11 | 12,271 | T Cell | NKT Cell | NKT Cell | raw_marker_winner | 0.626 | 1.000 | 0.374 | marker_final_disagreement;screfmapping_missing_for_scope |
| infection_study_03 | T_NK_lineage | 8 | 11,953 | T Cell | NKT Cell | NKT Cell | raw_marker_winner | 0.637 | 1.000 | 0.363 | marker_final_disagreement;screfmapping_missing_for_scope |

## LLM Review Queue

この表は Codex/LLM が読むための subcluster-level review queue です。LLM はこの evidence を読んで、final label が妥当か、ontology にちょうどよい label がないのか、registry / conservative policy を一般ルールとして更新すべきかを提案します。LLM の出力で per-cell label を直接書き換えず、採用する場合は registry/config を更新して deterministic pipeline を再実行します。

| study | lineage | cluster | cells | priority | reasons | suggested_action | final_label | marker_assignment | raw_marker_winner | score_margin |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| infection_study_03 | T_NK_lineage | 5 | 25,968 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | T Cell | NKT Cell | NKT Cell | 0.046 |
| infection_study_03 | T_NK_lineage | 3 | 24,218 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | T Cell | NKT Cell | NKT Cell | 0.023 |
| infection_study_03 | T_NK_lineage | 2 | 21,324 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | T Cell | NKT Cell | NKT Cell | 0.038 |
| infection_study_03 | T_NK_lineage | 0 | 17,363 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | T Cell | NKT Cell | NKT Cell | 0.063 |
| infection_study_03 | T_NK_lineage | 10 | 15,033 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | T Cell | NKT Cell | NKT Cell | 0.062 |
| infection_study_03 | T_NK_lineage | 1 | 14,371 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | T Cell | NKT Cell | NKT Cell | 0.023 |
| infection_study_03 | T_NK_lineage | 9 | 14,010 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | T Cell | NKT Cell | NKT Cell | 0.055 |
| infection_study_03 | T_NK_lineage | 11 | 12,271 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | T Cell | NKT Cell | NKT Cell | 0.090 |
| infection_study_03 | T_NK_lineage | 8 | 11,953 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | T Cell | NKT Cell | NKT Cell | 0.046 |
| infection_study_03 | B_lineage | 3 | 10,455 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | B Cell | Plasmablast | Plasmablast | 0.009 |
| infection_study_03 | T_NK_lineage | 7 | 10,132 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | T Cell | NKT Cell | NKT Cell | 0.090 |
| infection_study_03 | B_lineage | 5 | 9,079 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | B Cell | Plasma Cell | Plasma Cell | 0.009 |
| infection_study_03 | B_lineage | 8 | 2,818 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | B Cell | Plasmablast | Plasmablast | 0.143 |
| infection_study_03 | Myeloid_lineage | 7 | 33,932 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | Myeloid Cell | Classical Monocyte | Classical Monocyte | 0.031 |
| infection_study_03 | Myeloid_lineage | 9 | 21,420 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | Myeloid Cell | Eosinophil | Eosinophil | 0.002 |
| infection_study_03 | Myeloid_lineage | 0 | 19,475 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | Myeloid Cell | Neutrophil | Neutrophil | 0.063 |
| infection_study_03 | Myeloid_lineage | 5 | 17,535 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | Myeloid Cell | Neutrophil | Neutrophil | 0.049 |
| infection_study_03 | Myeloid_lineage | 2 | 13,119 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | Myeloid Cell | Neutrophil | Neutrophil | 0.110 |
| infection_study_03 | Myeloid_lineage | 3 | 12,903 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | Myeloid Cell | Neutrophil | Neutrophil | 0.056 |
| infection_study_03 | Myeloid_lineage | 1 | 9,064 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | Myeloid Cell | Neutrophil | Neutrophil | 0.081 |

## Cluster Consensus Evidence

| study | lineage | cluster | cells | chosen_label | accepted | score_margin | cluster_marker_assignment | treg_key_any | treg_key_bonus | marker_set | marker_alert |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| infection_study_03 | B_lineage | 4 | 24,451 | Naive B Cell | True | 0.728 | Naive B Cell | nan | nan | registry__naive_b_cell | pass |
| infection_study_03 | B_lineage | 1 | 14,216 | Naive B Cell | True | 0.644 | Naive B Cell | nan | nan | registry__naive_b_cell | pass |
| infection_study_03 | B_lineage | 0 | 13,682 | Naive B Cell | True | 0.587 | Naive B Cell | nan | nan | registry__naive_b_cell | pass |
| infection_study_03 | B_lineage | 6 | 11,147 | Naive B Cell | True | 0.630 | Naive B Cell | nan | nan | registry__naive_b_cell | pass |
| infection_study_03 | B_lineage | 3 | 10,455 | B Cell | False | 0.009 | Plasmablast | nan | nan | registry__plasmablast | pass |
| infection_study_03 | B_lineage | 5 | 9,079 | B Cell | False | 0.009 | Plasma Cell | nan | nan | registry__plasma_cell | pass |
| infection_study_03 | B_lineage | 2 | 4,095 | Plasmablast | True | 0.171 | Plasmablast | nan | nan | registry__plasmablast | pass |
| infection_study_03 | B_lineage | 8 | 2,818 | B Cell | False | 0.143 | Plasmablast | nan | nan | registry__plasmablast | pass |
| infection_study_03 | B_lineage | 7 | 2,693 | Plasmablast | True | 0.219 | Plasmablast | nan | nan | registry__plasmablast | pass |
| infection_study_03 | B_lineage | 9 | 1,215 | Naive B Cell | True | 0.487 | Naive B Cell | nan | nan | registry__naive_b_cell | pass |
| infection_study_03 | Myeloid_lineage | 7 | 33,932 | Myeloid Cell | False | 0.031 | Classical Monocyte | nan | nan | registry__classical_monocyte | pass |
| infection_study_03 | Myeloid_lineage | 9 | 21,420 | Myeloid Cell | False | 0.002 | Eosinophil | nan | nan | registry__eosinophil | pass |
| infection_study_03 | Myeloid_lineage | 0 | 19,475 | Myeloid Cell | False | 0.063 | Neutrophil | nan | nan | registry__neutrophil | pass |
| infection_study_03 | Myeloid_lineage | 5 | 17,535 | Myeloid Cell | False | 0.049 | Neutrophil | nan | nan | registry__neutrophil | pass |
| infection_study_03 | Myeloid_lineage | 2 | 13,119 | Myeloid Cell | False | 0.110 | Neutrophil | nan | nan | registry__neutrophil | pass |
| infection_study_03 | Myeloid_lineage | 3 | 12,903 | Myeloid Cell | False | 0.056 | Neutrophil | nan | nan | registry__neutrophil | pass |
| infection_study_03 | Myeloid_lineage | 1 | 9,064 | Myeloid Cell | False | 0.081 | Neutrophil | nan | nan | registry__neutrophil | pass |
| infection_study_03 | Myeloid_lineage | 6 | 4,836 | Myeloid Cell | False | 0.071 | Neutrophil | nan | nan | registry__neutrophil | pass |
| infection_study_03 | Myeloid_lineage | 8 | 3,449 | Myeloid Cell | False | 0.089 | Intermediate Monocyte | nan | nan | registry__intermediate_monocyte | pass |
| infection_study_03 | Myeloid_lineage | 4 | 1,828 | Myeloid Cell | False | 0.074 | Neutrophil | nan | nan | registry__neutrophil | pass |
| infection_study_03 | T_NK_lineage | 5 | 25,968 | T Cell | False | 0.046 | NKT Cell | 0.113 | 0.000 | registry__nkt_cell | pass |
| infection_study_03 | T_NK_lineage | 3 | 24,218 | T Cell | False | 0.023 | NKT Cell | 0.023 | 0.000 | registry__nkt_cell | pass |
| infection_study_03 | T_NK_lineage | 2 | 21,324 | T Cell | False | 0.038 | NKT Cell | 0.133 | 0.000 | registry__nkt_cell | pass |
| infection_study_03 | T_NK_lineage | 0 | 17,363 | T Cell | False | 0.063 | NKT Cell | 0.130 | 0.000 | registry__nkt_cell | pass |
| infection_study_03 | T_NK_lineage | 12 | 16,459 | NKT Cell | True | 0.288 | NKT Cell | 0.006 | 0.000 | registry__nkt_cell | pass |
| infection_study_03 | T_NK_lineage | 4 | 15,652 | NKT Cell | True | 0.259 | NKT Cell | 0.010 | 0.000 | registry__nkt_cell | pass |
| infection_study_03 | T_NK_lineage | 10 | 15,033 | T Cell | False | 0.062 | NKT Cell | 0.116 | 0.000 | registry__nkt_cell | pass |
| infection_study_03 | T_NK_lineage | 1 | 14,371 | T Cell | False | 0.023 | NKT Cell | 0.026 | 0.000 | registry__nkt_cell | pass |
| infection_study_03 | T_NK_lineage | 9 | 14,010 | T Cell | False | 0.055 | NKT Cell | 0.130 | 0.000 | registry__nkt_cell | pass |
| infection_study_03 | T_NK_lineage | 11 | 12,271 | T Cell | False | 0.090 | NKT Cell | 0.034 | 0.000 | registry__nkt_cell | pass |

## 出力ファイル

- Submission TSVs: `outputs/submission_v23_marker_rescue_scavenge/infection_study_03/submissions/`
- cellxgene H5ADs: `outputs/submission_v23_marker_rescue_scavenge/infection_study_03/cellxgene/`
- Marker availability table: `outputs/submission_v23_marker_rescue_scavenge/infection_study_03/tables/marker_gene_availability.tsv`
- Marker availability alerts: `outputs/submission_v23_marker_rescue_scavenge/infection_study_03/tables/marker_gene_availability_alerts.tsv`
- Subcluster evidence: `outputs/submission_v23_marker_rescue_scavenge/infection_study_03/tables/lineage_subcluster_evidence.tsv.gz`
- Source disagreement summary: `outputs/submission_v23_marker_rescue_scavenge/infection_study_03/tables/source_disagreement_summary.tsv`
- Source effectiveness summary: `outputs/submission_v23_marker_rescue_scavenge/infection_study_03/tables/source_effectiveness_summary.tsv`
- Diagnostics tables: `outputs/submission_v23_marker_rescue_scavenge/infection_study_03/tables/`
