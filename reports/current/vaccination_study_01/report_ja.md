# HIPC データセットアノテーションレポート: vaccination_study_01

更新日: 2026-06-15 EDT

このレポートは `hipc-annotation` Codex workflow によって生成したデータセット別レビュー文書です。固定 method は repository README に置き、このレポートでは実際の evidence、弱い箇所、レビュー優先度、UMAP / dotplot を確認します。

## 2026-06-12 提出候補メモ

- 現行の緊急提出候補では、この dataset は v23 aggressive marker-rescue output を採用しています。
- CellTypist の過去出力は存在しますが、barcode/input 世代の整合性に不安があり、直接の全面置換には使っていません。
- parent/Blood residual fraction は 0.8583 と高く、Treg marker も `FOXP3/IL2RA/CTLA4` 欠損のため、細かい T cell annotation は信頼しにくいです。
- 次に改善するなら、sample/batch-aware な Harmony embedding を作り、cluster 単位で CellTypist / marker / reference evidence を再評価する必要があります。

## データセット概要

| study | cells | analysis_X_genes | pre_hvg_genes | counts_layer_genes | labels | parent_or_blood_fraction | Blood Cell | Doublet | artifact_like | median_confidence | low_confidence | source_disagreement | invalid_labels |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| vaccination_study_01 | 307,194 | 10,528 | 10,528 | 10,528 | 14 | 0.041 | 7,172 | 0 | 8,392 | 0.786 | 12,443 | 66,977 (0.218) | none |

## 実行概要

- 実行単位: one dataset in, one annotated dataset out。
- 実行経路: Codex skill `hipc-annotation` -> bundled helper `run_one.sh` -> annotation CLI -> validator -> report inspection。
- 検証: submission row count、H5AD observation count、official label validity、H5AD/submission agreement、confidence column、report image link を確認する。
- このレポートは workflow の再掲ではなく、このデータセットの marker 欠損、UMAP、label 構成、review concern を読むためのもの。

## データセット固有の解釈

- `vaccination_study_01`: 307,194 cells、analysis X/var 10,528 genes、pre-HVG slot 10,528 genes、submitted label 14 種、parent/Blood residual fraction 0.041、median confidence 0.786。
  - 12,443 cells は low confidence。QC / confidence UMAP 上で局在を確認する。
  - 7,172 cells は `Blood Cell` として残存。これは filter-out ではなく、曖昧な細胞を公式 parent label で残したもの。
  - Marker gene 欠損アラート: Treg。該当 marker set に依存する fine label は慎重に見る。

## データセット固有の評価

- 全体像: 307,194 cells / analysis X/var 10,528 genes / pre-HVG slot 10,528 genes。parent/Blood residual は 0.041、low-confidence は 12,443 cells、source disagreement flag は 66,977 cells (0.218)。
- 優先確認: low-confidence 領域が QC UMAP と source-disagreement UMAP で同じ場所に集まるかを確認する。
- 優先確認: `Blood Cell` 残存が孤立 cluster なのか、複数 lineage に分散した曖昧領域なのかを UMAP で確認する。
- Marker gene 欠損: Treg は confidence cap 対象。該当 label は marker expression UMAP と dotplot で妥当性を確認する。

## Marker Gene 欠損アラート

| study | marker_set | alert | present_fraction | missing_critical_markers | missing_genes |
| --- | --- | --- | --- | --- | --- |
| vaccination_study_01 | Treg | critical | 0.143 | FOXP3;IL2RA;CTLA4 | FOXP3;IL2RA;CTLA4;TIGIT;TNFRSF18;CCR8 |

## ソース間不一致

| study | predicted_cell_type | cells | median_source_agreement | disagreement_cells | disagreement_fraction |
| --- | --- | --- | --- | --- | --- |
| vaccination_study_01 | B Cell | 5,271 | 0.000 | 5,263 | 0.998 |
| vaccination_study_01 | Blood Cell | 7,172 | 0.000 | 5,844 | 0.815 |
| vaccination_study_01 | CD4 Naive / T Central Memory | 70,198 | 0.667 | 25,278 | 0.360 |
| vaccination_study_01 | CD8 Cytotoxic / T Effector Memory | 13,257 | 0.667 | 4,698 | 0.354 |
| vaccination_study_01 | Classical Monocyte | 80,515 | 0.667 | 16,261 | 0.202 |
| vaccination_study_01 | Plasma Cell | 543 | 0.667 | 89 | 0.164 |
| vaccination_study_01 | Memory B Cell | 9,128 | 0.667 | 1,299 | 0.142 |
| vaccination_study_01 | Conventional DC 2 | 15,460 | 1.000 | 2,060 | 0.133 |
| vaccination_study_01 | Naive B Cell | 12,528 | 1.000 | 1,635 | 0.131 |
| vaccination_study_01 | NK Cell | 52,211 | 1.000 | 3,338 | 0.064 |
| vaccination_study_01 | Non-Classical Monocyte | 25,357 | 1.000 | 1,179 | 0.046 |
| vaccination_study_01 | Plasmacytoid DC | 7,162 | 1.000 | 33 | 0.005 |

## アノテーションソース効果

この表は外部 ground truth に対する正解率ではありません。各 annotation source がどれだけの細胞で情報を持ち、final label とどれだけ一致したかを示す監査用統計です。`coverage` は source が `not_available` 以外を返した割合、`final_concordance` は informative cells の中で final label と一致した割合、`unique_support` はその source だけが final label と一致した細胞数です。

| study | source | informative_cells | coverage | final_concordance | high_conf_concordance | unique_support | discordant |
| --- | --- | --- | --- | --- | --- | --- | --- |
| vaccination_study_01 | CellTypist | 307,194 | 1.000 | 0.819 | 0.847 | 1,128 | 55,486 |
| vaccination_study_01 | Azimuth PBMC L2 | 307,194 | 1.000 | 0.690 | 0.721 | 38 | 95,313 |
| vaccination_study_01 | Azimuth PBMC L3 | 307,194 | 1.000 | 0.320 | 0.305 | 770 | 208,963 |
| vaccination_study_01 | Cluster marker assignment | 291,624 | 0.949 | 0.953 | 0.972 | 24,114 | 13,606 |
| vaccination_study_01 | Pan-human Azimuth | 263,305 | 0.857 | 0.740 | 0.762 | 95 | 68,549 |
| vaccination_study_01 | Cluster consensus | 0 | 0.000 | 0.000 | 0.000 | 0 | 0 |
| vaccination_study_01 | scRefMapping | 0 | 0.000 | 0.000 | 0.000 | 0 | 0 |

## レビュー優先事項

| study | concern | cells |
| --- | --- | --- |
| vaccination_study_01 | High source disagreement for B Cell | 5,263 |
| vaccination_study_01 | High source disagreement for Blood Cell | 5,844 |
| vaccination_study_01 | High dataset-level source disagreement | 66,977 |
| vaccination_study_01 | Large Blood Cell/ambiguous residual remains | 7,172 |
| vaccination_study_01 | Many low-confidence cells; QC or mixed-marker effects likely remain | 12,443 |

## ラベル構成

| study | predicted_cell_type | cells |
| --- | --- | --- |
| vaccination_study_01 | Classical Monocyte | 80,515 |
| vaccination_study_01 | CD4 Naive / T Central Memory | 70,198 |
| vaccination_study_01 | NK Cell | 52,211 |
| vaccination_study_01 | Non-Classical Monocyte | 25,357 |
| vaccination_study_01 | Conventional DC 2 | 15,460 |
| vaccination_study_01 | CD8 Cytotoxic / T Effector Memory | 13,257 |
| vaccination_study_01 | Naive B Cell | 12,528 |
| vaccination_study_01 | Memory B Cell | 9,128 |
| vaccination_study_01 | Platelet | 8,075 |
| vaccination_study_01 | Blood Cell | 7,172 |
| vaccination_study_01 | Plasmacytoid DC | 7,162 |
| vaccination_study_01 | B Cell | 5,271 |
| vaccination_study_01 | Plasma Cell | 543 |
| vaccination_study_01 | HSC | 317 |

## Inline Figures

### vaccination_study_01

![vaccination_study_01 final labels](assets/umap_vaccination_study_01_annotation_label.png)

![vaccination_study_01 lineage and annotation reason](assets/umap_vaccination_study_01_annotation_lineage_reason.png)

![vaccination_study_01 QC and confidence](assets/umap_vaccination_study_01_annotation_qc_confidence.png)

![vaccination_study_01 source agreement and disagreement](assets/umap_vaccination_study_01_annotation_source_disagreement.png)

![vaccination_study_01 annotation-source effectiveness](assets/figure_02_source_effectiveness.png)

![vaccination_study_01 marker expression UMAPs](assets/umap_vaccination_study_01_annotation_marker_expression.png)

![vaccination_study_01 submitted-label marker dotplot](assets/dotplot_vaccination_study_01_annotation_marker_dotplot.png)

#### vaccination_study_01 B_lineage true subcluster UMAP

![vaccination_study_01 B_lineage true subcluster labels](assets/umap_vaccination_study_01_B_lineage_true_subcluster_label.png)

![vaccination_study_01 B_lineage true subcluster source labels](assets/umap_vaccination_study_01_B_lineage_true_subcluster_source_labels.png)

![vaccination_study_01 B_lineage true subcluster QC](assets/umap_vaccination_study_01_B_lineage_true_subcluster_qc.png)

![vaccination_study_01 B_lineage true subcluster marker scores](assets/umap_vaccination_study_01_B_lineage_true_subcluster_marker_scores.png)

![vaccination_study_01 B_lineage true subcluster marker expression](assets/umap_vaccination_study_01_B_lineage_true_subcluster_marker_expression.png)

![vaccination_study_01 B_lineage subcluster marker score heatmap](assets/subcluster_marker_score_heatmap_vaccination_study_01_B_lineage.png)

![vaccination_study_01 B_lineage subcluster marker dotplot](assets/dotplot_vaccination_study_01_B_lineage_true_subcluster_marker_dotplot.png)

Tables: `tables/vaccination_study_01_B_lineage_true_subcluster_umap.tsv.gz`, `tables/vaccination_study_01_B_lineage_subcluster_candidate_scores.tsv`.

#### vaccination_study_01 T_NK_lineage true subcluster UMAP

![vaccination_study_01 T_NK_lineage true subcluster labels](assets/umap_vaccination_study_01_T_NK_lineage_true_subcluster_label.png)

![vaccination_study_01 T_NK_lineage true subcluster source labels](assets/umap_vaccination_study_01_T_NK_lineage_true_subcluster_source_labels.png)

![vaccination_study_01 T_NK_lineage true subcluster QC](assets/umap_vaccination_study_01_T_NK_lineage_true_subcluster_qc.png)

![vaccination_study_01 T_NK_lineage true subcluster marker scores](assets/umap_vaccination_study_01_T_NK_lineage_true_subcluster_marker_scores.png)

![vaccination_study_01 T_NK_lineage true subcluster marker expression](assets/umap_vaccination_study_01_T_NK_lineage_true_subcluster_marker_expression.png)

![vaccination_study_01 T_NK_lineage subcluster marker score heatmap](assets/subcluster_marker_score_heatmap_vaccination_study_01_T_NK_lineage.png)

![vaccination_study_01 T_NK_lineage subcluster marker dotplot](assets/dotplot_vaccination_study_01_T_NK_lineage_true_subcluster_marker_dotplot.png)

Tables: `tables/vaccination_study_01_T_NK_lineage_true_subcluster_umap.tsv.gz`, `tables/vaccination_study_01_T_NK_lineage_subcluster_candidate_scores.tsv`.

#### vaccination_study_01 Myeloid_lineage true subcluster UMAP

![vaccination_study_01 Myeloid_lineage true subcluster labels](assets/umap_vaccination_study_01_Myeloid_lineage_true_subcluster_label.png)

![vaccination_study_01 Myeloid_lineage true subcluster source labels](assets/umap_vaccination_study_01_Myeloid_lineage_true_subcluster_source_labels.png)

![vaccination_study_01 Myeloid_lineage true subcluster QC](assets/umap_vaccination_study_01_Myeloid_lineage_true_subcluster_qc.png)

![vaccination_study_01 Myeloid_lineage true subcluster marker scores](assets/umap_vaccination_study_01_Myeloid_lineage_true_subcluster_marker_scores.png)

![vaccination_study_01 Myeloid_lineage true subcluster marker expression](assets/umap_vaccination_study_01_Myeloid_lineage_true_subcluster_marker_expression.png)

![vaccination_study_01 Myeloid_lineage subcluster marker score heatmap](assets/subcluster_marker_score_heatmap_vaccination_study_01_Myeloid_lineage.png)

![vaccination_study_01 Myeloid_lineage subcluster marker dotplot](assets/dotplot_vaccination_study_01_Myeloid_lineage_true_subcluster_marker_dotplot.png)

Tables: `tables/vaccination_study_01_Myeloid_lineage_true_subcluster_umap.tsv.gz`, `tables/vaccination_study_01_Myeloid_lineage_subcluster_candidate_scores.tsv`.


## Subcluster Marker Score Review

上の lineage-specific panel は、各 lineage subset で HVG 選択、PCA、neighbors、Leiden、UMAP を再計算した true local subcluster analysis から生成しています。Marker gene による fine label の確認は global UMAP だけではなく、この local UMAP、CellTypist/Azimuth/Pan-human/cluster-level marker gene assignment overlay、cluster marker gate score UMAP、marker-expression UMAP、dotplot を主に見ます。Treg など sparse marker label は cell-wise marker winner ではなく、local cluster の FOXP3/IL2RA/CTLA4 など key-marker support と reference support で判定します。

## Marker Assignment Feedback

Marker gene assignment は final label を強制的に上書きするものではなく、cluster-level の自己点検です。`raw_marker_winner` は marker score だけの勝者、`marker_assignment` は conservative policy と source-supported tie-break を通した marker-based assignment です。この表は marker assignment と final/reference-driven label がずれる cluster、marker specificity が弱い cluster、scRefMap が期待される lineage で欠落する cluster を示します。`marker_score` は raw marker base score から negative/confound marker penalty を差し引いた cluster-level marker gate score です。

| study | lineage | cluster | cells | chosen_label | marker_assignment | raw_marker_winner | assignment_reason | marker_score | base_score | penalty | flags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| vaccination_study_01 | T_NK_lineage | 5 | 21,429 | NK Cell | NK Cell | NKT Cell | source_supported_marker_tiebreak | 0.874 | 1.000 | 0.126 | screfmapping_missing_for_scope |
| vaccination_study_01 | T_NK_lineage | 2 | 19,484 | CD4 Naive / T Central Memory | CD4 Naive / T Central Memory | CD4 Naive / T Central Memory | raw_marker_winner | 0.843 | 1.000 | 0.157 | screfmapping_missing_for_scope |
| vaccination_study_01 | T_NK_lineage | 9 | 16,378 | CD4 Naive / T Central Memory | CD4 Naive / T Central Memory | CD4 Naive / T Central Memory | raw_marker_winner | 0.820 | 1.000 | 0.180 | screfmapping_missing_for_scope |
| vaccination_study_01 | T_NK_lineage | 6 | 15,656 | CD4 Naive / T Central Memory | CD4 Naive / T Central Memory | CD4 Naive / T Central Memory | raw_marker_winner | 0.848 | 1.000 | 0.152 | screfmapping_missing_for_scope |
| vaccination_study_01 | T_NK_lineage | 8 | 14,105 | NK Cell | NK Cell | NKT Cell | source_supported_marker_tiebreak | 0.868 | 1.000 | 0.132 | screfmapping_missing_for_scope |
| vaccination_study_01 | T_NK_lineage | 1 | 13,257 | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | NKT Cell | source_supported_marker_tiebreak | 0.629 | 1.000 | 0.371 | screfmapping_missing_for_scope |
| vaccination_study_01 | T_NK_lineage | 7 | 12,227 | CD4 Naive / T Central Memory | CD4 Naive / T Central Memory | CD4 Naive / T Central Memory | raw_marker_winner | 0.732 | 0.950 | 0.218 | screfmapping_missing_for_scope |
| vaccination_study_01 | T_NK_lineage | 3 | 10,150 | NK Cell | NK Cell | NKT Cell | source_supported_marker_tiebreak | 0.851 | 1.000 | 0.149 | screfmapping_missing_for_scope |
| vaccination_study_01 | Myeloid_lineage | 2 | 7,162 | Plasmacytoid DC | Intermediate Monocyte | Intermediate Monocyte | raw_marker_winner | 0.834 | 0.988 | 0.154 | marker_final_disagreement |
| vaccination_study_01 | T_NK_lineage | 4 | 6,526 | NK Cell | NK Cell | NK Cell | raw_marker_winner | 0.880 | 1.000 | 0.120 | screfmapping_missing_for_scope |
| vaccination_study_01 | T_NK_lineage | 0 | 6,453 | CD4 Naive / T Central Memory | CD4 Naive / T Central Memory | CD4 Naive / T Central Memory | raw_marker_winner | 0.734 | 1.000 | 0.266 | screfmapping_missing_for_scope |
| vaccination_study_01 | B_lineage | 0 | 2,137 | B Cell | Plasmablast | Plasmablast | raw_marker_winner | 0.424 | 0.719 | 0.296 | marker_final_disagreement;screfmapping_missing_for_scope |
| vaccination_study_01 | B_lineage | 1 | 1,429 | Naive B Cell | Naive B Cell | Naive B Cell | raw_marker_winner | 0.723 | 1.000 | 0.277 | screfmapping_missing_for_scope |
| vaccination_study_01 | B_lineage | 2 | 1,397 | Naive B Cell | Naive B Cell | Naive B Cell | raw_marker_winner | 0.515 | 1.000 | 0.485 | screfmapping_missing_for_scope |
| vaccination_study_01 | B_lineage | 3 | 1,365 | Memory B Cell | Memory B Cell | Naive B Cell | source_supported_marker_tiebreak | 0.453 | 1.000 | 0.547 | screfmapping_missing_for_scope |
| vaccination_study_01 | B_lineage | 4 | 1,363 | B Cell | Naive B Cell | Naive B Cell | raw_marker_winner | 0.349 | 0.767 | 0.418 | marker_final_disagreement;weak_marker_specificity;screfmapping_missing_for_scope |
| vaccination_study_01 | B_lineage | 5 | 1,297 | Naive B Cell | Naive B Cell | Naive B Cell | raw_marker_winner | 0.797 | 1.000 | 0.203 | screfmapping_missing_for_scope |
| vaccination_study_01 | B_lineage | 6 | 1,221 | Naive B Cell | Naive B Cell | Naive B Cell | raw_marker_winner | 0.672 | 1.000 | 0.328 | screfmapping_missing_for_scope |
| vaccination_study_01 | B_lineage | 7 | 1,180 | Memory B Cell | Memory B Cell | Memory B Cell | raw_marker_winner | 0.515 | 0.855 | 0.339 | screfmapping_missing_for_scope |
| vaccination_study_01 | B_lineage | 8 | 1,079 | Naive B Cell | Naive B Cell | Naive B Cell | raw_marker_winner | 0.726 | 1.000 | 0.274 | screfmapping_missing_for_scope |

## LLM Review Queue

この表は Codex/LLM が読むための subcluster-level review queue です。LLM はこの evidence を読んで、final label が妥当か、ontology にちょうどよい label がないのか、registry / conservative policy を一般ルールとして更新すべきかを提案します。LLM の出力で per-cell label を直接書き換えず、採用する場合は registry/config を更新して deterministic pipeline を再実行します。

| study | lineage | cluster | cells | priority | reasons | suggested_action | final_label | marker_assignment | raw_marker_winner | score_margin |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| vaccination_study_01 | B_lineage | 0 | 2,137 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | B Cell | Plasmablast | Plasmablast | 0.202 |
| vaccination_study_01 | B_lineage | 22 | 587 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | B Cell | Plasma Cell | Plasma Cell | 0.029 |
| vaccination_study_01 | B_lineage | 32 | 120 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | B Cell | Plasmablast | Plasmablast | 0.057 |
| vaccination_study_01 | B_lineage | 4 | 1,363 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;screfmapping_not_available | check_if_finer_official_label_is_supported | B Cell | Naive B Cell | Naive B Cell | 0.475 |
| vaccination_study_01 | B_lineage | 10 | 1,064 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;screfmapping_not_available | check_if_finer_official_label_is_supported | B Cell | Naive B Cell | Naive B Cell | 0.413 |
| vaccination_study_01 | T_NK_lineage | 5 | 21,429 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | NK Cell | NK Cell | NKT Cell | 2.436 |
| vaccination_study_01 | T_NK_lineage | 8 | 14,105 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | NK Cell | NK Cell | NKT Cell | 2.176 |
| vaccination_study_01 | T_NK_lineage | 1 | 13,257 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | NKT Cell | 1.056 |
| vaccination_study_01 | T_NK_lineage | 3 | 10,150 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | NK Cell | NK Cell | NKT Cell | 2.391 |
| vaccination_study_01 | B_lineage | 23 | 543 | medium | marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | Plasma Cell | Plasmablast | Plasmablast | 0.816 |
| vaccination_study_01 | Myeloid_lineage | 2 | 7,162 | medium | marker_assignment_disagrees_with_final;screfmapping_not_available | review_marker_vs_reference_disagreement | Plasmacytoid DC | Intermediate Monocyte | Intermediate Monocyte | 2.290 |
| vaccination_study_01 | B_lineage | 21 | 596 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | Naive B Cell | Naive B Cell | Plasma Cell | 0.606 |
| vaccination_study_01 | B_lineage | 3 | 1,365 | medium | raw_marker_winner_changed_by_policy;screfmapping_not_available | accept | Memory B Cell | Memory B Cell | Naive B Cell | 2.159 |
| vaccination_study_01 | B_lineage | 11 | 1,005 | medium | raw_marker_winner_changed_by_policy;screfmapping_not_available | accept | Memory B Cell | Memory B Cell | Naive B Cell | 2.092 |
| vaccination_study_01 | B_lineage | 19 | 630 | medium | marker_assignment_disagrees_with_final;screfmapping_not_available | review_marker_vs_reference_disagreement | Memory B Cell | Naive B Cell | Naive B Cell | 1.865 |
| vaccination_study_01 | T_NK_lineage | 2 | 19,484 | low | screfmapping_not_available | accept | CD4 Naive / T Central Memory | CD4 Naive / T Central Memory | CD4 Naive / T Central Memory | 1.376 |
| vaccination_study_01 | T_NK_lineage | 9 | 16,378 | low | screfmapping_not_available | accept | CD4 Naive / T Central Memory | CD4 Naive / T Central Memory | CD4 Naive / T Central Memory | 1.364 |
| vaccination_study_01 | T_NK_lineage | 6 | 15,656 | low | screfmapping_not_available | accept | CD4 Naive / T Central Memory | CD4 Naive / T Central Memory | CD4 Naive / T Central Memory | 1.173 |
| vaccination_study_01 | T_NK_lineage | 7 | 12,227 | low | screfmapping_not_available | accept | CD4 Naive / T Central Memory | CD4 Naive / T Central Memory | CD4 Naive / T Central Memory | 1.399 |
| vaccination_study_01 | T_NK_lineage | 4 | 6,526 | low | screfmapping_not_available | accept | NK Cell | NK Cell | NK Cell | 1.598 |

## Cluster Consensus Evidence

| study | lineage | cluster | cells | chosen_label | accepted | score_margin | cluster_marker_assignment | treg_key_any | treg_key_bonus | marker_set | marker_alert |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| vaccination_study_01 | B_lineage | 0 | 2,137 | B Cell | False | 0.202 | Plasmablast | nan | nan | B_memory_ABC | pass |
| vaccination_study_01 | B_lineage | 1 | 1,429 | Naive B Cell | True | 2.804 | Naive B Cell | nan | nan | B_naive | pass |
| vaccination_study_01 | B_lineage | 2 | 1,397 | Naive B Cell | True | 2.537 | Naive B Cell | nan | nan | B_naive | pass |
| vaccination_study_01 | B_lineage | 3 | 1,365 | Memory B Cell | True | 2.159 | Memory B Cell | nan | nan | B_memory_ABC | pass |
| vaccination_study_01 | B_lineage | 4 | 1,363 | B Cell | False | 0.475 | Naive B Cell | nan | nan | B_memory_ABC | pass |
| vaccination_study_01 | B_lineage | 5 | 1,297 | Naive B Cell | True | 3.283 | Naive B Cell | nan | nan | B_naive | pass |
| vaccination_study_01 | B_lineage | 6 | 1,221 | Naive B Cell | True | 2.876 | Naive B Cell | nan | nan | B_naive | pass |
| vaccination_study_01 | B_lineage | 7 | 1,180 | Memory B Cell | True | 2.917 | Memory B Cell | nan | nan | B_memory_ABC | pass |
| vaccination_study_01 | B_lineage | 8 | 1,079 | Naive B Cell | True | 3.078 | Naive B Cell | nan | nan | B_naive | pass |
| vaccination_study_01 | B_lineage | 9 | 1,074 | Naive B Cell | True | 2.992 | Naive B Cell | nan | nan | B_naive | pass |
| vaccination_study_01 | B_lineage | 10 | 1,064 | B Cell | False | 0.413 | Naive B Cell | nan | nan | B_memory_ABC | pass |
| vaccination_study_01 | B_lineage | 11 | 1,005 | Memory B Cell | True | 2.092 | Memory B Cell | nan | nan | B_memory_ABC | pass |
| vaccination_study_01 | B_lineage | 12 | 957 | Memory B Cell | True | 2.624 | Memory B Cell | nan | nan | B_memory_ABC | pass |
| vaccination_study_01 | B_lineage | 13 | 883 | Memory B Cell | True | 2.959 | Memory B Cell | nan | nan | B_memory_ABC | pass |
| vaccination_study_01 | B_lineage | 14 | 876 | Naive B Cell | True | 2.995 | Naive B Cell | nan | nan | B_naive | pass |
| vaccination_study_01 | B_lineage | 15 | 793 | Memory B Cell | True | 2.787 | Memory B Cell | nan | nan | B_memory_ABC | pass |
| vaccination_study_01 | B_lineage | 16 | 764 | Naive B Cell | True | 3.130 | Naive B Cell | nan | nan | B_naive | pass |
| vaccination_study_01 | B_lineage | 17 | 755 | Naive B Cell | True | 0.119 | Naive B Cell | nan | nan | B_naive | pass |
| vaccination_study_01 | B_lineage | 18 | 656 | Naive B Cell | True | 1.903 | Naive B Cell | nan | nan | B_naive | pass |
| vaccination_study_01 | B_lineage | 19 | 630 | Memory B Cell | True | 1.865 | Naive B Cell | nan | nan | B_memory_ABC | pass |
| vaccination_study_01 | B_lineage | 20 | 620 | Memory B Cell | True | 2.235 | Memory B Cell | nan | nan | B_memory_ABC | pass |
| vaccination_study_01 | B_lineage | 21 | 596 | Naive B Cell | True | 0.606 | Naive B Cell | nan | nan | B_naive | pass |
| vaccination_study_01 | B_lineage | 22 | 587 | B Cell | False | 0.029 | Plasma Cell | nan | nan | B_naive | pass |
| vaccination_study_01 | B_lineage | 23 | 543 | Plasma Cell | True | 0.816 | Plasmablast | nan | nan | Plasma_ASC | pass |
| vaccination_study_01 | B_lineage | 24 | 543 | Naive B Cell | True | 0.190 | Naive B Cell | nan | nan | B_naive | pass |
| vaccination_study_01 | B_lineage | 25 | 525 | Memory B Cell | True | 2.527 | Memory B Cell | nan | nan | B_memory_ABC | pass |
| vaccination_study_01 | B_lineage | 26 | 430 | Memory B Cell | True | 2.779 | Memory B Cell | nan | nan | B_memory_ABC | pass |
| vaccination_study_01 | B_lineage | 27 | 390 | Memory B Cell | True | 2.331 | Memory B Cell | nan | nan | B_memory_ABC | pass |
| vaccination_study_01 | B_lineage | 28 | 357 | Naive B Cell | True | 0.589 | Naive B Cell | nan | nan | B_naive | pass |
| vaccination_study_01 | B_lineage | 29 | 350 | Memory B Cell | True | 0.704 | Memory B Cell | nan | nan | B_memory_ABC | pass |

## 出力ファイル

- Submission TSVs: `outputs/submission_v25_harmony_reference_rescue/vaccination_study_01/submissions/`
- cellxgene H5ADs: `outputs/submission_v25_harmony_reference_rescue/vaccination_study_01/cellxgene/`
- Marker availability table: `outputs/submission_v25_harmony_reference_rescue/vaccination_study_01/tables/marker_gene_availability.tsv`
- Marker availability alerts: `outputs/submission_v25_harmony_reference_rescue/vaccination_study_01/tables/marker_gene_availability_alerts.tsv`
- Subcluster evidence: `outputs/submission_v25_harmony_reference_rescue/vaccination_study_01/tables/lineage_subcluster_evidence.tsv.gz`
- Source disagreement summary: `outputs/submission_v25_harmony_reference_rescue/vaccination_study_01/tables/source_disagreement_summary.tsv`
- Source effectiveness summary: `outputs/submission_v25_harmony_reference_rescue/vaccination_study_01/tables/source_effectiveness_summary.tsv`
- Diagnostics tables: `outputs/submission_v25_harmony_reference_rescue/vaccination_study_01/tables/`

