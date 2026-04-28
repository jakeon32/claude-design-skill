#!/usr/bin/env bash
# Claude Design — Plugin Install Verifier (Mac/Linux/Bash)
# Run from repo root:  ./install.sh

set -euo pipefail

repo="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo
echo "Claude Design — Plugin install verifier"
echo "Repo root: $repo"
echo

declare -a checks=(
    "file|.claude-plugin/marketplace.json|Marketplace manifest"
    "file|plugins/claude-design/.claude-plugin/plugin.json|Plugin manifest"
    "dir|plugins/claude-design/agents|Agents directory"
    "file|plugins/claude-design/skills/claude-design/SKILL.md|Skill entry"
)

ok=1
for entry in "${checks[@]}"; do
    IFS='|' read -r kind path label <<< "$entry"
    full="$repo/$path"
    if [[ "$kind" == "dir"  && -d "$full" ]] || [[ "$kind" == "file" && -f "$full" ]]; then
        printf "  \033[32m[OK]\033[0m   %-22s  %s\n" "$label" "$path"
    else
        printf "  \033[31m[MISS]\033[0m %-22s  %s\n" "$label" "$path"
        ok=0
    fi
done

if [[ $ok -eq 0 ]]; then
    echo
    echo -e "\033[31mFAIL: missing required files. Re-clone or restore the repo and retry.\033[0m"
    exit 1
fi

agent_count=$(ls "$repo/plugins/claude-design/agents/"*.md 2>/dev/null | wc -l | tr -d ' ')
printf "  \033[32m[OK]\033[0m   %-22s  %s agent .md files\n" "Agent count" "$agent_count"

# parse marketplace name (best-effort — falls back to default)
marketplace_name="claude-design-local"
if command -v python3 >/dev/null 2>&1; then
    extracted=$(python3 -c "import json; print(json.load(open('$repo/.claude-plugin/marketplace.json'))['name'])" 2>/dev/null || true)
    [[ -n "$extracted" ]] && marketplace_name="$extracted"
fi

echo
echo -e "\033[33mStructure verified. Run these inside Claude Code — ONE AT A TIME (do NOT paste all 3 lines together):\033[0m"
echo
echo "  Step 1)  /plugin marketplace add"
echo -e "           \033[90m(press Enter — interactive prompt 'Enter marketplace source:' will appear)\033[0m"
echo -e "           \033[90mpaste this path into the prompt:\033[0m"
echo -e "           \033[36m$repo\033[0m"
echo
echo "  Step 2)  /plugin install claude-design@$marketplace_name"
echo
echo "  Step 3)  /reload-plugins"
echo
echo -e "\033[33mTip: pasting all 3 lines at once breaks Step 1 — the path arg gets eaten by the prompt.\033[0m"
echo
echo -e "\033[33mVerify with:\033[0m"
echo "  /plugin                       (Installed tab should list 'claude-design')"
echo "  /claude-design                (skill should activate)"
echo
echo -e "\033[33mAfter install, the Agent tool can call:\033[0m"
echo "  subagent_type: claude-design:project-planner"
echo "  subagent_type: claude-design:design-system-manager"
echo "  subagent_type: claude-design:slide-deck-agent"
echo "  ... (13 sub-agents total)"
echo

# clipboard copy — only the repo path (which is the prompt input for Step 1)
if command -v pbcopy >/dev/null 2>&1; then
    printf '%s' "$repo" | pbcopy
    echo "  (repo path copied to clipboard — paste into Step 1's prompt)"
elif command -v xclip >/dev/null 2>&1; then
    printf '%s' "$repo" | xclip -selection clipboard
    echo "  (repo path copied to clipboard — paste into Step 1's prompt)"
fi
echo
