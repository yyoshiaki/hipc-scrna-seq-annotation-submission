# HIPC Team04 emergency submission report

Updated: 2026-06-12 11:49:00 EDT

This report bundle matches the emergency submission package prepared for the June 12, 2026 HIPC scRNA-seq Annotation Benchmark deadline.

Submission package path on Yale server:

```text
/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_package_emergency_260612.zip
```

The package contains 9 per-study TSV files and intentionally excludes `infection_study_07` because the organizers stated that raw counts are unavailable for that study. The package includes `confidence_score` for all submitted cells.

## Source Selection

- Reviewed v22 evidence-derived TSVs: infection_study_01, infection_study_04, vaccination_study_04, vaccination_study_06, vaccination_study_09
- Current-clean fallback TSVs: infection_study_03, infection_study_06, vaccination_study_01, vaccination_study_10

This is a deadline-driven no-recompute package. It avoids submitting the all-current-clean package because that package was valid but overly coarse for every dataset. It also avoids submitting the full v22 package as-is because that package included `infection_study_07` and was not aligned with the corrected active manifest.

## Validation Summary

| study | columns_ok | invalid_label_n | confidence_min | confidence_max |
| --- | --- | --- | --- | --- |
| infection_study_01 | True | 0 | 0.4500 | 0.8500 |
| infection_study_03 | True | 0 | 0.3847 | 0.5432 |
| infection_study_04 | True | 0 | 0.4500 | 0.8500 |
| infection_study_06 | True | 0 | 0.3748 | 0.5185 |
| vaccination_study_01 | True | 0 | 0.3647 | 0.5500 |
| vaccination_study_04 | True | 0 | 0.3890 | 0.8500 |
| vaccination_study_06 | True | 0 | 0.3870 | 0.8500 |
| vaccination_study_09 | True | 0 | 0.3889 | 0.8500 |
| vaccination_study_10 | True | 0 | 0.3647 | 0.5500 |

## Package Summary

| study | source_package | n_rows | template_rows | barcode_order_matches_template | n_labels | median_confidence | low_confidence_n |
| --- | --- | --- | --- | --- | --- | --- | --- |
| infection_study_01 | v22 | 54924 | 54924 | True | 16 | 0.7772 | 2527 |
| infection_study_03 | current_clean | 646739 | 646739 | True | 4 | 0.4437 | 646739 |
| infection_study_04 | v22 | 43767 | 43767 | True | 15 | 0.7762 | 497 |
| infection_study_06 | current_clean | 827389 | 827389 | True | 4 | 0.4500 | 827389 |
| vaccination_study_01 | current_clean | 307194 | 307194 | True | 4 | 0.4366 | 307194 |
| vaccination_study_04 | v22 | 66065 | 66065 | True | 14 | 0.8063 | 1820 |
| vaccination_study_06 | v22 | 57419 | 57419 | True | 12 | 0.7724 | 3430 |
| vaccination_study_09 | v22 | 139960 | 139960 | True | 18 | 0.7772 | 478 |
| vaccination_study_10 | current_clean | 47511 | 47511 | True | 4 | 0.4500 | 47511 |

## Per-Dataset Reports

- [infection_study_01](../infection_study_01/report_en.md)
- [infection_study_03](../infection_study_03/report_en.md)
- [infection_study_04](../infection_study_04/report_en.md)
- [infection_study_06](../infection_study_06/report_en.md)
- [vaccination_study_01](../vaccination_study_01/report_en.md)
- [vaccination_study_04](../vaccination_study_04/report_en.md)
- [vaccination_study_06](../vaccination_study_06/report_en.md)
- [vaccination_study_09](../vaccination_study_09/report_en.md)
- [vaccination_study_10](../vaccination_study_10/report_en.md)

## Tables

- `tables/submission_package_summary.tsv`
- `tables/submission_validation_summary.tsv`
- `tables/all_final_submission_label_counts.tsv`
