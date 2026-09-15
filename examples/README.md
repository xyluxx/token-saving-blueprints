# Examples

All records here are synthetic and must not be read as benchmarks, provider certification or native account trials.

- `task-routing.json`: normalized task-route v2 requests and policy decisions.
- `capability-evidence.json`: versioned local/free worker evidence with exact runtime and capability dimensions.
- `task-routing-results.json`: correlated verifier/post-result v2 transitions with decision-derived expected verifier fields kept separate from actual verifier fields, plus fallback bounds and terminal late-result rejection.
- `local-gpu-routing.json`: coarse hardware admission only; admission explicitly does not establish task eligibility.
- `usage-normalization.json`: provider usage accounting fixtures.
- `api-cost-scenario.json`: assumption-based planning arithmetic, not measured savings.

The repository validator manually validates operational examples without dependencies. Draft 2020-12 schema interoperability files are in `schemas/`; standards validation requires an external JSON Schema implementation.
