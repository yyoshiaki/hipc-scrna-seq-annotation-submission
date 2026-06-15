# AGENTS

- Use Japanese for user-facing progress in the working environment; keep repository docs and code comments in English by default for submission portability.
- Default Python environment: `/gpfs/gibbs/project/hafler/yy693/conda_envs/scanpy1.10.2`.
- Main engine: `scripts/pipeline/hipc_annotate.py`.
- Main skill: `skills/hipc-annotation`.
- Do not commit large H5AD outputs, raw data, or generated reports unless explicitly requested.
- Use `configs/manifest.team04.current_clean.tsv` for the final Team04 clean-run input contract.
- Do not use deprecated development manifests for final work: `configs/manifest.example.tsv`, `configs/manifest.team04.beta_all.tsv`, and `configs/manifest.team04.shared.tsv`.
- The submitted package follows the organizer fake-submission structure: flat per-study `*_annotation.tsv` files plus `Team04_Pipeline_ApproachSummary.docx`.
- `infection_study_07` is intentionally excluded from the submitted set because raw counts were not available in the current Team04 distribution.
- `vaccination_study_10` is intentionally included but low confidence because the visible Team04 portal files only expose transformed processed matrices, not separate raw/unfiltered/filtered raw counts.
