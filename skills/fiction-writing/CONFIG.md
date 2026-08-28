# CONFIG.md

Host-overridable parameters. None of these are world facts.

| Key | Default | Meaning |
|---|---|---|
| `default_branch` | repository default (`main` if that is `origin/HEAD`) | Canonical baseline when the request is silent |
| `main_is_canonical_baseline` | `true` | Must stay true. A host that sets this false is non-compliant |
| `splash_is_automatically_canon` | `false` | Must stay false. Splash is classified against `main` |
| `splash_is_irrelevant` | `false` | Must stay false. Do not implement "Arena Splash is non-canon" |
| `conservative_on_divergence` | `true` | Uninspected Splash, or CONTRADICTORY Splash that the request would *establish* over `main`, → `REQUIRES_CLARIFICATION`. Extra `arena/*` existence alone is not this |
| `re_resolve_every_request` | `true` | Must stay true. A host that sets this false is non-compliant |
| `world_model_is_authority` | `false` | Must stay false for this project |
| `research_is_canon` | `false` | Must stay false |
| `drafts_are_canon` | `false` | Must stay false |
| `recovery_tags_are_live` | `false` | Must stay false |
| `high_impact_invalidation` | `systemic` | Broad revalidation |
| `local_invalidation` | `targeted` | Direct dependents only |
| `open_narrative_detail` | `pass_with_warnings` | Fill allowed in drafts; not admitted |
| `mystery_resolution` | `block` | Unless explicit canon change |
| `not_ready_invention` | `block` | Stewardship |
| `hash_algorithm` | `sha256` | Content hashes |
| `require_provenance` | `true` | Constraints without provenance are dropped |

Validation: if a host sets `re_resolve_every_request`, `world_model_is_authority`, `research_is_canon`, `drafts_are_canon`, or `recovery_tags_are_live` to a non-compliant value, the skill must refuse to run.
