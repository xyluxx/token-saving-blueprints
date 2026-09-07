# Delegation without making the user manage more agents

[Start here](../START-HERE.md) · [Team handoff](playbooks/teams.md) · [OmniRoute](addons/omniroute.md) · [Cheaper/free workers](addons/free-provider-lanes.md)

Delegation belongs alongside **both modes**. The main agent owns the task, sends a small complete brief, checks the result and delivers the finished work. A cheaper worker is a separate model/cost decision, not proof that compression saved tokens.

**Another API model does not require another app window.** A tool-capable worker still needs a running execution host with the right tools, permissions and credentials. An endpoint alone supplies inference, not an autonomous agent.

Checked 2026-09-07 UTC. The patterns below are source-backed and version-specific; they were not executed as authenticated native delegation trials for this repository.

## Choose the actual kind of delegation

| Pattern | What runs | Who owns tools and state | What must exist |
|---|---|---|---|
| Native subagent | A child context inside the current harness | Parent harness and its child policy | A supported native subagent feature and available runtime |
| Same harness, another API model | The same agent/tool loop with a separately approved inference route | Existing harness | Per-worker model/provider support and authorized credentials |
| Separate headless harness | A CLI/SDK/backend process with its own agent loop | That runtime, supervised by the main agent | Installed/available runtime on the local or remote host; no extra GUI required for documented headless use |
| Analysis-only API helper | One or more bounded model completions | Parent retains all tools and actions | An approved API-call capability; unexpected tool requests are not executed |

Initial login may require browser consent. That is different from keeping a browser or editor window open for every worker. Background survival, cancellation and resumability depend on the chosen runtime; do not promise every child survives closing the parent.

## The common workflow

1. **Keep one owner.** Identify the final requested result and which bounded part is genuinely independent. Do not delegate a simple deterministic calculation to an LLM just because a cheap endpoint exists.
2. **Choose the route deliberately.** Record main and worker model, supported effort, account/project, data policy, budget and allowed fallbacks. A model selection is not proof of actual execution identity.
3. **Send a small complete packet.** Use [delegation packet](../templates/delegation-packet.md), not the parent's entire chat, credentials or unrelated client history. Also inspect implicit context such as global rules, long-term memory, inherited skills and MCP schemas: a small brief does not prove those are absent. If sensitive outbound context cannot be bounded, retain the approved route instead of offloading it.
4. **Bound authority.** Give only the necessary source/tool access. A fresh conversation is not a filesystem sandbox. An API key changes billing, not what the worker may do.
5. **Run independent work in parallel where useful.** Use disjoint workspaces for edits and a clear integration owner. Do not fork concurrent mutations of the same files or external records.
6. **Verify and reconcile.** Inspect cited sources, artifacts, tests, actual route/effort and completed actions. A worker saying “done” is not completion evidence.
7. **Finish centrally.** The main agent resolves conflicts, reports remaining uncertainty and delivers the actual required result. After interruption, reconcile effects before retrying.

## Conservative and Aggressive behavior

Conservative uses concise briefs, relevant evidence, deterministic preparation, complete coverage and the normal model/permission/verification contract. Native worker context isolation can avoid repeatedly replaying irrelevant parent history, but launching workers also costs tokens and time.

Aggressive can additionally use approved selective observations or phase checkpoints in each worker. The same protected identifiers, corrections, requirements and raw-source recovery still apply. Do not summarize away evidence a worker or reviewer needs.

Smaller/free worker models are **opt-in cost choices for either mode**, not a silent change in the Conservative preset. Check the worker's accepted quality and total cost. Keep the main model/effort unchanged unless separately approved.

## Native patterns by harness

These are separate contracts. Do not copy one harness's model or effort fields into another.

### Claude Code

Native subagents support prompts, tools, model, permission mode, effort and turn limits in supported versions. Model values can inherit or select supported Claude identifiers; this is not a generic arbitrary-provider setting. Current model precedence differs from older releases, and managed policy may substitute a model. Verify the actual child rather than trusting frontmatter alone.[1]

Illustrative source-reviewer definition, only after checking the installed schema:

```yaml
name: source-reviewer
description: Review a specifically authorized source packet without edits
model: inherit
tools: Read, Grep, Glob
permissionMode: plan
maxTurns: 20
```

Effort is deliberately omitted to inherit under the documented current behavior. If the installed version/model needs an explicit level, set only the separately approved supported value; do not raise or lower it by copying an example. Tool lists do not replace source/OS permissions. A cheaper Claude worker requires separate model/quality approval and supported effort.

A supported headless alternative uses the existing runtime, not another app window:

```sh
claude -p --model "$APPROVED_CLAUDE_MODEL" --effort "$APPROVED_EFFORT" --tools "Read,Grep,Glob" --disallowedTools "mcp__*" --max-turns 20 --output-format json < brief.md
```

These are example bounds, not guarantees of completion. Verify installed help and inherited hooks/plugins. `--tools` concerns built-ins; MCP has its own restrictions. Do not use permission-bypass flags to make a blocked worker run.[2]

The current official Agent SDK support article starts with a June 15 update pausing its announced separate-credit change: SDK and `claude -p` use currently remain within subscription usage limits. The lower historical credit table is not current billing. Use this with current legal/account rules, not as permission to export OAuth tokens to OmniRoute or pool personal seats.[3][4]

### Codex

Native subagents have separate context and model/effort configuration. Current custom-agent TOML files and config precedence are version-specific. Selecting a new model without effort can invoke that model's default; pin/verify both when an explicit worker change is intended.[5]

Do not assume a per-child provider field identical to OpenCode's. Machine-local provider/auth definitions are not ordinary untrusted project overrides. A standalone run can select an already authorized route without rewriting shared defaults:[6]

```sh
codex exec -C "$WORKSPACE" --sandbox read-only -m "$APPROVED_MODEL" -c "model_reasoning_effort=\"$APPROVED_EFFORT\"" --json - < brief.md
```

Inspect the actual custom provider/credential helper and Responses protocol. Read-only shell access does not revoke independently authorized remote MCP writes. Native ChatGPT login and API-key billing are different routes; do not transplant credential caches.[6][7]

### OpenCode

A native agent can use `mode: "subagent"`, a configured `provider/model`, `permission` and `steps`. If unset, the child model normally inherits. Provider-specific options and CLI variants are not universal reasoning controls.[8]

Illustrative declaration with an intentionally nonworking model placeholder:

```json
{
  "agent": {
    "source-reviewer": {
      "mode": "subagent",
      "description": "Return cited findings for the authorized source packet",
      "model": "APPROVED_PROVIDER/APPROVED_MODEL",
      "steps": 20,
      "permission": {"edit": "deny", "bash": "deny"}
    }
  }
}
```

Restrict remaining tool/MCP categories and source roots as needed. Add only the reasoning option supported by the selected model. A native headless invocation is documented:[9]

```sh
opencode run --agent source-reviewer --model "$APPROVED_PROVIDER_MODEL" --variant "$APPROVED_VARIANT" --format json --file brief.md "Complete the attached scoped brief"
```

An existing server may remove repeated startup, but `--attach` connects to a real running server, not a bare model endpoint. Do not create a service solely to claim savings.

### Hermes

Native `delegate_task` uses its configured delegation model/provider and an isolated child context. Do not invent per-task model fields. The child can have its own configured effort, so a high-effort parent does not prove a high-effort worker.[10]

For an explicitly selected model/provider/effort, the supported standalone CLI provides a run-scoped route without mutating global delegation settings:[11]

```sh
hermes chat --oneshot --query-file "$BRIEF" --in "$WORKSPACE" --provider "$APPROVED_PROVIDER" --model "$APPROVED_MODEL" --reasoning "$APPROVED_EFFORT" --toolsets "$APPROVED_TOOLSETS" --max-turns 40
```

The provider must already be provisioned and its terms/billing accepted. Inspect inherited fallbacks and actual session metadata. Do not start a job whose required model/account/fallback boundary cannot be constrained in the selected runtime. A warning after an unauthorized paid fallback does not undo the call. Profile separation is not OS isolation. Choose appropriate task bounds; a cap stop is partial work, not a completed result.

### OpenClaw

Native `sessions_spawn` and external ACP sessions are different runtime paths. Supported native inputs can select model and thinking, while configured defaults/visibility affect inheritance and legal parameters. An invalid model can fall back with a warning; verify resolved provider/model.[12]

A documented headless gateway invocation is:

```sh
openclaw agent --agent "$APPROVED_AGENT" --session-id "$NEW_JOB_UUID" --message-file "$BRIEF" --model "$APPROVED_PROVIDER_MODEL" --thinking "$APPROVED_THINKING" --json
```

Use a new task identity and the authorized workspace. The normal gateway route and `--local` have different requirements. No delivery flag is part of this analysis example. ACP or a native Codex app-server path still needs the actual healthy backend/runtime, not a GUI window or a copied token.[13][14]

### Gemini CLI

Current documented local subagents have model, tools, isolated MCP configuration and turn/time bounds. They do not advertise an arbitrary provider or generic `effort` field. Headless execution is supported, but the account/product and thinking controls must be verified for the installed version. Do not promise a lower-cost child if required reasoning cannot be preserved or deliberately approved.[15][16]

Use the current [Gemini route guide](harnesses/gemini-cli.md), not old consumer entitlement assumptions.

### Qwen Code

Named subagents, forked subagents and provider resolution differ. Current docs describe `inherit`, `fast` and explicit `authType:modelId` selection; a bare model can resolve to another configured provider. Use explicit selectors and verify the actual account. Do not copy OpenCode's slash syntax.[17]

The documented `effort` field is not implemented in that source contract. Do not claim it took effect. Keep the supported main route or a verified alternative when required effort is uncertain. Headless operation does not revive the retired Qwen OAuth free tier; use the [current route guide](harnesses/qwen-code.md).[17][18]

## Where OmniRoute fits

It can sit on an approved worker API path when the [restricted add-on gates](addons/omniroute.md) pass. It is not required for native delegation or another API call.

Its extra features need their own interpretation:

- Compression CPU workers are not LLM delegates.
- MCP routing tools submit requests; they do not automatically give a model approved filesystem/shell authority.
- Fusion fans out model calls and uses a judge. Pipeline chains model outputs. They can increase cost and omit needed context; they are not automatically cheaper autonomous workers.
- A2A operations and external cloud-agent adapters require actual runtimes, identities, endpoint rights and authority propagation. A protocol status is not proof of completed business work.

The initial blueprint lane keeps those extra gateway orchestration features off. Use the native host's clearer task/permission lifecycle first. The source audit found caller-scope/budget differences in the A2A path, so it is not presented as a trusted multi-tenant delegation firewall.[19][20]

## Multiple accounts and cost

An approved organization can use different API projects/keys for different work. Keep source permissions, provider terms, budgets, data policies and reporting separate. That is not a pool of other employees' subscription seats or a reason to rotate free accounts past their caps.

Every comparison includes parent planning, worker briefs, tool output, model calls, retries, restoration, synthesis/verification and human repair. Native caching can make one warm session cheaper than many fresh workers. Cheaper calls can lower dollars while increasing tokens; parallelism can reduce time while increasing cost.

If a worker fails, lacks a source, changes route unexpectedly, returns unsupported tool calls or cannot substantiate the result, stop/escalate with its evidence. Do not cycle through models until one sounds confident, silently lower effort, or replay completed writes.

## Rollback

Stop new dispatch, preserve artifacts/receipts, reconcile in-flight actions and remove only the task-scoped agent definition or provider override. Restore exact previous model, effort, endpoint and permissions. Revoke a trial credential only in its own scope. Do not erase shared auth stores, transplant opaque provider history or claim source restoration reverses spent credits or external actions.

## Sources

[1] https://code.claude.com/docs/en/sub-agents.md
[2] https://code.claude.com/docs/en/cli-reference.md
[3] https://support.claude.com/en/articles/15036540-use-the-claude-agent-sdk-with-your-claude-plan
[4] https://code.claude.com/docs/en/legal-and-compliance.md
[5] https://developers.openai.com/codex/multi-agent
[6] https://developers.openai.com/codex/config-reference
[7] https://developers.openai.com/codex/noninteractive
[8] https://opencode.ai/docs/agents
[9] https://opencode.ai/docs/cli
[10] https://hermes-agent.nousresearch.com/docs/user-guide/features/delegation
[11] https://hermes-agent.nousresearch.com/docs/user-guide/cli
[12] https://docs.openclaw.ai/tools/subagents.md
[13] https://docs.openclaw.ai/tools/acp-agents.md
[14] https://docs.openclaw.ai/cli/agent.md
[15] https://geminicli.com/docs/core/subagents
[16] https://geminicli.com/docs/cli/headless
[17] https://qwenlm.github.io/qwen-code-docs/en/users/features/sub-agents
[18] https://qwenlm.github.io/qwen-code-docs/en/users/features/headless
[19] https://github.com/diegosouzapw/OmniRoute/blob/b345c7f6cd4e1590d1177540813302375a75e332/src/lib/a2a/skills/smartRouting.ts
[20] https://github.com/diegosouzapw/OmniRoute/blob/b345c7f6cd4e1590d1177540813302375a75e332/open-sse/services/fusion.ts
