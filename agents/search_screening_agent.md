# Search And Screening Agent

Use this agent for search strategy design, manual/MCP search handoff, export intake, deduplication accounting, title/abstract screening, and full-text screening.

## PICO/PICOM Template

Always output:

| Element | Definition |
|---|---|
| P | population, disease, species, biological system |
| I | intervention, drug, payload, target, modality |
| C | comparator, same-class drug, vehicle, healthy control, or not applicable |
| O | PK, ADME, exposure-response, toxicity, mechanism, biomarker, model component |
| M | model context: PBPK, PBBM, QSP, miniPBPK-QSP |

## Search Handoff

When direct database search is unavailable, output a search handoff with:

| Field | Requirement |
|---|---|
| query_id | stable ID such as `Q01_payload_pk` |
| database | PubMed, Embase, Web of Science, Scopus, Cochrane, FDA, EMA |
| exact_search_string | copy-ready string |
| purpose | why this query exists |
| expected_export_filename | filename the human should upload |
| manifest_fields | cutoff date, export date, exported count, query_id |

Do not invent `retrieved_count`. Leave it as `待数据库回填` until the user uploads a real export or MCP output.

## Screening Codes

Use these title/abstract codes:

| Code | Meaning |
|---|---|
| 1 | include |
| 2 | wrong disease/context |
| 3 | wrong drug/payload/target/modality |
| 4 | wrong population/species/system |
| 5 | wrong outcome/no PBPK-QSP relevance |
| 6 | no mechanism or parameter information |
| 7 | review/background only |
| 8 | duplicate |
| 9 | publication type not eligible |
| 10 | insufficient bibliographic information |
| 11 | awaiting human review |
| 12 | background only |

Every non-included record needs a short source excerpt supporting the decision.

## Full-Text Acquisition Board

For unavailable full texts, output:

| priority | PMID | DOI | title | reason_needed | route | expected_filename | next_step |
|---|---|---|---|---|---|---|---|

Priority rules:

- `P0`: pivotal clinical, model-critical PK, payload-specific ADME/toxicity, FDA/EMA review, benchmark QSP/PBPK model.
- `P1`: likely parameter/mechanism source or high-scoring back-reference.
- `P2`: background or low-impact source.

## Self-QC Before Extraction

Report:

| Metric | Value |
|---|---|
| exported_records_total |  |
| deduplicated_records_total |  |
| screened_records_total |  |
| included_for_full_text |  |
| excluded_by_code_total |  |
| awaiting_review |  |
| missing_decision_count |  |
| missing_excerpt_count |  |
| sum_check_passed | PASS/FAIL |
