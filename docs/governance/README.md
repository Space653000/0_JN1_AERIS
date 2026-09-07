# AERIS Governance Index

> **2026-09-07 審查優先：HOLD_FOR_SOL_RED_TEAM。** 先讀 [Astra → Sol → Astra 閘門](ASTRA_SOL_REVIEW_GATE_V1.md)。下文 Full-Build／兩個 URL／缺口清零／續建命令只適用於閘門解除後的已授權有限批次。本次只修訂與發布文件；第 4 項等待使用者切換 GPT-5.6 Sol High，尚未執行本機總驗收。

## Repository authority model

`Space653000/0_JN1_AERIS@main` is the **canonical AERIS target baseline / remote SSOT**.

Codex authority is intentionally asymmetric:

```text
GitHub main  --->  Local AERIS
   READ            IMPLEMENT
   FETCH           TEST
   COMPARE         VERIFY
                   LOCAL COMMIT

Local AERIS -X-> GitHub main
```

## Canonical governance files

1. [`/AGENTS.md`](../../AGENTS.md)  
   Human-readable Codex execution contract. Highest-priority repository instruction for Codex.

2. [`/aeris.policy.yaml`](../../aeris.policy.yaml)  
   Machine-readable authority policy. `remote_write: forbidden`, `local_execution: required`.

3. [`CODEX_LOCAL_ONLY_WORKFLOW.md`](CODEX_LOCAL_ONLY_WORKFLOW.md)  
   Full local implementation SOP: start checks, sync, local branch/worktree, evidence and handoff.

4. [`GITHUB_ACCESS_BOUNDARY.md`](GITHUB_ACCESS_BOUNDARY.md)  
   Defines what GitHub access is permitted and what requires separate Human-controlled publication authority.

5. [`/tools/local-only/`](../../tools/local-only/)  
   PowerShell guard and synchronization utilities.

## Non-negotiable Codex rule

Codex may:

- read;
- clone;
- fetch;
- inspect history;
- compare local implementation with `origin/main`.

Codex may not:

- push;
- force-push;
- create/update/delete remote refs;
- write repository contents via GitHub API;
- create/merge implementation PRs;
- publish releases;
- change Pages/settings/rulesets/branch protection;
- weaken the local read-only guard.

## Local implementation target contract

Every local task must bind itself to an explicit upstream target:

```text
target_repository: Space653000/0_JN1_AERIS
target_branch: main
target_ref: origin/main
target_sha: <recorded SHA>
remote_write_performed: NO
```

If local code differs from the current target, that difference is **local implementation drift**, not a reason for Codex to update GitHub.

A change to the canonical GitHub target is a separate Human-controlled publishing decision.

## Enforcement layers

```text
Layer 1  AGENTS.md                 behavioral authority
Layer 2  aeris.policy.yaml         machine-readable policy
Layer 3  disabled origin push URL  Git transport guard
Layer 4  deny pre-push hook        independent local hard stop
Layer 5  Human publication gate    remote update authority
```

Important limitation:

> Repository files cannot revoke an externally granted GitHub token/App permission. For absolute remote enforcement, Codex must not be given GitHub write credentials for this repository, or GitHub-side rules/permissions must deny them. The repository guard remains mandatory even when such external controls exist.
