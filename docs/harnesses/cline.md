# Cline

[Start here](../../START-HERE.md) · [Conservative](../modes/conservative.md) · [Aggressive](../modes/aggressive.md) · [Authentication and billing](../auth-and-billing.md) · [Measurement](../measurement.md)

Checked 2026-09-06 (UTC). Evidence: documented unless stated otherwise; no authenticated agent task or savings benchmark was run.

## Who this is for

Existing Cline IDE users doing multi-file coding with explicit tool approvals. Cline exposes persistent rules, context attachments and file checkpoints. This guide focuses on the editor extension; do not assume that a sidebar button is available in its separate CLI or SDK.[7][8][87]

## Authentication and billing routes

* Cline account sign-in: the built-in provider is usage-billed with Cline credits. Google/GitHub OAuth here identifies the Cline account; it is not a free subscription to all underlying models.[6]
* ClinePass: a distinct subscription provider with a curated open-model catalog. Its advertised usage advantage is a vendor claim, not a measured saving from this blueprint. Preserve the user's current provider; do not switch to qualify as token optimization.[6]
* Direct BYOK/cloud/local: select the already configured provider under Settings > API Provider. Anthropic, OpenAI, Gemini, OpenRouter, Bedrock and local runtimes have distinct credential and billing paths. Local inference still has compute costs and data exposure through any enabled remote tools.[6]
* Claude Code adapter: Cline documents a subscription route through the Claude CLI for Claude Pro/Max. Use the installed, authenticated native CLI and the documented provider selector; do not extract tokens into a generic endpoint. This route has streaming, image and prompt-cache limitations and should not be represented as identical to direct Anthropic API access.[27]

Keep provider billing, Cline usage credits and ClinePass/Claude subscription allowance separate. API cost estimates do not establish how much of a fixed subscription bill can be saved. No unverified environment-variable precedence is asserted for the extension.

## Conservative recipe

1. Record the selected provider and model in both Plan and Act configurations if the installation uses separate selections. Preserve model/effort, auto-approve settings and checkpoints. Back up the existing workspace rule files; do not change account or global rules.
2. Create `.clinerules/task-scope.md` in the project root, or append a small nonduplicated section to an existing rule. Open the Rules panel and confirm the rule is enabled. Other detected instruction formats also appear there; inspect them for conflicts rather than silently replacing them.[7]
3. Use this task instruction:

   > Keep all original requirements and permissions. Enumerate the full candidate file/record set first. Read exact task-relevant ranges and dependencies, maintaining a coverage checklist. Use existing deterministic tools for bulk changes and calculations over all qualifying rows. Apply minimal native patches, then run every required test. Show actual failures and unresolved work. Do not shorten history or use samples as evidence of full review.

4. Attach the named files with Cline's `@` context controls. Start by asking for investigation and a file list; approve the resulting tools only after reviewing scope. Full-file review remains full-file review even when source reads are paginated.[87]
5. Use the existing terminal/editor and only needed, already approved read-only MCP sources. The MCP integration adds explicit tools, not a filter over Cline's entire prompt stream.[88]
6. Review changes with checkpoint Compare and the project diff. Execute the complete test/check list. Do not enable broad auto-approve because snapshots exist.[8]

## Aggressive recipe

1. Before a large terminal/query result, request a full local artifact plus a compact view containing source revision, exact query, complete record/test counts, every error and the original locations. Let the next agent read target the view rather than repeatedly loading successful raw output. Use existing tools; no middleware is required.
2. Keep full evidence readable only to the authorized project team. Redact secrets before any provider/MCP transfer, but do not redact evidence needed to answer the task; instead use an approved local source or report the access limitation.
3. At a clean phase boundary, prepare a handoff with exact requirements, completed changes, test results, unresolved work, original file locations and prior external-action status. Retain the old task and open a new task with the handoff and specific context attachments. Do not edit internal task-storage files.
4. Verify critical identifiers and every failed check against raw sources. Incomplete counts, lost constraints, newly failing tests or stale sources require reopening full evidence and correcting the handoff. A high model-confidence statement is not verification.

Control ceiling: rule compliance is advisory; explicit context/tool selection and native checkpoint restoration are supported. Checkpoints are for project files and/or conversation rollback, not a universal lossless history compressor.[7][8]

## Verify and roll back

On the same scoped task/model, compare observed provider usage or Cline task cost, total tool work including retries, patch quality and full test output. If the subscription adapter does not expose billable tokens, use its actual quota display and state the observation limit; do not fabricate a token meter.

Disable only the new rule in the Rules panel and restore original attachments/tools. Checkpoint Restore offers Restore Files, Restore Task Only, or Restore Files & Task: choose deliberately. Rewinding messages alone leaves code in place. Back up unrelated/uncommitted work before restoring files, then re-run tests. Keep the old task available rather than relying on a summary. Neither checkpoint mode restores a remote database or unsends a message.[8]

## Limits and evidence

Documented, not native-smoke-tested. Checkpoint documentation's broad safety language is not a guarantee for shell commands, ignored data, remote writes or concurrent edits. Consumer subscription adapters are included only as Cline-documented integrations, not as blanket authorization to reuse a subscription elsewhere. API routing, account-level top-ups and any automatic model fallback must remain as originally approved.[8][27]

## Sources

[6] https://docs.cline.bot/getting-started/authorizing-with-cline
[7] https://docs.cline.bot/features/cline-rules
[8] https://docs.cline.bot/features/checkpoints
[27] https://docs.cline.bot/provider-config/anthropic
[87] https://docs.cline.bot/core-workflows/working-with-files
[88] https://docs.cline.bot/mcp/mcp-overview
