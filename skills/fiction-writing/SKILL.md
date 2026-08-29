# Skill: Pre-Generation Canon Guard

**Type:** standalone, model-agnostic, project-specialized canon-protection ecosystem (pre-generation gate + locked contract + post-generation verification).
**Host location:** `skills/fiction-writing/` (this directory is the complete skill package).
**Objective:** resolve the *current* applicable canon from the *current* state of this project's branches, verify the request **before** generation, emit a **locked** Generation Contract, then verify generated claims **after** generation against that same Canon State. Either layer may block. Neither admits material to `02-canon/`.
**Non-objective (explicit):** storing a copy of the world's facts; freezing today's canon; auto-merging Arena Splash into `main`; dismissing Splash as non-canon; promoting drafts to canon; generating prose; reducing AI fictional tells; replacing the Canon Guard concept with a generic writing framework.

Ecosystem map: [`ECOSYSTEM.md`](ECOSYSTEM.md). Trust: [`TRUST.md`](TRUST.md). Severity: [`SEVERITY.md`](SEVERITY.md).

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
GENERATION CONTRACT (locked)
        ↓
GENERATION
        ↓
POST-GENERATION CANON VERIFICATION
        ↓
NEW MATERIAL (still proposed)
        ↓
CANON ADMISSION / BRANCH UPDATE
        ↓
NEXT CANON RESOLUTION
```

A PASS means: *this request is consistent with established canon on `main` and with the author's current working direction where that direction is sufficiently supported.*

A PASS does **not** mean: *this request will always be canonically valid.* It also does not mean Arena drafts are now canon.

---

## 2. Binding rules

1. **Branches are the authority.** Never treat a derived index, a previous verification, a Generation Contract, `WORLD-MODEL.md`, or this skill's own text as a substitute for the current branch contents.
2. **Re-resolve every time.** Before every generation request, perform the full guard process again. A prior PASS is not reusable.
3. **Do not freeze canon.** This skill must not hard-code current branch facts (names, dates, reigns, alliances, locations, deaths, knowledge). It defines *how* to derive current facts from evolving sources.
4. **Do not duplicate the world.** Provenance points at sources. The source remains the source.
5. **Do not invent branch certainty.** Classify branches from evidence in the repository (charter, directory layout, recovery tags, merge history). If the role of a branch is ambiguous, surface the ambiguity.
6. **`main` is the established canonical baseline. Arena (`arena/*`) is the current working / authoring state.** Consult Arena aggressively for current direction. Do not treat working-branch membership as established canon. Do not ignore Arena. Do not auto-merge. Classify content against `main`. A request does not PASS merely by not contradicting `main`. Differing from Arena is not automatically a BLOCK. See [`BRANCH_RELATIONSHIP.md`](BRANCH_RELATIONSHIP.md).
7. **Separate repository time from story time.** A newly written document can describe an earlier fictional period. A later-repo fact does not automatically apply to an earlier story-time generation.
8. **Separate establishment from in-world knowledge.** When a source later records that an entity learned something, that does not grant the entity the knowledge in earlier story periods.
9. **Generated material is proposed until admitted.** Drafts, pilots, quality reports, and chat output are not canon.
10. **Do not modify fictional canon by implementing or running this skill.** The skill reads sources and emits decisions. Admission is a separate, explicit protocol.
11. **Model-agnostic.** No LLM vendor, API, agent framework, memory provider, or programming language is required. The skill is portable inputs, operations, and outputs.
12. **Conservative under uncertainty.** If the current branch state does not provide enough reliable information to determine validity, the decision is `REQUIRES_CLARIFICATION`, not a guessed PASS.
13. **Locked contract.** The generator must not add, drop, or relabel constraints. Mutation is `CX-BYPASS`.
14. **Post-generation is a second layer.** A pre-generation PASS does not waive it. Post-generation PASS does not admit the text. Skipping pre-generation is `CX-BYPASS`.

---

## 3. What the skill is and is not for

**For:**
- Pre-generation verification of narrative requests (when the applicable branch authorizes narrative).
- Pre-generation verification of worldbuilding / canon-expansion requests.
- Post-generation verification of structured output against the **same** locked contract and Canon State.
- Detection of contradiction, ambiguity, stale derived state, continuity breaks, bypass, and unauthorized canon contamination.
- Production of an auditable decision and a state-bound, **locked** Generation Contract (hard / soft / direction / provisional / forbidden).
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
| **PASS** | Consistent with established `main` canon **and** current Arena working direction (or none relevant). |
| **PASS_WITH_WARNINGS** | Safe vs `main`, but diverges from / ignores strong or provisional Arena development, or uses working material that is not established. |
| **REQUIRES_CLARIFICATION** | Uninspected Arena, unresolved overlap, or competing Arena directions. Guessing would be unsafe. |
| **BLOCK** | Materially violates established `main` canon, a live charter constraint, or would contaminate canon. Differing from Arena is not by itself a BLOCK. |
| **CANON_CHANGE_REQUIRED** | The user explicitly wants an outcome that requires changing established canon (including an Arena retcon proposal they want to establish). Follow [`CANON_CHANGE_PROTOCOL.md`](CANON_CHANGE_PROTOCOL.md). |

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
15. **Produce a Generation Contract** if generation is permitted ([`GENERATION_CONTRACT.md`](GENERATION_CONTRACT.md)). The contract is valid only for the evaluated canon state. It is **locked**. It must separate **ESTABLISHED_CANON** (`main`) from **CURRENT_WORKING_DEVELOPMENT**, **CANON_CLARIFICATIONS**, **AUTHORIAL_DIRECTION**, **PROVISIONAL**, **CONFLICTS**, and **OPEN_QUESTIONS**, and expose **HARD_CONSTRAINTS** / **SOFT_CONTEXT** / **CURRENT_AUTHORIAL_DIRECTION** / **PROVISIONAL_MATERIAL** / **FORBIDDEN_ASSUMPTIONS**.
16. **After generation, run post-generation verification** (`post_verify`) on structured claims from the output, using the same contract identity. Stale contracts are not honored. See [`layers/post-generation.md`](layers/post-generation.md).

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
- [`ECOSYSTEM.md`](ECOSYSTEM.md), [`TRUST.md`](TRUST.md), [`SEVERITY.md`](SEVERITY.md), [`ESCALATION.md`](ESCALATION.md)

Progressively load: conflict taxonomy, change protocol, admission protocol, invalidation spec, branch-awareness spec, branch-relationship spec, schemas.

**Never** load the current contents of `samur/02-canon/` *into the skill package*. Load them at verification time from the applicable branch.

The host must also have access to the project's Git refs (or an equivalent snapshot of branch contents). Without current branch access, the skill cannot run.

---

## 7. Interfaces

Portable functions (any language, any model):

```
resolve_branches(repo)              -> BranchContext
resolve_canon(branch_context, req)  -> CanonState
classify_splash(main_state, splash) -> SplashClassification[]
verify(request, canon_state)        -> VerificationReport
decide(report)                      -> Decision
contract(request, state, report)    -> GenerationContract | null  # locked
post_verify(output, contract, state)-> VerificationReport         # second layer; never admits
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
| **This skill** | `skills/fiction-writing/` | Before generation **and** after (canon verification of output; not tell reduction) |
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

Every verification identifies the canon state it evaluated. Minimum audit record: generation request, applicable branch context, canon state/version (commits + content hashes), layer (`pre_generation` / `post_generation`), relevant sources, constraints extracted, checks performed, findings (with severity band), decision, Generation Contract id / lock hash (if any), timestamp. Schema: [`schemas/verification-report.schema.json`](schemas/verification-report.schema.json). Post-generation reports bind the same `canon_state_id` and `contract_id`. Historical PASSes are not patched in place.
