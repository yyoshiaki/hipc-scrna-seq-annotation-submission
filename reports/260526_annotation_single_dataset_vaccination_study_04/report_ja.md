# HIPC v13 dataset review: `vaccination_study_04`

Updated: 2026-05-26 EDT

## Summary

この report は `vaccination_study_04` について、portal input から独立に作成した v13 annotation review です。reference mapping、marker score、lineage-specific subclustering、doublet/QC evidence を統合し、全細胞に official ontology label と confidence score を付与しました。

## Dataset Assessment

データは myeloid/DC enriched に見え、B/CD4T query は少数です。Treg marker は FOXP3/IL2RA 欠損により critical alert なので、Treg fine label は強く信用しない設定です。主な signal は Classical/Non-Classical Monocyte、cDC2、pDC、cDC1 で、whole PBMC として扱うより enriched dataset として読むべきです。

## Gene Space and Marker Alerts

| cells | portal genes | raw source | count-like | critical marker missing |
| ---: | ---: | --- | ---: | --- |
| 66,065 | 16,983 | layers[counts] | 1.000 | CD3D;CD8A;CD8B;PRF1;MS4A1;CD27;TNFRSF13B;TBX21;SDC1;FOXP3;IL2RA;XCR1 |

| marker set | present / expected | alert | missing critical markers |
| --- | ---: | --- | --- |
| Treg | 2/7 | critical | FOXP3;IL2RA |

## Annotation Summary

| cells | labels | parent/Blood fraction | Blood Cell | Doublet | artifact-like | median confidence | low confidence | invalid labels |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 66,065 | 12 | 0.007 | 464 | 647 | 408 | 0.846 | 1,111 | none |

## Source Agreement

| mean source agreement | screfmap-covered cells | interpretation |
| ---: | ---: | --- |
| 0.724 | 170 | screfmap は broad lineage ではなく、B/CD4T lineage 内の補助 evidence として使っています。 |

## Figures

![vaccination_study_04 v13 labels](assets/umap_vaccination_study_04_v13_label.png)

![vaccination_study_04 v13 lineage and reason](assets/umap_vaccination_study_04_v13_lineage_reason.png)

![vaccination_study_04 v13 QC and confidence](assets/umap_vaccination_study_04_v13_qc_confidence.png)

![vaccination_study_04 v13 marker dotplot](assets/dotplot_vaccination_study_04_v13_marker_dotplot.png)

![vaccination_study_04 B lineage subcluster labels](assets/umap_vaccination_study_04_B_lineage_v13_subcluster_label.png)

![vaccination_study_04 B lineage subcluster QC](assets/umap_vaccination_study_04_B_lineage_v13_subcluster_qc.png)

![vaccination_study_04 T/NK lineage subcluster labels](assets/umap_vaccination_study_04_T_NK_lineage_v13_subcluster_label.png)

![vaccination_study_04 T/NK lineage subcluster QC](assets/umap_vaccination_study_04_T_NK_lineage_v13_subcluster_qc.png)

![vaccination_study_04 Myeloid lineage subcluster labels](assets/umap_vaccination_study_04_Myeloid_lineage_v13_subcluster_label.png)

![vaccination_study_04 Myeloid lineage subcluster QC](assets/umap_vaccination_study_04_Myeloid_lineage_v13_subcluster_qc.png)

## Output Location

Large submission TSVs, annotated H5ADs, and diagnostics tables are stored on the Yale server working path:

`/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/final_annotations/260526_v13_input_contract_repair/`
