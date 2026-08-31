# AERIS Codex Local-Only Workflow

**Status:** Active governance baseline  
**Remote SSOT:** `https://github.com/Space653000/0_JN1_AERIS/tree/main`  
**Execution model:** Remote read-only target → Local implementation only

---

## 1. Purpose

This repository is the official AERIS target baseline. It defines what local AERIS implementations should converge toward, but Codex is not authorized to publish changes back to this repository.

The normal direction of work is one-way:

```text
GitHub main (canonical target)
        │
        │ clone / fetch / read / compare
        ▼
Local AERIS workspace
        │
        ├─ implementation
        ├─ tests
        ├─ evidence
        ├─ local commits
        └─ local handoff

Codex remote write path: DENIED
```

---

## 2. Why this separation exists

AERIS distinguishes:

- **Target truth** — what the official architecture / research / UI baseline says;
- **Implementation state** — what has actually been built and tested locally;
- **Publication authority** — who may change the official target.

Combining all three creates false-Done and accidental overwrite risk. Therefore:

> GitHub `main` is the target; local storage is the implementation; Human-controlled publication is a separate authority boundary.

---

## 3. Local folder SOP — new workspace

### Option A — clone normally, then harden immediately

```powershell
git clone https://github.com/Space653000/0_JN1_AERIS.git C:\path\to\AERIS-local
cd C:\path\to\AERIS-local
powershell -ExecutionPolicy Bypass -File .\tools\local-only\Protect-AERISReadOnly.ps1
powershell -ExecutionPolicy Bypass -File .\tools\local-only\Verify-AERISReadOnly.ps1

git fetch origin main
git switch -c local/bootstrap origin/main
```

After protection:

```text
origin fetch = https://github.com/Space653000/0_JN1_AERIS.git
origin push  = DISABLED://AERIS-REMOTE-READ-ONLY
pre-push     = always reject
```

### Option B — existing local AERIS folder

If the folder is already a Git worktree:

```powershell
cd <existing-local-aeris-folder>
powershell -ExecutionPolicy Bypass -File .\tools\local-only\Protect-AERISReadOnly.ps1
powershell -ExecutionPolicy Bypass -File .\tools\local-only\Verify-AERISReadOnly.ps1
```

The protection script does not reset working files or destroy local implementation. It only normalizes the upstream read URL and disables push.

---

## 4. Start every Codex task

Run:

```powershell
powershell -ExecutionPolicy Bypass -File .\tools\local-only\Sync-AERISTarget.ps1
```

This performs:

1. read-only guard verification;
2. `git fetch origin main`;
3. records current `origin/main` SHA;
4. writes the SHA to local-only `.aeris/target-main.sha`;
5. shows local drift against the target.

It does **not** merge, reset, push, create a PR or modify GitHub.

---

## 5. Local branch convention

Recommended:

```text
main                   = clean local mirror/reference
local/<topic>          = local implementation
local/<task-id>        = local implementation
experiment/<topic>     = optional local experiment
```

Codex should avoid modifying local `main` directly.

Example:

```powershell
git fetch origin main
git switch -c local/acoustic-skill-runtime origin/main
```

Local commits are allowed:

```powershell
git add .
git commit -m "local: implement acoustic skill runtime"
```

But:

```powershell
git push
```

must fail by design.

---

## 6. Updating a local implementation when GitHub target changes

First fetch only:

```powershell
powershell -ExecutionPolicy Bypass -File .\tools\local-only\Sync-AERISTarget.ps1
```

Then inspect target changes:

```powershell
git log --oneline HEAD..origin/main
git diff HEAD..origin/main
```

Choose the integration strategy locally:

- rebase local branch onto `origin/main`;
- merge `origin/main` into the local branch;
- manually port only relevant target changes.

No reverse synchronization from Codex is allowed.

---

## 7. Codex completion contract

A local delivery is complete only when Codex reports:

```text
Target remote: Space653000/0_JN1_AERIS
Target branch: main
Target SHA: <SHA>
Remote write performed: NO
Local workspace: <absolute path>
Local branch: <branch>
Changed local files: <list>
Tests/evals: PASS/FAIL + evidence
Drift vs origin/main: <summary>
Remaining blockers/risks: <summary>
```

If `Remote write performed` is anything except `NO`, the workflow is non-compliant.

---

## 8. Human-controlled publication

If the official GitHub baseline itself needs to change, that is a separate governance operation.

Codex may prepare locally:

- patch / diff;
- changed-file list;
- test evidence;
- architecture rationale;
- rollback plan;
- publication handoff note.

Codex may not publish that package to this repository.

The Human Chief Engineer or another explicitly authorized publication path decides whether the official SSOT changes.

---

## 9. GitHub-side defense in depth

Repository files now include:

- `AGENTS.md` — Codex authority boundary;
- `aeris.policy.yaml` — machine-readable policy;
- `.github/CODEOWNERS` — Human ownership signal;
- local `pushurl` disable script;
- local deny `pre-push` hook;
- verification and one-way sync scripts.

For stronger GitHub-side enforcement, configure a GitHub Ruleset / branch protection on `main` that requires controlled review and blocks direct pushes for non-authorized actors. This connector cannot currently configure repository Rulesets/branch protection, so that final server-side lock must be enabled through GitHub repository settings by an administrator.

---

## 10. Canonical rule

> **Codex reads AERIS GitHub as the target. Codex builds AERIS locally. Codex does not change the AERIS GitHub target.**
