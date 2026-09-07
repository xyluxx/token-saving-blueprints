# Google Antigravity

[Start here](../../START-HERE.md) · [Conservative](../modes/conservative.md) · [Aggressive](../modes/aggressive.md) · [Authentication and billing](../auth-and-billing.md) · [Measurement](../measurement.md)

Checked 2026-09-07 (UTC). Evidence: documented unless stated otherwise; no authenticated agent task or savings benchmark was run.

## Who this is for

Teams using Google's Antigravity editor/agent environment or its own Antigravity CLI. **Antigravity is not Gemini CLI.** Current Antigravity documentation describes a shared agent core and synchronized settings between its editor and CLI. Do not import Gemini CLI flags, OAuth tokens or API-key assumptions just because both products use Gemini models. Record whether the installed product is Antigravity 2.0, Antigravity CLI, an Antigravity IDE extension or the standalone Antigravity IDE; shared branding does not establish identical enterprise eligibility.[78][36]

## Authentication and billing routes

* Individual native account: baseline quotas differ across Google AI plans. Google AI Pro/Ultra can use purchased/promotional AI credits for overages according to the AI Credit Overages setting. Record Never/Always before work; do not enable overages to complete a token-saving trial.[16]
* Individual BYOK/custom endpoint: the current Plans page explicitly says there is no bring-your-own-key or endpoint route for additional rate limits. A Gemini API key is not a way to top up Antigravity's native subscription quota.[16]
* Enterprise: first identify the exact product. Current official onboarding supports Antigravity 2.0, Antigravity CLI and supported Antigravity IDE Extensions; it explicitly excludes Antigravity IDE (standalone) from enterprise deployments. On a supported surface, use the organization’s existing Business account → Continue with Google Cloud flow or its approved federation route, then confirm the assigned license, project and location. Gemini Enterprise Agent Platform consumption billing and Gemini Enterprise license quotas/managed overages are distinct routes. Preserve the existing identity, enabled service and administrative policy. Do not create a project, enable billing or migrate products for a token-saving recipe.[36]
* MCP OAuth or Google credentials authenticate a connected data/tool service. They do not change the core agent's subscription entitlement or turn it into Gemini CLI.[37]

Baseline quota, purchased AI credits and enterprise cloud consumption are distinct. Reducing context may preserve quota or reduce overages, but a fixed Google AI subscription does not become cheaper automatically. Limits and model availability can change.[16]

## Conservative recipe

1. Record the installed surface/version, account route, model/effort, quotas, overage setting and existing tool/permission state. Keep settings unchanged; CLI and editor synchronize important settings, so a supposed CLI-only change may affect the editor.[78]
2. Editor: in the agent panel's `...` menu, open Customizations > Rules > + Workspace. Create a task-specific manual rule and invoke it by `@` mention. Current workspace rules use `.agents/rules`; do not edit the shared global `~/.gemini/GEMINI.md` to optimize one project.[17]
3. Put the following discipline in that rule. For CLI, include it directly in the task prompt unless the installed rule controls have been verified; do not assume an editor button exists in the terminal.

   > Keep current model, effort, permissions and every acceptance criterion. Enumerate the complete candidate files/records. Read exact relevant ranges plus dependencies; report coverage. Use existing deterministic tools for bulk edits and all-row calculations. Patch minimally and run all required tests. Report actual failures and unresolved work. No new history rewriting, sampling of required records, or claiming a pointer as a completed answer.

4. Give the agent exact task files/sections rather than an unnecessary repository dump. Review the initial investigation and plan before implementation. Native workspace reads/writes may be auto-allowed, so a rule saying “ask first” is not a security control. Keep unrelated or sensitive material outside the approved workspace.[77]
5. Use existing editor/search/terminal tools and only approved MCP sources. MCP Servers is available through the agent panel; inspect tools and credentials before authorizing a call. Leave command/browser/MCP approvals as recorded and never grant wildcard permissions just to reduce interruptions.[37][77]
6. Review the diff and execute every required test. Report the real command/result and source coverage, even when successful logs are not pasted in full.

## Aggressive recipe

1. Before a large read/query/test result, ask the existing tool to save a complete local artifact and return a view containing source revision, exact query, complete coverage/counts, all failures, exit status and raw-source locations. Keep raw data protected under the same policy as the original source.
2. Give the next reasoning step that explicit view. For an all-record review, read every required page and track coverage; aggregate computation is not a substitute. Reopen original details on stale revisions, count discrepancies, missing requirements or unexplained failing checks.
3. At a finished phase, prepare a reviewed handoff with verbatim critical identifiers/requirements, decisions, files changed, tests, unresolved work and external actions already completed. Retain the prior conversation, then open a new one with the same provider/model and the handoff plus required sources.
4. Verify a protected requirement against the original source before continuing. If recovery needs unavailable raw material, stop rather than treating the handoff as complete evidence.

Control ceiling: rules guide behavior, MCP shapes only its own output, and native permissions control specified operations.[17][37][77] No universal context interceptor, hidden-history rewrite or Gemini CLI plugin compatibility is established. The CLI's shared harness/settings do not create an arbitrary-model gateway.[78]

## Verify and roll back

Record baseline and comparison quotas in editor Settings. In Antigravity CLI, `/usage` (alias `/quota`) refreshes the native quota panel. This is not a promise of a complete per-task invoice or an externally accessible token API. Reconcile purchased-credit/enterprise consumption separately and include retries and handoff-generation cost where visible.[16][69]

Confirm identical model/effort, full scope, required tests and patch quality. Remove only the new workspace rule and restore original tool/context choices. Reopen the original conversation or raw artifacts on recovery failure. Undo only reviewed task edits through backups/diffs, preserving unrelated changes. Check both editor and CLI if any shared setting was separately changed, and restore its original value. Do not delete shared Gemini configuration or credentials. Remote actions and spent credits cannot be rolled back by restoring files.

## Limits and evidence

Documented, no authenticated native trial. Individual no-BYOK wording and separate enterprise onboarding must not be flattened into either “all APIs work” or “no enterprise integration exists.” Core inference, remote MCP data and browser actions each need the appropriate permissions. No compression percentage or fictional automatic token meter is supplied.[16][36][37]

## Sources

[16] https://antigravity.google/docs/plans
[17] https://antigravity.google/docs/rules-workflows
[36] https://antigravity.google/docs/enterprise.md
[37] https://antigravity.google/docs/mcp
[69] https://antigravity.google/docs/cli/commands/usage
[77] https://antigravity.google/docs/permissions
[78] https://antigravity.google/docs/cli/overview
