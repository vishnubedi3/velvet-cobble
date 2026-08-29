# SEVERITY.md

Findings have a risk band. Decisions use the band. Harmless expansion is not a violation. A serious contradiction is not a vibes warning.

| Band | Meaning | Typical decision |
|---|---|---|
| **informational** | Noted; no constraint violated (legitimate expansion, corroboration) | PASS |
| **low** | Worth recording; does not bind the generator | PASS |
| **warning** | Canonically safe enough to proceed; direction, provisional use, or classified conflict must be labeled | PASS_WITH_WARNINGS |
| **significant** | Unsafe to guess (ambiguity, uninspected Arena, proposed-as-established) | REQUIRES_CLARIFICATION |
| **blocking** | Material violation of established `main` canon, charter, admission, contamination, continuity, bypass | BLOCK |
| **canon_change** | User wants an incompatible established outcome | CANON_CHANGE_REQUIRED |

Mapping from existing finding `severity` fields in the reference core:

| Engine field | Band |
|---|---|
| `info` | informational |
| `warn` | warning |
| `stop` | significant |
| `block` | blocking |

Do not upgrade a warning to a block to "be safe." Do not downgrade a block to a warning because generation is desired. Tests measure **false acceptance** and **false rejection** ([`spec/09-evaluation.md`](spec/09-evaluation.md)).
