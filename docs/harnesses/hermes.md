# Hermes Agent

[Start here](../../START-HERE.md) · [Conservative](../modes/conservative.md) · [Aggressive](../modes/aggressive.md) · [Auth and billing](../auth-and-billing.md) · [Measurement](../measurement.md)

Checked 2026-09-06 UTC. Evidence: official documentation and installed CLI help. No authenticated provider trial or model benchmark for this guide.

## Who this is for

People using Nous Research's Hermes Agent in the CLI or a persistent assistant workflow. Start with the existing tools, selective skill loading and project policy. A local observation workflow does not require changing the model provider or running a subscription proxy.

## Authentication and billing routes

1. Native documented subscription routes: use `hermes model` and the provider's own login. Nous Portal and “ChatGPT or Codex Subscription” are documented choices. The user authorizes their own account and Hermes maintains its provider credentials; no token copying or seat pooling is required.[29]
2. Other provider OAuth: Hermes documents MiniMax, Copilot and xAI choices. The xAI `xai-oauth` provider is separate from API-key `xai`; its guide says `XAI_API_KEY` is not used for the OAuth provider. Subscription consumption across chat/media features must be verified, not inferred from the X Search quota statement alone.[29][65]
3. Anthropic: direct `ANTHROPIC_API_KEY` is the straightforward API route. Current Hermes documentation describes Claude Max OAuth with purchased extra-usage credits, not included base Max allowance, and says Pro is unavailable through that path. This is not identical to native Claude Code subscription billing. Provider terms and the actual account bill still govern; do not turn this into a commercial subscription broker.[29][48] For a new setup, this project-reported subscription route is not approved here until its exact mechanism and current Anthropic permission are confirmed. Otherwise use a separately authorized API/cloud route; do not silently change an existing account.
4. Qwen warning: Hermes still lists `qwen-oauth`, but Qwen's own current auth documentation says its free tier was discontinued. Do not approve a new free-Qwen setup solely because a provider appears in a picker. Use a supported Alibaba/API plan after explicit account and billing approval.[29][56]
5. Direct keys: the documented provider picker supports OpenAI API (`openai-api`), Anthropic, Gemini, xAI, Alibaba and others. Put the selected provider's key in the active Hermes home's private `.env` or approved secret source, not a project instruction file. Provider identity is explicit; an OpenAI API key is not a Codex subscription token.[29]
6. Cloud: Bedrock uses the AWS credential chain, Vertex uses service-account/ADC authorization and GCP billing, and Azure Foundry uses the approved endpoint and credentials. Keep region, deployment/model, account and IAM scope fixed. These are separate from consumer subscriptions.[29]
7. Gateway/local: choose an approved provider such as OpenRouter, or a documented custom/local endpoint. The endpoint and protocol must support tools, streaming, reasoning/compaction items and usage. A name-compatible model is not feature equivalence. Do not add a proxy, pooled credential rotation or fallback to obtain “savings.”[29]

Provider setup through `hermes model` changes saved defaults; session model switching is a different operation. Resolve the active profile/home before any edit. Record CLI overrides, provider-specific variables, configured base URL, credential source and fallback chain without printing secrets. Inspect auxiliary models for compression, vision and other tools as well as the primary model; those calls can have separate costs.[29][43]

## Conservative recipe

1. Review the installed command surface and current session state:

   ```sh
   hermes chat --help
   hermes auth --help
   ```

   In the running session, `/model`, `/tools` and `/usage` inspect the selected route, available tools and usage. Do not select a different provider while checking.[53]
2. Merge an original, short policy into the existing project `AGENTS.md` or the already selected Hermes context file. Keep global identity and other projects untouched. Require exact source lookup, full reading when requested, all-row deterministic processing, full semantic coverage where required, minimal complete patches and all required tests.[62]
3. For repeated web/file/data operations, use native code execution when it is actually exposed. Keep full sources in the authorized workspace and return computed results, exceptions, counts and the requested artifact. The supported RPC tool allowlist is narrower than all tools: MCP calls, delegation and arbitrary credential extraction are not a code-execution bridge.[44]
4. Keep native tool discovery and relevant skills. Do not load every tool/schema or every skill for each request. Required approval and recovery tools must remain discoverable. Keep prompt/cache prefixes stable during the task.
5. Use native patching and available diagnostics, while still running the project's actual build, regression and integration tests. Diagnostics alone are not end-to-end behavior verification.

## Aggressive recipe

Use supported new-observation views rather than historical message rewrites. Retain full source/version/permissions and make omissions visible. If counts disagree, sources conflict, tests fail or the requested evidence is absent, restore the needed original observations immediately. Model confidence is not a recovery detector.

Before invoking native `/compress`, save and verify a checkpoint of task scope, exact facts, corrections, approvals, side effects, coverage, tests and unfinished work. Native archive/recovery and provider-specific compaction are useful but lossy in model attention. Do not replace opaque provider reasoning/continuation items or claim a context-engine plugin is installed merely because its API exists.[43][53]

Do not change the compression model, reasoning effort, tool backend, auth, fallback behavior or permissions as a default extension. Any extra summarizer or compressor call must be counted alongside restored reads.

## Verify and roll back

After authorizing a small usage trial, use a trusted disposable project and the currently selected route. The installed CLI help verifies this headless shape:

```sh
hermes chat --oneshot -q "Read README.md and report its title. Do not edit files or use external services."
```

Review inherited hooks, MCP access and the configured terminal backend first. A prompt restriction is advisory; native approvals and sandboxing must remain effective. Verify the exact file result, provider/model and real usage receipt, then perform an approved patch plus complete tests and a denied harmless-action fixture. Do not add `--yolo` or auto-accept hooks to make the smoke test succeed.

Rollback is removal of the added project paragraph or observation view. Restore only affected settings in the exact active profile using supported config tooling. If native compaction lost a fact, retrieve the original source and resume from a verified checkpoint instead of editing the session database. Never replay earlier service writes to reconstruct output.

If an optional route trial changed the saved provider/model, return to the precise prior choice through `hermes model` and verify it in a new session. Do not alter other profiles or a shared gateway's settings. Auth refresh and credentials stay owned by the user's original provider integration.[29]

## Limits and evidence

The prior source audit and current official docs establish useful native interfaces, not universal authenticated compatibility. Documentation itself leaves some subscription quota semantics unspecified. The presence of Qwen OAuth is specifically not accepted as current free entitlement. No live accounts, global configuration, gateway or model selection were changed in this research.

## Sources

[29] https://hermes-agent.nousresearch.com/docs/integrations/providers — hermes-provider
[43] https://hermes-agent.nousresearch.com/docs/developer-guide/context-compression-and-caching — hermes-compression
[44] https://hermes-agent.nousresearch.com/docs/user-guide/features/code-execution — hermes-execution
[48] https://code.claude.com/docs/en/legal-and-compliance — claude-legal
[53] https://hermes-agent.nousresearch.com/docs/user-guide/cli — hermes-cli
[56] https://raw.githubusercontent.com/QwenLM/qwen-code/92a8a8d17957b800548d6aaca7feb2916fbe6593/docs/users/configuration/auth.md — qwen-auth-pinned
[62] https://hermes-agent.nousresearch.com/docs/user-guide/features/context-files — hermes-context-files
[65] https://hermes-agent.nousresearch.com/docs/guides/xai-grok-oauth — hermes-xai
