# Forced task routing for enabled add-ons

This is the mandatory blueprint control for local GPU, free-model and OmniRoute add-ons. If any is enabled, every model-bound task needs a recorded decision before dispatch. An integration that bypasses it is not conformant.

Policy: [`catalog/task-routing-policy.json`](../catalog/task-routing-policy.json) · Architecture: [`docs/architecture.md`](architecture.md) · Task template: [`templates/task-route.md`](../templates/task-route.md) · Examples: [`examples/task-routing.json`](../examples/task-routing.json)

## Classification boundary

The host classifies natural language into the normalized v2 task contract. The reducer does not parse prose. Uncertain consequential fields remain `unknown` and route to `main`.

## Policy-driven decision

The policy is canonical configurable routing data. It declares route precedence, per-route bounds and each route's expected verifier authorization. The shipped order is `deterministic-code`, `local`, `free`, `main`; swapping valid local/free precedence changes the result without changing Python. Code plus the schemas enforce fixed v2 enums, reason semantics, post-result actions and immutable safety bounds; the policy JSON alone is not the sole authority.

Immutable safety invariants remain code-level bounds: unknown/open-ended tasks, high/unknown reasoning, credentials/unknown data, irreversible/unknown effects and missing/unknown verification stay on `main`; every route appears once; main fallback is limited to one. Policy cannot grant permissions or weaken these rules.

## Structured capability evidence

Broad flags such as “task class verified” are not trusted. Each automatic worker has capability-evidence v1 containing:

- worker ID, requested model and resolved model
- declared and observed runtime fingerprint
- evidence status, verification/freshness timestamps and evidence reference
- effective context tokens
- task classes and reasoning levels
- exact verified tools and output capabilities
- permitted data classes and verification methods
- availability and, for free routes, a verified hard spending stop

Matching is compositional. Every task requirement must be a subset/member of the corresponding evidence. Expired/unknown evidence, an unknown resolved model or fingerprint mismatch fails closed with a specific reason code. Required tools and output forms are matched exactly. Local GPU hardware admission only qualifies a configuration for a capability trial; it never proves task eligibility.

## Verification and post-result reduction

A worker result is provisional. An eligible worker decision records the expected verifier identity, type and independence selected from the validated route policy. Post-result v2 correlates task, decision, worker and evidence reference and carries those authoritative expected fields separately from the actual verifier identity, type, independence and result. Acceptance requires an exact expected/actual verifier match; a verifier cannot authorize itself by asserting that it is independent. The pure reducer returns the policy action:

- correlated verifier pass → `accept`
- failed/unknown verification with explicit authorization and no prior fallback → `fallback-main`
- no authorization, exhausted bound or invalid independence → `stop`
- correlation mismatch or a result arriving after a terminal state → `reject`

The reducer does not dispatch, verify, retry or mutate state. The host performs any returned action and enforces external-action approval.

## Schemas and validation

Focused Draft 2020-12 schemas are in [`schemas/`](../schemas/). Shipped task-route, capability and verifier examples are exercised by dependency-free manual validators. Standards-compliant JSON Schema validation requires external tooling; the project does not include a partial schema engine.

Run:

```bash
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

Deployment still requires route-specific canaries and evidence. To roll back, disable add-on dispatch, restore the prior endpoint/model mapping and verify a fresh main-route request. The repository remains a blueprint, not a runtime or control plane.
