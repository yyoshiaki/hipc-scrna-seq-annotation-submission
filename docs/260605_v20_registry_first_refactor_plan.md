# v20 Registry-First Refactor Plan

Updated: 2026-06-05 EDT

## Current Assessment

The v19 annotation output is conservative and auditable, but the implementation is not yet cleanly generalized.

What works:

- final labels are validated against the official ontology
- lineage-scoped subclustering is generated for B, T/NK, and myeloid lineages
- raw marker winner, adjudicated marker assignment, and final label are stored separately
- difficult labels such as `Plasmablast`, `NKT Cell`, and `gdT Cell` can enter the candidate set without dataset-specific rescue code

What is still weak:

- marker gene definitions were partly duplicated between `configs/marker_registry.yaml`, `configs/annotation_pipeline.json`, and `scripts/pipeline/hipc_annotate.py`
- the skill describes an LLM-assisted marker registry step, but the actual runtime still behaves mostly as a deterministic CLI
- ontology-to-marker curation is not yet represented as a first-class workflow artifact
- report interpretation is generated from templates and needs stronger post-run Codex review for dataset-specific conclusions

## Target Architecture

The workflow should have two explicit steps.

### Step 1: Build Or Audit Marker Registry

Input:

- official ontology table
- expected tissue/context when known
- optional existing registry
- optional user-provided marker preferences

Output:

- frozen `configs/marker_registry.yaml`
- marker registry audit tables
- notes for labels expected to be difficult or ambiguous

Codex/LLM role:

- curate marker candidates from immunology knowledge and ontology structure
- flag labels that are hard to separate in gene-only scRNA-seq
- write ambiguity notes and conservative candidate policies
- ask for human review only when ontology labels are biologically unclear or marker support is intrinsically weak

The LLM must not choose per-cell labels during runtime annotation.

### Step 2: Deterministic Annotation

Input:

- one H5AD evidence container
- frozen marker registry
- annotation config

Output:

- submission TSV
- cellxgene H5AD
- dataset-specific report
- diagnostic tables and figures

Runtime role:

- assign broad lineage from reference labels and QC evidence
- recluster within lineage
- score registry candidates within applicable lineage
- apply key-marker gates, source support, doublet/QC logic, and conservative policies
- preserve raw marker winner, adjudicated marker assignment, final label, and reason

## Refactor Rules

- `configs/marker_registry.yaml` is the source of truth for marker genes.
- `configs/annotation_pipeline.json` may define global thresholds and runtime policy, but should not duplicate label marker genes.
- `scripts/pipeline/hipc_annotate.py` may define evidence weighting and lineage workflow, but should not define biological marker lists.
- Hard-coded label rescue is not allowed unless it can be expressed as a general marker, source-support, QC, or ontology policy.
- Report generation should include deterministic evidence first, then allow Codex to add dataset-specific interpretation after reading the generated report and tables.

## Immediate v20 Changes

- Build marker scores from `configs/marker_registry.yaml` instead of hard-coded marker gene lists in `hipc_annotate.py`.
- Prefer registry marker sets for marker availability, dotplots, and confidence alerts.
- Replace the old v14-specific marker audit script with a generic ontology/registry audit.
- Update the skill contract to make the registry-building step explicit.

## Remaining Work

- Remove or deprecate `configs/annotation_pipeline.json:marker_sets` after confirming report plots remain complete.
- Add a small registry-generation template for Codex-assisted marker curation.
- Add a regression test that fails if marker genes are reintroduced directly into `hipc_annotate.py`.
- Re-run at least one dataset and compare final labels, gdT/Plasmablast behavior, and report richness before full v20 execution.
