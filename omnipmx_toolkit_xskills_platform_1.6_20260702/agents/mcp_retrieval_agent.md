# MCP Retrieval Agent

Use this agent when the xskills platform has external MCP tools enabled. MCP tools are platform-managed; this Skill package cannot install them automatically. The agent must first inspect available tool names and capabilities from MCP Preview or the platform calling interface.

## Retrieval Priority

Use tools in this order when available:

1. Platform `互联网搜索工具 web-tools` for PubMed/web searching and citation or webpage retrieval when available.
2. `omnipmx-regulatory-literature` / OmniPMX Regulatory/Literature Documents MCP for FDA document URLs, PMC/Europe PMC/Unpaywall full-text location, and official URL fetch.
3. `omnipmx-regulatory-literature` fallback tools for platform gaps: `pubmed_esearch_full`, `pdf_url_extract_text`, and `pubchem_compound_properties`.
4. `omnipmx-document-runtime` for OCR, DOCX/PDF generation, PNG chart rendering, and optional code execution.
5. Web search and webpage fetch MCP for non-indexed official source discovery.
6. EMA, EPAR, or regulatory document MCP when available.
7. Reference-manager or table parsing MCP.

If a needed tool is unavailable, record `MCP_MISSING` and fall back to `references/manual_search_handoff.md`.

## Required MCP Audit Log

For every MCP call, record:

| call_id | tool_name | purpose | exact_query_or_url | run_datetime | returned_count | output_file_or_record_ids | status | notes |
|---|---|---|---|---|---|---|---|---|

Do not summarize away failed calls. Failed or empty calls are part of the audit trail.

## PubMed MCP Workflow

When platform `互联网搜索工具 web-tools` or another PubMed-capable MCP exists:

1. Build PICO/PICOM concept blocks.
2. Run block-level searches when feasible.
3. Run combined searches.
4. Record exact query, date/time, and result count from the MCP output.
5. Retrieve complete PMID metadata for the final combined query.
6. Export or display records with PMID, title, abstract, journal, year, DOI, authors, and MeSH/keywords when available.
7. Continue to screening only after counts and records reconcile.

If `互联网搜索工具 web-tools` can only return top results, not full exports, label the retrieval `PARTIAL_MCP_OUTPUT` and request full database export or use manual export handoff.

If a complete PubMed count and PMID list are needed and `互联网搜索工具 web-tools` is limited to top results, call `omnipmx-regulatory-literature.pubmed_esearch_full` with the exact final query and requested date limits.

## FDA/EMA Document Workflow

When `omnipmx-regulatory-literature`, regulatory MCP, or web tools exist:

1. Identify drug/product, active ingredient/payload if relevant, sponsor, approval region, and same-class comparators.
2. Search official FDA or EMA pages first.
3. Prefer official review packages, labels, EPAR assessment reports, and regulatory summaries over secondary pages.
4. For every document, record URL, title, agency, document type, date if available, and retrieval status.
5. Use PDF/OCR MCP to extract text before evidence extraction.
6. If only a landing page is found and no review PDF/text is available, label `DOCUMENT_NOT_RETRIEVED`.

Do not claim FDA/EMA approval, label content, or review-package existence unless the MCP output or uploaded official document supports it.

## FDA PDF Text Workflow

When `fetch_document` returns `PDF_BINARY_RETRIEVED`, next call `pdf_url_extract_text` on the same URL.

Use extracted page text for screening and parameter extraction only when:

- `status` is `PDF_TEXT_EXTRACTED`;
- relevant pages contain readable text;
- source URL and page number are retained in extraction rows.

If `status` is `NO_EXTRACTABLE_TEXT`, report `BLOCKED_WAITING_FOR_OCR` and request a PDF/OCR MCP or human OCR output.

If `omnipmx-document-runtime` is available, call `pdf_extract_or_ocr` or `ocr_pdf` before reporting the blocker. Preserve page numbers in extraction rows.

## PubChem Physicochemical Workflow

For logP, molecular weight, charge, TPSA, and related descriptors, call `pubchem_compound_properties` by compound name or CID.

Important limitations:

- PubChem `XLogP` is predicted/curated descriptor evidence, not necessarily an experimental logP.
- pKa is not reliably available through the simple property endpoint. If pKa is model-critical, keep it as a gap unless another citable source provides it.

## Report Rendering Workflow

When the user requests Word/PDF/figures:

1. Draft the canonical report body following `references/final_report_workflow.md`.
2. Generate chart source tables in CSV form.
3. Call `omnipmx-document-runtime.csv_to_plot_png` for PRISMA/evidence/validation PNGs when simple charts are sufficient.
4. Call `omnipmx-document-runtime.markdown_to_docx` for DOCX.
5. Call `omnipmx-document-runtime.markdown_to_pdf` for PDF.
6. If the MCP returns base64, present the filename, MIME type, and base64 artifact output according to platform conventions.

Do not claim human-grade visual QA unless the platform or user confirms rendered files were opened and checked.

## Code Execution Workflow

Use `python_execute` only when all are true:

- `omnipmx-document-runtime` is connected;
- server-side `ENABLE_CODE_EXECUTION=true`;
- the task needs calculations or a reproducible transformation not covered by specific tools;
- the code is included in the audit log.

If the tool returns `CODE_EXECUTION_DISABLED`, use deterministic non-code fallbacks or report the blocker.

## Web/PDF/OCR Workflow

When a web or PDF tool exists:

1. Fetch the URL or uploaded document.
2. Extract text with page numbers when possible.
3. Preserve source URL/filename and retrieval date.
4. If extraction quality is poor, request OCR or human text transcription.
5. Do not extract numeric parameters from unreadable figures without OCR/table text.

## Fallback Status Values

Use these status values:

- `MCP_READY`: required tool exists and connection works.
- `MCP_MISSING`: required tool is unavailable.
- `MCP_FAILED`: tool exists but call failed.
- `PARTIAL_MCP_OUTPUT`: tool output is incomplete for final evidence accounting.
- `MANUAL_EXPORT_REQUIRED`: user must upload a complete export or official document.
- `BLOCKED_WAITING_FOR_TEXT_EXTRACTION`: PDF/image/scanned content needs OCR or text extraction.
