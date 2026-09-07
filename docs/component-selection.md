# Component selection

Choose a capability, not a bundle. None of the optional or experimental entries is required to use this blueprint. Start with the current approved harness and [the native baseline](#native-baseline). Read [Evidence](evidence.md) before interpreting any percentage.

## Route-aware decision

1. Identify the actual harness/version, native login or API/cloud route, billing owner, selected model, effort and permissions. Keep them unchanged unless separately approved.
2. Name the waste: repeated discovery, excessive source data, repeated deterministic work, noisy output, avoidable generated code, obsolete history, price or lack of accounting.
3. Check the built-in that already owns it. Do not credit native caching, compaction or tool discovery again.
4. Choose one owner for each surface. A gateway may transport a request while an explicit tool shapes its own result, but two reducers must not independently compress that same result.
5. State the coverage contract. Exact lookup, computation over every row, semantic review of every record and exploratory top-k search are different tasks.
6. Snapshot only the configuration being changed, retain exact source artifacts and record how to bypass the choice. Do not install automatically or modify a shared global profile.
7. Try one complete representative task, verify requirements and permissions, count the entire trajectory and revert on a failure. A small pilot is a screening decision, not a population savings claim.

## Optional delegation and OmniRoute

Use [host-native delegation](delegation.md) before adding another orchestrator. The [restricted OmniRoute add-on](addons/omniroute.md) is now an explicit optional method, not a blanket exclusion. It has source-level compression candidates and concrete activation gates; it is not a universal safe preset or a promised extra percentage. Keeping the main native subscription outside a new proxy is our initial rollout recommendation. OAuth-capable gateways and CLI-owned bridges exist; evaluate the exact provider-specific capability, terms and account independently. [Free-provider choices](addons/free-provider-lanes.md) are a separate account/data/cost decision.

## Fast choice by situation

| Situation | First choice | Add only for a demonstrated gap |
| --- | --- | --- |
| Native subscription coding | Native search, map/edit tools and complete coding discipline | Serena for missing navigation; narrowly explicit RTK for noisy commands |
| Repeated document search | Existing lexical search and retained source spans | QMD for a local recurring collection; existing LlamaIndex or Haystack for an application |
| All rows, totals or joins | Existing permitted Python/SQL over complete data | DuckDB if the existing engine is insufficient; not a semantic compressor |
| Repeated unchanged work | Verified exact artifact/result reuse | Existing gateway exact cache for suitable static API requests |
| Regular table text | Compact JSON or typed CSV | TOON only if round-trip and target-token checks win |
| Very long sessions | Native history/compaction and explicit saved progress | One supported, consented history method; otherwise no new history reducer |
| API governance or cost visibility | Existing gateway and provider receipts | One of LiteLLM, Bifrost, Portkey, Helicone or Cloudflare after edition/route review |
| Price pressure rather than tokens | Understand the actual bill and quota | Approved batch pricing or a separately authorized model-router experiment |

The entries below describe adoption feasibility, not tested installers. Use the upstream instructions for the exact pinned version; package names and hook APIs are not interchangeable across harnesses. Scope changes to a project or isolated trial, verify effective state, and keep original settings. No command here requires a new account, CA certificate or subscription broker.

## Core methods and optional components

<a id="native-baseline"></a>
### Existing harness and provider built-ins

Keep the current model, effort, native login, permissions, compaction, tool discovery and cache as the comparator. No optimizer installation is required. [118][31]

Control and best fit: Native context assembly, tool discovery and provider billing. Every task. Marginal mechanism: Avoid unnecessary schema loading; native caching discounts repeated prefixes rather than removing logical input tokens.

Adopt, verify, revert: Inventory effective route and built-ins before changing anything. Keep a settings snapshot; restore only changed project/session settings. Never rewrite opaque provider state.

Gates: Provider terms and the chosen harness license apply; no subscription credential redistribution. Evidence limit: First-party documentation and prior pinned harness-source inspection. No authenticated cross-harness smoke test in this scan.[31][23][33]

<a id="source-scoped-reads"></a>
### Focused reads and exact coverage

Start with exact filenames, IDs, source-side fields and relevant spans, not a new vector database. Full-reading and all-record requirements override top-k selection. [147][209]

Control and best fit: Source query and explicit read-tool inputs. Known-document lookup, repository exploration, research. Marginal mechanism: Less irrelevant material enters context and fewer repeated searches occur.

Adopt, verify, revert: Use existing read/search tools. Preserve source versions, qualifiers and coverage. Widen or restore full sources on missing evidence; remove optional search guidance to revert.

Gates: Use existing permitted tools. ripgrep is dual MIT/Unlicense. Evidence limit: Source/README inspection of lexical search; method recommendation, not a measured task-saving estimate.[147][209]

<a id="deterministic-execution"></a>
### Deterministic data execution

Parse, paginate, join, count, deduplicate and generate requested artifacts with existing code or SQL; ask the model to interpret verified results. [218][217]

Control and best fit: Native approved execution tool or source database. Spreadsheets, paginated APIs, finance calculations, report generation. Marginal mechanism: Avoid serial model-mediated row handling and repeated generation of unchanged data.

Adopt, verify, revert: Use read-only snapshots first. Reconcile page and row counts, nulls, multiplicity and totals; retain source and output artifacts. Revert to the existing query/script. Never replay external writes.

Gates: Existing runtime terms; SQLite core is public domain; optional engines have separate dependencies. Evidence limit: Official SQL documentation and native code-execution documentation; no savings benchmark run here.[218][217][119]

<a id="exact-reuse"></a>
### Versioned exact reuse

Reuse a verified read or deterministic result only when parameters, source versions, freshness and current authorization match. Matching question text alone is insufficient. [212][200]

Control and best fit: Application read cache, artifact store or unchanged source snapshot. Recurring reports, stable transformations, unchanged repository reads. Marginal mechanism: Avoid an entire redundant tool/model operation on valid hits; lookup and invalidation still cost work.

Adopt, verify, revert: Reuse existing artifacts keyed by exact dependencies and principal. On corrections, revocation or refresh, invalidate and reread. Disable cache to revert; never cache permission or a write confirmation.

Gates: No new required library. Existing store and retention terms apply. Evidence limit: Method recommendation grounded in exact-cache implementation and provider documentation; no hit-rate promise.[212][200]

<a id="ponytail"></a>
### Ponytail-inspired complete coding discipline

Adapt reuse, native-feature-first and smallest-complete-change guidance, not upstream scope reduction or one-check limits. Preserve every required feature, security boundary and project test. [53][51]

Control and best fit: Task-scoped coding instructions, not model/provider routing. Feature delivery, fixes and refactors. Marginal mechanism: Less speculative code generation and repeated deliberation or scaffolding.

Adopt, verify, revert: Load short adapted rules only for the coding task. Verify full acceptance and existing tests; remove the added rules to revert. Do not auto-install the upstream full/ultra plugin.

Gates: MIT upstream; independently written guidance here, no copied skill text. Evidence limit: Author real-agent benchmark: 12 features, Haiku 4.5, four runs per arm; 22% reported token reduction. Feature functionality was not fully exercised.[53][51][46]

<a id="aider"></a>
### Aider repository maps and native edit formats

For existing Aider users, keep its map and model-appropriate patch format. Do not install a second map simply to duplicate the overview. [3][2]

Control and best fit: Existing harness repository map and edit format. Unknown code architecture and focused changes. Marginal mechanism: A ranked structural map replaces whole-repository dumps; patches avoid regenerating unchanged files.

Adopt, verify, revert: Use native settings and existing map. Read full edit targets and callers; restore the prior map/edit setting if navigation or patch retries regress.

Gates: Apache-2.0 code; tree-sitter grammars and model-provider access are separate. Evidence limit: Official docs and repomap source: graph ranking under a token budget, with omissions and dynamic expansion. No incremental whole-task percentage claimed.[2][262][208]

<a id="rtk"></a>
### RTK

Use explicit, narrowly selected repetitive command filters only when the native output is still noisy. Never filter complete diffs or forensic records by default. [105][111]

Control and best fit: Explicit shell wrapper; automatic input rewrites depend on the harness adapter. Repetitive test/build/status output. Marginal mechanism: Remove progress and repeated output before subsequent model ingestion.

Adopt, verify, revert: Pilot explicit invocations in one project, retain raw stdout/stderr and exit code independently. Bypass RTK to revert. Its bounded tee is not a durable archive; never rerun a write for raw output.

Gates: Apache-2.0; check chosen release binary and dependencies. Evidence limit: README, tee/tracking source and benchmark inspection. Up to 90% concerns eligible Bash output; the inspected counter estimates bytes/4, not provider receipts.[111][112][104]

<a id="serena"></a>
### Serena

Add only if the current harness lacks healthy symbol navigation. Native diagnostics alone are not equivalent to definition/reference lookup. [133][134]

Control and best fit: Per-project MCP symbol lookup and edit tools. Cross-file coding and references. Marginal mechanism: Retrieve relevant symbols rather than repeatedly reading entire files.

Adopt, verify, revert: Use a scoped stdio server and required language server; inspect read/edit permissions. Remove its MCP registration and stop its process to revert; code edits still need normal review.

Gates: MIT core; language-server licenses/downloads and optional paid JetBrains backend require separate checks. Evidence limit: README, running guide and symbol-tools source inspected; no task-wide savings benchmark reproduced.[134][263][102]

<a id="toon"></a>
### TOON

Compare against compact JSON and typed CSV before selecting TOON for regular records. Keep actual protocol schemas and signed payloads unchanged. [266][137]

Control and best fit: Explicit model-visible data serialization. Uniform JSON arrays and repetitive keyed records. Marginal mechanism: Share field names instead of repeating them per record.

Adopt, verify, revert: Encode a retained copy, round-trip types/nulls/IDs/order and count the target tokenizer plus format instructions. Revert by returning the original compact JSON.

Gates: MIT; validate runtime numeric precision and chosen encoder dependencies. Evidence limit: Encoder source and author retrieval benchmark: 244 questions across four models; about 14.45% fewer format tokens than compact JSON, not full-task savings.[137][267][114]

<a id="qmd"></a>
### QMD by tobi

A practical local index for recurring notes/docs when lexical search is insufficient; not a replacement for a required full read. [178][179]

Control and best fit: Local CLI or scoped MCP index; lexical, vector and reranking modes. Repeated search across a permitted documentation collection. Marginal mechanism: Reuse an index and retrieve exact relevant spans instead of resending a corpus; neural stages add local compute.

Adopt, verify, revert: Start lexical-only on a small explicit collection. Check exclusions, stale entries and retrieval counts; multi_get has size limits. Remove the MCP entry and index configuration to revert, retaining original files. Avoid unauthenticated shared HTTP.

Gates: MIT code. Node/Bun and node-llama-cpp dependencies; GGUF embedding/reranking/expansion weights need their own terms and download approval. Evidence limit: README and MCP/store source inspected. Bench fixtures exist; no independently reproduced whole-task saving for this repository.[179][180][181]

<a id="llamaindex"></a>
### LlamaIndex

Use when it is already the application’s retrieval owner or real connectors/pipelines are needed; not a mandatory agent install. [184][185]

Control and best fit: Application retriever, node selection, metadata filters and reranking. Existing RAG applications with governed sources. Marginal mechanism: Return fewer irrelevant chunks; persistent indices avoid repeated ingestion.

Adopt, verify, revert: In a project environment, select core and only required integrations; explicitly select the existing model and embedder. Test ACL/freshness/answer-span recall, then restore the prior pipeline to revert.

Gates: MIT core; separately licensed integrations, embedding weights, parsers and paid LlamaCloud services. Evidence limit: README plus BM25 retriever/query-engine source inspected. Top-k and metadata filters exist; framework support does not establish recall or savings.[184][185][187]

<a id="haystack"></a>
### Haystack

Alternative to LlamaIndex for an existing application, not an additional retrieval layer. [188][189]

Control and best fit: Retrieval/ranking/pipeline components and approved application tools. RAG, document processing and existing Python pipelines. Marginal mechanism: Source filtering and retrieval selection can reduce irrelevant input; repeated indexing has overhead.

Adopt, verify, revert: Pilot a project-local pipeline with fixed source and authorization constraints; test filter replacement and telemetry policy. Restore the previous pipeline/config to revert.

Gates: Apache-2.0 core; integration/model terms and commercial Enterprise Platform are separate; review documented telemetry. Evidence limit: README and BM25 source inspected. Runtime filters default to replacing initialization filters; no default tenant-boundary guarantee.[188][189][190]

<a id="duckdb"></a>
### DuckDB

Choose only when existing Python/SQL tools do not comfortably handle the local analytical data; do not add a model to calculate totals. [144][145]

Control and best fit: Local analytical SQL over authorized source files. Large CSV/Parquet joins, aggregates and reports. Marginal mechanism: Model sees verified results and exceptions, not every row repeatedly.

Adopt, verify, revert: Use a scoped environment and read-only input copies; declare types and reconcile full row counts. Revert to the former query/script and retain original datasets.

Gates: MIT core; extensions and remote-file access need separate approval. Evidence limit: Official SQL docs and repository/license inspected; no LLM token benchmark or installed-engine trial here.[144][145][218]

<a id="tiktoken"></a>
### tiktoken

Useful for eligible OpenAI text encodings; provider usage receipts remain authoritative for billing and full requests. [206][207]

Control and best fit: Offline tokenizer for a specified text payload. Comparing compact encodings and eligible output filters. Marginal mechanism: Does not save tokens itself; rejects transformations that only reduce bytes.

Adopt, verify, revert: Use the encoding for the actual model and count explanatory overhead. Stop using the comparator or remove the local dependency to revert; do not report text counts as complete multimodal billing.

Gates: MIT code; verify the exact encoding/model mapping. Evidence limit: Tokenizer API/source inspected, not an arbitrary-provider metering standard.[206][207][205]

<a id="ccusage"></a>
### ccusage by ryoppippi

Use supported local logs to inspect task/session totals before adding a proxy. Dollar columns may be API-equivalent estimates, not subscription charges. [191][192]

Control and best fit: Read-only analysis of supported local usage logs. Native subscription and API coding-session accounting. Marginal mechanism: No direct reduction; reveals repeated work, cached input and expensive trajectories.

Adopt, verify, revert: Choose the correct adapter, time window and cost mode; reconcile sample events to logs and the provider account. Remove the optional reader to revert; retain original logs.

Gates: MIT app license; root LICENSE is a pointer, not the full grant. Inspect the selected package and log access. Evidence limit: Current README, cost-mode docs and Rust cost implementation inspected. Display mode uses zero for absent cost; absence is not evidence of free usage.[192][268][269]

<a id="headroom"></a>
### Headroom

Specialist option for a controlled application or explicit tool boundary, not the default transparent proxy. Disable effort routing and reject sampling for exhaustive work. [73][80]

Control and best fit: SDK transformation, MCP tool or optional gateway; exact capabilities depend on configuration. Repetitive logs, structured observations and exploration. Marginal mechanism: Select/encode observations before model input; sample-based paths are lossy and restore costs matter.

Adopt, verify, revert: Prefer an explicit eligible new-output path. Verify raw recovery, no effort changes, telemetry and unchanged endpoint. Bypass that transform to revert; proxy trials require restoring original provider settings too.

Gates: Apache-2.0 core with notices; optional dependency and model-weight closure requires review. Evidence limit: README, SmartCrusher source, limitations and four-scenario seeded payload artifact inspected. Tool-content tokens only, not complete task quality.[77][75][72]

<a id="context-mode"></a>
### context-mode

Optional user-installed execution/indexing tool when built-ins are inadequate. Offloading is not proof that the agent reviewed omitted content. [85][88]

Control and best fit: Explicit execution/search MCP tools; lifecycle hooks vary by harness. Large tool outputs and searchable session material. Marginal mechanism: Keep bulk execution/index contents outside the prompt, returning results or selected spans.

Adopt, verify, revert: Scope the instance and verify execution permissions, retention and restart recovery. Remove its MCP/hooks and restore raw tools to revert; export needed evidence before session cleanup.

Gates: Elastic License 2.0 source available; substantial hosted/managed-service use needs separate permission. Not a permissive managed-service dependency. Evidence limit: README/license, Codex hook and v0.4 benchmark artifact inspected. 198337 to 12609 bytes over 13 examples; retrieval receipts are not finished answers.[88][84][86]

<a id="litellm"></a>
### LiteLLM

Consider for an existing approved API application needing central metering, budgets or routing. For this initial API-governance recommendation, leave existing native subscription routes unchanged; provider-specific OAuth support and permission must be assessed separately. [129][130]

Control and best fit: Approved application endpoint/SDK and optionally request logging. Teams already operating API applications. Marginal mechanism: Budgets prevent unintended work; exact hits can avoid inference; cheaper routing changes price, not inherently token count.

Adopt, verify, revert: Reuse the existing gateway if any. Snapshot endpoint/model/auth mapping, disable unapproved fallbacks and semantic cache, test tools/streaming/usage and privacy. Restore original endpoint and revoke trial keys to revert.

Gates: MIT outside enterprise; audited proxy extra includes litellm-enterprise. Commercial terms and exact dependency closure are separate. Evidence limit: README, license and pyproject inspected; gateway/provider support and accounting, not a universal token-reduction benchmark.[130][264][265]

<a id="bifrost"></a>
### Bifrost

Consider for an existing approved API application needing central metering, budgets or routing. For this initial API-governance recommendation, leave existing native subscription routes unchanged; provider-specific OAuth support and permission must be assessed separately. [131][132]

Control and best fit: Approved application endpoint/SDK and optionally request logging. Teams already operating API applications. Marginal mechanism: Budgets prevent unintended work; exact hits can avoid inference; cheaper routing changes price, not inherently token count.

Adopt, verify, revert: Reuse the existing gateway if any. Snapshot endpoint/model/auth mapping, disable unapproved fallbacks and semantic cache, test tools/streaming/usage and privacy. Restore original endpoint and revoke trial keys to revert.

Gates: Apache-2.0 core; enterprise features and third-party notices/dependency obligations remain separate. Evidence limit: README and retained pinned license/dependency evidence inspected; throughput claims measure gateway overhead, not tokens saved.[131][132]

<a id="portkey"></a>
### Portkey AI Gateway

Consider for an existing approved API application needing central metering, budgets or routing. For this initial API-governance recommendation, leave existing native subscription routes unchanged; provider-specific OAuth support and permission must be assessed separately. [194][195]

Control and best fit: Approved application endpoint/SDK and optionally request logging. Teams already operating API applications. Marginal mechanism: Budgets prevent unintended work; exact hits can avoid inference; cheaper routing changes price, not inherently token count.

Adopt, verify, revert: Reuse the existing gateway if any. Snapshot endpoint/model/auth mapping, disable unapproved fallbacks and semantic cache, test tools/streaming/usage and privacy. Restore original endpoint and revoke trial keys to revert.

Gates: MIT gateway code; hosted and enterprise governance are commercial products. Evidence limit: README, cache cookbook and middleware source inspected; simple and semantic cache are different policies.[195][196][197]

<a id="helicone"></a>
### Helicone

Consider for an existing approved API application needing central metering, budgets or routing. For this initial API-governance recommendation, leave existing native subscription routes unchanged; provider-specific OAuth support and permission must be assessed separately. [154][155]

Control and best fit: Approved application endpoint/SDK and optionally request logging. Teams already operating API applications. Marginal mechanism: Budgets prevent unintended work; exact hits can avoid inference; cheaper routing changes price, not inherently token count.

Adopt, verify, revert: Reuse the existing gateway if any. Snapshot endpoint/model/auth mapping, disable unapproved fallbacks and semantic cache, test tools/streaming/usage and privacy. Restore original endpoint and revoke trial keys to revert.

Gates: Apache-2.0 repository; hosted gateway/observability and enterprise deployment terms are separate. Evidence limit: README and license inspected; trace/cost visibility is not a measured reduction. Async logging is an alternative to proxy insertion.[154][155]

<a id="cloudflare-ai-gateway"></a>
### Cloudflare AI Gateway

A managed option for approved API workloads, especially repeated static requests. Do not replace the existing route solely for a cache checkbox. [212]

Control and best fit: Approved gateway request cache and account settings. Static repeated API requests. Marginal mechanism: A valid exact hit avoids a provider call; native prefix caching does not.

Adopt, verify, revert: Scope one approved app, set retention/freshness and preserve key isolation. Verify HIT/MISS plus a changed-source MISS. Disable caching, purge relevant entries and restore direct endpoint to revert.

Gates: Hosted service terms and pricing apply; not an OSS license grant. Evidence limit: Official caching docs inspected: default key includes provider, endpoint, model, auth header and full request body; HIT/MISS is observable.[212]

<a id="provider-batch"></a>
### Provider Batch APIs

For eligible asynchronous API work already approved for delayed execution. Keep selected models and exact work; this is not token compression. [216]

Control and best fit: Native provider asynchronous request scheduling. Nonurgent independent extraction or classification jobs. Marginal mechanism: Lower price per eligible token; may reduce orchestration overhead, but no inherent token cut.

Adopt, verify, revert: Use existing batch tooling with explicit request IDs, result/error reconciliation and no duplicate writes. Stop submitting new batches; reconcile in-flight jobs before returning to synchronous requests.

Gates: Provider API agreement and data-retention rules, separate from consumer subscription seats. Evidence limit: OpenAI first-party Batch guide: 50% lower API cost for eligible batch processing with a 24-hour turnaround; not fewer logical tokens.[216]

## Optional experimental shelf

These are not required installations. A paper is permission to investigate a method, not permission to rewrite a native session or use its weights. The catalog contains the detailed gate and rollback for each entry.

| Surface | Candidates | Decision before a trial |
| --- | --- | --- |
| Learned new-observation compression | LLMLingua, Kompress, SWE-Pruner | Explicit helper/weight approval, exact protected spans, latency/privacy cost, full-body restoration before edits |
| History reduction | AgentDiet, ACON, observation masking, OpenCode DCP | Supported host seam, protected current state, cache accounting and one history owner; no universal turn window |
| Compression evaluation | TRACE | Restore equivalent executable state and test continuations; boundary success is not whole-task success |
| Local context wrappers | The three distinct LeanCTX projects, Paritok | Do not mix identities; inspect the particular installer, output surface, dependencies and overlapping owners |
| Managed compression | The Token Company, Compresr | Data-processing agreement, pricing, retention, exact endpoint, agreed allowed data and measured net benefit |
| Semantic answer reuse | GPTCache, vCache | Static low-risk scope, current authorization/freshness and explicit false-hit tolerance; never permission or live-state reuse |
| Reasoning/program optimization | TALE, DSPy, RLM | Separate cost for tuning/helpers, supported execution controls and complete quality checks; no concealed effort/model switch |
| Model-price routing | RouteLLM | Separately approved model pair and quality contract; report price changes apart from token changes |

## Overlap rules that prevent false savings

1. Native harness owns provider history, opaque reasoning, compaction items, authentication and approvals unless its documented extension seam explicitly permits a narrower operation.
2. Retrieval has one primary index/pipeline per corpus. Exact lexical lookup may complement semantic discovery; a second full index usually duplicates ingestion and governance.
3. A command handled by RTK is not also summarized by Headroom, context-mode and a gateway. Return to the retained original before changing the selected representation.
4. TOON applies to eligible data, never actual tool-call schemas, encrypted state or signed bytes. A compact encoding is not a reason to let the model do arithmetic.
5. A semantic answer cache is not an exact cache, and neither is a provider prefix cache. Never count their benefits as interchangeable.
6. Retain user corrections, conditions, negation, exact identifiers/units, errors, pending permissions, requested coverage and test requirements. A pointer is not the completed answer; model confidence is not proof that nothing important was removed.
7. Cold cache, helpers, retries, restores, additional tool turns, storage and human rework count. If the task is short, dense or already optimized, doing nothing can be the correct choice.

## Revert means recover the route and the work

Removing a plugin does not reverse code edits or external actions. Preserve completed valid artifacts and action receipts; never replay a write to reconstruct output. For a local tool, remove only its own registration/configuration and return to native tools. For an API trial, restore the exact former endpoint, model mapping and authentication route, remove trial-only credentials and verify a fresh read-only request through the former route. For a cache or index, disable it first and preserve original documents; delete derived data only under the agreed retention policy.

A monthly subscription fee does not fall because fewer tokens were used. Report observed task capacity or quota behavior only when legitimate telemetry supports it. API-equivalent prices are useful comparisons, not money recovered from a subscription invoice.

## Sources

[2] https://aider.chat/docs/more/edit-formats.html
[3] https://aider.chat/docs/repomap.html
[23] https://code.claude.com/docs/en/legal-and-compliance
[31] https://developers.openai.com/api/docs/guides/prompt-caching
[33] https://developers.openai.com/codex/auth
[46] https://raw.githubusercontent.com/DietrichGebert/ponytail/974d940a1c5344210874150b98ff0d2c861fab6a/LICENSE
[51] https://raw.githubusercontent.com/DietrichGebert/ponytail/974d940a1c5344210874150b98ff0d2c861fab6a/benchmarks/results/2026-06-18-agentic.md
[53] https://raw.githubusercontent.com/DietrichGebert/ponytail/974d940a1c5344210874150b98ff0d2c861fab6a/skills/ponytail/SKILL.md
[72] https://raw.githubusercontent.com/headroomlabs-ai/headroom/e67b3c8a29443a60d6b0018fb22f525c5cd7e709/LICENSE
[73] https://raw.githubusercontent.com/headroomlabs-ai/headroom/e67b3c8a29443a60d6b0018fb22f525c5cd7e709/README.md
[75] https://raw.githubusercontent.com/headroomlabs-ai/headroom/e67b3c8a29443a60d6b0018fb22f525c5cd7e709/benchmarks/results/index_proof_table.txt
[77] https://raw.githubusercontent.com/headroomlabs-ai/headroom/e67b3c8a29443a60d6b0018fb22f525c5cd7e709/docs/content/docs/limitations.mdx
[80] https://raw.githubusercontent.com/headroomlabs-ai/headroom/e67b3c8a29443a60d6b0018fb22f525c5cd7e709/headroom/transforms/smart_crusher.py
[84] https://raw.githubusercontent.com/mksglu/context-mode/aded72c62372515518994153c470344f1b7d81a1/LICENSE
[85] https://raw.githubusercontent.com/mksglu/context-mode/aded72c62372515518994153c470344f1b7d81a1/README.md
[86] https://raw.githubusercontent.com/mksglu/context-mode/aded72c62372515518994153c470344f1b7d81a1/hooks/codex/posttooluse.mjs
[88] https://raw.githubusercontent.com/mksglu/context-mode/aded72c62372515518994153c470344f1b7d81a1/tests/benchmark-results-v04.json
[102] https://raw.githubusercontent.com/oraios/serena/13ac8c5b1d51873bd148aea440dcb22f85d3a439/docs/02-usage/020_running.md
[104] https://raw.githubusercontent.com/rtk-ai/rtk/e53ec1cf180d801f33121855dce37b393ede258c/LICENSE
[105] https://raw.githubusercontent.com/rtk-ai/rtk/e53ec1cf180d801f33121855dce37b393ede258c/README.md
[111] https://raw.githubusercontent.com/rtk-ai/rtk/e53ec1cf180d801f33121855dce37b393ede258c/src/core/tee.rs
[112] https://raw.githubusercontent.com/rtk-ai/rtk/e53ec1cf180d801f33121855dce37b393ede258c/src/core/tracking.rs
[114] https://raw.githubusercontent.com/toon-format/toon/f151a5d830d001bc244395b891183cba37e0d935/benchmarks/results/retrieval-accuracy.md
[118] https://www.anthropic.com/engineering/advanced-tool-use
[119] https://www.anthropic.com/engineering/code-execution-with-mcp
[129] https://raw.githubusercontent.com/BerriAI/litellm/litellm_internal_staging/README.md
[130] https://raw.githubusercontent.com/BerriAI/litellm/litellm_internal_staging/LICENSE
[131] https://raw.githubusercontent.com/maximhq/bifrost/dev/README.md
[132] https://raw.githubusercontent.com/maximhq/bifrost/dev/LICENSE
[133] https://raw.githubusercontent.com/oraios/serena/main/README.md
[134] https://raw.githubusercontent.com/oraios/serena/main/LICENSE
[137] https://raw.githubusercontent.com/toon-format/toon/main/LICENSE
[144] https://raw.githubusercontent.com/duckdb/duckdb/v2.0-cyanoptera/README.md
[145] https://raw.githubusercontent.com/duckdb/duckdb/v2.0-cyanoptera/LICENSE
[147] https://raw.githubusercontent.com/BurntSushi/ripgrep/master/README.md
[154] https://raw.githubusercontent.com/Helicone/helicone/main/README.md
[155] https://raw.githubusercontent.com/Helicone/helicone/main/LICENSE
[178] https://raw.githubusercontent.com/tobi/qmd/dbfd0b4736aeaf761d1a16ca8e424f071df8feb9/README.md
[179] https://raw.githubusercontent.com/tobi/qmd/dbfd0b4736aeaf761d1a16ca8e424f071df8feb9/LICENSE
[180] https://raw.githubusercontent.com/tobi/qmd/dbfd0b4736aeaf761d1a16ca8e424f071df8feb9/src/mcp/server.ts
[181] https://raw.githubusercontent.com/tobi/qmd/dbfd0b4736aeaf761d1a16ca8e424f071df8feb9/src/store.ts
[184] https://raw.githubusercontent.com/run-llama/llama_index/d2ac544a27c73d2a68e9c57efec4b2ac0ef99892/README.md
[185] https://raw.githubusercontent.com/run-llama/llama_index/d2ac544a27c73d2a68e9c57efec4b2ac0ef99892/LICENSE
[187] https://raw.githubusercontent.com/run-llama/llama_index/d2ac544a27c73d2a68e9c57efec4b2ac0ef99892/llama-index-integrations/retrievers/llama-index-retrievers-bm25/llama_index/retrievers/bm25/base.py
[188] https://raw.githubusercontent.com/deepset-ai/haystack/82da3adc2fac4675b80ff5573b790ec07113697b/README.md
[189] https://raw.githubusercontent.com/deepset-ai/haystack/82da3adc2fac4675b80ff5573b790ec07113697b/LICENSE
[190] https://raw.githubusercontent.com/deepset-ai/haystack/82da3adc2fac4675b80ff5573b790ec07113697b/haystack/components/retrievers/in_memory/bm25_retriever.py
[191] https://raw.githubusercontent.com/ryoppippi/ccusage/2defd5550b9e4a26c0f4d4f175fc1508ca16fbc3/apps/ccusage/README.md
[192] https://raw.githubusercontent.com/ryoppippi/ccusage/2defd5550b9e4a26c0f4d4f175fc1508ca16fbc3/apps/ccusage/LICENSE
[194] https://raw.githubusercontent.com/Portkey-AI/gateway/669825cbe89ee51569918b8f78a9db486fd69dd4/README.md
[195] https://raw.githubusercontent.com/Portkey-AI/gateway/669825cbe89ee51569918b8f78a9db486fd69dd4/LICENSE
[196] https://raw.githubusercontent.com/Portkey-AI/gateway/669825cbe89ee51569918b8f78a9db486fd69dd4/src/middlewares/cache/index.ts
[197] https://raw.githubusercontent.com/Portkey-AI/gateway/669825cbe89ee51569918b8f78a9db486fd69dd4/cookbook/getting-started/enable-cache.md
[200] https://raw.githubusercontent.com/zilliztech/GPTCache/c59fb3a6152a4458b2a070ca183b61c4b614095f/gptcache/similarity_evaluation/exact_match.py
[205] https://raw.githubusercontent.com/openai/tiktoken/4e71bbe0c078468e00fefbf94b39849389f346e5/tiktoken/core.py
[206] https://raw.githubusercontent.com/openai/tiktoken/4e71bbe0c078468e00fefbf94b39849389f346e5/README.md
[207] https://raw.githubusercontent.com/openai/tiktoken/4e71bbe0c078468e00fefbf94b39849389f346e5/LICENSE
[208] https://raw.githubusercontent.com/Aider-AI/aider/main/LICENSE.txt
[209] https://raw.githubusercontent.com/BurntSushi/ripgrep/master/COPYING
[212] https://developers.cloudflare.com/ai-gateway/features/caching
[216] https://developers.openai.com/api/docs/guides/batch
[217] https://www.sqlite.org/copyright.html
[218] https://duckdb.org/docs/stable/sql/query_syntax/select.html
[262] https://raw.githubusercontent.com/Aider-AI/aider/main/aider/repomap.py
[263] https://raw.githubusercontent.com/oraios/serena/main/src/serena/tools/symbol_tools.py
[264] https://raw.githubusercontent.com/BerriAI/litellm/litellm_internal_staging/pyproject.toml
[265] https://raw.githubusercontent.com/BerriAI/litellm/litellm_internal_staging/enterprise/LICENSE.md
[266] https://raw.githubusercontent.com/toon-format/toon/main/packages/toon/README.md
[267] https://raw.githubusercontent.com/toon-format/toon/main/packages/toon/src/encode/encoders.ts
[268] https://raw.githubusercontent.com/ryoppippi/ccusage/2defd5550b9e4a26c0f4d4f175fc1508ca16fbc3/rust/crates/ccusage-core/src/cost.rs
[269] https://raw.githubusercontent.com/ryoppippi/ccusage/2defd5550b9e4a26c0f4d4f175fc1508ca16fbc3/docs/guide/cost-modes.md
