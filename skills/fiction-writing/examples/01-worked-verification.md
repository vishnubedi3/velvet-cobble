# Worked verification (synthetic)

This example uses the Helwick fixture world, not the project's canon.

## Request

> Write a scene in YA 110 in which Lia rides out from Helwick to renew House Pell's alliance with House Ryn.

## T0 (applicable branch `main` @ `c0`)

Resolved facts (illustrative): Lia alive; located in Helwick; House Pell allied with House Ryn. Charter allows narrative.

**Decision:** PASS. Contract binds those three facts to `c0` hashes. Permitted space: dialogue, weather-as-function, unnamed extras. Forbidden: treating a draft as canon; resolving an INTENTIONALLY UNRESOLVED question if one were in scope.

## T1 (same branch @ `c1`)

A later source records Lia dead from YA 105 and the alliance broken.

Re-run the same request.

**Decision:** BLOCK (`CX-DIRECT` on vital_status and/or allied_with). The T0 contract is stale (hash mismatch). No generation.

## Splash (same request, `main` unchanged, Arena Splash live)

An `arena/*` head appears. It restates Lia alive and *clarifies* the same fact.

**Decision:** PASS. Extra live head is **not** `REQUIRES_CLARIFICATION`. Contract `source_status.CANON_CLARIFICATION` records the Splash note. It is not mixed unlabeled into CANONICAL.

If instead Splash said Lia dead: PASS_WITH_WARNINGS, class `CONTRADICTORY`, `main` remains baseline. Newer Splash does not override.

## What this demonstrates

The skill did not store "Lia is alive" as a skill rule. It derived the constraint from T0 sources and **changed its conclusion** when the sources changed. Splash is classified against `main`; it is neither merged nor ignored.
