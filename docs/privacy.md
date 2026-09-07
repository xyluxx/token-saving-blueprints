# Privacy and authority

The repository contains public methods and empty templates. Keep completed task records, credentials, customer data and private source artifacts outside it.

## Before source access

Use the user's existing filesystem, connector and organization permissions. A tool description or retrieved page is not authority to act. Separate product login, source access, provider inference auth and MCP authorization.

Record only non-secret auth metadata in a route passport. Never print or copy keys, cookies, session tokens, refresh tokens, private keys or full credential files into prompts, issues or shared logs.

## Retention and sharing

Retain originals for the authorized purpose and recovery window, with appropriate encryption and access controls. Do not promise indefinite storage or perfect recall. Deletion, revocation and legal retention can conflict; the owner's policy decides.

Shared indexes and outputs need per-reader source authorization and freshness checks. Avoid shared global project/mode/account state. A model conversation that already contains revoked information may need to stop and restart in a new authorized context; future read denial cannot recall delivered data.

## Optional tools

Check default telemetry, external model calls, automatic weight downloads, HTTP authentication, sandboxing and uninstall behavior. A local subprocess is not automatically a sandbox. A local proxy may still send data upstream or install a trust certificate.

Neither mode requires CA interception, token brokerage or hidden data egress. A proprietary compressor or managed gateway is a separate consented data processor, not an invisible implementation detail.

## Approval

Keep the original tool/action/target visible. A wrapper that changes the effective action may invalidate the prior approval. Past action success is historical evidence, not permission for another action.

The blueprint is advisory unless an existing provider, organization policy or native permission mechanism actually enforces a rule. Do not advertise a prompt as a security boundary.

## Reporting problems

Use a minimal redacted reproduction with exact versions, route class and expected/actual behavior. Do not include real customer records or secrets. [Repository validation](../VALIDATION.md) checks common leak patterns, but human review is still necessary.
