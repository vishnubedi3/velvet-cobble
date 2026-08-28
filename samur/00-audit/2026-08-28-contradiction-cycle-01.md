# 2026-08-28 — Contradiction-Resolution Cycle 1 (audit record)

- **Date:** 2026-08-28
- **Auditor:** Samur Empire Historical Architect
- **Scope:** full cross-check of the 34 canon files (`02-canon/`), `WORLD-MODEL.md`, `PROJECT.md`, `samur/README.md`, `04-questions/REGISTER.md` + the 87 question files, `CHANGELOG.md`, the audits, and `skills/INTEGRATION.md`.
- **Method:** (1) dated-event consistency (every dated event checked against the TIM-03 master chronology and the TIM-01 era ranges); (2) reign/tenure range checks (DYN-02/FOR-02 tenures vs TIM-03 §8 fixed dates vs the DEM-02 §3 human scale); (3) cross-file fact agreement (institutions, rates, sizes, counts, directions, lists); (4) dependency-link sense; (5) register arithmetic; (6) WORLD-MODEL-vs-canon agreement (canon files win). Every candidate was either documented as a contradiction (CC-xx) with evidence + a resolution direction, or logged in the "checked — NOT contradictions" ledger with the reason it clears.

## The contradiction register

`samur/CONTRADICTIONS.md` created this cycle (the authority rule: canon files > WORLD-MODEL; resolved items are verified against the wider canon, then removed from the active register, with the resolution record in `CHANGELOG.md`).

## Results

### Findings — 8 contradictions documented (CC-01 → CC-08)

| ID | Priority | Conflict | Resolution | Status |
|---|---|---|---|---|
| CC-01 | 1 | the House of Kesra's end ~KE 680 (DYN-02) vs KE 675 (the TIM-03 §6, the DYN-04, the REL-02 §8, the DYN-05, the WORLD-MODEL) | DYN-02 → KE 675; era-label sweep (the DEM-02 §1, the MIL-02 §1, the TIM-03 §6 heading) | **RESOLVED + VERIFIED** |
| CC-02 | 2 | the withheld sanction's object — the REL-02 §5/§8 name the Kesra III; the canon cluster fixes the Threna I's consecration (the Tarn wing backs the Kesra III) | the REL-02 §3/§5/§8 corrected; the TIM-03 §5 pointer REL-02 §6 → §8; the WORLD-MODEL clarifies the object | **RESOLVED + VERIFIED** |
| CC-03 | 3 | the Phre governors' tenures (the FOR-02 §4 ~450–520 / ~520–620) vs the TIM-03 §8 fixed dates (the Q-073 resolution) | the FOR-02 §4 → the Phrean I 505–520; the Shoran 520–600; the KE 600–620 re-grant interval; the Phrean II 620–680 | **RESOLVED + VERIFIED** |
| CC-04 | 4 | the textile monopoly (the ADM-01 §3) vs the ECO-01 §4 + the ECO-02 §2 (the Q-023 resolution — the textiles taxed, not monopolized) | the ADM-01 §3 corrected (the monopolies = the salt/horses/pepper) | **RESOLVED + VERIFIED** |
| CC-05 | 5 | the sea-wind's direction — the GEO-03 §1 "south/southwest" vs the GEO-01 §1/§7 + the TIM-07 (the sea to the south and east) | the GEO-03 §1 → south/southeast | **RESOLVED + VERIFIED** |
| CC-06 | 6 | the DEM-02 §2 urban arithmetic — the fixed ~10–12% / ~2.5–4M urban vs the tiering's ~2.0M capacity (the towns 1–10k) | the town tier widened 1–10k → 2–35k each (the urban total ~0.9–4.48M carries the share; the cities + the share unchanged) | **RESOLVED + VERIFIED** |
| CC-07 | 7 | the REGISTER's final-state table — the Open row count 4 lists 5 questions; the Total 86 vs Q-001 → Q-087 = 87; the stale heading; the missing TIM-08 section heading | Q-087 into its own deep-unknown row; the Open row = Q-081/082/085/086; the Total 87; the heading + the TIM-08 heading corrected | **RESOLVED + VERIFIED** |
| CC-08 | 8 | the long-reign cluster — the Threna I (125 years), the Vethan II / the Khesh Ur II (130 years) + the FOR-02 era-length ranges vs the DEM-02 §3 human lifespan | — (both resolution paths recorded; each exceeds this cycle's mandate without manufacturing canon — the no-filler rule / the stewardship principle) | **CARRIED UNRESOLVED** |

### Verification protocol — honored

No item was marked resolved without verification against the wider canon: each fix was followed by a grep sweep of the canon + the WORLD-MODEL confirming (a) the corrected fact now agrees everywhere it appears, (b) no dependent reference was left stale, (c) the counts/rates/anchors the fix touches remain consistent downstream (the KE 675 agreement across 8 files; the sanction's object across the REL-02/TIM-03/DYN-02/DYN-04; the Phre tenures across the FOR-02/TIM-03/DYN-04; the monopoly list across the ADM-01/ECO-01/ECO-02; the wind direction carrier-free after the fix; the urban tiering's arithmetic; the register's row sum = 87 = the 87 question files).

### Checked — NOT contradictions (the 8 near-misses cleared)

The 0.3% army ceiling's charitable reading (the mobilization ceiling ~105k); the "KE 0–680+"/"680+ years" open lower bounds (true statements about an era running past KE 680); the GEO-02 8-city table (no exhaustiveness claim; the Tarenam omission is not a contradiction); the TIM-01/TIM-02 ranges containing the TIM-03 exact dates; the GEO-03 §2 cadence row (a Deep-Age phase, self-clarified by the TIM-05 operation); the DYN-05 §2 stray text (a text defect, recorded, not a canon contradiction); the INTEGRATION.md dated record; the PROJECT.md session line.

## Result

**7 contradictions resolved + verified; 1 carried unresolved (CC-08).** The canon is more consistent than at the cycle's start; no established anchor, count, or rate was altered except where it carried a genuine contradiction; no new canon invented; no story prose written. The next cycle inherits the `CONTRADICTIONS.md` register.

**Cycle complete.**
