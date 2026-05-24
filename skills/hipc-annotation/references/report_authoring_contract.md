# HIPC Report Authoring Contract

Updated: 2026-05-23 EDT

## Purpose

The deterministic CLI writes the evidence tables and figures. Codex must then read the generated report and add or revise the dataset-specific assessment so it is useful to a human reviewer.

## Required review pass after generation

1. Confirm validation passed and report image links resolve.
2. Read the dataset summary: cells, genes, labels, parent/Blood residuals, doublets, low-confidence cells, and source-disagreement cells.
3. Read marker gene availability alerts before trusting fine labels that depend on those marker sets.
4. Inspect final-label, QC/confidence, source-disagreement, marker-expression, dotplot, and lineage subcluster figures.
5. Check whether parent labels are isolated ambiguous clusters or spread across several lineages.
6. Check whether source disagreement overlaps with low gene count, high mitochondrial fraction, or mixed-lineage regions.
7. Update the `Dataset-Specific Assessment` section with concrete observations from this dataset, not generic pipeline text.

## What to write

- State what looks reliable and why.
- State what is weak and why.
- Name the labels or lineages affected by marker gene missingness.
- Name whether source disagreement is widespread or concentrated in specific labels.
- Avoid study-specific hard-coded fixes. Suggest general logic improvements only when they follow marker, reference, QC, doublet, or ontology principles.

## Minimum assessment structure

- Overall data quality and gene-count context.
- Marker gene availability and confidence-cap implications.
- Source disagreement interpretation.
- Parent-label residual and doublet interpretation.
- Suggested next checks before submission.
