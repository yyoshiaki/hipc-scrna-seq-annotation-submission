---
name: hipc-annotation-v12
description: Use when running, reviewing, designing, or packaging the HIPC scRNA-seq Annotation Benchmark v12 independent annotation workflow. This skill defines the single-dataset annotation interface, evidence hierarchy, hard-code guardrails, reporting contract, and execution/validation wrapper around the v12 CLI.
metadata:
  short-description: HIPC v12 one-dataset annotation and validation
---

# HIPC Annotation v12

## Purpose

Use this skill for HIPC scRNA-seq Annotation Benchmark work when the task involves annotation strategy, running v12, validating outputs, making reports, or preparing a clean submission implementation.

The primary interface is one dataset in, one annotated dataset out:

```bash
skills/hipc-annotation-v12/scripts/run_one.sh   --study-id STUDY   --input-h5ad /path/to/STUDY.h5ad   --out outputs/STUDY   --report-languages en,ja
```

Do not introduce a batch CLI unless explicitly requested. For multiple datasets, repeat `run_one.sh` per dataset.

## Core Concept

The goal is not just to run reference mapping. The goal is to encode a high-quality manual annotation workflow:

- assign broad lineage from independent evidence, not from prior submission labels
- recluster within broad lineages to expose B, T/NK, and myeloid structure
- adjudicate fine labels from marker support, cluster coherence, independent references, QC, and ontology constraints
- keep doublet and low-quality states explicit rather than silently filtering cells
- report enough UMAPs, dotplots, disagreement summaries, and validation tables for a human reviewer to audit the logic

For detailed decision rules, read `references/annotation_decision_contract.md` when modifying logic, reviewing label choices, or designing a new version.

## Required Environment

Run from the repository root unless the user gives another checkout:

```bash
cd /vast/palmer/pi/hafler/yy693/hipc-scrna-seq-annotation-submission
```

Use the single-cell environment:

```bash
/gpfs/gibbs/project/hafler/yy693/conda_envs/scanpy1.10.2/bin/python
```

## Standard Single-Dataset Run

```bash
skills/hipc-annotation-v12/scripts/run_one.sh   --study-id infection_study_04   --input-h5ad /path/to/infection_study_04.h5ad   --out outputs/single_dataset/infection_study_04   --report-languages en,ja
```

Validation-only check on existing outputs:

```bash
skills/hipc-annotation-v12/scripts/run_one.sh   --study-id infection_study_04   --out outputs/single_dataset/infection_study_04   --validate-only
```

## Input Contract

Required:

- one processed H5AD evidence container
- official ontology TSV from config
- v12 config
- study ID and output directory

Expected evidence when available:

- CellTypist labels
- Pan-human Azimuth labels
- cluster consensus and top-marker labels
- marker scores or marker genes
- QC and doublet fields
- lineage-scoped scRefMapping evidence

## Output Contract

For one dataset, the output root should include:

- `submissions/<study_id>_annotation.tsv`
- `cellxgene/<study_id>.final_v12_recursive_screfmapping.cxg.h5ad`
- `reports/report_en.md` and optional `reports/report_ja.md`
- `report_assets/*.png`
- diagnostics tables under `tables/`

## Independence Rules

- Do not use prior-version submission labels as the base label.
- Do not use prior-version parent lineage, subcluster, or confidence columns as starting points.
- Use CellTypist, Pan-human Azimuth, Azimuth when present, cluster consensus, top-marker labels, raw reference labels, marker scores, QC, doublet flags, and lineage-scoped scRefMapping evidence.
- scRefMapping is auxiliary and lineage-scoped only. It must not override weak marker availability without independent support.
- Avoid study-specific hard-coding. If a rule cannot be explained as a general marker/reference/QC/ontology principle, keep it out of the pipeline and document it as a review concern instead.

## Required Validation

A run is not complete unless validation reports all of the following:

- submission row counts match cellxgene H5AD `n_obs`
- `predicted_cell_type` has no missing values
- predicted labels are in the official ontology after configured exclusions
- submission TSV labels match `submission_cell_type_v12_recursive_screfmapping` in H5AD obs
- H5AD includes `confidence_score_v12_recursive_screfmapping`
- report inline image links resolve

## Rich Report Contract

A useful report should include:

- workflow Mermaid diagram
- per-study summary table with parent-label fraction, invalid labels, doublet counts, low-confidence counts, and median confidence
- UMAPs for final labels, lineage/reason, QC/confidence, and lineage-specific subclusters
- marker dotplots for submitted labels
- marker availability alerts, especially for scRefMapping-sensitive labels
- evidence-source disagreement summaries by lineage or cell type
- explicit review concerns rather than hidden hard-coded fixes

## Completion Criteria

Before reporting completion to the user, state:

- exact `run_one.sh` command used
- output root
- validation pass/fail summary
- report paths
- whether the clean submission repo was updated
