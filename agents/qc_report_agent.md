# QC And Report Agent

Use this agent for QC sampling, finalization gates, and final/interim report drafting.

## QC Sample

When extraction rows exist, create a 20% QC sample or at least 10 rows, whichever is smaller for small projects. Stratify across:

- numeric PK/ADME parameters;
- mechanism/pathway statements;
- human evidence;
- nonclinical or in vitro evidence;
- high-impact model assumptions;
- validation/comparison anchors.

Each QC row must include extracted value, source quote, and pass/fail comment.

## Canonical Report Requirement

Before drafting any final report, read `references/final_report_workflow.md`.

The expected final report is the canonical `QSP参数来源与验证数据整理报告` style report with structured sections, evidence tables, QC status, figures/tables where possible, and a finalization gate. A Markdown search summary is not enough.

## Text-Only Figure Fallback

If the platform cannot render or inspect figures, provide text/table equivalents:

- PRISMA as counts plus Mermaid flow.
- Evidence coverage as a matrix table.
- Parameter evidence as a long table.
- Validation comparison as benchmark-vs-evidence table.

Do not claim visual QA of Word/PDF pages unless a human or external renderer has inspected them.

## Finalization Status

Use:

- `FINAL_READY`: all hard gates pass.
- `INTERIM_NOT_FINAL`: useful report can be produced, but blockers remain.
- `BLOCKED_WAITING_FOR_INPUT`: cannot continue without exports, full texts, OCR, or user decisions.

Report blockers before conclusions.
