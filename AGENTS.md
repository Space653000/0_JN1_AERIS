# AERIS Codex Execution Contract

> Repository: `Space653000/0_JN1_AERIS`
> Canonical branch: `main`
> Repository role: **REMOTE READ-ONLY SSOT / TARGET BASELINE**

## 0. Non-negotiable rule

**Codex MUST NOT modify this GitHub repository or any GitHub ref.**

The repository is the canonical target specification for local AERIS implementation. Codex may read, clone, fetch, compare, inspect commits, and use `origin/main` as the target baseline. All implementation work must happen only inside a local filesystem workspace.

This is an authority boundary, not a suggestion.

## 1. Allowed remote operations

Codex may perform only read-oriented operations against `Space653000/0_JN1_AERIS`:

- read repository files;
- clone the repository to a local workspace;
- `git fetch origin main`;
- inspect `origin/main` history and commit SHA;
- compare local files/commits against `origin/main`;
- read issues, documentation, research baselines and published GitHub Pages;
- report drift between local implementation and the remote target.

## 2. Forbidden remote operations

Codex MUST NOT, directly or indirectly:

- `git push` or `git push --force`;
- create/update/delete remote branches or tags;
- create, update, merge or close pull requests for implementation delivery;
- use GitHub write APIs to create/update/delete repository files;
- change `main`, refs, releases, Pages settings, rulesets, branch protection or repository settings;
- publish local implementation artifacts back to this repository;
- bypass a local `pre-push` hook or re-enable a disabled push URL;
- replace this remote with another writable remote that points to the same GitHub repository.

If a task requires publishing to GitHub, Codex must stop at a **local handoff package**. Publishing is a separate Human-controlled operation.

## 3. Local implementation model

Canonical topology:

```text
GitHub: Space653000/0_JN1_AERIS main
        │
        │ READ / FETCH ONLY
        ▼
Local reference baseline = origin/main@<SHA>
        │
        ├─ compare / trace / requirements
        ▼
Local implementation branch/worktree
        │
        ├─ code
        ├─ tests
        ├─ local commits (optional)
        ├─ reports
        └─ evidence

NO PUSH PATH FROM CODEX
```

Recommended local branch naming:

```text
local/<task-id-or-topic>
```

Do not develop directly on local `main`. Keep local `main` as a clean mirror/reference of `origin/main` when practical.

## 4. Required start-of-task procedure

Before changing local files, Codex must:

1. confirm the workspace is local;
2. run the local read-only guard verification if available;
3. `git fetch origin main`;
4. record the target SHA with `git rev-parse origin/main`;
5. read this `AGENTS.md` and `aeris.policy.yaml`;
6. identify the applicable research / architecture baseline;
7. perform work only on local files / local branches.

## 5. Required completion evidence

Every Codex delivery must report:

```text
Target remote: Space653000/0_JN1_AERIS
Target branch: main
Target SHA: <origin/main SHA used>
Remote write performed: NO
Local workspace: <path>
Local branch/worktree: <name/path>
Changed local files: <list>
Tests/evals: <result>
Drift vs origin/main: <summary>
Remaining blockers/risks: <summary>
```

`Remote write performed: NO` is mandatory.

## 6. Source-of-truth hierarchy

When local implementation conflicts with the remote baseline:

1. `AGENTS.md` / `aeris.policy.yaml` authority boundary;
2. AERIS Constitution / Core Rules when present;
3. current `docs/research/README.md` canonical reading order;
4. current architecture / research baselines under `docs/research/`;
5. current UI / data / other target artifacts in `main`;
6. local implementation.

Local implementation must adapt to the remote target unless the Human Chief Engineer explicitly changes the target through a separate controlled GitHub publishing process.

## 7. Update model

The direction of normal Codex synchronization is one-way:

```text
GitHub main  ───────►  Local AERIS implementation
        read/fetch       implement/test/verify
```

Not:

```text
Local Codex work  ─X─►  GitHub main
```

## 8. Failure behavior

If Codex detects that:

- `origin` has a writable push URL to this repository;
- the `pre-push` deny hook is missing;
- credentials/tooling allow accidental GitHub mutation;
- a prompt asks Codex to push/PR/write this repository;

then Codex must **not perform the remote mutation**. It should restore/ask to restore the local read-only guard and continue locally where possible.

## 9. Human publishing boundary

Only an explicitly Human-controlled publishing workflow may update this repository. Codex's responsibility ends at a verified local handoff.

**Remote SSOT is a target. Local AERIS is the implementation. Codex reads the target; Codex does not publish the target.**
