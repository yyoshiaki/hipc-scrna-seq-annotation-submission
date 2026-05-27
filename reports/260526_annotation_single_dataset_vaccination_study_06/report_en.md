# HIPC v13 dataset review: `vaccination_study_06`

Updated: 2026-05-26 EDT

## Summary

This report is an independent v13 annotation review for `vaccination_study_06`. It integrates reference mapping, marker scores, lineage-specific subclustering, and doublet/QC evidence, then assigns every cell an official ontology label and confidence score.

## Dataset Assessment

This is the smallest gene-space dataset at 11,878 portal genes and shows broad Treg/Plasma/B-memory/myeloid marker loss. screfmap is useful in B/CD4T lineages, but single-source rescue is suppressed under marker warnings. The doublet call count is highest here at 1,502 cells and should remain visible as a quality flag.

## Gene Space and Marker Alerts

| cells | portal genes | raw source | count-like | critical marker missing |
| ---: | ---: | --- | ---: | --- |
| 57,419 | 11,878 | layers[counts] | 1.000 | IGHD;TNFRSF13B;FCRL5;JCHAIN;SDC1;FOXP3;LYZ;S100A8;S100A9;MS4A7;CLEC4C;CD1C;FCER1A;CLEC9A;XCR1 |

| marker set | present / expected | alert | missing critical markers |
| --- | ---: | --- | --- |
| Treg | 5/7 | warning | FOXP3 |
| Plasma_ASC | 4/9 | warning | JCHAIN |

## Annotation Summary

| cells | labels | parent/Blood fraction | Blood Cell | Doublet | artifact-like | median confidence | low confidence | invalid labels |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 57,419 | 17 | 0.004 | 216 | 1,502 | 2 | 0.820 | 1,771 | none |

## Source Agreement

| mean source agreement | screfmap-covered cells | interpretation |
| ---: | ---: | --- |
| 0.605 | 32,384 | screfmap is used as lineage-scoped auxiliary evidence inside B/CD4T lineages, not for broad-lineage assignment. |

## Figures

![vaccination_study_06 v13 labels](assets/umap_vaccination_study_06_v13_label.png)

![vaccination_study_06 v13 lineage and reason](assets/umap_vaccination_study_06_v13_lineage_reason.png)

![vaccination_study_06 v13 QC and confidence](assets/umap_vaccination_study_06_v13_qc_confidence.png)

![vaccination_study_06 v13 marker dotplot](assets/dotplot_vaccination_study_06_v13_marker_dotplot.png)

![vaccination_study_06 B lineage subcluster labels](assets/umap_vaccination_study_06_B_lineage_v13_subcluster_label.png)

![vaccination_study_06 B lineage subcluster QC](assets/umap_vaccination_study_06_B_lineage_v13_subcluster_qc.png)

![vaccination_study_06 T/NK lineage subcluster labels](assets/umap_vaccination_study_06_T_NK_lineage_v13_subcluster_label.png)

![vaccination_study_06 T/NK lineage subcluster QC](assets/umap_vaccination_study_06_T_NK_lineage_v13_subcluster_qc.png)

![vaccination_study_06 Myeloid lineage subcluster labels](assets/umap_vaccination_study_06_Myeloid_lineage_v13_subcluster_label.png)

![vaccination_study_06 Myeloid lineage subcluster QC](assets/umap_vaccination_study_06_Myeloid_lineage_v13_subcluster_qc.png)

## Output Location

Large submission TSVs, annotated H5ADs, and diagnostics tables are stored on the Yale server working path:

`/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/final_annotations/260526_v13_input_contract_repair/`
