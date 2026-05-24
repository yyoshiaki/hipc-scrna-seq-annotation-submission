# HIPC beta final annotation v12 fully independent calibrated-resolution report

Updated: 2026-05-23 EDT

## Summary

`v12_recursive_screfmapping` は、前バージョンの submission label、parent lineage、subcluster、confidence を使わずに、broad lineage、lineage-specific subcluster、final label、confidence を作り直す独立 annotation pass です。入力 evidence は CellTypist、Pan-human Azimuth、cluster consensus、top-marker label、raw reference label、marker score、QC、doublet flag です。

## Main Logic

- Broad lineage は CellTypist、Pan-human Azimuth、cluster consensus、top marker lineage、raw reference label、marker score から独立に投票して決める。
- B、T/NK、myeloid lineage は別々に再クラスタリングする。親ラベルだけを取り出して救済する処理ではない。
- Final label は lineage subcluster ごとの marker/reference consensus から決める。
- 各 study について B、T/NK、myeloid の subcluster UMAP を出力する。
- Doublet は override label とし、低 QC または mixed-marker cell は confidence を cap する。

## Workflow

```mermaid
flowchart TD
    A[Input H5AD evidence container] --> B[Per-cell evidence extraction]
    B --> B1[CellTypist labels]
    B --> B2[Pan-human Azimuth labels]
    B --> B3[Cluster consensus and top-marker labels]
    B --> B4[Raw reference labels]
    B --> B5[Marker gene scores and QC metrics]
    B1 --> C[Broad lineage vote per cell]
    B2 --> C
    B3 --> C
    B4 --> C
    B5 --> C
    C --> D{Broad lineage}
    D --> E[B lineage subset]
    D --> F[T/NK lineage subset]
    D --> G[Myeloid lineage subset]
    D --> H[Other or ambiguous cells]
    E --> I[Lineage-specific HVG, PCA, Leiden, UMAP]
    F --> I
    G --> I
    I --> J[Subcluster evidence scoring]
    J --> J1[Reference fraction]
    J --> J2[Raw-label fraction]
    J --> J3[Marker percentile]
    J --> J4[Best-vs-second score margin]
    J1 --> K[Final ontology label]
    J2 --> K
    J3 --> K
    J4 --> L[Calibrated confidence]
    H --> M[Ambiguous fallback or direct artifact call]
    K --> N[Doublet override and QC/mixed-marker confidence cap]
    L --> N
    M --> N
    N --> O[Submission TSV, cellxgene H5AD, diagnostics, report figures]
```

## Study Summary

| study | cells | v12 labels | parent/Blood fraction | B Cell | T Cell | Myeloid Cell | Blood Cell | artifact-like | Doublet | Effector B | median confidence | low confidence | invalid labels |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| infection_study_04 | 43,767 | 16 | 0.012 | 0 | 0 | 0 | 529 | 353 | 61 | 0 | 0.838 | 751 | none |

## Figures

![v12 parent or Blood Cell fraction](../report_assets/figure_01_v12_parent_or_blood_fraction.png)

### infection_study_04

![infection_study_04 v12 labels](../report_assets/umap_infection_study_04_v12_label.png)

![infection_study_04 v12 lineage and reason](../report_assets/umap_infection_study_04_v12_lineage_reason.png)

![infection_study_04 v12 QC and confidence](../report_assets/umap_infection_study_04_v12_qc_confidence.png)

![infection_study_04 v12 marker dotplot](../report_assets/dotplot_infection_study_04_v12_marker_dotplot.png)

#### infection_study_04 B_lineage subcluster UMAP

![infection_study_04 B_lineage subcluster labels](../report_assets/umap_infection_study_04_B_lineage_v12_subcluster_label.png)

![infection_study_04 B_lineage subcluster QC](../report_assets/umap_infection_study_04_B_lineage_v12_subcluster_qc.png)

#### infection_study_04 T_NK_lineage subcluster UMAP

![infection_study_04 T_NK_lineage subcluster labels](../report_assets/umap_infection_study_04_T_NK_lineage_v12_subcluster_label.png)

![infection_study_04 T_NK_lineage subcluster QC](../report_assets/umap_infection_study_04_T_NK_lineage_v12_subcluster_qc.png)

#### infection_study_04 Myeloid_lineage subcluster UMAP

![infection_study_04 Myeloid_lineage subcluster labels](../report_assets/umap_infection_study_04_Myeloid_lineage_v12_subcluster_label.png)

![infection_study_04 Myeloid_lineage subcluster QC](../report_assets/umap_infection_study_04_Myeloid_lineage_v12_subcluster_qc.png)

## Files

- Submission TSVs: `outputs/single_dataset_checks/260523_infection_study_04_current/submissions/`
- cellxgene H5ADs: `outputs/single_dataset_checks/260523_infection_study_04_current/cellxgene/`
- Subcluster evidence: `outputs/single_dataset_checks/260523_infection_study_04_current/tables/v12_lineage_subcluster_evidence.tsv.gz`
- Diagnostics tables: `outputs/single_dataset_checks/260523_infection_study_04_current/tables/`
