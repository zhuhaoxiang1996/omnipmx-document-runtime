# OmniPMX Document Runtime MCP

This MCP fills xskills platform runtime gaps:

- OCR images.
- OCR PDFs.
- PDF embedded text extraction with OCR fallback.
- Markdown/text to DOCX.
- Markdown/text to PDF.
- CSV to PNG chart rendering.
- Optional restricted Python execution.

## Endpoint

```text
https://<your-render-domain>/mcp
```

## Tools

```text
ocr_image
pdf_text_extract
ocr_pdf
pdf_extract_or_ocr
markdown_to_docx
markdown_to_pdf
csv_to_plot_png
python_execute
```

## Render Environment Variables

```text
HOST=0.0.0.0
PORT=8790
MCP_API_TOKEN=
ENABLE_CODE_EXECUTION=false
CODE_EXECUTION_TIMEOUT=15
```

Keep `ENABLE_CODE_EXECUTION=false` unless you explicitly need code execution. If enabled, the tool runs Python snippets inside the Render container with a timeout, but it is still a security-sensitive capability.

## xskills MCP Form

```text
标识名: omnipmx-document-runtime
显示名称: OmniPMX Document Runtime MCP
连接地址: https://<your-render-domain>/mcp
协议类型: streamableHTTP
请求头:
Content-Type=application/json
```

If `MCP_API_TOKEN` is set:

```text
Authorization=Bearer <token>
```

## Suggested Tests

Generate PDF:

```json
{
  "name": "markdown_to_pdf",
  "arguments": {
    "filename": "test_report_1.0_20260702.pdf",
    "markdown": "# 测试报告\n\n这是一段中文测试。"
  }
}
```

Generate DOCX:

```json
{
  "name": "markdown_to_docx",
  "arguments": {
    "filename": "test_report_1.0_20260702.docx",
    "markdown": "# 测试报告\n\n- 项目一\n- 项目二"
  }
}
```

Render chart:

```json
{
  "name": "csv_to_plot_png",
  "arguments": {
    "filename": "evidence_counts_1.0_20260702.png",
    "csv": "category,count\nPK,12\nSafety,8\nMechanism,6",
    "x_field": "category",
    "y_field": "count",
    "chart_type": "bar",
    "title": "Evidence Counts"
  }
}
```
