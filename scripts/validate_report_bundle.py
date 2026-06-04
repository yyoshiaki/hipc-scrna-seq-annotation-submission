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
REQUIRED_PHRASES_EN = [
    "Dataset-Specific Assessment",
    "Inline Figures",
    "Label Composition",
    "Cluster Consensus Evidence",
    "Subcluster Marker Score Review",
    "true subcluster",
]
REQUIRED_PHRASES_JA = [
    "データセット固有の評価",
    "Inline Figures",
    "ラベル構成",
    "Cluster Consensus Evidence",
    "Subcluster Marker Score Review",
    "true subcluster",
]
REQUIRED_TOPIC_PATTERNS = [
    re.compile(r"source|annotation source", re.IGNORECASE),
    re.compile(r"marker expression", re.IGNORECASE),
    re.compile(r"subcluster|lineage", re.IGNORECASE),
]

parser = argparse.ArgumentParser(description="Validate committed HIPC report bundle before release.")
parser.add_argument("--report-root", default="reports/current")
parser.add_argument("--min-images-per-study", type=int, default=23)
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
    root / "summary/tables/lineage_subcluster_evidence.tsv.gz",
    root / "summary/tables/source_disagreement_summary.tsv",
    root / "summary/tables/lineage_panel_status.tsv",
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

    required_tables = [
        study_dir / "tables/final_annotation_label_counts.tsv",
        study_dir / "tables/final_annotation_summary.tsv",
        study_dir / "tables/lineage_subcluster_evidence.tsv.gz",
        study_dir / "tables/source_disagreement_summary.tsv",
        study_dir / "tables/subcluster_candidate_scores.tsv",
        study_dir / "tables/lineage_panel_status.tsv",
    ]
    for lineage in ["B_lineage", "T_NK_lineage", "Myeloid_lineage"]:
        required_tables.extend(
            [
                study_dir / f"tables/{study}_{lineage}_true_subcluster_umap.tsv.gz",
                study_dir / f"tables/{study}_{lineage}_subcluster_candidate_scores.tsv",
            ]
        )
    for required in required_tables:
        if not required.exists():
            errors.append(f"Missing table for {study}: {required}")

    panel_status_path = study_dir / "tables/lineage_panel_status.tsv"
    if panel_status_path.exists():
        panel_status = {}
        for row in panel_status_path.read_text().splitlines()[1:]:
            fields = row.split("\t")
            if len(fields) >= 4:
                panel_status[fields[1]] = fields[3]
    else:
        panel_status = {}

    for lineage in ["B_lineage", "T_NK_lineage", "Myeloid_lineage"]:
        required_pngs = [
            study_dir / "assets" / f"umap_{study}_{lineage}_true_subcluster_label.png",
            study_dir / "assets" / f"umap_{study}_{lineage}_true_subcluster_qc.png",
            study_dir / "assets" / f"umap_{study}_{lineage}_true_subcluster_marker_scores.png",
            study_dir / "assets" / f"umap_{study}_{lineage}_true_subcluster_marker_expression.png",
            study_dir / "assets" / f"subcluster_marker_score_heatmap_{study}_{lineage}.png",
            study_dir / "assets" / f"dotplot_{study}_{lineage}_true_subcluster_marker_dotplot.png",
        ]
        if panel_status.get(lineage) != "generated":
            if lineage not in panel_status:
                errors.append(f"Missing lineage panel status for {study}: {lineage}")
            continue
        for required_png in required_pngs:
            if not required_png.exists():
                errors.append(f"Missing true subcluster marker plot for {study}: {required_png}")

    pngs = sorted((study_dir / "assets").glob("*.png"))
    png_total += len(pngs)
    generated_lineage_n = sum(1 for value in panel_status.values() if value == "generated")
    min_images = 7 + (generated_lineage_n * 6)
    if len(pngs) < min_images:
        errors.append(f"Too few PNG assets for {study}: {len(pngs)} < {min_images}")

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
        required_phrases = REQUIRED_PHRASES_JA if lang == "ja" else REQUIRED_PHRASES_EN
        for phrase in required_phrases:
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
