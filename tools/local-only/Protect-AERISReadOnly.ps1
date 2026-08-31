param(
    [Parameter(Mandatory=$false)]
    [string]$RepoPath = "."
)

$ErrorActionPreference = "Stop"
$ExpectedFetchUrl = "https://github.com/Space653000/0_JN1_AERIS.git"
$DisabledPushUrl = "DISABLED://AERIS-REMOTE-READ-ONLY"

Push-Location $RepoPath
try {
    git rev-parse --is-inside-work-tree | Out-Null
    if ($LASTEXITCODE -ne 0) { throw "Not a Git worktree: $RepoPath" }

    if (-not (git remote | Select-String -SimpleMatch "origin")) {
        git remote add origin $ExpectedFetchUrl
    }

    # Keep fetch/read access pointed at the canonical AERIS target.
    git remote set-url origin $ExpectedFetchUrl

    # Disable push at the remote configuration layer.
    git remote set-url --push origin $DisabledPushUrl

    # Add a second independent hard stop at the Git hook layer.
    $HookPath = git rev-parse --git-path hooks/pre-push
    $HookDir = Split-Path -Parent $HookPath
    New-Item -ItemType Directory -Force -Path $HookDir | Out-Null

    $Hook = @'
#!/bin/sh
echo "AERIS REMOTE WRITE DENIED: Codex/local implementation may not push to Space653000/0_JN1_AERIS." >&2
echo "Remote main is a read-only SSOT/target. Keep implementation local and prepare a human-controlled handoff instead." >&2
exit 1
'@
    [System.IO.File]::WriteAllText($HookPath, $Hook, (New-Object System.Text.UTF8Encoding($false)))

    git config remote.origin.prune true
    git config fetch.prune true

    Write-Host "AERIS read-only guard installed." -ForegroundColor Green
    Write-Host "Fetch URL : $(git remote get-url origin)"
    Write-Host "Push URL  : $(git remote get-url --push origin)"
    Write-Host "Pre-push  : $HookPath"
    Write-Host "Policy    : REMOTE READ-ONLY / LOCAL IMPLEMENTATION ONLY" -ForegroundColor Cyan
}
finally {
    Pop-Location
}
