# 01 — Project Binding (Samur)

**Status:** binding. This document is what makes the skill **non-portable by
design.** It defines what the skill requires from this repository, which
authority its findings carry, and which rules win when rules conflict.

> **This skill exists to reduce AI tells in *Samur* narrative drafts.** It is
> not a general-purpose AI-writing detector, not a reusable fiction-polishing
> skill, and not a standalone implementation of any external anti-slop
> method. Removed from this repository it does not degrade gracefully — it
> refuses (§1). The methodology in `frameworks/`, `taxonomy/`, `spec/` is
> deliberately written against this project's canon, terminology, factions,
> name registers, and drafting constraints. A different fictional project
> would need to rewrite the binding, the project-tell catalog
> (`../taxonomy/19-project-tells.md`), and every project-coupled detector
> before any of it could work there.

## 1. The binding contract (Stage 0 enforces it)

Every run requires a **project context**, supplied in `SkillInput.project_context`
(`../spec/03-input-schema.md` §1.1) and validated at intake:

| Requirement | Source in this repository |
|---|---|
| The draft is a Samur narrative draft, produced under this project's narrative-stage pipeline | `PROJECT.md` §2 (the narrative stage and its gate) |
| A live **canon resolution** (the applicable branch state of `samur/02-canon/`), never a frozen snapshot | `skills/canon-guard/` (the guard re-resolves before every generation; this skill consumes the same resolution) |
| The **Generation Contract** under which the segment was produced (genre, perspective, boundaries, canon surface) | `skills/canon-guard/GENERATION_CONTRACT.md` |
| The **drafting constraints in force** (the five gate terms) | `samur/00-audit/2026-08-28-initial-cross-check.md` §4 |
| The project's craft rules (the tic/structure/anachronism/world-integration lists) | `skills/canon-guard/anti-patterns.md` |
| The narrative's **KE position** (default: the Dhaneshra Period's equilibrium, post-KE ~900 — `samur/02-canon/DYN-04` §15) | `project_context.narrative_period_ke` |

A run without a valid project context is an **`input_rejection`**, not a
degraded-mode analysis. This is intentional: the skill's detectors
(`../taxonomy/19-project-tells.md`) reference canon IDs, name pools, and the
wind law; run without them they would produce confident nonsense.

**Division of labor (binding).** Canon *verification* of a draft belongs to
the Canon Guard (`skills/canon-guard/` — pre-generation gate +
post-generation `post_verify` on structured claims). This skill *detects*
canon-breaking prose patterns (they are AI tells too — PST-01, PST-03,
PST-04, PST-09, PST-10) and *reports* them to the author / guard workflow; it
never repairs canon itself, never files QUESTIONs, and never edits
`samur/`. Its edits are confined to the narrative draft's prose.

## 2. The three authority classes

Every finding carries an `authority` (`../spec/04-output-schema.md` §2):

1. **`project_canonical`** — a **PST** finding (`../taxonomy/19-project-tells.md`).
   Normative, not empirical: it encodes this project's rules (charter, canon,
   drafting constraints), so it is actionable on identification of an
   instance, without empirical confidence weighting. Its "evidence" cites
   canon IDs and project documents, not S-sources.
2. **`empirical`** — a generic-cluster finding (P01–P07, N01–N08, …). Exactly
   as the evidence hierarchy has always governed it
   (`../research/02-evidence-hierarchy.md`): confidence-weighted, never
   word-list-based, Low/Folklore non-actionable.
3. **`project_style_rule`** — the craft tics this project's author has
   *declared* (via `skills/canon-guard/anti-patterns.md` and the
   `author_intent.style_anchors` of the Generation Contract): e.g.
   weather-as-mood at scene openings, tricolon reflex, "as if"-simile
   density, em-dash/ellipsis dependence, double-explained metaphor,
   recycled ash/bell/rain motifs. Some of these are Folklore as *empirical*
   AI claims but **authorial style rules as project rules** — the author's
   declaration is what makes them actionable (Level ≤2; the intentionality
   logic inverted: the author asked for them *reduced*). They are PV-14's
   mirror: style anchors protect, style rules reduce.

## 3. The supremacy laws (how conflicts resolve)

1. **Canon supremacy.** No edit may alter an established Samur fact,
   institution, name, toponym, date, law, or negative space to serve a
   stylistic fix. A generic-tell fix that requires a canon change is rejected
   (the finding is re-routed to a canon-compatible fix or held at Level 0 and
   reported). Canon is the single source of truth; this skill never edits it
   and never invents it.
2. **Project-tell priority.** PST findings outrank empirical findings in the
   intervention queue when both are present: a draft can survive bland
   prose; it cannot survive a faction monolith or a resolved mystery. In
   `../spec/06-scoring.md` terms: no scoring term may push an empirical fix
   ahead of an unresolved `project_canonical` finding in the same span.
3. **Project constraint over generic improvement.** Where a generic No-Slop–style
   technique (kicker deletion, implication conversion, rhythm variation,
   specificity repair) would violate a project constraint — the in-world
   memory system, a register the canon fixes (the Veshna sacred register,
   the Khor oral register), a deliberate mystery, a drafting constraint —
   the project constraint wins and the generic fix is reformulated or
   dropped. Generic polish never overrides project canon, voice, or
   narrative logic.
4. **The in-world voice exception.** Samur narration may legitimately assert
   things the canon says are false — founding-myth idealizations, golden-age
   glorification, decline-and-loss framing (`samur/02-canon/CUL-01` §5: the
   empire imperfectly understands its own past). This is **not** N02/V02
   false profundity when the narration contract establishes an in-world
   chronicler, chronicle, or factional perspective; it is the world's memory
   system working. The detector asks *whose knowledge is this?* — the
   historian-omniscient voice asserting distorted history **as settled
   truth** is PST-04; an in-world voice asserting it as belief is craft.
5. **Mystery preservation.** Q-076 (the distant western partner), Q-077 (the
   hidden history), Q-078 (the Kesra Charter's text) and the NOT READY
   matters (Q-080/081/082/084/085/086) may be drawn on as the world's own
   uncertainty and may never be resolved by an edit (PST-10). "Improved
   closure" that closes a deliberate mystery is a rejection, not a fix.

## 4. What "generic" still means here

The generic clusters (`taxonomy/01`–`18` and `20`) and the project-tell
catalog (`taxonomy/19-project-tells.md`) remain in force — AI tells in
prose rhythm, dialogue symmetry, emotional captioning, scene skeletons, and
long-form drift are the same enemies here as anywhere. Two couplings:

- **Detection anchors.** Generic detectors that need an anchor now use the
  project's own facts: the transplant test's specificity anchor is the
  Samur world (`../frameworks/01-detection.md` §2 Pass C); the voice baseline
  includes the project's registers; uniformity baselines include the
  language map's legitimate register differences
  (`samur/02-canon/CUL-02`).
- **Project overrides.** Where the project is stricter than the generic
  taxonomy, the project wins and the taxonomy entry says so. Example:
  S04 (mood-signaling weather) is generic-FPR-3/Severity-1; in this project
  weather is never merely mood — the seasonal wind is the calendar, the
  agriculture, the military season, and the famine engine (GEO-03), so
  mood-weather is banned outright by the project's own anti-patterns and
  detected as PST-03.

## 5. Maintenance triggers (the binding is live)

This skill's project layer must be re-checked whenever the project changes:

| Project change | Required skill action |
|---|---|
| A canon file cited by `taxonomy/19` is revised or retired | Re-verify the PST entry against the live canon in the same commit (checklist T-11) |
| The drafting constraints change (a new gate / audit §4 revision) | Update `spec/01` §1 and the PST authority citations |
| A name pool, register, or toponym changes | Update PST-08/PST-09 detector anchors |
| A deliberate mystery is resolved or a NOT READY matter becomes canon | Update PST-10's protected list |
| The narrative period changes (a pre-fragmentation flashback arc, a deep-time prologue) | Update the KE-position contract; the in-world epistemology rules (PST-04) are period-sensitive |
| The Canon Guard's contract or anti-patterns change | Update the authority classes and the project style rules |

**Canon wins over this skill.** Where this folder and `samur/02-canon/`
disagree, canon wins, the disagreement is a defect here, and the fix is in
this folder — never in the canon.
