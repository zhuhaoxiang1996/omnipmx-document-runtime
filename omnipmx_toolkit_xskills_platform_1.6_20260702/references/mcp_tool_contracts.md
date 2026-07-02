# MCP Tool Contracts

This file defines the capabilities OmniPMX expects from external MCP tools. The Skill can reference these contracts, but the platform user must install or enable the actual MCP tools in xskills MCP Management.

## Required Tool Classes

| Tool class | Minimum capability | Required for final? |
|---|---|---|
| biomedical literature search | run exact PubMed-like query and return count plus complete record metadata | yes for direct platform retrieval; use the platform's existing PubMed MCP when available |
| web search/fetch | search web and fetch official source pages as text | yes for regulatory retrieval |
| PDF text extraction/OCR | convert uploaded or fetched PDF/scanned pages into page-numbered text | yes for PDF evidence extraction |
| regulatory document retrieval | search FDA/EMA official documents and return title, URL, agency, document type | recommended |
| table/spreadsheet parsing | read CSV/TSV/XLSX-style tables as text rows | recommended |

## Recommended MCP Split

Use the xskills platform's existing PubMed/web MCP for PubMed search execution, PubMed citation metadata, and general web retrieval:

```text
互联网搜索工具 web-tools
```

Use the companion `OmniPMX Regulatory/Literature Documents` MCP for the missing pieces:

| Tool | Purpose |
|---|---|
| `fda_drugsfda_search` | search openFDA Drugs@FDA application records |
| `fda_document_urls` | list FDA review, label, approval, and other application document URLs |
| `pmc_oa_lookup` | locate NCBI PMC Open Access downloadable files |
| `europepmc_lookup` | locate Europe PMC open full-text URLs |
| `unpaywall_lookup` | locate DOI open-access full text |
| `article_fulltext_locator` | combine PMC OA, Europe PMC, and Unpaywall for one article |
| `fetch_document` | fetch official HTML/text pages or retrieve bounded PDF binary metadata/base64 |
| `pdf_url_extract_text` | extract page-numbered text from text-based FDA/literature PDF URLs |
| `pubmed_esearch_full` | obtain PubMed total hit count and PMID list when platform PubMed returns only top-N |
| `pubchem_compound_properties` | retrieve PubChem descriptors such as XLogP, molecular weight, TPSA, charge, H-bond counts |

Recommended xskills MCP configuration:

| Role | xskills tool/server name |
|---|---|
| PubMed and web search | `互联网搜索工具 web-tools` |
| FDA review document URLs and open full-text location | `omnipmx-regulatory-literature` |
| FDA PDF text extraction | `omnipmx-regulatory-literature` -> `pdf_url_extract_text` |
| PubMed full count/PMID fallback | `omnipmx-regulatory-literature` -> `pubmed_esearch_full` |
| PubChem physicochemical descriptors | `omnipmx-regulatory-literature` -> `pubchem_compound_properties` |
| OCR images/PDFs | `omnipmx-document-runtime` -> `ocr_image`, `ocr_pdf`, `pdf_extract_or_ocr` |
| Generate DOCX/PDF report | `omnipmx-document-runtime` -> `markdown_to_docx`, `markdown_to_pdf` |
| Render PNG chart | `omnipmx-document-runtime` -> `csv_to_plot_png` |
| Optional Python execution | `omnipmx-document-runtime` -> `python_execute`, only if server env `ENABLE_CODE_EXECUTION=true` |

## Document Runtime MCP Contract

Recommended server name:

```text
omnipmx-document-runtime
```

Expected tools:

| Tool | Purpose |
|---|---|
| `ocr_image` | OCR image URL/base64 with Tesseract |
| `pdf_text_extract` | extract embedded PDF text without OCR |
| `ocr_pdf` | OCR rendered PDF pages |
| `pdf_extract_or_ocr` | extract embedded text first, OCR if text is absent/too short |
| `markdown_to_docx` | generate base64 DOCX from Markdown/text |
| `markdown_to_pdf` | generate base64 PDF from Markdown/text |
| `csv_to_plot_png` | render simple chart PNG from CSV text |
| `python_execute` | optional restricted Python execution; disabled unless explicitly enabled |

## PubMed Tool Contract

The ideal PubMed MCP exposes functions equivalent to:

| Function | Input | Output |
|---|---|---|
| search | exact query, date limits, max records | query_id, count, PMIDs |
| fetch_metadata | PMIDs | PMID, title, abstract, journal, year, DOI, authors, MeSH |
| export_records | query_id or PMIDs | CSV/NBIB/RIS-like records |

Minimum acceptable output for screening:

```text
PMID
title
abstract
journal
year
DOI if available
query_id
retrieval date/time
```

If abstracts or complete PMIDs are unavailable, the result is not enough for final screening.

## FDA Tool Contract

The ideal FDA MCP exposes functions equivalent to:

| Function | Input | Output |
|---|---|---|
| search_drug | drug name, active ingredient, application number | product matches and official URLs |
| list_documents | application number or product URL | labels, reviews, approval packages |
| fetch_document_text | document URL | page-numbered text or PDF file plus text extract |

Minimum acceptable output:

```text
agency = FDA
document title
official URL
document type
date if available
text extract or PDF retrieval status
```

## EMA Tool Contract

The ideal EMA MCP exposes functions equivalent to:

| Function | Input | Output |
|---|---|---|
| search_product | product, active substance, class | EPAR/product matches |
| list_documents | product URL | EPAR, assessment reports, labels, variation/safety documents |
| fetch_document_text | document URL | page-numbered text or PDF file plus text extract |

Minimum acceptable output:

```text
agency = EMA
product or active substance
document title
official URL
document type
date if available
text extract or PDF retrieval status
```

## Tool Availability Gate

At the start of any retrieval task, output:

| Tool class | Available? | Tool name | Test status | Impact |
|---|---|---|---|---|

If a tool is missing, continue only with the appropriate fallback:

- missing `互联网搜索工具 web-tools` or PubMed-capable MCP -> generate manual database handoff;
- missing web/FDA/EMA MCP -> generate official source acquisition board;
- missing PDF/OCR MCP -> request user-provided text extraction;
- missing `omnipmx-document-runtime` -> report OCR/DOCX/PDF/PNG/code rendering as blocked or produce Markdown-only fallback;
- missing table parser -> request CSV/TSV pasted text or upload.

## No False Capability Rule

The model must not say "I searched PubMed", "I downloaded the FDA review", or "I inspected the PDF" unless a tool call, uploaded file, or user-provided text proves it.
