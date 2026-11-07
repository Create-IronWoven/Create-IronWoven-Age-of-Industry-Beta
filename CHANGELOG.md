# Changelog

Player-facing summary of the current Ironwoven development pack. This is not a record of internal commits or a downloadable release archive.

## Current automatic version

<!-- IRONWOVEN_AUTO_VERSION -->

**Version format:** `v<release>.<content revision>.<top-level dedicated-server mod JARs>.<active accepted bug fixes>`.

- **Release:** starts at 0 and advances when an official Ironwoven release is published with a four-part version tag.
- **Content revision:** advances when the accepted dedicated-server content fingerprint changes.
- **Server mods:** counts top-level `.jar` files in the selected dedicated server's `mods/` folder. It does not count CurseForge client-profile entries or NeoForge mod IDs.
- **Bug fixes:** counts distinct active accepted Ironwoven pack fixes, not datapacks or individual resource files.

## Current server inventory evidence

The fresh Windows dedicated-server folder-properties screenshot from 7 November 2026 confirms **101 files** in the server `mods/` folder. The corresponding NeoForge Mod List contains 118 entries (116 non-core mod IDs plus Minecraft and NeoForge); that is a different runtime measurement and is not used by the version.

A separate CurseForge client-profile screenshot showed 99 entries. That client-profile count is not used for the server-pack version. Older client/test-server folder screenshots are historical inventory records only.

## Five accepted compatibility bug fixes

The current accepted-fix register contains five distinct defects:

| # | Bug-fix family | Included pack fix | Evidence scope |
|---:|---|---|---|
| 1 | Create: Design n' Decor optional Dye Depot loot-table decoding | `IronWoven-Recipe-Fixes` | 256 affected loot-table resources; targeted errors absent in the corrected server log |
| 2 | Create: Steam 'n' Rails optional track loot-table decoding | `IronWoven-Railways-Fix` | 192 affected loot-table resources; targeted errors absent in the corrected server log |
| 3 | Create Kinetic missing/stale loot-table item references | `IronWoven-Create-Kinetic-Fix` | 5 affected loot-table resources; targeted errors absent in the corrected server log |
| 4 | Create Deco placard recipe invalid ingredient key | `IronWoven-Recipe-Fixes` | 1 recipe defect; targeted error absent in the corrected server log |
| 5 | Sable / Copycats+ Catwalk physics selector points to an unregistered block | `IronWoven-Sable-Copycats-Fix` | 1 selector defect; targeted error absent in the corrected server log |

These five defects affect 455 individual resources in total, but contribute **5** to the bug-fix component. Four maintained datapacks address the five defects. Their targeted log-level retests passed; this does not claim every affected in-game feature has completed full functional testing.

## Other accepted mod updates

- Every Compat (Wood Good) updated from 2.11.56 to 2.11.57 (CurseForge file 9468938).
- Required Moonlight Lib (Selene) dependency updated from 3.8.1 to 3.8.2 (CurseForge file 9458248).

These are version updates to existing mod files. Their byte changes are detected by the content fingerprint when those files are present in the selected server `mods/` folder.

## Not counted as accepted bug fixes

- Create Aeronautics: Gadgets & Gizmos 2.0.0-Pre-Release-4 (CurseForge file 9260191) remains an uninstalled and untested update candidate; the observed installed baseline is bundled 1.2.10.
- The Aeronautics Structures uniform-loot override remains test-only.
- The local Struts JAR patch is not part of the accepted pack.
- The PowerGrid native DLL workaround and Shulker Box Tooltip / Supplementaries config workaround are not accepted distributed pack fixes.

**Release status:** internal development. No downloadable public beta package has been published.
