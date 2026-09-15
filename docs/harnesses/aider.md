# Aider

[Start here](../../START-HERE.md) · [Conservative](../modes/conservative.md) · [Aggressive](../modes/aggressive.md) · [Authentication and billing](../auth-and-billing.md) · [Measurement](../measurement.md)

Checked 2026-09-06 (UTC). Evidence: documented unless stated otherwise; no authenticated agent task or savings benchmark was run.

## Who this is for

Developers already using Aider in a terminal and wanting direct control over editable files, read-only references and visible context size. Its native `/add`, `/drop`, `/read-only`, `/tokens` and `/test` commands give this recipe more explicit control than a closed IDE's attachment advice.[11]

## Authentication and billing routes

* Provider API: Aider is the coding harness, not a bundled model subscription. Its documented provider configuration uses keys for direct providers or approved aggregators, and can also target local OpenAI-compatible inference.[64][70]
* Cloud: Azure uses the deployment name and endpoint, not simply a public model name. Bedrock uses AWS credentials and the appropriate model or inference-profile identifier. Preserve the current tenant, region and deployment policy.[71][72]
* Subscription boundary: this guide does not establish a native ChatGPT/Claude consumer-subscription OAuth route for Aider. Do not paste browser tokens into API-key fields or install a subscription proxy. Keep any organization-approved API/provider contract unchanged.
* Configuration risk: credentials may be supplied through flags, environment, `.env`, or `.aider.conf.yml`. Aider's YAML search order allows later files to take priority. Inspect the effective configuration privately before comparing costs; never print a secret in a report or assume the home configuration wins over the project.[70][86]

Local models have hardware/hosting costs; API providers bill their usage; a consumer subscription does not offset those charges automatically. Existing main, weak and editor models may all contribute cost. Do not silently switch models or effort.[11][12]

## Conservative recipe

Prerequisite: an existing authenticated Aider installation, a backed-up task workspace and the project's real test commands. The names below are placeholders: replace `path/to/target.py`, `path/to/spec.md` and `PROJECT_TEST_COMMAND` with existing project values before use.

1. Outside a model task, `aider --version` and `aider --help` identify the installed command surface. Record the existing model/provider, effort and relevant configuration privately. Do not reinstall or alter global config.[12]
2. In the existing session, run `/ls` and `/tokens`. Use `/read-only path/to/spec.md` for specifications and `/add path/to/target.py` only for files that need full review or editing. `/drop` removes irrelevant attached files. Retain required dependencies; the repository map is an index, not proof every file was reviewed.[11]
3. Add a short task instruction through your normal prompt or an already existing read-only project instruction file:

   > Enumerate all candidate files and preserve exact requirements. Read dependencies before patching; state coverage. Use deterministic bulk changes and computations over all required rows. Make the smallest coherent edit. Keep current models, effort and permissions. Run every required test and report actual failures. Do not clear history, sample required records, or replace a requested answer with a pointer.

4. Use `/ask` for the initial investigation and `/code` only for the approved implementation. Confirm the selected mode. Review `/diff` after each meaningful change rather than asking for repeated whole-file rewrites.[11]
5. Use `/test PROJECT_TEST_COMMAND` for each real required test command. It adds failed output to the conversation on a nonzero exit. A quiet successful run is not proof of all tests passing unless the command, coverage and exit result were actually checked. Preserve the complete test log separately when acceptance requires it.[11]
6. Compare `/tokens` after the attached-file reduction. This is current context reporting, not a provider invoice or full session token total.[11]

## Aggressive recipe

1. Use `/run` with the project's existing parser/query/test command to save a complete local result. Decide whether to add the result to chat. Prefer a reviewed view containing exact coverage, revision, full-row totals, all exceptions, test exit status and raw result locations over repeated success logs.[11]
2. Attach only that view through `/read-only`. Keep the complete input/result recoverable, with the same source-data access permissions. For all-record review, keep reading every record; a complete aggregate only proves its computation, not that review.
3. At a phase boundary, save the current file selection using `/save` and preserve a private copy of relevant conversation/context using `/copy-context` plus your existing transcript retention. `/save` stores commands to reconstruct file selection, **not** the conversation.[11]
4. Write and review a handoff containing exact requirements, identifiers, changed files, remaining work, tests and already executed external actions. Only then, with approval for lossy reset, use `/clear` and reintroduce the handoff plus required original sources. Prefer a separate new session if retaining the old context matters. `/reset` is broader: it drops files as well as history, so it is not this recipe.[11]
5. Verify protected details against the originals. Wrong identifiers, missing acceptance criteria, changed input revision or new test failures trigger full-source reattachment. Do not repeatedly clear until the symptom disappears.

Control ceiling: Aider provides explicit file/context commands. This is not a new transparent compressor, and no claim is made that `/clear` is reversible into an identical hidden state. Architect/two-model mode, weak-model changes and effort changes are separate cost/quality choices, not this recipe.[11]

## Verify and roll back

Run the same task with the same model/effort and full acceptance checks. Record `/tokens`, actual provider usage/cost where available, all test results and retry work. Include weak/editor-model usage and any summarization overhead when present. Estimated context or model metadata can disagree with billed usage.

Restore the original file selection using the saved command file after inspecting it, or reattach manually; `/load` executes commands, so never load an untrusted file. Restore original instruction/config edits. `/undo` only undoes Aider's last commit, not arbitrary earlier edits; inspect scope first and use the project's normal backup/diff workflow when necessary. Reattach original evidence after `/clear`; no automatic history restoration is promised. External operations are not undone by file rollback.[11]

## Limits and evidence

Documented commands; local read-only `--version`/`--help` confirmed Aider 0.86.2. No model call, provider authentication test or savings benchmark was run. Provider documentation contains older example model names, so examples are not recommendations to switch away from the approved model.[64]

Keep secrets out of copied context and source artifacts. A read-only attached file is read-only for editing, not prevented from being sent to the provider. Aider's native tools are the recipe; no universal MCP interception or third-party OAuth adapter is claimed.

## Sources

[11] https://aider.chat/docs/usage/commands.html
[12] https://aider.chat/docs/config/options.html
[64] https://aider.chat/docs/llms.html
[70] https://aider.chat/docs/config/api-keys.html
[71] https://aider.chat/docs/llms/azure.html
[72] https://aider.chat/docs/llms/bedrock.html
[86] https://aider.chat/docs/config/aider_conf.html
