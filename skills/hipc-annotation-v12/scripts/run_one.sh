#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DEFAULT_REPO_ROOT="$(cd "$SCRIPT_DIR/../../.." && pwd)"
REPO_ROOT="${HIPC_ANNOTATION_REPO:-$DEFAULT_REPO_ROOT}"
PYTHON_BIN="${HIPC_SCANPY_PYTHON:-/gpfs/gibbs/project/hafler/yy693/conda_envs/scanpy1.10.2/bin/python}"
CONFIG="configs/v12_pipeline.json"
REPORT_LANGUAGES="en"
BARCODE_KEY="index"
RAW_COUNT_LAYER="counts"
BATCH_KEY="study_id"
SAMPLE_KEY="study_id"
SUBMISSION_TEMPLATE=""
NOTES="single-dataset run"
VALIDATE_ONLY="0"
STUDY_ID=""
INPUT_H5AD=""
OUT=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    --study-id) STUDY_ID="$2"; shift 2 ;;
    --input-h5ad) INPUT_H5AD="$2"; shift 2 ;;
    --out) OUT="$2"; shift 2 ;;
    --config) CONFIG="$2"; shift 2 ;;
    --report-languages) REPORT_LANGUAGES="$2"; shift 2 ;;
    --barcode-key) BARCODE_KEY="$2"; shift 2 ;;
    --raw-count-layer) RAW_COUNT_LAYER="$2"; shift 2 ;;
    --batch-key) BATCH_KEY="$2"; shift 2 ;;
    --sample-key) SAMPLE_KEY="$2"; shift 2 ;;
    --submission-template) SUBMISSION_TEMPLATE="$2"; shift 2 ;;
    --notes) NOTES="$2"; shift 2 ;;
    --validate-only) VALIDATE_ONLY="1"; shift ;;
    *) echo "Unknown argument: $1" >&2; exit 2 ;;
  esac
done

if [[ -z "$STUDY_ID" || -z "$OUT" ]]; then
  echo "Required: --study-id and --out" >&2
  exit 2
fi
if [[ "$VALIDATE_ONLY" != "1" && -z "$INPUT_H5AD" ]]; then
  echo "Required unless --validate-only: --input-h5ad" >&2
  exit 2
fi

cd "$REPO_ROOT"
if [[ "$VALIDATE_ONLY" != "1" ]]; then
  "$PYTHON_BIN" scripts/pipeline/hipc_annotate_one.py     --study-id "$STUDY_ID"     --input-h5ad "$INPUT_H5AD"     --out "$OUT"     --config "$CONFIG"     --report-languages "$REPORT_LANGUAGES"     --barcode-key "$BARCODE_KEY"     --raw-count-layer "$RAW_COUNT_LAYER"     --batch-key "$BATCH_KEY"     --sample-key "$SAMPLE_KEY"     --submission-template "$SUBMISSION_TEMPLATE"     --notes "$NOTES"
fi

"$PYTHON_BIN" skills/hipc-annotation-v12/scripts/validate_v12_outputs.py   --out "$OUT"   --config "$CONFIG"   --study-id "$STUDY_ID"
