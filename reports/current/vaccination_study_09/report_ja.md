# HIPC データセットアノテーションレポート: vaccination_study_09

更新日: 2026-06-12 EDT

## 現行提出用サマリー

| 項目 | 内容 |
| --- | --- |
| 提出候補 package | v24 pragmatic package |
| 採用 source | `outputs/submission_final_v22/vaccination_study_09/submissions/vaccination_study_09_annotation.tsv` |
| 細胞数 | 139,960 |
| label 数 | 18 |
| parent/Blood residual | 155 cells (0.0011) |
| median confidence | 0.7772 |
| 上位 label | CD4 Naive / T Central Memory: 54,333; Classical Monocyte: 26,795; CD8 Cytotoxic / T Effector Memory: 13,647; Naive B Cell: 12,334; NK Cell: 9,187; CD8 Naive / T Central Memory: 7,394; MAIT Cell: 5,153; Non-Classical Monocyte: 3,949 |
| 現状判断 | 提出候補として比較的良好。T subset の粒度と gamma-delta / MAIT / NKT の扱いを個別 UMAP と marker evidence で確認する。 |

このレポートは `hipc-annotation` Codex workflow によって生成したデータセット別レビュー文書です。固定 method は repository README に置き、このレポートでは実際の evidence、弱い箇所、レビュー優先度、UMAP / dotplot を確認します。

## データセット概要

| study | cells | analysis_X_genes | pre_hvg_genes | counts_layer_genes | labels | parent_or_blood_fraction | Blood Cell | Doublet | artifact_like | median_confidence | low_confidence | source_disagreement | invalid_labels |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| vaccination_study_09 | 139,960 | 3,985 | 8,000 | 3,985 | 18 | 0.001 | 116 | 323 | 92 | 0.777 | 478 | 18,932 (0.135) | none |

## 実行概要

- 実行単位: one dataset in, one annotated dataset out。
- 実行経路: Codex skill `hipc-annotation` -> bundled helper `run_one.sh` -> annotation CLI -> validator -> report inspection。
- 検証: submission row count、H5AD observation count、official label validity、H5AD/submission agreement、confidence column、report image link を確認する。
- このレポートは workflow の再掲ではなく、このデータセットの marker 欠損、UMAP、label 構成、review concern を読むためのもの。

## データセット固有の解釈

- `vaccination_study_09`: 139,960 cells、analysis X/var 3,985 genes、pre-HVG slot 8,000 genes、submitted label 18 種、parent/Blood residual fraction 0.001、median confidence 0.777。
  - 478 cells は low confidence。QC / confidence UMAP 上で局在を確認する。
  - 323 cells は `Doublet` として提出。mixed-lineage marker expression と scrublet support を確認する。
  - 116 cells は `Blood Cell` として残存。これは filter-out ではなく、曖昧な細胞を公式 parent label で残したもの。
  - Marker gene 欠損アラート: Treg, gdT, B_memory_ABC, Plasma_ASC。該当 marker set に依存する fine label は慎重に見る。

## データセット固有の評価

- 全体像: 139,960 cells / analysis X/var 3,985 genes / pre-HVG slot 8,000 genes。parent/Blood residual は 0.001、low-confidence は 478 cells、source disagreement flag は 18,932 cells (0.135)。
- 優先確認: low-confidence 領域が QC UMAP と source-disagreement UMAP で同じ場所に集まるかを確認する。
- 優先確認: `Blood Cell` 残存が孤立 cluster なのか、複数 lineage に分散した曖昧領域なのかを UMAP で確認する。
- Marker gene 欠損: Treg, gdT, B_memory_ABC, Plasma_ASC は confidence cap 対象。該当 label は marker expression UMAP と dotplot で妥当性を確認する。

## Marker Gene 欠損アラート

| study | marker_set | alert | present_fraction | missing_critical_markers | missing_genes |
| --- | --- | --- | --- | --- | --- |
| vaccination_study_09 | Treg | critical | 0.286 | FOXP3;IL2RA;CTLA4 | FOXP3;IL2RA;CTLA4;IKZF2;CCR8 |
| vaccination_study_09 | gdT | warning | 0.333 | TRDC;TRGC1;TRGC2 | TRDC;TRGC1;TRGC2;TRDV2 |
| vaccination_study_09 | B_memory_ABC | warning | 0.500 | TNFRSF13B;ITGAX | TNFRSF13B;ITGAX;AIM2;CD86 |
| vaccination_study_09 | Plasma_ASC | warning | 0.333 | JCHAIN | JCHAIN;SDC1;IRF4;TNFRSF17;IGHG1;IGHA1 |

## ソース間不一致

| study | predicted_cell_type | cells | median_source_agreement | disagreement_cells | disagreement_fraction |
| --- | --- | --- | --- | --- | --- |
| vaccination_study_09 | Doublet | 323 | 0.000 | 323 | 1.000 |
| vaccination_study_09 | Blood Cell | 116 | 0.250 | 116 | 1.000 |
| vaccination_study_09 | B Cell | 39 | 0.000 | 39 | 1.000 |
| vaccination_study_09 | Treg | 873 | 0.500 | 403 | 0.462 |
| vaccination_study_09 | MAIT Cell | 5,153 | 0.667 | 1,468 | 0.285 |
| vaccination_study_09 | Conventional DC 2 | 1,541 | 1.000 | 302 | 0.196 |
| vaccination_study_09 | CD8 Cytotoxic / T Effector Memory | 13,647 | 1.000 | 2,595 | 0.190 |
| vaccination_study_09 | Classical Monocyte | 26,795 | 1.000 | 4,409 | 0.165 |
| vaccination_study_09 | Memory B Cell | 3,212 | 0.750 | 475 | 0.148 |
| vaccination_study_09 | Non-Classical Monocyte | 3,949 | 1.000 | 576 | 0.146 |
| vaccination_study_09 | Naive B Cell | 12,334 | 1.000 | 1,529 | 0.124 |
| vaccination_study_09 | CD4 Naive / T Central Memory | 54,333 | 1.000 | 5,896 | 0.109 |

## アノテーションソース効果

この表は外部 ground truth に対する正解率ではありません。各 annotation source がどれだけの細胞で情報を持ち、final label とどれだけ一致したかを示す監査用統計です。`coverage` は source が `not_available` 以外を返した割合、`final_concordance` は informative cells の中で final label と一致した割合、`unique_support` はその source だけが final label と一致した細胞数です。

| study | source | informative_cells | coverage | final_concordance | high_conf_concordance | unique_support | discordant |
| --- | --- | --- | --- | --- | --- | --- | --- |
| vaccination_study_09 | Cluster consensus | 139,960 | 1.000 | 0.854 | 0.870 | 614 | 20,385 |
| vaccination_study_09 | CellTypist | 139,960 | 1.000 | 0.820 | 0.810 | 17 | 25,190 |
| vaccination_study_09 | Pan-human Azimuth | 139,960 | 1.000 | 0.717 | 0.771 | 238 | 39,633 |
| vaccination_study_09 | Cluster marker assignment | 139,429 | 0.996 | 0.945 | 0.922 | 6,689 | 7,704 |
| vaccination_study_09 | scRefMapping | 76,084 | 0.544 | 0.771 | 0.887 | 147 | 17,409 |

## レビュー優先事項

| study | concern | cells |
| --- | --- | --- |
| vaccination_study_09 | High source disagreement for B Cell | 39 |
| vaccination_study_09 | High source disagreement for Blood Cell | 116 |
| vaccination_study_09 | High source disagreement for Doublet | 323 |
| vaccination_study_09 | critical marker availability for Treg | 873 |
| vaccination_study_09 | warning marker availability for B_memory_ABC | 3,212 |
| vaccination_study_09 | warning marker availability for Plasma_ASC | 161 |

## ラベル構成

| study | predicted_cell_type | cells |
| --- | --- | --- |
| vaccination_study_09 | CD4 Naive / T Central Memory | 54,333 |
| vaccination_study_09 | Classical Monocyte | 26,795 |
| vaccination_study_09 | CD8 Cytotoxic / T Effector Memory | 13,647 |
| vaccination_study_09 | Naive B Cell | 12,334 |
| vaccination_study_09 | NK Cell | 9,187 |
| vaccination_study_09 | CD8 Naive / T Central Memory | 7,394 |
| vaccination_study_09 | MAIT Cell | 5,153 |
| vaccination_study_09 | Non-Classical Monocyte | 3,949 |
| vaccination_study_09 | Memory B Cell | 3,212 |
| vaccination_study_09 | Conventional DC 2 | 1,541 |
| vaccination_study_09 | Treg | 873 |
| vaccination_study_09 | Plasmacytoid DC | 811 |
| vaccination_study_09 | Doublet | 323 |
| vaccination_study_09 | Plasma Cell | 161 |
| vaccination_study_09 | Blood Cell | 116 |
| vaccination_study_09 | Platelet | 82 |
| vaccination_study_09 | B Cell | 39 |
| vaccination_study_09 | HSC | 10 |

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
| vaccination_study_09 | T_NK_lineage | 0 | 7,828 | NK Cell | NK Cell | NKT Cell | conservative_policy_blocks_raw_marker_winner | 0.922 | 1.000 | 0.078 | screfmapping_missing_for_scope |
| vaccination_study_09 | T_NK_lineage | 4 | 5,983 | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | raw_marker_winner | 0.771 | 1.000 | 0.229 | screfmapping_missing_for_scope |
| vaccination_study_09 | T_NK_lineage | 5 | 5,730 | CD4 Naive / T Central Memory | MAIT Cell | MAIT Cell | raw_marker_winner | 0.844 | 1.000 | 0.156 | marker_final_disagreement |
| vaccination_study_09 | T_NK_lineage | 8 | 5,153 | MAIT Cell | MAIT Cell | NKT Cell | conservative_policy_blocks_raw_marker_winner | 0.800 | 1.000 | 0.200 | screfmapping_missing_for_scope |
| vaccination_study_09 | T_NK_lineage | 10 | 4,234 | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | NKT Cell | conservative_policy_blocks_raw_marker_winner | 0.777 | 1.000 | 0.223 | screfmapping_missing_for_scope |
| vaccination_study_09 | T_NK_lineage | 15 | 1,988 | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | NKT Cell | conservative_policy_blocks_raw_marker_winner | 0.796 | 1.000 | 0.204 | screfmapping_missing_for_scope |
| vaccination_study_09 | T_NK_lineage | 21 | 954 | NK Cell | NK Cell | NKT Cell | conservative_policy_blocks_raw_marker_winner | 0.871 | 0.982 | 0.111 | screfmapping_missing_for_scope |
| vaccination_study_09 | Myeloid_lineage | 13 | 811 | Plasmacytoid DC | Intermediate Monocyte | Intermediate Monocyte | raw_marker_winner | 0.890 | 0.997 | 0.107 | marker_final_disagreement |
| vaccination_study_09 | B_lineage | 3 | 735 | Memory B Cell | Memory B Cell | Memory B Cell | raw_marker_winner | 0.262 | 0.355 | 0.093 | weak_marker_specificity |
| vaccination_study_09 | T_NK_lineage | 23 | 678 | CD4 Naive / T Central Memory | gdT Cell | gdT Cell | raw_marker_winner | 0.617 | 0.802 | 0.185 | marker_final_disagreement |
| vaccination_study_09 | T_NK_lineage | 24 | 405 | NK Cell | NK Cell | NKT Cell | conservative_policy_blocks_raw_marker_winner | 0.909 | 0.976 | 0.067 | screfmapping_missing_for_scope |
| vaccination_study_09 | B_lineage | 8 | 381 | Memory B Cell | Memory B Cell | Memory B Cell | raw_marker_winner | 0.187 | 0.355 | 0.168 | weak_marker_specificity |
| vaccination_study_09 | B_lineage | 11 | 327 | Memory B Cell | Naive B Cell | Naive B Cell | raw_marker_winner | 0.186 | 0.416 | 0.229 | marker_final_disagreement;weak_marker_specificity |
| vaccination_study_09 | B_lineage | 53 | 100 | Memory B Cell | Naive B Cell | Naive B Cell | raw_marker_winner | 0.350 | 0.540 | 0.190 | marker_final_disagreement;weak_marker_specificity |
| vaccination_study_09 | B_lineage | 56 | 39 | B Cell | Plasmablast | Plasmablast | raw_marker_winner | 0.626 | 1.000 | 0.374 | marker_final_disagreement;screfmapping_missing_for_scope |
| vaccination_study_09 | T_NK_lineage | 26 | 19 | CD4 Naive / T Central Memory | gdT Cell | gdT Cell | raw_marker_winner | 0.453 | 0.582 | 0.128 | marker_final_disagreement |

## LLM Review Queue

この表は Codex/LLM が読むための subcluster-level review queue です。LLM はこの evidence を読んで、final label が妥当か、ontology にちょうどよい label がないのか、registry / conservative policy を一般ルールとして更新すべきかを提案します。LLM の出力で per-cell label を直接書き換えず、採用する場合は registry/config を更新して deterministic pipeline を再実行します。

| study | lineage | cluster | cells | priority | reasons | suggested_action | final_label | marker_assignment | raw_marker_winner | score_margin |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| vaccination_study_09 | B_lineage | 56 | 39 | high | parent_or_broad_final_label;marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate;screfmapping_not_available;low_total_score_or_margin | check_if_finer_official_label_is_supported | B Cell | Plasmablast | Plasmablast | 0.054 |
| vaccination_study_09 | T_NK_lineage | 0 | 7,828 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | NK Cell | NK Cell | NKT Cell | 2.494 |
| vaccination_study_09 | T_NK_lineage | 5 | 5,730 | medium | marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate | evaluate_ontology_gap_or_conservative_policy | CD4 Naive / T Central Memory | MAIT Cell | MAIT Cell | 0.991 |
| vaccination_study_09 | T_NK_lineage | 8 | 5,153 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | MAIT Cell | MAIT Cell | NKT Cell | 0.767 |
| vaccination_study_09 | T_NK_lineage | 10 | 4,234 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | NKT Cell | 2.408 |
| vaccination_study_09 | T_NK_lineage | 15 | 1,988 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | NKT Cell | 2.111 |
| vaccination_study_09 | T_NK_lineage | 21 | 954 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | NK Cell | NK Cell | NKT Cell | 2.387 |
| vaccination_study_09 | T_NK_lineage | 23 | 678 | medium | marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate | evaluate_ontology_gap_or_conservative_policy | CD4 Naive / T Central Memory | gdT Cell | gdT Cell | 0.886 |
| vaccination_study_09 | T_NK_lineage | 24 | 405 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | NK Cell | NK Cell | NKT Cell | 2.179 |
| vaccination_study_09 | Myeloid_lineage | 13 | 811 | medium | marker_assignment_disagrees_with_final;screfmapping_not_available | review_marker_vs_reference_disagreement | Plasmacytoid DC | Intermediate Monocyte | Intermediate Monocyte | 2.251 |
| vaccination_study_09 | T_NK_lineage | 26 | 19 | medium | marker_assignment_disagrees_with_final;ambiguous_or_missing_label_candidate | evaluate_ontology_gap_or_conservative_policy | CD4 Naive / T Central Memory | gdT Cell | gdT Cell | 2.074 |
| vaccination_study_09 | T_NK_lineage | 4 | 5,983 | low | screfmapping_not_available | accept | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | 2.431 |
| vaccination_study_09 | B_lineage | 11 | 327 | low | marker_assignment_disagrees_with_final | review_marker_vs_reference_disagreement | Memory B Cell | Naive B Cell | Naive B Cell | 1.886 |
| vaccination_study_09 | B_lineage | 53 | 100 | low | marker_assignment_disagrees_with_final | review_marker_vs_reference_disagreement | Memory B Cell | Naive B Cell | Naive B Cell | 1.154 |
| vaccination_study_09 | B_lineage | 3 | 735 | low | spot_check | accept | Memory B Cell | Memory B Cell | Memory B Cell | 2.787 |
| vaccination_study_09 | B_lineage | 8 | 381 | low | spot_check | accept | Memory B Cell | Memory B Cell | Memory B Cell | 1.747 |

## Cluster Consensus Evidence

| study | lineage | cluster | cells | chosen_label | accepted | score_margin | cluster_marker_assignment | treg_key_any | treg_key_bonus | marker_set | marker_alert |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| vaccination_study_09 | B_lineage | 0 | 1,220 | Memory B Cell | True | 3.290 | Memory B Cell | nan | nan | registry__memory_b_cell | pass |
| vaccination_study_09 | B_lineage | 1 | 1,001 | Naive B Cell | True | 3.442 | Naive B Cell | nan | nan | registry__naive_b_cell | pass |
| vaccination_study_09 | B_lineage | 2 | 995 | Naive B Cell | True | 3.227 | Naive B Cell | nan | nan | registry__naive_b_cell | pass |
| vaccination_study_09 | B_lineage | 3 | 735 | Memory B Cell | True | 2.787 | Memory B Cell | nan | nan | registry__memory_b_cell | pass |
| vaccination_study_09 | B_lineage | 4 | 705 | Naive B Cell | True | 3.485 | Naive B Cell | nan | nan | registry__naive_b_cell | pass |
| vaccination_study_09 | B_lineage | 5 | 688 | Naive B Cell | True | 3.550 | Naive B Cell | nan | nan | registry__naive_b_cell | pass |
| vaccination_study_09 | B_lineage | 6 | 634 | Naive B Cell | True | 3.726 | Naive B Cell | nan | nan | registry__naive_b_cell | pass |
| vaccination_study_09 | B_lineage | 7 | 449 | Memory B Cell | True | 0.898 | Memory B Cell | nan | nan | registry__memory_b_cell | pass |
| vaccination_study_09 | B_lineage | 8 | 381 | Memory B Cell | True | 1.747 | Memory B Cell | nan | nan | registry__memory_b_cell | pass |
| vaccination_study_09 | B_lineage | 9 | 354 | Naive B Cell | True | 4.104 | Naive B Cell | nan | nan | registry__naive_b_cell | pass |
| vaccination_study_09 | B_lineage | 10 | 345 | Naive B Cell | True | 4.005 | Naive B Cell | nan | nan | registry__naive_b_cell | pass |
| vaccination_study_09 | B_lineage | 11 | 327 | Memory B Cell | True | 1.886 | Naive B Cell | nan | nan | registry__memory_b_cell | pass |
| vaccination_study_09 | B_lineage | 12 | 324 | Naive B Cell | True | 3.437 | Naive B Cell | nan | nan | registry__naive_b_cell | pass |
| vaccination_study_09 | B_lineage | 13 | 311 | Naive B Cell | True | 2.636 | Naive B Cell | nan | nan | registry__naive_b_cell | pass |
| vaccination_study_09 | B_lineage | 14 | 257 | Naive B Cell | True | 3.939 | Naive B Cell | nan | nan | registry__naive_b_cell | pass |
| vaccination_study_09 | B_lineage | 15 | 250 | Naive B Cell | True | 3.770 | Naive B Cell | nan | nan | registry__naive_b_cell | pass |
| vaccination_study_09 | B_lineage | 16 | 250 | Naive B Cell | True | 3.759 | Naive B Cell | nan | nan | registry__naive_b_cell | pass |
| vaccination_study_09 | B_lineage | 17 | 237 | Naive B Cell | True | 3.391 | Naive B Cell | nan | nan | registry__naive_b_cell | pass |
| vaccination_study_09 | B_lineage | 18 | 236 | Naive B Cell | True | 3.964 | Naive B Cell | nan | nan | registry__naive_b_cell | pass |
| vaccination_study_09 | B_lineage | 19 | 233 | Naive B Cell | True | 3.991 | Naive B Cell | nan | nan | registry__naive_b_cell | pass |
| vaccination_study_09 | B_lineage | 20 | 232 | Naive B Cell | True | 3.705 | Naive B Cell | nan | nan | registry__naive_b_cell | pass |
| vaccination_study_09 | B_lineage | 21 | 231 | Naive B Cell | True | 3.939 | Naive B Cell | nan | nan | registry__naive_b_cell | pass |
| vaccination_study_09 | B_lineage | 22 | 225 | Naive B Cell | True | 3.569 | Naive B Cell | nan | nan | registry__naive_b_cell | pass |
| vaccination_study_09 | B_lineage | 23 | 219 | Naive B Cell | True | 3.718 | Naive B Cell | nan | nan | registry__naive_b_cell | pass |
| vaccination_study_09 | B_lineage | 24 | 213 | Naive B Cell | True | 3.378 | Naive B Cell | nan | nan | registry__naive_b_cell | pass |
| vaccination_study_09 | B_lineage | 25 | 212 | Naive B Cell | True | 4.064 | Naive B Cell | nan | nan | registry__naive_b_cell | pass |
| vaccination_study_09 | B_lineage | 26 | 210 | Naive B Cell | True | 3.768 | Naive B Cell | nan | nan | registry__naive_b_cell | pass |
| vaccination_study_09 | B_lineage | 27 | 209 | Naive B Cell | True | 4.016 | Naive B Cell | nan | nan | registry__naive_b_cell | pass |
| vaccination_study_09 | B_lineage | 28 | 198 | Naive B Cell | True | 4.131 | Naive B Cell | nan | nan | registry__naive_b_cell | pass |
| vaccination_study_09 | B_lineage | 29 | 195 | Naive B Cell | True | 2.872 | Naive B Cell | nan | nan | registry__naive_b_cell | pass |

## 出力ファイル

- Submission TSVs: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_final_v22/vaccination_study_09/submissions/`
- cellxgene H5ADs: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_final_v22/vaccination_study_09/cellxgene/`
- Marker availability table: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_final_v22/vaccination_study_09/tables/marker_gene_availability.tsv`
- Marker availability alerts: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_final_v22/vaccination_study_09/tables/marker_gene_availability_alerts.tsv`
- Subcluster evidence: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_final_v22/vaccination_study_09/tables/lineage_subcluster_evidence.tsv.gz`
- Source disagreement summary: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_final_v22/vaccination_study_09/tables/source_disagreement_summary.tsv`
- Source effectiveness summary: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_final_v22/vaccination_study_09/tables/source_effectiveness_summary.tsv`
- Diagnostics tables: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_final_v22/vaccination_study_09/tables/`
