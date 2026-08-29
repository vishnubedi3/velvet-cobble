# CANON_MODEL.md

A **Canon State** is the relevant state of the project's source material at a particular point in repository evolution. It is computed, used, audited, and discarded. It is not the world.

---

## 1. Identity of a Canon State

A Canon State is identified by:

- the applicable branch name(s)
- the commit SHA (or equivalent) of each applicable branch
- content hashes of every source document that contributed constraints
- the request's relevance filter (which documents were selected)
- a timestamp of evaluation

Two verifications evaluate "the same canon" only if those identifiers match.

Schema: [`schemas/canon-state.schema.json`](schemas/canon-state.schema.json).

---

## 2. Authority ranking (this project)

Re-read the applicable branch's `PROJECT.md` §3 and `samur/README.md` on every resolution. The ranking below is the **derivation rule** observed in those documents; if a future branch revises the taxonomy, the live documents win.

| Rank | Status (as currently named) | Default location | Citable as world fact? |
|---|---|---|---|
| 1 | **CANON** (not RETIRED) | `samur/02-canon/` | **Yes** — sole citable fact class |
| — | **CANON-INDEX** (summary) | `samur/WORLD-MODEL.md` | **No.** Navigation aid. If it disagrees with a canon file, the **canon file wins**. Record the disagreement. |
| — | **QUESTION** with Status RESOLVED | `samur/04-questions/` | Only as a **pointer** to the canon file named in the status line. Re-read that canon file. |
| — | **QUESTION** INTENTIONALLY UNRESOLVED | `samur/04-questions/` | Not a fact. A **forbidden resolution**. |
| — | **QUESTION** NOT READY / OPEN / PARTIALLY RESOLVED / BLOCKED | `samur/04-questions/` | Not a fact. Constrains what may be invented. |
| — | **HYPOTHESIS** | `samur/03-hypotheses/` | Never citable as canon. |
| — | **RESEARCH** | `samur/01-research/` | Never canon by location. Enters the world only via a transformation log. |
| — | **INFLUENCE** | influence register inside research | Drift control, not world fact. |
| — | **PILOT / DRAFT** | `samur/narrative/` **if that directory exists on the branch** | Not canon. |
| — | **ANALYSIS** | `samur/05-quality/` **if it exists** | Not canon. |
| — | Charter / protocol | `PROJECT.md`, optional root `AGENTS.md` | Branch **constraints** (authorization, separation rules), not world facts. |
| — | Changelog / contradictions register | `samur/CHANGELOG.md`, `samur/CONTRADICTIONS.md` | Process state. Active contradiction entries are **unresolved conflicts**, not facts to prefer. |
| — | Recovery tags | `recovery/*` | Historical snapshots. Not live canon unless the request is an explicit historical audit. |

Do not invent additional statuses. If a file has no status, it is not CANON.

---

## 3. Provenance (required on every constraint)

```
Canon Fact
  → Source Branch
  → Source Document
  → Source Location (heading / section if available)
  → Source Version (commit + content hash)
  → Derived Constraint
```

Do not copy the document body into the constraint record beyond the minimum span needed to audit the derivation.

---

## 4. Derived index (cache only)

Hosts may extract, for speed:

- entity mentions
- dated events
- dependency graph (`Depends on` / `Dependents`)
- high-impact flags
- question statuses
- negative-space claims
- knowledge-boundary markers (in-world vs author-level)

The index is **invalid** the moment any contributing hash changes. Re-extraction is not optional after invalidation.

Never ship a populated index inside this skill package.

---

## 5. Fact shape (derived, not stored)

When extraction occurs, record:

- `entity`, `predicate`, `value`
- `story_time_start` / `story_time_end` (optional; open-ended allowed)
- `epistemology`: `exact` | `range` | `order` | `relative` | `unknown` — this project uses more than one; do not coerce deep orders into false-precision dates
- `known_by`: omitted = world-true at author level; present = in-world knowledge bound
- `polarity`: asserted | denied | unknown | forbidden (negative space)
- `high_impact`: from the source header
- `depends_on` / `dependents`: from the source header
- `status`: CANON / etc.

Incompatible values for the same entity+predicate with overlapping story-time are conflicts.

---

## 6. Legitimate expansion vs. contradiction

New writing may add characters, places, relationships, events, political conditions, historical facts, capabilities, consequences, and knowledge.

**Expansion:** the new claim does not collide with an applicable established CANON fact, does not resolve an INTENTIONALLY UNRESOLVED question, does not invent a NOT READY answer, and does not smuggle a new high-impact fact through narrative.

**Contradiction:** the new claim is incompatible with applicable established CANON at the requested story-time.

**Canon change:** the user wants the incompatible outcome anyway. That is not a PASS. See [`CANON_CHANGE_PROTOCOL.md`](CANON_CHANGE_PROTOCOL.md).

---

## 7. Retirement

The project retires canon by status change (RETIRED), not deletion. Retired files remain in the tree. They are **not** citable. Dependents must be reworked in the same change. The guard treats RETIRED as: do not use as support; do use as a warning if a request cites the retired content as if live.

---

## 8. Splash is context, not a second fact table

Arena Splash facts are **not** appended to `facts` on the `main` Canon State. They are classified (`splash_classifications`) and hashed for freshness. Re-classification is required when either side's hashes move. See [`BRANCH_RELATIONSHIP.md`](BRANCH_RELATIONSHIP.md).

---

## 9. What this model refuses

- A one-time extraction of "all current facts."
- Treating today's file list as the permanent set of domains.
- Treating a previous Canon State as the next request's input without a freshness check.
- Unioning Splash `02-canon/` into `main` because the session labeled it CANON.
