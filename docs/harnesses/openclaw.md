# OpenClaw

[Start here](../../START-HERE.md) · [Conservative](../modes/conservative.md) · [Aggressive](../modes/aggressive.md) · [Auth and billing](../auth-and-billing.md) · [Measurement](../measurement.md)

Checked 2026-09-06 UTC. Evidence: current official documentation, with an earlier source audit used as background. No authenticated native trial.

## Who this is for

Operators of OpenClaw assistants who want to reduce repeated source ingestion while preserving their current account, exact model, agent runtime and permissions. A provider prefix alone does not identify the runtime that owns conversation history.[34]

## Authentication and billing routes

1. Native ChatGPT/Codex login: current OpenClaw docs use canonical provider `openai` for both API-key and ChatGPT OAuth credentials. They describe `openai-codex` profile/model references as legacy. Do not apply older prefix or credential-file recipes without checking the installed version.[31][34]
2. Direct API: OpenAI Platform keys and `ANTHROPIC_API_KEY` use their own API bills. Other documented providers include Google AI Studio, xAI and approved API services. Add only the exact user's authorized account; multiple credentials in a store are not permission to pool human seats.[34]
3. Anthropic subscription reuse: OpenClaw says Anthropic staff allowed Claude CLI reuse again, while recommending API keys for production. That project statement is not blanket permission to broker Claude session tokens. Classify a CLI-owned path running the unmodified binary separately from a path that directly stores/forwards Claude.ai tokens; this review did not establish provider clearance or billing for the latter. Anthropic's published policy distinguishes native binary use from credential intermediation. For a commercial rollout, resolve the exact mechanism and terms; this guide does not approve a generic Claude subscription proxy.[31][48] A new deployment of this project-reported subscription route is not approved here until its exact mechanism and current Anthropic permission are confirmed. Otherwise use the separately authorized API/cloud alternative, without silently changing an existing account.
4. Cloud/provider-specific: current docs describe `google-vertex` with Application Default Credentials. Preserve approved cloud project, IAM identity, model and billing. They do not create new Gemini CLI or Antigravity OAuth profiles as a setup/recovery route; an existing compatible profile is not a new enrollment recipe.[34]
5. Custom provider/gateway: retain the authorized endpoint, protocol and provider-specific key. Custom Responses/Chat Completions endpoints are not automatically the native Codex runtime. OpenClaw's provider/runtime routing and model-scoped request settings can affect backend selection, so record both before making a change.[34]

For an intentionally authorized OpenAI login on current versions, the documented command is `openclaw models auth login --provider openai`. In multi-agent setups, auth mutations require an explicit `--agent` target. Obtain that existing identifier before running anything. Do not add `--set-default` while merely refreshing auth: current docs say reauthentication preserves an existing primary model unless default replacement is explicitly requested.[34][54]

Credential storage has changed across versions. Current OAuth docs describe a canonical SQLite store and retired JSON files; older instructions mentioning only `auth-profiles.json` are not safe migration guidance. Do not hand-edit token stores or run `doctor --fix` as a token-saving step. It can migrate state and needs a separate backup/approval.[31]

Subscription billing, Platform API billing and cloud billing remain separate. Do not infer dollars saved from token counts or a successful login. Verify the account's usage receipts, quota and any auxiliary model calls.

## Conservative recipe

1. Record current config scope, named agent, model, provider/runtime and auth without live inference:

   ```sh
   openclaw models status
   openclaw models list
   ```

   Target the existing agent explicitly when needed. Do not use `--probe` for a supposedly free inspection; it sends real requests.[54]
2. Merge short policy into the selected agent workspace's existing `AGENTS.md`, not an unrelated global or channel configuration. Preserve original instructions and acceptance criteria. Require exact source reads, all-record coverage where requested, deterministic all-row calculations, retained errors and verified artifacts.[63]
3. Use authorized native exec/file/service tools to retrieve and compute in batches. Retain original payloads and exact IDs, quantities, timestamps and page counts. Expose the requested result plus exceptions; a pointer does not finish the answer.
4. Keep native compaction, discovery and existing provider-specific pruning as the baseline. Do not install a new context engine or rewrite the underlying Codex thread just to reduce command output.
5. For coding, reuse installed dependencies, fix the shared cause, patch only the required change and run every mandated test. For business tasks, retain approval and exact-target readback for every external write.

## Aggressive recipe

Prefer explicit new-tool-output views and reviewed checkpoints. Keep task scope, corrected facts, permissions, approvals, coverage, failures and completed external actions protected. Restore originals on coverage mismatch, source contradiction or failing tests.

OpenClaw also has a native pruning seam, but it is route-specific. Current docs say direct Anthropic API-key requests at the first-party endpoint use server-side tool-result clearing; other eligible routes can use persisted local TTL projections. Full local storage is not full model attention.[35]

An optional config excerpt from current docs, for an isolated approved trial, is below. It merges at `agents.defaults.contextPruning` in the active `openclaw.json`. Because `defaults` can affect multiple agents, do not apply it to a shared live installation without explicit scope approval. It is not a Conservative preset and not needed for explicit observation views.[35][64]

```json
{
  "agents": {
    "defaults": {
      "contextPruning": {"mode": "cache-ttl", "ttl": "5m"}
    }
  }
}
```

The five-minute TTL does not gate the direct Anthropic server-clearing path. Which tool results can be dropped must match the task's protected evidence and the route's behavior. Do not pretend this global example is a per-session setting.[35]

## Verify and roll back

1. Authorize a small native trial using the exact agent and intended provider. `openclaw models status --probe` is documented but potentially billable and can touch multiple configured profiles; restrict a test to the exact approved provider/profile using the current command help.[54]
2. A probe is only auth/inference evidence. Test a real read fixture, an approved patch or artifact task, its complete checks, and a harmless denied action. Verify model/runtime, endpoint, all requested outputs and actual usage. Include an exception in old output and confirm restoration retrieves it.
3. Remove the added workspace policy or explicit reducer. Restore only the changed config keys from backup. Do not replace the entire shared config or credential database.
4. Pruning rollback is not simply “off.” `mode: "off"` stops new pruning, but existing client projections keep replaying, including after a gateway restart, until compaction removes those results or the session resets. Use retained originals and a verified fresh-session checkpoint to recover full evidence; do not reset production sessions casually.[35]
5. Restore the exact provider/runtime/auth selection if deliberately changed. Do not replay external actions or delete legacy credential files by hand to make state look clean.

## Limits and evidence

The current canonical OpenAI provider, credential storage and pruning behavior differ from older guides. Installed-version verification is mandatory before migration. The Anthropic reuse/terms issue remains a packaging limitation, not a claim that all native OpenClaw auth is unsupported. No full benchmark, live probe, credential migration or gateway change was performed.

## Sources

[31] https://docs.openclaw.ai/concepts/oauth — openclaw-auth
[34] https://docs.openclaw.ai/concepts/model-providers — openclaw-providers
[35] https://docs.openclaw.ai/concepts/session-pruning — openclaw-pruning
[48] https://code.claude.com/docs/en/legal-and-compliance — claude-legal
[54] https://docs.openclaw.ai/cli/models — openclaw-models
[63] https://docs.openclaw.ai/concepts/agent-workspace — openclaw-workspace
[64] https://docs.openclaw.ai/gateway/configuration — openclaw-config
