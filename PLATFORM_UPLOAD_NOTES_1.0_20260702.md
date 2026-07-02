# OmniPMX toolkit-v0.1 xskills Upload Notes

## Package

Upload the zip file that contains this folder as its root:

```text
omnipmx_toolkit_xskills_platform_1.6_20260702/
```

For this revised MCP-aware package, the folder root is:

```text
omnipmx_toolkit_xskills_platform_1.6_20260702/
```

Required root file:

```text
SKILL.md
```

Important subfolders:

```text
agents/
references/
examples/
platform_validation/
```

## After Upload

1. Open Skill Management.
2. Upload the `.zip` package.
3. Enable `OmniPMX toolkit-v0.1`.
4. In a new chat, type `/` and select the skill.
5. Use `examples/validation_cases.md` to run at least 5 validation cases.
6. If output misses retrieval, OCR, PubMed, PDF, or webpage capabilities, enable the corresponding MCP tools in MCP Management and test their connections.

## MCP Setup

This zip cannot auto-install MCP servers. In xskills, MCP is managed separately from Skill files.

Before direct retrieval tasks, install or enable MCP tools for:

- PubMed/biomedical literature search;
- web search and webpage fetch;
- PDF text extraction/OCR;
- FDA/EMA or regulatory document retrieval when available;
- table/spreadsheet parsing.

Then use MCP Preview or a test chat to confirm the tool names. The Skill will follow `agents/mcp_retrieval_agent.md` and `references/mcp_tool_contracts.md` when those tools are available.

If the platform already provides PubMed/web MCP, keep using that for PubMed. In this setup the tool name is:

```text
互联网搜索工具 web-tools
```

Add the companion `OmniPMX Regulatory/Literature Documents` MCP only for FDA/official document lookup and article full-text location.

## DeepSeek Reminder

The package is text-first. For PDFs, figures, scans, screenshots, or Word/PDF report layout, provide text extraction, OCR, table export, or human QA confirmation before asking for final conclusions.
