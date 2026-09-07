# Claude Code

[Start here](../../START-HERE.md) · [Conservative](../modes/conservative.md) · [Aggressive](../modes/aggressive.md) · [Auth and billing](../auth-and-billing.md) · [Measurement](../measurement.md)

Checked 2026-09-07 UTC. Evidence: documented; installed CLI help also inspected. No authenticated native trial or savings benchmark.

## Who this is for

People using Anthropic's Claude Code who want less unnecessary reading and regeneration without giving up their current Claude model, effort, subscription, cloud account, or approvals. Begin with project instructions and native tools, not a proxy.

## Authentication and billing routes

1. Native subscription: launch `claude`, then complete the first-party browser login with your own Claude.ai account. Pro, Max, Team and Enterprise are documented routes, subject to the seat's entitlement. Use `/login` to choose the intended account. Do not copy another person's credential store.[11]
2. Direct API billing: supply your own `ANTHROPIC_API_KEY` through a private process environment or the organization's approved secret manager. On first launch it takes the API-key route instead of the browser prompt. Console browser sign-in is also API-based billing, not a Pro/Max allowance. Keyless Console OAuth is documented from v2.1.242; an older installed binary must not be assumed to offer it.[11]
3. Cloud: keep the approved Amazon Bedrock, Claude Platform on AWS, Google Cloud Agent Platform (formerly Vertex AI), or Microsoft Foundry setup. These use cloud credentials and cloud billing. The current first-run “3rd-party platform” wizard covers Bedrock and Vertex; use the linked provider setup for other routes. Retain the exact region, deployment/model ID and IAM identity.[12]
4. Organization gateway: the first-party Claude apps gateway supports corporate sign-in; a generic LLM gateway is a different route. An approved API gateway must implement the required Anthropic protocol and preserve tools, streaming, errors and usage. `ANTHROPIC_BASE_URL` and cloud-specific base-URL variables change inference routing. Do not point subscription credentials at an arbitrary gateway.[11][12]

Before changing anything, inspect `/status` and locally review credential selectors such as `ANTHROPIC_API_KEY`, `ANTHROPIC_AUTH_TOKEN`, `apiKeyHelper`, profile/federation settings, cloud flags and managed policy. These are not interchangeable and may outrank the browser login. Do not publish their values. `/status` reports the effective provider/base URL; a stored-login report alone is insufficient.[11][12]

The unmodified Claude Code binary with each user's own login is not the same as collecting or brokering subscription tokens for other software. Do not pool seats or resell a subscription endpoint. API price estimates do not establish a subscription bill reduction.[48]

## Conservative recipe

1. Record the installed version, current account route, exact model/effort, loaded MCP servers, permissions and one representative task's baseline usage. Inspect before adjusting:

   ```sh
   claude --version
   claude --help
   ```

   Inside the session, use `/status`, `/context` and `/mcp`. These are discovery steps, not a license to change auth or disable tools required for the task.[46][47]
2. Merge the following original instruction excerpt into the existing project-root `CLAUDE.md`, not user-global settings. Review existing rules first; keep project-specific commands and safety constraints.[70]

   ```text
   For this project, preserve the requested scope, model, effort and approvals.
   Locate exact files and symbols before broad reading; read full material when requested.
   Compute exact bulk results over all eligible records in code; retain source and counts.
   Reuse existing code and dependencies before adding abstractions.
   Make the smallest complete patch. Keep required regression, integration and build tests.
   Retain errors and unresolved work. Verify real output before calling the task complete.
   ```
3. Ask for file/symbol discovery, then read the affected flow, callers and tests. Use native edits for small changes. Keep deterministic parsing, joins, pagination and artifact generation in authorized local tools. Every-record semantic review still requires every substantive record, not a top-k excerpt.
4. Keep native prompt caching, compaction and MCP tool search as the baseline. Add only task-relevant MCP servers, with their own account login and least necessary data access. A proxy that loses `tool_reference` support can disable native discovery and increase context instead.[47]
5. Compare the complete resulting artifact and full required test suite with the baseline. Count failed patches and retries. Do not use `--bare` as a token preset: it changes context/customization loading and does not read native Anthropic OAuth.[46]

## Aggressive recipe

Start with explicit observation files: retain complete command output and its exit status, then show a selected view with exact source location, coverage and omissions. Do not transform the source needed for the active edit or review.

For long sessions, make a protected checkpoint containing acceptance criteria, exact identifiers, corrections, approvals, side effects already performed, errors, tests and source locations. Review it against the originals, then use native `/compact` with preservation instructions. This is lossy model context, even when source history exists.[46]

Current `PostToolUse` supports `hookSpecificOutput.updatedToolOutput`; it must match the original tool output shape. This is an optional, version-gated seam, not a reducer installed by this guide. A replacement needs retained raw output, full errors and a tested restore operation. Post hooks cannot undo actions, and telemetry may already contain the original. Do not copy this field to Codex or Grok hooks.[59]

Never lower effort, change models, auto-approve tools, or rewrite opaque provider history as an “Aggressive” default.

## Verify and roll back

1. In a trusted disposable project, first confirm `/status` still shows the intended route and model. After authorizing a small usage test, ask Claude to read a fixture containing a planted exception, produce a native patch and run the project's actual checks. Confirm the exception survives, the patch is complete, and a deliberately denied action remains denied. Do not use real external writes as the permission test.
2. For automation, current `-p` and `--output-format json` are documented. Print mode skips workspace trust UI, so review project hooks/config before using it. Inspect result errors, usage and actual files, not just an exit message.[46]
3. Remove only the added instruction paragraph or reducer hook. Restore the backed-up settings keys and original output view. Start a new session with the verified checkpoint and required original passages if a summary lost important context.
4. If an intentionally changed auth route must be reverted, restore the exact prior endpoint and selector settings, then use native login for the user's original account. Do not overwrite whole credential files. Logging out can affect other sessions using that credential.[11]

## Limits and evidence

The installed CLI identified as 2.1.205; live documentation contains later features. That version check does not certify newer hooks or keyless Console sign-in on that installation. This guide deliberately avoids a one-size hook installer and any claim of measured token savings. Native cache savings, fewer tokens, subscription quota and API dollars are separate measures.

## Native headless use and delegation

The current official SDK support article starts with a June 15 update pausing the proposed separate-credit change: supported Agent SDK and `claude -p` usage currently still draw from subscription usage limits. Do not use the lower historical credit table as current pricing. Keep this distinction separate from provider restrictions on credential collection/intermediation. See [Delegation](../delegation.md) for bounded native workers and headless patterns.[71]

## Sources

[70] https://code.claude.com/docs/en/memory.md — project-instructions
[11] https://code.claude.com/docs/en/authentication — claude-auth
[12] https://code.claude.com/docs/en/third-party-integrations — claude-cloud
[46] https://code.claude.com/docs/en/cli-reference — claude-cli
[47] https://code.claude.com/docs/en/mcp — claude-mcp
[48] https://code.claude.com/docs/en/legal-and-compliance — claude-legal
[59] https://code.claude.com/docs/en/hooks.md — claude-hooks-full

[71] https://support.claude.com/en/articles/15036540-use-the-claude-agent-sdk-with-your-claude-plan — current-sdk-billing-update
