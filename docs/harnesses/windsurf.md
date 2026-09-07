# Windsurf / Devin Desktop

[Start here](../../START-HERE.md) · [Conservative](../modes/conservative.md) · [Aggressive](../modes/aggressive.md) · [Authentication and billing](../auth-and-billing.md) · [Measurement](../measurement.md)

Checked 2026-09-06 (UTC). Evidence: documented unless stated otherwise; no authenticated agent task or savings benchmark was run.

## Who this is for

Existing Windsurf users: current first-party setup documentation calls the IDE **Devin Desktop**. The package name and login language changed while many documentation URLs still use `windsurf`. The primary local harness is now **Devin Local**; Cascade remains a separate legacy agent. This is not merely a model rename.[39][42]

## Authentication and billing routes

* Native Desktop account: use the existing authorized Devin/Windsurf account and plan. Current self-serve billing uses daily/weekly quota with optional paid extra usage, rather than a universal per-prompt credit allowance. Enterprise may use ACUs or a legacy credit contract.[9][41]
* Devin Local and Cascade: both are local agent choices within the IDE but have different features, models and permission behavior. Preserve the current agent; changing it is a separate migration, not this blueprint's saving.[39][40]
* BYOK boundary: old discovery/index material mentions BYOK, but the current model page retrieved for this review did not provide a complete active BYOK setup contract. Keep existing approved configurations untouched. New BYOK/cloud-endpoint migration is **limited** until the installed build and current vendor help confirm entitlement, models, fees and data path. Do not reuse old instructions as a universal current route.[34][40]
* A Devin API key used for manual Desktop login is an account credential, not an arbitrary OpenAI-compatible inference key.[42]

Quota reductions preserve allowance; they do not refund a seat. Extra usage is billed separately, and enterprise ACUs can include more than local model tokens. Preserve the actual contract and extra-usage settings rather than forcing legacy credit formulas.[9][41]

## Conservative recipe

1. Record version, account/plan, current agent, model/effort, usage meter, extra-usage state and existing permissions. Back up project rules and any task-local configuration. Do not run the migration wizard or switch agents as part of this recipe.
2. Devin Local: use the session/new-tab menu's Open customizations to see loaded rules, skills, hooks and MCP servers. Merge the following discipline into the project's existing `AGENTS.md`. If using Cascade, inspect Customizations and the existing project rule instead; both root `AGENTS.md` and the documented rule system are available.[10][39][83]

   > Preserve model, effort, permissions and acceptance criteria. Enumerate the full candidate set and report source coverage. Read precise task-relevant ranges plus dependencies. Use deterministic tools for bulk edits and complete-row calculations. Make minimal patches, run every required test, and report real failures. Do not infer all-record review from an aggregate or sample; do not rewrite history.

3. If adding a scoped Cascade rule through the UI, confirm its activation mode. Current docs prefer `.devin/rules/` while retaining `.windsurf/rules/` compatibility. Inspect loaded files to avoid duplicated/conflicting legacy instructions; do not blindly rename the whole directory.[10][83]
4. Devin Local: select Plan mode for the initial read-only investigation, review its saved plan, then approve implementation through the normal permission flow. Cascade: use its Chat mode for the investigation and switch to Code only for approved edits. These are distinct controls.[39][82]
5. Give the agent the exact relevant source files. Use native search/editor/terminal for minimal changes. Keep required tests intact; reduce repeated irrelevant observation, not execution coverage.
6. Inspect each needed MCP tool and its source-data permission. Devin Local normally prompts before MCP calls, unlike Cascade's documented behavior. Do not carry an all-server approval across the migration without review.[39]

## Aggressive recipe

1. Have the existing terminal or approved query tool save raw test/query output and return an explicit view: source revision, complete record/file coverage, test exit status, all failures and original locations. Process all rows for calculations; page through all rows when review of each is required.
2. Before a phase change, save a reviewed handoff beside the task artifacts. Include exact requirements, key identifiers, completed external actions, unresolved decisions and verified tests. Preserve the old session, then create a new conversation using the same agent/model and only the handoff plus necessary sources.
3. Reopen raw evidence for stale revisions, missing counts, uncertain dependencies, forgotten requirements or any new test failures. Keep complete coverage and actual final answers, not just artifact pointers.
4. Devin Local's plan file can be reviewed and carried into the next phase, but it is not a replacement for all source evidence. Cascade's conversation references retrieve relevant summaries/parts, typically not the complete conversation.[39][82]

Control ceiling: local native permissions and sandboxing are useful execution controls; rules and handoffs do not universally transform hidden prompts. Devin Local does not persist Cascade auto-memories. Use explicit rules/skills for durable requirements, and treat any memory migration as separately reviewed work.[10][39]

## Verify and roll back

Confirm the actual agent and loaded rule in Customizations, compare the patch with the approved file list, and run the full required checks. Record quota/extra-usage or contractual ACU observations from Plan Info/account usage; do not equate a visible percentage with raw tokens or cash saved.[9][41]

Restore only the added rule section and previous tool/permission choices. Reopen the original conversation or raw sources if the handoff loses details. Undo task edits through a reviewed diff and backup, preserving unrelated work. Do not migrate memories, change provider, or disable Cascade during rollback. File restoration cannot undo remote actions.

## Limits and evidence

Documented, no authenticated test. This guide covers Desktop local agents, not Devin cloud tasks, standalone CLI setup or Windsurf editor plugins. First-party pages currently mix old names/credit language with new Desktop/local-agent documentation; prioritize the exact installed build and account contract.[9][42][82]

No vendor-reported percentage reduction from changing harnesses is counted as this blueprint's measured saving.[39]

## Sources

[9] https://docs.windsurf.com/windsurf/accounts/usage
[10] https://docs.windsurf.com/windsurf/cascade/memories
[34] https://docs.windsurf.com/llms.txt
[39] https://docs.windsurf.com/windsurf/devin-local
[40] https://docs.windsurf.com/windsurf/models
[41] https://docs.windsurf.com/windsurf/accounts/quota
[42] https://docs.windsurf.com/windsurf/getting-started
[82] https://docs.windsurf.com/windsurf/cascade/cascade
[83] https://cli.devin.ai/docs/extensibility/rules
