# Platform coverage beyond terminal harnesses

Checked 2026-09-07 UTC. This complements the [existing CLI/IDE guides](harnesses/index.md). It is a platform selector, not an optimizer runtime or a promise that every application accepts a proxy. The companion [coverage catalogue](../catalog/coverage.json) gives the full conditions, authentication boundaries, billing caveats and sources for each row.

Start with the surface you actually use. Keep your current model, effort, account and permissions. Conservative means removing unnecessary work and improving explicit task context. Aggressive adds reviewed context projections or checkpoints where that surface permits them. Neither mode requires changing providers.

The catalogue has 34 additional platform/surface records, including legacy recognition, alongside 19 detailed CLI/IDE guides. These are not 53 independent products or tested integrations.

Where a hosted app hides model, effort or prompt state, record that as unknown rather than claiming a fixed-model or context guarantee. Its native workflow advice can still be useful.

No authenticated platform or OmniRoute integration was exercised for this coverage review. “Documented configurable interface” means the client has a documented configuration seam. It does not mean the complete client, gateway, upstream model and account combination has passed a trial.

## Choose your path

| What you use | Start here | What not to assume |
| :--- | :--- | :--- |
| ChatGPT, Claude or Gemini in a browser | Project/Gem instructions, relevant source files, exact task boundaries and reviewed handoffs | A web chat is not an API client with a configurable model base URL.[91][71][29] |
| ChatGPT desktop with Codex | Identify Chat, Work or Codex and whether work is local or cloud | The current desktop app includes different modes; CLI settings do not automatically apply to all of them.[109][110] |
| Claude Cowork | Native task/project context, approved file/connector access and artifact verification | Cowork is no longer accurately described as desktop-only or always local.[20] |
| Kiro or existing Amazon Q Developer | Identify the current surface and generation before using its own steering/spec controls | A Kiro automation API key is not provider BYOK; Q Developer console, IDE and old CLI are not one migration case.[50][15][115] |
| Your own Python/TypeScript/.NET agent application | Explicit tool contracts, deterministic workflow steps and the framework's real input/state controls | SDK names do not establish shared authentication, account allowance or protocol semantics.[1][3][11] |
| n8n, Dify or Langflow | Project complete business data into exact LLM inputs and keep deterministic work outside the model | A workflow call, AI response, provider token and hosting charge are different billing units.[69][17][18] |
| Copilot Studio | Identify the selected Studio harness, then use its instructions, knowledge, flows and tests | A custom connector is a tool integration, not necessarily replacement of the orchestration model.[19][72] |
| Open WebUI or LibreChat | Use the existing approved model connection and explicit source context | Application login and upstream model authentication are separate. Auxiliary calls can use other routes.[92][62] |
| Replit, Lovable, Bolt or Devin cloud | Scope the native task, plan first, inspect outputs and preserve checkpoints | An API key in a generated app or a task-creation API does not reroute the builder itself.[26][27][25] |

## Read support labels literally

| Label | Meaning |
| :--- | :--- |
| Documented configurable interface | A specific model client or provider setting can address a compatible endpoint. The proposed OmniRoute pairing remains conditional and untested. |
| Limited native/workflow-only support | The useful path is instructions, source selection, deterministic work, native tasks or reviewed handoffs. This is not a proxy connection. |
| Unsupported interface | Use only when the exact proposed interface is known not to implement the required contract. A missing recipe alone does not prove a vendor prohibition. |
| Unverified | A consequential mechanism, entitlement or behavior was not established. Do not manufacture a configuration to fill the gap. |

OAuth is an authentication mechanism. API transport and protocol are different questions. OmniRoute documents upstream OAuth and API-key mechanisms behind an API-facing gateway. That capability does not grant entitlement or override the upstream provider's terms.[108]

Keep seven facts separate: product capability, this blueprint's recommendation, credential owner/refresh mechanism, account entitlement, client/gateway protocol, observed test behavior, and unresolved limitations. Native CLI-owned login and a gateway directly managing OAuth tokens are not the same route.

## Native application and surface coverage

| Platform or surface | Useful first move | Decisive condition |
| :--- | :--- | :--- |
| ChatGPT web and Projects | Put the task contract in Project settings; attach authoritative sources; use separate focused chats | Project memory may carry context across chats. A fresh chat is not proof of an empty context or all-file review. No generic model proxy setting is established for browser chat.[91][110] |
| ChatGPT desktop, including Codex local work | Choose the actual mode and folder/project before asking for a bounded artifact | The old `/codex/app` documentation URL now resolves to “ChatGPT desktop app.” Current local Codex auth supports ChatGPT or API key; this does not make browser ChatGPT API-key configurable.[109][110] |
| Codex cloud/web | Use the approved repository environment, precise task and complete checks; inspect logs and diff | Cloud requires ChatGPT sign-in. Environment variables for a task are not proof of managed-inference endpoint control.[22][110] |
| Claude chat, Desktop and Cowork | Use project instructions/knowledge for chat; use Cowork for a bounded task needing file access or extended execution | Cowork now documents web/desktop/mobile and cloud sessions in beta, with plan/admin and local-feature conditions. Native subagents do not turn ordinary chat into an Agent SDK endpoint.[71][20] |
| Gemini Apps and Gems | Edit a Gem's instructions and relevant reference files, preview and explicitly save | This is native app customization, not Gemini CLI, Antigravity or ADK configuration.[29] |
| Kiro | Review existing `.kiro/steering/`, then use a task-specific steering file and exact spec | Current docs describe a unified harness across surfaces, but permissions and generations differ. Use Kiro's native subagents/compaction rather than inventing a proxy.[14][54][99] |
| Amazon Q Developer, existing users | Identify AWS console/chat versus IDE plugin versus old CLI; preserve the current route | AWS announces IDE plugin support ending April 30, 2027. That is not retirement of all Q Developer or Q Business. Kiro is the next update of Q CLI.[15][115] |

The reviewed “Claude apps gateway” is a service for Claude Code clients, with corporate sign-in and model-provider credentials held at the gateway. Its name does not establish generic Claude chat or Cowork interception.[85]

Kiro's paid-plan `KIRO_API_KEY` is for its own CLI automation and remains subject to organizational governance. It is not an Anthropic, Bedrock or OpenAI BYOK field. Headless tools need preauthorization; do not copy a trust-all example to save interruptions.[50][101]

## Application-owned SDKs and frameworks

These provide stronger control because your application owns some or all of the execution loop and model input. The useful first change is usually a precise tool result or deterministic workflow step, not a second model call that summarizes every observation.

| Platform | Conservative starting point | Optional Aggressive seam | Conditional gateway interface |
| :--- | :--- | :--- | :--- |
| OpenAI Agents SDK | Explicit model/effort, exact tool outputs, one session-history owner | Session input policy or handoff input filter with retained originals | `AsyncOpenAI(base_url, api_key)` plus the correct Responses or Chat Completions model class. Handoffs and agents-as-tools are different patterns.[1][2][113] |
| Claude Agent SDK | Native tool loop, scoped permissions and exact task contract | SDK sessions/hooks and focused subagents, validated for the installed version | Underlying Claude Code gateway contract, not a Chat-Completions-only endpoint. The Agent SDK is not the lower-level Anthropic Client SDK.[3][57][112] |
| LangGraph with LangChain integrations | Deterministic graph nodes, exact state and checkpoints | Pre-model projection, trimming or summarization with recoverable source state | `ChatOpenAI(base_url, api_key)` covers official OpenAI fields. Use a provider-specific adapter for non-standard reasoning fields.[6][87][7] |
| PydanticAI | Typed results, deterministic validation and explicit provider | History processors with supported copy/replace semantics | `OpenAIProvider(base_url, api_key)` with Chat or Responses model class as appropriate. Provider retries are separate from agent retry budgets.[8][9][88] |
| CrewAI | Exact task outputs, scoped tools and a small explicit crew/workflow | Reviewed task-to-task context and existing context-window controls | `LLM(custom_openai=True, base_url, api_key, model)` for a compatible gateway. Native provider integrations and LiteLLM-backed paths differ.[10][89] |
| Microsoft Agent Framework | Use functions for mechanical work, explicit clients, sessions and tools | Middleware/context providers and explicit workflow handoffs | Current OpenAI client source exposes `base_url`, API-key/callable and custom client controls. Verify the chosen Chat Completions/Responses client and language.[11][82][117] |
| Google ADK | Exact tool results and explicit model connector | Configured event compaction with full retained events | Python `LiteLlm` connector for external/local models. Connector support and configuration differ by language.[13][66][67] |
| Vercel AI SDK | Deterministic application code plus scoped model tools | `prepareStep` and explicit loop/input policy | `createOpenAICompatible` with `baseURL` and `apiKey` supplies Chat Completions models. Responses needs the appropriate adapter.[23][65][90] |
| GitHub Copilot SDK | Bounded session, explicit tools and a real permission handler | Separate focused sessions with retained evidence | Session `provider` configuration with base URL and explicit wire API; SDK talks JSON-RPC to the Copilot CLI server.[63][64] |
| Mastra | Explicit model/effort, tools and deterministic workflow steps | Input processors, memory projections and native subagents | Custom model object uses `url` and namespace-sensitive `id`; do not substitute a guessed `baseURL` field.[94][95][114] |
| Agno | Explicit model/embedding choices, typed outputs, scoped tools | Deliberate history selection and bounded Teams/workflows | Source-defined `OpenAIChat(base_url, api_key, id)` is a Chat Completions client. AgentOS is a separate runtime/control-plane surface.[96][97][98] |

### SDK authentication and billing conditions

1. OpenAI Agents SDK defaults to API-oriented clients. ChatGPT account entitlement is not automatically an SDK credential. Its tracing destination is separate from inference; the docs recommend disabling tracing or choosing another processor when no OpenAI API key is available.[1]
2. Claude's current support article begins with a June 15 pause: Agent SDK, `claude -p` and third-party app usage still draw from subscription usage limits. The lower historical separate-credit section is not the current billing rule.[56]
3. Separately, the Claude SDK overview says third-party developers may not offer `claude.ai` login or rate limits in their products without prior approval. Do not convert a billing statement into universal permission, or earlier blueprint caution into a blanket prohibition on native CLI-owned login.[3]
4. Copilot SDK documents a native CLI-auth route and BYOK without GitHub authentication. Its README says BYOK is key-based and does not support Entra/managed identities on that path. That limit must not be copied onto LangChain or Microsoft Agent Framework's different Azure identity integrations.[63][64][7]
5. Microsoft identifies Agent Framework as the successor to AutoGen and Semantic Kernel. AutoGen is in maintenance mode and directs new users to Agent Framework. Current Agent Framework Go coverage remains public preview, so language parity is not assumed.[11][59]
6. ADK's current LiteLLM connector documentation requires `litellm>=1.84` and discloses compromised earlier versions. Follow the current advisory and approved dependency policy rather than an old unconstrained installation snippet.[66]

Changing model, effort, provider, fallback order or account is a separate experiment. A lower-cost route is not itself token reduction. Include model retries, validators, compressors, embedding/reranking, tools and worker integration when comparing full tasks.

## Visual business builders and configurable chat UIs

| Platform | Useful first move | What can actually be configured | Important condition |
| :--- | :--- | :--- | :--- |
| n8n | Deterministic nodes process every required row, then return exact LLM fields and exceptions | OpenAI credential `Base URL` and key; selected Chat Model node's API mode | Current source and prose differ on the default Responses selection. Inspect node version and actual selector. Old node-level Base URL examples are version-gated.[102][86][69] |
| Dify | Deterministic workflow transforms plus precise prompts and retrieval scope | Official OpenAI-compatible provider plugin exposes `endpoint_url`, model and credential fields | Current Cloud AI credits are per model response, independent of its token count. BYOK and credits can coexist with Usage Priority; credentials/defaults are workspace-wide.[70][17] |
| Langflow | Prompt Template, exact inputs and deterministic components | Global Model Providers includes OpenAI Compatible; enable the intended model and connect the proper component output | Chat, embedding and other service configuration remain distinct. A global provider change can affect more than one flow.[18] |
| Microsoft Copilot Studio | Identify harness, then use exact instructions, knowledge, deterministic flows and native evaluations | Native model selector and connectors; no generic core-inference proxy route established | Standard, GitHub Copilot and Copilot chat harnesses have different capabilities and billing. A connector calling an external API is a tool call.[19][72] |
| Open WebUI | Use the existing approved connection and relevant files/tools | Admin > Connections > Manage OpenAI API Connections, with URL/key and explicit model IDs | Main documented protocol is Chat Completions; Open Responses is experimental. A failed `/models` check is not necessarily failed chat, but still needs a trial.[92] |
| LibreChat | Use exact context with an existing approved endpoint; inspect auxiliary calls | `endpoints.custom` in `librechat.yaml` exposes `baseURL`, key and models; current source also has a native Anthropic option | Application auth, inference, titles, activity labels, embeddings and other services can have different routes. Preserve SSRF/private-address controls.[62] |

Open WebUI now documents native subagents. They are disabled by default and require global/model enablement plus native function calling in UI chats; direct API callers do not automatically receive the delegation tool. Every child adds model work.[93]

For either UI, explicit context selection is useful before considering runtime extensions. Open WebUI's legacy Pipelines are not recommended here as a new deployment path; this packet does not install any extension.[78]

## Hosted coding and app-building workflows

| Product or surface | Practical path | Boundary |
| :--- | :--- | :--- |
| Replit Agent | Plan the exact change before building; inspect the actual output and checkpoints; retain paid-action approvals | Current modes include Free, Power and Max with separate enterprise behavior. Generated-app API credentials do not reroute Agent inference.[26][116] |
| Lovable | Agree a user flow and acceptance criteria, then make one coherent change and inspect it | A unified credit balance across Build, Cloud and deployed-app AI is rolling out gradually. Do not assume all workspaces have the same layout or credits measure only chat tokens.[103][104] |
| Bolt | Scope prompts and use direct Code view edits for suitable deterministic changes | Bolt says Code view edits do not use tokens. Hosted Bolt is not the separate `bolt.diy` project, and no generic core model proxy route is established here.[28][105] |
| Devin cloud | Give a well-scoped ticket, setup context and complete checks; inspect shell logs and patch; split independent work with clear ownership | This supplements the existing Devin Desktop/Windsurf guide. Devin's task API and local-to-cloud handoff are not an OpenAI model endpoint; exact current cloud billing remains account/contract-specific and was not established here.[25] |

Recommended Aggressive pattern for these surfaces: retain source files, full logs and a reviewed checkpoint; pass the next task only its required context, unresolved work and exact acceptance criteria. Do not delete conversations, silently change models, weaken approvals or treat checkpoint rollback as reversal of remote actions.

## How this coverage is organized

1. A native applications selector for ChatGPT web/desktop, Claude chat/Cowork, Gemini Apps and Codex cloud. These are not CLI profiles in disguise.
2. Kiro with a Q Developer migration boundary, including current CLI generations, paid automation keys and native steering/subagents.
3. Application-owned framework coverage for OpenAI Agents SDK, Claude Agent SDK, LangGraph, PydanticAI, CrewAI, Microsoft Agent Framework, Google ADK and Vercel AI SDK. Copilot SDK, Mastra and Agno add useful, source-backed programmatic paths rather than minor forks.
4. Builder coverage for n8n, Dify, Langflow and Copilot Studio, including non-token credit meters and workspace-wide configuration scope.
5. Open WebUI and LibreChat for configurable chat UIs. Keep them separate from closed web apps even when the visible chat experience looks similar.
6. Workflow-only coverage for Replit, Lovable, Bolt and Devin cloud, without claiming arbitrary backend proxy control.

## Exclusions and migration-only cases

| Candidate | Decision | Current evidence |
| :--- | :--- | :--- |
| Flowise | Do not add as a maintained new-builder recommendation. Provide a migration/retention note for existing users only. | Official repository and maintainer announcement say archived August 13, 2026, with EOL August 31.[60][83] |
| Roo Code | Do not add a new setup recipe. Do not automatically endorse a fork. | Owner repository says the extension shut down May 15 and the repo was archived.[24] |
| AutoGen | Use a migration note, not a competing default new Microsoft framework recommendation. | Publisher says maintenance mode and recommends Microsoft Agent Framework.[59] |
| Semantic Kernel | Cross-link the current Microsoft successor guidance; do not call the project technically archived without evidence. | Agent Framework's official overview explicitly describes the successor relationship.[11] |
| Existing 19 harness guides | Retain and link, rather than creating duplicate rows for their already-covered CLI/IDE routes. | This coverage was compared with their audience, identity, auth and control sections. Existing lifecycle corrections remain in those guides. |
| Small community Grokbot lookalikes and retired-tool forks | No automatic admission or credential recipe. | Exact identity and maintained adoption path are not established by a similar name. Use the existing Grokbot identity boundary. |

This is a bounded coverage decision, not a claim to enumerate every assistant product. Specialized retrieval components already present in the repository's market/component guides should stay there rather than being recast as extra chat applications.

## Further common surfaces and legacy recognition

The catalogue also includes the entries below. A configurable interface remains conditional, not a tested OmniRoute combination.

| Surface | What can be used | Boundary |
|---|---|---|
| Zed | Zed-owned AI supports documented compatible endpoints; source/context methods also apply | External Agents and Terminal Threads own separate runtime/auth settings; hosted access, API keys and existing subscriptions are different routes. |
| OpenHands and Software Agent SDK | Explicit LLM configuration, tool/event ownership and native context controls | Source exposes `base_url` and a subscription-login factory; protocol support, provider permission and account billing still need their own check. |
| Microsoft Copilot Chat / Microsoft 365 | Scoped sources, native tasks and approved agents | Chat, metered agents, Microsoft 365 licensing and Copilot Studio are not one product or meter. No generic core-chat model proxy setting is established here. |
| Gemini Notebook (NotebookLM URL) | Focused authoritative sources and checked citations | Current landing/help use Gemini Notebook. Native research workflow only here; no inference endpoint override or token saving percentage established. |
| Roo Code | Existing-user identification and migration planning | Official extension shutdown notice outranks old install instructions. No new setup or automatic fork endorsement. |
| Flowise | Retained-deployment inspection and migration planning | Repository archived; existing `ChatOpenAI` source maps `basePath` to `baseURL`. Do not treat retained code as a maintained new-platform recommendation. |

These are additional surfaces and legacy records, not six certified deployments. Read each record's exact conditions and sources in [the catalogue](../catalog/coverage.json).

Sources: [Zed model ownership](https://zed.dev/docs/ai/llm-providers), [Zed API setup](https://zed.dev/docs/ai/use-api-access.html), [OpenHands architecture](https://docs.openhands.dev/sdk/arch/llm), [OpenHands LLM source](https://github.com/OpenHands/software-agent-sdk/blob/main/openhands-sdk/openhands/sdk/llm/llm.py), [Microsoft Copilot Chat](https://learn.microsoft.com/en-us/copilot/overview), [Google notebook landing](https://notebooklm.google/), [Roo notice](https://docs.roocode.com/), [Flowise repository](https://github.com/FlowiseAI/Flowise).

## Verify before adopting a configurable endpoint

1. Inspect the current version and effective provider/client selection without printing secrets. Record account, model, effort, protocol and payer independently.
2. For a separately authorized small fixture, check real text output, streaming, tool-call/result IDs, structured output, reasoning/state items, cancellation, errors and usage. A successful model list or login is not sufficient.
3. Run the same complete task and acceptance checks as the native baseline. Include failed work, all workers, transformations, retries and restoration.
4. Restore only changed settings and reopen retained original evidence on failure. Do not delete sessions or credential stores. Do not replay already-completed external actions.

The fixture above is an adoption requirement, not a test performed by this document. Native workflow advice remains useful when no configurable gateway path is established.

## Sources

[1] https://openai.github.io/openai-agents-python/models
[2] https://openai.github.io/openai-agents-python/sessions
[3] https://code.claude.com/docs/en/agent-sdk/overview
[6] https://docs.langchain.com/oss/python/langgraph/overview
[7] https://docs.langchain.com/oss/python/integrations/chat/openai
[8] https://pydantic.dev/docs/ai/overview
[9] https://pydantic.dev/docs/ai/models/openai
[10] https://docs.crewai.com/v1.15.20/en/concepts/llms
[11] https://learn.microsoft.com/en-us/agent-framework/overview
[13] https://adk.dev/agents/models
[14] https://kiro.dev/docs
[15] https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/what-is.html
[17] https://docs.dify.ai/en/cloud/use-dify/workspace/model-providers
[18] https://docs.langflow.org/components-models
[19] https://learn.microsoft.com/en-us/microsoft-copilot-studio/fundamentals-what-is-copilot-studio
[20] https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork
[22] https://learn.chatgpt.com/docs/cloud
[23] https://ai-sdk.dev/docs/introduction
[24] https://github.com/RooCodeInc/Roo-Code
[25] https://docs.devin.ai/get-started/devin-intro
[26] https://docs.replit.com/features/agent/overview
[27] https://docs.lovable.dev/introduction/welcome
[28] https://support.bolt.new/get-started/intro-bolt
[29] https://support.google.com/gemini/answer/15235603?hl=en
[50] https://kiro.dev/docs/getting-started/authentication
[54] https://kiro.dev/docs/steering
[56] https://support.claude.com/en/articles/15036540-use-the-claude-agent-sdk-with-your-claude-plan
[57] https://code.claude.com/docs/en/agent-sdk/quickstart
[59] https://raw.githubusercontent.com/microsoft/autogen/main/README.md
[60] https://raw.githubusercontent.com/FlowiseAI/Flowise/main/README.md
[62] https://raw.githubusercontent.com/danny-avila/LibreChat/main/librechat.example.yaml
[63] https://raw.githubusercontent.com/github/copilot-sdk/main/README.md
[64] https://raw.githubusercontent.com/github/copilot-sdk/main/docs/auth/byok.md
[65] https://ai-sdk.dev/providers/openai-compatible-providers
[66] https://adk.dev/agents/models/litellm
[67] https://adk.dev/context/compaction
[69] https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatopenai
[70] https://raw.githubusercontent.com/langgenius/dify-official-plugins/main/models/openai_api_compatible/provider/openai_api_compatible.yaml
[71] https://support.claude.com/en/articles/9517075-what-are-projects
[72] https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-select-agent-model
[78] https://docs.openwebui.com/llms.txt
[82] https://learn.microsoft.com/en-us/agent-framework/integrations
[83] https://github.com/FlowiseAI/Flowise/discussions/6727
[85] https://code.claude.com/docs/en/claude-apps-gateway
[86] https://raw.githubusercontent.com/n8n-io/n8n/master/packages/@n8n/nodes-langchain/nodes/llms/LMChatOpenAi/LmChatOpenAi.node.ts
[87] https://docs.langchain.com/oss/python/langgraph/add-memory
[88] https://pydantic.dev/docs/ai/core-concepts/message-history
[89] https://docs.crewai.com/v1.15.20/en/concepts/agents
[90] https://ai-sdk.dev/docs/agents/loop-control
[91] https://help.openai.com/en/articles/10169521-projects-in-chatgpt
[92] https://docs.openwebui.com/getting-started/quick-start/connect-a-provider/starting-with-openai-compatible
[93] https://docs.openwebui.com/features/chat-conversations/chat-features/subagents
[94] https://mastra.ai/models.md
[95] https://mastra.ai/docs/agents/processors.md
[96] https://docs.agno.com/features/sdk.md
[97] https://raw.githubusercontent.com/agno-agi/agno/main/README.md
[98] https://raw.githubusercontent.com/agno-agi/agno/main/libs/agno/agno/models/openai/chat.py
[99] https://kiro.dev/docs/custom-agents/subagents.md
[101] https://kiro.dev/docs/cli/headless.md
[102] https://raw.githubusercontent.com/n8n-io/n8n/master/packages/nodes-base/credentials/OpenAiApi.credentials.ts
[103] https://docs.lovable.dev/tips-tricks/from-idea-to-app
[104] https://docs.lovable.dev/introduction/credits-and-usage
[105] https://support.bolt.new/account-and-subscription/tokens
[108] https://raw.githubusercontent.com/diegosouzapw/OmniRoute/main/README.md
[109] https://learn.chatgpt.com/docs/app.md
[110] https://learn.chatgpt.com/docs/auth.md
[112] https://code.claude.com/docs/en/agent-sdk/subagents
[113] https://openai.github.io/openai-agents-python/handoffs
[114] https://mastra.ai/docs/subagents.md
[115] https://kiro.dev/docs/upgrade-guides/migrating-from-q
[116] https://docs.replit.com/billing/ai-billing
[117] https://raw.githubusercontent.com/microsoft/agent-framework/main/python/packages/openai/agent_framework_openai/_chat_client.py
