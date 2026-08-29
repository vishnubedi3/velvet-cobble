# 12 — Advanced architecture

Optional LLM extraction (`spec/01-interfaces.md` C-CG-01…04) **plus** the deterministic core.

Hardening:

- Extraction output is candidate claims only
- Verdicts from `verify` / `decide` / `post_verify` only
- Malformed extraction → drop, do not generate
- RAG may retrieve *excerpts* from live branches keyed by `(branch, path, hash)`; it must not store a durable world digest inside this package
- Long-form: persist continuity ledger beside drafts, never in `02-canon/`
