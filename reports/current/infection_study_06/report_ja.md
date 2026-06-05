# HIPC データセットアノテーションレポート: infection_study_06

更新日: 2026-06-05 EDT

このレポートは `hipc-annotation` Codex workflow によって生成したデータセット別レビュー文書です。固定 method は repository README に置き、このレポートでは実際の evidence、弱い箇所、レビュー優先度、UMAP / dotplot を確認します。

## データセット概要

| study | cells | analysis_X_genes | pre_hvg_genes | counts_layer_genes | labels | parent_or_blood_fraction | Blood Cell | Doublet | artifact_like | median_confidence | low_confidence | source_disagreement | invalid_labels |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| infection_study_06 | 827,389 | 37,298 | 37,298 | 37,298 | 1 | 1.000 | 827,389 | 0 | 0 | 0.450 | 827,389 | 0 (0.000) | none |

## 実行概要

- 実行単位: one dataset in, one annotated dataset out。
- 実行経路: Codex skill `hipc-annotation` -> bundled helper `run_one.sh` -> annotation CLI -> validator -> report inspection。
- 検証: submission row count、H5AD observation count、official label validity、H5AD/submission agreement、confidence column、report image link を確認する。
- このレポートは workflow の再掲ではなく、このデータセットの marker 欠損、UMAP、label 構成、review concern を読むためのもの。

## データセット固有の解釈

- `infection_study_06`: 827,389 cells、analysis X/var 37,298 genes、pre-HVG slot 37,298 genes、submitted label 1 種、parent/Blood residual fraction 1.000、median confidence 0.450。
  - 827,389 cells は low confidence。QC / confidence UMAP 上で局在を確認する。
  - 827,389 cells は `Blood Cell` として残存。これは filter-out ではなく、曖昧な細胞を公式 parent label で残したもの。
  - Marker gene 欠損アラート: CD4_naive_tcm, CD4_effector_memory, Treg, gdT, NKT, B_naive, B_memory_ABC, Plasma_ASC。該当 marker set に依存する fine label は慎重に見る。

## データセット固有の評価

- 全体像: 827,389 cells / analysis X/var 37,298 genes / pre-HVG slot 37,298 genes。parent/Blood residual は 1.000、low-confidence は 827,389 cells、source disagreement flag は 0 cells (0.000)。
- 優先確認: low-confidence 領域が QC UMAP と source-disagreement UMAP で同じ場所に集まるかを確認する。
- 優先確認: `Blood Cell` 残存が孤立 cluster なのか、複数 lineage に分散した曖昧領域なのかを UMAP で確認する。
- Marker gene 欠損: CD4_naive_tcm, CD4_effector_memory, Treg, gdT, NKT, B_naive, B_memory_ABC, Plasma_ASC は confidence cap 対象。該当 label は marker expression UMAP と dotplot で妥当性を確認する。

## Marker Gene 欠損アラート

| study | marker_set | alert | present_fraction | missing_critical_markers | missing_genes |
| --- | --- | --- | --- | --- | --- |
| infection_study_06 | CD4_naive_tcm | critical | 0.000 | none | CD3D;CD3E;CD4;IL7R;CCR7;SELL;TCF7;LEF1;LTB |
| infection_study_06 | CD4_effector_memory | critical | 0.000 | GZMK;CCL5;NKG7;PRF1;GZMB | GZMK;CCL5;NKG7;GNLY;PRF1;GZMB;CXCR3;KLRB1 |
| infection_study_06 | Treg | critical | 0.000 | FOXP3;IL2RA;CTLA4 | FOXP3;IL2RA;CTLA4;IKZF2;TIGIT;TNFRSF18;CCR8 |
| infection_study_06 | gdT | critical | 0.000 | TRDC;TRGC1;TRGC2 | CD3D;CD3E;TRDC;TRGC1;TRGC2;TRDV2 |
| infection_study_06 | NKT | critical | 0.000 | CD3D;NKG7;ZBTB16 | CD3D;CD3E;TRAC;NKG7;GNLY;KLRD1;ZBTB16 |
| infection_study_06 | B_naive | critical | 0.000 | none | MS4A1;CD79A;CD79B;TCL1A;IGHD;IGHM;FCER2;IL4R |
| infection_study_06 | B_memory_ABC | critical | 0.000 | CD27;TNFRSF13B;FCRL5;ITGAX;TBX21 | CD27;TNFRSF13B;FCRL5;ITGAX;TBX21;AIM2;BANK1;CD86 |
| infection_study_06 | Plasma_ASC | critical | 0.000 | MZB1;JCHAIN;XBP1;PRDM1 | MZB1;XBP1;JCHAIN;SDC1;PRDM1;IRF4;TNFRSF17;IGHG1;IGHA1 |

## ソース間不一致

| study | predicted_cell_type | cells | median_source_agreement | disagreement_cells | disagreement_fraction |
| --- | --- | --- | --- | --- | --- |
| infection_study_06 | Blood Cell | 827,389 | 0.000 | 0 | 0.000 |

## アノテーションソース効果

この表は外部 ground truth に対する正解率ではありません。各 annotation source がどれだけの細胞で情報を持ち、final label とどれだけ一致したかを示す監査用統計です。`coverage` は source が `not_available` 以外を返した割合、`final_concordance` は informative cells の中で final label と一致した割合、`unique_support` はその source だけが final label と一致した細胞数です。

| study | source | informative_cells | coverage | final_concordance | high_conf_concordance | unique_support | discordant |
| --- | --- | --- | --- | --- | --- | --- | --- |
| infection_study_06 | CellTypist | 0 | 0.000 | 0.000 | 0.000 | 0 | 0 |
| infection_study_06 | Pan-human Azimuth | 0 | 0.000 | 0.000 | 0.000 | 0 | 0 |
| infection_study_06 | Cluster consensus | 0 | 0.000 | 0.000 | 0.000 | 0 | 0 |
| infection_study_06 | scRefMapping | 0 | 0.000 | 0.000 | 0.000 | 0 | 0 |
| infection_study_06 | Cluster marker assignment | 0 | 0.000 | 0.000 | 0.000 | 0 | 0 |

## レビュー優先事項

| study | concern | cells |
| --- | --- | --- |
| infection_study_06 | Large Blood Cell/ambiguous residual remains | 827,389 |
| infection_study_06 | Many low-confidence cells; QC or mixed-marker effects likely remain | 827,389 |

## ラベル構成

| study | predicted_cell_type | cells |
| --- | --- | --- |
| infection_study_06 | Blood Cell | 827,389 |

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

Skipped: fewer than 50 cells assigned to this broad lineage (`n_cells=0`).

Tables: `tables/infection_study_06_B_lineage_true_subcluster_umap.tsv.gz`, `tables/infection_study_06_B_lineage_subcluster_candidate_scores.tsv`.

#### infection_study_06 T_NK_lineage true subcluster UMAP

Skipped: fewer than 50 cells assigned to this broad lineage (`n_cells=0`).

Tables: `tables/infection_study_06_T_NK_lineage_true_subcluster_umap.tsv.gz`, `tables/infection_study_06_T_NK_lineage_subcluster_candidate_scores.tsv`.

#### infection_study_06 Myeloid_lineage true subcluster UMAP

Skipped: fewer than 50 cells assigned to this broad lineage (`n_cells=0`).

Tables: `tables/infection_study_06_Myeloid_lineage_true_subcluster_umap.tsv.gz`, `tables/infection_study_06_Myeloid_lineage_subcluster_candidate_scores.tsv`.


## Subcluster Marker Score Review

上の lineage-specific panel は、各 lineage subset で HVG 選択、PCA、neighbors、Leiden、UMAP を再計算した true local subcluster analysis から生成しています。Marker gene による fine label の確認は global UMAP だけではなく、この local UMAP、CellTypist/Azimuth/Pan-human/cluster-level marker gene assignment overlay、cluster marker gate score UMAP、marker-expression UMAP、dotplot を主に見ます。Treg など sparse marker label は cell-wise marker winner ではなく、local cluster の FOXP3/IL2RA/CTLA4 など key-marker support と reference support で判定します。

## Marker Assignment Feedback

Marker gene assignment は final label を強制的に上書きするものではなく、cluster-level の自己点検です。`raw_marker_winner` は marker score だけの勝者、`marker_assignment` は conservative policy と source-supported tie-break を通した marker-based assignment です。この表は marker assignment と final/reference-driven label がずれる cluster、marker specificity が弱い cluster、scRefMap が期待される lineage で欠落する cluster を示します。`marker_score` は raw marker base score から negative/confound marker penalty を差し引いた cluster-level marker gate score です。

なし。

## LLM Review Queue

この表は Codex/LLM が読むための subcluster-level review queue です。LLM はこの evidence を読んで、final label が妥当か、ontology にちょうどよい label がないのか、registry / conservative policy を一般ルールとして更新すべきかを提案します。LLM の出力で per-cell label を直接書き換えず、採用する場合は registry/config を更新して deterministic pipeline を再実行します。

なし。

## Cluster Consensus Evidence

なし。

## 出力ファイル

- Submission TSVs: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_final_v22/infection_study_06/submissions/`
- cellxgene H5ADs: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_final_v22/infection_study_06/cellxgene/`
- Marker availability table: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_final_v22/infection_study_06/tables/marker_gene_availability.tsv`
- Marker availability alerts: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_final_v22/infection_study_06/tables/marker_gene_availability_alerts.tsv`
- Subcluster evidence: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_final_v22/infection_study_06/tables/lineage_subcluster_evidence.tsv.gz`
- Source disagreement summary: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_final_v22/infection_study_06/tables/source_disagreement_summary.tsv`
- Source effectiveness summary: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_final_v22/infection_study_06/tables/source_effectiveness_summary.tsv`
- Diagnostics tables: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_final_v22/infection_study_06/tables/`

