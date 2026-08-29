# Continuity guard

Protect established *states* across chapters, documents, and storylines — without freezing Arena.

A continuity ledger is **derived** from admitted `main` canon (and, when continuing a storyline, from classified Arena states that the request is explicitly following). It is not a skill-owned factbook.

| Check | Finding |
|---|---|
| Same entity + predicate, overlapping story-time, incompatible value vs prior admitted/ledgers | `CX-CONTINUITY` → BLOCK |
| Later chapter uses knowledge not acquired by that story-time | `CX-KNOWLEDGE` |
| Later chapter inverts a recorded causal preclude | `CX-CAUSAL` |
| Later chapter follows superseded Arena after `main` moved | re-classify; do not honor the old direction |

The ledger is keyed by `(entity, predicate, story_time)` plus source hash. Hash change → drop those rows ([`../spec/03-invalidation.md`](../spec/03-invalidation.md)).

Legitimate expansion (new predicate, no collision) is not a continuity break.
