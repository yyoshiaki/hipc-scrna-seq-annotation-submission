# v15 cluster-consensus annotation summary

## Strategy

v15 was run as a clean cluster-consensus annotation. It does not use any previous final submitted label as the base annotation. Inputs were restricted to:

- full-gene portal H5AD
- neutral source-evidence containers
- generic marker registry
- official ontology

Cell-level marker winners are not directly converted into final labels. Instead, labels are adjudicated at Leiden/subcluster level using source support, marker scores, negative/confound markers, doublet calls, and QC. CD4 T Effector Memory did not pass whole-cluster rescue criteria, so only a limited subset with reference >=2, marker support, and non-dominant CD8/NK signal was rescued.

## Clean Execution Check

Default v15 inputs use neutral names:

```text
configs/manifest.tsv
configs/marker_registry.yaml
outputs/final_annotations/260602_current_evidence/evidence/*.evidence.h5ad
```

The v15 runner does not read previous final-label columns. The strings `v13`/`v14` appear only in validation checks that stop execution if versioned labels leak into output.

All v15 H5AD outputs passed:

- full-gene variable space retained
- `X_umap` present
- `submission_cell_type` matches the submission TSV
- no `v13`, `v14`, or `version` in obs column names or obs string values

## Summary

| study | cells | genes | labels | parent/Blood fraction | doublets | CD4 TEM |
|---|---:|---:|---:|---:|---:|---:|
| infection_study_01 | 54,924 | 33,538 | 22 | 8.8% | 1,278 | 1,159 |
| infection_study_04 | 43,767 | 26,361 | 23 | 8.0% | 132 | 53 |
| vaccination_study_04 | 66,065 | 16,983 | 17 | 2.0% | 647 | 0 |
| vaccination_study_06 | 57,419 | 11,878 | 19 | 13.8% | 1,502 | 445 |
| vaccination_study_09 | 139,960 | 19,141 | 20 | 7.1% | 579 | 865 |

## T Cell Interpretation

In `vaccination_study_09`, marker-only CD4 TEM was 7,667 cells, but v15 reports 865 cells. The marker-only value is inflated because the CD4 TEM marker program overlaps with CD8/MAIT/NK-like cytotoxic programs.

All v15 CD4 TEM calls in `vaccination_study_09` come from `limited_subset_reference_marker_support`. This means no large Leiden cluster was forced into CD4 TEM; only mixed-cluster cells with both reference and marker support were rescued.

## Outputs

```text
outputs/final_annotations/260602_v15_cluster_consensus/submissions/
outputs/final_annotations/260602_v15_cluster_consensus/cellxgene/
outputs/final_annotations/260602_v15_cluster_consensus/tables/
```

Key tables:

```text
outputs/final_annotations/260602_v15_cluster_consensus/tables/final_annotation_summary_cluster_consensus.tsv
outputs/final_annotations/260602_v15_cluster_consensus/tables/final_annotation_label_counts_cluster_consensus.tsv
outputs/final_annotations/260602_v15_cluster_consensus/tables/cluster_consensus_decisions.tsv
```

## Current Assessment

v15 is cleaner than the previous marker-gate output and suppresses marker-winner over-rescue in T cells. However, some parent/Blood Cell assignments increased, especially in `vaccination_study_06`. The next review target is whether Blood Cell fallback and T/NK parent fallback are biologically reasonable.
