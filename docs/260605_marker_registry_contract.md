# Marker Registry Contract

Updated: 2026-06-05 10:04:20 EDT

This document defines the first step of the HIPC annotation workflow: building a frozen marker registry from the official ontology before deterministic annotation.

## Purpose

The marker registry translates official ontology labels into evidence that can be scored reproducibly:

- broad lineage
- applicable lineage for local subclustering
- positive markers
- key markers
- negative markers
- confound markers
- marker role
- ambiguity notes
- conservative acceptance policy when needed

The registry may be curated with LLM assistance, literature knowledge, and human review. Runtime label assignment must not ask an LLM to choose cell labels.

## Required Fields

Each candidate label should define:

- `broad_lineage`: high-level biological lineage.
- `applicable_lineage`: local lineage scope such as `B_lineage`, `T_NK_lineage`, or `Myeloid_lineage`.
- `marker_role`: one of `terminal`, `parent`, `fallback_parent`, `artifact`, `rare_parent`, `rare_terminal`, or `ambiguous_terminal`.
- `positive`: markers expected in the candidate.
- `key`: markers with stronger diagnostic value.
- `negative`: markers that argue against the candidate.
- `confound`: markers that may be shared with neighboring states and should penalize over-calling.
- `notes`: short human-readable caution or interpretation.
- `provenance`: source of the marker definition.

## Ambiguous Fine Labels

Some official labels are biologically valid but hard to separate in gene-only PBMC scRNA-seq. They should still be represented in the registry, but with an explicit conservative policy.

Examples:

- `Plasmablast` vs `Plasma Cell`: require antibody-secreting markers plus a proliferation or immature plasmablast program before accepting `Plasmablast`.
- `NKT Cell` vs cytotoxic T/NK states: require both T-cell and NK-like evidence, and avoid accepting it from NK markers alone.
- `gdT Cell` vs cytotoxic T/MAIT-like states: use TCR gamma-delta markers when available; keep `ydT Cell` only as an input alias.

## Conservative Acceptance Policy

Use `candidate_policy` for labels that should be considered but not over-called.

```yaml
candidate_policy:
  conservative_accept: true
  min_marker_gate: 0.60
  min_support_sum: 0.80
  min_key_marker_any_fraction: 0.15
  required_any_markers: [GENE1, GENE2]
  min_required_any_fraction: 0.03
```

The deterministic pipeline reads this policy generically. Do not add dataset-specific label rescue rules unless they can be expressed as a general marker, source-support, QC, or ontology principle.

## Output Behavior

The pipeline should retain:

- raw marker winner for diagnostics
- adjudicated marker assignment after conservative policy and source support
- final submitted label
- reason or flag when these disagree

This preserves auditability while preventing marker-only labels from forcing noisy rare labels into the final submission.
