# Codex CLI

[Start here](../../START-HERE.md) · [Conservative](../modes/conservative.md) · [Aggressive](../modes/aggressive.md) · [Auth and billing](../auth-and-billing.md) · [Measurement](../measurement.md)

Checked 2026-09-07 UTC. Evidence: documented plus installed CLI help inspection. No authenticated model call or end-to-end integration trial.

## Who this is for

Users of OpenAI's Codex CLI, including ChatGPT subscribers and API/cloud customers. This guide optimizes work inside the current route. It does not turn a ChatGPT subscription into a general-purpose API key.

## Authentication and billing routes

1. Native ChatGPT: `codex login` opens the first-party browser flow. On SSH/headless hosts, `codex login --device-auth` is documented when device-code login is enabled in the account/workspace. The user authorizes their own account. Local CLI and IDE credentials can be shared by those surfaces; Codex cloud requires ChatGPT sign-in.[23]
2. Direct OpenAI API: provision your own Platform key privately, then use the documented stdin command below. This selects API billing instead of included ChatGPT plan credits.[23]

   ```sh
   printenv OPENAI_API_KEY | codex login --with-api-key
   codex login status
   ```

   Run only when intentionally choosing API mode, with the variable already supplied securely. Do not paste a key into command arguments or logs.
3. Enterprise automation: current docs also distinguish Codex access tokens from Platform keys and describe workload identity federation. These require workspace permissions or a configured trust relationship. A cached OAuth access token copied from another harness is not automatically a Codex enterprise access token.[23]
4. Cloud: current docs include built-in `amazon-bedrock` using the AWS credential chain or a named profile/region, and custom Azure Responses configuration using the exact endpoint, deployment, API version and `AZURE_OPENAI_API_KEY`. Confirm the installed version supports the chosen cloud path. AWS/Azure billing and IAM apply, not ChatGPT subscription credits.[26]
5. Gateway or local model: custom providers can use their own `env_key`. Setting `requires_openai_auth = true` instead selects OpenAI authentication and ignores `env_key`. Current advanced configuration also supports an approved command-backed `model_providers.<id>.auth` helper; do not combine that auth table with `env_key`, `experimental_bearer_token` or `requires_openai_auth`. Absence of the two usual selectors alone does not prove an unauthenticated route: inspect the effective auth table, bearer-token and header settings without printing their values. Preserve an existing organization helper rather than creating one for token savings. Use only an approved endpoint with the correct protocol; do not forward ChatGPT tokens to an unrelated or unapproved host. The first-party auth guide does document OpenAI authentication through an LLM proxy; that does not certify every gateway, model or account.[23][25][26]

Configuration normally lives in `~/.codex/config.toml` under `CODEX_HOME`. Managed restrictions, selected provider, CLI overrides and stored auth all matter. A provider can be configured without being selected. Record `codex login status` and the actual selected model/provider at startup, not just environment-variable presence. Include configured credential helpers and explicit or environment-backed authentication headers in the private audit; a missing API-key variable is not proof of no credential path.[23][25][26]

For an already authorized third-party Responses endpoint, this is a declaration-only template to merge under a unique provider ID in the user config. Replace both placeholders from that provider's documentation; it deliberately does not change `model_provider` or `model`.[23][26]

```toml
[model_providers.approved_gateway]
name = "Approved API gateway"
base_url = "https://YOUR_APPROVED_HOST/v1"
wire_api = "responses"
env_key = "APPROVED_GATEWAY_API_KEY"
requires_openai_auth = false
```

Do not use this template for a Chat-Completions-only service, or replace the built-in `openai` provider ID. Test reasoning items, tool IDs, cancellation and usage before adopting it. Free local inference still has hardware and operational costs.

## Conservative recipe

1. Inspect without logging in or making requests:

   ```sh
   codex --version
   codex exec --help
   codex login status
   ```

   The local binary inspected for this guide was `codex-cli 0.149.0`; your installed help is the authority for available flags.[23][25]
2. Merge a concise project policy into the existing root `AGENTS.md`: exact path/symbol discovery, complete requested coverage, deterministic bulk computation, existing dependencies first, native patches, all required tests, and explicit unresolved errors. Do not duplicate large global instructions in every nested directory.[26]
3. Preserve Codex's existing sandbox/approval policy, model and reasoning effort. Use exact reads and `apply_patch`; compute all-row totals in local code and retain source files rather than asking the model to reproduce every cell.
4. Keep native compaction and discovery in the baseline. MCP tools are optional task interfaces, not a model-auth bridge. Connect each approved server with its own user-owned service authorization. Current code-mode features are version-dependent and not required by this recipe.[24][25]
5. Use a bounded real task and inspect all required artifacts/tests. If the prompt requires full review, do not replace the full diff or record set with a summary.

## Aggressive recipe

Use explicit, source-linked observation views produced by approved tools before context ingestion. Save the full output, source version, command, exit status and omitted ranges; restore the relevant raw range when an exception, contradiction, coverage mismatch or failed test appears.

A reviewed checkpoint can seed a new native session: include task scope, exact state, approvals, completed external actions, coverage and unresolved failures. Never rewrite encrypted reasoning/compaction items or retag persisted threads to make them fit a different provider.

Current Codex does have `PreToolUse` input rewriting via `updatedInput` for supported tools. That does not make Claude output hooks portable: `updatedMCPToolOutput` and `suppressOutput` remain unsupported in the documented post-tool contract. Blocking/replacing with feedback is not a transparent output reducer. No hook installer or history surgery is prescribed here.[24]

## Verify and roll back

For a user-approved smoke test in a trusted existing repository, this documented headless command keeps model/auth selection unchanged while making shell access read-only:[27]

```sh
codex exec --sandbox read-only --json "Read README.md and identify its title. Do not edit files or use external services."
```

This can consume plan quota or API funds. Read-only shell sandboxing does not automatically revoke independent remote MCP write permissions; disable unauthorized remote services before the trial. Check the real answer against the file, inspect errors and usage events, then separately exercise an approved native patch/test workflow and verify its complete output.

Restore only added `AGENTS.md` text and config keys. Remove an experimental provider declaration only if nothing else depends on it; reselect the exact prior provider/model if you intentionally changed it. A fresh process reverts run-scoped flags. Use `codex logout` and native login only when reverting an intentional auth change; the CLI and IDE may share the same credential cache.[23]

If reduced context was insufficient, restore original observations in a new checkpointed session. Never re-run an external write merely to recover its missing output.

## Limits and evidence

Public docs evolve faster than installed binaries. New enterprise, hook and cloud features require version and account validation. The proposed gateway template is documented syntax, not a claim that an arbitrary provider implements Codex correctly. No native smoke test was performed during this research. All helpers, restoration calls and failures belong in the measured task cost.

## Sources

[27] https://developers.openai.com/codex/noninteractive.md — noninteractive-execution
[23] https://developers.openai.com/codex/auth.md — codex-auth-md
[24] https://developers.openai.com/codex/hooks.md — codex-hooks
[25] https://developers.openai.com/codex/config-reference.md — codex-config-md
[26] https://developers.openai.com/codex/config-advanced.md — codex-advanced
