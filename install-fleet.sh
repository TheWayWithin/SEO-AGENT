#!/usr/bin/env bash
# SEO-Agent fleet installer (bulk operator)
#
# Reads ~/Shared/tools/agent-11-fleet/seo-fleet-registry.yaml.
# For each entry where tier=active and installed!=true, clones the repo into
# its workspace path under ~/SEO-Agents/, then calls install.sh.
#
# Usage:
#   bash install-fleet.sh [options]
#
# Options:
#   --dry-run           Print what would happen for every repo; no filesystem changes.
#   --filter <pattern>  Only process repos matching pattern. Pattern can be:
#                         - a priority (p1, p2, p3, p4)
#                         - a name substring (case-insensitive)
#                         - "p1,p2"  (comma-separated)
#   --skip-clone        Don't clone; only run install.sh on existing workspaces.
#   --keep-going        Continue on per-repo failure (default: stop at first failure).
#   --upgrade           Pass --upgrade to install.sh (refresh SEO product files only).
#   --help, -h          This message.
#
# Hard safety rule (inherited from install.sh):
#   Refuses any workspace path under ~/DevProjects/. seo-fleet-registry.yaml
#   should not contain such paths; this is a defence-in-depth check.
#
# Examples:
#   # Dry-run the whole P1 cohort:
#   bash install-fleet.sh --filter p1 --dry-run
#
#   # Real run on aisearchmastery only:
#   bash install-fleet.sh --filter aisearchmastery
#
#   # Real run on all P1 + P2:
#   bash install-fleet.sh --filter p1,p2

set -euo pipefail

SOURCE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REGISTRY="${SEO_FLEET_REGISTRY:-/Users/jamiewatters/Shared/tools/agent-11-fleet/seo-fleet-registry.yaml}"
INSTALL_SH="$SOURCE/install.sh"

DRY_RUN=0
FILTER=""
SKIP_CLONE=0
KEEP_GOING=0
UPGRADE=0

usage() {
  sed -n '/^# Usage:/,/^set -euo/p' "$0" | grep '^#' | sed 's/^# \?//'
}

err() { echo "ERROR: $*" >&2; exit 1; }
note() { echo "  $*"; }
phase() { echo ""; echo "=== $* ==="; }

while [ $# -gt 0 ]; do
  case "$1" in
    --dry-run) DRY_RUN=1; shift ;;
    --filter) FILTER="$2"; shift 2 ;;
    --skip-clone) SKIP_CLONE=1; shift ;;
    --keep-going) KEEP_GOING=1; shift ;;
    --upgrade) UPGRADE=1; shift ;;
    --help|-h) usage; exit 0 ;;
    *) err "Unknown arg: $1" ;;
  esac
done

[ -f "$REGISTRY" ] || err "Registry not found: $REGISTRY"
[ -x "$INSTALL_SH" ] || err "install.sh not found or not executable: $INSTALL_SH"

# ---- Tiny YAML parser (registry-specific; not general-purpose) ----
# Yields TSV: name<tab>workspace<tab>remote<tab>branch<tab>public_url<tab>tier<tab>priority<tab>installed
parse_registry() {
  awk '
    BEGIN { in_repos=0; rec_open=0 }
    /^repos:/ { in_repos=1; next }
    !in_repos { next }
    /^  - name:/ {
      if (rec_open) { print rec(); reset() }
      rec_open=1
      name=val($0)
      next
    }
    rec_open && /^    workspace:/ { workspace=val($0); next }
    rec_open && /^    remote:/    { remote=val($0); next }
    rec_open && /^    branch:/    { branch=val($0); next }
    rec_open && /^    public_url:/ { public_url=val($0); next }
    rec_open && /^    tier:/      { tier=val($0); next }
    rec_open && /^    priority:/  { priority=val($0); next }
    rec_open && /^    installed:/ { installed=val($0); next }
    END { if (rec_open) print rec() }

    function val(line,    v) {
      sub(/^[^:]+:[ ]*/, "", line)
      gsub(/^"|"$/, "", line)
      gsub(/^[ \t]+|[ \t]+$/, "", line)
      return line
    }
    function rec() {
      return name "\t" workspace "\t" remote "\t" branch "\t" public_url "\t" tier "\t" priority "\t" installed
    }
    function reset() {
      name=""; workspace=""; remote=""; branch=""; public_url=""; tier=""; priority=""; installed=""
    }
  ' "$REGISTRY"
}

# ---- Filter logic ----
# Returns 0 if the repo passes the filter, 1 otherwise.
matches_filter() {
  local name="$1" priority="$2"
  [ -z "$FILTER" ] && return 0   # no filter = include all

  # Comma-split
  local IFS=','
  for token in $FILTER; do
    token="$(echo "$token" | tr '[:upper:]' '[:lower:]' | tr -d '[:space:]')"
    case "$token" in
      p1|p2|p3|p4)
        [ "$priority" = "$token" ] && return 0 ;;
      *)
        # name substring (case-insensitive)
        echo "$name" | tr '[:upper:]' '[:lower:]' | grep -q "$token" && return 0 ;;
    esac
  done
  return 1
}

# ---- Plan + execute ----
phase "SEO-Agent fleet install"
echo "  registry:       $REGISTRY"
echo "  install.sh:     $INSTALL_SH"
echo "  dry-run:        $DRY_RUN"
echo "  filter:         ${FILTER:-<none — all active repos>}"
echo "  skip-clone:     $SKIP_CLONE"
echo "  keep-going:     $KEEP_GOING"
echo "  upgrade:        $UPGRADE"

planned_count=0
skipped_count=0
done_count=0
fail_count=0

while IFS=$'\t' read -r name workspace remote branch public_url tier priority installed; do
  [ -z "$name" ] && continue

  # Skip non-active tiers
  if [ "$tier" != "active" ]; then
    continue
  fi

  # Skip already-installed
  if [ "$installed" = "true" ]; then
    note "skip (installed=true): $name"
    skipped_count=$((skipped_count+1))
    continue
  fi

  # Apply filter
  if ! matches_filter "$name" "$priority"; then
    continue
  fi

  planned_count=$((planned_count+1))

  phase "Repo: $name (priority=$priority, branch=$branch)"
  echo "  workspace: $workspace"
  echo "  remote:    $remote"
  echo "  public:    $public_url"

  # Defence-in-depth: refuse DevProjects paths
  case "$workspace" in
    /Users/jamiewatters/DevProjects/*|"$HOME/DevProjects/"*)
      note "REFUSED: workspace under ~/DevProjects/ — registry error"
      fail_count=$((fail_count+1))
      [ "$KEEP_GOING" = "1" ] && continue || err "halt (--keep-going to continue)"
      ;;
  esac

  # Build install.sh args
  install_args=("$workspace")
  if [ "$SKIP_CLONE" = "0" ] && [ ! -d "$workspace" ]; then
    install_args+=(--clone-from "$remote" --branch "$branch")
  fi
  [ "$UPGRADE" = "1" ] && install_args+=(--upgrade)
  [ "$DRY_RUN" = "1" ] && install_args+=(--dry-run)

  echo ""
  echo "  → bash install.sh ${install_args[*]}"
  echo ""

  if "$INSTALL_SH" "${install_args[@]}"; then
    done_count=$((done_count+1))
    note "✓ $name done"
  else
    fail_count=$((fail_count+1))
    note "✗ $name FAILED"
    if [ "$KEEP_GOING" = "0" ]; then
      err "Halted at $name. Re-run with --keep-going to continue past failures."
    fi
  fi
done < <(parse_registry)

phase "Fleet install summary"
echo "  planned: $planned_count"
echo "  done:    $done_count"
echo "  skipped: $skipped_count (already installed)"
echo "  failed:  $fail_count"
[ "$DRY_RUN" = "1" ] && echo "" && echo "  THIS WAS A DRY RUN — no filesystem changes made."

[ "$fail_count" -gt 0 ] && exit 1 || exit 0
