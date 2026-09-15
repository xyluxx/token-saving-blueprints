# Local GPU route worksheet

Complete this outside the public repository. Record capabilities and measurements, not credential values or private prompts.

## Current route and task contract

- Harness/version:
- Current provider/auth/billing route:
- Task class: general-purpose / specialist:
- Required result and acceptance checks:
- Required tools, schemas, vision/embedding features and context:
- Data permitted to remain on this host:
- Existing local runtime: LM Studio / Ollama / other / none:

## Hardware and candidate specification

- OS and runtime/backend version:
- CPU architecture and instruction support:
- Dedicated VRAM (GiB), or unified memory (GiB):
- System RAM (GiB):
- GPU/backend reported as active:
- Candidate parameter range (billions):
- Quantization class/bit floor (Q4-or-better for a general-purpose route):
- Architecture/capabilities required (instruction tuning, tools, structured output, vision):
- Configured context and output reserve:
- Runtime memory estimate at that context:
- Memory estimate × 1.15 fits available memory:

Do not nominate 512M/1B/2B-class models as general-purpose routes. Do not use Q1 for a 27B-class model. For an average PC/laptop, start the general-purpose pilot at the repository's minimum-good specification: capable 7B–9B instruction model, quality-preserving 4-bit-or-better quantization, 8 GiB dedicated VRAM where available, 16 GiB system/unified memory and at least 8k tested context. These are specification floors, not product endorsements or quality guarantees.

## Compatibility trial

- Health/model-list check:
- Exact protocol and endpoint class:
- Streaming and cancellation:
- Structured output/schema adherence:
- Tool names/arguments/results round trip:
- Context allocation and truncation behavior:
- Runtime reports intended GPU/offload (no accidental CPU fallback):
- Warm/cold latency and tokens/second:
- Output acceptance result versus current route:
- Full required checks passed:

## Decision and rollback

- Decision: retain current / pilot local / reject local:
- Reason/tier:
- Jobs eligible for local routing:
- Jobs prohibited from local routing:
- Fallback triggers (timeout, OOM, malformed tool call, failed check):
- Explicit fallback route and spend approval:
- Configuration changed:
- Restore command/path (no secrets):
- Post-restore read-only verification:

Use the [local GPU routing guide](../docs/local-gpu-routing.md), [task contract](task-contract.md) and [change receipt](change-receipt.md). A local endpoint is a separate route; it does not inherit a cloud model's identity, quality, tools, authentication or billing.
