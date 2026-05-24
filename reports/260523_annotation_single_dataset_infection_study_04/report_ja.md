# HIPC データセットアノテーションレポート: infection_study_04

更新日: 2026-05-23 EDT

このレポートは `hipc-annotation` Codex workflow によって生成したデータセット別レビュー文書です。固定 method は repository README に置き、このレポートでは実際の evidence、弱い箇所、レビュー優先度、UMAP / dotplot を確認します。

## データセット概要

| study | cells | genes | labels | parent_or_blood_fraction | Blood Cell | Doublet | artifact_like | median_confidence | low_confidence | source_disagreement | invalid_labels |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| infection_study_04 | 43,767 | 3,933 | 16 | 0.012 | 529 | 61 | 353 | 0.838 | 751 | 11,680 (0.267) | none |

## 実行概要

- 実行単位: one dataset in, one annotated dataset out。
- 実行経路: Codex skill `hipc-annotation` -> bundled helper `run_one.sh` -> annotation CLI -> validator -> report inspection。
- 検証: submission row count、H5AD observation count、official label validity、H5AD/submission agreement、confidence column、report image link を確認する。
- このレポートは workflow の再掲ではなく、このデータセットの marker 欠損、UMAP、label 構成、review concern を読むためのもの。

## データセット固有の解釈

- `infection_study_04`: 43,767 cells、3,933 genes、submitted label 16 種、parent/Blood residual fraction 0.012、median confidence 0.838。
  - 751 cells は low confidence。QC / confidence UMAP 上で局在を確認する。
  - 61 cells は `Doublet` として提出。mixed-lineage marker expression と scrublet support を確認する。
  - 529 cells は `Blood Cell` として残存。これは filter-out ではなく、曖昧な細胞を公式 parent label で残したもの。
  - Marker gene 欠損アラート: Treg, Plasma_ASC。該当 marker set に依存する fine label は慎重に見る。

## データセット固有の評価

- 全体像: 43,767 cells / 3,933 genes。parent/Blood residual は 0.012、low-confidence は 751 cells、source disagreement flag は 11,680 cells (0.267)。
- 優先確認: low-confidence 領域が QC UMAP と source-disagreement UMAP で同じ場所に集まるかを確認する。
- 優先確認: `Blood Cell` 残存が孤立 cluster なのか、複数 lineage に分散した曖昧領域なのかを UMAP で確認する。
- Marker gene 欠損: Treg, Plasma_ASC は confidence cap 対象。該当 label は marker expression UMAP と dotplot で妥当性を確認する。
- Codex review: source disagreement は全体の 26.7% で無視できない。特に `Memory B Cell` は 72.4%、`Treg` は 70.2% が disagreement flag で、reference label と marker/cluster-based final label のずれが大きい。B memory/naive 境界と Treg は最優先の目視確認対象。
- Codex review: `Treg` は FOXP3/IL2RA/CTLA4 が var に無く、IKZF2/TIGIT など限られた marker での判定になる。提出 label としては残しているが、confidence cap 済みの provisional fine label として扱う。
- Codex review: `Plasma Cell` は JCHAIN が欠損している一方で MZB1/XBP1/PRDM1/IRF4 が存在し、source disagreement fraction も 9.2% と低い。Treg よりは robust だが、JCHAIN 欠損は report 上に残す。
- Codex review: `Blood Cell` と `Doublet` は disagreement fraction 1.0 だが、これは parent/override label の性質上 expected。問題は数ではなく UMAP 上で孤立した ambiguous region か、複数 lineage に散る QC/mixed artifact かを確認すること。
- Codex review: CD4/CD8 T cell は disagreement cells が多いが、fraction は 33-37% 程度で、細胞数が多いことの影響もある。source-disagreement UMAP で特定 cluster に濃縮する場合は T subtype rule の再調整候補。

## Marker Gene 欠損アラート

| study | marker_set | alert | present_fraction | missing_critical_markers | missing_genes |
| --- | --- | --- | --- | --- | --- |
| infection_study_04 | Treg | critical | 0.286 | FOXP3;IL2RA;CTLA4 | FOXP3;IL2RA;CTLA4;TNFRSF18;CCR8 |
| infection_study_04 | Plasma_ASC | warning | 0.667 | JCHAIN | JCHAIN;SDC1;TNFRSF17 |

## ソース間不一致

| study | predicted_cell_type | cells | median_source_agreement | disagreement_cells | disagreement_fraction |
| --- | --- | --- | --- | --- | --- |
| infection_study_04 | Blood Cell | 529 | 0.000 | 529 | 1.000 |
| infection_study_04 | Doublet | 61 | 0.000 | 61 | 1.000 |
| infection_study_04 | Memory B Cell | 1,136 | 0.400 | 823 | 0.724 |
| infection_study_04 | Treg | 554 | 0.400 | 389 | 0.702 |
| infection_study_04 | Naive B Cell | 2,070 | 0.600 | 811 | 0.392 |
| infection_study_04 | CD4 Naive / T Central Memory | 7,824 | 0.600 | 2,925 | 0.374 |
| infection_study_04 | CD8 Cytotoxic / T Effector Memory | 8,696 | 0.500 | 2,933 | 0.337 |
| infection_study_04 | Classical Monocyte | 11,755 | 0.750 | 1,979 | 0.168 |
| infection_study_04 | NK Cell | 6,007 | 1.000 | 852 | 0.142 |
| infection_study_04 | Conventional DC 2 | 306 | 0.750 | 34 | 0.111 |
| infection_study_04 | Plasma Cell | 3,145 | 0.800 | 288 | 0.092 |
| infection_study_04 | Non-Classical Monocyte | 1,102 | 1.000 | 48 | 0.044 |

## レビュー優先事項

| study | concern | cells |
| --- | --- | --- |
| infection_study_04 | High source disagreement for Blood Cell | 529 |
| infection_study_04 | High source disagreement for Doublet | 61 |
| infection_study_04 | High source disagreement for Memory B Cell | 823 |
| infection_study_04 | High source disagreement for Treg | 389 |
| infection_study_04 | High dataset-level source disagreement | 11,680 |
| infection_study_04 | critical marker availability for Treg | 554 |
| infection_study_04 | warning marker availability for Plasma_ASC | 3,145 |

## ラベル構成

| study | predicted_cell_type | cells |
| --- | --- | --- |
| infection_study_04 | Classical Monocyte | 11,755 |
| infection_study_04 | CD8 Cytotoxic / T Effector Memory | 8,696 |
| infection_study_04 | CD4 Naive / T Central Memory | 7,824 |
| infection_study_04 | NK Cell | 6,007 |
| infection_study_04 | Plasma Cell | 3,145 |
| infection_study_04 | Naive B Cell | 2,070 |
| infection_study_04 | Memory B Cell | 1,136 |
| infection_study_04 | Non-Classical Monocyte | 1,102 |
| infection_study_04 | Treg | 554 |
| infection_study_04 | Blood Cell | 529 |
| infection_study_04 | Conventional DC 2 | 306 |
| infection_study_04 | Plasmacytoid DC | 229 |
| infection_study_04 | Platelet | 148 |
| infection_study_04 | RBC | 132 |
| infection_study_04 | HSC | 73 |
| infection_study_04 | Doublet | 61 |

## 図

### infection_study_04

![infection_study_04 final labels](assets/umap_infection_study_04_annotation_label.png)

![infection_study_04 lineage and annotation reason](assets/umap_infection_study_04_annotation_lineage_reason.png)

![infection_study_04 QC and confidence](assets/umap_infection_study_04_annotation_qc_confidence.png)

![infection_study_04 source agreement and disagreement](assets/umap_infection_study_04_annotation_source_disagreement.png)

![infection_study_04 marker expression UMAPs](assets/umap_infection_study_04_annotation_marker_expression.png)

![infection_study_04 submitted-label marker dotplot](assets/dotplot_infection_study_04_annotation_marker_dotplot.png)

#### infection_study_04 B_lineage subcluster UMAP

![infection_study_04 B_lineage subcluster labels](assets/umap_infection_study_04_B_lineage_subcluster_label.png)

![infection_study_04 B_lineage subcluster QC](assets/umap_infection_study_04_B_lineage_subcluster_qc.png)

#### infection_study_04 T_NK_lineage subcluster UMAP

![infection_study_04 T_NK_lineage subcluster labels](assets/umap_infection_study_04_T_NK_lineage_subcluster_label.png)

![infection_study_04 T_NK_lineage subcluster QC](assets/umap_infection_study_04_T_NK_lineage_subcluster_qc.png)

#### infection_study_04 Myeloid_lineage subcluster UMAP

![infection_study_04 Myeloid_lineage subcluster labels](assets/umap_infection_study_04_Myeloid_lineage_subcluster_label.png)

![infection_study_04 Myeloid_lineage subcluster QC](assets/umap_infection_study_04_Myeloid_lineage_subcluster_qc.png)


## 出力ファイル

- Submission TSVs: `outputs/single_dataset_checks/260523_infection_study_04_assessment_v2/submissions/`
- cellxgene H5ADs: `outputs/single_dataset_checks/260523_infection_study_04_assessment_v2/cellxgene/`
- Marker availability table: `outputs/single_dataset_checks/260523_infection_study_04_assessment_v2/tables/marker_gene_availability.tsv`
- Marker availability alerts: `outputs/single_dataset_checks/260523_infection_study_04_assessment_v2/tables/marker_gene_availability_alerts.tsv`
- Subcluster evidence: `outputs/single_dataset_checks/260523_infection_study_04_assessment_v2/tables/lineage_subcluster_evidence.tsv.gz`
- Source disagreement summary: `outputs/single_dataset_checks/260523_infection_study_04_assessment_v2/tables/source_disagreement_summary.tsv`
- Diagnostics tables: `outputs/single_dataset_checks/260523_infection_study_04_assessment_v2/tables/`

## 追加レビュー用プロンプト

このデータセット別 HIPC annotation report をレビューしてください。
marker gene 欠損アラート、parent/Blood label の残存、low-confidence 領域、doublet call、marker-expression UMAP が submitted label を支持しているかに注目してください。
README の固定 workflow は繰り返さず、このデータセット固有の懸念点と次に確認すべき点だけを返してください。
