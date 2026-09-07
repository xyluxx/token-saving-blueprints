# JetBrains Junie: AI Chat, IDE plugin and CLI

[Start here](../../START-HERE.md) · [Conservative](../modes/conservative.md) · [Aggressive](../modes/aggressive.md) · [Authentication and billing](../auth-and-billing.md) · [Measurement](../measurement.md)

Checked 2026-09-06 (UTC). Evidence: documented unless stated otherwise; no authenticated agent task or savings benchmark was run.

## Who this is for

JetBrains teams already using Junie. Current documentation recommends Junie in the IDE's AI Chat; a separately installed Junie plugin provides its own tool window. Junie CLI is another route, with its own authentication, commands and configuration. Do not copy a setting between these surfaces merely because the agent name matches.[33][60][61]

## Authentication and billing routes

* AI Chat/separate IDE plugin: the reviewed documentation activates Junie through a JetBrains AI subscription and its usage/top-up system. This guide does not establish that every AI Assistant BYOK setting also applies to the Junie IDE agent. New IDE BYOK adoption is limited pending the specific installed integration's current documentation.[60][61]
* CLI native: browser sign-in to JetBrains uses the subscription; a Junie API key is a distinct usage-billed route. Neither is a provider API key.[33]
* CLI BYOK: `/account` > Use your own API key manages direct OpenAI, Anthropic, Google, xAI and OpenRouter credentials; the documented list also includes GitHub Copilot OAuth. Custom endpoints have a separate configuration route. If BYOK and a JetBrains subscription both offer a model, BYOK takes billing priority.[13][33]
* CLI environment risk: `JUNIE_API_KEY` selects Junie authentication, while `JUNIE_OPENAI_API_KEY`, `JUNIE_ANTHROPIC_API_KEY` and the other documented provider variables configure direct access. `JUNIE_LLM_PROVIDER`, `JUNIE_MODEL`, `JUNIE_EFFORT` and CLI flags can also affect the route; flags take priority over equivalent environment settings. Record presence and effective selections without exposing values.[63]

Lower provider usage can reduce API cost. Lower JetBrains usage may preserve included/top-up credits, but does not refund a fixed subscription. The same application can consume both if different models/routes are used. Native Copilot OAuth listed by JetBrains is not permission to export the token to a generic endpoint.[13]

## Conservative recipe

1. Record the actual surface/version, account route, model/effort, automatic-context state and permissions. Back up current project guidelines. Do not enable Brave Mode or replace authentication for this task.
2. AI Chat: open the existing chat and select Junie by JetBrains. The context indicator toggles whether the active file name and selected text are automatically attached; use `@` to attach additional needed files. Record its original state and omit only irrelevant context, not dependencies or required records.[60]
3. Separate plugin: inspect Settings > Tools > Junie > Project Settings for a custom guidelines path. Otherwise merge into the currently effective guidelines file. `.junie/AGENTS.md` takes precedence and is used exclusively; creating it can hide the root `AGENTS.md`, playbook and rules. Do not create a new override merely to add a small instruction.[61]
4. CLI: inspect the same precedence documented for CLI, including any `JUNIE_GUIDELINES_FILENAME` override. Merge into the effective file rather than changing discovery order. Use `/account` only to inspect existing credentials and `/usage` to observe the session; do not add keys.[33][48][63]
5. Add this discipline through the effective guidelines or, in AI Chat, explicitly in the task prompt:

   > Preserve all requirements, model, effort and permissions. Enumerate the candidate files/records; read precise relevant ranges and dependencies while tracking coverage. Use existing deterministic tools for bulk edits and full-row calculations. Make a minimal coherent patch. Run the complete required tests and state actual results and blockers. Do not replace all-record review with a sample or clear history.

6. Investigate first, then approve the exact implementation through the existing mode/approval UI. Use native editor/terminal and only approved MCP tools. Review the changed-files panel and all required test results.[33][60][61]

## Aggressive recipe

1. Ask the existing tool to retain complete query/test output in a protected project artifact, while returning a view with exact coverage, source revision, all failures, exit status and raw-source locations. For a required review of every record, preserve a page-by-page coverage checklist instead of substituting the view for review.
2. Use explicit file attachments to give Junie the view for the next phase. Keep critical identifiers, decisions, permissions and unresolved requirements verbatim in a handoff; include what external actions already happened so they are not replayed.
3. CLI: after stopping or completing work in the current session, `/new` opens another live session. Existing sessions remain active in the background; confirm none is still writing to the same files before continuing. Keep the original session in Task history and attach the handoff/original evidence in the new one.[33]
4. IDE: retain the prior chat/task and begin a new task with the handoff and selected files. This is explicit context selection, not a hidden history rewrite. If the new task loses a requirement, uses stale sources, misses counts or changes test outcomes, return to full evidence immediately.

Control ceiling: native attachments, tools, approvals and fresh sessions are supported. No universal transcript replacement hook is asserted. A separate plugin's rule precedence is not proof of the same parser in every AI Chat/ACP client. Optional MCP only controls its own data/actions, not all model input.[60][61]

## Verify and roll back

Check that the effective guideline still contains prior project requirements, then compare patch scope and the complete test/check list. CLI `/usage` reports token/model/cost details; reconcile those with the actual billing route. If the IDE shows only account credits, report that observation rather than converting visible text to billed tokens.[33]

Restore the original guideline section, context indicator and task-specific tools. Use AI Chat's per-file rollback or Rollback control only after preserving unrelated edits; the separate plugin also supports reviewing/reverting files. Reopen the old task or reattach raw artifacts if the handoff failed. Do not delete provider keys to roll back a rule. Native file rollback does not reverse terminal side effects, remote writes or consumed credits.[60][61]

## Limits and evidence

Documented, not authenticated/native-smoke-tested. CLI BYOK precedence is explicitly verified from current docs, not extrapolated to the IDE. No new IDE BYOK recipe is recommended without route-specific proof. Read permissions for source files do not automatically authorize transfer to a direct provider or remote MCP service. Context summaries and local artifacts must follow the same retention/access policy as the originals.

## Sources

[13] https://junie.jetbrains.com/docs/byok.html
[33] https://junie.jetbrains.com/docs/junie-cli.html
[48] https://junie.jetbrains.com/docs/guidelines-and-memory.html
[60] https://www.jetbrains.com/help/ai-assistant/junie-agent.html
[61] https://junie.jetbrains.com/docs/junie-ide-plugin.html
[63] https://junie.jetbrains.com/docs/environment-variables.html
