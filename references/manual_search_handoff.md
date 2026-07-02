# Manual Search And Export Handoff

Use this file when the platform cannot directly run PubMed, Embase, Web of Science, Scopus, FDA, EMA, Zotero, or EndNote.

## Search Design Output

For every database query, provide:

| Field | Required content |
|---|---|
| query_id | stable ID such as `Q01_payload_pk` |
| database | PubMed, Embase, Web of Science, Scopus, FDA, EMA |
| concept_blocks | P/I/C/O/M blocks before combination |
| exact_search_string | copy-ready search |
| purpose | what evidence gap this query addresses |
| cutoff_date | date limit requested |
| expected_export_filename | filename user should upload |
| expected_format | RIS, NBIB, BibTeX, CSV, TSV, PDF text extract |

## Human Execution Instructions

Tell the user to:

1. Copy each exact search string into the named database.
2. Record search date, cutoff date, and retrieved count.
3. Export complete results, not selected citations.
4. Upload the export files with a manifest.
5. Upload full-text PDFs or text/OCR extracts for included or review-needed records when requested.

## Export Manifest

Require one manifest table:

| query_id | database | exact_search_string | search_date | cutoff_date | exported_count | export_filename | notes |
|---|---|---|---|---|---|---|---|

If any row is missing `exported_count` or `export_filename`, the search-import stage is not final.

## Must-Not-Do Rules

- Do not treat screenshots as database exports.
- Do not use hand-picked citations as the denominator.
- Do not invent counts when exports are unavailable.
- Do not merge multiple databases without preserving `query_id`.
- Do not proceed to final PRISMA until deduplication and screening counts reconcile.

## Ready-To-Upload Prompt

Use this text when handing off:

```text
请在数据库中逐条执行下面的检索式，并上传完整导出文件。每个导出文件请同时填写 manifest：query_id、数据库、检索日期、截止日期、导出记录数、文件名。没有完整导出前，本 Skill 只能生成检索交接包，不能声称完成系统检索或最终报告。
```
