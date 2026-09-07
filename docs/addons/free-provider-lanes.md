# Optional free and lower-cost model lanes

[Delegation](../delegation.md) · [OmniRoute add-on](omniroute.md) · [Auth and billing](../auth-and-billing.md)

**A separate economic choice for either mode.** It may lower API charges while using the same or more tokens. It is not permission to change the main model, pool personal subscriptions or send private data to an arbitrary endpoint.

Checked 2026-09-07 UTC. Provider examples are documented categories, not accounts authenticated or benchmarked by this repository.

## Start with the task, not the free-model list

Prefer deterministic code for a calculation, join, known validation or repeated procedure. A free LLM is unnecessary when no model is needed.

Reasonable worker candidates include a bounded public-source summary, alternative draft, independent test ideas or schema extraction where the accepted quality can be checked. Keep financial/legal/medical decisions, sensitive records, credentials, permissions and consequential actions off an unapproved free service. The main agent remains responsible for the result.

## Different meanings of “free”

| Category | Examples and boundary | What to verify |
|---|---|---|
| Official account-key free tier | Groq Free, eligible Gemini API free projects, Cloudflare Workers Free, specific OpenRouter `:free` variants | Actual account tier, exact model, hard stop, data policy, limits and whether billing/top-up is enabled |
| Public/anonymous community API | AI Horde documents anonymous access and volunteer execution | Public/nonconfidential tasks only; queue/quality/tool-support limitations; no private business data |
| Promotional credits | Eligible Google Cloud trial or current signup credit | Expiry, eligibility, payment/upgrade state and charges after credit; not recurring free capacity |
| Included paid subscription | Native authorized coding-agent usage | Paid seat already exists; use its supported client and account rules, not exported OAuth cookies |
| Local model endpoint | Existing Ollama, LM Studio or another approved server | Host/runtime actually running, model rights, hardware, power, latency, maintenance and data access |
| Metadata says price zero | A router/catalog label | **Not evidence of any of the above.** Missing pricing, unavailable models or unverified endpoints must remain unknown |

The provider distinctions are supported by current official pricing/account documentation; the operator must still verify their own route.[1][2][3][4][5]

Cerebras illustrates why the exact current offer matters: its fetched pricing page advertises trial credit, while older gateway documentation describes a recurring free quota and newer gateway metadata adds conditions not independently established by that page. Do not promise a particular recurring quota or expiry from mixed versions.[6]

Qwen's retired OAuth free tier is not revived by a cached token or a router menu. OpenCode Zen's documented keyed/free promotion has billing, reload and data-policy conditions; it does not authorize an undocumented keyless endpoint.[7][8]

## Direct API delegation is usually the simpler starting point

A host that already supports a second approved API provider can send a small complete worker packet without opening another app window. That endpoint supplies inference. The host must provide any tools, lifecycle, source access and verification.

Use native subagents or a supported headless runtime when the job needs agent tools. Use an analysis-only completion when the parent should retain all tool access. See the actual [harness patterns](../delegation.md), rather than assuming a router can create an autonomous agent.

Different authorized organization API accounts can be kept separate by project and purpose. That is not permission to share employees' personal seats, rotate free accounts to evade quotas, or import another application's credential cache.

## If using OmniRoute for the worker

Only after the [restricted API route gate](omniroute.md) passes:

1. Pick one official provider/account and concrete model. Keep a verified upstream hard stop and automatic paid upgrade/reload disabled if the intent is free-only.
2. Use a restricted inference key and preserve source/data permission. No management token, dashboard cookie, cloud-sync credential bundle, MCP/A2A worker authority or broad shared instance by default.
3. Keep automatic pool expansion and emergency fallback off. Model-family fallback is separate; use a verified non-family resolved model or an independently enforced allowed-model boundary. A price label is not that boundary.
4. Treat unknown/expired quota, absent pricing and unsupported models as unavailable, not as an invitation to find another account or bill a paid model.
5. Start with a small, nonconfidential, stateless analysis packet. Keep the main model and its native account outside this experimental lane.
6. Record actual upstream attempts/model/account and accepted output. Include retries, parent verification and any compression/recovery overhead.

At the inspected OmniRoute pin, the automatic strict-free pool cannot be promised as a usable official free pool: the literal hard-stop model rows and quota-adapter registry do not intersect for credentialed candidates. A normal keyless candidate is also tagged with terms to avoid. This is an availability/policy gate, not a reason to turn those protections off.[9]

A gateway zero budget is not a zero-dollar stop, and missing pricing can become zero in its accounting. Do not use either to certify free inference. The provider/account must supply the real spending boundary, with failure-path verification.[10]

## Model choice and verification

Record main and worker model/effort separately. Confirm actual worker metadata; requested settings may be inherited, unsupported or substituted by the harness. Keep all required source coverage and task tests.

If a worker cannot use tools, do not execute unexpected tool-call text as commands. If the output is incomplete or conflicts with sources, restore evidence or escalate within the agreed budget. Do not keep cycling through free endpoints until something sounds confident.

A low-price or free worker can be useful, but many retries or a full paid re-review can erase the benefit. Compare complete accepted work, not only the worker's quoted price.

## No “extra percentage” by default

Do not add a routing discount to a compression percentage. Show separately:

- Actual API dollars across parent, workers, retries and validation.
- Total token use with each model/tokenizer named.
- Native subscription capacity where observable.
- Quality, latency and human repair.

No universal extra 20–30% from OmniRoute, free providers or delegation is established. Use the [trial record](../../templates/trial-record.md) and [delegation packet](../../templates/delegation-packet.md).

## Sources

[1] https://console.groq.com/docs/billing-faqs
[2] https://ai.google.dev/gemini-api/docs/billing
[3] https://developers.cloudflare.com/workers-ai/platform/pricing
[4] https://openrouter.ai/docs/guides/routing/model-variants/free
[5] https://aihorde.net
[6] https://cerebras.ai/pricing
[7] https://qwenlm.github.io/qwen-code-docs/en/users/configuration/auth
[8] https://opencode.ai/docs/zen
[9] https://github.com/diegosouzapw/OmniRoute/blob/b345c7f6cd4e1590d1177540813302375a75e332/open-sse/services/autoCombo/strictZeroCostFilter.ts
[10] https://github.com/diegosouzapw/OmniRoute/blob/b345c7f6cd4e1590d1177540813302375a75e332/src/domain/costRules.ts


Direct implementation evidence: [literal free-model rows](https://github.com/diegosouzapw/OmniRoute/blob/b345c7f6cd4e1590d1177540813302375a75e332/open-sse/config/freeModelCatalog.data.ts), [usage-adapter registrations](https://github.com/diegosouzapw/OmniRoute/blob/b345c7f6cd4e1590d1177540813302375a75e332/open-sse/services/usage/fetcherProviders.ts) and [missing-price cost calculation](https://github.com/diegosouzapw/OmniRoute/blob/b345c7f6cd4e1590d1177540813302375a75e332/src/lib/usage/costCalculator.ts).
