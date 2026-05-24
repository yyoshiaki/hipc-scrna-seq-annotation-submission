#!/usr/bin/env python
import argparse
import subprocess
from pathlib import Path

import pandas as pd

parser = argparse.ArgumentParser(description="Run HIPC v12 annotation for one dataset")
parser.add_argument("--study-id", required=True)
parser.add_argument("--input-h5ad", required=True)
parser.add_argument("--out", required=True)
parser.add_argument("--config", default="configs/v12_pipeline.json")
parser.add_argument("--report-languages", default="en")
parser.add_argument("--barcode-key", default="index")
parser.add_argument("--raw-count-layer", default="counts")
parser.add_argument("--batch-key", default="study_id")
parser.add_argument("--sample-key", default="study_id")
parser.add_argument("--submission-template", default="")
parser.add_argument("--notes", default="single-dataset run")
args = parser.parse_args()

project_root = Path.cwd()
out = Path(args.out)
if not out.is_absolute():
    out = project_root / out
out.mkdir(parents=True, exist_ok=True)
manifest_path = out / f"{args.study_id}.manifest.tsv"

manifest = pd.DataFrame(
    [
        {
            "study_id": args.study_id,
            "input_h5ad": args.input_h5ad,
            "barcode_key": args.barcode_key,
            "raw_count_layer": args.raw_count_layer,
            "batch_key": args.batch_key,
            "sample_key": args.sample_key,
            "submission_template": args.submission_template,
            "notes": args.notes,
        }
    ]
)
manifest.to_csv(manifest_path, sep="	", index=False)

cmd = [
    "/gpfs/gibbs/project/hafler/yy693/conda_envs/scanpy1.10.2/bin/python",
    "scripts/pipeline/hipc_annotate_v12.py",
    "--config",
    args.config,
    "--manifest",
    str(manifest_path),
    "--out",
    str(out),
    "--report-languages",
    args.report_languages,
]
subprocess.run(cmd, check=True)
