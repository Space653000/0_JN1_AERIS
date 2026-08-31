# AERIS GitHub Access Boundary

**Policy:** Codex runtime must have no GitHub write credential for `Space653000/0_JN1_AERIS`.

## Preferred access model

Because `Space653000/0_JN1_AERIS` is a public repository, Codex can clone, fetch and read the canonical target without any GitHub token.

Preferred Codex runtime:

```text
GitHub repository visibility: public
Codex GitHub credential: none
Fetch/clone: anonymous HTTPS
Push URL: disabled locally
pre-push hook: deny
Remote write API credential: none
```

This is stronger than relying only on prompt instructions.

## If authenticated read access is ever required

Use a dedicated credential whose repository permissions are read-only. Do not reuse the Human owner's GitHub credential, Personal Access Token, GitHub CLI login or writable GitHub App token inside the Codex runtime.

Minimum principle:

```text
Metadata: read
Contents: read
Pull requests: no write
Issues: no write unless explicitly required for a separate non-publication workflow
Administration: none
Workflows/Actions: no write
```

## Never expose to Codex

Do not expose credentials that can:

- write repository contents;
- update refs / branches / tags;
- create or merge PRs;
- change Actions workflows;
- change Pages settings;
- change repository administration / rulesets / protection;
- publish releases.

## Defense layers

AERIS uses multiple independent controls:

```text
Layer 1  AGENTS.md authority contract
Layer 2  aeris.policy.yaml machine policy
Layer 3  no writable GitHub credential in Codex runtime
Layer 4  disabled local origin push URL
Layer 5  deny pre-push hook
Layer 6  CODEOWNERS / Human publication ownership
Layer 7  GitHub Ruleset / branch protection (recommended server-side lock)
```

The target state is not merely “Codex should not push.” It is:

> **Codex should not possess a viable path that can mutate the official AERIS GitHub repository.**
