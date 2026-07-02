---
name: OmniPMX toolkit-v0.1
description: Text-first PBPK/PBBM/QSP evidence toolkit for xskills/DeepSeek platforms. Use for project intake, PICO/PICOM search design, manual or MCP-assisted literature retrieval handoff, reference-manager export processing, title/abstract and full-text screening, ADaM-like vertical extraction, regulatory/literature evidence integration, model-assumption mapping, QC, and canonical QSP/PBPK report drafting.
---

# OmniPMX Toolkit v0.1

## Purpose

Use this skill as the single entry point for PBPK, PBBM, and QSP evidence projects from project startup to final report. The platform model is assumed to be DeepSeek or another text-only model, so all work must be based on text files, tables, uploaded exports, Markdown references, and MCP text outputs.

Never provide a clinical dose recommendation. For dose-related requests, provide evidence collection, model-assumption support, uncertainty assessment, and expert pharmacometric review needs.

## Platform Operating Mode

This package follows the xskills operator manual upload contract: a zipped Skill folder with `SKILL.md`, `agents/`, `references/`, and optional examples. After upload, enable the skill in Skill Management, then validate it with at least 5 fixed cases before using it as a final workflow.

The skill must not depend on multimodal image reading. If the user uploads PDFs, screenshots, scanned pages, figures, or report pages, first request text extraction, OCR, a table export, or a platform MCP/tool output. If visual layout matters, generate a human QA checklist rather than claiming the model has visually inspected the page.

## Stage Router

Classify the user request into the earliest active stage and read the listed file first.

| Stage | Use when the user asks for | Read first |
|---|---|---|
| Project startup | modeling question, scope, friendly intake, deliverable definition | `agents/coordinator.md` |
| Search design | PICO/PICOM, PubMed/Embase/WoS query, search handoff | `agents/search_screening_agent.md` and `references/manual_search_handoff.md` |
| MCP retrieval/runtime | PubMed/web search via `互联网搜索工具 web-tools`, FDA/full-text retrieval via `omnipmx-regulatory-literature`, OCR/DOCX/PDF/PNG/runtime via `omnipmx-document-runtime` | `agents/mcp_retrieval_agent.md` and `references/mcp_tool_contracts.md` |
| Export processing | uploaded RIS/BibTeX/NBIB/CSV/TSV, deduplication, manifest checks | `agents/search_screening_agent.md` |
| Screening | title/abstract screening, full-text screening, PRISMA counts | `agents/search_screening_agent.md` |
| Extraction | ADaM-like vertical extraction, source-value-context rows | `agents/extraction_agent.md` |
| Model mapping | assumption evidence, PBPK/QSP component mapping, leakage control | `agents/qsp_mapping_agent.md` |
| QC and report | finalization gate, figures/tables, canonical report | `agents/qc_report_agent.md` and `references/final_report_workflow.md` |
| Platform limitation | DeepSeek text-only fallback, MCP/GitHub skill compensation | `references/deepseek_compensation.md` |
| Worked examples | validation prompts and expected checks | `examples/validation_cases.md` |

## Core Workflow

1. Parse the drug, payload/target/modality, disease, population, model type, development context, and requested deliverable.
2. Define eligibility criteria before screening. If criteria change later, version the change and record why.
3. Build PICO/PICOM questions and keep search concept blocks separate before combining.
4. Before manual handoff, check available MCP tools. Prefer platform `互联网搜索工具 web-tools` for PubMed/web retrieval and `omnipmx-regulatory-literature` for FDA document URLs and open full-text location. Use `agents/mcp_retrieval_agent.md` to run retrieval and record exact tool outputs.
5. If the platform cannot execute database searches directly, output a manual search handoff package with exact strings, database targets, export filenames, manifest fields, and must-not-do rules.
6. Accept only complete database/reference-manager exports or auditable MCP retrieval outputs for screening. Hit counts, screenshots, or hand-picked citations are not enough for a final package.
7. Screen every record with coded reasons and short source excerpts. Reconcile counts before moving to full text.
8. Track unavailable high-priority full texts in a retrieval board. Do not hide unresolved records from denominators.
9. Extract one row per source, study/arm/condition/time, parameter/result, statistic/value, unit, and source quote.
10. Preserve uncertainty fields: SD, SE, 95% CI, range, IQR, sample size, timepoint, matrix, assay method, and species/system.
11. Separate derivation evidence from held-out QSP/model validation evidence. Never import QSP model-paper parameters as independent observed evidence unless they are explicitly observed calibration/validation data.
12. Map evidence to model assumptions, PBPK/QSP components, parameter candidates, contradictions, and gaps.
13. Before any report deliverable, read `references/final_report_workflow.md`. The canonical report is a structured Word/PDF-style parameter-source and validation report, not a casual Markdown literature summary.
14. Run the finalization gate. If hard blockers remain, label the output `INTERIM_NOT_FINAL`.

## Non-Negotiable Rules

- Do not invent search result counts, search dates, PMIDs, DOIs, full-text availability, approval status, or regulatory documents.
- Do not say a database search was executed unless a real platform MCP/tool output or user-provided export proves it.
- Do not merge multiple parameter values into one numeric cell.
- Put `%` in unit fields, not numeric value fields.
- Every exclusion needs a coded reason and a supporting excerpt.
- Every extracted value needs a source quote or a clear source location.
- If the model cannot read a figure/image/table visually, request OCR/text/table extraction.
- User-facing deliverables created in this workspace must follow `<stem>_<version>_<YYYYMMDD><extension>` unless the platform requires a fixed name.

## Required Output Contract

For a final or interim evidence package, include:

1. Modeling question and assumptions.
2. Search strategy, cutoff date, manifest, and retrieval status.
3. Export import/deduplication status.
4. Eligibility criteria version.
5. PRISMA-style flow and screening counts.
6. Included evidence table.
7. ADaM-like long-table extraction summary.
8. Mechanism/source matrix.
9. Parameter candidate table.
10. Assumption-evidence mapping.
11. Evidence gaps and uncertainty.
12. QC sample or reason it cannot be generated.
13. Published-result comparison when a held-out benchmark exists.
14. Safety boundary.
15. Finalization-gate status.

Use this boundary text:

> This evidence package supports PBPK/QSP model preparation. It does not recommend a clinical dose, does not determine the final model structure, and does not replace expert pharmacometric review.
