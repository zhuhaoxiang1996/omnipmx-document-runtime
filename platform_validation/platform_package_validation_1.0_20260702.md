# Platform Package Validation

Package: `omnipmx_toolkit_xskills_platform_1.6_20260702`

Skill name: `OmniPMX toolkit-v0.1`

Validation date: 2026-07-02

## Structural Checks

| Check | Status | Evidence |
|---|---|---|
| root `SKILL.md` exists | PASS | `SKILL.md` |
| YAML front matter has `name` | PASS | `OmniPMX toolkit-v0.1` |
| YAML front matter has `description` | PASS | text-first PBPK/PBBM/QSP evidence toolkit |
| `agents/` directory exists | PASS | 6 role files |
| `references/` directory exists | PASS | platform, handoff, compensation, MCP contracts, final report workflow |
| examples included | PASS | `examples/validation_cases.md` |
| hidden files excluded | PASS | no hidden files detected |
| final report workflow corrected | PASS | copied from confirmed `final_report_workflow.md` source |

## DeepSeek/Text-Only Checks

| Check | Status | Evidence |
|---|---|---|
| no multimodal dependency required | PASS | `references/deepseek_compensation.md` |
| OCR/text extraction fallback included | PASS | conversion table included |
| manual search handoff included | PASS | `references/manual_search_handoff.md` |
| no invented PubMed counts allowed | PASS | `SKILL.md` and search agent rules |
| MCP-aware retrieval path included | PASS | `agents/mcp_retrieval_agent.md`, `references/mcp_tool_contracts.md` |
| platform PubMed/web tool name included | PASS | `互联网搜索工具 web-tools` |
| blocker-resolution MCP tools included | PASS | `pubmed_esearch_full`, `pdf_url_extract_text`, `pubchem_compound_properties` |
| document runtime MCP included | PASS | `omnipmx-document-runtime` OCR/DOCX/PDF/PNG/code tools |
| finalization gate required | PASS | coordinator and report agent |
| final report is not a Markdown-only summary | PASS | `references/final_report_workflow.md` |

## Upload Validation To Run On xskills

1. Upload the `.zip` package in Skill Management.
2. Enable `OmniPMX toolkit-v0.1`.
3. Start a new chat and select it with `/`.
4. Run at least 5 prompts from `examples/validation_cases.md`.
5. In detailed mode, confirm the expected agent/reference files are read.
6. Check that missing exports/full texts/OCR produce `INTERIM_NOT_FINAL` or `BLOCKED_WAITING_FOR_INPUT`, not a false final report.

## Local GitHub Skill Compensation

| Skill | Status |
|---|---|
| `pdf` | already installed locally |
| `playwright` | already installed locally |
| `jupyter-notebook` | installed from GitHub |
| `screenshot` | installed from GitHub |

Restart Codex to pick up newly installed local skills in future sessions.
