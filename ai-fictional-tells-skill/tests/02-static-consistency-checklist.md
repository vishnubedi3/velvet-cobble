# 02 — Static Consistency Checklist (T-1 … T-10)

Checks that keep the distributed folder internally coherent. Run them on
every release of this skill and after any edit that touches cross-file
references, IDs, or schemas. They are static (no LLM, no runtime); a small
shell/Python harness is sufficient, and the commands below are exact.

## T-1 — All internal links resolve

Every Markdown link target inside the folder must exist, resolving from the
referencing file's own directory. Run from the folder root:

```bash
python3 - <<'EOF'
import re, os, glob
for f in glob.glob('**/*.md', recursive=True):
    for m in re.finditer(r'\]\(([^)#]+?)(?:#[^)]*)?\)', open(f).read()):
        t = m.group(1)
        if t.startswith(('http','mailto','#')): continue
        p = os.path.normpath(os.path.join(os.path.dirname(f), t))
        assert os.path.exists(p), f"{f} -> {t}"
print("T-1 OK")
EOF
```

Also verifies that no link leaves the folder (`..`-chains resolving above the
folder root fail the `exists` check only if the target is missing — add an
explicit check that the resolved path starts with the folder root if you want
stricter containment).

## T-2 — JSON Schemas are valid and loaded cross-consistently

```bash
python3 -c "
import json, glob
for f in glob.glob('schemas/*.json'):
    json.load(open(f)); print('valid', f)
"
```

Consistency: `schemas/skill-input.schema.json` must mirror
`spec/03-input-schema.md` §1–§5 field-for-field; `schemas/analysis-report.schema.json`
must mirror `spec/04-output-schema.md` §2; `schemas/story-model.schema.json` must
mirror `interventions/03-story-model.md` §1. Any field added to one must be
added to the other in the same change (checked manually; the manifests flag
which pairs are coupled).

## T-3 — Tell IDs referenced exist in the canonical index

Extract the canonical tell-ID list from `taxonomy/README.md` (the table's ID
column). Every `tell_ids` reference and every standalone tell ID used in
`frameworks/`, `interventions/`, `spec/`, `examples/`, and `tests/` must be in
that list. `CONSOLIDATION-REPORT.md` is exempt: it is a historical record and
legitimately quotes defect strings that are no longer live identifiers.
(Note the `S` disambiguation: description tells S01–S06 vs. source
IDs S01–S53 — see [`../glossary.md`](../glossary.md) §6.)

## T-4 — Source IDs referenced are defined in `research/03-source-index.md`

Every `S` + digits token used as a citation must appear in the source index.
The index is the only place source IDs are defined.

## T-5 — Every file is in `MANIFEST.md` and vice versa

The manifest must list exactly the files present (excluding `.git`):
no orphans, no phantom entries. Add new files to the manifest in the same
commit that adds the files.

## T-6 — Terminology matches `glossary.md`

Spot-grep for the terms in [`../glossary.md`](../glossary.md) §1–§9; no file may use
competing terms (e.g., "humanization score", "AI score", "fix pass" for what
the glossary calls re-evaluation). The glossary is canonical; update it, then
the files, not the other way around. This checklist file itself is exempt
from the spot-grep for the example terms quoted in this paragraph.

## T-7 — Numbering invariants

- Spec files: `spec/02`…`spec/13` with exactly the documented gaps
  (no `01`, `08`, `10` — see [`../glossary.md`](../glossary.md) §9). Files must not be
  renumbered without updating every reference (T-1 catches broken links, but
  numbering is also referenced in prose).
- Taxonomy: `01`–`18` and `20`; no `19`.
- Tests: `tests/01-adversarial-suite.md` (A-T1…A-T23, 23 tests, none missing,
  none duplicated) and `tests/02-static-consistency-checklist.md` (T-1…T-10).
- Failure modes F-1…F-10, preservation dimensions PV-1…PV-14, pipeline
  invariants I-1…I-6, final-read checks FR-1…FR-7, benchmark metrics
  A1–A7 / P1–P5 / M1–M4 — each set complete and referenced only by its
  canonical name.

## T-8 — No out-of-folder dependencies

```bash
grep -rn "\.\./" --include='*.md' . | grep -v "^\./\.git"
```

All `../` chains must stay inside the folder. Also grep for absolute paths
(`/home/`, `/Users/`, `C:\`) and for the old repository paths (`velvet-cobble`,
`skill/0`, `skill/1`) — none may remain.

## T-9 — Exactly one entry point

`README.md` must exist at the folder root, must link `SKILL.md` as the
primary specification, and must be self-sufficient (a new reader can start
the skill from it alone). `SKILL.md` must link back to the README's quick
start or contain the same core contract.

## T-10 — Config consolidation

Every parameter in [`../CONFIG.md`](../CONFIG.md) must be cited from at least one
spec/taxonomy/framework file, and every number stated in the spec files as a
default must appear in CONFIG.md (or be explicitly marked "not configurable"
in CONFIG.md §8). Numbers found only in prose are review-triggers, not
failures — but two different defaults for the same parameter in two files is
a hard failure.

---

## Running all checks

A release passes when T-1…T-10 all pass. This checklist itself is part of the
release: if the folder gains a new document class (e.g., a new schema pair),
extend the checklist in the same commit and note it in
[`../CONSOLIDATION-REPORT.md`](../CONSOLIDATION-REPORT.md).
