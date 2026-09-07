# Evidence: what the numbers actually support

Checked 2026-09-06 (UTC). No live optimizer, authenticated native-harness savings benchmark or paid model trial was run for this market scan. The work inspected primary papers, source, licenses and author artifacts, and locally parsed selected published data. It does not establish an empirical average for this blueprint.

## Four evidence types, not one confidence badge

| Type | What it establishes | What it does not establish |
| --- | --- | --- |
| Primary study | Results for the paper’s named tasks, models, scaffold, metric and settings | Independent reproduction, current-native-harness compatibility or universal quality |
| Author benchmark | What the project’s disclosed procedure and artifacts report | A neutral comparison or a whole-task result when only payloads were counted |
| Source inspection | The inspected code path, defaults, license and documented boundaries | Successful installation, runtime safety or equivalent task outcomes |
| Local verification | The exact fixture, parsing, arithmetic or runtime behavior actually exercised | Generalization beyond the tested artifact or route |

A published study may also be an author-run benchmark. Independence, executable artifacts and metric scope are separate attributes. “Source-inspected” is not “native-smoke-tested.” Reading a test does not mean running it. A stored original does not mean the model noticed what a summary omitted.

## Conditional results worth knowing

### Ponytail: useful behavioral evidence, incomplete feature-quality proof

The June 18 author benchmark used Claude Code 2.1.177 with Haiku 4.5 on 12 feature tickets in a pinned FastAPI/React template, four runs per task/arm and four arms. It reports 22% fewer tokens and 54% fewer added lines for Ponytail versus the native agent without the skill. Tokens include input, output, cache reads and cache creation. The terse-prose Caveman control used 7% more tokens despite writing less code.[51][50]

The planned feature population was 192 cells; four force-killed cells contributed LOC but not cost/time. Bash was disallowed, no server/browser feature validation was performed, and a separate small safety-function tier is not proof that every feature met its requirements. A later completeness-judge script is not a committed completeness result for this cohort. Use the reuse/minimal-complete-change idea, not its percentage as this blueprint’s outcome.[51][50]

### Payload reducers: large reductions with small denominators

| Candidate and evidence | Exact measured population | Reported or derived result | Missing from that denominator |
| --- | --- | --- | --- |
| RTK, source plus author claim | Eligible Bash/command-output text, not built-in file tools or the entire task | README says up to 90%; inspected counter is rounded bytes divided by four | Actual target-model receipts, full history/output, retries and task quality |
| Headroom, committed seeded artifact | Four synthetic MCP-format scenarios; tool-role text counted with TiktokenCounter, model label gpt-5.6 | 178,024 to 104,261 tool-content tokens; artifact rounds this to 41% | System/user/schema envelope, generated answer, recovery calls and task success |
| context-mode v0.4.0, February 23 artifact | 13 indexing/execution/search examples | 198,337 to 12,609 bytes, a locally calculated 93.64% reduction; artifact rounds to 94% | Model tokens, complete later retrieval, all subsequent turns and semantic task quality |

RTK’s row uses its README and tracking source.[105][112]

Headroom’s row uses its result artifact and counting implementation.[75][74]

context-mode’s row uses its committed JSON artifact.[88]

Some context-mode entries are tiny indexing receipts or computed summaries. They are not evidence that an agent read the underlying document or delivered every requested record. Headroom’s statistical sampling can suit an overview but cannot replace all-row reconciliation. The RTK tee is bounded, so an independent retained raw-output path is necessary where restoration is required.[88][80][111]

### TOON: use the right baseline

The author’s retrieval benchmark has 244 questions across four models, or 976 answer trials for each format that supports the full set. It uses `o200k_base` for the reported format-body token counts. Average TOON is 2,474 tokens at 72.2% answer accuracy; pretty JSON is 4,308 at 71.4%; compact JSON is 2,892 at 69.0%. The locally recomputed format reduction is 42.57% versus pretty JSON but only 14.45% versus compact JSON. These are not entire-request or entire-task savings.[114]

CSV supports only the 109-question flat subset, so do not treat it as another complete 244-question arm. The report’s stated aggregate call count does not reconcile cleanly with that subset; no aggregate all-format count is adopted here. On its nested-configuration subset, compact JSON uses 562 tokens and TOON 669, with both at 106/116 correct. The strongest negative case is simple: the “optimized” representation can be larger. Encoding every value also does not make an LLM an exact calculator.[114]

### SWE-Pruner: a stronger agent-level positive case

Primary study v4, Mini SWE Agent on SWE-bench Verified, 500 tasks per model:

| Agent model | Baseline | With SWE-Pruner |
| --- | --- | --- |
| Claude Sonnet 4.5 | 353/500 solved; mean reported tokens 0.911M per task; 51.0 rounds | 360/500 solved; 0.701M tokens; 41.7 rounds; author reports 23.1% token reduction |
| GLM 4.6 | 277/500 solved; 0.791M tokens; 49.3 rounds | 283/500 solved; 0.488M tokens; 36.6 rounds; author reports 38.3% token reduction |

The 0.6B skimmer is a separate model and serving cost. The study also reports code-completion degradation under stronger compression, so code-QA or bug-solving gains do not establish exact edit/completion fidelity. Earlier paper versions have different solved counts; this table uses v4, not a mixture of versions. Raw trajectory reconciliation and trials on a different native harness remain open.[17][43]

### History reduction: the negative case matters as much as the win

The Complexity Trap v3 uses SWE-agent on nominally 500 SWE-bench Verified tasks per model configuration. For Qwen3-Coder 480B, masking changes solve rate from 53.4% to 54.8% and reported dollars per instance from $1.29 to $0.61. But for Gemini 2.5 Flash with thinking, masking reduces dollars from $0.56 to $0.24 while solve rate falls from 40.4% to 36.4%; summarization falls further to 31.4%. The masking loss is statistically significant in the released paired analysis. A cheaper failed task is not a successful optimization.[10]

These are dollar/solve-rate results, not total-token percentages. Retained raw cost data contains some 496 to 499-row groups while the paired artifact declares 500 common tasks; this is a disclosure, not a repaired reproduction. Reusing the same recent-message window across scaffolds also failed in the paper. No universal “mask the last N turns” recipe follows.[10]

AgentDiet v2 reports four model/benchmark comparisons using 200 held-out SWE-bench Verified tasks and 300 Multi-SWE-bench Flash tasks with Claude 4 Sonnet or Gemini 2.5 Pro. Accumulated agent-input reduction is 39.9 to 59.7%, but net cost reduction after cache effects and the GPT-5-mini reflection helper is 21.1 to 35.9%. Quality changes range from a one percentage-point loss to a two-point gain across those comparisons. Do not collapse this into one average or call it a main-model-only result.[12]

ACON v3 illustrates metric substitution: on AppWorld test-normal, 168 tasks (including 63 hard), GPT-4.1 agent/compressor history UTCO changes overall accuracy from 56.0% to 56.5%, but hard accuracy from 39.7% to 30.2% and mean steps from 16.14 to 22.82. Peak input falls from 9.93K to 7.33K and excludes system tokens. Peak context is neither cumulative input nor the bill.[13]

TRACE v1 supplies a newer caution: AppWorld test-normal, 168 tasks, two independent runs, MiniMax-M3 agent and compressor. Mean success is 85.7% with full context and 77.1% with TRACE; both-run success is 77.4% and 67.3%, respectively. It is useful for evaluating continuation behavior, not evidence that a newer summary always beats full context. Its replay procedure must restore interpreter state as well as databases; boundary screening still needs an eventual full-task check.[21][90]

### A fresh artifact check: leanctx’s hardware difference

The `jia-gao/leanctx` README reports a CPU run adding compression after ClawRouter on 503 LongBench v2 items. Local parsing verified 503 A records and 503 B records, plus two unrelated agent probes in the same file. The retained token totals are 13,277,567 for A and 10,799,469 for B, a 18.66% additional payload reduction. All accuracy fields in those A/B records are null: this local check establishes payload arithmetic, not evaluated answers.[203][272]

The linked earlier GPU report instead gives 24.1% payload reduction and accuracy 45.3% to 43.5% using Haiku 4.5. The README explains CPU timeout/fail-open and hardware differences. The CPU token figure and GPU quality figure are not one coupled reproduced trial. Its prose-heavy estimates reweight the observed traffic mix; they are scenarios, not an empirical average for business work.[203][204]

## What this blueprint does not claim

There is no measured Conservative/Aggressive whole-task average for this blueprint. Illustrative planning ranges depend on declared assumptions and must not be presented as empirical averages. No overall average is inferred by collecting the studies above.

Never add or multiply component headlines to invent a stack saving. They act on overlapping material, compare different native baselines and measure different units. Prompt-cache discounts, cheaper routing, batch pricing, wire-byte compression, lower peak context and fewer generated tokens are different outcomes. Trimming an answer after generation does not refund its output tokens. A native monthly subscription fee stays fixed unless the actual plan changes.

## Validate your own task without a research laboratory

1. Pick a real recurring task with an ordinary case, an awkward case and an already-small case. Keep inputs, requested result, model, effort, permissions and native features comparable. This is a practical screen, not a statistically sufficient sample for a universal claim.
2. Record the native result and available usage receipts. Save the exact acceptance checks: required fields, totals, source/citation coverage, working code and required tests. If the provider exposes no reliable quota or token measure, mark it unavailable rather than infer it from bytes.
3. Change one surface. Keep the original sources and the one-step bypass. For lossy views, include a difficult qualifier, correction or ordinary non-anomalous record in the check; do not let model confidence be the only detector.
4. Finish the same requested task. Include every helper call, failed attempt, restore and fallback. Retain input, cached-input and output classes separately; reasoning may already be part of output. Record latency and human rework as well as tokens/cost.
5. Keep the change only if acceptance passes and the full observed work improves for the intended use. Repeat unstable cases and inspect regressions. Otherwise widen the evidence, lower aggressiveness or revert. Never improve the metric by deleting a feature or test.

For an API workload, compare the sum of actual billed costs or explicitly labeled rate estimates for all attempted calls. For tokens, use one minus optimized full-task tokens divided by baseline full-task tokens, stating model/tokenizer and cache accounting. Show failures separately as well as including their costs. For a subscription, report actual observed quota/capacity only if available; an API-equivalent dollar estimate is not subscription savings.

A successful pilot justifies a limited local choice. A public numerical claim needs repeated representative tasks, stable baselines, full denominators, quality outcomes and disclosed failures. The cost of testing should be proportional to the risk and intended claim, not a permanent research project.

## Sources

[10] https://arxiv.org/html/2508.21433v3
[12] https://arxiv.org/html/2509.23586v2
[13] https://arxiv.org/html/2510.00615v3
[17] https://arxiv.org/html/2601.16746v4
[21] https://arxiv.org/html/2608.06503v1
[43] https://raw.githubusercontent.com/Ayanami1314/swe-pruner/96171b5f3ecaf89745cbeb436c8893b57f3400bd/swe-pruner/README.md
[50] https://raw.githubusercontent.com/DietrichGebert/ponytail/974d940a1c5344210874150b98ff0d2c861fab6a/benchmarks/agentic/run.py
[51] https://raw.githubusercontent.com/DietrichGebert/ponytail/974d940a1c5344210874150b98ff0d2c861fab6a/benchmarks/results/2026-06-18-agentic.md
[74] https://raw.githubusercontent.com/headroomlabs-ai/headroom/e67b3c8a29443a60d6b0018fb22f525c5cd7e709/benchmarks/index_proof_table.py
[75] https://raw.githubusercontent.com/headroomlabs-ai/headroom/e67b3c8a29443a60d6b0018fb22f525c5cd7e709/benchmarks/results/index_proof_table.txt
[80] https://raw.githubusercontent.com/headroomlabs-ai/headroom/e67b3c8a29443a60d6b0018fb22f525c5cd7e709/headroom/transforms/smart_crusher.py
[88] https://raw.githubusercontent.com/mksglu/context-mode/aded72c62372515518994153c470344f1b7d81a1/tests/benchmark-results-v04.json
[90] https://raw.githubusercontent.com/nokia-applied-research/Trace/9be7d66911bb7600fdec66e64f4825865397e944/data/rollout_replay_pilot/README.md
[105] https://raw.githubusercontent.com/rtk-ai/rtk/e53ec1cf180d801f33121855dce37b393ede258c/README.md
[111] https://raw.githubusercontent.com/rtk-ai/rtk/e53ec1cf180d801f33121855dce37b393ede258c/src/core/tee.rs
[112] https://raw.githubusercontent.com/rtk-ai/rtk/e53ec1cf180d801f33121855dce37b393ede258c/src/core/tracking.rs
[114] https://raw.githubusercontent.com/toon-format/toon/f151a5d830d001bc244395b891183cba37e0d935/benchmarks/results/retrieval-accuracy.md
[203] https://raw.githubusercontent.com/jia-gao/leanctx/84329a47161c449c14817db88c1f3218e95e22fb/README.md
[204] https://raw.githubusercontent.com/jia-gao/leanctx/84329a47161c449c14817db88c1f3218e95e22fb/benchmarks/clawrouter/full_long_bench_evaluation_result.md
[272] https://raw.githubusercontent.com/jia-gao/leanctx/84329a47161c449c14817db88c1f3218e95e22fb/benchmarks/clawrouter/results/full503_phase1_results.jsonl
