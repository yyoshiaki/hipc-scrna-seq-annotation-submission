# scRefMapping Reference Distribution

Updated: 2026-05-23 EDT

## Current state

The clean repository stores only the reference manifest path in `configs/screfmapping_references.tsv`. Large scRefMapping reference objects are not committed.

## Distribution requirement

For an external submission or reusable public workflow, scRefMapping references need a public, versioned download location. Do not rely on internal Yale paths or internal S3 mounts for external users.

## Recommended public targets

- Zenodo or Figshare for immutable DOI-versioned reference bundles.
- Hugging Face datasets for easier programmatic download if file size and licensing allow it.
- GitHub Releases only for small metadata files, not large reference matrices.

## Skill behavior

When scRefMapping is requested but reference files are unavailable, Codex should:

1. Continue the annotation using CellTypist, Azimuth/Pan-human, marker, QC, and clustering evidence.
2. Report that scRefMapping was unavailable rather than fabricating evidence.
3. Mark the run as limited by missing auxiliary references if B or CD4T fine adjudication would benefit from scRefMapping.
