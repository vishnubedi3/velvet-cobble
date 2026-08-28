# Glossary

Terms that must not drift between files.

| Term | Meaning |
|---|---|
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
| **Source status** | Contract bands: CANONICAL / CANON_CLARIFICATION / AUTHORIAL_INTENT / PROPOSED / CONFLICT. |
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
