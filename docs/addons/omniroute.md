# OmniRoute: optional, restricted API add-on

[Start here](../../START-HERE.md) · [Delegation](../delegation.md) · [Compression inventory](omniroute-compression.md) · [Free-provider choices](free-provider-lanes.md)

**Status: source-inspected, pilot-gated.** This guide does not install a gateway or certify a live account. It replaces blanket exclusion of the project with specific permitted candidates and explicit stop conditions. Keep the core blueprint and native login working without this add-on.

Inspected pin: `diegosouzapw/OmniRoute` at `b345c7f6cd4e1590d1177540813302375a75e332`, checked 2026-09-07 UTC. These limits describe that source revision; verify changes in a later version before applying them.

## What it adds, and what it does not

OmniRoute provides provider connections, routing, protocol translation, compression, caches and some multi-model/protocol operations. That can be useful when an API workflow genuinely needs them. It does not make a free model an authorized tool worker or remove the main harness's responsibility for context, permissions, verification and completion.[1][2]

The initial candidate is a separately approved, small API analysis lane. Do not route the main native subscription through a new proxy just to try compression. Do not install multiple apps merely to call another model; an existing host can make an approved API call. Tool-capable workers still need their actual harness/runtime. See [Delegation](../delegation.md).

## Choose one of these paths

| Path | What stays unchanged | Candidate method | Activation boundary |
|---|---|---|---|
| Route-only baseline | Same task, approved API model/effort and data permission | One explicit provider/account/model; compression and answer cache off | Prove actual route and failure behavior before any optimization |
| Conservative plus OmniRoute | Core Conservative requirements and selected model | Headroom alone on validated ordinary JSON data | Requires exact domain/coverage checks, request-size bounds and route acceptance; otherwise leave compression off |
| Aggressive plus OmniRoute | Required work, permissions and separately chosen model | One RTK observation stage on eligible repetitive command output | Retain full originals; no duplicate reducer; no exhaustive logs/diffs/active code; prove restoration |
| Optional cheaper/free worker | Main model stays on its original route; worker model is a separate approved choice | A named, bounded API helper or host-native worker | Account entitlement, data use, cost/fallback and worker quality must be accepted separately |

These are blueprint profiles, **not the gateway's identically named presets**. Blueprint Aggressive does not mean `defaultMode: "aggressive"`. There is no all-features import file here.

## Before putting any traffic through it

1. Keep an existing direct/native baseline. Use only an already authorized isolated OmniRoute instance, or obtain separate installation approval. Do not copy a global profile over a shared service.
2. Record the exact version, effective settings, provider/account/project, model after alias resolution, worker identity, data scope, retention and rollback. Use the [route passport](../../templates/route-passport.md) and [add-on trial](../../templates/addon-trial.md).
3. Use an API account/key belonging to the operator or authorized organization. No consumer cookie/OAuth imports, personal seat pooling, undocumented keyless access, stealth/TLS interception or quota evasion.
4. Keep cloud sync/tunnel endpoints unconfigured for the isolated lane unless separately approved. Inspect the process environment and secret source. The inspected sync bundle can carry credentials; a flag about inbound credential overwrite is not an outbound secret filter.[11]
5. Provider connection creation is not necessarily offline: `POST /api/providers` automatically tests a newly created connection. Authorize possible upstream traffic **before** clicking Add/Test or sending a create request.[10]
6. Use a restricted database-backed inference key, not a dashboard/management key or deployment environment key. Worker credentials must not grant provider creation, routing changes or management access.[3]

Separate data domains should use appropriately isolated service identities/stores or remain on their current route. A connection label or API-key namespace alone is not enterprise tenant-isolation proof.

## Route safety comes before compression

### Fixed model means the actual dispatched model

The pin has several independent fallback paths. Disabling emergency fallback does not disable ordinary combo or model-family fallback. A `modelPinned` label or inbound model allowlist is not by itself proof that every internal fallback preserves the approved model.[4][5]

A useful source-level narrowing exists: the inspected family-fallback templates contain specific Claude/Gemini families. `getNextFamilyFallback` returns no sibling for an actual post-alias model outside that map; context-overflow candidates also come from that family set. A concrete approved non-family API model is therefore a narrower trial candidate. This avoids that particular mechanism, not every possible transport/provider behavior.[4][5]

For the first trial:

- Use one explicit provider-prefixed model and one approved connection, not `auto`, a saved combo, fuzzy alias, wildcard or subscription ladder.
- Verify the **resolved wire model** is outside the inspected family map, or require an independently enforced upstream model boundary / verified upstream fix. Do not change the required main model merely to make this condition true.
- Explicitly disable emergency fallback, full-pool free fallback and rotation for the isolated lane. Verify effective flags; a database override can outrank the environment.
- If fixed-model/fallback behavior cannot be established for the chosen route, keep the direct/native route. Do not remove the allowlist to make a trial succeed.

This is not a native runtime verification. Before accepting a lane, exercise approved failure cases and inspect every attempted upstream model/account, not only the final answer.

### Budgets and free labels are not hard guarantees

At this pin, a zero gateway budget means unlimited, not zero spending. Admission does not reserve the maximum cost of every in-flight request, and missing cost can appear as zero. Use current provider/project hard controls when required; distinguish a real enforced cap from an alert or reporting limit.[6]

The automatic strict-free path also has an availability gap: the inspected hard-stop model rows and quota-adapter registry do not yield a usable credentialed intersection. Do not weaken terms filters or enable a paid pool to manufacture a free option. An explicit official account-owned free API may still be usable directly, or in a separately validated lane. See [Free-provider choices](free-provider-lanes.md).[12]

## Read back these controls in the owned test scope

Names below are source-supported controls, not a complete safe configuration to paste blindly. Preserve required nested fields when the update API is only shallow-partial.

| Surface | Controls to inspect | Why |
|---|---|---|
| Client authentication | Effective `REQUIRE_API_KEY=true` | Missing/invalid keys must not degrade to anonymous access |
| Emergency/automatic routing | `OMNIROUTE_EMERGENCY_FALLBACK=false`, `OMNIROUTE_AUTO_FREE_FALLBACK_TO_FULL_POOL=false`, `OMNIROUTE_ROTATION_ENABLED=false` | Distinct paths; none alone disables family fallback |
| Key model scope | `modelAccessMode: "restricted"`, nonempty exact `allowedModels` | Avoid legacy empty-list-means-all behavior |
| Key connection scope | `connectionAccessMode: "restricted"`, explicit `allowedConnections` on the supported key PATCH | Creation and update schemas differ; use real connection IDs |
| Combo scope | Explicit `allowedCombos: []` | Do not assume it also blocks all aliases/virtual routing paths |
| Worker authority | No management scopes; `allowedEndpoints: ["chat"]`; no dashboard cookies | Endpoint categories are not a complete arbitrary-path firewall |
| Privacy/cache | `noLog: true`, `cacheDefaultMode: "bypass"` | Narrow effects, not a universal no-storage guarantee |
| Initial compression | Per-key `compressionEnabled:false`; global `enabled:false`, `defaultMode:"off"`, `autoTriggerMode:"off"` in the dedicated instance | Establish the route-only baseline |
| Independent transforms | `contextBudget.mode:"off"`, `contextEditing.enabled:false`, no output styles, MCP/A2A disabled for this lane | Optional prompt compression is not the only possible transformation |

Key/schema and effective-flag behavior are documented in the inspected code.[3][7] Do not give workers deployment environment keys just because those are convenient: they can synthesize broadly privileged metadata. A management token and an inference key have different jobs.

Keep native provider prompt caching as part of the baseline. The gateway's final-answer cache has an incomplete request signature at this pin; bypass it for the trial instead of counting unsafe reuse as a saving.[13]

## Conservative compression candidate

After route acceptance, the narrow candidate is **Headroom only** on a controlled ordinary JSON-data surface. The source can choose GCF/TOON representation by character size. That does not prove token savings or model interpretation, and `JSON.parse` can lose duplicate keys or unsafe numeric precision before encoding.[8]

Required external checks:

- Only the intended data packet can reach the selected stage. No instructions, schemas, approvals, active code, media, exact-lexeme exports or opaque provider state.
- Validate all source values and preserve order, multiplicity, null/missing, identifiers and monetary precision. Use validated strings where exact numeric spelling matters; reject unsupported inputs before lossy parsing.
- Keep the original artifact. Compute required totals from the full original data, not the model's reading of compact text.
- Compare the actual tokenizer including format instructions and complete task output.
- Bound the whole uncompressed request below independent context-fit thresholds. A selected engine is not a fence around other reactive behavior.
- Verify the task's coverage and answer, including an ordinary record and a quiet exception that a relevance filter might otherwise discard.

Use `headroom` as the sole selected engine, system preservation always, no auto-trigger/adaptive budget, no provider context editing, no live-zone/output-style/learned/history stages. Exact supported fields and the broader inventory are in [Compression controls](omniroute-compression.md).

If these gates cannot be satisfied, the Conservative recipe is **compression off** and native explicit representation/data processing. This page does not certify a general lossless OmniRoute preset.

## Aggressive compression candidate

After route acceptance, select **one RTK stage** for eligible repetitive test/build output. Keep complete raw stdout/stderr, exit status, source revision and failure evidence independently. OmniRoute's RTK is an implementation inspired by the external CLI, not a transfer of that CLI's benchmark.[9]

Source-supported candidate constraints include standard detail, tool results only, no assistant/code-block rewriting, grouping/renderers/comment stripping off, docstrings retained, no project/custom filters and explicit bounded output limits. These settings still allow deduplication/caps outside a filter match, so only feed the approved output class and verify what survived.[9]

Do not apply it to exhaustive logs, full review diffs, active implementation, legal/financial evidence or a task that needs every line. If native RTK or another upstream owner already reduced the same output, omit this stage.

A single output-generation policy can be a different axis, but the base blueprint already supplies complete concise output and Ponytail-derived coding discipline. Do not add `less-code` plus `ponytail` and credit both. Default add-on output styles stay empty.

Learned prose selection, CCR, history aging and image encoding are separate experiments, not extra checkboxes to append to this profile.

## Why “off” and “preserved” need verification

- `x-omniroute-compression: off` is not a universal kill switch: adaptive budgeting can escalate it under pressure, and reactive context fitting is separate.
- Per-key compression opt-out does not independently disable all context-fit behavior while the master is enabled.
- Empty/unknown-only persisted stacks can normalize back to a built-in RTK/Caveman stack rather than stay off.
- MCP description/result rewriting, provider context editing and final-answer caching have their own controls.
- Preservation/fidelity gates use heuristics and protected-token checks. They do not prove all relationships, qualifiers, records or task outcomes survived.

The exact source boundaries are in the [inventory](../../catalog/omniroute-features.json) and pinned resolution/settings code.[7][14][15]

## Verify, compare and roll back

Use a small owned lane first. Tests requiring traffic need explicit account/budget approval.

1. Test missing/invalid/expired/revoked keys, denied models/connections, forbidden combo/alias, wrong endpoint, unknown/exhausted quota and unknown price.
2. Exercise model-unavailable, context-overflow, empty response, 402/429/5xx, cancellation and concurrent calls. Confirm no unapproved provider/model/account request occurs.
3. Verify source privacy, actual worker identity/effort, complete output and every required check. A successful text response does not certify a full native tool/streaming/continuation workflow.
4. Compare **blueprint alone** against **the same blueprint plus the chosen add-on**, not against a deliberately bloated raw prompt. Count all attempts, helper work, cache churn, restores, verification and local compute.
5. For a cheaper/free worker, disclose the different worker model and quality outcome. That is a separate economic comparison, not compression-only savings.

No measured extra 20–30% is established. Additional savings can be small, zero or negative; unrelated component percentages cannot supply the missing comparison.[16]

Rollback: stop new dispatch, reconcile in-flight effects, restore the exact prior endpoint/model/effort and only the changed settings, revoke the trial key if appropriate, and recover original source context through supported native methods. Never replay writes or reset other users' configurations. Setting an empty compression stack is not the rollback procedure.

## Sources

[1] https://github.com/diegosouzapw/OmniRoute/tree/b345c7f6cd4e1590d1177540813302375a75e332
[2] https://github.com/diegosouzapw/OmniRoute/blob/b345c7f6cd4e1590d1177540813302375a75e332/open-sse/services/fusion.ts
[3] https://github.com/diegosouzapw/OmniRoute/blob/b345c7f6cd4e1590d1177540813302375a75e332/src/shared/validation/schemas/keys.ts
[4] https://github.com/diegosouzapw/OmniRoute/blob/b345c7f6cd4e1590d1177540813302375a75e332/open-sse/services/modelFamilyFallback.ts
[5] https://github.com/diegosouzapw/OmniRoute/blob/b345c7f6cd4e1590d1177540813302375a75e332/open-sse/handlers/chatCore.ts
[6] https://github.com/diegosouzapw/OmniRoute/blob/b345c7f6cd4e1590d1177540813302375a75e332/src/domain/costRules.ts
[7] https://github.com/diegosouzapw/OmniRoute/blob/b345c7f6cd4e1590d1177540813302375a75e332/src/shared/validation/compressionConfigSchemas.ts
[8] https://github.com/diegosouzapw/OmniRoute/blob/b345c7f6cd4e1590d1177540813302375a75e332/open-sse/services/compression/engines/headroom/smartcrusher.ts
[9] https://github.com/diegosouzapw/OmniRoute/blob/b345c7f6cd4e1590d1177540813302375a75e332/open-sse/services/compression/engines/rtk/index.ts
[10] https://github.com/diegosouzapw/OmniRoute/blob/b345c7f6cd4e1590d1177540813302375a75e332/src/app/api/providers/route.ts
[11] https://github.com/diegosouzapw/OmniRoute/blob/b345c7f6cd4e1590d1177540813302375a75e332/src/lib/cloudSync.ts
[12] https://github.com/diegosouzapw/OmniRoute/blob/b345c7f6cd4e1590d1177540813302375a75e332/open-sse/services/autoCombo/strictZeroCostFilter.ts
[13] https://github.com/diegosouzapw/OmniRoute/blob/b345c7f6cd4e1590d1177540813302375a75e332/src/lib/semanticCache.ts
[14] https://github.com/diegosouzapw/OmniRoute/blob/b345c7f6cd4e1590d1177540813302375a75e332/open-sse/services/compression/adaptiveCompression/resolveAdaptivePlan.ts
[15] https://github.com/diegosouzapw/OmniRoute/blob/b345c7f6cd4e1590d1177540813302375a75e332/src/lib/db/compression.ts
[16] https://github.com/diegosouzapw/OmniRoute/blob/b345c7f6cd4e1590d1177540813302375a75e332/docs/compression/COMPRESSION_GUIDE.md


Direct implementation evidence: [literal free-model rows](https://github.com/diegosouzapw/OmniRoute/blob/b345c7f6cd4e1590d1177540813302375a75e332/open-sse/config/freeModelCatalog.data.ts), [usage-adapter registrations](https://github.com/diegosouzapw/OmniRoute/blob/b345c7f6cd4e1590d1177540813302375a75e332/open-sse/services/usage/fetcherProviders.ts) and [missing-price cost calculation](https://github.com/diegosouzapw/OmniRoute/blob/b345c7f6cd4e1590d1177540813302375a75e332/src/lib/usage/costCalculator.ts).
