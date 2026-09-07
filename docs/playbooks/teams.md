# Teams and cross-harness handoffs

Share useful authorized work, not human subscription credentials or unrestricted conversation memory. A solo user does not need this coordination layer.

## The common handoff

Use [handoff record](../../templates/handoff.md) with the actual task, source revisions, completed criteria, unresolved issues, exact artifact locations and current permission boundary.

A handoff from Claude Code to Codex can carry a source-linked task summary, changed files and verification evidence. It cannot assume that provider-specific encrypted reasoning, session tokens, tool IDs or approvals are portable.

## Avoid duplicate work safely

Before repeating a scan or calculation, check whether a current authorized result already exists for the same task/source/environment. Reuse it only when its meaning and dependencies still match.

Do not merge tasks merely because prompts sound similar. Different clients, branches, date ranges, acceptance criteria and role assignments can make them different work. A cached research note is not a live fact or permission to act.

## Keep mutable work isolated

Use existing project permissions and separate worktrees/workspaces where required. Give every execution a task/session identity. Avoid shared process-global current project, mode or account settings.

For a coupled task, one accountable owner integrates results and verifies the complete outcome. Independent workers can gather evidence, but their summaries are not automatically accepted conclusions.

## Source updates and revocation

Record dependencies from source to excerpt, calculation, summary and answer. Corrections supersede prior facts and invalidate affected derived results. Recheck access when someone retrieves a shared result, not only when it was created.

Revocation cannot retract content already delivered to a model or person. Stop or quarantine affected work and start a fresh authorized context where necessary. Offline clients need an explicit lease/refresh policy; do not promise instantaneous revocation while disconnected.

## Subscriptions and API budgets

Each person keeps their own provider seat where required. A company API project may use properly scoped keys under its contract. Do not pool human logins or treat unused colleague quotas as a transferable resource.

Separate advisory budget estimates from hard controls actually enforced by the provider or a managed gateway. Work that bypasses a gateway is outside its budget authority. See [authentication and billing](../auth-and-billing.md).

## Roll out one recipe at a time

Use a small approved cohort. Freeze ordinary policy versions during an active task, apply security revocation immediately, and preserve rollback. A successful installation is not proof every operator's auth, source scope and required tools work.

## Verify team value

Measure repeated work actually avoided, accepted outcomes, latency, interruptions, restoration and rework. The number of agents or seats is not itself a savings multiplier.
