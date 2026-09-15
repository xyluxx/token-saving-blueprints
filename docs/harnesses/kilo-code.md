# Kilo Code

[Start here](../../START-HERE.md) · [Conservative](../modes/conservative.md) · [Aggressive](../modes/aggressive.md) · [Authentication and billing](../auth-and-billing.md) · [Measurement](../measurement.md)

Checked 2026-09-06 (UTC). Evidence: documented unless stated otherwise; no authenticated agent task or savings benchmark was run.

## Who this is for

Teams already using Kilo Code's editor extension or CLI.[19] Current docs describe a newer configuration engine with `kilo.jsonc`, native snapshots and multiple provider paths. Do not blindly apply older Roo-style `.kilocode` recipes or treat every Kilo-branded service as one billing route.[44][45][84]

## Authentication and billing routes

* Kilo Gateway account: paid model inference draws from the Kilo balance. Current billing documentation says upstream model pricing has no inference markup but credit purchases carry a separate payment-processing fee. Team platform charges and provider inference should be accounted for separately.[67]
* Gateway BYOK: a key saved to the Kilo account/organization routes matching models through that provider. The model picker shows a BYOK badge. Invalid matching keys fail rather than falling back to Kilo keys. Kilo-side inference cost is reported as zero for BYOK, but the external provider still bills it.[43][67]
* Direct provider: Settings > Providers can configure direct OpenAI or Anthropic access; native cloud routes include Azure, Bedrock and Vertex. This is distinct from storing a key in Gateway BYOK. Preserve the actual provider/endpoint and data-residency agreement.[66][73][74]
* ChatGPT subscription: Kilo documents Sign in to OpenAI Codex through its ChatGPT Plus/Pro provider. This is an official Kilo UI OAuth integration with the Codex catalog, not an exported subscription token. It covers core extension/CLI use, not Kilo Cloud Agents or Deploy, which require Gateway. Native subscription limits still apply.[75]

Changing from Gateway balance to provider API or OAuth is a separate billing decision, not a default optimization. A subscription quota saving is not a refund. Check both Kilo and provider records for hybrid usage; a zero-cost Kilo BYOK entry alone is not “free.”[43][67][75]

## Conservative recipe

1. Record version, provider/model/effort, Gateway/BYOK badge or OAuth state, tools, auto-approve settings, snapshots and any built-in paste summarization. Leave them as configured. Back up every effective project config and rule; do not copy secrets into notes.
2. Inspect project `kilo.jsonc` and `.kilo/kilo.jsonc`; the latter wins when both exist. Other legacy configuration may also merge. Settings UI clearing can remove a setting from multiple files, so prefer a targeted project edit for this recipe, not clearing global controls.[84]
3. Create `.kilo/rules/task-scope.md` and add that single path to the existing effective project's `instructions` array, retaining all existing entries. Do not replace the whole config. Current docs require that reference; merely creating a new rule directory is not enough. Legacy `.kilocode/rules/` is still auto-included, so check for duplicate rules.[44]

   > Preserve current provider, model, effort, permissions and all acceptance criteria. Enumerate the full candidate set; read exact relevant ranges and dependencies while tracking coverage. Use existing deterministic tools for bulk edits and all-row computations. Make minimal patches and run every required test. Report real failures and blockers. Do not clear history or replace required full review with sampled records.

4. Extension: open a task, select the existing model and attach the exact source files. CLI: use the installed client's normal interactive task with the same project config, not a copied extension-only button or a new auth flow. Rules apply on the next interaction; verify that the task recognizes the effective rule and prior requirements.[44]
5. Use native search/patch/terminal and only approved tools. Inspect permission prompts rather than increasing auto-approve. Keep source credentials read-only when writes are unnecessary. Built-in paste summarization is not exact ingestion of every record; use direct tool reads and a coverage checklist when that matters.[84]
6. Review all task diffs and run the complete test/check list. Do not use task completion text or snapshots as proof that tests passed.

## Aggressive recipe

1. Through existing terminal or approved MCP tools, retain raw query/test output and return a task-specific view containing source revision, exact query, complete coverage/counts, all failures, exit status and original locations. No new gateway or custom compressor is needed.
2. Feed that view into the next step instead of repeated success logs. For required all-record review, page through every record; the view cannot stand in for omitted review. Reopen raw data when counts, source revision, acceptance criteria or test outcomes disagree.
3. At a phase boundary, preserve a handoff with exact identifiers/requirements, decisions, changes, tests, pending work and already performed external actions. Retain the old session and begin a new one with the same provider/model plus the handoff and needed files.
4. Compare critical details to original sources before further writes. Do not rely on automatic clipboard summaries or rewound conversations as a full-state backup.

Control ceiling: best-effort rules plus native context/tool/config controls. Kilo Gateway is an existing optional billing/provider service, not proof every IDE request can be intercepted. Snapshots affect supported workspace changes; they do not summarize history losslessly or reverse remote actions.[44][45]

## Verify and roll back

Confirm that only one effective task-rule reference was added and that old rules still apply. Compare the same scoped task/model/effort, complete tests and patch quality. Gateway usage exposes input/output/cache token categories, cost and BYOK status; reconcile provider billing for BYOK and subscription quota for OAuth. Include retries and native helper calls, and do not count built-in caching twice.[67]

Restore the original project instructions array/rule, attachment selection and any separately approved setting changes. For snapshots, use the task's Revert to here control only after reviewing the affected range and preserving unrelated work. If snapshots are disabled or absent, only the conversation may rewind while files remain changed. Snapshots exclude ignored files and require an eligible Git workspace. Check actual files and tests after restoration; use your original backups when needed.[45]

OAuth tokens are not included in the extension's settings export. Preserve the existing login rather than treating a config backup as a credential backup. Do not disconnect a provider just to undo a rule. Filesystem restoration cannot refund inference or reverse a database/API write.[75]

## Limits and evidence

Documented, not authenticated/native-smoke-tested. The step-by-step editor UI targets the current VS Code extension; JetBrains UI parity is not asserted. CLI shared project rules and the documented OAuth route are covered, but no undocumented CLI settings flags are supplied. Read-only source permissions do not authorize copying data to an unapproved provider or remote tool. Current and legacy configuration can merge, so preserve all effective originals before editing.[44][75][84]

## Sources

[19] https://kilo.ai/docs
[43] https://kilo.ai/docs/getting-started/byok
[44] https://kilo.ai/docs/customize/custom-rules
[45] https://kilo.ai/docs/code-with-ai/features/checkpoints
[66] https://kilo.ai/docs/ai-providers
[67] https://kilo.ai/docs/gateway/usage-and-billing
[73] https://kilo.ai/docs/ai-providers/openai
[74] https://kilo.ai/docs/ai-providers/anthropic
[75] https://kilo.ai/docs/ai-providers/openai-chatgpt-plus-pro
[84] https://kilo.ai/docs/getting-started/settings
