# Authentication, providers and money

**Identify the paying route before changing the workflow.** The harness is the application; the model is what reasons; the provider is where inference runs; authentication determines which account and entitlement are used. These can be four different things.

Use a [route passport](../templates/route-passport.md), then the exact [harness guide](harnesses/index.md).

## Native subscriptions and OAuth

Keep the unmodified supported client and its own sign-in. Do not extract session tokens, pool colleagues' accounts or turn a consumer subscription into a shared API.

The immediate goal is more useful completed work within the account's actual allowance, fewer unnecessary resets/retries and less additional paid usage where applicable. The flat monthly fee does not fall just because a task uses fewer tokens.

A displayed model name is not proof of the billing route. Existing API environment variables, custom endpoints or managed settings may change it. Inspect non-secret route/status information and verify a small authorized task; a login indicator alone is not a completed inference or tool test.

If a native account is exhausted:

1. Check the actual status and reset policy without guessing a token-to-quota conversion.
2. If the deadline permits, save a complete task checkpoint and resume through a supported mechanism later.
3. If an approved paid alternative exists, show its model/capability, privacy and spending implications before switching.
4. Otherwise stop honestly. Do not rotate unrelated accounts or silently use a different model.

## Direct API keys

Use the organization's or user's intended API account with least-privilege access. Keep secrets outside prompts, repositories, receipts and shared notes.

Potential economic levers include fewer actual calls/tokens, provider-native prompt caching, approved asynchronous batch processing and routing among explicitly allowed equivalents. These are distinct mechanisms. Prompt caching can lower price without removing logical input tokens; batch processing changes latency and may be unsuitable for an interactive task.

Prefer native same-provider features before a gateway. If using a gateway, confirm tools, streaming, cancellation, opaque state, usage and native discovery still work. A successful text reply is not full compatibility.

## Cloud or enterprise provider

Keep the approved project, region, identity and endpoint. Bedrock, Azure/Foundry, Google cloud routes, managed coding plans and third-party providers have different model availability, parameter support, retention, quotas and billing.

Do not copy a direct-API example into a cloud endpoint unchanged. Verify the selected route's guide, account permissions and data policy. An advertised compatible API is only the beginning of the check.

## Product-owned credits and IDEs

Some editors manage inference, model selection and credits internally. Use their supported rules, context controls, tools and account settings. BYOK, where supported, is a separate route and may have a different feature set.

If the product does not expose total tokens or a control surface, call that unknown or advisory. Do not claim to enforce a budget on traffic the recipe cannot observe or control.

## Mixed subscriptions and APIs

A practical policy can favor an already-authorized native subscription for suitable interactive work, an approved API for unattended/controlled integration, and deferred execution when a nonurgent job can wait. That is a decision policy, not a universal automatic router supplied by this repository.

Before switching, verify:

- The same person or organization is entitled to use the route.
- The exact selected model/capabilities are acceptable; matching brand names are insufficient.
- Data residency, confidentiality and account permissions permit it.
- The incremental spend has been approved.
- State can continue safely; provider-specific encrypted history is not portable by assumption.

Never divide a subscription price by an imagined token allowance and treat that as a real provider rate. Never count another employee's unused seat as a transferable resource without explicit provider permission.

## Separate the controls

| Control | Where it can be real | Limitation |
|---|---|---|
| Provider/project spending limit | A provider or managed billing product that actually enforces it | An alert or forecast is not necessarily a hard limit |
| Gateway policy | Requests that legitimately pass through the configured gateway | Bypassing traffic is outside its authority |
| Native project instructions | The assistant's behavior in that scope | Instructions are not a security boundary |
| Source permissions | The data system, filesystem, connector or sandbox | A summary cannot grant access |
| Task budget and stop rule | A supported job/session control or an operator procedure | A guessed budget cannot prove task completion |
| Subscription right-sizing | Owner decision using actual usage/renewal data | Do not cancel/downgrade accounts automatically |

## What counts as saving money

Report these separately:

1. Variable API charges avoided.
2. Additional subscription usage avoided, where billed and observable.
3. More accepted work from the same flat subscription.
4. Subscription/seat changes actually approved at renewal.
5. Compressor, storage, local hardware and maintenance costs added.

Some benefits are capacity rather than cash savings. Both matter, but calling them the same number undermines trust.

## Native account terms are independent of open-source licenses

A repository's MIT/Apache license does not grant access to its upstream providers. A technical OAuth forwarding example does not override the account contract. For example, [Claude Code's legal guidance](https://code.claude.com/docs/en/legal-and-compliance) distinguishes supported native use from credential intermediation. [OpenAI's terms](https://openai.com/policies/terms-of-use/) govern its accounts separately from a CLI code license.

For cache accounting, use the current [OpenAI prompt-caching documentation](https://developers.openai.com/api/docs/guides/prompt-caching) and the specific provider's usage fields. See [measurement](measurement.md) for full-task comparisons.
