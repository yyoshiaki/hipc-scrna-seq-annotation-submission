# HIPC データセットアノテーションレポート: infection_study_01

更新日: 2026-06-12 EDT

## 現行提出用サマリー

| 項目 | 内容 |
| --- | --- |
| 提出候補 package | v24 pragmatic package |
| 採用 source | `outputs/submission_final_v22/infection_study_01/submissions/infection_study_01_annotation.tsv` |
| 細胞数 | 54,924 |
| label 数 | 16 |
| parent/Blood residual | 178 cells (0.0032) |
| median confidence | 0.7772 |
| 上位 label | Classical Monocyte: 17,789; CD8 Cytotoxic / T Effector Memory: 10,509; NK Cell: 8,060; CD4 T Effector Memory: 4,387; Naive B Cell: 4,269; CD4 Naive / T Central Memory: 2,341; Memory B Cell: 2,100; Non-Classical Monocyte: 1,979 |
| 現状判断 | 提出候補として比較的良好。parent/Blood residual は低く、個別 UMAP と marker evidence の確認を優先する。 |

このレポートは `hipc-annotation` Codex workflow によって生成したデータセット別レビュー文書です。固定 method は repository README に置き、このレポートでは実際の evidence、弱い箇所、レビュー優先度、UMAP / dotplot を確認します。

## データセット概要

| study | cells | analysis_X_genes | pre_hvg_genes | counts_layer_genes | labels | parent_or_blood_fraction | Blood Cell | Doublet | artifact_like | median_confidence | low_confidence | source_disagreement | invalid_labels |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| infection_study_01 | 54,924 | 3,961 | 8,000 | 3,961 | 16 | 0.003 | 178 | 981 | 1,313 | 0.777 | 2,527 | 7,522 (0.137) | none |

## 実行概要

- 実行単位: one dataset in, one annotated dataset out。
- 実行経路: Codex skill `hipc-annotation` -> bundled helper `run_one.sh` -> annotation CLI -> validator -> report inspection。
- 検証: submission row count、H5AD observation count、official label validity、H5AD/submission agreement、confidence column、report image link を確認する。
- このレポートは workflow の再掲ではなく、このデータセットの marker 欠損、UMAP、label 構成、review concern を読むためのもの。

## データセット固有の解釈

- `infection_study_01`: 54,924 cells、analysis X/var 3,961 genes、pre-HVG slot 8,000 genes、submitted label 16 種、parent/Blood residual fraction 0.003、median confidence 0.777。
  - 2,527 cells は low confidence。QC / confidence UMAP 上で局在を確認する。
  - 981 cells は `Doublet` として提出。mixed-lineage marker expression と scrublet support を確認する。
  - 178 cells は `Blood Cell` として残存。これは filter-out ではなく、曖昧な細胞を公式 parent label で残したもの。
  - Marker gene 欠損アラート: Treg, B_memory_ABC, Plasma_ASC。該当 marker set に依存する fine label は慎重に見る。

## データセット固有の評価

- 全体像: 54,924 cells / analysis X/var 3,961 genes / pre-HVG slot 8,000 genes。parent/Blood residual は 0.003、low-confidence は 2,527 cells、source disagreement flag は 7,522 cells (0.137)。
- 優先確認: low-confidence 領域が QC UMAP と source-disagreement UMAP で同じ場所に集まるかを確認する。
- 優先確認: `Blood Cell` 残存が孤立 cluster なのか、複数 lineage に分散した曖昧領域なのかを UMAP で確認する。
- Marker gene 欠損: Treg, B_memory_ABC, Plasma_ASC は confidence cap 対象。該当 label は marker expression UMAP と dotplot で妥当性を確認する。

## Marker Gene 欠損アラート

| study | marker_set | alert | present_fraction | missing_critical_markers | missing_genes |
| --- | --- | --- | --- | --- | --- |
| infection_study_01 | Treg | critical | 0.143 | FOXP3;IL2RA;CTLA4 | FOXP3;IL2RA;CTLA4;IKZF2;TNFRSF18;CCR8 |
| infection_study_01 | B_memory_ABC | warning | 0.500 | TNFRSF13B;FCRL5 | TNFRSF13B;FCRL5;AIM2;CD86 |
| infection_study_01 | Plasma_ASC | warning | 0.444 | MZB1 | MZB1;SDC1;IRF4;TNFRSF17;IGHG1 |

## ソース間不一致

| study | predicted_cell_type | cells | median_source_agreement | disagreement_cells | disagreement_fraction |
| --- | --- | --- | --- | --- | --- |
| infection_study_01 | Doublet | 981 | 0.000 | 981 | 1.000 |
| infection_study_01 | Blood Cell | 178 | 0.000 | 178 | 1.000 |
| infection_study_01 | Plasmablast | 44 | 0.250 | 44 | 1.000 |
| infection_study_01 | MAIT Cell | 284 | 0.667 | 78 | 0.275 |
| infection_study_01 | CD4 T Effector Memory | 4,387 | 0.667 | 1,143 | 0.261 |
| infection_study_01 | CD8 Cytotoxic / T Effector Memory | 10,509 | 1.000 | 2,561 | 0.244 |
| infection_study_01 | NK Cell | 8,060 | 1.000 | 1,021 | 0.127 |
| infection_study_01 | CD4 Naive / T Central Memory | 2,341 | 1.000 | 285 | 0.122 |
| infection_study_01 | Conventional DC 2 | 469 | 1.000 | 54 | 0.115 |
| infection_study_01 | Non-Classical Monocyte | 1,979 | 1.000 | 186 | 0.094 |
| infection_study_01 | Naive B Cell | 4,269 | 1.000 | 278 | 0.065 |
| infection_study_01 | Plasmacytoid DC | 93 | 0.667 | 6 | 0.065 |

## アノテーションソース効果

この表は外部 ground truth に対する正解率ではありません。各 annotation source がどれだけの細胞で情報を持ち、final label とどれだけ一致したかを示す監査用統計です。`coverage` は source が `not_available` 以外を返した割合、`final_concordance` は informative cells の中で final label と一致した割合、`unique_support` はその source だけが final label と一致した細胞数です。

| study | source | informative_cells | coverage | final_concordance | high_conf_concordance | unique_support | discordant |
| --- | --- | --- | --- | --- | --- | --- | --- |
| infection_study_01 | CellTypist | 54,924 | 1.000 | 0.857 | 0.945 | 20 | 7,858 |
| infection_study_01 | Cluster consensus | 54,924 | 1.000 | 0.825 | 0.901 | 190 | 9,586 |
| infection_study_01 | Pan-human Azimuth | 54,924 | 1.000 | 0.746 | 0.793 | 72 | 13,962 |
| infection_study_01 | Cluster marker assignment | 52,452 | 0.955 | 0.925 | 0.964 | 3,120 | 3,918 |
| infection_study_01 | scRefMapping | 11,783 | 0.215 | 0.732 | 0.952 | 16 | 3,158 |

## レビュー優先事項

| study | concern | cells |
| --- | --- | --- |
| infection_study_01 | High source disagreement for Blood Cell | 178 |
| infection_study_01 | High source disagreement for Doublet | 981 |
| infection_study_01 | High source disagreement for Plasmablast | 44 |
| infection_study_01 | warning marker availability for B_memory_ABC | 2,100 |
| infection_study_01 | warning marker availability for Plasma_ASC | 172 |

## ラベル構成

| study | predicted_cell_type | cells |
| --- | --- | --- |
| infection_study_01 | Classical Monocyte | 17,789 |
| infection_study_01 | CD8 Cytotoxic / T Effector Memory | 10,509 |
| infection_study_01 | NK Cell | 8,060 |
| infection_study_01 | CD4 T Effector Memory | 4,387 |
| infection_study_01 | Naive B Cell | 4,269 |
| infection_study_01 | CD4 Naive / T Central Memory | 2,341 |
| infection_study_01 | Memory B Cell | 2,100 |
| infection_study_01 | Non-Classical Monocyte | 1,979 |
| infection_study_01 | Platelet | 1,313 |
| infection_study_01 | Doublet | 981 |
| infection_study_01 | Conventional DC 2 | 469 |
| infection_study_01 | MAIT Cell | 284 |
| infection_study_01 | Blood Cell | 178 |
| infection_study_01 | Plasma Cell | 128 |
| infection_study_01 | Plasmacytoid DC | 93 |
| infection_study_01 | Plasmablast | 44 |

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
| infection_study_01 | T_NK_lineage | 0 | 1,549 | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | NKT Cell | conservative_policy_blocks_raw_marker_winner | 0.565 | 1.000 | 0.435 | screfmapping_missing_for_scope |
| infection_study_01 | T_NK_lineage | 1 | 1,517 | NK Cell | NK Cell | NKT Cell | conservative_policy_blocks_raw_marker_winner | 0.868 | 1.000 | 0.132 | screfmapping_missing_for_scope |
| infection_study_01 | T_NK_lineage | 3 | 1,263 | NK Cell | NK Cell | NKT Cell | conservative_policy_blocks_raw_marker_winner | 0.911 | 1.000 | 0.089 | screfmapping_missing_for_scope |
| infection_study_01 | T_NK_lineage | 4 | 1,255 | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | NKT Cell | conservative_policy_blocks_raw_marker_winner | 0.667 | 1.000 | 0.333 | screfmapping_missing_for_scope |
| infection_study_01 | T_NK_lineage | 5 | 1,212 | NK Cell | NK Cell | NKT Cell | conservative_policy_blocks_raw_marker_winner | 0.838 | 0.997 | 0.159 | screfmapping_missing_for_scope |
| infection_study_01 | T_NK_lineage | 6 | 1,203 | CD4 T Effector Memory | CD4 Naive / T Central Memory | CD4 Naive / T Central Memory | raw_marker_winner | 0.829 | 1.000 | 0.171 | marker_final_disagreement |
| infection_study_01 | T_NK_lineage | 7 | 1,101 | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | NKT Cell | conservative_policy_blocks_raw_marker_winner | 0.719 | 1.000 | 0.281 | screfmapping_missing_for_scope |
| infection_study_01 | T_NK_lineage | 9 | 990 | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | NKT Cell | conservative_policy_blocks_raw_marker_winner | 0.800 | 1.000 | 0.200 | screfmapping_missing_for_scope |
| infection_study_01 | T_NK_lineage | 11 | 911 | CD4 T Effector Memory | CD4 Naive / T Central Memory | CD4 Naive / T Central Memory | raw_marker_winner | 0.746 | 0.964 | 0.218 | marker_final_disagreement |
| infection_study_01 | T_NK_lineage | 12 | 796 | NK Cell | NK Cell | NKT Cell | conservative_policy_blocks_raw_marker_winner | 0.876 | 1.000 | 0.124 | screfmapping_missing_for_scope |
| infection_study_01 | T_NK_lineage | 13 | 784 | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | NKT Cell | conservative_policy_blocks_raw_marker_winner | 0.745 | 1.000 | 0.255 | screfmapping_missing_for_scope |
| infection_study_01 | T_NK_lineage | 14 | 748 | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | NKT Cell | conservative_policy_blocks_raw_marker_winner | 0.753 | 1.000 | 0.247 | screfmapping_missing_for_scope |
| infection_study_01 | T_NK_lineage | 15 | 746 | NK Cell | NK Cell | NKT Cell | conservative_policy_blocks_raw_marker_winner | 0.854 | 0.999 | 0.145 | screfmapping_missing_for_scope |
| infection_study_01 | T_NK_lineage | 16 | 735 | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | NKT Cell | conservative_policy_blocks_raw_marker_winner | 0.752 | 1.000 | 0.248 | screfmapping_missing_for_scope |
| infection_study_01 | T_NK_lineage | 17 | 722 | NK Cell | NK Cell | NKT Cell | conservative_policy_blocks_raw_marker_winner | 0.840 | 0.964 | 0.124 | screfmapping_missing_for_scope |
| infection_study_01 | T_NK_lineage | 18 | 692 | NK Cell | NK Cell | NKT Cell | conservative_policy_blocks_raw_marker_winner | 0.856 | 1.000 | 0.144 | screfmapping_missing_for_scope |
| infection_study_01 | T_NK_lineage | 19 | 677 | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | NKT Cell | conservative_policy_blocks_raw_marker_winner | 0.645 | 1.000 | 0.355 | screfmapping_missing_for_scope |
| infection_study_01 | T_NK_lineage | 21 | 585 | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | NKT Cell | conservative_policy_blocks_raw_marker_winner | 0.561 | 1.000 | 0.439 | screfmapping_missing_for_scope |
| infection_study_01 | T_NK_lineage | 22 | 575 | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | NKT Cell | conservative_policy_blocks_raw_marker_winner | 0.554 | 1.000 | 0.446 | screfmapping_missing_for_scope |
| infection_study_01 | T_NK_lineage | 23 | 541 | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | NKT Cell | conservative_policy_blocks_raw_marker_winner | 0.763 | 1.000 | 0.237 | screfmapping_missing_for_scope |

## LLM Review Queue

この表は Codex/LLM が読むための subcluster-level review queue です。LLM はこの evidence を読んで、final label が妥当か、ontology にちょうどよい label がないのか、registry / conservative policy を一般ルールとして更新すべきかを提案します。LLM の出力で per-cell label を直接書き換えず、採用する場合は registry/config を更新して deterministic pipeline を再実行します。

| study | lineage | cluster | cells | priority | reasons | suggested_action | final_label | marker_assignment | raw_marker_winner | score_margin |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| infection_study_01 | T_NK_lineage | 0 | 1,549 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | NKT Cell | 1.949 |
| infection_study_01 | T_NK_lineage | 1 | 1,517 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | NK Cell | NK Cell | NKT Cell | 2.208 |
| infection_study_01 | T_NK_lineage | 3 | 1,263 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | NK Cell | NK Cell | NKT Cell | 2.062 |
| infection_study_01 | T_NK_lineage | 4 | 1,255 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | NKT Cell | 2.181 |
| infection_study_01 | T_NK_lineage | 5 | 1,212 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | NK Cell | NK Cell | NKT Cell | 2.500 |
| infection_study_01 | T_NK_lineage | 7 | 1,101 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | NKT Cell | 1.508 |
| infection_study_01 | T_NK_lineage | 33 | 90 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available;low_total_score_or_margin | evaluate_ontology_gap_or_conservative_policy | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | NKT Cell | 0.063 |
| infection_study_01 | T_NK_lineage | 9 | 990 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | NKT Cell | 0.141 |
| infection_study_01 | T_NK_lineage | 12 | 796 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | NK Cell | NK Cell | NKT Cell | 2.312 |
| infection_study_01 | T_NK_lineage | 13 | 784 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | NKT Cell | 0.392 |
| infection_study_01 | T_NK_lineage | 14 | 748 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | NKT Cell | 1.238 |
| infection_study_01 | T_NK_lineage | 15 | 746 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | NK Cell | NK Cell | NKT Cell | 2.519 |
| infection_study_01 | T_NK_lineage | 16 | 735 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | NKT Cell | 2.038 |
| infection_study_01 | T_NK_lineage | 17 | 722 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | NK Cell | NK Cell | NKT Cell | 0.173 |
| infection_study_01 | T_NK_lineage | 18 | 692 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | NK Cell | NK Cell | NKT Cell | 2.413 |
| infection_study_01 | T_NK_lineage | 19 | 677 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | NKT Cell | 2.307 |
| infection_study_01 | T_NK_lineage | 21 | 585 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | NKT Cell | 2.543 |
| infection_study_01 | T_NK_lineage | 22 | 575 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | NKT Cell | 2.491 |
| infection_study_01 | T_NK_lineage | 23 | 541 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | CD8 Cytotoxic / T Effector Memory | CD8 Cytotoxic / T Effector Memory | NKT Cell | 2.355 |
| infection_study_01 | T_NK_lineage | 25 | 441 | medium | raw_marker_winner_changed_by_policy;ambiguous_or_missing_label_candidate;screfmapping_not_available | evaluate_ontology_gap_or_conservative_policy | NK Cell | NK Cell | NKT Cell | 0.524 |

## Cluster Consensus Evidence

| study | lineage | cluster | cells | chosen_label | accepted | score_margin | cluster_marker_assignment | treg_key_any | treg_key_bonus | marker_set | marker_alert |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| infection_study_01 | B_lineage | 0 | 504 | Memory B Cell | True | 4.223 | Memory B Cell | nan | nan | registry__memory_b_cell | pass |
| infection_study_01 | B_lineage | 1 | 473 | Naive B Cell | True | 4.191 | Naive B Cell | nan | nan | registry__naive_b_cell | pass |
| infection_study_01 | B_lineage | 2 | 467 | Naive B Cell | True | 4.431 | Naive B Cell | nan | nan | registry__naive_b_cell | pass |
| infection_study_01 | B_lineage | 3 | 460 | Memory B Cell | True | 2.943 | Naive B Cell | nan | nan | registry__memory_b_cell | pass |
| infection_study_01 | B_lineage | 4 | 416 | Naive B Cell | True | 4.582 | Naive B Cell | nan | nan | registry__naive_b_cell | pass |
| infection_study_01 | B_lineage | 5 | 376 | Naive B Cell | True | 3.732 | Naive B Cell | nan | nan | registry__naive_b_cell | pass |
| infection_study_01 | B_lineage | 6 | 369 | Naive B Cell | True | 4.196 | Naive B Cell | nan | nan | registry__naive_b_cell | pass |
| infection_study_01 | B_lineage | 7 | 346 | Naive B Cell | True | 4.258 | Naive B Cell | nan | nan | registry__naive_b_cell | pass |
| infection_study_01 | B_lineage | 8 | 327 | Memory B Cell | True | 2.872 | Naive B Cell | nan | nan | registry__memory_b_cell | pass |
| infection_study_01 | B_lineage | 9 | 326 | Naive B Cell | True | 4.241 | Naive B Cell | nan | nan | registry__naive_b_cell | pass |
| infection_study_01 | B_lineage | 10 | 321 | Memory B Cell | True | 3.339 | Memory B Cell | nan | nan | registry__memory_b_cell | pass |
| infection_study_01 | B_lineage | 11 | 288 | Memory B Cell | True | 3.718 | Memory B Cell | nan | nan | registry__memory_b_cell | pass |
| infection_study_01 | B_lineage | 12 | 280 | Naive B Cell | True | 4.006 | Naive B Cell | nan | nan | registry__naive_b_cell | pass |
| infection_study_01 | B_lineage | 13 | 241 | Naive B Cell | True | 2.294 | Naive B Cell | nan | nan | registry__naive_b_cell | pass |
| infection_study_01 | B_lineage | 14 | 217 | Naive B Cell | True | 4.361 | Naive B Cell | nan | nan | registry__naive_b_cell | pass |
| infection_study_01 | B_lineage | 15 | 216 | Naive B Cell | True | 4.369 | Naive B Cell | nan | nan | registry__naive_b_cell | pass |
| infection_study_01 | B_lineage | 16 | 200 | Memory B Cell | True | 2.771 | Naive B Cell | nan | nan | registry__memory_b_cell | pass |
| infection_study_01 | B_lineage | 17 | 167 | Naive B Cell | True | 4.314 | Naive B Cell | nan | nan | registry__naive_b_cell | pass |
| infection_study_01 | B_lineage | 18 | 151 | Naive B Cell | True | 2.082 | Naive B Cell | nan | nan | registry__naive_b_cell | pass |
| infection_study_01 | B_lineage | 19 | 138 | Naive B Cell | True | 3.781 | Naive B Cell | nan | nan | registry__naive_b_cell | pass |
| infection_study_01 | B_lineage | 20 | 128 | Plasma Cell | True | 3.512 | Plasma Cell | nan | nan | registry__plasma_cell | pass |
| infection_study_01 | B_lineage | 21 | 44 | Plasmablast | True | 0.437 | Plasmablast | nan | nan | registry__plasmablast | pass |
| infection_study_01 | B_lineage | 22 | 42 | Naive B Cell | True | 2.572 | Naive B Cell | nan | nan | registry__naive_b_cell | pass |
| infection_study_01 | B_lineage | 23 | 23 | Naive B Cell | True | 2.547 | Naive B Cell | nan | nan | registry__naive_b_cell | pass |
| infection_study_01 | B_lineage | 24 | 21 | Naive B Cell | True | 2.148 | Naive B Cell | nan | nan | registry__naive_b_cell | pass |
| infection_study_01 | Myeloid_lineage | 0 | 1,613 | Non-Classical Monocyte | True | 1.692 | Non-Classical Monocyte | nan | nan | registry__non_classical_monocyte | pass |
| infection_study_01 | Myeloid_lineage | 1 | 1,595 | Classical Monocyte | True | 2.463 | Classical Monocyte | nan | nan | registry__classical_monocyte | pass |
| infection_study_01 | Myeloid_lineage | 2 | 1,496 | Classical Monocyte | True | 2.520 | Classical Monocyte | nan | nan | registry__classical_monocyte | pass |
| infection_study_01 | Myeloid_lineage | 3 | 1,447 | Classical Monocyte | True | 1.947 | Classical Monocyte | nan | nan | registry__classical_monocyte | pass |
| infection_study_01 | Myeloid_lineage | 4 | 1,327 | Classical Monocyte | True | 2.144 | Classical Monocyte | nan | nan | registry__classical_monocyte | pass |

## 出力ファイル

- Submission TSVs: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_final_v22/infection_study_01/submissions/`
- cellxgene H5ADs: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_final_v22/infection_study_01/cellxgene/`
- Marker availability table: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_final_v22/infection_study_01/tables/marker_gene_availability.tsv`
- Marker availability alerts: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_final_v22/infection_study_01/tables/marker_gene_availability_alerts.tsv`
- Subcluster evidence: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_final_v22/infection_study_01/tables/lineage_subcluster_evidence.tsv.gz`
- Source disagreement summary: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_final_v22/infection_study_01/tables/source_disagreement_summary.tsv`
- Source effectiveness summary: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_final_v22/infection_study_01/tables/source_effectiveness_summary.tsv`
- Diagnostics tables: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_final_v22/infection_study_01/tables/`
