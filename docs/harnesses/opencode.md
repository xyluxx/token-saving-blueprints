# OpenCode

[Start here](../../START-HERE.md) · [Conservative](../modes/conservative.md) · [Aggressive](../modes/aggressive.md) · [Auth and billing](../auth-and-billing.md) · [Measurement](../measurement.md)

Checked 2026-09-06 UTC. Evidence: current official documentation. No installed-binary or authenticated provider trial.

## Who this is for

Users of OpenCode who want exact navigation, focused edits and less repeated tool output without replacing their current provider, model, effort or permission policy. Existing native features are the baseline, not savings attributable to this guide.

## Authentication and billing routes

1. Native supported subscriptions: use `/connect`, choose OpenAI, then the documented ChatGPT Plus/Pro browser option; authorize your own account. The provider guide also documents supported GitHub Copilot and GitLab Duo subscription integrations. Provider entitlement is distinct from installing the OpenCode binary.[32]
2. Direct API keys: `/connect` → provider → manual API key uses that provider's API bill. Keys are stored in the user's OpenCode credential store; environment variables and project `.env` can also supply credentials. Do not import someone else's store or put real keys in a shared repo.[32][45]
3. Anthropic subscription limit: the current provider page includes old Pro/Max instructions but also explicitly says those plugins are prohibited and no longer bundled as of 1.3.0. Do not advertise Claude Pro/Max login as supported on the strength of the stale subsection. Use an approved Anthropic API key or cloud route instead.[32]
4. AWS Bedrock: use the existing named AWS profile/credential chain or documented Bedrock bearer-token path, with the approved region/model access. Google Vertex uses the approved project and ADC/service account. Azure OpenAI uses the actual resource/deployment and supported key or Microsoft Entra ID method. These are cloud bills and cloud IAM boundaries, not consumer plan credits.[32]
5. OpenCode-hosted/gateway providers: Zen/Go and other listed services have their own keys, plans and terms. `provider.<id>.options.baseURL` can route inference to a custom endpoint. An approved third-party endpoint must implement the selected SDK/protocol, model/tool schema, streaming and error/usage semantics. Do not repoint subscription OAuth to an unrelated service.[32]
6. Local models: documented compatible local endpoints are possible. Hardware cost, model capability and context limits remain real; local/cheaper routing is a separate explicit cost choice, not token reduction.[32]

Use `/models` to inspect the actual provider/model selection. Configuration is merged: remote organizational defaults, user config, custom config, project config and inline overrides can all contribute; managed settings can take highest priority. User config is normally `~/.config/opencode/opencode.json`, with project `opencode.json` and explicit override variables. A provider declaration or saved key alone does not prove the active route.[36][51]

Do not assume a universal credential-priority rule across all provider SDKs. Inspect environment, the relevant provider options and saved authentication locally, then verify the actual endpoint and bill. Subscription usage estimates are not API charges.

## Conservative recipe

1. Confirm the installed surface before invoking inference:

   ```sh
   opencode --version
   opencode auth list
   ```

   `auth list` reports stored providers, not the health or active routing of every credential.[45]
2. Merge a compact original policy into existing project `AGENTS.md`: locate relevant sources first; read full material when requested; preserve every record for exhaustive review; compute exact bulk values in code; reuse dependencies; produce the smallest complete patch; run all required tests and report failures. Do not replace project-specific conventions or security rules.[52]
3. Use native LSP where available, then exact reads of the affected code/callers/tests. Do not add a second language server simply because it has a familiar name. Native diagnostics help but do not replace integration or behavioral tests.[66]
4. Keep only task-relevant authorized MCP tools and extensions. Native permissions remain active. A reduced tool catalog must not hide recovery or required verification tools.[36]
5. Retain raw source/output and counts for deterministic data work. Return exact requested outputs and exceptions rather than repeating every transport field. All-record interpretation is not satisfied by inspecting a sample.

## Aggressive recipe

First use explicit new observation views with retained source versions, errors and omitted spans. Prepare a reviewed checkpoint with exact task state, corrections, approvals, already-performed actions and unfinished tests before using `/compact`.[51]

Current config docs say automatic compaction defaults to true and old-tool-output pruning defaults to false. Do not repeat an older source audit's pruning behavior as today's universal default. This optional project-scope JSON merge enables the documented pruning switch for a separately approved experiment; it does not alter model or permission settings:[36]

```json
{
  "$schema": "https://opencode.ai/config.json",
  "compaction": {"prune": true}
}
```

Merge into the existing project `opencode.json`, preserving all other keys and any existing `compaction` settings. Before enabling, retain needed raw results and a checkpoint. Pruning can remove evidence from what the model sees. Do not treat a compressed transcript as the authoritative source.

Custom plugins and MCP tools are possible, but this guide installs none. Do not port a Claude hook by renaming an event, combine multiple reducers over the same output, or rewrite opaque provider history. Learned compression, cheaper providers and effort changes are separate experiments with their own approvals.

## Verify and roll back

In a trusted disposable repository, after authorizing the usage test and auditing inherited MCP/permission settings, use the documented headless shape:[45]

```sh
opencode run "Read README.md and identify its title. Do not edit files or use external services." --format json
```

The prompt is advisory, not a read-only sandbox. Preserve native permissions and disable unapproved service access before the trial. Inspect the actual route/model, returned title and error/usage events, then test an approved patch, full checks and a harmless denied action. Include a planted old-output exception and make the agent restore it before accepting a pruning trial.

`opencode stats` provides session usage/cost statistics; reconcile with the provider bill and include all retries, compressor calls and restored reads.[45]

Remove the added policy and restore the exact previous `compaction.prune` value or remove only that newly added key. Restoring a setting does not reconstruct previously lost model-visible content: reopen retained originals in a new checkpointed session. Restore only the intentionally changed provider settings/selection, and reauthorize your own account if required. Do not delete the whole auth store or revoke other providers to undo one experiment.

## Limits and evidence

Current documentation differs from the earlier snapshot in defaults and some auth guidance. The explicit Anthropic prohibition outweighs stale login instructions on the same page. This guide does not certify any third-party plugin, every compatible API, or a whole-task savings percentage. No native smoke test or full model benchmark was run.

## Sources

[32] https://opencode.ai/docs/providers — opencode-provider
[36] https://opencode.ai/docs/config — opencode-config
[45] https://opencode.ai/docs/cli — opencode-cli
[51] https://opencode.ai/docs/tui — opencode-tui
[52] https://opencode.ai/docs/rules — opencode-rules
[66] https://opencode.ai/docs/lsp — opencode-lsp
