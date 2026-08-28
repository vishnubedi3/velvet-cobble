# Benchmark Cases — Manifest & Authoring Template

The case suite is described in [`../README.md`](../README.md) (harness
contract, case inventory, ground-truth discipline) and measured by the
metrics in [`../spec/09-evaluation-benchmark.md`](../../spec/09-evaluation-benchmark.md).
This directory holds the case files themselves. The skill functions without
them; a conformant implementation should populate this directory per the
inventory below.

## Required cases (per the inventory)

| Case ID | Type | Purpose |
|---|---|---|
| `seeded-redundancy` | tell-seeded | U02/E02/FS03 detection + Level 2 deletion + carrier audit |
| `seeded-uniform-dialogue` | tell-seeded | D01/D04/D06 detection + Level 3 re-voicing + metric A7 |
| `seeded-template-structure` | tell-seeded | N04/R02 detection + Level 4 variance + causality audit |
| `seeded-ledger-breaks` | tell-seeded, long-form | L04/L05/L09/A02 detection + Level 1–2 state corrections |
| `seeded-skeleton-recycle` | tell-seeded, long-form | L03/SC05 + Level 4 beat reorder |
| `trap-01` … `trap-08` | adversarial | traps A-T1…A-T8 as full drafts (zero-edit expectation) |
| `genre-*` (13) | genre matrix | one per genre in the contract table ([`frameworks/07-genre-awareness.md`](../../frameworks/07-genre-awareness.md) §1), each with a contractual element that must survive |
| `human-control-*` | false-positive | human-written drafts with deliberate "AI-looking" devices that must be preserved |
| `calibration-*` | cross-model | per-generator baseline cases ([`taxonomy/17-genre-and-model-variation.md`](../../taxonomy/17-genre-and-model-variation.md) §17.3) |
| `longform-*` | long-form | 10k+ word drafts with planted drift/repetition/contradictions |

## Case file format (one JSON file per case)

```json
{
  "case_id": "seeded-redundancy",
  "type": "tell-seeded",
  "skill_input": { "...": "a full SkillInput per schemas/skill-input.schema.json" },
  "ground_truth": {
    "planted_spans": ["<exact draft spans where tells were injected>"],
    "expected_level_max": 2,
    "protected_spans": ["<spans that must NOT be edited>"]
  },
  "metrics": ["A1", "P1", "P2", "P3", "M2", "M3", "M4"]
}
```

## Authoring rules

1. **Planted tells must be real instances of the taxonomy pattern** — build
   them from the tell's "example pattern" field, not from word lists.
2. **Ground truth specifies the level ceiling, never the wording** — the
   skill may fix differently as long as function is restored and nothing
   outside the causal neighborhood changes.
3. **Protected spans** exist in every case (even seeded ones): a contractual
   device, a declared motif, or a voice anchor that must survive. A case
   without protected spans tests nothing about preservation.
4. **Human-control cases** must include the author's `declared_devices`
   entries so the intentionality path is exercised.
5. Add every new case to this manifest and to `benchmark/README.md`'s
   inventory table in the same commit ([`tests/02-static-consistency-checklist.md`](../../tests/02-static-consistency-checklist.md) T-5 applies to this directory too).
