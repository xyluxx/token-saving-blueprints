# Runtime-neutral local GPU routing

This module adds a reversible **decision route** to the blueprint; it does not install a runtime, download weights or silently replace the selected model. Use an existing LM Studio, Ollama or other approved local server when it already exposes the protocol and capabilities the harness needs. The policy is runtime-neutral and specification-led.

Structured policy: [`catalog/local-gpu-routing.json`](../catalog/local-gpu-routing.json) · Worksheet: [`templates/local-gpu-route.md`](../templates/local-gpu-route.md) · Deterministic fixtures: [`examples/local-gpu-routing.json`](../examples/local-gpu-routing.json)

## When local routing saves tokens or money

A local route does **not inherently reduce logical tokens**. It can avoid metered API charges for eligible work and keep permitted data on one host, while adding hardware, electricity, setup, latency and verification costs. It may also lose quality or require retries, erasing any apparent benefit. Report local-compute substitution separately from token reduction and subscription savings.

In the repository's explicit upper planning case, Aggressive mode plus OmniRoute reaches a rounded **75% reduction in variable API cost** when **65.5% of the remaining workload** qualifies for local execution, local compute costs 5% of the displaced cloud inference, and coordination/fallback overhead adds 5%. This can happen for a highly eligible workload, but it is not an average, forecast, token-count reduction or fixed-subscription saving. See the reproducible [scenario data](../examples/api-cost-scenario.json).

Use it only for a bounded workload whose task contract can be tested against the current route. Keep the stronger/current route for tasks that fail quality, tool, context, latency or authority gates.

Once the route is enabled, the [forced task-routing layer](task-routing.md) must evaluate every model-bound task before dispatch. Local inference is selected only for task classes already verified on the exact runtime/model route. Unknown metadata, failed capability gates or failed post-result verification use the approved main fallback.

## Specification floors, not model shopping

Choose by capability and measured fit rather than a product name:

| Tier | Parameters | Quantization | Practical memory floor | Use |
|---|---:|---:|---:|---|
| Specialist only | 0.5B–2B | 4-bit or better | 4 GiB VRAM / 8 GiB RAM | Narrow classification, short extraction or autocomplete with deterministic checks |
| **Minimum good general-purpose** | **7B–9B** | **quality-preserving 4-bit or better** | **8 GiB VRAM where available / 16 GiB RAM or unified memory** | Average PC/laptop starting point for bounded drafting, focused coding and verified tools |
| Strong local | 12B–14B | 4-bit or better | 12 GiB VRAM / 24 GiB RAM or unified memory | More demanding synthesis or multi-file coding pilots |
| Large local | 27B–32B | 4-bit or better | 24 GiB VRAM / 32 GiB RAM or unified memory | Quality-sensitive local pilots with full checks |

These are conservative repository recommendations, not vendor benchmarks or guarantees. Architecture, active parameters, vision adapters, KV-cache format, context, batch size, backend and GPU offload change actual memory and quality. Use the runtime's estimator or a measured load at the intended context, then retain at least 15% memory headroom.

**Hard exclusions:**

- Do not route general-purpose work to 512M/1B/2B-class models. They remain specialist or experimental lanes even if they answer a short prompt.
- Do not use below-4-bit quantization as the general-purpose floor.
- **Reject Q1 for 27B-class and larger models.** Prefer a smaller capable model at Q4-or-better instead of buying parameter count with extreme quantization.
- Do not call a route agent-capable until required tools, structured output, streaming, cancellation and error handling pass the exact harness trial.

## Decision procedure

1. **Protect the task.** Complete the task contract first: required result, coverage, tools, context, latency, privacy and checks. “Runs locally” is not an acceptance criterion.
2. **Inventory, do not reinstall.** Detect whether an approved runtime is already running. Record its version, endpoint class and GPU backend without changing it. Do not download weights or open a network listener automatically.
3. **Select a specification tier.** For general-purpose work start at minimum-good or higher. A specialist-only route must have a narrow named task and deterministic verifier.
4. **Estimate the real load.** Include weights, KV cache at configured context, runtime buffers and any vision/embedding adapters. Require `estimated runtime memory × 1.15 <= available memory`. Weight-file size alone is insufficient.
5. **Verify execution placement.** Confirm the runtime reports the intended GPU/offload and context. CPU fallback may be valid for a deliberate slow lane, but it is not a successful GPU route.
6. **Run a capability canary.** Test a harmless prompt plus every required protocol feature: schema, tool arguments/results, stop/cancel, timeout and malformed-call handling. Do not forward cloud subscription credentials to a local endpoint.
7. **Compare a complete task.** Use identical requirements and checks. Record cold/warm latency, failures, retries, accepted output and any external fallback. Token counts from different tokenizers are not directly interchangeable.
8. **Route narrowly.** Allow only the task class that passed. On OOM, truncation, failed schema/tool call, timeout or failed acceptance check, stop and use the explicitly approved fallback—not a hidden cascade.
9. **Rollback exactly.** Restore the former endpoint/model/auth mapping, remove only trial-specific settings and verify a fresh read-only request through the former route.

## Runtime adapters

The policy does not depend on command names. Map these neutral operations to the installed runtime:

| Neutral operation | LM Studio example | Ollama example | Required evidence |
|---|---|---|---|
| Inventory | list downloaded/loaded models | list models/processes | IDs and state, no downloads |
| Estimate/load | memory estimate with intended context and GPU offload | load/run with intended context | memory fit and effective context |
| Confirm GPU | reported GPU-offload state | process `PROCESSOR` state | no unintended CPU fallback |
| Serve | approved local API server | approved local API server | loopback binding by default |
| Stop/rollback | unload/stop server | stop model/server | former route restored |

LM Studio documents 16 GB RAM as recommended and at least 4 GB dedicated VRAM on Windows, and provides an estimate-only load mode that accounts for context and offload.[1][2] Ollama documents that context length raises memory use, exposes the active processor/context through its process view, and supports multiple GPU backends.[3][4] Those facts support measuring the intended runtime; they do not establish the quality tiers above.

## Security and network boundary

- Bind to loopback unless an authenticated, firewalled network service is explicitly approved.
- Treat prompts, tool outputs, model files and runtime logs according to the same retention policy as the existing route.
- Do not expose an unauthenticated local API to a LAN or public interface.
- Do not grant a local model broader filesystem, shell or external-write permissions because inference is local.
- Keep endpoint credentials separate. Never reuse or forward browser/OAuth/subscription tokens to an unrelated endpoint.
- Verify model-file provenance, license and checksum through the chosen distribution process; this module does not endorse or download weights.

## Failure matrix

| Signal | Decision | Recovery |
|---|---|---|
| Runtime estimate exceeds headroom | Reject candidate | Lower context only if task allows, choose smaller Q4+ tier, or retain current route |
| Process view shows unintended CPU fallback | Fail GPU gate | Correct supported backend/device selection or retain current route |
| Tool/schema test fails | Prohibit agent/tool workload | Keep local route text-only for an eligible task, or retain current route |
| Output fails acceptance check | Reject for that task class | Preserve evidence and run approved fallback once |
| OOM, timeout or truncation | Stop; no retry loop | Restore prior route or choose a separately tested tier |
| Local server would require unsafe exposure | Reject topology | Keep loopback or add approved authentication/firewall before trial |

## Verify and record

Run the repository checker and unit tests. They validate the policy schema and synthetic decisions, including rejection of tiny general-purpose routes, Q1 at 27B and loads without headroom. They do not load a model, benchmark quality or certify a GPU/runtime.

For a real trial, retain the completed worksheet privately and publish only redacted aggregate evidence. Recheck runtime documentation and hardware support before changing versions or devices.

## Sources

[1] https://lmstudio.ai/docs/system-requirements
[2] https://lmstudio.ai/docs/cli/local-models/load
[3] https://docs.ollama.com/context-length
[4] https://docs.ollama.com/gpu

Sources checked 2026-09-14. Product names identify existing runtime adapters only; no model product is recommended.
