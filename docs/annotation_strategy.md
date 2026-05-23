# Annotation Strategy

Updated: 2026-05-23 EDT

The v12 workflow separates deterministic execution from annotation reasoning.

- CLI role: reproducibly produce submission TSVs, cellxgene H5ADs, diagnostics, and reports.
- Skill role: preserve the manual-annotation decision contract and prevent ad hoc, study-specific fixes.

Core principles:

1. Do not use prior-version submitted labels as the base annotation.
2. Assign broad lineage from independent reference, marker, raw-label, and QC evidence.
3. Recluster B, T/NK, and myeloid lineages separately.
4. Use marker support and subcluster coherence before accepting fine labels.
5. Treat scRefMapping as lineage-scoped auxiliary evidence, especially when marker availability is low.
6. Submit `Doublet` only when supported; do not filter cells out silently.
7. Prefer documented uncertainty over hard-coded local fixes.
8. Reports must expose UMAPs, marker dotplots, disagreement, parent-label residuals, confidence, and validation.
