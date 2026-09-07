# Install, update and roll back without breaking the setup

This repository supplies instructions and templates, not an automatic installer. Most starting changes require no new component.

## Before a change

1. Read the exact [harness route](harnesses/index.md) and current official source.
2. Identify whether settings are project, user, workspace, organization or managed policy. Do not edit a broader scope by convenience.
3. Record model, effort, auth/provider route, relevant versions and existing plugins.
4. Back up only the affected files/settings using the user's established secure method. Backups can contain secrets; keep them out of Git and this repository.
5. Write the intended diff and rollback in a [change receipt](../templates/change-receipt.md).
6. Ask for approval. Do not bypass a native protected-file consent or administrator control.

## Apply narrowly

- Merge a documented field or append a clearly delimited instruction section. Never replace the whole file with a sample.
- Keep the user's existing rules and test requirements authoritative.
- Pin an optional component's version and read its install script/dependencies before running it.
- Do not run a fetched shell installer blindly, install root certificates, change shell-wide proxy variables or export credentials into a shared process as a shortcut.
- Do not copy a hook contract from one harness into another.
- Choose one owner for each transformation surface and leave overlapping plugins alone until the conflict is understood.

## Verify effective behavior

A configuration file that parses is not proof the running client loaded it. Check native status/version information and exercise one permitted representative task. Verify model/auth, expected tool behavior, errors, approvals, cancellation, required outputs and access to the original source.

A sign-in indicator is not proof inference or tool execution works. A text response is not proof images, structured tools or native continuation are compatible.

## Roll back

Restore the recorded native setting or remove only the section you added. Preserve later user edits rather than copying an old backup over them. Reopen/reload through the official mechanism if required and verify the original workflow still works.

Never “restore” a revoked credential, replay a mutating command to recover its output or modify encrypted/signed provider history. If recovery requires a new authorized session, say so.

## Update

Recheck release notes, auth changes, settings schemas, licensing and the exact recipe. A version number being newer does not prove compatibility. Use a small approved canary before a team-wide change. Do not silently switch models, accounts or optional features during an update.

## Remove an optional component

Read its actual uninstall behavior. Some tools delete local history/data or modify shell trust and startup services. Export/retain evidence according to policy before removal. Remove only owned entries and verify the native account, other plugins and project files are intact.

## Evidence to keep privately

Version, scoped config diff without secrets, source links, original settings, task outcome, errors, rollback result and unresolved limits. Do not upload private traces or credentials to a public issue; use a minimal redacted reproduction.
