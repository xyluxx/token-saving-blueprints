# goose

[Start here](../../START-HERE.md) · [Conservative](../modes/conservative.md) · [Aggressive](../modes/aggressive.md) · [Authentication and billing](../auth-and-billing.md) · [Measurement](../measurement.md)

Checked 2026-09-06 (UTC). Evidence: documented unless stated otherwise; no authenticated agent task or savings benchmark was run.

## Who this is for

Teams already using the open-source goose Desktop or CLI with approved providers and extensions. Use its existing hints, tool selection and session workflows, not a newly built gateway. The project is now published under `aaif-goose/goose` and identifies itself as part of the Agentic AI Foundation at the Linux Foundation.[90]

The public project has provider adapters as well as direct API routes; an adapter is not identical to controlling the underlying agent's full context.[15][56][58]

## Authentication and billing routes

* Direct API or cloud: the documented provider list includes OpenAI, Anthropic, OpenRouter, Bedrock, Azure OpenAI and Vertex AI, plus compatible endpoints and local runtimes. Keep the existing model, endpoint, credentials, cloud project and region. Configure/view them through Desktop Settings > Models or the installed CLI's `goose configure`, without replacing the existing selection.[15]
* Subscription OAuth: goose documents a Desktop ChatGPT Subscription browser sign-in and a GitHub Copilot device flow. These are project-supported provider paths; use their own selectors and authentication, not an extracted token or generic API base. Entitlement and account-policy eligibility still need confirmation by the user.[15]
* Native-agent adapters: goose also documents Cursor Agent and ACP integrations with other coding agents. They require an existing supported, authenticated agent and inherit its entitlement or API route. Do not install an adapter merely to reduce tokens, and do not assume outer goose controls replace its inner permission system.[15][68]
* Environment/endpoints: provider-specific variables such as `OPENAI_API_KEY`, `OPENAI_HOST`, `GOOGLE_API_KEY`, cloud credentials and custom endpoints can change the actual request path. The provider guide documents these settings; this guide does not assert a universal environment-key override of every OAuth provider.[15]

The goose application is not itself an unlimited model subscription. Provider charges, aggregator balances, cloud billing, local compute and an adapter's subscription quotas are different meters. Native prompt caching is already part of several provider implementations; do not count it as a newly installed saving.[15]

## Conservative recipe

1. Record the current provider/model/effort, active extensions, permissions and session. Back up project hints. Keep account/global configuration unchanged; use the current session rather than auto-detecting a new provider from a key.
2. Merge a small section into the project's `.goosehints` or already active `AGENTS.md`, avoiding duplicate instructions. Hints are added to the prompt and nested hints load as files are accessed. New content must be checked in a new session because hints load at session start.[56]

   > Keep original requirements, model, effort and permissions. Enumerate the complete candidate set. Read precise relevant source ranges and dependencies, recording coverage. Use existing deterministic tools for bulk changes and all-row computation. Patch minimally, run all required tests, and report actual results. Do not clear history, sample required review, or count a pointer as an answer.

3. In Desktop, review Extensions and retain the necessary Developer tools and approved read-only data sources. In CLI use existing extension controls; do not install new servers from an untrusted recipe. Extensions expose concrete tools, and may execute local commands.[58]
4. Preserve the current approval mode. If it is autonomous and that conflicts with the task's approval requirement, stop for an explicit permission decision. With approval to tighten it, CLI `/mode approve` selects manual approval; the docs warn that prompts may cover tools classified as writes, not every possible read. It is not a complete source-data isolation boundary.[58][68]
5. Give goose the exact task files and request a coverage-first investigation. Inspect proposed shell/MCP operations, perform the minimal edit, then run every required test. Do not spawn extra agents just to hide their cost or omit their work from measurement.

## Aggressive recipe

1. Through the existing Developer terminal or an approved read-only query tool, save the complete source/query/test result, then produce an explicit observation view. It must identify the source revision, query, complete coverage/counts, all failures and raw-result locations. No new gateway or extension is required.
2. Present that view for subsequent reasoning. If every record must be reviewed, use complete paginated review instead; deterministic totals do not replace it. Restore raw detail on count mismatches, stale revisions, missed constraints or unexplained test changes.
3. At a phase boundary, create a reviewed handoff of exact requirements, identifiers, decisions, work remaining, changed files, real test results and external actions already performed. Retain the original session and open a new one from the same project/provider with only the handoff and required sources.
4. Verify the new session uses the original hints and reconstructs critical requirements from original evidence before further edits. Never mutate goose's session database or treat a summary as a complete backup.

Control ceiling: hints are instructions, not enforcement. Extensions/MCP can shape their own returned data; they do not universally rewrite the model's history. With a CLI/ACP provider there is another harness in the path, so its permissions, context handling and billing must also be inspected.[15][56][68]

## Verify and roll back

Compare identical tasks/model/effort and all test requirements. Include helper/tool work, adapter activity and retries. Use actual provider usage and any native session display that exists in the installed version. If an adapter exposes quota but no trustworthy token count, report quota observations and unknown token attribution, not an invented meter.

Restore the hints file and previous extension selection. If separately approved permission changes were made, restore their recorded original state. Open the retained session or reattach original evidence when the handoff fails. Revert only task edits via a reviewed diff/backup and rerun tests; do not undo unrelated work. File restoration does not reverse a remote tool call or model billing.

## Limits and evidence

Documented provider and native-tool capabilities; no authenticated execution or savings benchmark. Approval UI is not a substitute for read-only source credentials, filesystem boundaries or an approved processing provider. Even local inference can transmit data through remote extensions. Do not export credentials or add a self-hosted relay as an incidental optimization. A separately approved OAuth integration or native-agent bridge needs its own provider-specific terms, account, credential-custody and runtime review. Availability of a goose-documented integration is not a universal license to use another service outside its terms.[15][58][68]

## Sources

[15] https://raw.githubusercontent.com/aaif-goose/goose/main/documentation/docs/getting-started/providers.md
[56] https://block.github.io/goose/docs/guides/context-engineering/using-goosehints
[58] https://block.github.io/goose/docs/getting-started/using-extensions
[68] https://block.github.io/goose/docs/guides/managing-tools/goose-permissions
[90] https://github.com/aaif-goose/goose
