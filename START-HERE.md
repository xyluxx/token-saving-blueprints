# Start here

Do not begin by installing a compressor. Begin by identifying what you are paying for and which parts of the task you can actually control.

## 1. Pick your route

Open the [harness index](docs/harnesses/index.md). Match the actual application, then its authentication path:

- Native subscription or OAuth sign-in.
- Direct provider API key.
- Organization cloud/managed endpoint.
- Explicit third-party provider or gateway.
- Product-owned credits with limited external controls.

Fill in [route passport](templates/route-passport.md). If you do not know the route, ask the agent to inspect non-secret settings and explain the result. Do not print keys, cookies or credential files. Do not assume a model name identifies its billing path.

## 2. Choose one real task

Use a task you genuinely repeat or care about. Record its required result, source coverage and acceptance checks in [task contract](templates/task-contract.md).

Good initial tasks include a known repository change with tests, a repeated report over complete records, or a document question with checkable sources. Avoid starting with your most sensitive production transaction or an irreducibly small prompt.

## 3. Record the native baseline

Keep the current model, reasoning, authentication and legitimate existing rules. Record versions and enabled native features. Complete the task normally and save whatever usage and outcome evidence the harness actually exposes.

No token meter? Record that limitation. Do not invent a number from screen text or convert an API estimate into a subscription bill.

## 4. Choose the smallest useful change

Start with [Conservative](docs/modes/conservative.md): focused source reads, deterministic bulk processing, precise patches, valid reuse or one supported output view. Many tasks need no new dependency.

Use [Aggressive](docs/modes/aggressive.md) only when the task permits selective context and you can restore the original. Do not start with every component enabled.

Want to see the forms filled in? Read the [illustrative first-change walkthrough](examples/first-change.md). It uses an existing native account and no new dependency, with no fabricated savings result.

## 5. Capture the change and rollback

Use [change receipt](templates/change-receipt.md). Identify exactly which setting, instruction section or optional tool changes, who owns it, and how to restore the prior state. Request approval before changing a live setup.

Do not overwrite a whole settings file with an example. Do not let a copied instruction override existing permissions or project tests.

## 6. Compare the completed work

Run the agreed checks. Count all calls, retries and restoration where telemetry is available. Keep the change only if its value is real for this task, not merely because the first response became shorter.

If something breaks, restore through the recorded native path. If permissions fail, stop rather than bypass them. If the original cannot fit or be recovered, state what remains incomplete.

## Then expand deliberately

Apply the method to a second task type, record differences, and only then consider more components or a broader rollout. A team rollout needs [shared-work boundaries](docs/playbooks/teams.md), not shared human credentials.

The full process is described in [measurement](docs/measurement.md) and [install/rollback](docs/install-and-rollback.md).
