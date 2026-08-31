param(
    [Parameter(Mandatory=$true)]
    [string]$TargetPath,

    [Parameter(Mandatory=$false)]
    [string]$LocalBranch = "local/bootstrap"
)

$ErrorActionPreference = "Stop"
$RepoUrl = "https://github.com/Space653000/0_JN1_AERIS.git"

if (Test-Path $TargetPath) {
    $items = Get-ChildItem -Force -Path $TargetPath -ErrorAction SilentlyContinue
    if ($items.Count -gt 0) {
        throw "TargetPath already exists and is not empty: $TargetPath"
    }
}

$Parent = Split-Path -Parent $TargetPath
if ($Parent) { New-Item -ItemType Directory -Force -Path $Parent | Out-Null }

Write-Host "Cloning AERIS canonical target..." -ForegroundColor Cyan
git clone $RepoUrl $TargetPath
if ($LASTEXITCODE -ne 0) { throw "git clone failed" }

$Protect = Join-Path $TargetPath "tools\local-only\Protect-AERISReadOnly.ps1"
$Verify = Join-Path $TargetPath "tools\local-only\Verify-AERISReadOnly.ps1"

& $Protect -RepoPath $TargetPath
if ($LASTEXITCODE -ne 0) { throw "read-only protection failed" }

Push-Location $TargetPath
try {
    git fetch origin main
    if ($LASTEXITCODE -ne 0) { throw "git fetch origin main failed" }

    git switch -c $LocalBranch origin/main
    if ($LASTEXITCODE -ne 0) { throw "failed to create local implementation branch: $LocalBranch" }

    New-Item -ItemType Directory -Force -Path ".aeris" | Out-Null
    $TargetSha = (git rev-parse origin/main).Trim()
    [System.IO.File]::WriteAllText(
        ".aeris\target-main.sha",
        "$TargetSha`n",
        (New-Object System.Text.UTF8Encoding($false))
    )
}
finally {
    Pop-Location
}

& $Verify -RepoPath $TargetPath
if ($LASTEXITCODE -ne 0) { throw "read-only verification failed" }

Write-Host "" 
Write-Host "AERIS local workspace created." -ForegroundColor Green
Write-Host "Path        : $TargetPath"
Write-Host "Local branch: $LocalBranch"
Write-Host "Remote      : READ/FETCH ONLY"
Write-Host "Push        : DENIED"
Write-Host "Codex mode  : LOCAL IMPLEMENTATION ONLY" -ForegroundColor Cyan
