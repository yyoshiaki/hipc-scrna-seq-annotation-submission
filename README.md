# HIPC scRNA-seq Annotation Submission

Updated: 2026-06-15 EDT

Clean implementation repository for the HIPC scRNA-seq Annotation Benchmark Team04 workflow.

This repository is organized around a Codex skill plus deterministic helper scripts. The intended interface is not a hand-written one-off notebook: Codex receives an ontology and one dataset, checks or builds the marker registry, runs the deterministic annotation workflow, validates outputs, inspects the generated report, and only then returns a completion summary.

## Submission Scope

Team04 beta target set is handled from the current May 11 beta distribution under:

```text
/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/data/raw/hipc_beta_20260511
```

The clean active manifest is `configs/manifest.team04.current_clean.tsv`. It excludes `infection_study_07` because the organizers stated that raw counts are not available for that study, and the current Team04 directory also has no `unfiltered`, `raw`, or `filtered_raw` file for it.

The active clean submission set contains 9 datasets:

- `infection_study_01`
- `infection_study_03`
- `infection_study_04`
- `infection_study_06`
- `vaccination_study_01`
- `vaccination_study_04`
- `vaccination_study_06`
- `vaccination_study_09`
- `vaccination_study_10`

`vaccination_study_10` remains in the active manifest, but it is flagged as a transformed 1,271-gene processed matrix because no additional raw-count file is visible in the current Team04 distribution. Raw-count-dependent evidence should not be interpreted normally for this dataset unless a corrected upstream file is provided.

Older development manifests may remain for audit history only. Do not use `configs/manifest.team04.beta_all.tsv` or `configs/manifest.team04.shared.tsv` for clean submission generation.

## Current Clean-Run Status

Updated: 2026-06-15 EDT

The current clean run completed for all 9 active datasets and excluded `infection_study_07`.

Local run root:

```text
/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_v25_harmony_reference_rescue
```

Submission package:

```text
/vast/palmer/pi/hafler/yy693/hipc-scrna-seq-annotation-submission/outputs/current_submission_package.zip
```

Validation status:

- All 9 active datasets have matching submission rows and H5AD cells.
- No invalid ontology labels were emitted.
- Required CellTypist, Pan-human Azimuth, and Azimuth PBMC L2 coverage checks passed for all datasets where those evidence sources are required.
- `reports/current` validates with 9 expected datasets, 261 PNG files, and 504 inline image links.

Important caveat:

- `vaccination_study_10` remains a known low-gene/raw-count-limited exception. It is included in the package, but reference-mapping evidence is unavailable in the current input contract and all cells are low confidence.
- `infection_study_07` is excluded because raw counts are unavailable in the current organizer-provided Team04 distribution.

Large H5ADs, generated H5ADs, and upload TSVs are not committed to GitHub. They are generated under the Yale server workspace and packaged separately.

## Directory Map

- `skills/hipc-annotation/`: Codex operating procedure and report templates.
- `configs/annotation_pipeline.json`: deterministic thresholds, ontology path, report options, and reference manifests.
- `configs/marker_registry.yaml`: frozen marker registry used by deterministic scoring.
- `configs/manifest.team04.current_clean.tsv`: active clean Team04 beta inputs, excluding `infection_study_07`.
- `configs/manifest.team04.beta_all.tsv`: deprecated mixed development manifest; do not use for final clean runs.
- `data/reference/`: small official ontology/reference files.
- `scripts/pipeline/`: deterministic annotation implementation.
- `scripts/package_clean_reports.py`: packages generated per-dataset reports into `reports/current/`.
- `scripts/package_submission_files.py`: packages per-study submission TSVs into a review/upload directory and ZIP.
- `reports/current/`: committed lightweight report bundle only.

## Standard Codex Workflow

### Step 1: Ontology-to-Registry Preparation

Input:

- official ontology TSV, usually `data/reference/CT_Ontology_Spreadsheet_20260323.tsv`
- target tissue/context notes, if available
- optional existing marker registry

Codex should:

1. Read the ontology labels and identify terminal, parent, ambiguous, artifact, and difficult-to-separate labels.
2. Create or revise `configs/marker_registry.yaml` with positive, key, negative, and confound markers for candidate labels.
3. Add conservative notes for labels expected to be hard to distinguish, for example `Plasma Cell` vs `Plasmablast`, `gdT Cell` vs cytotoxic T/MAIT, or `NKT Cell` vs NK/cytotoxic T.
4. Run `scripts/pipeline/hipc_audit_marker_registry.py` and stop if coverage or schema validation fails.
5. Freeze the registry before final deterministic annotation. Runtime LLM per-cell labeling is not allowed.

### Step 2: Single-Dataset Annotation and Review

Input:

- one processed H5AD
- `study_id`
- output directory
- frozen marker registry
- official ontology config

Codex should:

1. Run the `hipc-annotation` skill on one dataset.
2. Use the bundled helper internally; do not ask the user to run shell commands unless blocked.
3. Validate submission row counts, official labels, H5AD/submission agreement, confidence fields, and report image links.
4. Inspect `tables/source_effectiveness_summary.tsv`, `tables/source_disagreement_summary.tsv`, `tables/marker_assignment_feedback.tsv`, and `tables/llm_subcluster_review_queue.tsv`.
5. If the report is too generic, improve the dataset-specific assessment and rerun/package cleanly rather than manually patching `reports/current/`.

Example Codex request:

```text
Use the hipc-annotation skill.
Study ID: infection_study_04
Input H5AD: /path/to/infection_study_04_processed.h5ad
Output root: /path/to/outputs/submission_final/infection_study_04
Report languages: en,ja
Run end-to-end and report back only after validation passes.
```

## Deterministic Annotation Method

```mermaid
flowchart TD
    U[User provides ontology + one H5AD] --> C1[Codex: inspect input, config, registry]
    C1 --> R1{Registry complete for ontology?}
    R1 -- no --> R2[Codex: curate marker registry]
    R2 --> R3[Audit registry coverage and schema]
    R3 --> C1
    R1 -- yes --> P0[Pipeline: read H5AD and evidence]

    P0 --> E1[Reference labels: CellTypist, Pan-human/Azimuth, cluster consensus]
    P0 --> E2[Marker registry scores and availability]
    P0 --> E3[QC and doublet evidence]
    P0 --> E4[scRefMapping if lineage-scoped evidence exists]

    E1 --> B[Assign broad lineage]
    E2 --> B
    E3 --> B
    B --> S[Recluster within broad lineage]
    S --> F[Score official candidate labels]
    E4 --> F
    E2 --> F
    F --> O[Ontology-constrained final label]
    O --> Q[Confidence calibration and doublet/QC handling]
    Q --> T[Submission TSV + annotated H5AD]
    Q --> D[Diagnostics tables and inline report]
    D --> L[LLM review queue for policy/registry feedback]
    T --> V[Validator]
    D --> V
    V --> C2[Codex: inspect report and summarize concerns]
```

scRefMapping is intentionally lineage-scoped. It is not used for broad lineage assignment.

## Evidence and Source-Effectiveness Reporting

The report includes `Annotation Source Effectiveness`. This is not accuracy against external ground truth. It summarizes how much each source contributed to the final annotation:

- `coverage`: fraction of cells where a source returned an informative label.
- `final_concordance`: fraction of informative cells where that source agreed with the final label.
- `high_conf_concordance`: concordance restricted to high-confidence final labels.
- `unique_support`: cells where only that source agreed with the final label.
- `discordant`: informative cells where that source disagreed with the final label.

These statistics are intended to show which sources supported the deterministic result in each dataset. They should not be reported as benchmark accuracy without organizer ground truth.

## Output Contract

For one dataset:

```text
<output_root>/
  submissions/<study_id>_annotation.tsv
  cellxgene/<study_id>.final_annotation.cxg.h5ad
  report_en.md
  report_ja.md
  assets/*.png
  figures/*.png or *.pdf
  tables/final_annotation_summary.tsv
  tables/final_annotation_validation.tsv
  tables/source_effectiveness_summary.tsv
  tables/source_disagreement_summary.tsv
  tables/marker_assignment_feedback.tsv
  tables/llm_subcluster_review_queue.tsv
```

Submission TSV schema:

```text
cell_barcode
predicted_cell_type
confidence_score
```

## Packaging Reports and Submission Files

Report bundle packaging:

```bash
python scripts/package_clean_reports.py   --run-root /vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_v25_harmony_reference_rescue   --report-root reports/current   --replace
python scripts/validate_report_bundle.py --report-root reports/current
```

Submission TSV package:

```bash
python scripts/package_submission_files.py   --run-root /vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_v25_harmony_reference_rescue   --out outputs/current_submission_package   --replace
```

The package helper writes per-study TSVs, a summary table, a README, and a ZIP archive.

## Validation Contract

A run is not complete unless validation confirms:

- submission rows match H5AD observations
- `predicted_cell_type` has no missing values
- predicted labels are official ontology labels after configured exclusions
- H5AD `submission_cell_type` matches the submission TSV
- `confidence_score` is present
- report inline image links resolve
- source-effectiveness and source-disagreement diagnostics are present

## Core Guardrails

- Do not use prior-version submitted labels as the base annotation.
- Do not hard-code study-specific rescues that cannot be explained as marker/reference/QC/ontology policy.
- Use marker genes through `configs/marker_registry.yaml`, not ad hoc code lists.
- Keep doublets as submitted labels when supported; do not silently filter cells out.
- Use parent/root labels conservatively when evidence is weak, and expose that uncertainty in confidence and reports.
- If a report is insufficient, update the pipeline/template and rerun cleanly; do not manually patch committed reports.
