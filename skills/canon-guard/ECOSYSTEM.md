# Canon Guard ecosystem

This package is not a single prompt. It is a **canon-protection ecosystem**: cooperating guardrails around the whole writing lifecycle. It builds on the existing Canon Guard. It does not replace it.

There is **no skill named Fishnet** in this repository. The in-repo analog for ecosystem *design* is [`ai-fictional-tells-skill/`](../../ai-fictional-tells-skill/SKILL.md) (binding contract, independent stages, evidence-before-action, preservation over zeal, failure-mode catalog, adversarial tests, pipeline invariants, generator independence). Those properties transfer. Tell detection, intervention levels, and detector scores **do not**.

---

## 1. What transfers (and what does not)

| Tell-skill / Fishnet-style property | Transfer to Canon Guard? |
|---|---|
| Defense in depth; no single LLM judgment | **Yes** — staged extract → resolve → classify → conflict → dependency → decide |
| Evidence before action | **Yes** — every finding cites branch + path + hash |
| Preservation over polish | **Yes** — do not block legitimate expansion; do not freeze Arena |
| Failure-mode catalog with countermeasures | **Yes** — [`spec/07-failure-modes.md`](spec/07-failure-modes.md) |
| Pipeline invariants | **Yes** — [`spec/02-pipeline.md`](spec/02-pipeline.md), [`spec/08-lifecycle.md`](spec/08-lifecycle.md) |
| Generator cannot redefine the rules it obeys | **Yes** — contract is upstream and locked |
| Post-pass re-evaluation | **Yes** — post-generation verification is a *second* layer, not a substitute |
| Adversarial tests for false accept *and* false reject | **Yes** |
| Minimal vs advanced hosting | **Yes** — [`spec/11-minimal-architecture.md`](spec/11-minimal-architecture.md) |
| Tell taxonomy / prose intervention levels | **No** |
| Detector scores | **No** |
| Editing the draft to reduce artifacts | **No** — that remains the tell skill, after this ecosystem |

---

## 2. Binding model (unchanged)

```
main     = established canonical baseline
Arena    = current working / authoring state
Arena content = canon-relevant working material
                classified against main; not automatic canon; not irrelevant
```

Do not freeze either branch. Do not copy `samur/02-canon/` into this package. Do not create a duplicate canon repository.

---

## 3. Lifecycle

```
SOURCE BRANCHES (main + Arena)
        ↓
CANON OBSERVATION
        ↓
CANON RESOLUTION
        ↓
CANON CLASSIFICATION
        ↓
DEPENDENCY MODEL
        ↓
GENERATION REQUEST ANALYSIS          ← untrusted proposal
        ↓
PRE-GENERATION CANON GUARD
        ↓
GENERATION CONTRACT (locked)
        ↓
GENERATION                           ← untrusted until verified
        ↓
POST-GENERATION CANON VERIFICATION
        ↓
CANON ADMISSION / REJECTION
        ↓
UPDATED BRANCH STATE
        ↓
CANON RE-RESOLUTION
```

Pre-generation and post-generation are **separate layers**. Post-generation never replaces the gate.

---

## 4. Components (purpose → home)

Every component exists because a real failure mode needs it. Details live in the cited file, not as a second copy of the world.

| # | Component | Purpose | Home |
|---|---|---|---|
| 1 | Canon resolution | Current applicable canon from `main` + relevant Arena | [`CANON_RESOLUTION.md`](CANON_RESOLUTION.md) |
| 2 | Branch intelligence | Roles, evolution, meaningful change | [`BRANCH_RELATIONSHIP.md`](BRANCH_RELATIONSHIP.md), [`spec/04-branch-awareness.md`](spec/04-branch-awareness.md) |
| 3 | Classification | Established / clarification / extension / direction / provisional / exploratory / contradiction / retcon / abandoned / unresolved | [`BRANCH_RELATIONSHIP.md`](BRANCH_RELATIONSHIP.md) §5 |
| 4 | Constraint extraction | Request-relevant constraints with provenance | [`CANON_MODEL.md`](CANON_MODEL.md), engine |
| 5 | Pre-generation verification | Gate the request | [`DECISION_PROTOCOL.md`](DECISION_PROTOCOL.md) |
| 6 | Dependency analysis | Indirect / downstream | [`spec/03-invalidation.md`](spec/03-invalidation.md) |
| 7 | Temporal guard | Chronology, era, order | `CX-TEMPORAL` |
| 8 | Knowledge-state guard | Who may know what | `CX-KNOWLEDGE` |
| 9 | Continuity guard | States across chapters / drafts | [`layers/continuity.md`](layers/continuity.md) |
| 10 | Contradiction engine | Direct, indirect, causal, … | [`CONFLICT_TAXONOMY.md`](CONFLICT_TAXONOMY.md) |
| 11 | Ambiguity guard | Not enough reliable information | `CX-AMBIGUITY` |
| 12 | Canon-change guard | Intentional change, not silent overwrite | [`CANON_CHANGE_PROTOCOL.md`](CANON_CHANGE_PROTOCOL.md) |
| 13 | Admission guard | Generated text is not canon | [`CANON_ADMISSION_PROTOCOL.md`](CANON_ADMISSION_PROTOCOL.md) |
| 14 | Stale-state detection | Contracts die when hashes move | [`spec/03-invalidation.md`](spec/03-invalidation.md) |
| 15 | Divergence detection | `main` vs Arena, classified not auto-error | [`BRANCH_RELATIONSHIP.md`](BRANCH_RELATIONSHIP.md) |
| 16 | Contract generator | Hard / soft / direction / provisional / forbidden | [`GENERATION_CONTRACT.md`](GENERATION_CONTRACT.md) |
| 17 | Post-generation verification | Did the output obey *this* contract? | [`layers/post-generation.md`](layers/post-generation.md) |
| 18 | Contamination detection | Draft presented as established canon | [`layers/contamination.md`](layers/contamination.md) |
| 19 | Audit | Why valid / warning / block | [`layers/audit.md`](layers/audit.md) |
| 20 | Recovery and escalation | Proceed / warn / clarify / block / change / human | [`ESCALATION.md`](ESCALATION.md) |

Trust: [`TRUST.md`](TRUST.md). Severity: [`SEVERITY.md`](SEVERITY.md). Failure modes: [`spec/07-failure-modes.md`](spec/07-failure-modes.md).

---

## 5. Independent stages (no single judgment)

```
REQUEST EXTRACTION        untrusted
    → CONSTRAINT EXTRACTION    from sources, provenance required
    → SOURCE RESOLUTION        main baseline + classified Arena
    → CONFLICT ANALYSIS        typed CX-* findings
    → DEPENDENCY ANALYSIS      dependents, precludes, invalidation scope
    → DECISION                 DECISION_PROTOCOL only
```

The generator does not run these stages. It receives a **locked** contract. It cannot add, drop, or relabel constraints.

---

## 6. Hosting

- **Minimal:** structured claims + [`reference/canon_guard.py`](reference/canon_guard.py) ([`spec/11-minimal-architecture.md`](spec/11-minimal-architecture.md)).
- **Full:** live git resolution + optional LLM extraction validated by the deterministic core ([`spec/12-advanced-architecture.md`](spec/12-advanced-architecture.md)).

Either way the verdict is code, not a second model vote.

---

## 7. Principle

Protect established canon. Stay synchronized with the author's current working storyline. Prevent accidental, unsupported, or contradictory change. Allow deliberate creative evolution.
