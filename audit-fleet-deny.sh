#!/usr/bin/env bash
# audit-fleet-deny.sh — Sprint 12-4
#
# Walks every workspace in ~/SEO-Agents/, reads each .claude/settings.json,
# reports per-workspace which deny rules conflict with bulk-HTTP fetch tools.
#
# Exit codes:
#   0 — all workspaces clean (no conflicts)
#   1 — at least one workspace has conflicts (CI hygiene gate)
#   2 — usage / setup error
#
# Usage:
#   bash audit-fleet-deny.sh                       # walk default ~/SEO-Agents/
#   bash audit-fleet-deny.sh --root <path>         # custom root
#   bash audit-fleet-deny.sh --json                # machine-readable output
#   bash audit-fleet-deny.sh --help

set -euo pipefail

ROOT="${HOME}/SEO-Agents"
JSON_OUTPUT=0

usage() {
  sed -n '/^# Usage:/,/^set -euo/p' "$0" | grep '^#' | sed 's/^# \?//'
}

while [ $# -gt 0 ]; do
  case "$1" in
    --root) ROOT="$2"; shift 2 ;;
    --json) JSON_OUTPUT=1; shift ;;
    --help|-h) usage; exit 0 ;;
    *) echo "Unknown arg: $1" >&2; usage; exit 2 ;;
  esac
done

[ -d "$ROOT" ] || { echo "ERROR: root not found: $ROOT" >&2; exit 2; }

# Run the audit via python (handles JSON parsing cleanly; uses only stdlib)
python3 - "$ROOT" "$JSON_OUTPUT" <<'PYEOF'
import json, sys, os, re
from pathlib import Path

root = Path(sys.argv[1])
json_output = sys.argv[2] == "1"

MONITORED_TOOLS = ["curl", "wget", "httpie", "http"]

def detect_conflicts(deny_list):
    """Return list of (rule, tool, suggested_replacement) for each conflicting deny."""
    conflicts = []
    for rule in deny_list:
        for tool in MONITORED_TOOLS:
            if rule.startswith(f"Bash({tool}") and "http://" not in rule:
                suggested = f'"Bash({tool} http://*)"'
                conflicts.append({
                    "rule": rule,
                    "tool": tool,
                    "suggested_replacement": suggested,
                })
                break
    return conflicts

workspaces = sorted([p for p in root.iterdir() if p.is_dir() and not p.name.startswith(".")])
results = []
any_conflict = False
any_missing_settings = False

for ws in workspaces:
    settings_path = ws / ".claude" / "settings.json"
    entry = {"workspace": ws.name, "settings_path": str(settings_path)}
    if not settings_path.exists():
        entry["status"] = "no_settings_json"
        entry["conflicts"] = []
        any_missing_settings = True
    else:
        try:
            data = json.loads(settings_path.read_text())
            deny = data.get("permissions", {}).get("deny", [])
            allow_count = len(data.get("permissions", {}).get("allow", []))
            conflicts = detect_conflicts(deny)
            entry["status"] = "conflicts" if conflicts else "clean"
            entry["allow_count"] = allow_count
            entry["deny_count"] = len(deny)
            entry["conflicts"] = conflicts
            if conflicts:
                any_conflict = True
        except json.JSONDecodeError as e:
            entry["status"] = "invalid_json"
            entry["error"] = str(e)
            entry["conflicts"] = []
            any_missing_settings = True
    results.append(entry)

if json_output:
    print(json.dumps({
        "root": str(root),
        "workspace_count": len(workspaces),
        "any_conflict": any_conflict,
        "results": results,
    }, indent=2))
else:
    # Human-readable table
    print(f"")
    print(f"=== SEO-Agent Fleet Deny-Conflict Audit ===")
    print(f"Root: {root}")
    print(f"Workspaces: {len(workspaces)}")
    print(f"")
    print(f"{'Workspace':<28} {'Status':<14} {'Allow':>6} {'Deny':>6} {'Conflicts':>10}")
    print(f"{'-'*28} {'-'*14} {'-'*6} {'-'*6} {'-'*10}")
    for r in results:
        if r["status"] == "no_settings_json":
            print(f"{r['workspace']:<28} {'no settings':<14}")
        elif r["status"] == "invalid_json":
            print(f"{r['workspace']:<28} {'INVALID JSON':<14}")
        else:
            n_conflicts = len(r["conflicts"])
            print(f"{r['workspace']:<28} {r['status']:<14} {r['allow_count']:>6} {r['deny_count']:>6} {n_conflicts:>10}")

    # Per-conflict detail
    conflicted = [r for r in results if r.get("conflicts")]
    if conflicted:
        print(f"")
        print(f"=== Per-conflict detail ===")
        for r in conflicted:
            print(f"")
            print(f"  {r['workspace']}: {len(r['conflicts'])} conflict(s)")
            print(f"  settings: {r['settings_path']}")
            for c in r["conflicts"]:
                print(f"")
                print(f"    Conflict: {c['rule']!r} blocks ALL {c['tool']}")
                print(f"    Fix in deny block:")
                print(f"      REPLACE:  \"{c['rule']}\",")
                print(f"      WITH:     {c['suggested_replacement']},")

    # Summary
    n_conflict = sum(1 for r in results if r.get("conflicts"))
    n_clean = sum(1 for r in results if r["status"] == "clean")
    n_missing = sum(1 for r in results if r["status"] in ("no_settings_json", "invalid_json"))
    print(f"")
    print(f"=== Summary ===")
    print(f"  clean:        {n_clean}")
    print(f"  with conflict: {n_conflict}")
    print(f"  no/bad settings: {n_missing}")
    print(f"")
    print(f"See field-manual/permission-conflicts.md for resolution guidance.")
    print(f"")

# Exit code: 1 if any conflict, 0 if clean
sys.exit(1 if any_conflict else 0)
PYEOF
