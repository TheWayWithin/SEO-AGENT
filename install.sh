#!/usr/bin/env bash
# SEO-Agent installer (single-site)
#
# Installs the SEO-Agent product layer (agents, missions, commands, templates,
# routines) into a target workspace. Designed to overlay an existing Agent-11 v6
# framework install — only adds SEO-specific files; preserves framework files.
#
# Usage:
#   bash install.sh <target-dir> [options]
#
# Options:
#   --clone-from <url>   Clone the given remote into <target-dir> first (target
#                        must not exist or must be empty). Implies --branch=main
#                        unless --branch is also given.
#   --branch <branch>    Branch to clone (default: main). Used with --clone-from.
#   --upgrade            Refresh SEO product files only; preserve site-specific
#                        config (seo-evidence.md, tracking/config/, .gitignore,
#                        CLAUDE.md). Use after first install to update.
#   --force              Overwrite even site-specific files (CLAUDE.md, etc.).
#   --dry-run            Print what would change; do not modify the filesystem.
#   --help, -h           This message.
#
# Hard safety rule:
#   Refuses any target path starting with /Users/jamiewatters/DevProjects/.
#   Those are dev repos; SEO workspaces live under ~/SEO-Agents/.
#
# Examples:
#   # Install into existing workspace (you cloned manually):
#   bash install.sh ~/SEO-Agents/freecalchub
#
#   # Clone + install in one step:
#   bash install.sh ~/SEO-Agents/aisearchmastery \
#     --clone-from https://github.com/TheWayWithin/aisearchmastery.git
#
#   # Refresh SEO files in an existing install:
#   bash install.sh ~/SEO-Agents/freecalchub --upgrade --dry-run

set -euo pipefail

# ---- Locate source ----
SOURCE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SOURCE_COMMIT="$(cd "$SOURCE" && git rev-parse --short HEAD 2>/dev/null || echo "unknown")"

# ---- Defaults ----
TARGET=""
CLONE_FROM=""
CLONE_BRANCH="main"
MODE="install"   # install | upgrade
FORCE=0
DRY_RUN=0

# ---- Helpers ----
usage() {
  sed -n '/^# Usage:/,/^set -euo/p' "$0" | grep '^#' | sed 's/^# \?//'
}

err() { echo "ERROR: $*" >&2; exit 1; }
note() { echo "  $*"; }
phase() { echo ""; echo "=== $* ==="; }

run() {
  if [ "$DRY_RUN" = "1" ]; then
    echo "  WOULD RUN: $*"
  else
    "$@"
  fi
}

copy_file() {
  local src="$1" dst="$2" preserve="${3:-0}"
  if [ ! -e "$src" ]; then
    note "SKIP (source missing): $src"
    return
  fi
  if [ -e "$dst" ] && [ "$preserve" = "1" ] && [ "$FORCE" = "0" ]; then
    note "PRESERVE: $dst (exists; use --force to overwrite)"
    return
  fi
  if [ "$DRY_RUN" = "1" ]; then
    if [ -e "$dst" ]; then
      note "WOULD OVERWRITE: $dst"
    else
      note "WOULD CREATE:    $dst"
    fi
  else
    cp "$src" "$dst"
    note "wrote: $dst"
  fi
}

# ---- Parse args ----
while [ $# -gt 0 ]; do
  case "$1" in
    --clone-from) CLONE_FROM="$2"; shift 2 ;;
    --branch) CLONE_BRANCH="$2"; shift 2 ;;
    --upgrade) MODE="upgrade"; shift ;;
    --force) FORCE=1; shift ;;
    --dry-run) DRY_RUN=1; shift ;;
    --help|-h) usage; exit 0 ;;
    -*) err "Unknown option: $1" ;;
    *) [ -z "$TARGET" ] && TARGET="$1" || err "Multiple targets given: $TARGET and $1"; shift ;;
  esac
done

[ -z "$TARGET" ] && { usage; err "Target directory required"; }

# ---- Hard safety rule: refuse DevProjects ----
case "$TARGET" in
  /Users/jamiewatters/DevProjects/*|"$HOME/DevProjects/"*)
    err "REFUSED: target $TARGET is under ~/DevProjects/. SEO workspaces must live under ~/SEO-Agents/. This is a hard safety rule."
    ;;
esac

# ---- Clone if requested ----
if [ -n "$CLONE_FROM" ]; then
  phase "Clone phase"
  if [ -e "$TARGET" ] && [ "$(ls -A "$TARGET" 2>/dev/null)" ]; then
    err "Target $TARGET exists and is not empty. Cannot clone into it. Remove --clone-from or clear the target."
  fi
  PARENT="$(dirname "$TARGET")"
  run mkdir -p "$PARENT"
  if [ "$DRY_RUN" = "1" ]; then
    note "WOULD RUN: git clone --branch $CLONE_BRANCH $CLONE_FROM $TARGET"
  else
    git clone --branch "$CLONE_BRANCH" "$CLONE_FROM" "$TARGET" || err "Clone failed"
    note "cloned into $TARGET (branch: $CLONE_BRANCH)"
  fi
fi

# ---- Validate target exists ----
if [ "$DRY_RUN" = "0" ]; then
  [ -d "$TARGET" ] || err "Target dir not found: $TARGET (did the clone fail?)"
  TARGET="$(cd "$TARGET" && pwd)"  # canonicalise
fi

# ---- Re-check safety after canonicalisation ----
case "$TARGET" in
  /Users/jamiewatters/DevProjects/*|"$HOME/DevProjects/"*)
    err "REFUSED post-canonicalisation: $TARGET resolves under ~/DevProjects/."
    ;;
esac

# ---- Detect existing install ----
EXISTING_INSTALL=0
if [ -e "$TARGET/.seo-agent-version" ]; then
  EXISTING_INSTALL=1
  note "Detected existing SEO-Agent install at $TARGET"
  if [ "$MODE" = "install" ]; then
    note "Switching MODE to 'upgrade' (use --force to override)."
    [ "$FORCE" = "0" ] && MODE="upgrade"
  fi
fi

phase "Install plan"
echo "  source:        $SOURCE (commit $SOURCE_COMMIT)"
echo "  target:        $TARGET"
echo "  mode:          $MODE"
echo "  force:         $FORCE"
echo "  dry-run:       $DRY_RUN"
echo "  clone-from:    ${CLONE_FROM:-<none>}"

# ---- Phase 1: Directories ----
phase "Phase 1: Ensure directories"
for dir in .claude/agents .claude/missions .claude/commands templates/deliverables routines runs tracking/config; do
  if [ "$DRY_RUN" = "1" ]; then
    note "WOULD MKDIR: $TARGET/$dir"
  else
    mkdir -p "$TARGET/$dir"
    note "ensured: $TARGET/$dir"
  fi
done

# ---- Phase 2: SEO agents ----
phase "Phase 2: SEO agents (7) — added alongside framework agents"
for agent in seo-strategist seo-coordinator seo-technical seo-content seo-researcher seo-analyst seo-builder; do
  copy_file "$SOURCE/.claude/agents/$agent.md" "$TARGET/.claude/agents/$agent.md"
done

# ---- Phase 3: SEO missions ----
phase "Phase 3: SEO missions (5)"
for mission in site-audit content-gap technical-fix ai-search-optimize sitewide-verify; do
  copy_file "$SOURCE/.claude/missions/$mission.md" "$TARGET/.claude/missions/$mission.md"
done

# ---- Phase 4: SEO commands ----
phase "Phase 4: SEO commands (3) — added alongside framework commands"
for cmd in seo-commands track tracking-commands; do
  copy_file "$SOURCE/.claude/commands/$cmd.md" "$TARGET/.claude/commands/$cmd.md"
done

# ---- Phase 5: SEO-augmented coord.md (REPLACES framework version) ----
phase "Phase 5: coord.md (REPLACES framework version with SEO Mode D)"
copy_file "$SOURCE/.claude/commands/coord.md" "$TARGET/.claude/commands/coord.md"

# ---- Phase 6: Deliverable templates ----
phase "Phase 6: Deliverable templates (4)"
for f in README.md analysis-report.md marketing-report.md aimpactscanner-data.schema.json; do
  copy_file "$SOURCE/templates/deliverables/$f" "$TARGET/templates/deliverables/$f"
done

# ---- Phase 7: Evidence template ----
phase "Phase 7: Evidence template"
copy_file "$SOURCE/templates/seo-evidence-template.md" "$TARGET/templates/seo-evidence-template.md"

# ---- Phase 8: Routine templates ----
phase "Phase 8: Routine templates (3)"
for f in README.md weekly-snapshot.md monthly-report.md; do
  copy_file "$SOURCE/routines/$f" "$TARGET/routines/$f"
done

# ---- Phase 9: runs/ landing zone ----
phase "Phase 9: runs/ landing zone"
if [ "$DRY_RUN" = "0" ]; then
  touch "$TARGET/runs/.gitkeep"
  note "ensured: $TARGET/runs/.gitkeep"
else
  note "WOULD TOUCH: $TARGET/runs/.gitkeep"
fi

# ---- Phase 10: Site-specific files (preserved on upgrade) ----
phase "Phase 10: Site-specific files (init only on first install; preserved on upgrade)"
if [ "$MODE" = "install" ] && [ "$EXISTING_INSTALL" = "0" ]; then
  # CLAUDE.md handling: preserve existing if present
  if [ -e "$TARGET/CLAUDE.md" ] && [ ! -e "$TARGET/CLAUDE-product-dev.md" ]; then
    if [ "$DRY_RUN" = "1" ]; then
      note "WOULD MOVE: $TARGET/CLAUDE.md → $TARGET/CLAUDE-product-dev.md"
    else
      mv "$TARGET/CLAUDE.md" "$TARGET/CLAUDE-product-dev.md"
      note "preserved existing CLAUDE.md → CLAUDE-product-dev.md"
    fi
  fi
  copy_file "$SOURCE/CLAUDE.md" "$TARGET/CLAUDE.md" 1

  # seo-evidence.md (site-specific rolling artefact store)
  copy_file "$SOURCE/templates/seo-evidence-template.md" "$TARGET/seo-evidence.md" 1

  # .gitignore (only if missing)
  if [ ! -e "$TARGET/.gitignore" ]; then
    if [ "$DRY_RUN" = "1" ]; then
      note "WOULD CREATE: $TARGET/.gitignore"
    else
      cat > "$TARGET/.gitignore" <<'GITIGNORE'
# Sensitive credentials — never commit
.env
.env.*
!.env*.template

# OS / editor noise
.DS_Store
*.swp
*.swo
__pycache__/
*.pyc
GITIGNORE
      note "created: $TARGET/.gitignore"
    fi
  else
    note "PRESERVE existing $TARGET/.gitignore (manually verify .env* protection)"
  fi
else
  note "MODE=$MODE, existing_install=$EXISTING_INSTALL — site-specific files left alone"
fi

# ---- Phase 11: Curl allowlist for workspace's public_url (Sprint 11-C) ----
phase "Phase 11: Curl allowlist for workspace public_url (Sprint 11-C)"

REGISTRY="${SEO_FLEET_REGISTRY:-/Users/jamiewatters/Shared/tools/agent-11-fleet/seo-fleet-registry.yaml}"
WS_BASENAME="$(basename "$TARGET")"

if [ ! -f "$REGISTRY" ]; then
  note "SKIP: registry not found at $REGISTRY; manual settings.json edit required for sitewide-verify"
else
  PUBLIC_URL=$(python3 - <<PYEOF
import re, sys
content = open("$REGISTRY").read()
ws = "$WS_BASENAME"
pat_name = re.compile(rf'^\s+-\s+name:\s+"?{re.escape(ws)}"?\s*$', re.MULTILINE)
m = pat_name.search(content)
if m:
    after = content[m.end():m.end()+800]  # peek next ~15 lines
    pat_url = re.compile(r'^\s+public_url:\s+(.+)$', re.MULTILINE)
    u = pat_url.search(after)
    if u:
        url = u.group(1).strip().strip('"')
        print(url)
PYEOF
)

  if [ -z "$PUBLIC_URL" ] || [ "$PUBLIC_URL" = "TBD" ] || [ "$PUBLIC_URL" = "null" ]; then
    note "SKIP: no public_url for $WS_BASENAME in registry (got: '${PUBLIC_URL:-<empty>}'). sitewide-verify will require manual settings.json edit."
  else
    PUBLIC_URL="${PUBLIC_URL%/}"
    DOMAIN=$(echo "$PUBLIC_URL" | sed -E 's|^https?://([^/]+).*|\1|')
    note "public_url: $PUBLIC_URL → domain: $DOMAIN"

    SETTINGS="$TARGET/.claude/settings.json"
    if [ "$DRY_RUN" = "1" ]; then
      note "WOULD MERGE curl allowlist for $DOMAIN into $SETTINGS"
    else
      python3 - "$SETTINGS" "$DOMAIN" <<'PYEOF'
import json, sys
from pathlib import Path

settings_path = Path(sys.argv[1])
domain = sys.argv[2]

# Build both apex and www variants (sites canonicalize differently;
# safer to allow both than assume which one production uses)
if domain.startswith("www."):
    apex = domain[4:]
    www = domain
else:
    apex = domain
    www = f"www.{domain}"

# Three patterns × two domain variants = 6 entries
# Patterns cover curl with various flag positions
new_entries = []
for d in [apex, www]:
    new_entries.extend([
        f"Bash(curl https://{d}/*)",
        f"Bash(curl -* https://{d}/*)",
        f"Bash(curl * https://{d}/*)",
    ])

if settings_path.exists():
    try:
        data = json.loads(settings_path.read_text())
    except json.JSONDecodeError as e:
        print(f"  ERROR: existing {settings_path} is not valid JSON ({e}); refusing to overwrite. Add curl allowlist manually.")
        sys.exit(0)
else:
    data = {}

if "permissions" not in data:
    data["permissions"] = {}
if "allow" not in data["permissions"]:
    data["permissions"]["allow"] = []

added = []
for entry in new_entries:
    if entry not in data["permissions"]["allow"]:
        data["permissions"]["allow"].append(entry)
        added.append(entry)

# Sprint 12 deny-conflict detection: extended pattern matching + exact diff
# Monitored tools: any bulk-HTTP-fetch tool sitewide-verify might use
MONITORED_TOOLS = ["curl", "wget", "httpie", "http"]
deny_list = data.get("permissions", {}).get("deny", [])
conflicts = []
for rule in deny_list:
    for tool in MONITORED_TOOLS:
        # Match Bash(<tool>...) where the pattern doesn't already restrict to http://
        if rule.startswith(f"Bash({tool}") and "http://" not in rule:
            # Suggest scoped replacement: deny only insecure HTTP for that tool
            suggested = f'"Bash({tool} http://*)"'
            conflicts.append((rule, suggested, tool))
            break

if conflicts:
    print(f"  ⚠ WARNING: settings.json deny block has {len(conflicts)} rule(s) that will OVERRIDE the allowlist below:")
    print(f"")
    for rule, suggested, tool in conflicts:
        print(f"    Conflict: deny rule {rule!r} blocks ALL {tool} (including the scoped HTTPS allow entries we just provisioned)")
        print(f"    Suggested fix in {settings_path}:")
        print(f"      REPLACE:  \"{rule}\",")
        print(f"      WITH:     {suggested},")
        print(f"")
    print(f"  Rationale: \"{conflicts[0][2]} http://*\" pattern keeps insecure HTTP blocked (security)")
    print(f"  while letting your scoped HTTPS allowlist take effect.")
    print(f"  Or remove the deny rule entirely if no HTTP restriction needed.")
    print(f"  See field-manual/permission-conflicts.md for full pattern context.")
    print(f"  install.sh does NOT auto-modify deny rules — security decision belongs to you.")
    print(f"")

if added:
    settings_path.parent.mkdir(parents=True, exist_ok=True)
    settings_path.write_text(json.dumps(data, indent=2) + "\n")
    print(f"  merged {len(added)} curl allowlist entries into {settings_path} (apex + www variants)")
    for e in added:
        print(f"    + {e}")
else:
    print(f"  all {len(new_entries)} curl allowlist entries already present in {settings_path} (idempotent)")
PYEOF
    fi
  fi
fi

# ---- Phase 12: Version stamp ----
phase "Phase 12: Version stamp"
if [ "$DRY_RUN" = "1" ]; then
  note "WOULD WRITE: $TARGET/.seo-agent-version"
else
  cat > "$TARGET/.seo-agent-version" <<EOF
SEO-Agent installed from: $SOURCE
Source commit: $SOURCE_COMMIT
Install date: $(date -u +%Y-%m-%dT%H:%M:%SZ)
Mode: $MODE
EOF
  note "wrote: $TARGET/.seo-agent-version"
fi

# ---- Done ----
phase "✓ Install complete"
echo "  Target: $TARGET"
echo "  Source commit: $SOURCE_COMMIT"
echo "  Mode: $MODE"
if [ "$DRY_RUN" = "1" ]; then
  echo ""
  echo "  THIS WAS A DRY RUN — no files modified."
  echo "  Re-run without --dry-run to actually install."
fi
echo ""
echo "  Next steps:"
echo "    cd $TARGET"
if [ "$MODE" = "install" ] && [ "$EXISTING_INSTALL" = "0" ]; then
  echo "    git checkout -b seo-tooling   # create SEO branch (if not on one)"
fi
echo "    # Edit tracking/config/tracking.yml with site-specific config"
echo "    claude"
echo "    # Then in the Claude session:"
echo "    # /coord site-audit lite <your-domain>"
