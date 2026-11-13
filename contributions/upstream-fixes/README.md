# Upstream Compatibility Fix Contributions
<!-- IRONWOVEN_CHRONOLOGY
{
  "record_id": "IRONWOVEN-BETA-UPSTREAM-README-0001",
  "record_type": "beta_upstream_contribution_index_and_publication_scope",
  "created_at": "unknown",
  "updated_at": "unknown",
  "verified_at": "2026-11-13T14:33:30Z",
  "migrated_at": "2026-11-13T14:33:30Z",
  "source_ref": [
    "Beta contributions/upstream-fixes/README.md, lines 1–14 and 26 onward — current public handoff scope, non-distribution boundary, privacy links and usage limits rechecked; all eight contribution-folder targets exist and reports remain proposals, not accepted upstream fixes."
  ],
  "timezone_display": "Europe/Amsterdam",
  "chronology_status": "CURRENT"
}
-->
<!-- IRONWOVEN_CHRONOLOGY
{
  "record_id": "IRONWOVEN-BETA-UPSTREAM-README-0002",
  "record_type": "beta_upstream_status_struts_issue6",
  "created_at": "unknown",
  "updated_at": "unknown",
  "verified_at": "2026-11-13T14:33:30Z",
  "migrated_at": "2026-11-13T14:33:30Z",
  "source_ref": [
    "Beta contributions/upstream-fixes/README.md, original line 19 — Strut Your Stuff issue #6 remains OPEN (GitHub API checked 13 November 2026); current source struts.mixins.json still lists StrutRenderSystemAccessor in the common mixins array and the class targets RenderSystem."
  ],
  "timezone_display": "Europe/Amsterdam",
  "chronology_status": "CURRENT"
}
-->
<!-- IRONWOVEN_CHRONOLOGY
{
  "record_id": "IRONWOVEN-BETA-UPSTREAM-README-0003",
  "record_type": "beta_upstream_status_create_kinetic_mixin",
  "created_at": "unknown",
  "updated_at": "unknown",
  "verified_at": "2026-11-13T14:33:30Z",
  "migrated_at": "2026-11-13T14:33:30Z",
  "source_ref": [
    "Beta contributions/upstream-fixes/README.md, original line 20 — the main_aeronautics_1.21.1 branch exists; current createkinetic.mixins.json still lists client.MinecraftMixin in common mixins while the class targets net.minecraft.client.Minecraft. GitHub open-issue search returned zero matching open issues on 13 November 2026."
  ],
  "timezone_display": "Europe/Amsterdam",
  "chronology_status": "CURRENT"
}
-->
<!-- IRONWOVEN_CHRONOLOGY
{
  "record_id": "IRONWOVEN-BETA-UPSTREAM-README-0004",
  "record_type": "beta_upstream_status_copycats_sable",
  "created_at": "unknown",
  "updated_at": "unknown",
  "verified_at": "2026-11-13T14:33:30Z",
  "migrated_at": "2026-11-13T14:33:30Z",
  "source_ref": [
    "Beta contributions/upstream-fixes/README.md, original line 21 — Copycats+ issue #437 remains OPEN; PR #443 is CLOSED and unmerged. The current multiloader copycat_catwalk physics resource still selects copycats:copycat_catwalk; its public issue describes the shared COPYCAT_BOARD backing block."
  ],
  "timezone_display": "Europe/Amsterdam",
  "chronology_status": "CURRENT"
}
-->
<!-- IRONWOVEN_CHRONOLOGY
{
  "record_id": "IRONWOVEN-BETA-UPSTREAM-README-0005",
  "record_type": "beta_upstream_status_design_n_decor",
  "created_at": "unknown",
  "updated_at": "unknown",
  "verified_at": "2026-11-13T14:33:30Z",
  "migrated_at": "2026-11-13T14:33:30Z",
  "source_ref": [
    "Beta contributions/upstream-fixes/README.md, original line 22 — Design n' Decor issue #139 remains OPEN; PR #140 is CLOSED and unmerged. Its public PR discussion contains the maintainer comment 'poor way of doing it'; no accepted upstream correction is claimed."
  ],
  "timezone_display": "Europe/Amsterdam",
  "chronology_status": "CURRENT"
}
-->
<!-- IRONWOVEN_CHRONOLOGY
{
  "record_id": "IRONWOVEN-BETA-UPSTREAM-README-0006",
  "record_type": "beta_upstream_status_steam_n_rails",
  "created_at": "unknown",
  "updated_at": "unknown",
  "verified_at": "2026-11-13T14:33:30Z",
  "migrated_at": "2026-11-13T14:33:30Z",
  "source_ref": [
    "Beta contributions/upstream-fixes/README.md, original line 23 — Steam 'n' Rails issues #302 and #378 remain OPEN; PR #393 and earlier PR #339 remain OPEN. PR #393's current diff changes the root condition key and condition field as described by the report; no merge is claimed."
  ],
  "timezone_display": "Europe/Amsterdam",
  "chronology_status": "CURRENT"
}
-->
<!-- IRONWOVEN_CHRONOLOGY
{
  "record_id": "IRONWOVEN-BETA-UPSTREAM-README-0007",
  "record_type": "beta_upstream_status_create_deco",
  "created_at": "unknown",
  "updated_at": "unknown",
  "verified_at": "2026-11-13T14:33:30Z",
  "migrated_at": "2026-11-13T14:33:30Z",
  "source_ref": [
    "Beta contributions/upstream-fixes/README.md, original line 24 — Create Deco issue #268 and PR #271 remain OPEN; issue #282 remains OPEN and its comments identify it as a possible duplicate of #268. Current 1.21-neo placard recipe still uses id for white_dye."
  ],
  "timezone_display": "Europe/Amsterdam",
  "chronology_status": "CURRENT"
}
-->

This folder is a public technical handoff area for compatibility issues that may be useful to the maintainers of the original projects.

It contains short, source-focused explanations and minimal proposed changes. It is not an alternate distribution of any mod, does not contain modified JARs, and does not claim that any proposal has been accepted upstream.

## Privacy and publication scope

Only information needed for public technical review is included here. This folder intentionally excludes private project records, private repository links, local computer paths, local account or machine identifiers, private server or world names, save files, raw logs, screenshots, credentials, and private conversations.

The environment is described only at the general compatibility level: Minecraft 1.21.1, NeoForge 1.21.x, and Java 21. Each report links to the relevant public upstream source, issue, or pull request.

See [PRIVACY_REVIEW.md](PRIVACY_REVIEW.md) for the scope and limits of the content check.

## Contribution status

| Project | Public upstream reference | Status in this handoff |
|---|---|---|
| Strut Your Stuff | [Issue #6](https://github.com/cakeGit/StrutYourStuff/issues/6) | Minimal mixin-side proposal prepared; upstream build and runtime validation required |
| Create Kinetic | [Source repository](https://github.com/Lightning323/Create-Kinetic) | Minimal client-mixin placement proposal prepared; upstream build and runtime validation required |
| Copycats+ | [Issue #437](https://github.com/copycats-plus/copycats/issues/437), [PR #443](https://github.com/copycats-plus/copycats/pull/443) | Investigation only; previous PR closed without merging |
| Create: Design n' Decor | [Issue #139](https://github.com/DrMango14/Create-Design-n-Decor/issues/139), [PR #140](https://github.com/DrMango14/Create-Design-n-Decor/pull/140) | Investigation only; previous PR closed without merging and its approach should not be repeated |
| Steam 'n' Rails | [Issues #302](https://github.com/Porters-of-Railways/Railway-1.21.1/issues/302) and [#378](https://github.com/Porters-of-Railways/Railway-1.21.1/issues/378), [PR #393](https://github.com/Porters-of-Railways/Railway-1.21.1/pull/393) | Existing upstream work is open; review and support that work rather than duplicate it |
| Create Deco | [Issue #268](https://github.com/talrey/CreateDeco/issues/268), [PR #271](https://github.com/talrey/CreateDeco/pull/271) | Existing PR addresses the malformed white-dye ingredient; no duplicate proposal |

## How to use these notes

1. Read the relevant report before applying or adapting a proposal.
2. Confirm the target branch and source files have not changed since the report was prepared.
3. Run the upstream project's own build and tests.
4. Validate both dedicated-server and client behavior where relevant.
5. Discuss proposals in the existing upstream issue or pull request before creating overlapping work.

No proposal in this folder should be treated as an official upstream fix or a released mod update.
