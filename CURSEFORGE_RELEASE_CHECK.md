# CurseForge Release Permission Check

**Target:** Create IronWoven 0.1.0-beta  
**Distribution:** CurseForge only  
**Platform:** Minecraft 1.21.1 · NeoForge 21.1.265 · Java 21  
**Status:** In progress — not a release approval.  
**Last reviewed:** 5 November 2026

Create IronWoven will be distributed exclusively through CurseForge. GitHub is used for project documentation and development records, not as an alternative modpack download platform.

## Release rules

- CurseForge-hosted mods must be selected through the CurseForge App and referenced by its generated `manifest.json`.
- Do not manually place CurseForge-hosted mod JARs in `overrides/mods`.
- Only mods with an official CurseForge project/file are eligible. If no suitable CurseForge file exists, mark the mod Not eligible and exclude it. No external source or exception route is permitted.
- Export the App-generated ZIP with `manifest.json` and pack-owned files in `overrides/`. Do not manually edit the manifest.
- A mod's presence in a development/test profile does not automatically clear it for public release.

Official guidance:
- https://support.curseforge.com/support/solutions/articles/9000197908
- https://support.curseforge.com/support/solutions/articles/9000197279
- https://support.curseforge.com/support/solutions/articles/9000197913

## Known item requiring review

| Mod | Finding | Release status |
|---|---|---|
| Ender Villages 2.0 | Exact 1.21.1 NeoForge CurseForge file 6741737; project licence states All Rights Reserved. | CurseForge-hosted; use App manifest, never manually bundle JAR. Gameplay/side checks pending |

## Audit scope and limitation

The private development repository contains the detailed audit register for the recorded installed/test inventory and current planned candidates. The recorded 88-entry launcher snapshot is not a fresh CurseForge manifest, and the historical server inventory is a separate snapshot. Exact project/file IDs and licence terms for every installed item still need reconciliation against a fresh CurseForge App export.

Candidates remain separate from installed mods and are not approved by appearing in the audit.

## Before beta submission

1. Export the latest client profile from the CurseForge App.
2. Reconcile every manifest project/file ID and every current server JAR.
3. Verify exact Minecraft 1.21.1 NeoForge files, dependencies, current approval, project licences, and project-specific restrictions.
4. Confirm that every mod has an official CurseForge project/file; exclude any mod without one.
5. Perform a clean CurseForge export/import test.

**Current decision: not ready for CurseForge submission.** No mod has been installed, removed, updated, or approved by this audit.


## Expanded release-audit scope — 4 November 2026

The audit is being performed against the **entire** current inventory and potential-mod register, not only the most recent additions:

- Current test profile: all entries in [MODS.md](MODS.md), including Create/Aeronautics addons, world generation, building/storage/food, UI utilities, client-only graphics, and support libraries.
- Test/server inventory: reconciled against the private master record; the 88-entry launcher snapshot and historical 79-JAR / 82-loaded server snapshot are distinct.
- Potential additions: all entries in [MOD_PLANS.md](MOD_PLANS.md), including QoL, gameplay, End content, MineColonies ecosystem, performance/rendering, and dependencies.

### Official CurseForge checks recorded so far

- Create 6.0.10 and Create Aeronautics 1.3.2 have matching 1.21.1 NeoForge CurseForge files. Create Aeronautics uses a Custom License and requires Create plus Sable.
- Create Deco 2.1.3 has an exact 1.21.1 NeoForge CurseForge file. Its project licence is All Rights Reserved, but it is hosted on CurseForge and should be selected through the App-generated manifest, not manually bundled.
- Create: Kinetic 1.4.3 is confirmed as CurseForge file **9293815** for 1.21.1 NeoForge (GPLv3).
- Create: Fluids Be Gone 1.0.1 is confirmed on CurseForge for 1.21.1 NeoForge (MIT).
- Regions Unexplored 0.6.3 is confirmed for 1.21.1 NeoForge (MIT).
- MineColonies 1.1.1403 is available for 1.21.1 NeoForge (file 9058295). Its required libraries are Structurize, MultiPiston, BlockUI, and Domum Ornamentum at the minimum versions declared by that file.
- TownTalk 1.2.0 is available for 1.21.1 NeoForge but has an All Rights Reserved licence and unset environment metadata; treat it as a separate review item.
- Dynamic Trees — Regions Unexplored 1.1.2 is available for 1.21.1 NeoForge; the base Dynamic Trees file still needs its own verification.
- ImmediatelyFast 1.6.15 is available for 1.21.1 NeoForge and is client-only. Flerovium is also identified as client-only and requires Sodium.
- More Culling 1.0.11 is listed on CurseForge as a Minecraft 1.21.1 NeoForge release. Project metadata identifies it as GPLv3 and client-only; the exact file ID still needs reconciliation before selection.

CurseForge-hosted mods, including those with custom or restrictive project licences, must be referenced through the App-generated manifest. Do not manually bundle their JARs in `overrides/mods`. No mods hosted outside CurseForge will be considered or included.

**This is partial source/file verification, not a completed clearance of every entry.** Remaining installed mods and candidates still need exact project/file, dependency, loader, side, and source reconciliation. No candidates have been installed or approved.


## Ongoing per-mod source and permission checks

Every mod already recorded in the installed/test inventory and every candidate in [MOD_PLANS.md](MOD_PLANS.md) is subject to an individual release-source audit. New suggestions are checked before they are recommended for inclusion. This is separate from compatibility testing and production approval.

For each distinct project, the private development audit records its official project page, CurseForge-hosted status, exact 1.21.1 NeoForge file and current availability, licence and explicit project restrictions, dependencies, client/server metadata, source links, and review date.

- CurseForge-hosted mods are selected through the CurseForge App and its generated manifest. Their JARs must not be manually bundled in `overrides/mods`.
- Mods without an official CurseForge project/file are not eligible and must be excluded. No external downloads or developer-provided JARs are accepted.
- A custom or All Rights Reserved licence label alone is not treated as proof that a CurseForge manifest reference is prohibited; explicit terms are reviewed separately.
- A source/permission pass does not mean a mod is compatible, tested, selected, or approved for installation.
- Unknown or ambiguous items remain on hold. Current file availability and approval are rechecked before each release export.

The detailed per-mod evidence and outstanding checks are maintained in the private repository's `docs/CURSEFORGE_PERMISSION_AUDIT.md`. This public checklist is not a blanket release clearance.


## Audit progress — Create addon batch (4 November 2026)

A first additional project-page pass found CurseForge-hosted pages for Create Crafts & Additions, Create: Bits 'n' Bobs, Create: Diesel Generators, Create: Blocks & Bogies, Create: Pantographs & Wires, and Create Aeronautics: Gadgets & Gizmos. They must be selected through the CurseForge App manifest, not manually bundled.

Two inventory/file mismatches remain open: the recorded Bits 'n' Bobs 2.3.5 versus the surfaced 2.3.2 page file, and the recorded bundled Gadgets & Gizmos 1.2.10 versus the surfaced standalone 1.1.3 file. Pantographs & Wires still needs its licence/terms and exact manifest file ID recorded. These entries are not yet fully release-cleared. See the private audit register for exact sources and remaining checks.
