# Glossary

Terms that must not drift between files.

| Term | Meaning |
|---|---|
| **Canon Guard** | This skill (`skills/fiction-writing/`). Canon-protection ecosystem: resolve, verify, lock, post-verify. Not tell reduction. |
| **Applicable branch** | The ref a request is evaluated against. `main` is the default canonical baseline. |
| **Arena** | Live `arena/*` session heads. The **current working / authoring state**. Not automatically established canon. Consulted aggressively and classified against `main`. |
| **Current Working Canon Context** | Established `main` canon plus classified Arena developments for one request. Not a merge. |
| **Splash classification** | Content-level class: `CONFIRMS_CANON`, `CLARIFIES_CANON`, `EXTENDS_CANON`, `DEVELOPS_INTENDED_CANON`, `PROPOSED_CANON`, `DEVELOPMENTAL`, `EXPLORATORY`, `CONTRADICTS_CANON`, `RETCON_PROPOSAL`, `ABANDONED_OR_SUPERSEDED`, `UNRESOLVED`. |
| **Admission** | Explicit promotion of proposed material into `samur/02-canon/` via project workflow. |
| **Canon State** | Relevant source state at specific commits/hashes. Derived, not authority. |
| **Canon file** | A document under `samur/02-canon/` with `Status: CANON`. |
| **Constraint** | A derived rule bound to provenance. |
| **Content hash** | Hash of a source file body used for freshness. |
| **CX-*** | Conflict class IDs in `CONFLICT_TAXONOMY.md`. |
| **Derived index** | Optional cache of extracted facts. Never the authority. |
| **Divergence** | Materially different facts or charters on live refs. Not silently merged. Extra `arena/*` is classified Splash, not automatic `REQUIRES_CLARIFICATION`. |
| **Source status** | Contract bands: ESTABLISHED_CANON / CURRENT_WORKING_DEVELOPMENT / CANON_CLARIFICATIONS / AUTHORIAL_DIRECTION / PROVISIONAL / CONFLICTS / OPEN_QUESTIONS. |
| **Constraint bands** | HARD_CONSTRAINTS (obey) / SOFT_CONTEXT / CURRENT_AUTHORIAL_DIRECTION / PROVISIONAL_MATERIAL / FORBIDDEN_ASSUMPTIONS. |
| **Locked contract** | Generation Contract hashed and immutable for the generator. |
| **Post-generation verification** | Second canon layer (`post_verify`). Not tell reduction. Never admits. |
| **Contamination** | Working or generated material presented as established `main` canon. |
| **Bypass** | Generator redefines or skips locked constraints / the pre-generation gate. |
| **Continuity ledger** | Derived prior-chapter states keyed by entity, predicate, story-time, source hash. Cache only. |
| **Epistemology** | How a source dates or knows a claim (`exact`, `range`, `order`, `relative`, in-world vs author-level). |
| **Generation Contract** | State-bound permission object. Stale when hashes move. |
| **High-impact** | Header flag on a canon file; changes trigger broad invalidation and dependency sweeps. |
| **Host** | The agent or system running this skill. |
| **Negative space** | Canonical non-event or forbidden development. |
| **Proposed material** | Generated output not yet admitted. |
| **Recovery tag** | `recovery/*` snapshot. Not live canon. |
| **Repository time** | Git history. |
| **Story time** | Fictional chronology. |
| **Stale** | A Canon State or contract whose contributing hashes no longer match. |
| **WORLD-MODEL** | Summary index on a branch. Loses to canon files. |
