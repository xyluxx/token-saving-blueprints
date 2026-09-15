# Qwen Code

[Start here](../../START-HERE.md) · [Conservative](../modes/conservative.md) · [Aggressive](../modes/aggressive.md) · [Auth and billing](../auth-and-billing.md) · [Measurement](../measurement.md)

Checked 2026-09-06 UTC. Evidence: official documentation, including repository docs pinned at `92a8a8d17957b800548d6aaca7feb2916fbe6593`. No authenticated native trial.

## Who this is for

Users of the `QwenLM/qwen-code` terminal harness. The harness is not a particular Qwen model and is not a free inference entitlement. Current authentication differs materially from older tutorials.[56]

## Authentication and billing routes

Start `qwen`, then use `/auth`. Current choices are Alibaba ModelStudio, Third-party Providers, and Custom Provider. After setup, `/model` shows configured choices and `/doctor` checks the current setup. Do not use the removed standalone `qwen auth`, including `qwen auth status` or `qwen auth coding-plan`.[56]

1. Old native OAuth: the official docs say the Qwen OAuth free tier ended 2026-04-15 and is no longer selectable. Cached-token code or an old “free daily requests” guide is not a supported new setup. Do not promise a current free OAuth route or try to revive somebody else's cache.[56]
2. Coding Plan subscription: `/auth` → Alibaba ModelStudio → Coding Plan → your account's region → your own plan key. This is a subscription-specific API key and dedicated endpoint, not the retired browser OAuth and not a standard DashScope key. Billing is fixed-plan quota subject to current regional terms.[56]
3. Token Plan: `/auth` → Alibaba ModelStudio → Token Plan → Beijing or Singapore → your key → explicitly select offered model IDs. This is usage-based token billing on a dedicated endpoint, not Coding Plan. The endpoint's available models must be selected, not guessed from a blog.[56]
4. Standard API: select Standard API Key under ModelStudio, or use a supported direct provider. Standard DashScope has its own endpoint and usage-based bill. OpenAI-compatible, Anthropic and Google GenAI protocols use separate provider entries and keys.[56]
5. Cloud: Vertex AI supports a Google key or authorized ADC/project setup with the Gemini protocol. Explicitly select `vertex-ai` through the documented auth setting or `--auth-type vertex-ai`, especially for keyless ADC; published and repository docs differ on environment auto-detection. Azure OpenAI is documented under compatible providers, but requires the deployment's actual endpoint/protocol and credentials, not just any OpenAI key.[7][56]
6. Third-party/custom: the menu includes services such as Grok, DeepSeek, OpenRouter and Requesty. These are their own API billing routes. Custom Provider can connect approved local/proxy services, but ChatGPT, Claude and Google consumer subscriptions are not generic keys for it. Validate streaming, tools, reasoning, error handling and usage per endpoint.[56]

Endpoint distinctions, verified in the pinned official auth guide:[56]

| Route | Beijing | International |
| :--- | :--- | :--- |
| Coding Plan | `https://coding.dashscope.aliyuncs.com/v1` | `https://coding-intl.dashscope.aliyuncs.com/v1` |
| Token Plan | `https://token-plan.cn-beijing.maas.aliyuncs.com/compatible-mode/v1` | `https://token-plan.ap-southeast-1.maas.aliyuncs.com/compatible-mode/v1` |

For a deliberately selected Beijing Coding Plan account, merge this example into `~/.qwen/settings.json`, preserving other entries. Supply `BAILIAN_CODING_PLAN_API_KEY` separately through a private environment/secret store. The model is a documentation example, not an instruction to change your existing model.[56]

```json
{
  "modelProviders": {
    "openai": [{
      "id": "qwen3-coder-plus",
      "baseUrl": "https://coding.dashscope.aliyuncs.com/v1",
      "envKey": "BAILIAN_CODING_PLAN_API_KEY"
    }]
  },
  "security": {"auth": {"selectedType": "openai"}},
  "model": {"name": "qwen3-coder-plus"}
}
```

For Token Plan, use its region-specific endpoint, a model actually offered during setup and `BAILIAN_TOKEN_PLAN_API_KEY` as the bound `envKey`. That provider-specific variable alone does not select the auth type. The explicit binding avoids the unreliable assumption that setting a key variable configures the whole route.[56]

Conflicts: CLI credential arguments outrank shell environment, then the first discovered `.env`, then `settings.json`'s `env` fallback. `.env` files are not merged. User-scope `modelProviders` is recommended to avoid project/user merge conflicts. Never place real keys in a shared settings file; do not pass secrets on the command line. `/model` selections persist across sessions.[56]

## Conservative recipe

1. Inspect `/doctor`, `/model`, project rules and active MCP tools. Record the exact provider, region, model, effort and permissions; do not change them for token savings.
2. Merge a short work policy into the project's existing `QWEN.md` context file: locate exact files first, respect full-reading requests, retain complete raw data for bulk computations, reuse code/dependencies, patch the complete requested change, and run every required check. Confirm the context filename has not been customized.[8]
3. Use native file/search/edit tools. For all-row calculations, run deterministic code over every row, retaining counts and exceptions. For all-record semantic review, expose every relevant substantive record in bounded batches.
4. Keep only relevant authorized MCP servers. Qwen supports MCP, but server credentials and permissions are separate from inference auth. Do not enable deprecated `tools.core` or `tools.allowed` settings as a universal safety preset; the current settings docs prefer native permissions.[8][60]
5. Use native context management as the baseline. Do not add prompt hooks that call another model to every step; their calls and latency are not free.[39]

## Aggressive recipe

Produce explicit observation views with raw-source locations and coverage first. For long sessions, create a reviewed checkpoint that preserves exact identifiers, corrections, approvals, completed actions, test failures and unfinished work; then use the documented `/compress` command if accepting lossy context. `/summary` exports a summary; `/compress` replaces chat history. `/compress-fast` strips old tool/thinking content and is not the Conservative default.[57]

Qwen's documented `PreToolUse` supports `updatedInput`, while `PostToolUse` describes decisions and additional context, not Claude's generic `updatedToolOutput`. Adding context does not remove the original payload. Therefore this guide uses explicit tool outputs and native compaction, not an invented transparent post-hook reducer.[39]

## Verify and roll back

After authorized setup, check `/doctor` and `/model`, then run a small fixture through the actual chosen route. The documented headless shape is:[40]

```sh
qwen -p "Read README.md and report its title. Do not edit files or use external services." --approval-mode plan --output-format json
```

Use only in a trusted disposable project with reviewed hooks, MCP permissions and sandbox. Plan mode is not a complete security sandbox. The test consumes actual quota or API usage. Confirm the title, provider/model, quota/billing destination and error state. A second approved patch/test fixture must retain a planted exception and pass the full required checks.

Headless `ask` hook decisions fall back to denial when no confirmation UI exists. Budget flags such as `--max-wall-time` and `--max-tool-calls` are documented, but choose limits for the task and report budget exhaustion as partial, not success. Do not copy an auto-edit or yolo example to avoid an approval failure.[39][40]

Rollback: restore only the edited provider/model/auth keys and original project policy. Restore previous process variables and the relevant `.env` source. Reopen Qwen and confirm `/doctor` and `/model` match the prior route. Recover needed source passages from retained originals after compaction; `/restore` concerns project-file checkpoints, not reversal of API charges or external writes.[56][57]

## Limits and evidence

The website auth page still contains historical OAuth explanatory text, and lags the repository's full Token Plan section. The discontinuation warning and current three-choice menu govern new setup. No new OAuth/free quota or universal Coding Plan price is promised. Models and regional quotas must be checked in the user's own account. No model-quality or savings benchmark was run.

## Sources

[7] https://raw.githubusercontent.com/QwenLM/qwen-code/main/docs/users/configuration/auth.md — qwen-auth
[8] https://raw.githubusercontent.com/QwenLM/qwen-code/main/docs/users/configuration/settings.md — qwen-settings
[39] https://raw.githubusercontent.com/QwenLM/qwen-code/92a8a8d17957b800548d6aaca7feb2916fbe6593/docs/users/features/hooks.md — qwen-hooks
[40] https://raw.githubusercontent.com/QwenLM/qwen-code/92a8a8d17957b800548d6aaca7feb2916fbe6593/docs/users/features/headless.md — qwen-headless
[56] https://raw.githubusercontent.com/QwenLM/qwen-code/92a8a8d17957b800548d6aaca7feb2916fbe6593/docs/users/configuration/auth.md — qwen-auth-pinned
[57] https://raw.githubusercontent.com/QwenLM/qwen-code/92a8a8d17957b800548d6aaca7feb2916fbe6593/docs/users/features/commands.md — qwen-commands
[60] https://raw.githubusercontent.com/QwenLM/qwen-code/92a8a8d17957b800548d6aaca7feb2916fbe6593/docs/users/features/mcp.md — qwen-mcp-features
