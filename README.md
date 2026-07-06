# Annotation Guide Lint

| | |
| --- | --- |
| Focus | annotation quality |
| Command | `annotation-guide-lint` |
| Inputs | text, JSON, JSONL, or CSV |
| Output | Markdown or JSON |

![Annotation Guide Lint cover](assets/readme-cover.svg)

Check annotation guides for ambiguous labels and missing tie-break rules. The repository is intentionally plain: a small command, a visible rule surface, and enough examples to make the behavior inspectable.

## Policy surface

| Rule | Level | Why it matters |
| --- | --- | --- |
| `ambiguous-label` | high | ambiguous label guidance |
| `missing-examples` | medium | examples are missing |
| `missing-tiebreak` | low | tie-break rule missing |

## Local run

```bash
git clone https://github.com/mertefekurt/annotation-guide-lint.git
cd annotation-guide-lint
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
annotation-guide-lint examples/sample.txt
annotation-guide-lint examples/sample.txt --json
```

## Why the sample fails

`label positive ambiguous examples missing tie_break none` is intentionally shaped to hit the rules above, so it is useful as a quick smoke test after edits.
