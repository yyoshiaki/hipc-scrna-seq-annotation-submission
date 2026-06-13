# HIPC Team04 Emergency Submission Status

Updated: 2026-06-12 America/New_York

## Current Recommendation

Use `outputs/submission_package_v24_pragmatic_260612.zip` as the current emergency submission candidate.

This package combines:

- v22 outputs for the five previously stable studies: `infection_study_01`, `infection_study_04`, `vaccination_study_04`, `vaccination_study_06`, and `vaccination_study_09`.
- v23 marker-rescue outputs for `infection_study_03`, `infection_study_06`, and `vaccination_study_01`, because the conservative v24 outputs remained too broad for these datasets.
- v24 safe output for `vaccination_study_10`, because this dataset has a transformed 1271-gene input and marker-only rescue is not reliable without raw counts.
- `infection_study_07` is excluded because the organizers indicated that the no-raw-count fallback can be omitted.

The per-study package summary is stored at:

`reports/current/summary/tables/submission_package_v24_pragmatic_260612_summary.tsv`

## Why The Result Is Still Not Good Enough

The problematic datasets still have high broad-parent label fractions:

- `infection_study_03`: 0.8379 parent-or-Blood fraction in the pragmatic package.
- `infection_study_06`: 0.8234 parent-or-Blood fraction in the pragmatic package.
- `vaccination_study_01`: 0.8583 parent-or-Blood fraction in the pragmatic package.
- `vaccination_study_10`: 1.0000 parent-or-Blood fraction in the pragmatic package.

This means the pipeline is valid as an emergency package, but it is not biologically satisfying. The key failure mode is that some datasets lack usable reference-transfer evidence in the current evidence container, so the pipeline falls back to marker/subcluster evidence and broad lineage labels.

## v24 Safety Fix

v24 fixed a real safety issue in the marker-only rescue logic:

- Marker availability alerts were not reliably applied to registry-derived marker labels.
- Marker-only rescue could revive labels that had been rejected by label-specific conservative gates.
- Marker-only rescue is now blocked for warning/critical marker availability and for rare or artifact-prone labels.
- `vaccination_study_10` is handled conservatively because the available matrix is transformed and gene-limited.

This makes v24 safer, but more conservative. It does not solve the biological resolution problem by itself.

## Next Required Improvement

Harmony or another batch-correction strategy is likely needed before final annotation optimization.

The current pipeline relies heavily on reference labels and marker-gated subclusters. For the problematic datasets, this is not enough. A Harmony-based workflow should:

- Build a batch-corrected embedding per dataset or per compatible study group.
- Recompute neighbor graph, Leiden clusters, and UMAP on the corrected embedding.
- Use corrected clusters as the annotation unit rather than relying only on reference-transfer labels.
- Re-evaluate marker evidence on cluster-level summaries.
- Keep raw or count-like expression for marker scoring and reference mapping where required.

The expected benefit is not just prettier UMAPs. The goal is to recover stable broad lineage structure before fine-label assignment, especially for datasets where the current pipeline leaves many cells as `Blood Cell`, `T Cell`, `B Cell`, or `Myeloid Cell`.
