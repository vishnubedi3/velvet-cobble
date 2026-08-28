# 02 — Static consistency checklist

Manual / host checks on the skill package (not on the world).

| ID | Check |
|---|---|
| T-1 | Every markdown link inside this folder is file-relative and resolves |
| T-2 | `SKILL.md` lists the five decisions and the 15-step gate |
| T-3 | No file in this package contains a copied dynastic list, city table, or other `02-canon/` body |
| T-4 | `MANIFEST.md` lists every skill file that the tests and specs reference |
| T-5 | JSON schemas parse as JSON |
| T-6 | `re_resolve_every_request` default is true and marked non-compliant if flipped |
| T-7 | `WORLD-MODEL` is documented as non-authority |
| T-8 | Recovery tags are documented as non-live |
| T-9 | `anti-patterns.md` still exists (preserved, not overwritten) |
| T-10 | Fixtures live under `fixtures/` and do not import `samur/` |
| T-11 | [`BRANCH_RELATIONSHIP.md`](../BRANCH_RELATIONSHIP.md) exists; Splash is not automatically canon and is not dismissed as non-canon |
