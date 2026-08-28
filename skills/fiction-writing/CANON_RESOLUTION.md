# CANON_RESOLUTION.md

How to derive current relevant canon from living branches. Re-run this procedure on every request. Do not cache its *conclusions* inside the skill.

---

## 1. Discover refs

From the repository (and `git ls-remote` when available), collect:

- heads (`main`, session branches, any other heads)
- recovery tags (`recovery/*`)
- open PR heads if the host can see them

Absence of a previously seen branch is itself a change.

---

## 2. Classify refs (evidence, not folklore)

Use **observable signals**. Do not assign a role just because a name looks like a role.

| Signal | Suggests | Does not prove |
|---|---|---|
| Default branch / `origin/HEAD` | Merged project state | That it is the right branch for *this* request |
| Name `arena/*` | Session / development work | That it is experimental, or that it is canon |
| Name `recovery/*` | Pre-operation snapshot | Anything about story-time |
| PR merged into default | Historical contribution now on default | That unmerged siblings are obsolete |
| PR open | Review | Canon |
| Directory `samur/02-canon/` present | World sources exist on that ref | Completeness |
| Directory `samur/narrative/` present on one ref and absent on another | **Material divergence** | Which side is authorized |
| `PROJECT.md` §2 differs across refs | **Charter divergence** | Which charter the user intends |
| Root `AGENTS.md` present on one ref only | Operational-protocol divergence | That the other ref is invalid |

Do not invent a merged super-canon. Do not invent an independent Splash timeline.

**Default canonical baseline** when the request is silent: the repository's default branch (`main` if that is `origin/HEAD`).

**Arena** (`arena/*`) is the **current working / authoring state**, not automatically that baseline. After inspecting `main`, inspect relevant Arena **aggressively** and **classify content** against `main` ([`BRANCH_RELATIONSHIP.md`](BRANCH_RELATIONSHIP.md)). A second live head is not by itself `REQUIRES_CLARIFICATION`. Ignoring strong current Arena development is a warning, not a silent PASS.

A request may name a branch. Then that branch is the **authoring context**. Splash continuation still labels source status and does not promote proposed/developmental material into established `main` canon.

If a live Splash head exists and has not been inspected, that is insufficient information (`REQUIRES_CLARIFICATION` / `CX-AMBIGUITY`) — not a reason to ignore it, and not a reason to treat it as canon.

---

## 3. Inventory sources on the applicable ref

Walk the tree of the chosen commit. Do not use a frozen file list from this skill.

On this project the **current** map is defined by `samur/README.md` and `PROJECT.md` §6 on that same commit. Typical (re-read; may grow):

- `samur/02-canon/*.md` — candidate CANON (parse `Status:`)
- `samur/03-hypotheses/` — hypotheses
- `samur/04-questions/` including `REGISTER.md` — questions (parse each file's `Status:`; **do not trust the register alone** if an individual file disagrees — that disagreement is a finding)
- `samur/01-research/` — research + transformation logs + influence register
- `samur/CHANGELOG.md`, `samur/CONTRADICTIONS.md`, `samur/WORLD-MODEL.md`
- `samur/00-audit/` — process evidence, not facts
- `samur/narrative/`, `samur/05-quality/` — only if present
- `PROJECT.md` — authorization and taxonomy
- optional root `AGENTS.md` — operational constraints if present

Skip: this skill package, the tell-reduction skill, `.git`.

For each inventoried file record path, status header, `Last revised` if present, `Depends on` / `Dependents` / `High-impact` if present, and a content hash.

---

## 4. Select the relevant subset

Do not load the entire world unless the request is foundational or the change under review is high-impact.

Relevance procedure:

1. Parse the request for names, domains, story-time, generation kind.
2. Read the **current** domain-prefix table from `samur/README.md` (TIM, GEO, DEM, DYN, ADM, ECO, MIL, TEC, REL, CUL, FOR, NS, and any prefixes added later).
3. Map request topics to prefixes **by that live table**, not by memory.
4. Include the matching canon files plus the `Depends on` closure (and `Dependents` if the request would change a fact).
5. Include any QUESTION files whose related-IDs intersect that set.
6. Include `CONTRADICTIONS.md` if it exists.
7. Include `WORLD-MODEL.md` only as an index: follow its pointers into canon files; if a claim appears only in the world-model, treat it as **unproven by canon** until the pointed file confirms it.
8. Include the charter clause that governs the generation kind (narrative authorization, no-story-writing, directory separation).

If relevance cannot be determined, widen (safer) or `REQUIRES_CLARIFICATION` — never silently skip a high-impact file that the dependency graph reaches.

---

## 5. Extract constraints from the subset

From headers (deterministic):

- `Status`, `Depends on`, `Dependents`, `High-impact`, `Date`, `Last revised`

From bodies (model-hosted or careful reading):

- asserted facts, denied facts, dated events, knowledge bounds, negative space, name-pool rules, world-law statements

Bind provenance. Mark epistemology (`exact` / `range` / `order` / `relative`) from how the source itself states the claim. This project forbids false precision in deep time: do not upgrade an order into a year.

---

## 6. Compare Splash against main (every time Splash is live)

When a live Arena Splash head exists:

1. Build the `main` Canon State (baseline).
2. Inventory relevant Splash sources on that head. Do **not** union them into `main` facts.
3. Classify each relevant Splash statement: `CONFIRMED_CANON`, `CANON_CLARIFICATION`, `CANON_EXTENSION`, `AUTHORIAL_INTENT`, `PROPOSED_CANON`, `DEVELOPMENTAL`, `EXPLORATORY`, `CONTRADICTORY`, `UNRESOLVED`.
4. A newer Splash commit does not replace `main` merely by being newer.
5. Compatible clarification may be used to understand `main` better, labeled as clarification.
6. Proposed / developmental / exploratory material is authoring context, not established canon.
7. Contradictions are classified and recorded. They are not silently resolved either direction.

A generation request evaluates against **`main` as baseline**, plus classified Splash context. Explicit continuation of a Splash storyline uses Splash as the authoring context while still labeling status.

Non-splash, unnamed divergence (a live head that is neither `main` nor `arena/*`, with no target) remains `REQUIRES_CLARIFICATION`.

---

## 7. Freshness

A Canon State is stale when:

- any contributing commit moved, or
- any contributing content hash changed, or
- a new relevant file appeared, or
- a relevant file was retired, or
- the applicable branch set changed

Stale → re-resolve. There is no "repair the index in place" path that skips hashing sources.

---

## 8. Historical verification

If the request asks "was this valid as of commit X / tag Y":

- Resolve a Canon State at that ref.
- Label it `historical_audit`.
- Do not use it to authorize generation on the live branch.

Recovery tags are for this purpose (and for rollback). They are not the next chapter's canon.
