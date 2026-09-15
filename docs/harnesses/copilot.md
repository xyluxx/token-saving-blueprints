# GitHub Copilot: IDE and CLI are different routes

[Start here](../../START-HERE.md) · [Conservative](../modes/conservative.md) · [Aggressive](../modes/aggressive.md) · [Authentication and billing](../auth-and-billing.md) · [Measurement](../measurement.md)

Checked 2026-09-06 (UTC). Evidence: documented unless stated otherwise; no authenticated agent task or savings benchmark was run.

## Who this is for

Copilot users who want tighter task context without replacing native GitHub authentication. The concrete IDE recipe below is for VS Code. Do not assume its settings, model-provider extensions or instruction discovery work identically in Visual Studio, JetBrains or other Copilot hosts. Copilot CLI is a separate terminal harness with its own commands and context controls.[31][46][55]

## Authentication and billing routes

* Native IDE or CLI: GitHub account authorization uses the applicable Copilot entitlement. Current individual billing uses GitHub AI Credits, with base credits plus a variable flex allotment and separately budgeted additional usage. Paid code completions and next edit suggestions are not billed in AI credits. Old premium-request figures are not the current universal meter.[54]
* VS Code BYOK: Chat: Manage Language Models > Add Models adds a supported provider. Chat/utility BYOK can work without GitHub sign-in or a Copilot plan. Inline suggestions, semantic search and embedding-dependent features have different requirements; do not claim the whole IDE is moved to the provider. Azure OpenAI Entra ID and compatible endpoints are documented. Administrators can disable BYOK. Agent Host BYOK requires its separate experimental setting.[31]
* CLI OAuth: `copilot login` uses the official web/device flow. Existing `COPILOT_GITHUB_TOKEN`, then `GH_TOKEN`, then `GITHUB_TOKEN` can select authentication instead; never print their values. A GitHub automation token may change whose entitlement is used. Classic PATs are not supported by the current CLI reference.[46]
* CLI external-model boundary: the CLI reference exposes `copilot help providers` and mentions BYOK behavior, but a complete current CLI provider-configuration contract was not recovered in this review. Keep any approved existing provider untouched; classify new CLI BYOK setup as limited pending the installed help. Do not copy VS Code model JSON or Copilot SDK provider examples into the CLI.[46]

A native seat plus a VS Code API model can create hybrid billing. Token reduction may preserve AI credits or reduce additional usage; it does not refund the fixed subscription. Record provider-side charges separately.

## Conservative recipe

1. Back up the project's instructions. Record account, provider/model/effort, selected tools, additional-usage budget and enabled API models. For CLI, check environment variable presence without exposing token values. Do not log out or add a provider to perform this recipe.
2. Merge a small task discipline section into repository-root `.github/copilot-instructions.md`. Both the reviewed VS Code and CLI routes support it. Do not overwrite existing requirements or duplicate them through several instruction files.[55][85]

   > Keep the approved model, effort and permissions. Enumerate the complete candidate set for this task. Read targeted source ranges and relevant dependencies; record coverage. Use deterministic code for mechanical edits and exact all-record calculations. Make a minimal coherent patch. Run the full required test/check set and report actual output and unresolved failures. Preserve source identifiers, user decisions and external-action status. Do not rewrite history or infer unreviewed records from a sample.

3. IDE: open Copilot Chat, confirm the existing model, attach the task's files using the context picker, and inspect the included context. Avoid broad attachment when it is not required. Custom instructions do not apply to inline suggestions.[55]
4. CLI: in the project, run `copilot` using the existing authorized setup. Use `/instructions` to confirm the merged file is enabled and `/context` to record the current context categories. Attach the named files and request a coverage-first investigation.[46][52][85]
5. Approve only existing necessary tools and exact operations. Use native search and patching for coding; use the project's parser/database for complete counts. Run every required test even if its successful output will be summarized afterward.

## Aggressive recipe

1. Both routes: before expensive reads, produce a narrow observation with existing terminal/query tools. Retain raw results locally, including source revision, exact query/filter, total matched records, exit status, all failing test names and original error locations. Give the agent that view, not a sampled dataset. Restore raw detail for contradictions, missing counts, changing revisions or unexamined failures.
2. CLI has a genuine native seam: preserve a reviewed handoff file and source artifacts, then use `/compact` at a phase boundary if additional lossy summarization is approved. Inspect `/context` afterward. Automatic compaction and large-output offloading are already native behavior; leave their thresholds alone in Conservative mode and do not count them twice.[52]
3. Compaction loses fine detail. Preserve exact requirements, identifiers, open questions, completed external actions and test evidence outside the summary. Ask the next turn to identify the original sources and verify one protected requirement against them. If it cannot, reattach the originals or start a fresh session from the retained full evidence. The CLI checkpoint is a summary artifact, not a complete transcript backup.[52]
4. IDE alternative: retain the original chat and start a new task chat with the reviewed handoff and explicit files. This is a supported ordinary chat workflow, not an undocumented IDE transcript-editing hook.

Control ceiling: native CLI compaction/inspection is not universal IDE control. VS Code provider extensions and MCP servers add their own capabilities; they do not intercept every Copilot surface. Avoid custom compressors, telemetry exporters and permission bypasses for this recipe.

## Verify and roll back

Require the same input scope, model, effort and tests for baseline and comparison. In CLI record `/context`; in either surface record observed account AI credits and provider charges. Context occupancy is not cumulative billed usage. Include compaction and any retry overhead. If usage is only an aggregate dashboard change, label attribution uncertain.[52][54]

Restore only the added instruction section and task-specific tool choices. Use the editor's reviewed file diff/backups to undo task edits. Retain the old chat before starting a new one; no promise is made that `/compact` can be reversed into full history. Restore source material explicitly. Leave original credentials and budgets intact. A file rollback never reverses a GitHub issue, PR, deployment or other external write.

## Limits and evidence

Documented, no authenticated native run. CLI BYOK setup remains limited, not unsupported in principle. Host-specific UI versions and enterprise policies must be checked before use. Keep secrets out of instructions and logs; read-only repository permission does not authorize sending its contents to an unapproved BYOK provider or MCP service. Built-in Ollama support in VS Code is deprecated in favor of the official Ollama extension, so old local-model setup instructions need revision.[31]

## Sources

[31] https://code.visualstudio.com/docs/copilot/customization/language-models
[46] https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference
[52] https://docs.github.com/en/copilot/concepts/agents/copilot-cli/context-management
[54] https://docs.github.com/en/copilot/concepts/billing/usage-based-billing-for-individuals
[55] https://code.visualstudio.com/docs/copilot/customization/custom-instructions
[85] https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions
