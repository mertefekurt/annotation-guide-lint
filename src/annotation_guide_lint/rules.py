from __future__ import annotations

from annotation_guide_lint.models import Rule

PROJECT_NAME = 'annotation-guide-lint'
SUMMARY = 'Check annotation guides for ambiguous labels and missing tie-break rules.'
SAMPLE_RISK = 'label positive ambiguous examples missing tie_break none'
SAMPLE_CLEAN = 'label positive definition clear examples 5 tie_break reviewer'
TEXT_FIELDS = ("text", "content", "description", "summary", "body", "notes", "message")
SUBJECT_FIELDS = ("id", "name", "path", "service", "endpoint", "field", "event")

RULES = (
    Rule(
        code='ambiguous-label',
        severity='high',
        pattern='ambiguous',
        message='ambiguous label guidance',
        recommendation='clarify label definition',
    ),
    Rule(
        code='missing-examples',
        severity='medium',
        pattern='examples\\s+(missing|none|0)',
        message='examples are missing',
        recommendation='add positive and negative examples',
    ),
    Rule(
        code='missing-tiebreak',
        severity='low',
        pattern='tie_break\\s+(none|missing|unknown)',
        message='tie-break rule missing',
        recommendation='define adjudication rule',
    ),
)
