# OmniRoute authentication and account routes

[Gateway controls](omniroute.md) · [Platform coverage](../platform-coverage.md) · [Auth matrix](../../catalog/omniroute-auth.json)

Source review: 2026-09-07 UTC. Default release pin `b345c7f6cd4e1590d1177540813302375a75e332`; main snapshot `c0b2253f21c2e70c5d73581ae1be6f60a4ac5647`. Counts below belong to those snapshots.

## Authentication is not the protocol or the bill

Record six facts separately:

| Dimension | Example | What it does not establish |
|---|---|---|
| Product/runtime | Codex CLI, a native app-server, OmniRoute, IDE, SDK | The model, account or provider rights |
| Client protocol | Responses, Chat Completions, Anthropic Messages, Gemini, ACP | Whether the upstream requires an API key or OAuth |
| Authentication and credential custody | Provider API key, OAuth PKCE/device code, cloud identity, CLI-owned login, imported cookie | A paid plan, free tier or every model entitlement |
| Entitlement and billing | Included subscription usage, metered API, product credits, cloud project | Protocol compatibility or tool authority |
| Provider policy | Current first-party terms and the exact supported integration | Guaranteed technical compatibility or account health |
| Demonstrated behavior | A named version/account's authorized task and error/recovery evidence | Success on every account or universal savings |

OAuth is not the opposite of API transport. OmniRoute exposes APIs to callers and supports OAuth as well as API-key upstream connections. A restricted OmniRoute inference key can authenticate the caller while the upstream connection uses OAuth. Conversely, Qwen Coding Plan uses a subscription-specific API key, and Claude Console OAuth can select API billing.[3][5][18]

Native client login, a gateway-managed OAuth exchange, imported native credentials and browser cookies are different mechanisms. Retaining the current native client is the recommended first step, not a universal statement that all proxies are prohibited. Anthropic's current terms explicitly permit an end user to sign into the unmodified Claude Code binary under the documented conditions, while restricting third-party Claude.ai login and credential intermediation. OpenAI Codex documents OpenAI-auth proxy configuration and secure own-account cache transfer. Do not flatten these into one provider rule.[1][70]

## OmniRoute: real OAuth capability, separate adoption decisions

Snapshot: default release `b345c7f6cd4e1590d1177540813302375a75e332`. All rows below are documented/source-inspected only; no account was authenticated or benchmarked for this repository. There are 24 OAuth-category entries in this release. The generated reference on main lists 25 including Raycast, which is absent from this default release. Neither category count is a count of working accounts or independent OAuth implementations.

| Provider IDs | Technical mechanism | Runtime/interface | Provider policy and account boundary |
|---|---|---|---|
| `claude` | Gateway PKCE code exchange; access/refresh tokens mapped into connection | Direct gateway credential custody, not Claude CLI process | Do not offer as an approved deployment under current Anthropic restrictions without provider agreement; native unmodified CLI is a different path. Subscription/extra usage not tested.[97] |
| `codex` | Gateway PKCE browser login; separate device/import paths exist | Direct Codex OAuth-backed API connection | OpenAI docs describe OpenAI-auth proxies; generic terms and intended use still govern. No blanket ban or universal gateway approval inferred. Eligible ChatGPT/Codex account and actual quota/billing untested.[100] |
| `xai-oauth` | PKCE code exchange, gateway refresh token custody | api.x.ai via XaiExecutor | Project-supported transport. Exact third-party permission and account feature scope not established. Not the Grok Build JWT or an API-key invoice by assumption.[110] |
| `grok-cli` | Device flow plus browser PKCE; native auth JSON/JWT import also implemented | Grok Build proxy endpoint via gateway executor, not the native CLI process | Project-supported gateway. Keep product-specific policy unresolved; imported access token alone may lack refresh. Build entitlement, plan and extra usage untested.[105] |
| `github, ghe-copilot` | Device-code OAuth; GHE requires its instance URL | GitHub/GHE entitlement and Copilot token exchange | Organization policy and exact permitted integration must be checked; not automatically the same as GitHub native CLI. Not all GitHub accounts have Copilot entitlement.[102][103] |
| `gitlab-duo` | Registered OAuth app/client required; authorization flow | GitLab Duo endpoint; scopes ai_features/read_user | App registration, scopes and deployment policy required; no working default client asserted. GitLab Duo entitlement untested.[104] |
| `antigravity, agy` | Google authorization-code flow; agy login import also offered | Antigravity backend/project routes | Not Gemini CLI consumer entitlement. Exact provider permission/client scopes must be established; no generic Google OAuth interchangeability. Google account/organization eligibility untested.[94][96] |
| `kiro, amazon-q` | Builder ID/device and provider-specific imported-token paths | Related AWS auth handler, separately identified connections | OmniRoute labels Kiro third-party use prohibited. Current AWS service terms were inspected but that precise blanket sentence was not recovered; retain attributed warning/unresolved provider check, not an invented legal ruling. No credit-to-token conversion accepted; account and terms untested.[95] |
| `qoder` | Authorization-code flow | Qoder service | Project-supported technical connection, provider permission unresolved. Plan/quota untested.[109] |
| `cursor` | Provider-specific login/import service | Cursor-backed request path | Not Cursor BYOK and not blanket permission to export native credentials; gateway policy unresolved. Cursor plan/credit billing untested.[101] |
| `zed` | Import-token handler, OS keychain/manual API-key import | Underlying provider credentials | No standard browser OAuth for this entry; do not relabel imported provider keys as Zed subscription entitlement. Underlying provider invoices apply as configured, not tested.[84] |
| `zed-hosted` | Native-app sign-in with one-time RSA challenge | Zed hosted model aggregator | Distinct technical integration from zed import; provider agreement/plan unresolved. Zed hosted allowance untested.[111] |
| `trae` | Import-token handler; browser-assisted capture also advertised | Trae SOLO/cloud JWT with identity metadata | No generic headless refresh guarantee for pasted tokens; provider policy unresolved. Plan and expiry behavior untested.[85] |
| `kimi-coding` | Device-code OAuth with device identity | Kimi Coding Plan endpoint | Technical implementation exists; confirm actual plan and supported third-party use. Not ordinary Moonshot API billing by assumption.[107] |
| `kilocode` | Gateway/account OAuth and optional anonymous fallback in metadata | Kilo provider | Do not equate metadata anonymous fallback with authenticated paid entitlement or approved zero-cost mode. Kilo/account/provider charges untested.[106] |
| `cline, clinepass` | WorkOS OAuth handler reused by two catalog entries | Cline credits versus ClinePass model catalog | Separate entitlement despite same login flow; direct API-key support also advertised for ClinePass. No current universal price/catalog claim adopted.[98] |
| `devin-desktop, devin-cli` | OAuth registry actually selects import_token; browser login disabled there | Existing Devin token; CLI executor additionally needs native binary | Do not advertise generic Sign in with OAuth for these entries; native CLI login and gateway token import are separate paths. Account/CLI path untested.[86] |
| `codebuddy-cn` | Device-code flow; API-key option also documented | Tencent CodeBuddy CN | Provider-specific integration, not interchangeable with other coding plans. Account/model eligibility untested.[99] |
| `openference` | Account OAuth | api.openference.com | Provider-specific connection; successful OAuth is not sufficient for inference. Gateway warns an active plan is required and missing plan can return 402.[108] |

The matrix distinguishes literal handlers from labels: Zed and Devin import-token handlers explicitly reject generic browser authorization, and Trae's imported JWT path does not establish native OAuth refresh parity.[82][84][85]

Additional CLI-owned paths: OmniRoute describes `codex-app-server`, `auggie`, `devin-cli-agentic` and `zcode` as not storing a provider API key in OmniRoute. They still require the actual CLI/runtime and upstream sign-in. This “No-auth” category means no gateway-owned upstream credential for those entries, not anonymous inference.[18]

The Codex app-server adapter is materially different from `codex` OAuth. It uses a real app-server, creates threads and forwards the requested model/effort. Harness tools are relayed back to the outer host; its own sandbox and approval rules remain another boundary. Test those semantics before treating it as equivalent to a native thread.[29]

Qwen Code's discontinued OAuth/free tier is not offered as a new path. Qwen Web cookies, Alibaba Coding Plan keys and standard/token-plan APIs are separate products and contracts. `grok-cli` and `xai-oauth` similarly do not share interchangeable sessions or billing.[5][18]

## Practical paths for both modes

### Path 1: existing supported native login

1. Keep the original native CLI/IDE/account/model/effort and permissions.
2. Conservative: exact retrieval, complete code calculations, native patching, valid artifact reuse and full acceptance checks. No gateway is needed.
3. Aggressive: additionally use that runtime's supported selective observations or checkpoint/compaction with retained originals and explicit consent.
4. Native/headless delegates may use the existing CLI-owned login where documented. Record actual worker model, effort and usage. An SDK or command flag does not automatically change billing.

### Path 2: already approved gateway OAuth upstream

1. Confirm that the selected provider row is a supported, permitted mechanism for the operator's use. “Project supports OAuth” is not the provider's permission or the user's entitlement.
2. Keep upstream account, resolved model and effort fixed. Use the gateway's own provider flow when appropriate; do not paste an unrelated token into an API-key field. Login may require browser/device consent and can have account/traffic side effects, so it needs its own approval.
3. Record credential/refresh custody, exact inbound and upstream protocols, quota/billing, source-data permission and rollback. Use a restricted inference key for callers, not a management credential.
4. Establish route-only baseline with optional compression and answer cache off, plus the separately documented adaptive/context-edit/MCP gates. Authorize and test the smallest meaningful request, tools, failures and recovery before claiming compatibility. Check actual attempts, not only final output.
5. Conservative can keep this same approved OAuth route and apply exact task preparation. Its narrow structured-data candidate requires validated values, complete coverage, raw retention and tokenizer checks.
6. Aggressive can keep the same route and add one eligible lossy observation method, with protected state and recovery. Do not enable every gateway preset or weaken account/model controls to make a trial pass.

This path is conditional on provider-specific permission. It is not offered for direct Claude.ai credential intermediation contrary to the current Anthropic conditions. The native unmodified Claude CLI path remains separate.[1]

### Path 3: CLI-owned bridge or separate headless runtime

1. Use an existing authorized native runtime and its own sign-in. No extra graphical window is required for documented headless use, but the process/service must really exist.
2. For OmniRoute's Codex app-server path, validate the bridge URL/access control, source/workspace permissions, tool passthrough, actual model/effort and bridge approval/sandbox policy. Do not reuse direct `codex` token configuration as if it were this path.
3. Apply Conservative or Aggressive methods to the supported tool/context surface without assuming preservation of opaque native history. Count startup/context rebuilding, helper and verification work.
4. If the bridge changes required semantics, retain the direct native CLI instead of forcing generic protocol translation.

The inspected Codex bridge is a technical option, not an authenticated parity result.[29]

### Path 4: approved API-key/cloud/local route

Retain the exact provider account/project/region/model and its protocol. Existing direct API helpers are often simpler than a gateway. A cheaper worker or a free API tier is an optional cost/quality decision for either mode, not automatic token reduction. Validate free-tier hard stops, automatic paid upgrade/reload, missing prices and failure paths without pooling accounts.

## Billing and economics wording

The current Claude support notice says the announced separate-credit change is paused: Claude Agent SDK, `claude -p`, and third-party app usage still draw from subscription usage limits. Historical credit tables lower on that page are not current pricing. This billing statement does not override the separate legal conditions for a specific integration.[1][2]

Report four outcomes separately: total task tokens with cache semantics, actual variable charges, observable subscription capacity/overage effects, and accepted task quality/latency. Include parent and workers, retries, restoration, cache churn, final verification and local compute. Missing usage or price is unknown, not zero.

There is no measured combined saving for these blueprints plus delegation or OmniRoute. Published payload rates cannot be added or multiplied into a promised stack average. For a fixed subscription, fewer tokens do not reduce the monthly fee; they may preserve useful capacity or avoid separately charged usage. A cheaper model changes economics but may consume more tokens or require more repair.

Use the same task and acceptance criteria with one changed factor. If a future scenario is useful, label every workload share, unit price, cache assumption and helper/retry assumption; calculate it reproducibly and never present it as a measured result. No such new scenario is needed for this factual revision.

## Sources

[1] https://code.claude.com/docs/en/legal-and-compliance.md
[2] https://support.claude.com/en/articles/15036540-use-the-claude-agent-sdk-with-your-claude-plan
[3] https://code.claude.com/docs/en/authentication.md
[5] https://raw.githubusercontent.com/QwenLM/qwen-code/main/docs/users/configuration/auth.md
[18] https://raw.githubusercontent.com/diegosouzapw/OmniRoute/main/docs/reference/PROVIDER_REFERENCE.md
[29] https://raw.githubusercontent.com/diegosouzapw/OmniRoute/main/open-sse/executors/codex-app-server.ts
[70] https://developers.openai.com/codex/auth
[82] https://github.com/diegosouzapw/OmniRoute/blob/b345c7f6cd4e1590d1177540813302375a75e332/src/lib/oauth/providers.ts
[84] https://github.com/diegosouzapw/OmniRoute/blob/b345c7f6cd4e1590d1177540813302375a75e332/src/lib/oauth/providers/zed.ts
[85] https://github.com/diegosouzapw/OmniRoute/blob/b345c7f6cd4e1590d1177540813302375a75e332/src/lib/oauth/providers/trae.ts
[86] https://github.com/diegosouzapw/OmniRoute/blob/b345c7f6cd4e1590d1177540813302375a75e332/src/lib/oauth/providers/devin-desktop.ts
[94] https://github.com/diegosouzapw/OmniRoute/blob/b345c7f6cd4e1590d1177540813302375a75e332/src/lib/oauth/providers/agy.ts
[95] https://github.com/diegosouzapw/OmniRoute/blob/b345c7f6cd4e1590d1177540813302375a75e332/src/lib/oauth/providers/kiro.ts
[96] https://github.com/diegosouzapw/OmniRoute/blob/b345c7f6cd4e1590d1177540813302375a75e332/src/lib/oauth/providers/antigravity.ts
[97] https://github.com/diegosouzapw/OmniRoute/blob/b345c7f6cd4e1590d1177540813302375a75e332/src/lib/oauth/providers/claude.ts
[98] https://github.com/diegosouzapw/OmniRoute/blob/b345c7f6cd4e1590d1177540813302375a75e332/src/lib/oauth/providers/cline.ts
[99] https://github.com/diegosouzapw/OmniRoute/blob/b345c7f6cd4e1590d1177540813302375a75e332/src/lib/oauth/providers/codebuddy-cn.ts
[100] https://github.com/diegosouzapw/OmniRoute/blob/b345c7f6cd4e1590d1177540813302375a75e332/src/lib/oauth/providers/codex.ts
[101] https://github.com/diegosouzapw/OmniRoute/blob/b345c7f6cd4e1590d1177540813302375a75e332/src/lib/oauth/providers/cursor.ts
[102] https://github.com/diegosouzapw/OmniRoute/blob/b345c7f6cd4e1590d1177540813302375a75e332/src/lib/oauth/providers/ghe-copilot.ts
[103] https://github.com/diegosouzapw/OmniRoute/blob/b345c7f6cd4e1590d1177540813302375a75e332/src/lib/oauth/providers/github.ts
[104] https://github.com/diegosouzapw/OmniRoute/blob/b345c7f6cd4e1590d1177540813302375a75e332/src/lib/oauth/providers/gitlab-duo.ts
[105] https://github.com/diegosouzapw/OmniRoute/blob/b345c7f6cd4e1590d1177540813302375a75e332/src/lib/oauth/providers/grok-cli.ts
[106] https://github.com/diegosouzapw/OmniRoute/blob/b345c7f6cd4e1590d1177540813302375a75e332/src/lib/oauth/providers/kilocode.ts
[107] https://github.com/diegosouzapw/OmniRoute/blob/b345c7f6cd4e1590d1177540813302375a75e332/src/lib/oauth/providers/kimi-coding.ts
[108] https://github.com/diegosouzapw/OmniRoute/blob/b345c7f6cd4e1590d1177540813302375a75e332/src/lib/oauth/providers/openference.ts
[109] https://github.com/diegosouzapw/OmniRoute/blob/b345c7f6cd4e1590d1177540813302375a75e332/src/lib/oauth/providers/qoder.ts
[110] https://github.com/diegosouzapw/OmniRoute/blob/b345c7f6cd4e1590d1177540813302375a75e332/src/lib/oauth/providers/xai-oauth.ts
[111] https://github.com/diegosouzapw/OmniRoute/blob/b345c7f6cd4e1590d1177540813302375a75e332/src/lib/oauth/providers/zed-hosted.ts
