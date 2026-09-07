# OmniRoute compression: what each switch actually means

[Optional add-on](omniroute.md) · [Machine-readable inventory](../../catalog/omniroute-features.json)

Pin `b345c7f6cd4e1590d1177540813302375a75e332`, inspected 2026-09-07 UTC. This is source inspection and published-artifact analysis, not execution of the gateway or its test suite. Do not import the inventory as settings.

## Not all registered engines are ordinary settings

The built-in source registry contains **15 engines**. The public catalog and writable stacked-pipeline schema expose **12**. `ionizer`, `llm` and `read-lifecycle` are registered but not normal persisted-profile choices at this pin. Dynamic externally registered engines are outside this inventory.[1][2]

| Engine | What it does | Blueprint disposition |
|---|---|---|
| `lite` | Whitespace changes, adjacent-content dedup, optional tool truncation, some image placeholders | Not a universal lossless preset; leave off in the narrow Conservative candidate |
| `caveman` | Regex prose rewriting with role/language/intensity controls | Separate lossy prose experiment; global mode name is `standard` |
| `aggressive` | Tool reduction, aging and rule summaries | Not the same as this blueprint's Aggressive mode; not the initial add-on selection |
| `ultra` | Heuristic token pruning; optional async small-model tier | Experimental, with compute/fallback and quality checks |
| `rtk` | Command-output filtering, dedup and caps | Candidate single owner for explicitly eligible repetitive test/build output |
| `codex-responses` | Specific Responses output minification/filtering | Not a general Codex guarantee; no JSON-minification-only switch established |
| `session-dedup` | Replaces repeated blocks with references; fuzzy option | Recovery and changed-information risks; separate experiment |
| `headroom` | JSON arrays into GCF/TOON-like representations | Narrow structured-data candidate after parsing, coverage and tokenizer gates |
| `ccr` | Content-addressed offloading | Requires advertised retrieval capability, lifetime and source-access verification |
| `llmlingua` | Optional async local model-based prose pruning | Separate learned-compression experiment; missing dependencies can no-op |
| `ionizer` | Statistical array sampling | Programmatic-only here; not full-record processing |
| `relevance` | Query-conditioned sentence selection | Separate exploratory view; not complete review or authoritative state |
| `llm` | Injectable model compression backend | Registered but production backend is no-op unless supplied; not a provisioned helper |
| `read-lifecycle` | Replaces earlier Read observations after later read/write activity | Programmatic-only and not proof of complete newer coverage or write success |
| `omniglyph` | Route/model-gated context-as-image encoding | Experimental; not an ordinary GPT or exact-code default |

The linked inventory preserves engine-specific controls, submechanisms, availability and source links. They are not independent percentages to add together.

## The baseline controls matter more than the preset label

Fresh compression settings are disabled, with mode off. Existing installations can retain older settings. An empty stored stack can normalize to an RTK/Caveman default rather than act as an off switch. Explicit stack arrays run in the supplied order; engine-toggle plans use a different priority ordering.[2][3]

Before a route-only trial, inspect the effective master state, active/named profile, combo overrides, engines map, request header and automatic triggers. Do not trust a decorative boolean or the fact an update endpoint accepted a field.

Request `x-omniroute-compression: off` and per-key `compressionEnabled:false` have narrower effects than a full bypass. Adaptive budgeting can escalate header-off under pressure; reactive context fitting and provider editing are separate. Keep `contextBudget.mode:"off"` and `contextEditing.enabled:false` in the owned trial scope and use the actual route checks in the [add-on guide](omniroute.md).[4][5]

## Conservative candidate: representation, not silent selection

The Headroom implementation parses ordinary JSON arrays, may encode homogeneous or heterogeneous objects, and chooses a character-length winner. It skips system/developer messages. That is not byte-exact source preservation or a guarantee an LLM reads every value correctly.[6]

`JSON.parse` itself can lose duplicate keys, large integer precision and numeric spelling. The candidate therefore requires a narrowly validated input domain, original sources, deterministic complete computations and exact coverage checks outside the compressor. Compare the actual target tokenizer, not characters alone. The source round-trip oracle is a test helper, not an automatically invoked production decoder.

Only after the route gate passes: one `headroom` selection; all other input stages off; preserve system always; no output styles, adaptive budget, auto-trigger, provider context editing, live-zone/history/learned/image stages. Bound the complete request below independent reactive/context-fit thresholds. Supported fields are detailed in the inventory and schema; no universal safe import is supplied.[2][6]

If the caller cannot enforce that domain and request boundary, stay with native explicit representation changes or compression off.

## Aggressive candidate: a narrow command view

Use one RTK stage on an explicit class of repetitive test/build output. Its implementation is inspired by RTK, not automatically equivalent to the external CLI's benchmark. An `enabledFilters` list does not govern every operation: deduplication and output caps can run outside the filter match. Full raw retention is also bounded.[7]

Source-supported candidate choices include:

- `standard` detail and tool results only;
- assistant/code-block rewriting off;
- grouping, semantic renderers and code-comment stripping off;
- docstrings retained;
- custom/project filters off;
- explicit caps and independently retained complete raw artifacts.

A cap can discard required evidence. This candidate is unsuitable for exhaustive logs, complete diffs, legal/financial review or active source code. Verify exit status, failures, identifiers and task-relevant content against the original. If upstream RTK or another tool already owns the same output, omit this gateway stage.

A generation policy is a separate axis, not another input compressor. The source has `terse-prose`, `less-code`, `ponytail`, `i-have-adhd` and locale-gated `terse-cjk`, each with levels. They inject instructions before generation. They can add input cost and overlap the blueprint's existing policy. Default them off; never shorten required output or stack Ponytail and less-code for the same benefit.[8]

## Why the other engines remain experiments

- **Lite:** no fenced-code awareness in its general whitespace pass; tool truncation is on by default when selected, and adjacent-content dedup is not a tool-ID equivalence proof.[9]
- **History aging:** message distance is not semantic obsolescence. Disabling one summarizer setting does not disable every summary/aging branch. Low savings can trigger other reducers.[10]
- **Relevance:** the latest user message participates in its own query scoring, and a selected step's `enabled:false` is not an effective guard in apply. Its standalone mapping and stacked mapping differ.[11]
- **Dedup:** a surviving original/reference can be transformed again later. Exact repeated text does not prove repeated events are redundant; fuzzy replacement is additionally lossy.[12]
- **CCR:** the caller must advertise `omniroute_ccr_retrieve`. Retention, size limits and best-effort durable writes are not permanent memory. Validate retrieval before accepting an answer or action.[13]
- **Learned/ultra:** local model loading, inference and fallback consume compute and may change meaning. A no-op on missing dependencies is not savings. A heuristic fallback is not necessarily original-text fallback.[14]
- **OmniGlyph:** the transport/model gate is intentionally narrow. Input image estimates, output inflation, refusals, cache behavior and quality must all be compared. Current source and published examples do not justify applying it to arbitrary models or exact coding work.[15]

## Independent mechanisms and guard limits

The catalog also lists **22 supporting mechanism groups**, including MCP descriptions/results/cardinality, reactive fitting, provider context editing, adaptive planning, caches, prefix/live-zone handling, output styles, fidelity/risk/inflation guards and CPU worker offloading.

Important distinctions:

- MCP result/description rewriting is independent of the prompt-compression master. Disabling compression does not disable every MCP transform.
- Compression memoization caches a transform result, not a model response.
- Provider prompt caching is a native baseline benefit, not new logical-token deletion.
- The gateway's so-called semantic answer cache uses a limited deterministic signature at this pin. It omits some answer-changing state, so bypass it for the initial trial.
- CPU compression workers are not LLM subagents. Fusion/model panels are not automatically cheaper delegation.
- A fidelity score based on protected substrings or keys cannot establish associations, multiplicity, negations or complete task correctness. Some engines bypass that gate; some runtime guard options are not accepted by the public settings update schema.
- Smaller serialized output can still have more model tokens, destroy a warm cache or require more later work.

Source support and exact scopes are retained in the [inventory](../../catalog/omniroute-features.json).[5][16][17]

## What the published savings establish

The often-cited stacked percentage combines assumed rates on eligible content. That is not a measured increment over this blueprint or a full native task. A repeated-error fixture can reduce dramatically while ordinary clean reads achieve little. The inspected golden-set savings test has a title suggesting a larger average than its actual mean/median assertions; inspect assertions, not titles.[18]

External Caveman and OmniGlyph reports use different wrappers, models, payloads and quality tests. Their figures do not become OmniRoute's contribution to your current workflow. No additional 20–30% estimate is established here.

Use the same complete task with and without exactly one selected add-on, and include helper calls, recovery, failed trials, changed cache behavior, output, local compute and human repair. [Measurement](../measurement.md) explains the ledger.

## Sources

[1] https://github.com/diegosouzapw/OmniRoute/blob/b345c7f6cd4e1590d1177540813302375a75e332/open-sse/services/compression/engines/index.ts
[2] https://github.com/diegosouzapw/OmniRoute/blob/b345c7f6cd4e1590d1177540813302375a75e332/src/shared/validation/compressionConfigSchemas.ts
[3] https://github.com/diegosouzapw/OmniRoute/blob/b345c7f6cd4e1590d1177540813302375a75e332/src/lib/db/compression.ts
[4] https://github.com/diegosouzapw/OmniRoute/blob/b345c7f6cd4e1590d1177540813302375a75e332/open-sse/services/compression/adaptiveCompression/resolveAdaptivePlan.ts
[5] https://github.com/diegosouzapw/OmniRoute/blob/b345c7f6cd4e1590d1177540813302375a75e332/open-sse/handlers/chatCore.ts
[6] https://github.com/diegosouzapw/OmniRoute/blob/b345c7f6cd4e1590d1177540813302375a75e332/open-sse/services/compression/engines/headroom/smartcrusher.ts
[7] https://github.com/diegosouzapw/OmniRoute/blob/b345c7f6cd4e1590d1177540813302375a75e332/open-sse/services/compression/engines/rtk/index.ts
[8] https://github.com/diegosouzapw/OmniRoute/blob/b345c7f6cd4e1590d1177540813302375a75e332/open-sse/services/compression/outputStyles/apply.ts
[9] https://github.com/diegosouzapw/OmniRoute/blob/b345c7f6cd4e1590d1177540813302375a75e332/open-sse/services/compression/lite.ts
[10] https://github.com/diegosouzapw/OmniRoute/blob/b345c7f6cd4e1590d1177540813302375a75e332/open-sse/services/compression/aggressive.ts
[11] https://github.com/diegosouzapw/OmniRoute/blob/b345c7f6cd4e1590d1177540813302375a75e332/open-sse/services/compression/engines/relevance/index.ts
[12] https://github.com/diegosouzapw/OmniRoute/blob/b345c7f6cd4e1590d1177540813302375a75e332/open-sse/services/compression/engines/session-dedup/index.ts
[13] https://github.com/diegosouzapw/OmniRoute/blob/b345c7f6cd4e1590d1177540813302375a75e332/open-sse/services/compression/engines/ccr/index.ts
[14] https://github.com/diegosouzapw/OmniRoute/blob/b345c7f6cd4e1590d1177540813302375a75e332/open-sse/services/compression/engines/llmlingua/index.ts
[15] https://github.com/diegosouzapw/OmniRoute/blob/b345c7f6cd4e1590d1177540813302375a75e332/open-sse/services/compression/engines/omniglyphAdapter.ts
[16] https://github.com/diegosouzapw/OmniRoute/blob/b345c7f6cd4e1590d1177540813302375a75e332/open-sse/services/compression/fidelityGateStep.ts
[17] https://github.com/diegosouzapw/OmniRoute/blob/b345c7f6cd4e1590d1177540813302375a75e332/src/lib/semanticCache.ts
[18] https://github.com/diegosouzapw/OmniRoute/blob/b345c7f6cd4e1590d1177540813302375a75e332/tests/golden-set/compression-savings.test.ts
