---
name: hipc-annotation-v12
description: Use when running, reviewing, designing, or packaging the HIPC scRNA-seq Annotation Benchmark v12 independent annotation workflow. This skill defines the annotation philosophy, evidence hierarchy, hard-code guardrails, reporting contract, and execution/validation wrapper around the v12 CLI.
metadata:
  short-description: HIPC v12 annotation concept, run, and validation
---

# HIPC Annotation v12

## Purpose

Use this skill for HIPC scRNA-seq Annotation Benchmark work when the task involves annotation strategy, running v12, validating outputs, making reports, or preparing a clean submission implementation.

The CLI is the deterministic engine:

```bash
scripts/pipeline/hipc_annotate_v12.py
```

The skill is the concept and operating contract around that engine. It should prevent ad hoc relabeling and preserve the manual-annotation logic we want to generalize.

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
cd /vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation
```

Use the single-cell environment:

```bash
/gpfs/gibbs/project/hafler/yy693/conda_envs/scanpy1.10.2/bin/python
```

## Standard Run

Use the wrapper unless custom paths are required:

```bash
skills/hipc-annotation-v12/scripts/run_v12.sh
```

For custom output:

```bash
HIPC_V12_OUT=outputs/final_annotations/YYMMDD_v12_independent_cli REPORT_LANGUAGES=en,ja skills/hipc-annotation-v12/scripts/run_v12.sh
```

Validation-only execution check on existing outputs:

```bash
HIPC_V12_VALIDATE_ONLY=1 HIPC_V12_OUT=outputs/final_annotations/260522_v12_independent_cli skills/hipc-annotation-v12/scripts/run_v12.sh
```

## Independence Rules

- Do not use prior-version submission labels as the base label.
- Do not use prior-version parent lineage, subcluster, or confidence columns as starting points.
- Use CellTypist, Pan-human Azimuth, Azimuth when present, cluster consensus, top-marker labels, raw reference labels, marker scores, QC, doublet flags, and lineage-scoped scRefMapping evidence.
- scRefMapping is auxiliary and lineage-scoped only. It must not override weak marker availability without independent support.
- Avoid study-specific hard-coding. If a rule cannot be explained as a general marker/reference/QC/ontology principle, keep it out of the pipeline and document it as a review concern instead.

## Required Validation

After every real run, execute:

```bash
skills/hipc-annotation-v12/scripts/validate_v12_outputs.py --out "$HIPC_V12_OUT"
```

A run is not complete unless validation reports all of the following:

- submission row counts match cellxgene H5AD `n_obs` for every study
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

- exact CLI command or wrapper used
- output root
- studies processed
- validation pass/fail summary
- whether outputs were published to cellxgene, if requested
- whether the clean submission repo was updated, if requested
