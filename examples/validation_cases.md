# Validation Cases

Use these fixed cases after uploading the skill. The goal is to verify workflow behavior, not to prove scientific conclusions.

## Case 1: ADC Payload PBPK Search Handoff

Prompt:

```text
我要做 ADC 类药物的 PBPK，请以 MMAE 为 payload，找 payload 相关验证文献。请优先调用平台的 `互联网搜索工具 web-tools` 进行 PubMed/互联网检索；如需 FDA 审评文件或开放全文定位，请调用 `omnipmx-regulatory-literature` MCP。若工具输出不完整，再生成检索交接包和 manifest，不要编造检索数量。
```

Expected:

- Checks/uses `互联网搜索工具 web-tools` for PubMed/web retrieval if available.
- Checks/uses `omnipmx-regulatory-literature` for FDA/full-text location if needed.
- Records exact MCP call log and returned counts/URLs.
- Leaves counts as `待数据库回填` only when MCP output is unavailable or incomplete.
- Final status is not final until full screening/extraction gates pass.

## Case 2: Uploaded Export Screening

Prompt:

```text
我已上传 PubMed NBIB/CSV 导出和 manifest。请进行题录去重和标题摘要筛选，输出 coded screening 表和自检计数。
```

Expected:

- Uses screening codes.
- Every exclusion has excerpt.
- Count reconciliation table is present.
- Does not start extraction if count QC fails.

## Case 3: Full-Text Extraction

Prompt:

```text
我上传了 5 篇全文的文本提取文件，请提取 ADC payload PBPK 相关参数，按 ADaM-like 长表输出。
```

Expected:

- One value/result per row.
- Source quote per row.
- Units separated from numeric values.
- Missing context marked `not_reported`.

## Case 4: QSP Leakage Control

Prompt:

```text
我有一篇 published QSP 模型文章和多篇原始临床/PK 文献。请判断哪些可用于参数推导，哪些只能用于 held-out validation。
```

Expected:

- Splits derivation vs held-out validation.
- Does not import model-paper fitted parameters as independent evidence.
- Adds gaps when only model-paper evidence exists.

## Case 5: Final Report Request With Blockers

Prompt:

```text
请把目前 evidence package 输出为最终报告。但仍有 2 篇 P0 全文未获得，且报告页面未人工 QA。
```

Expected:

- Reads/follows final report workflow.
- Produces an interim report outline or blocker report.
- Labels status `INTERIM_NOT_FINAL`.
- Lists exact closure actions and expected filenames.

## Case 6: Final Report Ready

Prompt:

```text
所有检索导出、全文、提取长表、QC 抽样和人工页面 QA 均已完成。请生成 canonical QSP/PBPK 参数来源与验证数据整理报告。
```

Expected:

- Includes canonical report sections.
- Includes evidence tables, QC, finalization gate.
- Uses `FINAL_READY` only if all hard gates pass.

## Case 7: Fingolimod Cardiac PBPK Blocker Resolution

Prompt:

```text
我在芬戈莫德心脏 PBPK 项目中遇到阻断：平台 PubMed 每次只返回 5 条、FDA ClinPharm Review 只能返回 PDF_BINARY、需要 logP 等物化参数。请调用可用 MCP 尝试解锁：互联网搜索工具 web-tools、omnipmx-regulatory-literature.pubmed_esearch_full、pdf_url_extract_text、pubchem_compound_properties。无法解决的请明确标为仍需人工处理。
```

Expected:

- Uses `pubmed_esearch_full` for full PubMed count/PMID fallback.
- Uses `pdf_url_extract_text` after FDA PDF URL retrieval.
- Uses `pubchem_compound_properties` for PubChem descriptors.
- Keeps paywalled article full text and scanned/OCR failures as unresolved blockers.
- Does not claim Word/PDF/ggplot final report generation inside a no-code xskills mode.

## Case 8: OCR And Report Runtime

Prompt:

```text
请检查是否已连接 `omnipmx-document-runtime`。如果已连接，请说明可用工具，并用一个短 Markdown 示例生成 DOCX/PDF；如果有表格数据，请用 csv_to_plot_png 生成 PNG。若代码执行未启用，请不要调用 python_execute，并说明仍为禁用状态。
```

Expected:

- Lists document runtime tools.
- Uses `markdown_to_docx` and `markdown_to_pdf` for small report artifacts.
- Uses `csv_to_plot_png` for chart rendering when CSV is provided.
- Does not claim visual QA unless user confirms.
- Treats `python_execute` as optional and disabled unless MCP reports it is enabled.
