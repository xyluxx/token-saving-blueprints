# Synthetic accounting examples

These fixtures are invented input values for testing accounting rules. They are **not API responses captured from a user, measurements of savings, or a benchmark of either mode**.

[usage-normalization.json](usage-normalization.json) illustrates two declared schemas:

- An OpenAI Responses-style total already contains cached input and reasoning output. The subsets are not added again.
- An Anthropic Messages-style record separates ordinary input from cache-read and cache-creation input, so those input fields are combined once.

The validator checks the expected normalized total. Missing required fields, unknown schemas, negative values and impossible subset values fail rather than becoming zero/free usage. This small helper is not a universal provider usage SDK; check current provider semantics before adapting it to real data.

Run `python3 scripts/validate.py` from the repository root, then the unit tests listed in [VALIDATION.md](../VALIDATION.md).


## Hypothetical API-cost scenario

[api-cost-scenario.json](api-cost-scenario.json) contains the explicit assumptions and eight combinations displayed in the README. It is a calculated illustration, not measured performance, an average, a forecast or an account-usage record. The checker recomputes costs and rounding with decimal arithmetic and rejects loss of the nonbenchmark/nonforecast labels. It does not validate the assumptions as likely outcomes.
