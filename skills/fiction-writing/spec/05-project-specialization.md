# 05 — Project specialization

Specialization means: the guard knows **this repository's machinery**. It does not mean: the guard contains the world.

Do not copy fictional contents here. Re-read the live files.

---

## 1. What kind of project this is

A material-conditions worldbuilding repository for a fictional medieval imperial setting, with a blocked-or-gated narrative stage depending on the applicable branch's charter. Comparative real-world research is strictly separated from canon. Generated fiction, when it exists, is stored apart from canon.

The guard must therefore handle **worldbuilding generation** and **narrative generation** as different kinds with different authorization checks — both evaluated against live CANON.

---

## 2. Source layout (re-read `samur/README.md`)

Typical directories (names may grow):

- `00-audit/` — process
- `01-research/` — not canon; transformation logs live under comparative research
- `02-canon/` — the only citable world facts; file IDs like `GEO-01`
- `03-hypotheses/` — not canon
- `04-questions/` + `REGISTER.md` — status-bearing questions; register can **lag** individual files — parse both
- optional `narrative/`, optional `05-quality/`
- `CHANGELOG.md`, `CONTRADICTIONS.md`, `WORLD-MODEL.md`

Canon file headers to parse every time:

```
Status: CANON | RETIRED | ...
Depends on: ...
Dependents: ...
High-impact: yes | no | (yes with a reason)
Last revised: ...
```

Domain prefixes are listed in `samur/README.md`. Use that table as the relevance map. Do not freeze the current ID inventory (it grows: foundation files, deepening `-02/-03` series, later operations).

---

## 3. Load-bearing *mechanisms* (not facts)

These are process invariants observed in the charter and audits. They constrain generation **as rules of work**, while their *contents* stay in canon files:

- **Transformation gate.** Major institutions/events need the 5-step log or explicit material/geographic reasoning.
- **Influence register.** Real-world counterparts recorded to catch renamed transplants.
- **Dependency sweeps** on high-impact edits.
- **Changelog** for every canon add/revise/retire.
- **Retire, don't delete.**
- **No-transplant / no-Earth** (stated in deep-chronology files and transformation rules): research is mechanism, not a source to reskin.
- **No false precision** in deep time: orders and relative order vs. exact era dates — two epistemologies. Do not coerce.
- **No constant-activity filler** in deep time.
- **Deliberate mysteries** stay unresolved until an explicit, authorized change.
- **Stewardship:** NOT READY remains untouched; no provisional canon.
- **Negative space** is load-bearing (things that did *not* happen).
- **Name pools** (when narrative is authorized): names come from current CUL/DYN pool files — re-read them; do not copy the pool into this skill.
- **In-world vs author-level knowledge** (deep chronology files distinguish the world's knowledge from author truth). Generation in a period must respect what that period's people can know.

The **current** list of mystery question IDs, era names, office names, etc. is **not** repeated here on purpose.

---

## 4. WORLD-MODEL vs canon files

`WORLD-MODEL.md` declares itself a summary. The contradictions register's authority rule: **canon files win**. The guard:

- may use the world-model to find pointers
- must verify those pointers in files
- must not treat a world-model-only sentence as CANON
- logs summary lag as a process finding, not as a second fact

---

## 5. Question statuses (parse the file)

Observed status vocabulary (extend if new words appear in files):

- RESOLVED (with pointer)
- PARTIALLY RESOLVED
- INTENTIONALLY UNRESOLVED
- OPEN (including "narrative detail", "deep unknown", "next development unit")
- NOT READY
- BLOCKED by missing information
- REJECTED premise / CONSOLIDATED / BOOKKEEPING

REGISTER.md is an index. If REGISTER and `Q-NNN_*.md` disagree, that is `CX-AMBIGUITY` / process conflict — do not pick silently.

---

## 6. Chronology epistemologies

Observed (re-read TIM files to see current structure):

- Exact dated events in an era calendar
- Era ranges that *contain* later exact dates (not a conflict)
- Deep orders of magnitude and relative order (not years)
- A master chronology that may have a deep section plus an exact section

Temporal checks must use the epistemology of the source they cite.

---

## 7. Narrative authorization is a live charter bit

On some refs, `PROJECT.md` §2 forbids story writing until a distinct command.

On some session refs, the same section has been rewritten to authorize a pilot and to locate prose under `samur/narrative/`.

The guard reads **the applicable ref's §2**. It does not hard-code "narrative is blocked" or "narrative is authorized."

H-001 (story location) may be awaiting confirmation on one ref and confirmed on another. Believe the applicable ref.

---

## 8. Complementary skills

- This package: pre-generation, canon-aware.
- `anti-patterns.md`: prose craft during generation.
- `ai-fictional-tells-skill`: post-generation, locate it on the applicable tree.

---

## 9. What specialization forbade

- A "current facts" appendix
- A copied dynastic list
- A copied toponym list
- Treating the 2026-08-28 file count as permanent
- Treating CC-08 or any other register item as eternal (re-read the register)
