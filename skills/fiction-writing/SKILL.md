# Skill: Pre-Generation Canon Guard

**Type:** standalone, model-agnostic, project-specialized, pre-generation skill.
**Host location:** `skills/fiction-writing/` (this directory is the complete skill package).
**Objective:** before any generation begins, resolve the *current* applicable canon from the *current* state of this project's branches, verify the request against that state, and either block generation or emit a Generation Contract bound to that state.
**Non-objective (explicit):** storing a copy of the world's facts; freezing today's canon; auto-merging Arena Splash into `main`; dismissing Splash as non-canon; promoting drafts to canon; generating prose; reducing AI fictional tells.

This file is the binding skill contract. Mechanism details live in the sibling documents listed in [`README.md`](README.md).

---

## 1. Core principle

The repository branches are living canonical sources.

The Canon Guard is the enforcement layer.

The generation system is downstream.

The canon is not static.

```
CURRENT BRANCH STATE
        ↓
CANON RESOLUTION
        ↓
GENERATION REQUEST
        ↓
RELEVANT CANON RESOLUTION
        ↓
CONSTRAINT EXTRACTION
        ↓
CONSISTENCY VERIFICATION
        ↓
DECISION
        ↓
GENERATION CONTRACT
        ↓
GENERATION
        ↓
NEW MATERIAL
        ↓
CANON ADMISSION / BRANCH UPDATE
        ↓
NEXT CANON RESOLUTION
```

A PASS means: *this request is compatible with the applicable canon state evaluated at this point.*

A PASS does **not** mean: *this request will always be canonically valid.*

---

## 2. Binding rules

1. **Branches are the authority.** Never treat a derived index, a previous verification, a Generation Contract, `WORLD-MODEL.md`, or this skill's own text as a substitute for the current branch contents.
2. **Re-resolve every time.** Before every generation request, perform the full guard process again. A prior PASS is not reusable.
3. **Do not freeze canon.** This skill must not hard-code current branch facts (names, dates, reigns, alliances, locations, deaths, knowledge). It defines *how* to derive current facts from evolving sources.
4. **Do not duplicate the world.** Provenance points at sources. The source remains the source.
5. **Do not invent branch certainty.** Classify branches from evidence in the repository (charter, directory layout, recovery tags, merge history). If the role of a branch is ambiguous, surface the ambiguity.
6. **Main is the default canonical baseline. Arena Splash (`arena/*`) is not automatically canon, not an independent timeline, and not irrelevant.** Classify Splash content against current `main`. Do not auto-merge. Do not ignore. Do not treat all Splash equally. Newer Splash does not override `main`. See [`BRANCH_RELATIONSHIP.md`](BRANCH_RELATIONSHIP.md).
7. **Separate repository time from story time.** A newly written document can describe an earlier fictional period. A later-repo fact does not automatically apply to an earlier story-time generation.
8. **Separate establishment from in-world knowledge.** When a source later records that an entity learned something, that does not grant the entity the knowledge in earlier story periods.
9. **Generated material is proposed until admitted.** Drafts, pilots, quality reports, and chat output are not canon.
10. **Do not modify fictional canon by implementing or running this skill.** The skill reads sources and emits decisions. Admission is a separate, explicit protocol.
11. **Model-agnostic.** No LLM vendor, API, agent framework, memory provider, or programming language is required. The skill is portable inputs, operations, and outputs.
12. **Conservative under uncertainty.** If the current branch state does not provide enough reliable information to determine validity, the decision is `REQUIRES_CLARIFICATION`, not a guessed PASS.

---

## 3. What the skill is and is not for

**For:**
- Pre-generation verification of narrative requests (when the applicable branch authorizes narrative).
- Pre-generation verification of worldbuilding / canon-expansion requests.
- Detection of contradiction, ambiguity, stale derived state, and unauthorized canon contamination.
- Production of an auditable decision and a state-bound Generation Contract.
- Invalidation of derived state after source changes.

**Not for:**
- Writing chapters, scenes, or lore.
- Post-generation tell reduction (that is `ai-fictional-tells-skill`).
- Replacing `samur/02-canon/` with an extracted factbase.
- Treating `recovery/*` tags as live canon.
- Silently rewriting established facts because a generation request wants them changed.

---

## 4. Decision vocabulary

| Decision | Meaning |
|---|---|
| **PASS** | Compatible with the applicable canon state evaluated now. Generation may proceed under the emitted contract. |
| **PASS_WITH_WARNINGS** | Compatible, but the contract records uncertainties, permitted-but-unadmitted fill, or non-blocking issues. |
| **REQUIRES_CLARIFICATION** | The current branch state (or branch selection) is insufficient or ambiguous; guessing would be unsafe. |
| **BLOCK** | The request conflicts with currently applicable canon, violates a live branch constraint, or would contaminate canon. |
| **CANON_CHANGE_REQUIRED** | The user explicitly wants an outcome that requires changing established canon. Do not silently overwrite. Follow [`CANON_CHANGE_PROTOCOL.md`](CANON_CHANGE_PROTOCOL.md). |

---

## 5. Operating procedure (normative)

Full pipeline: [`spec/02-pipeline.md`](spec/02-pipeline.md). Every generation request, without exception:

1. **Identify the applicable current branch state.** Discover live refs. `main` is the default canonical baseline. If Arena Splash (`arena/*`) is live, inspect it — do not skip it, do not auto-merge it. Record head commits. See [`BRANCH_RELATIONSHIP.md`](BRANCH_RELATIONSHIP.md), [`spec/04-branch-awareness.md`](spec/04-branch-awareness.md), and [`CANON_RESOLUTION.md`](CANON_RESOLUTION.md).
2. **Resolve relevant current canon.** From `main` at those commits, inventory living sources by *status and location*, not by a frozen file list. Then classify relevant Splash material against that baseline. Select the relevant subset for this request. See [`CANON_MODEL.md`](CANON_MODEL.md).
3. **Analyze the generation request.** Kind, story-time, viewpoint, implied claims, named entities, proposed new facts, whether a canon change is explicit.
4. **Extract implied constraints.** Bind each constraint to provenance: fact → branch → document → location → version/state.
5. **Identify dependencies.** Use the project's own `Depends on` / `Dependents` / `High-impact` fields when present. Walk the live graph.
6. **Check direct consistency.** Claim vs. currently applicable CANON facts at the requested story-time.
7. **Check indirect consistency.** Consequences, dependents, negative space, summaries that disagree with their source files.
8. **Check temporal consistency.** Story chronology vs. repository chronology. Era-bounded facts. Exact dates vs. ranges vs. orders (this project uses more than one dating epistemology; re-read the current chronology sources to learn which).
9. **Check knowledge-state consistency.** In-world knowledge vs. author-level truth. Learning events do not apply retroactively.
10. **Check causal consistency.** Causes, actors, effects, second-order consequences as currently recorded.
11. **Check branch-specific constraints.** Charter authorization (Splash charter only when continuing a Splash storyline), directory separation, recovery-tag exclusion. Splash classifications are not a second canon.
12. **Detect ambiguity.** Missing facts, unresolved Splash overlapping the request, register-vs-file disagreement, WORLD-MODEL-vs-canon-file disagreement (canon file wins; the disagreement is still a finding). Extra `arena/*` heads are classified, not treated as automatic `REQUIRES_CLARIFICATION`.
13. **Detect unresolved conflicts.** Live entries in the contradictions register; unresolved high-impact disagreements.
14. **Produce a decision** from [`DECISION_PROTOCOL.md`](DECISION_PROTOCOL.md).
15. **Produce a Generation Contract** if generation is permitted ([`GENERATION_CONTRACT.md`](GENERATION_CONTRACT.md)). The contract is valid only for the evaluated canon state. Constraints must be labeled by **source status** (CANONICAL / CANON CLARIFICATION / AUTHORIAL INTENT / PROPOSED / CONFLICT).

---

## 6. Knowledge base (what a host must load)

Minimum viable load:

- This file (`SKILL.md`)
- [`CANON_MODEL.md`](CANON_MODEL.md)
- [`CANON_RESOLUTION.md`](CANON_RESOLUTION.md)
- [`BRANCH_RELATIONSHIP.md`](BRANCH_RELATIONSHIP.md)
- [`DECISION_PROTOCOL.md`](DECISION_PROTOCOL.md)
- [`GENERATION_CONTRACT.md`](GENERATION_CONTRACT.md)
- [`spec/02-pipeline.md`](spec/02-pipeline.md)
- [`spec/05-project-specialization.md`](spec/05-project-specialization.md)

Progressively load: conflict taxonomy, change protocol, admission protocol, invalidation spec, branch-awareness spec, branch-relationship spec, schemas.

**Never** load the current contents of `samur/02-canon/` *into the skill package*. Load them at verification time from the applicable branch.

The host must also have access to the project's Git refs (or an equivalent snapshot of branch contents). Without current branch access, the skill cannot run.

---

## 7. Interfaces

Portable functions (any language, any model):

```
resolve_branches(repo)              -> BranchContext
resolve_canon(branch_context, req)  -> CanonState
verify(request, canon_state)        -> VerificationReport
decide(report)                      -> Decision
contract(request, state, report)    -> GenerationContract | null
detect_changes(prev_state, next)    -> ChangeSet
invalidate(derived, change_set)     -> DerivedState
admit(proposal, workflow)           -> AdmissionRecord   # never implicit
```

JSON schemas: [`schemas/`](schemas/). Prompt contracts for LLM-hosted extraction: [`spec/01-interfaces.md`](spec/01-interfaces.md).

A small deterministic reference core (structured states only) lives in [`reference/canon_guard.py`](reference/canon_guard.py) so the adaptive property can be tested without a model.

---

## 8. Relationship to other layers

| Layer | Path | When |
|---|---|---|
| **This skill** | `skills/fiction-writing/` | Before generation |
| Prose anti-patterns (draft rules, preserved) | [`anti-patterns.md`](anti-patterns.md) | During narrative generation, if authorized |
| Post-generation tell reduction | `ai-fictional-tells-skill/` (root on `main`; may move under `skills/` on other branches — resolve live) | After a draft exists |
| Integration record | `skills/INTEGRATION.md` | Host wiring |

This skill is **canon-aware and tell-agnostic**. It does not run the tell pipeline. The tell skill is **canon-agnostic and tell-aware**. Neither modifies `samur/02-canon/`.

---

## 9. Adaptive property (non-optional)

The skill must change its conclusions when the underlying canon changes. Required demonstrations live in [`tests/01-adaptive-suite.md`](tests/01-adaptive-suite.md). Structural tests must not be limited to static contradictions.

When sources change:

```
Source → Detect Change → Invalidate Affected Derived State
      → Re-index / Re-resolve → Update Constraints
      → Use New State for Future Verification
```

---

## 10. Auditability

Every verification identifies the canon state it evaluated. Minimum audit record: generation request, applicable branch context, canon state/version (commits + content hashes), relevant sources, constraints extracted, checks performed, findings, decision, Generation Contract (if any), timestamp. Schema: [`schemas/verification-report.schema.json`](schemas/verification-report.schema.json).
