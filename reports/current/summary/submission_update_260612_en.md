# HIPC Submission Candidate Update 2026-06-12

Updated: 2026-06-12 EDT

## Recommendation

The current emergency submission candidate is `submission_package_v24_pragmatic_260612.zip`.

This package uses a mixed strategy:

- `infection_study_01`, `infection_study_04`, `vaccination_study_04`, `vaccination_study_06`, `vaccination_study_09`: stable v22 outputs.
- `infection_study_03`, `infection_study_06`, `vaccination_study_01`: v23 aggressive marker-rescue outputs to improve specificity.
- `vaccination_study_10`: v24 safe fallback because the input is a transformed 1271-gene matrix and marker-only rescue is not reliable.
- `infection_study_07`: excluded because of raw-count availability issues and organizer guidance.

## Submission Packages

Server-side zip:

`/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_package_v24_pragmatic_260612.zip`

Comparison packages:

- Safe: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_package_v24_safe_260612.zip`
- Aggressive: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_package_v23_aggressive_260612.zip`

## Important Caveat

v23 reduces parent/Blood labels through marker-only rescue, but it can bypass marker availability alerts and label-specific conservative gates. v24 fixes this behavior.

However, v24 safe is too conservative for several datasets and leaves many parent/Blood labels in `infection_study_03`, `infection_study_06`, `vaccination_study_01`, and `vaccination_study_10`. The pragmatic package is therefore the current emergency choice.

## Summary Tables

- [Pragmatic package summary](tables/submission_package_v24_pragmatic_260612_summary.tsv)
- [Safe package summary](tables/submission_package_v24_safe_260612_summary.tsv)
- [Aggressive package summary](tables/submission_package_v23_aggressive_260612_summary.tsv)

