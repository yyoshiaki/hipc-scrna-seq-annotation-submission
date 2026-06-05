---
name: hipc-annotation
description: Use when Codex must annotate, validate, review, or package one HIPC scRNA-seq Annotation Benchmark dataset using the independent annotation workflow. This skill tells Codex how to inspect the input, apply the evidence hierarchy, run the deterministic helper scripts, validate outputs, and report review concerns without relying on prior-version labels or ad hoc hard-coding.
metadata:
  short-description: Codex workflow for one HIPC dataset
---

# HIPC Annotation

## What This Skill Is

This is a Codex operating procedure for one HIPC dataset. The skill is not the shell script. The shell scripts are bundled deterministic helpers that Codex may run to avoid rewriting fragile pipeline commands.

When this skill triggers, Codex should own the workflow end-to-end: inspect inputs, choose an output root, run the helper, validate outputs, inspect the report, and summarize concerns. Do not hand the command back to the user unless blocked.

The report templates are part of this skill at `templates/report_dataset_en.md` and `templates/report_dataset_ja.md`. The deterministic CLI fills evidence-backed tables and figure links; Codex remains responsible for inspecting whether the generated interpretation is adequate for the dataset and editing the report when a dataset needs a more tailored explanation.

## Core Workflow For Codex

1. Confirm the task is one dataset unless the user explicitly asks for multi-dataset orchestration.
2. Identify `study_id`, `input_h5ad`, and output root. Use a dated output root if none is given.
3. Inspect or infer whether the H5AD is an evidence container with reference labels, marker/QC fields, and doublet evidence.
4. If changing annotation logic, read `references/annotation_decision_contract.md` first.
5. Confirm `configs/marker_registry.yaml` exists and covers the official ontology labels needed for the dataset. If it is missing or inadequate, pause final annotation and build or revise the marker registry first.
6. Run `scripts/pipeline/hipc_audit_marker_registry.py` after marker registry edits. Do not proceed to final annotation if ontology coverage or schema validation fails.
7. Run the bundled helper `scripts/run_one.sh` from the repository root.
8. Let `run_one.sh` call the deterministic CLI and validator. Do not skip validation.
9. Inspect `tables/llm_subcluster_review_queue.tsv` and `tables/llm_subcluster_review_prompts.md` when present. Use them as a review layer, not as direct label-edit instructions.
10. Read `references/report_authoring_contract.md`, inspect the generated report, and revise the `Dataset-Specific Assessment` section when the automated assessment is too generic.
11. Inspect the generated report for obvious broken paths, stale metadata, missing UMAPs/dotplots, misleading file paths, or generic interpretation text.
12. Report completion only after validation passes, or report the exact failing validation item.

For multiple datasets, Codex should repeat this single-dataset workflow per dataset. Do not add a batch CLI unless explicitly requested.

## Helper Invocation Pattern

Codex may run the helper like this after resolving real paths:

```bash
skills/hipc-annotation/scripts/run_one.sh   --study-id STUDY   --input-h5ad /path/to/STUDY.h5ad   --out outputs/STUDY   --report-languages en,ja
```

For validating an existing single-dataset output, Codex may run:

```bash
skills/hipc-annotation/scripts/run_one.sh   --study-id STUDY   --out outputs/STUDY   --validate-only
```

These commands are not user instructions. They are reliable local tools for Codex to execute.

## Required Environment

Default repository root:

```text
/vast/palmer/pi/hafler/yy693/hipc-scrna-seq-annotation-submission
```

Default Python:

```text
/gpfs/gibbs/project/hafler/yy693/conda_envs/scanpy1.10.2/bin/python
```

## Input Contract

Required:

- one processed H5AD evidence container
- study ID
- output directory
- official ontology TSV from config
- annotation config

Expected evidence when available:

- CellTypist labels
- Pan-human Azimuth labels
- Azimuth labels when present
- cluster consensus and top-marker labels
- marker scores or marker genes
- QC and doublet fields
- lineage-scoped scRefMapping evidence

If evidence fields are missing, Codex should treat that as an input limitation, not silently invent labels.

## Marker Registry Contract

`configs/marker_registry.yaml` is the static marker-reference input for marker scoring. It should contain broad lineage, applicable lineage, positive markers, key markers, negative markers, confound markers, marker role, notes, and provenance for each candidate ontology label.

Codex should use this ask-first rule:

- If a suitable registry exists, audit ontology coverage and marker availability and use it as deterministic input.
- If the registry is missing, incomplete for the requested ontology labels, or inconsistent with the dataset context, create or revise the registry before final annotation unless the user explicitly says not to.
- Do not ask the LLM to choose per-cell labels at runtime. LLM-assisted marker curation must be frozen into the registry first.
- Marker evidence is applied after broad lineage assignment. Candidate labels compete only within the applicable lineage and must pass key-marker availability/support gates.
- Rare or artifact-like labels require stronger key-marker support and should not override normal lineage labels without QC or lineage-consistent evidence.
- If key marker availability is weak, cap confidence and surface a report alert rather than silently trusting reference mapping.

The intended generalized workflow is:

1. Convert the official ontology into a reviewed marker registry.
2. Add notes and conservative policies for labels that are expected to be hard to distinguish, such as plasma cell vs plasmablast, NKT vs NK/cytotoxic T, or gdT vs cytotoxic/MAIT-like T cells.
3. Freeze the registry and audit it.
4. Run deterministic annotation against one dataset.
5. Let Codex review the generated subcluster evidence queue and report, but not mutate labels by ad hoc per-dataset rules.
6. If the review finds a useful general improvement, encode it as a marker registry, source-support, QC, or ontology policy update, then rerun deterministic annotation.

Implementation guardrail:

- Biological marker genes should live in `configs/marker_registry.yaml`, not in `scripts/pipeline/hipc_annotate.py`.
- `configs/annotation_pipeline.json` may contain thresholds, paths, and report options, but should not be the source of truth for marker biology.

## Annotation Logic Contract

The goal is to encode a high-quality manual annotation workflow:

- assign broad lineage from independent evidence, not from prior submission labels
- recluster within broad lineages to expose B, T/NK, and myeloid structure
- adjudicate fine labels from marker support, cluster coherence, independent references, QC, and ontology constraints
- keep doublet and low-quality states explicit rather than silently filtering cells
- report enough UMAPs, dotplots, disagreement summaries, and validation tables for a human reviewer to audit the logic

## Independence Rules

- Do not use prior-version submission labels as the base label.
- Do not use prior-version parent lineage, subcluster, or confidence columns as starting points.
- Use CellTypist, Pan-human Azimuth, Azimuth when present, cluster consensus, top-marker labels, raw reference labels, marker scores, QC, and doublet flags for broad lineage assignment.
- scRefMapping is auxiliary and lineage-scoped only after broad lineage assignment. It must not vote in broad lineage assignment or override weak marker availability without independent support.
- If scRefMapping reference files are missing or internal-only, read `references/screfmapping_reference_distribution.md` and report that limitation instead of fabricating evidence.
- Avoid study-specific hard-coding. If a rule cannot be explained as a general marker/reference/QC/ontology principle, keep it out of the pipeline and document it as a review concern instead.

## Output Contract

For one dataset, the output root should include:

- `submissions/<study_id>_annotation.tsv`
- `cellxgene/<study_id>.final_annotation.cxg.h5ad`
- `report_en.md` and optional `report_ja.md`
- `assets/*.png`
- diagnostics tables under `tables/`

## Required Validation

A run is not complete unless validation confirms:

- submission row counts match cellxgene H5AD `n_obs`
- `predicted_cell_type` has no missing values
- predicted labels are in the official ontology after configured exclusions
- submission TSV labels match `submission_cell_type` in H5AD obs
- H5AD includes `confidence_score`
- report inline image links resolve

## Report Review Checklist

Before declaring success, Codex should inspect that the report includes:

- summary table with parent-label fraction, invalid labels, doublet counts, low-confidence counts, and median confidence
- dataset gene count and marker gene availability alerts
- dataset-specific assessment that has been read and, if needed, edited by Codex after generation
- source-disagreement table and UMAP
- UMAPs for final labels, lineage/reason, QC/confidence, and lineage-specific subclusters
- marker dotplots for submitted labels
- marker availability alerts or concerns when relevant
- explicit review concerns rather than hidden hard-coded fixes

## Completion Response

Codex should report:

- input H5AD and study ID
- output root
- validation result
- report paths
- notable warnings or review concerns
- commit/push status if repository files changed
