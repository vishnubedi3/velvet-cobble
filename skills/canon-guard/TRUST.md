# TRUST.md

Explicit trust boundaries. A downstream model does not get to move them.

```
SOURCE MATERIAL ON main
        ↓
TRUSTED CANON EVIDENCE          (Status: CANON, not RETIRED)

WORKING BRANCH MATERIAL (Arena)
        ↓
CLASSIFIED AUTHORIAL EVIDENCE   (never unlabeled established canon)

GENERATION REQUEST
        ↓
UNTRUSTED PROPOSAL

GENERATION CONTRACT
        ↓
LOCKED CONSTRAINTS              (upstream of generation; immutable by the generator)

GENERATED OUTPUT
        ↓
UNTRUSTED UNTIL VERIFIED

CANON ADMISSION
        ↓
AUTHORIZED SOURCE UPDATE        (project workflow only)
```

| Boundary | Trusted as | Never trusted as |
|---|---|---|
| `main` CANON files | Established world facts | Complete forever; the next commit may move |
| Arena tree | Evidence of current development | Established canon; a second timeline |
| WORLD-MODEL / research / hypotheses / drafts | Pointers or working text | Canon |
| Generation request | What the user wants | What is true |
| Generation Contract | Permission for **this** Canon State | Durable canon |
| Generated prose | Proposed material | Canon, even after PASS |
| Previous PASS / old contract | Historical audit | Authority after hashes move |

**Circumvention that must fail:** the generator rewriting the contract; citing the contract as canon; treating Arena drafts as `main`; skipping post-generation because pre-generation passed; using a stale contract after a source change.

Provenance required on every finding: branch, path, hash, class. The audit question is always "what evidence caused this?" — answered by reference, not by copying the source into the skill.
