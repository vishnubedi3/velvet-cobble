# Tests

Synthetic only. These tests must never load `samur/02-canon/`.

```
python3 skills/canon-guard/tests/run_adaptive_tests.py
```

| File | What it proves |
|---|---|
| [`01-adaptive-suite.md`](01-adaptive-suite.md) | Adaptive scenarios A01–A33 (main vs Arena working state) |
| [`02-static-consistency-checklist.md`](02-static-consistency-checklist.md) | Package integrity |
| [`03-decision-cases.md`](03-decision-cases.md) | Mystery, charter, epistemology extras |
| [`04-adversarial-suite.md`](04-adversarial-suite.md) | False-accept and false-reject (A31–A37) |
| [`run_adaptive_tests.py`](run_adaptive_tests.py) | Executable runner |
