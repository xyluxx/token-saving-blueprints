# Grok Build

[Start here](../../START-HERE.md) · [Conservative](../modes/conservative.md) · [Aggressive](../modes/aggressive.md) · [Auth and billing](../auth-and-billing.md) · [Measurement](../measurement.md)

Checked 2026-09-06 UTC. Evidence: official xAI documentation and repository user guide at `72a61251fcffb464bcc687aeb5a998e5a98ec0c9`. No installed-binary or authenticated route trial.

## Who this is for

Users of the official `xai-org/grok-build` project and its `grok` terminal CLI. The repository publishes the Rust CLI/runtime, and the official xAI website links the documentation and product. This is not an unidentified package named Grokbot and not a third-party “Grok Build” download site. `grokbuild.homes` is not an authority for this guide.[28][41]

If “Grokbot” was your intended product name, first use the [identity guide](grokbot.md). Do not install Grok Build merely because the names resemble each other.

## Authentication and billing routes

1. Native account: `grok login` uses the first-party browser OAuth/OIDC flow at `auth.x.ai`. `grok login --device-auth` supports a user-owned browser authorization from another device. Session credentials are kept under the user's Grok home and refreshed natively. Do not share `auth.json` or MCP credentials.[27]
2. Subscription/trial entitlement: the official product page advertises a free trial and links to SuperGrok. This is evidence of a native account path, not an unlimited free plan or a verified entitlement for every X/SuperGrok tier. Check the actual account's Build allowance and extra-usage settings before proceeding. No fixed universal price or subscription savings is asserted.[41]
3. Direct xAI API: use your own `XAI_API_KEY` for the direct API path and its separate API bill. Important precedence: per-model `api_key`, then per-model `env_key`, then active session token, then the fallback `XAI_API_KEY`. Merely exporting `XAI_API_KEY` while logged in does not force API billing.[1][27]
4. Enterprise OIDC: the company can supply its approved issuer/client through `GROK_OIDC_ISSUER` and `GROK_OIDC_CLIENT_ID`. The pinned guide documents PKCE and default scopes `openid`, `profile`, `email`, `offline_access`, `api:access`. Consent and team restrictions remain organization-owned. Online and repository docs disagree on the OIDC TOML section, so use the common documented environment path and inspect the loaded config instead of copying an unverified stanza.[1][27]
5. External corporate auth: `[auth].auth_provider_command` is a supported command-based credential path. It must be an approved existing organization helper. Do not build a subscription broker to optimize tokens. Background refresh and interactive login have different timeout/input contracts; an unattended helper must not wait for browser input during refresh.[1][27]
6. Third-party/BYOK: per-model endpoints support a configured `api_backend` such as `responses`, `chat_completions` or `messages`. A local model, hosted API or cloud gateway needs its own credentials and protocol verification. Grok login does not confer entitlement at that endpoint. Native AWS/Azure/Google IAM integration for every custom endpoint was not established here; use the endpoint's documented auth instead of assuming cloud OAuth is interchangeable.[16]

For an intentionally chosen direct API test, merge this declaration into user-level `~/.grok/config.toml` or `$GROK_HOME/config.toml`, not project config. Inject your key privately. It creates an explicit per-model API route but leaves the default untouched:[16][27]

```toml
[model.direct_xai]
model = "grok-4.6"
base_url = "https://api.x.ai/v1"
name = "Direct xAI API"
env_key = "XAI_API_KEY"
api_backend = "responses"
```

`grok-4.6` is the official documented model at this check, not a permanent model guarantee. Choosing `direct_xai` changes billing deliberately; it is not required for either saving mode. Review the live API model availability before selecting it.[5]

Direct API price snapshot, USD per million tokens, checked 2026-09-06 UTC:[68]

| Request prompt size | Input | Cached input | Output |
| :--- | ---: | ---: | ---: |
| Below 200,000 tokens | $2.00 | $0.50 | $6.00 |
| At least 200,000 tokens | $4.00 | $1.00 | $12.00 |

The model page says the higher band applies to all tokens in a request once its prompt reaches the threshold. It lists a 500,000-token context window. The generic configuration page's example uses a different context-window value; do not copy that sample as a model capability override. These API prices are not the price of a SuperGrok subscription, and external tools can add separate charges.[68][16]

Configuration scope matters: project `.grok/config.toml` is limited to MCP, plugins and permission rules. User preferences, managed defaults and requirements are distinct layers. System `/etc/grok/requirements.toml` outranks user preferences and can pin policy.[1][16]

Grok can also discover Claude/Cursor rules, hooks and MCP configuration, so inspect inherited integrations before launching an unfamiliar repository.[17][18][19]

## Conservative recipe

1. Inspect the exact installation and discovered scope:

   ```sh
   grok --version
   grok inspect
   grok mcp list
   ```

   These commands are documented. Review every loaded rule/MCP/hook origin, selected model and auth selector. Keep the approved account, effort, permissions and endpoint unchanged.[28][16][18]
2. Merge concise original instructions into the existing project `AGENTS.md`: source-limited exact reads, complete requested coverage, deterministic all-row processing, existing code/dependencies first, minimal complete patches and all required tests. Rules load in full with no size cap, so do not copy a large handbook into every nested file.[19]
3. Use native file/search/edit tools before adding services. Keep raw command output with exit status and source version, returning exact results and relevant exceptions. A stored pointer is not a delivered answer.
4. MCP may use stdio or remote HTTP and its own OAuth. Project definitions can replace same-name user servers entirely. Authorize the exact server and its data scope; `grok mcp doctor` diagnoses connectivity but cannot establish that a remote service has the intended permissions.[18]
5. Keep approvals in place. Plan mode is not a shell security boundary. The sandbox is a separate filesystem/network control and is not something token optimization should silently disable.[1]

## Aggressive recipe

Use explicit selected observation files before context ingestion. Retain the full original, exact omitted ranges, errors and recovery path. A checkpoint before `/compact` should preserve scope, identifiers, corrections, approvals, completed actions, tests and unresolved errors. `/compact` and native auto-compaction are lossy context controls, not lossless recall.[20]

Do not install a Claude-style post-output reducer here. Grok's documented hook contract uses `PreToolUse` as the blocking event; passive-event stdout is ignored. Timeouts, malformed output and crashes are fail-open. A hook named `PostToolUse` does not establish an output-replacement seam. Use explicit CLI/MCP result views instead.[17]

## Verify and roll back

After user authorization for a small usage test, in a trusted disposable repository with no inherited write-capable integrations, use the documented restrictive headless controls:[1][4]

```sh
grok -p "Read README.md and report its title. Do not modify anything."   --permission-mode dontAsk --allow Read --allow Grep   --sandbox strict --output-format json
```

Unallowed operations are denied, not a reason to add `--always-approve`. Confirm the sandbox actually applies on the installed OS. Compare the result with the fixture, inspect model/usage/error receipts, then independently test an authorized patch and complete tests. Account billing must confirm which route paid. No such inference test was performed for this guide.

Remove only added rules, model declarations and reducer integrations. Restore backed-up settings and prior environment. Use `grok inspect` again. An auth rollback may need `grok logout` followed by the original user's native login; do not delete or hand-edit opaque token stores.[27]

Use `--resume` for existing sessions. The headless summary and sessions page disagree on `--session-id`; the latter describes it as creating a new supplied UUID. `/rewind` can modify files and truncate conversation, so back up work before using it. It cannot undo network writes or usage charges.[4][20]

## Limits and evidence

Official identity is verified; individual plan eligibility, deployed model access and exact effective pricing remain account-specific. The two documented conflicts above are not concealed by presenting a universal config. No CA installation, TLS interception, token brokerage, headless auto-approval or full model benchmark is part of this guide.

## Sources

[1] https://docs.x.ai/build/enterprise.md — grok-enterprise
[4] https://docs.x.ai/build/cli/headless-scripting.md — grok-headless
[5] https://docs.x.ai/build/overview.md — grok-overview
[16] https://docs.x.ai/build/settings.md — grok-settings
[17] https://docs.x.ai/build/features/hooks.md — grok-hooks
[18] https://docs.x.ai/build/features/mcp-servers.md — grok-mcp
[19] https://docs.x.ai/build/features/project-rules.md — grok-rules
[20] https://docs.x.ai/build/features/sessions.md — grok-sessions
[27] https://raw.githubusercontent.com/xai-org/grok-build/72a61251fcffb464bcc687aeb5a998e5a98ec0c9/crates/codegen/xai-grok-pager/docs/user-guide/02-authentication.md — grok-auth-source
[28] https://raw.githubusercontent.com/xai-org/grok-build/72a61251fcffb464bcc687aeb5a998e5a98ec0c9/README.md — grok-cli-source
[41] https://x.ai/cli — grok-site
[68] https://docs.x.ai/developers/models/grok-4.6.md — grok-model-price
