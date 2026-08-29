# Post-generation verification

A second layer. It does **not** replace the pre-generation gate.

Inputs: generated output (structured claims), the **same** Generation Contract, the **same** Canon State identity.

```
output + locked contract + evaluated Canon State
        ↓
stale? → stop (re-resolve; do not honor the old PASS)
bypass? (redefines constraints) → BLOCK CX-BYPASS
        ↓
run the same verify() against the output-as-request
        ↓
contamination? (presents working/generated material as established) → BLOCK
        ↓
decision
```

Checks (minimum):

- Introduced contradictions vs `main`
- New unsupported high-impact facts
- Knowledge / timeline / relationship / state / causal breaks
- Unauthorized canon change
- Arena/main misclassification (provisional presented as established)
- Canon contamination
- Contract identity mismatch

A pre-generation PASS does not waive this. A post-generation PASS does not admit the text to `02-canon/`.
