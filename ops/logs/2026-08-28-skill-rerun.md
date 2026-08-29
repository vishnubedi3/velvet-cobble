# Operations Log — 2026-08-28 — Canon Guard + AI Fictional Tells Re-run

## Action
Fresh re-run of both the Canon Guard (`skills/fiction-writing/anti-patterns.md`) and the `ai-fictional-tells-skill` post-generation pipeline against the current pilot chapter (`samur/narrative/pilot-chapter.md`). Previous skill report treated as superseded.

## Recovery Point
`recovery/pre-skill-rerun` — created at HEAD before any changes.

## Area Affected
- `samur/narrative/pilot-chapter.md` — 3 passages corrected + header updated
- `samur/05-quality/skill-report-pilot.md` — overwritten with replacement report
- `samur/00-audit/2026-08-28-skill-report-pilot-superseded.md` — previous report preserved
- `samur/CHANGELOG.md` — entry added

## Canon Effect
No canon files modified. The 34 canon files are unchanged.

## Significant Results

### Canon Guard Findings (2 corrections applied)
1. **CG-1:** "eight hundred years" for Dharan builders' blocks → "more than six hundred years" (canon: Great Temple built KE 240–265; at ~KE 912 that is ~650 years)
2. **CG-2:** Guru's résumé listed events 172+ years before his tenure → trimmed to Claim Moratorium's aftermath and equilibrium (events within ~872–912 tenure)

### AI Fictional Tells Findings (6 total; 2 applied, 4 preserved)
- F1 (V02): Guru's résumé — narrator exposition trimmed (overlaps CG-2)
- F2 (V02/U02): Temple Line explanation — narrator exposition removed; dialogue carries context
- F3 (P02), F4 (P07/V03), F5 (V04), F6 (D02): preserved as intentional/functional

### Comparison with Previous Report
- Previous: 13 findings, 17 edits applied
- This run: 6 findings, 2 edits + 1 canon fix
- 12 tells that were previously flagged or improved now pass cleanly

## Verification
- Canon Guard: PASS (all items verified against canon files)
- AI Fictional Tells: PASS (6 findings, 2 applied, 4 preserved)
- Preservation check: PASS (14/14 dimensions)
- Re-evaluation on changed spans: PASS

## Dependencies Affected
None. No canon files were modified.

## Contradictions Discovered or Resolved
None.

## Matters Left Unresolved
None. The pilot chapter is verified and clean.
