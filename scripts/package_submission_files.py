#!/usr/bin/env python3
import argparse
import shutil
import zipfile
from pathlib import Path

import pandas as pd

DEFAULT_STUDIES = [
    "infection_study_01",
    "infection_study_03",
    "infection_study_04",
    "infection_study_06",
    "vaccination_study_01",
    "vaccination_study_04",
    "vaccination_study_06",
    "vaccination_study_09",
    "vaccination_study_10",
]

parser = argparse.ArgumentParser(description="Package HIPC per-study submission TSVs for upload/review.")
parser.add_argument("--run-root", required=True, help="Directory containing one output directory per study.")
parser.add_argument("--out", required=True, help="Output package directory.")
parser.add_argument("--studies", default=",".join(DEFAULT_STUDIES), help="Comma-separated study IDs to include.")
parser.add_argument("--replace", action="store_true")
args = parser.parse_args()

run_root = Path(args.run_root).resolve()
out = Path(args.out).resolve()
studies = [study.strip() for study in args.studies.split(",") if study.strip()]

if out.exists() and args.replace:
    shutil.rmtree(out)
out.mkdir(parents=True, exist_ok=True)
submission_dir = out / "submissions"
submission_dir.mkdir(parents=True, exist_ok=True)

summary_rows = []
for study in studies:
    source = run_root / study / "submissions" / f"{study}_annotation.tsv"
    if not source.exists():
        raise SystemExit(f"Missing submission TSV: {source}")
    target = submission_dir / source.name
    shutil.copy2(source, target)
    table = pd.read_csv(target, sep="\t")
    required_cols = ["cell_barcode", "predicted_cell_type", "confidence_score"]
    missing = [col for col in required_cols if col not in table.columns]
    if missing:
        raise SystemExit(f"{target}: missing columns {missing}")
    summary_rows.append(
        {
            "study": study,
            "submission_tsv": str(target.relative_to(out)),
            "n_rows": int(table.shape[0]),
            "n_labels": int(table["predicted_cell_type"].nunique()),
            "median_confidence": float(table["confidence_score"].median()),
            "low_confidence_n": int(table["confidence_score"].lt(0.60).sum()),
        }
    )

summary = pd.DataFrame(summary_rows)
summary.to_csv(out / "submission_package_summary.tsv", sep="\t", index=False)
readme_lines = [
    "# HIPC submission package",
    "",
    "This directory contains one per-study TSV for the Team04 HIPC scRNA-seq Annotation Benchmark target set.",
    "Each TSV has `cell_barcode`, `predicted_cell_type`, and `confidence_score` columns.",
    "",
    "## Files",
    "",
]
for row in summary.itertuples(index=False):
    readme_lines.append(f"- `{row.submission_tsv}`: {row.n_rows} rows, {row.n_labels} labels, median confidence {row.median_confidence:.3f}")
(out / "README.md").write_text("\n".join(readme_lines) + "\n", encoding="utf-8")
zip_path = out.with_suffix(".zip")
if zip_path.exists():
    zip_path.unlink()
with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
    for path in sorted(out.rglob("*")):
        if path.is_file():
            zf.write(path, path.relative_to(out.parent))
print(summary.to_string(index=False))
print(f"Wrote {out}")
print(f"Wrote {zip_path}")
