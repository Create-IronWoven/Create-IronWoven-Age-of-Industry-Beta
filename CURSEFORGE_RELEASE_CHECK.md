# CurseForge Release Permission Check

**Target:** Create IronWoven 0.1.0-beta  
**Distribution:** CurseForge only  
**Platform:** Minecraft 1.21.1 · NeoForge 21.1.265 · Java 21  
**Status:** In progress — not a release approval.

Create IronWoven will be distributed exclusively through CurseForge. GitHub is used for project documentation and development records, not as an alternative modpack download platform.

## Release rules

- CurseForge-hosted mods must be selected through the CurseForge App and referenced by its generated `manifest.json`.
- Do not manually place CurseForge-hosted mod JARs in `overrides/mods`.
- Mods not hosted on CurseForge may only be included if they appear on CurseForge's approved Non-CurseForge Mods list and meet its published conditions.
- Export the App-generated ZIP with `manifest.json` and pack-owned files in `overrides/`. Do not manually edit the manifest.
- A mod's presence in a development/test profile does not automatically clear it for public release.

Official guidance:
- https://support.curseforge.com/support/solutions/articles/9000197908
- https://support.curseforge.com/support/solutions/articles/9000197279
- https://support.curseforge.com/support/solutions/articles/9000197913

## Known item requiring review

| Mod | Finding | Release status |
|---|---|---|
| Ender Villages 2.0 | The project's licence page states All Rights Reserved. Review the exact 1.21.1 file and terms before release. | Hold — licence/terms review |

## Audit scope and limitation

The private development repository contains the detailed audit register for the recorded installed/test inventory and current planned candidates. The recorded 88-entry launcher snapshot is not a fresh CurseForge manifest, and the historical server inventory is a separate snapshot. Exact project/file IDs and licence terms for every installed item still need reconciliation against a fresh CurseForge App export.

Candidates remain separate from installed mods and are not approved by appearing in the audit.

## Before beta submission

1. Export the latest client profile from the CurseForge App.
2. Reconcile every manifest project/file ID and every current server JAR.
3. Verify exact Minecraft 1.21.1 NeoForge files, dependencies, current approval, project licences, and project-specific restrictions.
4. Check every non-CurseForge item against CurseForge's approved list; otherwise exclude it.
5. Perform a clean CurseForge export/import test.

**Current decision: not ready for CurseForge submission.** No mod has been installed, removed, updated, or approved by this audit.
