# Coding and review

Use this for a real feature, bug fix or review. Keep the original requirements, model, native account and project checks. A shorter diff is not automatically a better implementation.

## Conservative sequence

1. State the behavior that must change and what must remain unchanged. Name acceptance tests and affected flows.
2. Search exact filenames, symbols, errors and current tests. Prefer native language navigation; use an optional tool only for a missing capability.
3. Read the relevant implementations, callers, configuration and dynamic paths. A repository map is not full review.
4. Reuse existing functions, standard libraries and native platform features when they satisfy the complete requirement.
5. Make a small unambiguous patch against the current source version. Inspect the actual diff.
6. Run focused checks while developing and all required final checks. Preserve failures and stderr; do not replace testing with a confident explanation.
7. Return the changed behavior, verification and remaining limitations without reprinting unchanged files.

Use [coding policy](../../templates/coding-policy.md) as a scoped addition to existing instructions, not a replacement for them.

## Aggressive additions

For discovery-heavy work, try a supported goal-aware view of remote/background code or a source-linked checkpoint for completed investigation. Keep active edit bodies and required dependencies exact. Restore full source before consequential edits.

A specialized skimmer is an experiment for a named task cohort. Better benchmark solve rates do not prove that the same pruning is safe for code completion, security review or your current harness.

## Example: adding a date field

A native date input may avoid a new dependency if it satisfies accessibility, browser support, validation, locale and design requirements. It is not an acceptable replacement if the user explicitly needs unsupported behavior. Compare against the actual acceptance contract, not the fewest lines.

## Example: noisy test run

Run the complete required suite. Present the failing tests, exact errors, status and a link to full output rather than every progress line. Keep warnings or neighboring context needed to diagnose the failure. Do not rerun a stateful command merely to recreate the raw log.

## Shared repository work

Keep task/branch/worktree identity explicit. Do not let two agents edit the same mutable worktree without coordination. Reuse an authorized current index, not another task's assumptions or approvals. Existing CI evidence must match the exact source revision; never describe cached status as a fresh test run.

## Stop conditions

Expand or revert when callers are missing, edits target the wrong occurrence, tests regress, required behavior is dropped, restored context keeps looping or the chosen model/auth changes unexpectedly.

## Record

Use [trial record](../../templates/trial-record.md). Count failed patches, test/repair loops, source rereads, required verification and final output. Keep code-size changes separate from model tokens.
