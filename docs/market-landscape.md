# Market landscape

Checked 2026-09-06 (UTC). This is a blueprint for choosing and using existing capabilities, not a new optimizer, proxy or agent runtime.

## The practical conclusion

Start with the current harness, model, effort and legitimate billing route. Remove repeated work, retrieve the right evidence and use deterministic execution before adding a compressor. Add an optional component only where a specific control surface is still missing. The [component selection guide](component-selection.md) turns that decision into an adoption and rollback checklist.

The market already contains tool-output reducers, context managers, repository navigation, retrieval frameworks, caches, trained compressors, gateways and usage readers. Headroom, LeanCTX and context-mode already combine several of these ideas. This repository does not claim to have invented context routing, reversible storage or complete-task measurement.[73][164][85]

Its useful contribution is a documented operating method: identify the route, keep one owner for each surface, prefer built-ins, preserve requirements and permissions, measure the marginal change, and undo an unsuccessful choice. That is a usability proposition, not a world-first or world-best claim. It should succeed without requiring readers to build middleware or install an entire catalog.

## What the scan covers

The scan reused retained primary-source research, then added current GitHub repository searches and web discovery across compression, retrieval/indexing, exact and semantic reuse, reasoning budgets, agent turns, data execution, commercial gateways and token accounting. It yielded 143 result records across 21 queries. Grouping GitHub subpages under their repository and normalizing other destinations produced 136 canonical source/repository destinations with 7 repeated occurrences. A literal URL comparison after trimming trailing slashes gives 139 distinct page URLs. These include project pages, documentation and secondary articles, not 136 fully audited repositories.

The [catalog](../catalog/market.json) contains 53 selected decision records: 6 core methods, 17 optional choices, 20 experimental references and 10 important exclusions. A method, vendor service and repository are different kinds of records. The [source catalog](../catalog/sources-market.json) identifies their supporting sources and evidence limits.

Representative GitHub queries were `token compression stars:>100`, `llm cache stars:>500`, `agent context retrieval stars:>500`, `llm gateway stars:>1000`, `token usage stars:>500` and `reasoning token budget`. Searches used the first page, at most 20 results, sorted by stars. Several had more hits than retrieved. Exact-name web queries supplemented these, including QMD, llmtrim and Compresr. Empty broad web searches were followed by simpler controls and direct primary-source access, not treated as proof that no project exists.

This is a bounded, category-based market scan, not a census of the Internet. English descriptions, search indexing, repository metadata and popularity sorting create selection bias. The scan did not test every release artifact, dependency or hosted edition. Default branches and live documentation can change after the check date.

## How candidates were selected

A core method must be usable through existing tools and preserve the task contract. An optional component must solve a concrete missing capability without becoming a new mandatory platform. An experimental entry has useful evidence or an interesting mechanism but unresolved quality, compatibility, rights or operational questions. An excluded entry is outside this blueprint’s recommended recipes, not necessarily a bad product.

Authority signals are explicit, not a numeric league table:

1. First-party documentation for the actual route, plus readable implementation and license files.
2. Released benchmark artifacts with a named baseline, task population, metric and quality outcome.
3. Maintained releases, tests, clear issue/recovery paths and deployment instructions.
4. Adoption and activity as screening context only. Where available, the catalog records dated GitHub stars, forks, creation and push dates; none proves security or correctness.
5. A feasible narrow trial, clear rollback and no conflict with provider contracts or protected data.

A published paper can justify studying a small project ahead of a popular wrapper. Conversely, a large star count does not clear a license, make a proxy preserve native state or turn a payload-size demo into a whole-task result. Evidence classes and exact denominators are in [Evidence](evidence.md).

## The market by control surface

### Work selection and agent turns

Ponytail addresses unnecessary coding rather than merely shortening answers. Aider already supplies repository maps and model-specific edit formats. The blueprint adopts the useful discipline while keeping complete scope and every required test; upstream brevity rules are not an authority to ship less.[53][3][2]

Research such as TALE changes reasoning budgets; DSPy optimizes application prompts/programs. These are separate experiments, not permission to lower the current effort invisibly. Fewer visible words do not prove fewer reasoning tokens or fewer retries.[7][174][51]

### Retrieval, indexing and code navigation

Use existing lexical/file tools first. Serena fills missing symbol navigation. QMD offers a local documentation index. LlamaIndex and Haystack are application frameworks when connectors and pipelines are genuinely needed. They are alternatives at the retrieval-owner level, not a recommended pile of installs.[133][178][184]

Haystack’s source demonstrates why retrieval needs an authorization review: runtime filters can replace initialization filters. QMD documents collection and size controls, but its HTTP endpoints are unauthenticated unless separately protected. Neither a filter name nor a local index proves tenant isolation or complete coverage.[190][178]

### Data execution and exact reuse

Existing Python/SQL, SQLite or optional DuckDB can do exact arithmetic and joins without feeding every intermediate row back to the model. An exact result cache can avoid a repeated operation altogether. These are often simpler interventions than a learned compressor, especially for operational reports.[218][217][212]

Do not confuse provider prefix caching, exact result reuse and semantic answer caching. GPTCache’s exact matcher compares question strings; a production reuse policy must additionally validate source versions, permissions and freshness. Its README also says new model/API adapters are no longer being added, an important maturity limit despite established adoption.[200][198][31]

### Observation shaping and compression

RTK is narrow command-output tooling. TOON is a representation choice. context-mode offers execution and offloading. Headroom offers SDK/MCP/proxy transforms, including lossy paths. These solve different problems, but can still process the same payload twice if installed indiscriminately.[105][85][80]

LLMLingua, Kompress and SWE-Pruner add learned compression. AgentDiet, ACON and observation masking address recurring history. Their positive results are conditional and accompanied by quality, helper-cost or cache effects. Treat them as specialist evidence, not a mandatory first install.[6][17][12]

### Commercial choices and price routing

LiteLLM, Bifrost, Portkey, Helicone and Cloudflare AI Gateway address API governance, observability, caching or routing. Reuse the customer’s approved gateway if it already covers the need. Open-source core licenses do not grant enterprise features, hosted contracts or provider-account rights. LiteLLM’s inspected proxy extra includes an enterprise package, so a blanket “MIT-only install” would be misleading.[264][194][212]

The Token Company and Compresr offer explicit hosted compression APIs. They deserve a procurement option for organizations that prefer managed operation, with a second data processor, contract and net-cost evaluation. Model weights are not made open by an SDK license. Vendor input-reduction or speed claims are not independent whole-task evidence.[213][214]

RouteLLM and provider Batch APIs can change price economics. Routing to a cheaper model does not inherently reduce tokens. Eligible Batch work trades immediate results for a different API rate; neither mechanism makes an unchanged native monthly subscription cheaper.[258][216]

### Accounting before another optimizer

Native usage receipts are the first choice. ccusage can read supported local logs; tiktoken can compare eligible OpenAI text representations. A dashboard, shorter byte count or API-equivalent dollar total is not a subscription invoice. Missing usage is unknown, not zero.[269][268][206]

## Important exclusions and identity traps

OmniRoute is not the default because its broader routing/broker features exceed the approved scope. llmtrim’s documented setup includes a private CA, shell changes and subscription routing, so its installer is excluded. This blueprint never needs a CA, pooled human seats, hidden fallback or a new provider to deliver its basic method.[176][166][23]

pxpipe’s own README discloses silent exact-string failures, so text-to-image conversion is not a recommended substitute for protected instructions, tool definitions or exact identifiers. LMCache changes inference-serving infrastructure, a surface that ordinary API/subscription clients do not own.[170][172]

Qdrant is excluded as a new mandatory dependency, not as a capable existing vector store. claw-compactor, opentoken, Blockify, squeez and TokenSkip remain searched exclusions with explicit review limits in the catalog. Their discovery descriptions are not endorsements or reproduced benchmarks.

“LeanCTX” is not one identity: `yvgude/lean-ctx` is an Apache-2.0 context toolkit, `jia-gao/leanctx` is an MIT Python compression wrapper, and `mirkobrombin/leanctx` is a separate MIT Go lexical compressor. The catalog preserves all three instead of merging incompatible capabilities or licenses.[165][161][163]

## What differentiation is defensible

The method is useful if a reader can make one good change without changing who bills them, which model does the work or what “done” means. It is not differentiated merely by listing more tools or multiplying their advertised percentages.

A successful recipe records the existing baseline, the missing surface, the selected owner, expected change, source/permission protections, observed outcome and a clean revert. Conservative work stops before introducing new lossy history transformations. Aggressive work adds only supported selective observation or checkpoint practices with protected state and tested restoration. If the harness has no supported seam, use explicit tools or stay native; do not invent an interception layer.

## Sources

[2] https://aider.chat/docs/more/edit-formats.html
[3] https://aider.chat/docs/repomap.html
[6] https://arxiv.org/html/2403.12968v2
[7] https://arxiv.org/html/2412.18547v5
[12] https://arxiv.org/html/2509.23586v2
[17] https://arxiv.org/html/2601.16746v4
[23] https://code.claude.com/docs/en/legal-and-compliance
[31] https://developers.openai.com/api/docs/guides/prompt-caching
[51] https://raw.githubusercontent.com/DietrichGebert/ponytail/974d940a1c5344210874150b98ff0d2c861fab6a/benchmarks/results/2026-06-18-agentic.md
[53] https://raw.githubusercontent.com/DietrichGebert/ponytail/974d940a1c5344210874150b98ff0d2c861fab6a/skills/ponytail/SKILL.md
[73] https://raw.githubusercontent.com/headroomlabs-ai/headroom/e67b3c8a29443a60d6b0018fb22f525c5cd7e709/README.md
[80] https://raw.githubusercontent.com/headroomlabs-ai/headroom/e67b3c8a29443a60d6b0018fb22f525c5cd7e709/headroom/transforms/smart_crusher.py
[85] https://raw.githubusercontent.com/mksglu/context-mode/aded72c62372515518994153c470344f1b7d81a1/README.md
[105] https://raw.githubusercontent.com/rtk-ai/rtk/e53ec1cf180d801f33121855dce37b393ede258c/README.md
[133] https://raw.githubusercontent.com/oraios/serena/main/README.md
[161] https://raw.githubusercontent.com/jia-gao/leanctx/main/LICENSE
[163] https://raw.githubusercontent.com/mirkobrombin/leanctx/master/LICENSE
[164] https://raw.githubusercontent.com/yvgude/lean-ctx/main/README.md
[165] https://raw.githubusercontent.com/yvgude/lean-ctx/main/LICENSE
[166] https://raw.githubusercontent.com/fkiene/llmtrim/main/README.md
[170] https://raw.githubusercontent.com/teamchong/pxpipe/main/README.md
[172] https://raw.githubusercontent.com/LMCache/LMCache/dev/README.md
[174] https://raw.githubusercontent.com/stanfordnlp/dspy/main/README.md
[176] https://raw.githubusercontent.com/diegosouzapw/OmniRoute/release/v3.8.51/README.md
[178] https://raw.githubusercontent.com/tobi/qmd/dbfd0b4736aeaf761d1a16ca8e424f071df8feb9/README.md
[184] https://raw.githubusercontent.com/run-llama/llama_index/d2ac544a27c73d2a68e9c57efec4b2ac0ef99892/README.md
[190] https://raw.githubusercontent.com/deepset-ai/haystack/82da3adc2fac4675b80ff5573b790ec07113697b/haystack/components/retrievers/in_memory/bm25_retriever.py
[194] https://raw.githubusercontent.com/Portkey-AI/gateway/669825cbe89ee51569918b8f78a9db486fd69dd4/README.md
[198] https://raw.githubusercontent.com/zilliztech/GPTCache/c59fb3a6152a4458b2a070ca183b61c4b614095f/README.md
[200] https://raw.githubusercontent.com/zilliztech/GPTCache/c59fb3a6152a4458b2a070ca183b61c4b614095f/gptcache/similarity_evaluation/exact_match.py
[206] https://raw.githubusercontent.com/openai/tiktoken/4e71bbe0c078468e00fefbf94b39849389f346e5/README.md
[212] https://developers.cloudflare.com/ai-gateway/features/caching
[213] https://thetokencompany.com/docs/llms.txt
[214] https://compresr.ai/docs/introduction
[216] https://developers.openai.com/api/docs/guides/batch
[217] https://www.sqlite.org/copyright.html
[218] https://duckdb.org/docs/stable/sql/query_syntax/select.html
[258] https://raw.githubusercontent.com/lm-sys/RouteLLM/main/README.md
[264] https://raw.githubusercontent.com/BerriAI/litellm/litellm_internal_staging/pyproject.toml
[268] https://raw.githubusercontent.com/ryoppippi/ccusage/2defd5550b9e4a26c0f4d4f175fc1508ca16fbc3/rust/crates/ccusage-core/src/cost.rs
[269] https://raw.githubusercontent.com/ryoppippi/ccusage/2defd5550b9e4a26c0f4d4f175fc1508ca16fbc3/docs/guide/cost-modes.md
