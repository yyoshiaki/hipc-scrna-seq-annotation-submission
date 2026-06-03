#!/usr/bin/env python3
import argparse
import re
from pathlib import Path

EXPECTED_STUDIES = [
    "infection_study_01",
    "infection_study_04",
    "vaccination_study_04",
    "vaccination_study_06",
    "vaccination_study_09",
]
FORBIDDEN_PATTERNS = [
    "v13",
    "v14",
    "v15",
    "260526",
    "260602_annotation_single",
    "marker-gate-applied",
    "final_v14",
]
REQUIRED_PHRASES = [
    "Dataset-Specific Assessment",
    "Inline Figures",
    "Label Composition",
    "Cluster Consensus Evidence",
]
REQUIRED_TOPIC_PATTERNS = [
    re.compile(r"source|annotation source", re.IGNORECASE),
    re.compile(r"marker expression", re.IGNORECASE),
    re.compile(r"subcluster|lineage", re.IGNORECASE),
]

parser = argparse.ArgumentParser(description="Validate committed HIPC report bundle before release.")
parser.add_argument("--report-root", default="reports/current")
parser.add_argument("--min-images-per-study", type=int, default=8)
args = parser.parse_args()

root = Path(args.report_root)
errors = []
if not root.exists():
    errors.append(f"Missing report root: {root}")

summary_required = [
    root / "summary/report_en.md",
    root / "summary/report_ja.md",
    root / "summary/tables/final_annotation_summary.tsv",
    root / "summary/tables/final_annotation_label_counts.tsv",
    root / "summary/tables/cluster_consensus_decisions.tsv",
]
for path in summary_required:
    if not path.exists():
        errors.append(f"Missing summary file: {path}")

inline_link_total = 0
png_total = 0
for study in EXPECTED_STUDIES:
    study_dir = root / study
    if not study_dir.exists():
        errors.append(f"Missing study directory: {study_dir}")
        continue

    for required in [study_dir / "tables/label_counts.tsv", study_dir / "tables/cluster_consensus_decisions.tsv"]:
        if not required.exists():
            errors.append(f"Missing table for {study}: {required}")

    pngs = sorted((study_dir / "assets").glob("*.png"))
    png_total += len(pngs)
    if len(pngs) < args.min_images_per_study:
        errors.append(f"Too few PNG assets for {study}: {len(pngs)} < {args.min_images_per_study}")

    for lang in ["en", "ja"]:
        report = study_dir / f"report_{lang}.md"
        if not report.exists():
            errors.append(f"Missing report for {study}: {report}")
            continue
        text = report.read_text()
        links = re.findall(r"!\[[^\]]*\]\(([^)]+)\)", text)
        inline_link_total += len(links)
        if not links:
            errors.append(f"No inline image links in {report}")
        for link in links:
            if not (report.parent / link).exists():
                errors.append(f"Broken image link in {report}: {link}")
        for phrase in REQUIRED_PHRASES:
            if phrase not in text:
                errors.append(f"Missing required section in {report}: {phrase}")
        for pattern in REQUIRED_TOPIC_PATTERNS:
            if not pattern.search(text):
                errors.append(f"Missing required report topic in {report}: {pattern.pattern}")
        for forbidden in FORBIDDEN_PATTERNS:
            if forbidden in text:
                errors.append(f"Forbidden old-version string in {report}: {forbidden}")

for path in root.rglob("*.md"):
    text = path.read_text()
    for forbidden in FORBIDDEN_PATTERNS:
        if forbidden in text:
            errors.append(f"Forbidden old-version string in {path}: {forbidden}")

print(f"report_root={root}")
print(f"expected_studies={len(EXPECTED_STUDIES)}")
print(f"png_files={png_total}")
print(f"inline_image_links={inline_link_total}")
print(f"errors={len(errors)}")
if errors:
    for err in errors:
        print(f"ERROR: {err}")
    raise SystemExit(1)
print("report bundle validation passed")
