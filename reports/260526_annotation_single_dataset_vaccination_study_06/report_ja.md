# HIPC v13 dataset review: `vaccination_study_06`

Updated: 2026-05-26 EDT

## Summary

この report は `vaccination_study_06` について、portal input から独立に作成した v13 annotation review です。reference mapping、marker score、lineage-specific subclustering、doublet/QC evidence を統合し、全細胞に official ontology label と confidence score を付与しました。

## Dataset Assessment

Full portal gene space は 11,878 genes と最も小さく、Treg/Plasma/B-memory/myeloid marker 欠損が目立ちます。screfmap は CD4T/B lineage では有用ですが、marker availability warning により単独 rescue は抑制しています。doublet は 1,502 cells で最も多く、品質警告として残すべきです。

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
| 0.605 | 32,384 | screfmap は broad lineage ではなく、B/CD4T lineage 内の補助 evidence として使っています。 |

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
