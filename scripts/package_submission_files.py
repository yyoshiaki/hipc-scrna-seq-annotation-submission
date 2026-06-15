#!/usr/bin/env python3
import argparse
import shutil
import zipfile
from pathlib import Path
import xml.sax.saxutils as sx

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
parser.add_argument("--github-link", default="https://github.com/yyoshiaki/hipc-scrna-seq-annotation-submission")
parser.add_argument("--replace", action="store_true")
args = parser.parse_args()

run_root = Path(args.run_root).resolve()
out = Path(args.out).resolve()
studies = [study.strip() for study in args.studies.split(",") if study.strip()]

if out.exists() and args.replace:
    shutil.rmtree(out)
out.mkdir(parents=True, exist_ok=True)

summary_rows = []
for study in studies:
    source = run_root / study / "submissions" / f"{study}_annotation.tsv"
    if not source.exists():
        raise SystemExit(f"Missing submission TSV: {source}")
    target = out / source.name
    shutil.copy2(source, target)
    table = pd.read_csv(target, sep="\t")
    required_cols = ["cell_barcode", "predicted_cell_type", "confidence_score"]
    missing = [col for col in required_cols if col not in table.columns]
    if missing:
        raise SystemExit(f"{target}: missing columns {missing}")
    summary_rows.append(
        {
            "study": study,
            "submission_tsv": target.name,
            "n_rows": int(table.shape[0]),
            "n_labels": int(table["predicted_cell_type"].nunique()),
            "median_confidence": float(table["confidence_score"].median()),
            "low_confidence_n": int(table["confidence_score"].lt(0.60).sum()),
        }
    )

summary = pd.DataFrame(summary_rows)
summary.to_csv(out / "submission_package_summary.tsv", sep="\t", index=False)
readme_lines = [
    "# HIPC Team04 submission package",
    "",
    "This package follows the organizer fake-submission structure: one annotation TSV per study plus a methodology DOCX.",
    "",
    f"GitHub repository: {args.github_link}",
    "",
    "Each TSV has `cell_barcode`, `predicted_cell_type`, and `confidence_score` columns.",
    "",
    "Excluded study: `infection_study_07` was not submitted because raw counts were not available in the current Team04 portal distribution.",
    "",
    "Known caveat: `vaccination_study_10` was submitted, but the current Team04 portal only exposed processed H5AD/RDS files with transformed non-integer matrices; no separate raw, unfiltered, or filtered raw count matrix was visible.",
    "",
    "## Files",
    "",
]
for row in summary.itertuples(index=False):
    readme_lines.append(f"- `{row.submission_tsv}`: {row.n_rows} rows, {row.n_labels} labels, median confidence {row.median_confidence:.3f}")
(out / "README.md").write_text("\n".join(readme_lines) + "\n", encoding="utf-8")
(out / "github_link.txt").write_text(args.github_link + "\n", encoding="utf-8")

method_text = [
    "HIPC scRNA-seq Annotation Benchmark - Team04 Approach Summary",
    "",
    f"GitHub repository: {args.github_link}",
    "",
    "Submission scope",
    "We submit annotations for nine Team04 datasets: infection_study_01, infection_study_03, infection_study_04, infection_study_06, vaccination_study_01, vaccination_study_04, vaccination_study_06, vaccination_study_09, and vaccination_study_10. infection_study_07 was excluded because raw counts were not available in the current organizer-provided Team04 directory.",
    "",
    "Method overview",
    "The annotation workflow combines ontology-constrained reference mapping, broad-lineage assignment, lineage-scoped reclustering, marker-registry scoring, QC/doublet evidence, and confidence calibration. CellTypist, Azimuth/Pan-human Azimuth, marker evidence, cluster consensus, and scRefMapping were used when the required input evidence was available. Final labels were constrained to the official ontology labels and validated against the submission barcode templates.",
    "",
    "Raw-count handling",
    "For datasets with raw-count-like unfiltered matrices, raw counts were used for raw-count-dependent evidence sources. vaccination_study_10 is a known exception: the current Team04 portal directory contains only processed H5AD/RDS files. The RDS RNA counts layer and H5AD matrices are transformed non-integer values, so raw-count-dependent evidence is not interpreted normally for this dataset.",
    "",
    "Validation",
    "Each per-study TSV contains cell_barcode, predicted_cell_type, and confidence_score columns. Row counts were validated against the corresponding dataset outputs, predicted labels were checked against the official ontology, and reports were generated for review.",
    "",
    "Manual intervention",
    "No per-cell manual labels were injected. Manual work was limited to ontology review, marker-registry curation, policy decisions for ambiguous/low-confidence evidence, and review of diagnostic reports.",
]

def paragraph(text):
    if not text:
        return "<w:p/>"
    escaped = sx.escape(text)
    return f'<w:p><w:r><w:t xml:space="preserve">{escaped}</w:t></w:r></w:p>'

document_xml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:body>
    %s
    <w:sectPr><w:pgSz w:w="12240" w:h="15840"/><w:pgMar w:top="1440" w:right="1440" w:bottom="1440" w:left="1440"/></w:sectPr>
  </w:body>
</w:document>
""" % "\n".join(paragraph(line) for line in method_text)
content_types = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
</Types>
"""
rels = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
</Relationships>
"""
with zipfile.ZipFile(out / "Team04_Pipeline_ApproachSummary.docx", "w", compression=zipfile.ZIP_DEFLATED) as zf:
    zf.writestr("[Content_Types].xml", content_types)
    zf.writestr("_rels/.rels", rels)
    zf.writestr("word/document.xml", document_xml)

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
