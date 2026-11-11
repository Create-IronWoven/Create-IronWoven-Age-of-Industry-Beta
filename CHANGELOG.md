# Changelog

Player-facing summary of the current Ironwoven development pack. This is not a record of internal commits or a downloadable release archive.

## Current automatic version

<!-- IRONWOVEN_AUTO_VERSION -->
**Current Ironwoven pack version:** `v0.1.101.5` — release `0`, content revision `1`, `101` top-level server mod JARs, and `5` active accepted bug fixes.

**Version format:** `v<release>.<content revision>.<top-level dedicated-server mod JARs>.<active accepted bug fixes>`.

- **Release:** starts at 0 and advances when an official Ironwoven release is published with a four-part version tag.
- **Content revision:** advances when the accepted dedicated-server content fingerprint changes.
- **Server mods:** counts top-level `.jar` files in the selected dedicated server's `mods/` folder. It does not count CurseForge client-profile entries or NeoForge mod IDs.
- **Bug fixes:** counts distinct active accepted Ironwoven pack fixes, not datapacks or individual resource files.

## Current server inventory evidence

The fresh Windows dedicated-server folder-properties screenshot from 7 November 2026 confirms **101 files** in the server `mods/` folder. The corresponding NeoForge Mod List contains 118 entries (116 non-core mod IDs plus Minecraft and NeoForge); that is a different runtime measurement and is not used by the version.

The 10 November active test-profile archive audit confirms 102 JARs in the client archive and 102 in the dedicated-server test archive. 101 shared non-WITS JARs have identical SHA-256 hashes; WITS is a temporary utility excluded from the mod set. These test-profile archives are not used for the displayed version, which is based on the separate clean v.0.1 server. Deployment of accepted test-profile updates to that server has not been confirmed. The 99-entry CurseForge screenshot and older client/server folder screenshots remain historical inventory records only.

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

## Accepted mod updates — 10 November 2026

- Sophisticated Backpacks updated from 3.26.20.2244 (CurseForge file 9431839) to 3.26.21.2249 (file 9524812); authorised shared smoke PASS and exact client/server SHA-256 parity confirmed.
- Sophisticated Core dependency updated from 1.5.28.2458 (file 9431812) to 1.5.32.2464 (file 9524669); validated in the same coordinated Backpacks smoke test and hash-matched on both sides.
- Create: The Factory Must Grow Community Edition updated from 1.3.3 (file 9413167) to 1.3.3a (file 9482161); authorised shared smoke PASS and exact client/server SHA-256 parity confirmed.
- FastSuite 6.0.7 (CurseForge file 7527945) and Placebo 9.9.4 (file 9153039) accepted into the active mod set after exact-file/dependency preflight, matching client/server hashes, and authorised combined-profile smoke PASS on 11 November. No isolated optimizer run is required; feature/recipe/JEI/performance checks remain Pending for beta testers. FastFurnace 9.0.1 loaded in the same profile but its exact file/dependency/side preflight remains open and it is not yet accepted.

Feature/function checks remain pending and are not marked Pass from smoke testing. TFMG's Custom License distribution review remains a separate release gate. The versioned clean v.0.1 server has not been re-scanned after deployment of these test-profile updates; retain its recorded automatic version until the selected server itself is updated and the private updater is previewed.

## Not counted as accepted bug fixes

- Create Aeronautics: Gadgets & Gizmos 2.0.0-Pre-Release-4 (CurseForge file 9260191) is **ON HOLD**. Do not install or test this prerelease; keep bundled 1.2.10 (file 9141062) unchanged until a stable 2.x release and exact dependency/side/version review are available, followed by separate maintainer approval.
- The Aeronautics Structures uniform-loot override remains test-only.
- The local Struts JAR patch is not part of the accepted pack.
- The PowerGrid native DLL workaround and Shulker Box Tooltip / Supplementaries config workaround are not accepted distributed pack fixes.

**Release status:** internal development. No downloadable public beta package has been published.
