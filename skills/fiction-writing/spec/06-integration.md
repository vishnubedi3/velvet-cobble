# 06 — Integration with this repository

---

## 1. Where this skill lives

`skills/fiction-writing/` on the branch that contains it. Completing this directory fulfills the charter's named pre-generation canon guard. It does not reorganize `samur/02-canon/`.

---

## 2. Hook points

```
author / agent request
        ↓
Canon Guard (this skill)          ← always
        ↓
  BLOCK / CLARIFY / CHANGE  → stop
  PASS / PASS_WITH_WARNINGS → Generation Contract
        ↓
generator (any model)
        ↓
draft (narrative/ or proposed canon text, per kind)
        ↓
ai-fictional-tells-skill          ← narrative drafts only
        ↓
review
        ↓
admission protocol                ← only if accepting into 02-canon/
```

Worldbuilding requests skip the tell skill (it has no function on canon files). They still cannot skip this guard.

---

## 3. Report storage

Prefer `samur/05-quality/` **when that directory exists on the applicable branch**. Otherwise store beside the host's audit logs (`samur/00-audit/` is for repository audits, not per-request guard reports — do not dump request reports there unless the host already uses it that way).

Never write into `02-canon/` or into prose files.

---

## 4. Effect on existing canon

**None** by implementation or by a verification run. The skill reads. Admission and canon-change writes are separate, user-authorized operations following project protocol.

---

## 5. Acceptance

- Adaptive suite green (A01–A27, including main vs Arena working state): `python3 skills/fiction-writing/tests/run_adaptive_tests.py`
- Static checklist: [`../tests/02-static-consistency-checklist.md`](../tests/02-static-consistency-checklist.md)
- No Samur lore bodies copied into this package (spot-check: no dynastic lists, no copied city tables)
- `02-canon/` untouched by the skill's own commits except if an unrelated project operation happens
