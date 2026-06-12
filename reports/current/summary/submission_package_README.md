# HIPC Team04 emergency submission package

Created: 2026-06-12 EDT

This package contains the best locally available no-recompute submission TSVs for the June 12 deadline. `infection_study_07` is intentionally excluded because the organizer thread indicates raw counts are unavailable and local processing could not support the standard raw-count workflow.

## Contents

- `infection_study_01_annotation.tsv`: 54924 rows, source `v22`, 16 labels, median confidence 0.7772
- `infection_study_03_annotation.tsv`: 646739 rows, source `current_clean`, 4 labels, median confidence 0.4437
- `infection_study_04_annotation.tsv`: 43767 rows, source `v22`, 15 labels, median confidence 0.7762
- `infection_study_06_annotation.tsv`: 827389 rows, source `current_clean`, 4 labels, median confidence 0.45
- `vaccination_study_01_annotation.tsv`: 307194 rows, source `current_clean`, 4 labels, median confidence 0.4366
- `vaccination_study_04_annotation.tsv`: 66065 rows, source `v22`, 14 labels, median confidence 0.8063
- `vaccination_study_06_annotation.tsv`: 57419 rows, source `v22`, 12 labels, median confidence 0.7724
- `vaccination_study_09_annotation.tsv`: 139960 rows, source `v22`, 18 labels, median confidence 0.7772
- `vaccination_study_10_annotation.tsv`: 47511 rows, source `current_clean`, 4 labels, median confidence 0.45

## Validation

- All included TSV row counts match the corresponding Team04 annotation template row counts.
- All included TSV barcode orders match the corresponding Team04 annotation templates.
- Columns are `cell_barcode`, `predicted_cell_type`, and `confidence_score`.
