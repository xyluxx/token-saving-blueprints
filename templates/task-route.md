# Forced task route record v2

Complete before dispatch when any local GPU, free-model or OmniRoute add-on is enabled. Use the exact JSON contract in [`schemas/task-route.schema.json`](../schemas/task-route.schema.json); unknown values force `main`.

## Correlation and classification

- Schema version: 2
- Task ID:
- Task class:
- Task shape: bounded / open-ended / unknown
- Operation: deterministic / semantic / mixed / unknown
- Reasoning: low / medium / high / unknown
- Data class: public / internal / confidential / credentials / unknown
- External effect: none / reversible / irreversible / unknown
- Verification: deterministic / human / none / unknown
- Required context tokens:
- Exact required tools (array):
- Required output capabilities (array):
- Evaluation timestamp with timezone:

## Enabled add-ons

- Local GPU enabled: true / false
- Free model enabled: true / false
- OmniRoute enabled: true / false

## Capability evidence

Attach a v1 record for both the local and free slots using [`templates/capability-evidence.md`](capability-evidence.md). A disabled slot still needs a structurally valid evidence record in the reference contract; it is not evaluated. Coarse GPU admission is not capability evidence.

## Decision

- Decision ID (assigned by host):
- Route: deterministic-code / local / free / main
- Closed reason code from policy:
- Forced: true / false
- Worker ID and evidence reference, when applicable:
- Expected verifier identity, type and independence from the route decision, when applicable:

## Post-result

Use [`templates/verifier-result.md`](verifier-result.md). Routing does not grant external-action permission and the pure reducer does not execute the returned action.
