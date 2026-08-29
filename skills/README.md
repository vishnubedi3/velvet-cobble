# `skills/` — Agent skills

Skills are not canon.

| Path | Role |
|---|---|
| [`canon-guard/`](canon-guard/) | **Canon Guard ecosystem** (complete skill package). Pre-generation gate, locked contract, post-generation canon verification. Not tell reduction. |
| [`INTEGRATION.md`](INTEGRATION.md) | How the pre-generation guard and the post-generation tell skill fit together. |

The post-generation tell-reduction skill is a separate package. On this branch it lives at repo-root `ai-fictional-tells-skill/`. Other live branches may move it under `skills/` — resolve the applicable tree; do not assume one layout.

That skill is **bound to this repository's project**: it validates a Samur project context at intake (rejecting unbound drafts rather than running generically), checks drafts against project tells derived from `samur/02-canon/` and the drafting constraints before generic craft tells, gives project rules (canon, registers, author standards) priority over generic corrections, and reports — never fixes — canon contradictions to the Canon Guard workflow. It is adapted from, not a copy of, external anti-slop methodology, and it is not portable to other projects; changes to the project's narrative standards may require skill changes (same-commit re-verification). See its [`README.md` §5](../ai-fictional-tells-skill/README.md) and [`spec/01-project-binding.md`](../ai-fictional-tells-skill/spec/01-project-binding.md).
