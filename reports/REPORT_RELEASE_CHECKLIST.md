# Report Release Checklist

Updated: 2026-06-03 11:27:42 EDT

This checklist is mandatory before replacing or pushing any committed report bundle under `reports/current/`.

## Why This Exists

A previous report release accidentally replaced rich per-dataset reports with a thin TSV-derived summary bundle. That removed inline UMAPs, marker-expression panels, source-label overlays, and lineage subcluster views from GitHub. This file defines the release gate that prevents that failure mode from recurring.

## Required Structure

A valid current report bundle must use this layout:

```text
reports/current/
  summary/
    report_en.md
    report_ja.md
    tables/final_annotation_summary.tsv
    tables/final_annotation_label_counts.tsv
    tables/cluster_consensus_decisions.tsv
  <study_id>/
    report_en.md
    report_ja.md
    assets/*.png
    tables/label_counts.tsv
    tables/cluster_consensus_decisions.tsv
```

For Team04, the expected dataset directories are:

- `infection_study_01`
- `infection_study_04`
- `vaccination_study_04`
- `vaccination_study_06`
- `vaccination_study_09`

## Required Content Gates

Before commit or push, all of these must pass:

- Each expected dataset directory exists under `reports/current/`.
- Each dataset has both `report_en.md` and `report_ja.md`.
- Each dataset report contains inline image links.
- Each dataset has at least 8 PNG images under `assets/`.
- Every Markdown inline image link resolves to an existing file.
- Reports include dataset-specific assessment text.
- Reports include source-label or annotation-source sections.
- Reports include marker-expression sections.
- Reports include lineage/subcluster sections.
- Reports include compact evidence tables.
- Old internal version strings must not appear in public current reports: `v13`, `v14`, `v15`, `260526`, `260602_annotation_single`, `marker-gate-applied`, `final_v14`.

## Required Validation Command

Run this from the repository root before committing:

```bash
python scripts/validate_report_bundle.py --report-root reports/current
```

The command must exit with status 0. Do not push report changes if it fails.

## Required Human Spot Check

After the validation command passes, open at least one dataset report and confirm that the rendered GitHub Markdown shows inline figures. The minimum spot check is:

```text
reports/current/infection_study_01/report_ja.md
```

Confirm that `Inline Figures` shows UMAP and marker-expression panels, not only tables.

## Release Rule

Do not replace `reports/current/` with a post-hoc summary-only bundle. If reports are regenerated from current H5AD outputs, regenerate or copy the dataset-level figure assets at the same time and rerun the validator.
