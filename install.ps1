# Claude Design — Plugin Install Verifier (Windows / PowerShell)
# Run from repo root:  .\install.ps1

$ErrorActionPreference = 'Stop'

$repo = $PSScriptRoot
Write-Host ""
Write-Host "Claude Design — Plugin install verifier" -ForegroundColor Cyan
Write-Host "Repo root: $repo"
Write-Host ""

$checks = @(
    @{ path = ".claude-plugin\marketplace.json";                              label = "Marketplace manifest" }
    @{ path = "plugins\claude-design\.claude-plugin\plugin.json";             label = "Plugin manifest" }
    @{ path = "plugins\claude-design\agents";                                 label = "Agents directory"; isDir = $true }
    @{ path = "plugins\claude-design\skills\claude-design\SKILL.md";          label = "Skill entry" }
)

$allOk = $true
foreach ($c in $checks) {
    $full = Join-Path $repo $c.path
    $exists = if ($c.isDir) { Test-Path $full -PathType Container } else { Test-Path $full -PathType Leaf }
    $mark = if ($exists) { "[OK]" } else { "[MISS]"; $allOk = $false }
    $color = if ($exists) { "Green" } else { "Red" }
    Write-Host "  $mark  $($c.label.PadRight(22))  $($c.path)" -ForegroundColor $color
}

if (-not $allOk) {
    Write-Host ""
    Write-Host "FAIL: missing required files. Re-clone or restore the repo and retry." -ForegroundColor Red
    exit 1
}

# count agents
$agentCount = (Get-ChildItem (Join-Path $repo "plugins\claude-design\agents") -Filter '*.md').Count
Write-Host "  [OK]  Agent count            $agentCount agent .md files" -ForegroundColor Green

# parse marketplace name (defensive — may not be JSON-valid in all PS versions)
$marketplaceName = "claude-design-local"
try {
    $mp = Get-Content (Join-Path $repo ".claude-plugin\marketplace.json") -Raw | ConvertFrom-Json
    if ($mp.name) { $marketplaceName = $mp.name }
} catch {}

Write-Host ""
Write-Host "Structure verified. Run these inside Claude Code — ONE AT A TIME (do NOT paste all 3 lines together):" -ForegroundColor Yellow
Write-Host ""
Write-Host "  Step 1)  /plugin marketplace add" -ForegroundColor White
Write-Host "           (press Enter — interactive prompt 'Enter marketplace source:' will appear)" -ForegroundColor DarkGray
Write-Host "           paste this path into the prompt:" -ForegroundColor DarkGray
Write-Host "           $repo" -ForegroundColor Cyan
Write-Host ""
Write-Host "  Step 2)  /plugin install claude-design@$marketplaceName" -ForegroundColor White
Write-Host ""
Write-Host "  Step 3)  /reload-plugins" -ForegroundColor White
Write-Host ""
Write-Host "Tip: pasting all 3 lines at once breaks Step 1 — the path arg gets eaten by the prompt." -ForegroundColor DarkYellow
Write-Host ""
Write-Host "Verify with:" -ForegroundColor Yellow
Write-Host "  /plugin                       (Installed tab should list 'claude-design')" -ForegroundColor White
Write-Host "  /claude-design                (skill should activate)" -ForegroundColor White
Write-Host ""
Write-Host "After install, the Agent tool can call:" -ForegroundColor Yellow
Write-Host "  subagent_type: claude-design:project-planner"
Write-Host "  subagent_type: claude-design:design-system-manager"
Write-Host "  subagent_type: claude-design:slide-deck-agent"
Write-Host "  ... (13 sub-agents total)"
Write-Host ""

# clipboard copy — only the repo path (which is the prompt input for Step 1)
if (Get-Command Set-Clipboard -ErrorAction SilentlyContinue) {
    Set-Clipboard -Value $repo
    Write-Host "  (repo path copied to clipboard — paste into Step 1's 'Enter marketplace source:' prompt)" -ForegroundColor DarkGray
    Write-Host ""
}
