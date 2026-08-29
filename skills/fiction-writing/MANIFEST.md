# MANIFEST — Canon Guard package inventory

## Root

| File | Contents |
|---|---|
| [`README.md`](README.md) | Entry point |
| [`SKILL.md`](SKILL.md) | Binding contract |
| [`AGENTS.md`](AGENTS.md) | Hosting notes for agents |
| [`ARCHITECTURE.md`](ARCHITECTURE.md) | Layers, clocks, cache rules |
| [`CANON_MODEL.md`](CANON_MODEL.md) | Canon State |
| [`CANON_RESOLUTION.md`](CANON_RESOLUTION.md) | Live resolution procedure |
| [`BRANCH_RELATIONSHIP.md`](BRANCH_RELATIONSHIP.md) | Main vs Arena Splash: classify, don't merge, don't ignore |
| [`CONFLICT_TAXONOMY.md`](CONFLICT_TAXONOMY.md) | Finding classes |
| [`DECISION_PROTOCOL.md`](DECISION_PROTOCOL.md) | Decision table |
| [`GENERATION_CONTRACT.md`](GENERATION_CONTRACT.md) | Contract rules |
| [`CANON_CHANGE_PROTOCOL.md`](CANON_CHANGE_PROTOCOL.md) | Intentional change |
| [`CANON_ADMISSION_PROTOCOL.md`](CANON_ADMISSION_PROTOCOL.md) | Drafts are not canon |
| [`CONFIG.md`](CONFIG.md) | Parameters |
| [`glossary.md`](glossary.md) | Terminology |
| [`ECOSYSTEM.md`](ECOSYSTEM.md) | Lifecycle and cooperating layers |
| [`TRUST.md`](TRUST.md) | Trust boundaries |
| [`SEVERITY.md`](SEVERITY.md) | Finding bands |
| [`ESCALATION.md`](ESCALATION.md) | Proceed / warn / clarify / block / change |
| [`MANIFEST.md`](MANIFEST.md) | This file |
| [`STATUS.md`](STATUS.md) | Directory status (updated) |
| [`CHANGELOG.md`](CHANGELOG.md) | Skill-package versions |
| [`anti-patterns.md`](anti-patterns.md) | Preserved prose rules (not canon) |

## Spec

| File | Contents |
|---|---|
| [`spec/01-interfaces.md`](spec/01-interfaces.md) | Portable functions and prompt contracts |
| [`spec/02-pipeline.md`](spec/02-pipeline.md) | Stages and invariants |
| [`spec/03-invalidation.md`](spec/03-invalidation.md) | Local vs systemic invalidation |
| [`spec/04-branch-awareness.md`](spec/04-branch-awareness.md) | Observed ref roles |
| [`spec/05-project-specialization.md`](spec/05-project-specialization.md) | How to read this repo |
| [`spec/06-integration.md`](spec/06-integration.md) | Hook points |
| [`spec/07-failure-modes.md`](spec/07-failure-modes.md) | Generator/host failures |
| [`spec/08-lifecycle.md`](spec/08-lifecycle.md) | Lifecycle invariants |
| [`spec/09-evaluation.md`](spec/09-evaluation.md) | False accept / false reject |
| [`spec/11-minimal-architecture.md`](spec/11-minimal-architecture.md) | Host without an LLM |
| [`spec/12-advanced-architecture.md`](spec/12-advanced-architecture.md) | Optional LLM extraction |
| [`spec/13-architectural-audit.md`](spec/13-architectural-audit.md) | Weaknesses found and fixed |
| [`layers/`](layers/) | Continuity, post-generation, contamination, audit, constraint bands |

## Schemas

| File | Contents |
|---|---|
| [`schemas/generation-request.schema.json`](schemas/generation-request.schema.json) | Input |
| [`schemas/canon-state.schema.json`](schemas/canon-state.schema.json) | Evaluated state |
| [`schemas/verification-report.schema.json`](schemas/verification-report.schema.json) | Audit record |
| [`schemas/generation-contract.schema.json`](schemas/generation-contract.schema.json) | Contract |
| [`schemas/canon-change-proposal.schema.json`](schemas/canon-change-proposal.schema.json) | Change proposal |
| [`schemas/admission-record.schema.json`](schemas/admission-record.schema.json) | Admission |

## Reference, tests, examples, fixtures

| File | Contents |
|---|---|
| [`reference/canon_guard.py`](reference/canon_guard.py) | Deterministic core |
| [`tests/README.md`](tests/README.md) | How to run tests |
| [`tests/01-adaptive-suite.md`](tests/01-adaptive-suite.md) | Adaptive scenarios |
| [`tests/02-static-consistency-checklist.md`](tests/02-static-consistency-checklist.md) | Doc/schema checks |
| [`tests/03-decision-cases.md`](tests/03-decision-cases.md) | Extra project-mechanism cases |
| [`tests/04-adversarial-suite.md`](tests/04-adversarial-suite.md) | False-accept and false-reject cases |
| [`tests/run_adaptive_tests.py`](tests/run_adaptive_tests.py) | Runner |
| [`fixtures/README.md`](fixtures/README.md) | Synthetic worlds only |
| [`fixtures/adaptive/*.json`](fixtures/adaptive/) | T0/T1 scenario data |
| [`examples/01-worked-verification.md`](examples/01-worked-verification.md) | Worked mechanism demo |
