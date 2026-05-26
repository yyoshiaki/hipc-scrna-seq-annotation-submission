# HIPC データセットアノテーションレポート: vaccination_study_09

更新日: 2026-05-26 EDT

このレポートは `hipc-annotation` Codex workflow によって生成したデータセット別レビュー文書です。固定 method は repository README に置き、このレポートでは実際の evidence、弱い箇所、レビュー優先度、UMAP / dotplot を確認します。

## 重要な制限

この 260526 report は v11 evidence container から生成した中間レビューです。4 dataset では upstream workflow が元の gene space を 8,000 genes に prefilter し、その後 HVG subset で約 4,000 genes の analysis X に落としています。そのため、この report の marker gene 欠損アラートは「元データに遺伝子が無い」という意味ではなく、「v11 analysis container に無い」という意味です。FOXP3/IL2RA/CTLA4 など、元の processed H5AD には存在するが analysis container から落ちている marker が確認されています。最終判断には、CellTypist、marker scoring、marker availability を original all-gene input から再計算する必要があります。

## データセット概要

| study | cells | original_processed_genes | pre_hvg_genes | analysis_X_genes | counts_layer_genes | labels | parent_or_blood_fraction | Blood Cell | Doublet | artifact_like | median_confidence | low_confidence | source_disagreement | invalid_labels |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| vaccination_study_09 | 139,960 | 19,141 | 8,000 | 3,985 | 3,985 | 17 | 0.001 | 120 | 323 | 104 | 0.838 | 443 | 29,879 (0.213) | none |

## 実行概要

- 実行単位: one dataset in, one annotated dataset out。
- 実行経路: Codex skill `hipc-annotation` -> bundled helper `run_one.sh` -> annotation CLI -> validator -> report inspection。
- 検証: submission row count、H5AD observation count、official label validity、H5AD/submission agreement、confidence column、report image link を確認する。
- このレポートは workflow の再掲ではなく、このデータセットの marker 欠損、UMAP、label 構成、review concern を読むためのもの。

## データセット固有の解釈

- `vaccination_study_09`: 139,960 cells、original processed 19,141 genes、pre-HVG 8,000 genes、analysis X/var 3,985 genes、submitted label 17 種、parent/Blood residual fraction 0.001、median confidence 0.838。
  - 443 cells は low confidence。QC / confidence UMAP 上で局在を確認する。
  - 323 cells は `Doublet` として提出。mixed-lineage marker expression と scrublet support を確認する。
  - 120 cells は `Blood Cell` として残存。これは filter-out ではなく、曖昧な細胞を公式 parent label で残したもの。
  - Marker gene 欠損アラート: Treg, B_memory_ABC, Plasma_ASC。該当 marker set に依存する fine label は慎重に見る。

## データセット固有の評価

- 全体像: 139,960 cells / original processed 19,141 genes / pre-HVG 8,000 genes / analysis X/var 3,985 genes。最大 dataset で、parent/Blood residual は 120 cells (0.001) と非常に低いです。median confidence は 0.838 で良好ですが、source disagreement は 29,879 cells (0.213) と無視できません。
- 信頼しやすい領域: NK Cell、Plasma Cell、pDC、Platelet、Non-Classical Monocyte は source agreement が高く、UMAP/dotplot での確認優先度は低めです。Naive B Cell と Memory B Cell も vaccination_study_06 より安定しています。
- T cell 側の弱点: CD8 Naive/Tcm は disagreement 0.591、Treg は 0.564 で目立ちます。Treg は FOXP3/IL2RA/CTLA4 欠損のため、Treg 1,823 cells は provisional fine label として読む必要があります。
- Marker gene 欠損: B_memory_ABC と Plasma_ASC も warning ですが、B-cell labels の source disagreement は中等度以下です。したがって、この dataset の主な review point は B cell より T-cell fine-state assignment です。
- 解釈: 大規模 dataset として broad lineage と多くの mature PBMC label は安定しています。提出前の重点確認は CD8 Naive/Tcm、Treg、MAIT の境界と、source-disagreement UMAP が QC artifact 由来か biological continuum 由来かの切り分けです。

## Marker Gene 欠損アラート

| study | marker_set | alert | present_fraction | missing_critical_markers | missing_genes |
| --- | --- | --- | --- | --- | --- |
| vaccination_study_09 | Treg | critical | 0.286 | FOXP3;IL2RA;CTLA4 | FOXP3;IL2RA;CTLA4;IKZF2;CCR8 |
| vaccination_study_09 | B_memory_ABC | warning | 0.500 | TNFRSF13B;ITGAX | TNFRSF13B;ITGAX;AIM2;CD86 |
| vaccination_study_09 | Plasma_ASC | warning | 0.333 | JCHAIN | JCHAIN;SDC1;IRF4;TNFRSF17;IGHG1;IGHA1 |

## ソース間不一致

| study | predicted_cell_type | cells | median_source_agreement | disagreement_cells | disagreement_fraction |
| --- | --- | --- | --- | --- | --- |
| vaccination_study_09 | Doublet | 323 | 0.000 | 323 | 1.000 |
| vaccination_study_09 | Blood Cell | 120 | 0.000 | 120 | 1.000 |
| vaccination_study_09 | CD8 Naive / T Central Memory | 10,260 | 0.400 | 6,064 | 0.591 |
| vaccination_study_09 | Treg | 1,823 | 0.400 | 1,029 | 0.564 |
| vaccination_study_09 | Conventional DC 2 | 1,970 | 0.750 | 715 | 0.363 |
| vaccination_study_09 | MAIT Cell | 5,716 | 0.500 | 1,843 | 0.322 |
| vaccination_study_09 | CD4 Naive / T Central Memory | 50,418 | 0.800 | 10,159 | 0.201 |
| vaccination_study_09 | CD8 Cytotoxic / T Effector Memory | 13,146 | 0.750 | 2,375 | 0.181 |
| vaccination_study_09 | Classical Monocyte | 26,842 | 0.750 | 4,474 | 0.167 |
| vaccination_study_09 | Naive B Cell | 12,156 | 0.800 | 1,955 | 0.161 |
| vaccination_study_09 | Memory B Cell | 3,374 | 0.600 | 496 | 0.147 |
| vaccination_study_09 | Non-Classical Monocyte | 3,473 | 1.000 | 175 | 0.050 |

## レビュー優先事項

| study | concern | cells |
| --- | --- | --- |
| vaccination_study_09 | High source disagreement for Blood Cell | 120 |
| vaccination_study_09 | High source disagreement for CD8 Naive / T Central Memory | 6,064 |
| vaccination_study_09 | High source disagreement for Doublet | 323 |
| vaccination_study_09 | High source disagreement for Treg | 1,029 |
| vaccination_study_09 | High dataset-level source disagreement | 29,879 |
| vaccination_study_09 | critical marker availability for Treg | 1,823 |
| vaccination_study_09 | warning marker availability for B_memory_ABC | 3,374 |
| vaccination_study_09 | warning marker availability for Plasma_ASC | 161 |

## ラベル構成

| study | predicted_cell_type | cells |
| --- | --- | --- |
| vaccination_study_09 | CD4 Naive / T Central Memory | 50,418 |
| vaccination_study_09 | Classical Monocyte | 26,842 |
| vaccination_study_09 | CD8 Cytotoxic / T Effector Memory | 13,146 |
| vaccination_study_09 | Naive B Cell | 12,156 |
| vaccination_study_09 | CD8 Naive / T Central Memory | 10,260 |
| vaccination_study_09 | NK Cell | 9,268 |
| vaccination_study_09 | MAIT Cell | 5,716 |
| vaccination_study_09 | Non-Classical Monocyte | 3,473 |
| vaccination_study_09 | Memory B Cell | 3,374 |
| vaccination_study_09 | Conventional DC 2 | 1,970 |
| vaccination_study_09 | Treg | 1,823 |
| vaccination_study_09 | Plasmacytoid DC | 806 |
| vaccination_study_09 | Doublet | 323 |
| vaccination_study_09 | Plasma Cell | 161 |
| vaccination_study_09 | Blood Cell | 120 |
| vaccination_study_09 | Platelet | 90 |
| vaccination_study_09 | HSC | 14 |

## 図

### vaccination_study_09

![vaccination_study_09 final labels](assets/umap_vaccination_study_09_annotation_label.png)

![vaccination_study_09 lineage and annotation reason](assets/umap_vaccination_study_09_annotation_lineage_reason.png)

![vaccination_study_09 QC and confidence](assets/umap_vaccination_study_09_annotation_qc_confidence.png)

![vaccination_study_09 source agreement and disagreement](assets/umap_vaccination_study_09_annotation_source_disagreement.png)

![vaccination_study_09 marker expression UMAPs](assets/umap_vaccination_study_09_annotation_marker_expression.png)

![vaccination_study_09 submitted-label marker dotplot](assets/dotplot_vaccination_study_09_annotation_marker_dotplot.png)

#### vaccination_study_09 B_lineage subcluster UMAP

![vaccination_study_09 B_lineage subcluster labels](assets/umap_vaccination_study_09_B_lineage_subcluster_label.png)

![vaccination_study_09 B_lineage subcluster QC](assets/umap_vaccination_study_09_B_lineage_subcluster_qc.png)

#### vaccination_study_09 T_NK_lineage subcluster UMAP

![vaccination_study_09 T_NK_lineage subcluster labels](assets/umap_vaccination_study_09_T_NK_lineage_subcluster_label.png)

![vaccination_study_09 T_NK_lineage subcluster QC](assets/umap_vaccination_study_09_T_NK_lineage_subcluster_qc.png)

#### vaccination_study_09 Myeloid_lineage subcluster UMAP

![vaccination_study_09 Myeloid_lineage subcluster labels](assets/umap_vaccination_study_09_Myeloid_lineage_subcluster_label.png)

![vaccination_study_09 Myeloid_lineage subcluster QC](assets/umap_vaccination_study_09_Myeloid_lineage_subcluster_qc.png)


## 出力ファイル

- Submission TSVs: `outputs/single_dataset_checks/260526_vaccination_study_09_assessment_all/submissions/`
- cellxgene H5ADs: `outputs/single_dataset_checks/260526_vaccination_study_09_assessment_all/cellxgene/`
- Marker availability table: `outputs/single_dataset_checks/260526_vaccination_study_09_assessment_all/tables/marker_gene_availability.tsv`
- Marker availability alerts: `outputs/single_dataset_checks/260526_vaccination_study_09_assessment_all/tables/marker_gene_availability_alerts.tsv`
- Subcluster evidence: `outputs/single_dataset_checks/260526_vaccination_study_09_assessment_all/tables/lineage_subcluster_evidence.tsv.gz`
- Source disagreement summary: `outputs/single_dataset_checks/260526_vaccination_study_09_assessment_all/tables/source_disagreement_summary.tsv`
- Diagnostics tables: `outputs/single_dataset_checks/260526_vaccination_study_09_assessment_all/tables/`
