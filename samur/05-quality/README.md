# `05-quality/` — Narrative Quality Analysis

This directory holds all reports, outputs, and records produced by narrative-quality analysis tools — the `ai-fictional-tells-skill` post-generation pipeline, the pre-flight canon guard, and any future narrative-quality analysis.

## Purpose

Every narrative draft in `samur/narrative/` is subject to quality analysis. The analysis outputs live here, **never** in the narrative folder. This separation ensures:

- The narrative folder contains only clean prose — the reader-facing artifact.
- The quality folder contains the analytical substrate — the detection reports, intervention logs, preservation checks, and rejected-edit records.
- Provenance is auditable: each report is versioned with the draft it revised.

## Contents

| File | What it is |
|---|---|
| `skill-report-pilot.md` | The `ai-fictional-tells-skill` v1.0.0 post-generation AnalysisReport + InterventionLog for the pilot chapter. 13 findings, 17 applied edits, 4 rejected edits, 14 preservation dimensions verified. |

## Naming convention

`<tool>-report-<target>.md` — e.g., `skill-report-pilot.md`, `skill-report-ch01.md`, `canon-guard-report-ch01.md`.

## Governance

- Reports are **not canon**. They are analytical outputs that inform revision of narrative drafts.
- Reports do not modify `02-canon/`. The skill is canon-agnostic (it does not validate canon-compliance); the pre-flight canon guard is tell-agnostic (it does not run the tell pipeline).
- Each report is persisted alongside the draft it revised and recorded in `CHANGELOG.md`.
- The `ai-fictional-tells-skill` itself lives at `ai-fictional-tells-skill/` (the distributable skill folder on `main`). The pre-generation canon guard lives at `skills/fiction-writing/`. Integration is documented at `skills/INTEGRATION.md`.
