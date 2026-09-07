# Gemini CLI

[Start here](../../START-HERE.md) · [Conservative](../modes/conservative.md) · [Aggressive](../modes/aggressive.md) · [Auth and billing](../auth-and-billing.md) · [Measurement](../measurement.md)

Checked 2026-09-06 UTC. Evidence: official documentation and migration notice. No authenticated native trial.

## Who this is for

Existing Gemini CLI users, especially Gemini Code Assist Standard/Enterprise and paid API/cloud customers. Identify the current product before applying an old free-tier setup guide.

Google's official transition notice says Gemini CLI stopped serving Google AI Pro/Ultra and free Code Assist for individuals on June 18, 2026. Standard/Enterprise access remains supported, along with the paid API paths described in the notice. The authentication page still explains historical individual Google sign-in, but also carries the migration warning. That older explanation is not a promise of present individual entitlement.[33][42]

## Authentication and billing routes

1. Supported native Google account route: start `gemini`, choose Sign in with Google, and use your own eligible organization account/project. Confirm the assigned Code Assist license and required service/project access. Do not transfer a consumer Google login to another CLI as a generic subscription credential.[33][42]
2. Individual subscription/free route: follow Google's official Antigravity migration guidance if that is your account type. This guide does not silently rename a Gemini binary or apply Gemini hooks to Antigravity.[42]
3. Direct Gemini API: select Use Gemini API Key and supply your own `GEMINI_API_KEY` securely. API usage has its own billing/quotas; a Google AI subscription is not an API key.[33]
4. Vertex AI / Google cloud: select Vertex AI with the approved project/location and either ADC, a narrowly scoped service-account credential, or a Google Cloud API key. For ADC, the docs explicitly require removing conflicting `GOOGLE_API_KEY` and `GEMINI_API_KEY` from that process. `GOOGLE_APPLICATION_CREDENTIALS` selects a credential file; do not point it at another person's downloaded key.[33]
5. Third-party gateway: no generic OpenAI-compatible endpoint recipe is established by Gemini CLI's documented auth choices. Preserve the supported Google protocol/cloud route. Any organization-specific gateway needs its own tested connector, data policy and auth documentation; do not invent an `OPENAI_BASE_URL` substitution or proxy consumer OAuth.[33]

For an intentionally selected Vertex ADC route, the official setup includes `gcloud auth application-default login`, project configuration, starting `gemini` and selecting Vertex AI. That login writes credentials and must be performed by the user only for this exact account. Existing managed/cloud identity should not be replaced just to optimize token usage.[33]

Before setup, inspect shell variables, project/user environment files, the saved auth selection and organization's policy. Record the active route, project, model and effort. Account sign-in, model choice and the payer are different facts. Do not disclose credential values in an inspection transcript.

## Conservative recipe

1. Confirm the installed CLI and flags without invoking a model:

   ```sh
   gemini --version
   gemini --help
   ```

   Use the auth menu to verify the supported route before trying an old subscription login.[33][49]
2. Merge a concise task policy into the existing project-root `GEMINI.md`, or the configured context filename if customized. Require exact file/symbol discovery, complete requested reading, deterministic all-row computation, reuse of existing dependencies, native edits and the full project's test obligations. Review enabled extensions, hooks and MCP servers instead of globally removing safeguards.[67]
3. Use native file/search tools and permissioned shell work. Retain full sources and errors; return exact computation results with record counts. A summary is not every-record semantic review.
4. Keep native caching and compaction as the baseline. Load only relevant service tools through the current supported MCP mechanism. Each service owns its own auth and data scope; model login is not permission to write into those services.[37]
5. Test the same complete task before and after adding the policy. Preserve model, effort, permissions and output requirements. Less prose after generation is not a refund of generated tokens.

## Aggressive recipe

Use explicit observation projections as the first extension: save the original output, then expose task-relevant fields/spans with omissions and restoration locations. Store protected task state before a native new-session handoff or existing compaction workflow. Do not hand-edit persisted model reasoning/history.

Gemini's current hooks differ from Claude's: `BeforeTool` can merge rewritten arguments; `AfterTool` can deny/hide the original with replacement feedback or request a tail tool whose result replaces the original. `additionalContext` appends rather than compresses. A tail tool is another operation, whose permissions, cost, errors and side effects must be counted. These are optional documented seams, not a tested reducer installed by this guide.[37]

`AfterModel` processes generated content, so output trimming there cannot reduce already-generated tokens. Do not use it to claim generation savings. Do not use automatic model/effort downgrade as part of this mode.[37]

## Verify and roll back

After permission for a small usage test, in a trusted disposable repository, run the documented headless shape with the existing route:[49]

```sh
gemini -p "Read README.md and identify its title. Do not edit files or use external services." --output-format json
```

Keep native approval/sandbox controls and audit inherited MCP write access first. Headless execution is not a permission bypass; an operation that needs interactive approval may fail. Compare the actual title with the source, inspect the selected auth/model and provider usage, then exercise a separately approved patch/test fixture. Confirm a planted exception and a denied harmless action are handled correctly. A valid cached login alone proves none of these outcomes.

Remove only added policy text and experimental hook entries. Restore the exact prior settings, environment and auth selection; restart the session to clear run-scoped changes. Restore omitted evidence from raw sources or a reviewed checkpoint. Do not revoke shared organization credentials or delete all Google auth state to undo a tool-output experiment.

If the failure is the announced individual entitlement migration, do not switch to a billable API key without consent. Report the product/account boundary and use the official migration path instead.[42]

## Limits and evidence

The transition notice is more specific than generic account examples still on the auth page. Eligibility and model availability remain account-specific. This guide does not assert equivalent hooks, costs or context handling in Antigravity. No authenticated Gemini/Vertex trial or comparative quality/token benchmark was performed.

## Sources

[33] https://geminicli.com/docs/get-started/authentication — gemini-auth
[37] https://geminicli.com/docs/hooks/reference — gemini-hooks
[42] https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli — gemini-transition
[49] https://geminicli.com/docs/cli/cli-reference — gemini-cli
[67] https://geminicli.com/docs/cli/gemini-md — gemini-context
