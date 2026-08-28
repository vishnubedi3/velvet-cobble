# `ops/` — Operational Records

This directory contains operational records: agent logs, recovery point documentation, and other records of project activity that are not canon, not research, not narrative prose, and not quality analysis.

## Contents

| Directory | What it contains |
|---|---|
| `logs/` | Agent operation logs — concise records of meaningful actions (what was done, what was affected, what was verified, what recovery point was created). Named `<YYYY-MM-DD>-<operation>.md`. |
| `recovery/` | Recovery point documentation — records of recovery points created (git tags), what they protect, and any recovery operations performed. |

## Purpose

Operational records exist to make the project's development history understandable without mixing historical records with current canon. They provide:

- **Auditability:** every consequential action is recorded with its recovery point.
- **Traceability:** the chain of operations that produced the current state is preserved.
- **Separation:** operational records do not contaminate canon, research, or narrative folders.

## Rules

- Logs are concise. Record the action, the area affected, the result, the verification, and the recovery point. Do not reproduce hidden chain-of-thought. Do not reproduce the AGENTS.md directive text.
- Recovery points are annotated git tags (`recovery/<operation-name>`). The `ops/recovery/` directory documents them in human-readable form for quick reference.
- Operational records are never canon, never narrative prose, never research.
- Failed operations are recorded, not concealed.

## Relationship to Other Directories

- `samur/CHANGELOG.md` — the canon change log (records canon-level changes with dependency tracking)
- `samur/00-audit/` — repository and workspace audits (run before major lore work)
- `AGENTS.md` §2.3 — the recovery point discipline
- `AGENTS.md` §10 — the agent logging requirements
