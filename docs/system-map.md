# System map: a layer of methods, not another platform

The blueprint sits around work decisions that existing harnesses already make. It does not require a new middleware service to control every request.

## The shared workflow

```text
Your request
  → identify harness + auth + provider + task requirements
  → decide whether fresh model reasoning is needed
  → prepare exact data and the smallest sufficient evidence
  → use the chosen harness/model through its supported route
  → verify all requested work
  → retain a change receipt or restore the prior setup
```

Use [the route passport](../templates/route-passport.md), [task contract](../templates/task-contract.md), [working set](../templates/working-set.md) and [change receipt](../templates/change-receipt.md). They are templates for your existing agent or team, not a demand to maintain a new dashboard.

## Control three different things

### Work

Can this deterministic operation run through existing code? Has a verified result already been produced for the same source/version/authority? Did anything relevant change? Is another operator already completing the same authorized task?

This is where entire repeated model calls can disappear. Do not skip scheduled obligations, required semantic review or current-state checks.

### Context

What must the model actually read now? Can exact retrieval, a verified calculation, a native patch or an artifact replace repetitive data movement? Does a stronger selected view lose a qualifier or active dependency?

Use one owner per surface. Native tools, MCP servers, wrappers and gateways must not each transform the same material independently.

### Spend

Which account and billing path pays for this job? Is the budget enforced by a provider, managed endpoint or only a recommendation? Is moving the work supported and authorized? Will a cache change actually lower price, or just change token categories?

A subscription fee, a model token and an API dollar are not interchangeable units. See [authentication and billing](auth-and-billing.md).

## Match the integration to the surface

| Surface | Practical control | Do not assume |
|---|---|---|
| Native CLI with supported hooks | Project instructions, exact tools and the documented event fields | Another CLI accepts the same hook JSON |
| MCP-capable agent | Your selected tool's query/output and declared schema | Control of hidden prompts or all native tools |
| IDE with product-owned credits | Native context/rules/tools and visible account controls | Transparent interception or complete token receipts |
| Direct API application | Approved request preparation and provider-native parameters | Every protocol/state can be translated through generic chat |
| Organization gateway | Its configured routes, keys, limits and observability | Control of jobs that bypass it, or rights to broker human subscriptions |
| Closed consumer chat | Supported uploads, instructions and manual workflow practices | Universal background automation or middleware control |

## The advantage to aim for

The differentiator is the complete decision path: route-specific guidance, exact coverage, avoided work, one-change adoption, recoverability and honest economics. No single component supplies that experience by itself, but the pieces can be used through existing systems.

Do not claim market-wide uniqueness. Make the repository useful enough that an operator can select a route, make a justified change and recover cleanly without researching the entire market again.
