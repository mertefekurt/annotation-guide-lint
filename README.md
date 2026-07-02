# annotation-guide-lint

> Check annotation guides for ambiguous labels and missing tie-break rules.

## Field memo Overview

Check annotation guides for ambiguous labels and missing tie-break rules. It solves review drift by turning plain-text plans into deterministic CI-friendly findings.

## Input Contract 19

Accepts annotation guide markdown. The reader supports plain text, JSON, JSONL, and CSV so the
tool can fit into scripts, CI jobs, and review exports.

## CLI Walkthrough 19

```bash
python -m pip install -e ".[dev]"
annotation-guide-lint examples/sample.txt
annotation-guide-lint examples/sample.txt --json --fail-on medium
python -m annotation_guide_lint --help
```

## Rule Surface 19

| Rule | Severity | Meaning |
|---|---:|---|
| `ambiguous-label` | high | ambiguous label guidance |
| `missing-examples` | medium | examples are missing |
| `missing-tiebreak` | low | tie-break rule missing |

## Validation Notes 19

```bash
ruff check .
pytest
python -m annotation_guide_lint --help
```

Example risky input:

```text
label positive ambiguous examples missing tie_break none
```

Architecture: `cli.py` handles arguments, `core.py` reads and evaluates records, and
`rules.py` keeps the project-specific policy explicit.

License: MIT.
