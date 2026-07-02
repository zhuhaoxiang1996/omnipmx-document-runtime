# QSP Parameter Source Report And PDF Workflow

Use this reference whenever the user asks to create, revise, reproduce, or QA a QSP parameter-source and validation-data Word/PDF report, including reports like `QSP参数来源与验证数据整理报告_1.2_20260629.pdf`.

This reference fixes the detailed report-generation workflow. Do not replace it with a vague “make a report” step.

## Required Inputs

Start from the already reviewed extraction outputs. For the finalized 2026-06-29 workflow these lived under `qsp_vertical_extraction_1.0_20260628/`:

- `LI_1.0_20260628.csv`
- `TS_1.0_20260628.csv`
- `DM_1.0_20260628.csv`
- `MH_1.0_20260628.csv`
- `EX_1.0_20260628.csv`
- `BC_1.0_20260628.csv`
- `MECH_1.0_20260628.csv`
- `PD_1.0_20260628.csv`
- `PK_1.0_20260628.csv`
- `PUBMED_SIX_CATEGORY_RECLASSIFICATION_*.csv`
- `PUBMED_CATEGORY_EXTRACTION_STATUS_*.csv`
- `COMBINED_MECH_FDA_PUBMED_CATEGORY_*.csv`
- `COMBINED_PD_FDA_PUBMED_CATEGORY_*.csv`
- `MERGED_COMBINED_LI_TS_DM_MH_EX_PD_*.csv`
- `COMBINED_FDA_PUBMED_QC_*.txt`

If filenames or versions differ in the active project, adapt script constants but preserve the table roles.

## Pre-Report QC Gate

Do not build the report until the extraction tables pass deterministic QC.

1. Run the vertical extraction validator on the extraction folder.
2. Build or refresh the FDA plus PubMed combined outputs.
3. Check `COMBINED_FDA_PUBMED_QC_*.txt` and merged-table QC outputs.
4. Continue only when there are no obvious multi-value numeric cells and no reported `qc_errors` that affect delivered tables.

Required semantic checks before plotting:

- `AVAL`, `BASE`, `CHG`, `LOWER`, `UPPER`, `N`, `EXDOSE` must each contain one atomic value.
- Units must be in unit fields such as `AVALU`, not embedded in numeric fields.
- Multi-endpoint cells must be split before plotting.
- QSP model-paper values must not be treated as observed validation data unless the source table clearly gives observed calibration or validation data.

## Output Contract

Create one versioned output folder and keep all report artifacts together:

```text
qsp_parameter_source_report_<version>_<YYYYMMDD>/
```

For the finalized `1.2` report the user-facing outputs were:

```text
qsp_parameter_source_report_1.2_20260629/
  QSP参数来源与验证数据整理报告_1.2_20260629.docx
  QSP参数来源与验证数据整理报告_1.2_20260629.pdf
  Evidence_category_counts_1.2_20260629.png
  Mechanism_feature_counts_1.2_20260629.png
  Validation_percent_scatter_1.2_20260629.png
  Validation_month_rows_1.2_20260629.png
  rendered/page-*.png
```

Apply the user's file-naming SOP to every user-facing output.

## Figure Generation Rules

Figures must be generated with R/ggplot2. Do not use screenshots, spreadsheet chart exports, PIL-drawn fallback charts, or previous non-ggplot images.

Use this base theme exactly unless the user gives a newer style:

```r
bp <- theme_bw() +
  theme(axis.text.x = element_text(colour = "black", size = rel(1.4))) +
  theme(axis.text.y = element_text(colour = "black", size = rel(1.4), angle = 90)) +
  theme(axis.title.x = element_text(vjust = -2, size = rel(1.4))) +
  theme(axis.title.y = element_text(vjust = 2, size = rel(1.4))) +
  theme(plot.margin = margin(0.5, 0.5, 0.5, 0.5, "cm")) +
  theme(plot.title = element_text(hjust = 0.5),
        panel.grid.major = element_blank(),
        panel.grid.minor = element_blank())
```

Allowed local overrides:

- Rotate long x-axis labels for readability.
- Set horizontal-bar y-axis text to `angle = 0`.
- Put legends at the top for grouped plots.
- Increase figure width/height to prevent clipping.

Do not use `theme_minimal()` for this report family.

Required figures for the QSP parameter-source report:

1. `Evidence_category_counts_<version>_<date>.png`
   - Data: `PUBMED_CATEGORY_EXTRACTION_STATUS_*`.
   - Plot: count of included PubMed sources by the six formal categories.
   - Recommended geometry: `geom_col()` plus count labels.

2. `Mechanism_feature_counts_<version>_<date>.png`
   - Data: `COMBINED_MECH_FDA_PUBMED_CATEGORY_*`.
   - Plot: top mechanism evidence features from `PATHWAY`, `CELLTYPE`, `CYTOKINE`, and `RECEPTOR`.
   - Recommended geometry: horizontal `geom_col()` grouped by feature type.

3. `Validation_percent_scatter_<version>_<date>.png`
   - Data: `COMBINED_PD_FDA_PUBMED_CATEGORY_*`.
   - Include rows where `AVALU == "%"`.
   - Plot one atomic PD/validation row per point.
   - Color by source, e.g. FDA/existing vs PubMed category extraction.
   - Use jitter only to separate overlapping points; do not aggregate away row-level observations.

4. `Validation_month_rows_<version>_<date>.png`
   - Data: `COMBINED_PD_FDA_PUBMED_CATEGORY_*`.
   - Include rows where `AVALU == "months"`.
   - Summarize median OS/PFS or other time-to-event endpoint by source when appropriate.
   - Label bars with value and row count.

Save PNGs at 320 dpi or higher.

## Word Report Structure

Use `python-docx` or an equivalent document API. The final `.docx` must be the source for the final `.pdf`.

Recommended section order:

1. Title and report purpose.
2. Evidence package overview and six-category classification summary.
3. Parameter-source matrix in the style of QSP paper parameter-source tables.
4. Mechanism and model-structure parameter summary.
5. Validation-data summary by endpoint class, unit, and source.
6. FDA/regulatory plus PubMed integration notes.
7. Review conclusion and next extraction priorities.
8. Appendix: generated table and figure index.

Tables must be scientific three-line tables:

- Top border on the header row.
- Bottom border under the header row.
- Bottom border on the final row.
- No vertical grid lines.
- No full internal grid.
- No decorative shaded header unless the user explicitly asks for it.

Important report tables:

- Six-category evidence summary.
- QSP parameter-source matrix.
- Mechanism feature/source summary.
- Validation endpoint summary.
- Output file index.

Insert the generated ggplot PNG files into Word; do not insert screenshots of plots.

## PDF Rendering And Visual QA

After saving the `.docx`, render it to PDF and page PNGs using the documents skill renderer or the active document-rendering equivalent. Example command pattern:

```bash
/Users/zhuhaoxiang/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 \
  /Users/zhuhaoxiang/.codex/plugins/cache/openai-primary-runtime/documents/26.623.12021/skills/documents/render_docx.py \
  qsp_parameter_source_report_<version>_<date>/QSP参数来源与验证数据整理报告_<version>_<date>.docx \
  --output_dir qsp_parameter_source_report_<version>_<date>/rendered \
  --emit_pdf
```

If the renderer writes the PDF into `rendered/`, copy the final PDF to the report folder using the SOP filename.

Visually inspect rendered `page-*.png` files before final delivery. Check:

- Figures have `theme_bw()` style, black axis text, no major/minor grid, centered title.
- No old blue/purple web-style charts, screenshots, or PIL fallback charts remain.
- Axis labels and legends are not clipped.
- Tables are three-line tables, not full-grid tables.
- No text overlaps, orphaned table headers, blank trailing pages, or missing figures.
- Figure captions and table titles describe the data source and unit clearly.

## Failure Modes That Must Be Fixed Before Delivery

- A figure looks like a screenshot, spreadsheet export, `theme_minimal()` plot, or PIL chart.
- A plotted point/bar was created from a cell containing multiple values.
- A Word table displays full grid borders.
- PDF pages show clipped labels, squeezed legends, or unreadable axis text.
- The final PDF was produced from stale DOCX or stale PNG files.
- File names do not follow `<original-file-stem>_<version>_<YYYYMMDD><extension>`.

## Final Response Checklist

Only final-report delivery is acceptable after all checks pass:

- Link the final `.docx`.
- Link the final `.pdf`.
- Mention that ggplot `bp` figures were regenerated.
- Mention that rendered PNG pages were visually inspected.
- State any remaining limitation, such as source extraction incompleteness, if present.
