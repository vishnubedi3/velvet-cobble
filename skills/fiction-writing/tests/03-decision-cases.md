# 03 — Extra decision cases (project mechanisms)

These are not substitutes for the adaptive suite. They lock project-specific *mechanisms* using synthetic data.

| Case | Setup | Decision |
|---|---|---|
| Mystery | Question `Q-X` INTENTIONALLY UNRESOLVED; claim `resolves_question=Q-X` | BLOCK `CX-MYSTERY` |
| NOT READY | Question `Q-Y` NOT READY; claim invents an age | BLOCK `CX-NOT-READY` |
| OPEN detail | Question OPEN; claim fills it | PASS_WITH_WARNINGS |
| Charter | `narrative_authorized: false`; kind `narrative` | BLOCK `CX-BRANCH` |
| Worldbuilding while narrative blocked | kind `worldbuilding`; no contradiction | PASS (worldbuilding is the live work) |
| Summary citation | `cited_status: CANON-INDEX` | REQUIRES_CLARIFICATION `CX-AUTHORITY` |
| Explicit change | `explicit_canon_change: true` plus a direct conflict | CANON_CHANGE_REQUIRED |
| Active register | OPEN contradiction intersecting the entity | REQUIRES_CLARIFICATION |
| Repo time ≠ story time | Source written "later" describing an earlier ordinal; request at the earlier ordinal uses the *described* state, not the write time | temporal check uses ordinal |
| Newer Splash vs `main` | Splash says dead, `main` says alive, Splash commit is newer | `CONTRADICTORY`; `main` remains baseline; dead not CANONICAL |
| Uninspected Splash | Live `arena/*` head, no classification | REQUIRES_CLARIFICATION `CX-AMBIGUITY` |

The last two-clock row: repository commit order must not be treated as story order. Newer Splash is also not story-order and not a canon override.
