# Changelog — Canon Guard skill package

Skill-package history. Not the world's changelog (`samur/CHANGELOG.md`).

## 1.2.0 — 2026-08-29

Ecosystem expansion of the existing Canon Guard (not a rebuild):

- Locked Generation Contract (`locked`, `lock_hash`) and hard/soft/direction/provisional/forbidden bands.
- `post_verify` second layer; never replaces the pre-generation gate; never admits.
- New finding classes: `CX-CONTAMINATION`, `CX-BYPASS`, `CX-CONTINUITY`; engine now emits `CX-STALE`, `CX-TEMPORAL`, `CX-RETIRED`.
- Severity bands on findings; trust / escalation docs.
- Adaptive A28–A30, A33 + adversarial A31–A37.
- Architectural audit: [`spec/13-architectural-audit.md`](spec/13-architectural-audit.md).

## 1.1.0 — 2026-08-28

Working-branch model: `main` = established canonical baseline; Arena = current working / authoring state. Classified, not merged.

## 1.0.0 — 2026-08-28

Initial Pre-Generation Canon Guard package.
