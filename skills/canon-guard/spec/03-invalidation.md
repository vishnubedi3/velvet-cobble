# 03 — Invalidation

Derived state is a cache. Source changes punch holes in it.

---

## 1. Detect

Compare Canon States (or a previous state's hash list vs. current files):

- path added / removed / renamed
- content hash changed
- header fields changed (`Status`, `High-impact`, `Depends on`, `Dependents`)
- question status line changed
- contradictions-register active set changed
- charter clause changed
- branch head moved

---

## 2. Classify

| Change | Scope |
|---|---|
| Non-high-impact body edit; dependents empty or listed as documentary | **local** — drop facts from that document; re-extract that document and its direct dependents |
| Dated event / reign / era bound | **temporal** — drop facts whose story-time interval intersects the edited interval; re-extract chronology dependents |
| `High-impact: yes`, or edit to geography / succession / currency / core religion / calendar / world-law | **systemic** — drop the whole derived index for that Canon State; next request full re-resolve of the relevant closure (which may be the entire canon set) |

When unsure, widen.

---

## 3. What gets invalidated

- derived facts whose `source.path` matches
- derived facts whose `depends_on` includes the changed document ID
- Generation Contracts listing any changed hash
- WORLD-MODEL-derived index entries (always; it is not authority)
- knowledge-boundary entries if the change is a learning event

Do not invalidate unrelated local facts when the change is local.

Do not keep a contract "mostly valid." Hash mismatch → stale.

---

## 4. What does not get invalidated

- Historical audit records (they remain records of *that* state)
- RETIRED files' archival status (they stay retired until a source says otherwise)
- Other branches' Canon States (a change on branch A does not patch branch B's cache; it may create *divergence findings* on the next multi-branch discovery)

---

## 5. Tests

Scenarios 14 (systemic) and 15 (local) of the adaptive suite must fail if the engine rebuilds everything on a local edit or fails to rebuild on a high-impact edit.
