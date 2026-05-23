# v12 Full Run Validation

Updated: 2026-05-23 EDT

Full run executed from the clean submission repository using:

```bash
HIPC_V12_OUT=outputs/final_annotations/260523_v12_full_run \
HIPC_V12_MANIFEST=configs/v12_manifest.team04.shared.tsv \
REPORT_LANGUAGES=en,ja \
skills/hipc-annotation-v12/scripts/run_v12.sh
```

Validation result: `VALIDATION_PASSED`.

The committed report bundle contains Markdown reports and inline figure assets only. Large generated H5ADs, submission TSVs, and diagnostics tables remain under ignored `outputs/`.
