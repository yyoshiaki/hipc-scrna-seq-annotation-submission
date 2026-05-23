# HIPC scRNA-seq Annotation Submission

Updated: 2026-05-23 EDT

Clean implementation repository for the HIPC scRNA-seq Annotation Benchmark v12 independent annotation workflow.

## Purpose

This repository is intended to hold the portable submission implementation, not exploratory runs or large derived files. The working repository remains the place for experiments, large outputs, and review artifacts.

## Directory Map

- `scripts/pipeline/`: deterministic annotation CLI
- `configs/`: pipeline config, manifest templates, and reference manifests
- `data/reference/`: small official ontology/reference tables only
- `skills/`: Codex skill describing annotation concept, execution, validation, and reporting contract
- `docs/`: design notes for submission strategy
- `outputs/`: generated outputs, ignored by git
- `reports/`: generated reports, mostly ignored by git

## Standard Run

From this repository root:

```bash
skills/hipc-annotation-v12/scripts/run_v12.sh
```

For the Team04 shared evidence containers on the Yale server:

```bash
HIPC_V12_OUT=outputs/final_annotations/260523_v12_submission_check REPORT_LANGUAGES=en,ja /gpfs/gibbs/project/hafler/yy693/conda_envs/scanpy1.10.2/bin/python scripts/pipeline/hipc_annotate_v12.py   --config configs/v12_pipeline.json   --manifest configs/v12_manifest.team04.shared.tsv   --out outputs/final_annotations/260523_v12_submission_check   --report-languages en,ja
```

Validate outputs:

```bash
/gpfs/gibbs/project/hafler/yy693/conda_envs/scanpy1.10.2/bin/python skills/hipc-annotation-v12/scripts/validate_v12_outputs.py   --out outputs/final_annotations/260523_v12_submission_check
```

## Data Policy

Large input H5ADs and generated outputs are not committed. Team04 shared evidence containers currently live in the working repository output area and are referenced by `configs/v12_manifest.team04.shared.tsv`.

## Submission Philosophy

The implementation should remain independent of prior-version submission labels. The skill decision contract defines the annotation principles: broad lineage assignment from independent evidence, lineage-specific subclustering, marker/reference/QC/ontology adjudication, explicit doublet handling, and rich report diagnostics.
