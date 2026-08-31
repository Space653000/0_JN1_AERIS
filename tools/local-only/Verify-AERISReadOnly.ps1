param(
    [Parameter(Mandatory=$false)]
    [string]$RepoPath = "."
)

$ErrorActionPreference = "Stop"
$ExpectedFetchUrl = "https://github.com/Space653000/0_JN1_AERIS.git"
$ExpectedPushUrl = "DISABLED://AERIS-REMOTE-READ-ONLY"
$Failures = @()

Push-Location $RepoPath
try {
    git rev-parse --is-inside-work-tree | Out-Null
    if ($LASTEXITCODE -ne 0) { throw "Not a Git worktree: $RepoPath" }

    $FetchUrl = (git remote get-url origin).Trim()
    $PushUrl = (git remote get-url --push origin).Trim()
    $HookPath = git rev-parse --git-path hooks/pre-push

    if ($FetchUrl -ne $ExpectedFetchUrl) {
        $Failures += "origin fetch URL is '$FetchUrl' (expected '$ExpectedFetchUrl')"
    }
    if ($PushUrl -ne $ExpectedPushUrl) {
        $Failures += "origin push URL is '$PushUrl' (expected disabled push URL)"
    }
    if (-not (Test-Path $HookPath)) {
        $Failures += "pre-push deny hook is missing: $HookPath"
    }
    elseif (-not ((Get-Content -Raw $HookPath) -match "AERIS REMOTE WRITE DENIED")) {
        $Failures += "pre-push hook exists but is not the AERIS deny hook"
    }

    if ($Failures.Count -gt 0) {
        Write-Host "AERIS READ-ONLY GUARD: FAIL" -ForegroundColor Red
        $Failures | ForEach-Object { Write-Host " - $_" -ForegroundColor Red }
        Write-Host "Run tools/local-only/Protect-AERISReadOnly.ps1 before Codex continues." -ForegroundColor Yellow
        exit 2
    }

    $OriginSha = $null
    git show-ref --verify --quiet refs/remotes/origin/main
    if ($LASTEXITCODE -eq 0) {
        $OriginSha = (git rev-parse origin/main).Trim()
    }

    Write-Host "AERIS READ-ONLY GUARD: PASS" -ForegroundColor Green
    Write-Host "Fetch URL : $FetchUrl"
    Write-Host "Push URL  : $PushUrl"
    Write-Host "Pre-push  : DENY"
    if ($OriginSha) { Write-Host "origin/main: $OriginSha" }
    Write-Host "Remote write performed: NO" -ForegroundColor Cyan
}
finally {
    Pop-Location
}
