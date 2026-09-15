# Recurring operations: avoid the model call when it adds no value

A repeated report or monitor often wastes more on rediscovering a procedure than on the final explanation. Use the user's existing scheduler, scripts and authorized connectors; this blueprint does not require a new automation platform.

## Select an eligible operation

Good candidates have stable input/output schemas and checkable steps: fetching all pages, validating records, computing aggregates, formatting a report or comparing a source version.

Do not compile arbitrary judgment or replay a past agent transcript. A recipe needs parameters, source/environment preconditions, permissions, validation, an exception route and a rollback/checkpoint.

## Conservative sequence

1. Let the selected model develop or revise a procedure when needed.
2. Verify it on the actual allowed input and required output.
3. Save the procedure in the user's existing versioned workspace.
4. On later runs, verify preconditions and execute the deterministic portion without asking the model to regenerate it.
5. Invoke the model when there is a relevant change, ambiguity, new question or failure that requires judgment.
6. Keep complete evidence and a concise outcome receipt.

A no-change check can avoid model inference entirely. It still uses network, CPU and storage, and only saves model tokens if the baseline would actually have invoked a model.

## Change detection is not “hash unchanged, ignore everything”

Account for time-based obligations, expiring permissions, scheduled substantive reviews, schema changes, deletions, partial fetches and source freshness. An empty search or failed API read is not no change.

For incremental processing, update every affected downstream result. If dependency coverage is uncertain, recompute the relevant region or full operation. Do not present stale totals as current because only one visible row changed.

## Approval boundaries

Repeat permission to read is not automatically repeat permission to send, purchase, publish or modify records. Keep the exact authorized action scope. Refresh relevant live state before a write, use supported idempotency and verify the result.

## Aggressive additions

Use a compact source-linked history of completed phases for long workflows, through a supported native surface. Do not summarize away unfinished obligations. Keep the current task, latest corrections and action status exact. If restoration fails, stop rather than invent continuity.

## Practical example

A weekly report can fetch all source records, validate counts, calculate metrics and render the document through a stable script. The model can interpret material changes and draft the requested explanation. The saving comes from avoiding repeated procedure generation and raw-data retransmission, not from skipping records.

## Measure separately

Record initial development/indexing, maintenance, ordinary runs, exception runs, model calls avoided, added helpers and human rework. Do not apply a second compression percentage to work already counted as avoided.
