# DeepSeek Text-Only Compensation

The xskills platform commonly uses DeepSeek-class text models. Assume no reliable multimodal vision and no hidden local code execution unless an MCP explicitly provides it.

## Main Limitation

DeepSeek can reason over text, tables, Markdown, CSV-like content, and tool outputs. It should not be asked to inspect report page layout, screenshots, scanned PDFs, gel images, plots, or complex figure panels without OCR/text extraction.

## Required Compensation Pattern

| Input type | Required conversion before analysis |
|---|---|
| searchable PDF | text extract by platform PDF tool, local PDF skill, or user-provided text |
| scanned PDF/image | OCR text plus page number and confidence if available |
| figure/table image | OCR/table extraction or human-transcribed table |
| Word/PDF final report | text export plus human visual QA checklist |
| webpage evidence | browser/MCP text scrape plus captured URL/date |
| spreadsheet | CSV/TSV table export |

If conversion is unavailable, label the step `BLOCKED_WAITING_FOR_TEXT_EXTRACTION`.

## MCP Recommendations For xskills

In MCP Management, install and enable tools that provide text outputs:

- Web search and webpage extraction.
- PubMed or biomedical literature retrieval.
- PDF text extraction or OCR.
- Reference-manager import/export processing if available.
- Spreadsheet/table parsing.
- FDA/EMA/regulatory document search if available.

After installing an MCP, use "test connection" before relying on it.

See `references/mcp_tool_contracts.md` for the exact capabilities this Skill expects. If an installed MCP has different tool names, map the available functions to the contract before retrieval.

## GitHub Skills Installed Locally For Compensation

The following GitHub skills were installed in local Codex to support preparation, validation, and preprocessing outside the xskills platform:

| Skill | Status | Use |
|---|---|---|
| `pdf` | already installed | PDF text extraction and render/check workflows |
| `playwright` | already installed | browser automation and webpage evidence capture |
| `jupyter-notebook` | installed from GitHub | reproducible data/table processing and audit notebooks |
| `screenshot` | installed from GitHub | page capture and human evidence traceability |

## Companion MCP For Missing Retrieval

If the platform already has PubMed/web MCP, do not duplicate PubMed retrieval. In this xskills setup, use:

```text
互联网搜索工具 web-tools
```

for PubMed and web search. Add the custom `OmniPMX Regulatory/Literature Documents` MCP for:

- FDA Drugs@FDA application document URLs;
- FDA official review/label/approval document fetch;
- PMC Open Access full-text link lookup;
- Europe PMC full-text URL lookup;
- DOI open-access lookup through Unpaywall;
- bounded official URL/PDF retrieval.
- page-numbered text extraction from text-based PDFs via `pdf_url_extract_text`;
- PubMed full hit count and PMID fallback via `pubmed_esearch_full` when `互联网搜索工具 web-tools` returns only top results;
- PubChem physicochemical descriptors via `pubchem_compound_properties`.

## Unresolved Limits

The following cannot be solved by the Skill or MCP without additional access:

- closed/paywalled full text such as subscription-only Clin Pharmacokinet articles;
- scanned PDFs with no embedded text unless an OCR MCP or human OCR output is available;
- platform-native Word/PDF/ggplot generation when the platform has no code execution/rendering environment.

## Document Runtime MCP Resolution

When `omnipmx-document-runtime` is installed, the previous platform limitations are reduced:

- OCR: use `ocr_image`, `ocr_pdf`, or `pdf_extract_or_ocr`.
- DOCX: use `markdown_to_docx`.
- PDF: use `markdown_to_pdf`.
- PNG figures: use `csv_to_plot_png`.
- Code execution: use `python_execute` only if enabled on the MCP server.

Remaining limitations:

- Generated DOCX/PDF still require human visual QA before claiming final publication-ready formatting.
- OCR quality depends on scan quality and language packs.
- `python_execute` may be disabled for safety.

Restart Codex to make newly installed local skills appear in future Codex sessions.

## Prompting Rules

1. Work one phase at a time for large corpora.
2. Use stable IDs such as `SRC001`, `STUDY001`, `ARM001`, `ASM001`.
3. Demand source excerpts for exclusions and extracted values.
4. Use `not_reported` or `insufficient_evidence` rather than guessing.
5. End every final or interim output with a gate table.
6. If visual evidence is needed, request OCR/table extraction or human QA.

## Report QA Without Vision

When Word/PDF report rendering is unavailable in the platform, output this checklist for human verification:

| Check | Pass/Fail | Notes |
|---|---|---|
| title page and version/date correct |  |  |
| section order matches final report workflow |  |  |
| all tables fit page width |  |  |
| all figure captions match text |  |  |
| references/citations visible |  |  |
| no placeholder text remains |  |  |
| finalization status visible |  |  |

Do not mark visual QA as passed until the user confirms it.
