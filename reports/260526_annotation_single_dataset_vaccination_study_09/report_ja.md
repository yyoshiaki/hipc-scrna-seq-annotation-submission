# HIPC v13 dataset review: `vaccination_study_09`

Updated: 2026-05-26 EDT

## Summary

この report は `vaccination_study_09` について、portal input から独立に作成した v13 annotation review です。reference mapping、marker score、lineage-specific subclustering、doublet/QC evidence を統合し、全細胞に official ontology label と confidence score を付与しました。

## Dataset Assessment

最大 dataset で 139,960 cells、T cell と B cell が多いです。T marker は揃っていますが、B naive/plasma で IGHD/IGHM/JCHAIN 欠損があるため、B subtype と plasma/ASC は caution です。screfmap は B/CD4T の fine annotation に大きく寄与しています。

## Gene Space and Marker Alerts

| cells | portal genes | raw source | count-like | critical marker missing |
| ---: | ---: | --- | ---: | --- |
| 139,960 | 19,141 | layers[counts] | 1.000 | IGHD;IGHM;JCHAIN |

| marker set | present / expected | alert | missing critical markers |
| --- | ---: | --- | --- |
| Plasma_ASC | 6/9 | warning | JCHAIN |

## Annotation Summary

| cells | labels | parent/Blood fraction | Blood Cell | Doublet | artifact-like | median confidence | low confidence | invalid labels |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 139,960 | 17 | 0.005 | 695 | 579 | 144 | 0.822 | 1,286 | none |

## Source Agreement

| mean source agreement | screfmap-covered cells | interpretation |
| ---: | ---: | --- |
| 0.574 | 56,028 | screfmap は broad lineage ではなく、B/CD4T lineage 内の補助 evidence として使っています。 |

## Figures

![vaccination_study_09 v13 labels](assets/umap_vaccination_study_09_v13_label.png)

![vaccination_study_09 v13 lineage and reason](assets/umap_vaccination_study_09_v13_lineage_reason.png)

![vaccination_study_09 v13 QC and confidence](assets/umap_vaccination_study_09_v13_qc_confidence.png)

![vaccination_study_09 v13 marker dotplot](assets/dotplot_vaccination_study_09_v13_marker_dotplot.png)

![vaccination_study_09 B lineage subcluster labels](assets/umap_vaccination_study_09_B_lineage_v13_subcluster_label.png)

![vaccination_study_09 B lineage subcluster QC](assets/umap_vaccination_study_09_B_lineage_v13_subcluster_qc.png)

![vaccination_study_09 T/NK lineage subcluster labels](assets/umap_vaccination_study_09_T_NK_lineage_v13_subcluster_label.png)

![vaccination_study_09 T/NK lineage subcluster QC](assets/umap_vaccination_study_09_T_NK_lineage_v13_subcluster_qc.png)

![vaccination_study_09 Myeloid lineage subcluster labels](assets/umap_vaccination_study_09_Myeloid_lineage_v13_subcluster_label.png)

![vaccination_study_09 Myeloid lineage subcluster QC](assets/umap_vaccination_study_09_Myeloid_lineage_v13_subcluster_qc.png)

## Output Location

Large submission TSVs, annotated H5ADs, and diagnostics tables are stored on the Yale server working path:

`/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/final_annotations/260526_v13_input_contract_repair/`
