# Extraction Agent

Use this agent for ADaM-like vertical extraction from uploaded full texts, text extracts, regulatory reviews, tables, and reference exports.

## Atomic Row Rule

One row equals one source, one study/experiment, one arm/group/condition/timepoint, one parameter or result, one statistic/value, and one unit. Split lists into separate rows.

## Required Columns

| Column | Requirement |
|---|---|
| source_id | stable `SRC###` |
| citation | author/year or regulatory document |
| PMID_or_document_id | PMID, DOI, FDA/EMA ID, or filename |
| evidence_domain | literature, FDA, EMA, in vitro, animal, clinical, model |
| study_id | stable `STUDY###` |
| species_system | human, mouse, cynomolgus, cell line, in vitro matrix |
| disease_context | indication or biological context |
| analyte | parent drug, ADC, total antibody, payload, catabolite |
| matrix | plasma, serum, tissue, tumor, cell, microsome |
| parameter_name | CL, V, half-life, IC50, DAR, binding, expression, toxicity endpoint |
| statistic | mean, median, geometric mean, SD, SE, CI, range, n |
| value | numeric or categorical value only |
| unit | unit, including `%` when applicable |
| timepoint | time after dose, cycle, experiment duration |
| condition | dose, regimen, assay condition, comparator |
| source_quote | short text excerpt supporting the row |
| extraction_note | caveat or derivation note |

## Validation Rules

- Numeric value fields must not include units.
- Percent signs belong in `unit`.
- Ranges and CIs should be split into separate fields or clearly labeled statistics.
- Do not convert units unless the conversion formula and source unit are reported.
- If a table is only available as an image, request OCR or a text/table extract before extraction.
- Mark unavailable context as `not_reported`, not blank.

## Minimum PBPK/ADC Families

For ADC payload PBPK projects, try to capture:

- ADC and payload plasma PK.
- Cleavable/non-cleavable linker behavior.
- Payload release and catabolite evidence.
- Plasma protein binding and blood/plasma partitioning.
- Hepatic metabolism, transporter, biliary/fecal/renal elimination.
- Tissue distribution, tumor uptake, bystander effect, payload permeability.
- Safety/toxicity endpoints relevant to exposure validation.
- Same-payload or same-linker comparator evidence when direct evidence is sparse.
