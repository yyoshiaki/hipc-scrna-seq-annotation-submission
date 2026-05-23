#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DEFAULT_REPO_ROOT="$(cd "$SCRIPT_DIR/../../.." && pwd)"
REPO_ROOT="${HIPC_ANNOTATION_REPO:-$DEFAULT_REPO_ROOT}"
PYTHON_BIN="${HIPC_SCANPY_PYTHON:-/gpfs/gibbs/project/hafler/yy693/conda_envs/scanpy1.10.2/bin/python}"
HIPC_V12_OUT="${HIPC_V12_OUT:-outputs/final_annotations/260522_v12_independent_cli}"
REPORT_LANGUAGES="${REPORT_LANGUAGES:-en}"
HIPC_V12_VALIDATE_ONLY="${HIPC_V12_VALIDATE_ONLY:-0}"

cd "$REPO_ROOT"
if [[ "$HIPC_V12_VALIDATE_ONLY" != "1" ]]; then
  "$PYTHON_BIN" scripts/pipeline/hipc_annotate_v12.py   --config configs/v12_pipeline.json   --manifest configs/v12_manifest.example.tsv   --out "$HIPC_V12_OUT"   --report-languages "$REPORT_LANGUAGES"
fi

"$PYTHON_BIN" skills/hipc-annotation-v12/scripts/validate_v12_outputs.py   --out "$HIPC_V12_OUT"   --config configs/v12_pipeline.json
