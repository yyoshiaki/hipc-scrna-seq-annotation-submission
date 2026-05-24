# HIPC Annotation Decision Contract

Updated: 2026-05-23 EDT

## Why a skill adds value beyond a CLI

The CLI guarantees reproducible execution. The skill preserves the reasoning contract: what evidence is allowed, how evidence conflicts are resolved, what must be reported, and what should be treated as a review concern rather than silently hard-coded into the implementation.

## Evidence hierarchy

1. Marker support and marker availability define whether a fine label is biologically credible.
2. Subcluster coherence defines whether a label is stable on local manifold structure.
3. Independent reference agreement from CellTypist, Pan-human Azimuth, Azimuth, and scRefMapping adds support but should not override absent markers.
4. QC and doublet evidence can cap confidence or override the cell type to `Doublet`.
5. Ontology constraints define the allowed submitted label space.

## Manual annotation loop to encode

1. Build broad lineage without prior-version labels.
2. Recluster B, T/NK, and myeloid lineages separately.
3. Score candidate official labels within each lineage using marker percentiles, reference fractions, raw-label fractions, and best-vs-second margins.
4. Assign a fine label only when the subcluster has coherent evidence.
5. Fall back to a stable parent label when evidence is weak, not to a study-specific workaround.
6. Emit concerns and figures for ambiguous regions.

## Doublet handling

Doublet calls are not filtering. They are submitted labels when supported by Scrublet or strong incompatible marker mixtures, especially T/B, T/Mono, or B/Mono mixtures. Platelet/immune or erythroid/immune signals should usually be flagged unless paired with stronger doublet evidence.

## scRefMapping rules

scRefMapping is useful only inside an appropriate lineage. B references should only affect B-lineage adjudication; CD4T references should only affect CD4/T-lineage adjudication. If marker gene availability is poor, scRefMapping must become a weak auxiliary signal and the report must show an alert.

## Hard-code guardrails

Do not encode a rule because one study has an awkward cluster. A rule is acceptable only if it can be stated as a general principle using marker genes, ontology, reference agreement, QC, or doublet logic.

## Required report diagnostics

The report should let a reviewer answer these questions without rerunning the pipeline:

- Which cells remained parent labels and where are they on UMAP?
- Which labels depend on weak marker availability?
- Where do CellTypist, Pan-human Azimuth, Azimuth, scRefMapping, and marker evidence disagree?
- Which subclusters are low confidence or mixed-lineage?
- Are submitted labels all official and in barcode order?
