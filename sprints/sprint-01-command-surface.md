# Sprint 1 — Command Surface Slim-Down

**Theme**: De-bloat
**Effort**: S (2 to 4 hours after rescope)
**Dependencies**: None
**Status**: COMPLETE 2026-05-09

> **RESCOPE 2026-05-09** (see `sprints/RESCOPE-2026-05-09.md`)
> Original premise (delete generic dev missions) is wrong under the layer model. Generic missions are **framework** tools we use to build SEO-Agent — keep them.
> Replacement scope:
> 1. Register the four SEO missions in `.claude/commands/coord.md` routing table (currently absent).
> 2. Normalise mission file locations — move `ai-search-optimize.md` into `.claude/missions/` alongside the other three.
> 3. Update `.claude/commands/seo-commands.md` to point at canonical mission paths.
> Sprint 4 (Universal Mission Router) is merged in here; v6 forbids NLP, so router work reduces to registering missions.

## Sprint Goal

Reduce `/missions/` to only the SEO-relevant missions so `/coord` can dispatch without competing against generic dev workflows.

## Motivation

Per blueprint section 2: SEO-Agent currently ships every generic dev mission from Agent-11 (build, fix, refactor, deploy, mvp, migrate, document, optimize, security, integrate, release, architecture, product-description). This dilutes the focus of an SEO tool and confuses the router. Cutting them is the smallest, lowest-risk lever and makes later sprints cleaner.

## Scope: In

- Remove all generic dev mission files from `/missions/`
- Keep the four SEO missions: `site-audit`, `content-gap`, `technical-fix`, `ai-search-optimize`
- Update `/coord` command documentation to reflect the trimmed roster
- Update README and any quick-start docs that list missions
- Update `/missions/library.md` (the index)

## Scope: Out

- No agent prompt changes (Sprint 3)
- No CLAUDE.md rewrite (Sprint 2)
- No routing logic changes (Sprint 4)
- Deliverable format changes (Sprint 5)

## Task List (post-rescope — original list cancelled, generic missions retained as framework dependency)

- [x] Move `missions/ai-search-optimize.md` → `.claude/missions/ai-search-optimize.md` via `git mv` (2026-05-09)
- [x] Add Mode D — SEO row to coord.md mode legend (2026-05-09)
- [x] Add 4 SEO missions to coord.md routing table inside `SEO-PRODUCT-LAYER-START/END` marker comments (2026-05-09)
- [x] Extend coord.md dispatch step 5 with SEO load path (`.claude/missions/[name].md`) (2026-05-09)
- [x] Add SEO line to coord.md Unknown Mission help (2026-05-09)
- [x] Add SEO examples to coord.md Examples block (2026-05-09)
- [x] Verify all four missions co-located in `.claude/missions/` (2026-05-09)
- [x] Confirm `seo-commands.md` needs no edit (uses `@agent` direct delegation, no mission paths) (2026-05-09)

## Acceptance Criteria

- `/missions/` contains only SEO-relevant files plus shared templates
- `grep` for deleted mission names returns zero hits outside archive/backup directories
- `/coord` help output lists only the four SEO missions
- README mission list matches what exists in `/missions/`

## Assessment Protocol (freecalchub.com)

1. Run `/coord site-audit freecalchub.com` and confirm it dispatches as before
2. Run `/coord build some-spec.md` and confirm it errors or refuses with a clear message
3. Record both outcomes in `seo-evidence.md`

DONE means: only four SEO missions are dispatchable, no broken links in docs, and a site-audit still runs end to end on freecalchub.com.

## Risks & Mitigations

| Risk | Mitigation |
|------|------------|
| Latent docs or examples reference deleted missions | Run grep sweep before and after deletion |
| `/coord` command breaks because routing assumes a mission exists | Update command in the same commit as the deletion |
| User has muscle memory for `/coord build` | Replace with a clear error message pointing to supported missions |

## Exit Notes

When closing this sprint, update `handoff-notes.md` with:
- The final list of retained missions
- Any references that could not be cleanly removed (for Sprint 3 or later)
- Confirmation that `/coord site-audit freecalchub.com` still works
