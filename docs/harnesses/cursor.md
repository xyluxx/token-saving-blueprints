# Cursor IDE

[Start here](../../START-HERE.md) · [Conservative](../modes/conservative.md) · [Aggressive](../modes/aggressive.md) · [Authentication and billing](../auth-and-billing.md) · [Measurement](../measurement.md)

Checked 2026-09-06 (UTC). Evidence: documented unless stated otherwise; no authenticated agent task or savings benchmark was run.

## Who this is for

Teams already using Cursor Agent for repository work. Start with project rules, specific files and existing tools. These recipes do not replace Cursor's private prompt assembly, intercept every request, or change Tab completion.[1]

Cursor documents native rules, MCP and hooks, but each has a different scope.[2][38][76]

## Authentication and billing routes

* Native Cursor login: keep the existing seat, model picker choice, effort and usage settings. Current plans distinguish Cursor Models and Other Models usage pools; included models and availability of on-demand usage vary by plan. Some entry plans also restrict effort controls. Teams/Enterprise have additional administration and a Cursor Token Rate on third-party models, including BYOK. Do not reuse old unlimited-Auto or premium-request arithmetic.[3]
* BYOK: in Cursor Settings > Models, a saved provider key changes that provider's chat route. OpenAI support is limited to the documented chat-model subset; Anthropic and Google have their own supported catalogs. Tab continues through Cursor. An invalid key fails rather than silently restoring native access.[1]
* Cloud: Azure OpenAI deployments and AWS Bedrock credentials/IAM setup are documented options. Preserve the approved endpoint, deployment, region and organization policy instead of substituting a public API.[1]
* Hybrid warning: BYOK requests still pass through Cursor's backend for final prompt construction. Cursor says its Zero Data Retention policy does not apply to BYOK; provider data policies apply. Team/Enterprise Cursor fees can coexist with provider charges. A ChatGPT or Claude consumer subscription is not an API key for this settings field.[1][3]

Less included usage normally preserves allowance, not cash already paid for a seat. Compare overages and provider invoices separately from the subscription.

## Conservative recipe

1. Record the installed version, active account/plan, provider, model/effort, enabled tools, key-enabled providers and spending settings without copying secrets. Back up existing project rules; do not modify User or Team Rules.
2. In Customize > Rules > Add Rule, create a project rule called `task-scope`. Select Apply Manually and invoke it with `@task-scope` for this task. Let Cursor create the `.mdc` file in `.cursor/rules`; a plain `.md` there is ignored.[2]
3. Put this instruction in that rule, filling in the task's exact files and test commands before invoking it:

   > Keep the approved model, effort, scope and permissions. Enumerate candidate files first, then read exact relevant ranges and their dependencies. State what was and was not inspected. Use deterministic search, parsers and bulk operations for mechanical work; compute over all required records, never a sample. Make the smallest coherent patch. Run every required test and report actual results, failures and blockers. Do not summarize away history, suppress errors, or treat a file pointer as the final answer.

4. Open a task chat and attach the named source files through the context picker instead of a whole repository dump. Ask Agent for a coverage map before edits. Expand coverage whenever dependencies, call sites or the task's all-file requirement demand it. The instruction is advice, not an access-control barrier.
5. Use the built-in editor/search/terminal. In Customize, retain only MCP tools relevant to this task and already approved for this repository. Inspect each requested operation. An MCP server's read-only credential scope matters more than its name; never approve a write just to reduce interaction count.[76]
6. Review the native diff and run the project's full required validation. Keep existing caching and compaction as the baseline, not a second claimed saving.

## Aggressive recipe

1. Retain the Conservative safeguards. Before a bulky test or data query, tell the existing terminal or read-only MCP tool to preserve the full result in an access-controlled local artifact, then return an explicit view: source revision, covered files/record count, calculation method, all failures/exceptions and locations of omitted detail.
2. For exact arithmetic, have the existing parser/database aggregate every qualifying record. For a requirement to review every record, page through every record and maintain a coverage checklist; an aggregate is not that review.
3. Have Agent read the view instead of pasting the entire successful log into the next prompt. Check at least one critical source location and every reported failure. Missing counts, truncation, changed source revisions or an unexplained test discrepancy require reopening the raw material, not trusting the summary.
4. At a completed phase, save a handoff containing exact requirements, identifiers, decisions, changed files, test commands/results, unresolved work, source locations and any external actions already performed. Keep the old chat; open a new chat with that handoff and the next phase's files. This is an explicit new-context workflow, not rewriting hidden history.

Control ceiling: rules guide behavior; MCP shapes only its own returned data. Native hooks can gate/observe documented events, but `preCompact` is explicitly observational and cannot block or modify compaction. This recipe does not install hook scripts or claim arbitrary prompt transformation.[38]

## Verify and roll back

Compare the same bounded task before/after with identical model, effort, files and test requirements. Verify the manual rule appears active, tool calls used the named sources, changed files stay in scope, and all required tests actually ran. Compare account usage/on-demand entries and BYOK provider usage where available; visible characters are not billed tokens.[2][3]

Restore the backed-up rule and original tool selections. Reattach full sources or reopen the retained chat if the handoff fails. Revert only this task's file edits through reviewed diffs/backups, preserving unrelated work. If separately approved billing settings were changed, restore the original provider/key-enabled state through Settings > Models; do not delete credentials as a cleanup shortcut. Local rollback cannot undo external writes or refund usage.

## Limits and evidence

Documented configuration and UI instructions, not native-smoke-tested. No universal context meter or measured saving is supplied. Hook telemetry is not automatically a complete billing ledger. Proprietary indexing, system prompts, Tab, background agents and other extension traffic are outside this recipe's interception control. Permissions for source data, Cursor processing and any third-party MCP server must all be acceptable before work begins.[1][38][76]

## Sources

[1] https://cursor.com/docs/settings/api-keys
[2] https://cursor.com/docs/context/rules
[3] https://cursor.com/docs/account/pricing
[38] https://cursor.com/docs/hooks
[76] https://cursor.com/docs/mcp
