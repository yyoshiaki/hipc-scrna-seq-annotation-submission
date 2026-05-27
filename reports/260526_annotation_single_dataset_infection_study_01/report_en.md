# HIPC v13 dataset review: `infection_study_01`

Updated: 2026-05-26 EDT

## Summary

This report is an independent v13 annotation review for `infection_study_01`. It integrates reference mapping, marker scores, lineage-specific subclustering, and doublet/QC evidence, then assigns every cell an official ontology label and confidence score.

## Dataset Assessment

The full portal gene space contains 33,538 genes with no critical marker loss. Major B/T/myeloid lineages are stable by subcluster and marker evidence, and the parent/Blood fraction is low at 0.30%. screfmap is used as auxiliary B/CD4T support.

## Gene Space and Marker Alerts

| cells | portal genes | raw source | count-like | critical marker missing |
| ---: | ---: | --- | ---: | --- |
| 54,924 | 33,538 | layers[counts] | 1.000 | none |

| marker set | present / expected | alert | missing critical markers |
| --- | ---: | --- | --- |
| none | - | - | - |

## Annotation Summary

| cells | labels | parent/Blood fraction | Blood Cell | Doublet | artifact-like | median confidence | low confidence | invalid labels |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 54,924 | 19 | 0.003 | 166 | 1,278 | 1,389 | 0.846 | 2,209 | none |

## Source Agreement

| mean source agreement | screfmap-covered cells | interpretation |
| ---: | ---: | --- |
| 0.692 | 12,523 | screfmap is used as lineage-scoped auxiliary evidence inside B/CD4T lineages, not for broad-lineage assignment. |

## Figures

![infection_study_01 v13 labels](assets/umap_infection_study_01_v13_label.png)

![infection_study_01 v13 lineage and reason](assets/umap_infection_study_01_v13_lineage_reason.png)

![infection_study_01 v13 QC and confidence](assets/umap_infection_study_01_v13_qc_confidence.png)

![infection_study_01 v13 marker dotplot](assets/dotplot_infection_study_01_v13_marker_dotplot.png)

![infection_study_01 B lineage subcluster labels](assets/umap_infection_study_01_B_lineage_v13_subcluster_label.png)

![infection_study_01 B lineage subcluster QC](assets/umap_infection_study_01_B_lineage_v13_subcluster_qc.png)

![infection_study_01 T/NK lineage subcluster labels](assets/umap_infection_study_01_T_NK_lineage_v13_subcluster_label.png)

![infection_study_01 T/NK lineage subcluster QC](assets/umap_infection_study_01_T_NK_lineage_v13_subcluster_qc.png)

![infection_study_01 Myeloid lineage subcluster labels](assets/umap_infection_study_01_Myeloid_lineage_v13_subcluster_label.png)

![infection_study_01 Myeloid lineage subcluster QC](assets/umap_infection_study_01_Myeloid_lineage_v13_subcluster_qc.png)

## Output Location

Large submission TSVs, annotated H5ADs, and diagnostics tables are stored on the Yale server working path:

`/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/final_annotations/260526_v13_input_contract_repair/`
