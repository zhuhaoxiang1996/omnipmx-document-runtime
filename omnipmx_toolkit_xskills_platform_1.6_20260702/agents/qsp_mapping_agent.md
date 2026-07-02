# QSP Mapping Agent

Use this agent to map extracted evidence to PBPK/QSP assumptions, parameters, model components, uncertainty, and validation claims.

## Evidence Classes

For QSP/PBPK evidence packages, route sources into:

1. `QSP/MIDD监管方法学`
2. `QSP模型文章`
3. `机制与模型结构证据`
4. `模型输入/参数证据`
5. `校准/验证数据`
6. `模拟与决策支持证据`

## Derivation vs Validation Split

If benchmark QSP/PBPK/model papers exist:

- Use non-model primary evidence as the derivation set.
- Hold QSP/PBPK/model papers out as validation/comparison evidence.
- Do not import model-paper fitted parameters as independently observed parameters.
- If a parameter exists only in held-out model papers, mark `not_independently_validated` and create a search gap.

## Assumption-Evidence Map

Output:

| assumption_id | model_component | assumption | supporting_sources | conflicting_sources | parameter_candidates | uncertainty | validation_status | action |
|---|---|---|---|---|---|---|---|---|

Validation status values:

- `numeric_support`
- `direction_only`
- `partial_support`
- `conflicting`
- `not_independently_validated`
- `insufficient_evidence`

## ADC Payload PBPK Mapping

For ADC payload projects, map evidence to:

- systemic ADC PK;
- payload release;
- free payload distribution;
- payload metabolism and clearance;
- tumor and normal tissue exposure;
- toxicity organ exposure;
- species translation;
- comparator ADC or payload class evidence.

Always distinguish direct payload evidence from same-payload ADC evidence and same-class extrapolation.
