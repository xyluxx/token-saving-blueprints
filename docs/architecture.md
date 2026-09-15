# Reference architecture

Token Saving Blueprints defines contracts and pure reducers. It is **not an agent runtime, dispatcher, hosted control plane, persistence layer, telemetry store, retry service or configuration mutation engine**.

## Classification

A host classifier converts a natural-language request into explicit metadata. Classification is outside the reducer. Consequential uncertainty remains `unknown`; it is never guessed to make a cheaper route qualify. The host must preserve the original request and classifier evidence.

## Normalized task contract

A task-route v2 request identifies the task class, shape, operation, reasoning, data class, external effect, verifier method, effective context requirement, exact required tools and output capabilities. It also carries an explicit evaluation timestamp, enabled add-ons and route capability evidence. Routing consumes only this record—never chat history or ambient runtime state.

## Policy and immutable safety

[`catalog/task-routing-policy.json`](../catalog/task-routing-policy.json) is the canonical configurable routing-data record. It declares route precedence and each worker route's bounds and expected verifier authorization. The Python reducer plus the Draft 2020-12 schemas enforce the immutable v2 safety contract, including fixed enums, reason semantics and post-result actions; the JSON file alone is not the sole authority. Reordering a valid local/free precedence changes the reducer's output without a Python edit.

Policy flexibility does not include permission to weaken safety. Code-level invariants keep unknown/open-ended work, high or unknown reasoning, credentials or unknown data, irreversible or unknown effects, and absent/unknown verification on `main`. Every valid policy contains each route exactly once and permits at most one main fallback. Routing never grants external-action permission.

## Capability evidence

A capability-evidence v1 record binds verification to a worker, requested and resolved model, runtime fingerprint, observed fingerprint, freshness interval, evidence status and reference. It records effective context, task classes, reasoning levels, exact verified tools, output capabilities, data classes and verification methods. Qualification is compositional: every required dimension passes or the route fails with a specific stable reason code. Unknown/expired evidence, unknown resolved identity and fingerprint mismatch fail closed.

Local GPU size, quantization and memory checks are only coarse admission to a capability trial. Their result explicitly says `task_eligible: false`; only the full task-route reducer can establish eligibility from structured evidence.

## Execution boundary

`route_task` and `resolve_task_result` are deterministic reference reducers. They return decisions/actions but do not classify, dispatch, invoke a model, run a verifier, retry a provider, mutate configuration or persist state. The integrating host owns those operations and must enforce its own permissions.

## Verification and fallback

Post-result v2 inputs correlate task, decision, worker and evidence reference. A worker-route decision carries the authoritative expected verifier identity, type and required independence; the post-result record keeps those expected fields separate from the actual verifier report. Worker output remains provisional. A pass may be accepted only when the actual verifier tuple exactly matches the decision-derived expected tuple. Failure or unknown can produce the policy's `fallback-main` action only when explicitly authorized and below the policy's one-fallback bound. Terminal states reject late results; they cannot silently re-enter execution.

## Restoration

The blueprint's context methods retain source and recovery pointers. A host using selective/lossy context must widen to a complete observation or restore the retained source, verify its identity, and fall back to the conservative route when restoration fails. The reducer does not perform restoration.

## Telemetry

Integrations should record task/decision/worker IDs, reason code, requested/resolved model, runtime fingerprint, evidence reference, verifier identity/result, fallback count and final state. Raw provider receipts and normalized usage should remain distinguishable. This repository defines fields and examples only; it adds no telemetry storage or monitoring service.

## Contract interoperability

Focused Draft 2020-12 schemas in [`schemas/`](../schemas/) describe the operational task-route, capability-evidence, post-result and policy records. The dependency-free repository validator performs explicit manual contract checks against shipped examples. Full standards-compliant JSON Schema validation requires external tooling; this repository intentionally does not implement a partial JSON Schema engine.
