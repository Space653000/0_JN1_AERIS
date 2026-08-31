param(
    [Parameter(Mandatory=$false)]
    [string]$RepoPath = "."
)

$ErrorActionPreference = "Stop"

Push-Location $RepoPath
try {
    $VerifyScript = Join-Path $PSScriptRoot "Verify-AERISReadOnly.ps1"
    & $VerifyScript -RepoPath "."
    if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

    Write-Host "Fetching canonical AERIS target: origin/main..." -ForegroundColor Cyan
    git fetch --prune origin main
    if ($LASTEXITCODE -ne 0) { throw "git fetch origin main failed" }

    $TargetSha = (git rev-parse origin/main).Trim()
    $CurrentBranch = (git branch --show-current).Trim()

    New-Item -ItemType Directory -Force -Path ".aeris" | Out-Null
    [System.IO.File]::WriteAllText(
        (Join-Path ".aeris" "target-main.sha"),
        "$TargetSha`n",
        (New-Object System.Text.UTF8Encoding($false))
    )

    Write-Host "Target baseline updated." -ForegroundColor Green
    Write-Host "Target remote : Space653000/0_JN1_AERIS"
    Write-Host "Target branch : main"
    Write-Host "Target SHA    : $TargetSha"
    Write-Host "Local branch  : $CurrentBranch"
    Write-Host "Marker        : .aeris/target-main.sha"
    Write-Host "Remote write performed: NO" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "Local drift summary vs origin/main:" -ForegroundColor Yellow
    git status --short
    git diff --stat origin/main...HEAD
}
finally {
    Pop-Location
}
