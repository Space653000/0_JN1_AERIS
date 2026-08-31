# AERIS Local-Only Tooling

這個資料夾只負責一件事：

> **讓本機 AERIS 可以持續以 GitHub `main` 為目標同步與實作，但阻止 Codex 把本機工作寫回 `Space653000/0_JN1_AERIS`.**

Canonical upstream:

```text
https://github.com/Space653000/0_JN1_AERIS.git
branch: main
role: READ-ONLY TARGET / SSOT
```

## Recommended first-time setup

```powershell
powershell -ExecutionPolicy Bypass -File .\tools\local-only\New-AERISLocalWorkspace.ps1 -TargetPath "C:\AERIS"
```

This performs:

1. clone canonical `main`;
2. install read-only guards;
3. disable the `origin` push URL;
4. install a deny-all `pre-push` hook;
5. fetch `origin/main`;
6. create a local implementation branch;
7. record the target SHA;
8. verify the guard.

## Existing local clone

Install / repair the guard:

```powershell
powershell -ExecutionPolicy Bypass -File .\tools\local-only\Protect-AERISReadOnly.ps1
```

Verify before Codex starts work:

```powershell
powershell -ExecutionPolicy Bypass -File .\tools\local-only\Verify-AERISReadOnly.ps1
```

Synchronize the latest target baseline:

```powershell
powershell -ExecutionPolicy Bypass -File .\tools\local-only\Sync-AERISTarget.ps1
```

## Expected Git topology

```text
GitHub main
  |
  | clone / fetch / compare only
  v
origin/main@<SHA>          = canonical target
  |
  +--> local/<task>        = Codex implementation
         |
         +--> edit
         +--> test
         +--> local commit (optional)
         +--> evidence / reports
         X--> NO PUSH TO GITHUB
```

## Required result

```text
origin fetch URL = https://github.com/Space653000/0_JN1_AERIS.git
origin push URL  = DISABLED://AERIS-REMOTE-READ-ONLY
pre-push hook    = DENY
```

Codex must never remove, bypass or weaken these guards.

See also:

- `/AGENTS.md`
- `/aeris.policy.yaml`
- `/docs/governance/CODEX_LOCAL_ONLY_WORKFLOW.md`
- `/docs/governance/GITHUB_ACCESS_BOUNDARY.md`
