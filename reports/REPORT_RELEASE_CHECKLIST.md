# Report Release Checklist

Updated: 2026-06-04 12:58:57 EDT

This checklist is mandatory before replacing or pushing any committed report bundle under `reports/current/`.

## Why This Exists

A previous report release accidentally replaced rich per-dataset reports with a thin TSV-derived summary bundle. That removed inline UMAPs, marker-expression panels, source-label overlays, and lineage subcluster views from GitHub. A later repair also allowed global UMAP overlays to masquerade as lineage-specific subcluster UMAPs. This file defines the release gate that prevents both failure modes from recurring.

## Required Structure

A valid current report bundle must use this layout:

```text
reports/current/
  summary/
    report_en.md
    report_ja.md
    tables/final_annotation_summary.tsv
    tables/final_annotation_label_counts.tsv
    tables/lineage_subcluster_evidence.tsv.gz
    tables/source_disagreement_summary.tsv
    tables/lineage_panel_status.tsv
  <study_id>/
    report_en.md
    report_ja.md
    assets/*.png
    tables/final_annotation_summary.tsv
    tables/final_annotation_label_counts.tsv
    tables/lineage_subcluster_evidence.tsv.gz
    tables/source_disagreement_summary.tsv
    tables/subcluster_candidate_scores.tsv
    tables/lineage_panel_status.tsv
    tables/<study_id>_<lineage>_true_subcluster_umap.tsv.gz
    tables/<study_id>_<lineage>_subcluster_candidate_scores.tsv
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
- Each dataset has at least 23 PNG images under `assets/`.
- Every Markdown inline image link resolves to an existing file.
- Reports include dataset-specific assessment text.
- Reports include source-label or annotation-source sections.
- Reports include marker-expression sections.
- Reports include true lineage-specific subcluster sections.
- Reports include `Subcluster Marker Score Review`.
- Each generated B/T-NK/Myeloid lineage panel has true subcluster label UMAPs, local source-label UMAPs for CellTypist/Azimuth/Pan-human/cluster-level marker-gene assignment, QC UMAPs, cluster marker gate score UMAPs, marker-expression UMAPs, marker-score heatmaps, and marker dotplots. Updated 2026-06-04 13:52:46 EDT. Lineages with fewer than 50 assigned cells must be explicitly marked `skipped_lt50` in `lineage_panel_status.tsv` and must not emit broken image links.
- Each dataset has B/T-NK/Myeloid true subcluster UMAP coordinate tables and candidate-score tables.
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

Confirm that `Inline Figures` shows global UMAPs, marker-expression panels, true lineage-specific subcluster UMAPs, and local source-label overlays. Confirm that `Subcluster Marker Score Review` shows lineage-specific cluster marker gate score UMAPs, marker-expression UMAPs, score heatmaps, and dotplots, not only tables.

## Release Rule

Do not replace `reports/current/` with a post-hoc summary-only bundle or hand-patched report bundle. If report content is insufficient, update the deterministic pipeline/templates/validator, rerun each dataset cleanly, package with `scripts/package_clean_reports.py`, and rerun the validator.
