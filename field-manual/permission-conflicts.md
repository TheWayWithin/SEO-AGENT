# Permission Conflicts in Workspace settings.json

**Audience**: anyone setting up or operating a SEO-Agent workspace
**Sprint origin**: 12-5 (2026-05-17)
**Related work**: Sprint 11 (allowlist provisioning + Phase 0 preflight), Sprint 11 hotfix + 12 (deny-conflict detection)

## The pattern

SEO-Agent workspaces inherit a `.claude/settings.json` from the Agent-11 framework. The framework provides sensible security defaults — including a `deny` block that blocks broad classes of risky commands, e.g.:

```json
"deny": [
  "Bash(curl:*)",
  "Bash(wget:*)",
  "Bash(rm -rf /*)",
  "Bash(sudo:*)"
]
```

`Bash(curl:*)` and `Bash(wget:*)` are common defaults because curl and wget are how exfiltration attacks happen — denying them by default protects against an LLM accidentally curl-uploading sensitive data.

**This conflicts with sitewide-verify** (and any future bulk-HTTP mission). Sitewide-verify needs to fetch ~110 live pages from your tracked site. That's exactly what `Bash(curl:*)` blocks.

## Why allow-rules don't override deny

In Claude Code's permission model, **deny wins regardless of scope**. Even if `settings.json` has:

```json
"allow": [
  "Bash(curl https://www.freecalchub.com/*)"
],
"deny": [
  "Bash(curl:*)"
]
```

the deny still matches first. The curl is blocked.

This is correct security design — you don't want a narrow allow accidentally bypassing a broad safety deny. But it means the SEO-Agent install can't fix this by adding allow entries; it needs the deny rule itself to be scoped.

## The canonical fix

Replace broad tool denies with HTTP-scheme-scoped variants:

```diff
 "deny": [
-  "Bash(curl:*)",
+  "Bash(curl http://*)",
-  "Bash(wget:*)",
+  "Bash(wget http://*)",
   ...
 ]
```

This keeps insecure HTTP curl/wget blocked (the genuine risk — encrypted HTTPS is harder to exfiltrate to malicious endpoints unobserved) while letting the scoped HTTPS allowlist Sprint 11-C provisioned take effect.

**Alternative**: if you're confident about the workspace's exposure, remove the broad deny entirely. Workspaces are scoped to one site and the SEO mission set is reviewed; the risk surface is lower than for a general dev workspace.

Don't replace with something MORE specific than `http://*` (e.g. `Bash(curl http://evil.com/*)`) unless you have a specific threat model. The `http://*` scope is the smallest restriction that still serves the security intent.

## How SEO-Agent detects this

Three detection points, all using the same pattern matcher:

1. **install.sh** (Sprint 11 hotfix + 12-3) — at install or `--upgrade` time, scans the workspace settings.json deny block; warns with exact REPLACE/WITH suggestion for each conflict found. Monitored tools: `curl`, `wget`, `httpie`, `http`.
2. **sitewide-verify Phase 0 — Task A** (Sprint 12-1) — at mission run time, re-inspects settings.json before the live curl preflight. Catches the case where settings.json drifted AFTER install.
3. **audit-fleet-deny.sh** (Sprint 12-4) — fleet-wide hygiene check; walks all `~/SEO-Agents/*/` workspaces, reports which have conflicts, exits non-zero if any.

None of these tools auto-modify your deny rules. The fix is always a user decision because it's a security trade-off.

## Workflow for new workspaces

When you install SEO-Agent on a new workspace:

1. `bash install.sh ~/SEO-Agents/<name>` — provisions scoped curl allowlist
2. **Read install.sh output for ⚠ WARNING lines** — if your workspace inherited a broad curl/wget deny, you'll be told exactly what to change
3. Edit `.claude/settings.json` per the suggested REPLACE/WITH
4. Re-run `bash install.sh ~/SEO-Agents/<name> --upgrade` to confirm cleanliness (warning will disappear)
5. Fire `/coord sitewide-verify <domain>` — Phase 0 should pass cleanly

For workspaces installed before Sprint 11/12: run `bash audit-fleet-deny.sh` to see which have conflicts; fix per the report.

## When the broad deny is actually correct

There ARE workspaces where you genuinely want `Bash(curl:*)` blocked broadly — e.g. a sandboxed workspace handling sensitive data where you don't want ANY outbound HTTP regardless of scheme. In those cases:

- Don't install SEO-Agent's sitewide-verify mission there (you don't want it running anyway)
- Or accept that sitewide-verify will Phase-0-fail by design

The conflict detection is informational, not mandatory. Your security policy wins.

## Pattern reference for adding new monitored tools

If a future SEO mission uses a tool not in `[curl, wget, httpie, http]`, extend the `MONITORED_TOOLS` list in:

- `install.sh` (Phase 11 conflict detection)
- `audit-fleet-deny.sh` (fleet audit)
- `.claude/missions/sitewide-verify.md` Phase 0 Task A

Keep the three lists in sync. Document the rationale in this file's history.
