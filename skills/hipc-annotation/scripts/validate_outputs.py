#!/usr/bin/env python
import argparse
import json
import re
from pathlib import Path

import anndata as ad
import pandas as pd

parser = argparse.ArgumentParser(description="Validate HIPC annotation outputs")
parser.add_argument("--out", required=True)
parser.add_argument("--config", default="configs/annotation_pipeline.json")
parser.add_argument("--study-id", default="")
args = parser.parse_args()

project_root = Path.cwd()
output_root = Path(args.out)
if not output_root.is_absolute():
    output_root = project_root / output_root

config = json.loads((project_root / args.config).read_text())
ontology = pd.read_csv(project_root / config["ontology"]["path"], sep="	")
allowed_labels = set(ontology[config["ontology"]["label_column"]].astype(str)) - set(config["ontology"].get("excluded_submission_labels", []))

rows = []
failures = []
submission_paths = sorted((output_root / "submissions").glob("*_annotation.tsv"))
if args.study_id:
    submission_paths = [path for path in submission_paths if path.name == f"{args.study_id}_annotation.tsv"]
if not submission_paths:
    raise SystemExit(f"No submission TSV found for study_id={args.study_id or 'ALL'} in {output_root / 'submissions'}")

for sub_path in submission_paths:
    study = sub_path.name.replace("_annotation.tsv", "")
    h5ad_path = output_root / "cellxgene" / f"{study}.final_annotation.cxg.h5ad"
    if not h5ad_path.exists():
        failures.append(f"missing h5ad: {h5ad_path}")
        continue
    sub = pd.read_csv(sub_path, sep="	")
    if "predicted_cell_type" not in sub.columns:
        failures.append(f"{study}: missing predicted_cell_type column")
        continue
    h5 = ad.read_h5ad(h5ad_path, backed="r")
    invalid_labels = sorted(set(sub["predicted_cell_type"].astype(str)) - allowed_labels)
    obs_label_column = "submission_cell_type"
    has_obs_label = obs_label_column in h5.obs.columns
    h5ad_annotation_match = False
    if has_obs_label and len(sub) == h5.n_obs:
        h5ad_annotation_match = bool((h5.obs[obs_label_column].astype(str).values == sub["predicted_cell_type"].astype(str).values).all())
    row = {
        "study": study,
        "submission_rows": len(sub),
        "h5ad_n_obs": h5.n_obs,
        "row_match": len(sub) == h5.n_obs,
        "missing_label": int(sub["predicted_cell_type"].isna().sum()),
        "invalid_label_n": len(invalid_labels),
        "invalid_labels": ",".join(invalid_labels),
        "h5ad_annotation_match": h5ad_annotation_match,
        "has_confidence": "confidence_score" in h5.obs.columns,
    }
    rows.append(row)
    h5.file.close()
    for key in ["row_match", "h5ad_annotation_match", "has_confidence"]:
        if not row[key]:
            failures.append(f"{study}: {key}=False")
    if row["missing_label"]:
        failures.append(f"{study}: missing predicted labels")
    if invalid_labels:
        failures.append(f"{study}: invalid labels {invalid_labels}")

broken_links = []
report_paths = sorted(output_root.glob("report_*.md"))
if not report_paths:
    report_paths = sorted((output_root / "reports").glob("report_*.md"))
for report in report_paths:
    text = report.read_text()
    for target in re.findall(r"!\[[^\]]*\]\(([^)]+)\)", text):
        resolved = (report.parent / target).resolve()
        if not resolved.exists():
            broken_links.append(f"{report.name}: {target}")

if broken_links:
    failures.extend([f"broken report link: {item}" for item in broken_links])

summary = pd.DataFrame(rows)
print(summary.to_string(index=False))
print(f"broken_report_links: {len(broken_links)}")
if failures:
    print("VALIDATION_FAILED")
    for failure in failures:
        print(f"- {failure}")
    raise SystemExit(1)
print("VALIDATION_PASSED")
