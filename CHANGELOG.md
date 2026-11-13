# Changelog

Player-facing summary of the current Ironwoven development pack. This is not a record of internal commits or a downloadable release archive.

<!-- IRONWOVEN_CHRONOLOGY
{"record_id":"IRONWOVEN-BETA-CHANGELOG-0001","record_type":"beta_current_automatic_pack_version","created_at":"unknown","updated_at":"unknown","verified_at":"2026-11-13T13:52:01Z","migrated_at":"2026-11-13T13:52:01Z","source_ref":["Beta CHANGELOG.md — generated version display v0.1.101.5. Exact current version, release/revision components, 101-JAR clean-server baseline and five active accepted fix IDs checked against private VERSIONING, PROJECT_STATUS and accepted-bug-fixes register. Generated line itself was not edited."],"timezone_display":"Europe/Amsterdam","chronology_status":"CURRENT"}
-->

## Current automatic version

<!-- IRONWOVEN_AUTO_VERSION -->
**Current Ironwoven pack version:** `v0.1.101.5` — release `0`, content revision `1`, `101` top-level server mod JARs, and `5` active accepted bug fixes.

**Version format:** `v<release>.<content revision>.<top-level dedicated-server mod JARs>.<active accepted bug fixes>`.

- **Release:** starts at 0 and advances when an official Ironwoven release is published with a four-part version tag.
- **Content revision:** advances when the accepted dedicated-server content fingerprint changes.
- **Server mods:** counts top-level `.jar` files in the selected dedicated server's `mods/` folder. It does not count CurseForge client-profile entries or NeoForge mod IDs.
- **Bug fixes:** counts distinct active accepted Ironwoven pack fixes, not datapacks or individual resource files.

<!-- IRONWOVEN_CHRONOLOGY
{"record_id":"IRONWOVEN-BETA-CHANGELOG-0002","record_type":"beta_clean_server_inventory_and_profile_boundary","created_at":"unknown","updated_at":"unknown","verified_at":"2026-11-13T13:52:01Z","migrated_at":"2026-11-13T13:52:01Z","source_ref":["Beta CHANGELOG.md — selected clean Windows server inventory is 101 top-level mod JARs, separate from the 10 November test-profile archives (102 JARs each, 101 common non-WITS JARs; WITS temporary/excluded). Checked against private Project Status and Versioning; no fresh local scan was performed and working-profile deployment to the clean versioned server remains unconfirmed."],"timezone_display":"Europe/Amsterdam","chronology_status":"CURRENT"}
-->

## Current server inventory evidence

The fresh Windows dedicated-server folder-properties screenshot from 7 November 2026 confirms **101 files** in the server `mods/` folder. The corresponding NeoForge Mod List contains 118 entries (116 non-core mod IDs plus Minecraft and NeoForge); that is a different runtime measurement and is not used by the version.

The 10 November active test-profile archive audit confirms 102 JARs in the client archive and 102 in the dedicated-server test archive. 101 shared non-WITS JARs have identical SHA-256 hashes; WITS is a temporary utility excluded from the mod set. These test-profile archives are not used for the displayed version, which is based on the separate clean v.0.1 server. Deployment of accepted test-profile updates to that server has not been confirmed.

<!-- IRONWOVEN_CHRONOLOGY
{"record_id":"IRONWOVEN-BETA-CHANGELOG-0003","record_type":"beta_five_active_accepted_bug_fixes_summary","created_at":"unknown","updated_at":"unknown","verified_at":"2026-11-13T13:52:01Z","migrated_at":"2026-11-13T13:52:01Z","source_ref":["Beta CHANGELOG.md — five distinct active accepted IronWoven compatibility bug-fix IDs affecting 455 resources across four datapacks. Private accepted-bug-fixes.json confirms five accepted active IDs; targeted log-level retests do not prove complete feature testing."],"timezone_display":"Europe/Amsterdam","chronology_status":"CURRENT"}
-->

## Five accepted compatibility bug fixes

The current accepted-fix register contains five distinct defects:

| # | Bug-fix family | Included pack fix | Evidence scope |
|---:|---|---|---|
| 1 | Create: Design n' Decor optional Dye Depot loot-table decoding | `IronWoven-Recipe-Fixes` | 256 affected loot-table resources; targeted errors absent in the corrected server log |
| 2 | Create: Steam 'n' Rails optional track loot-table decoding | `IronWoven-Railways-Fix` | 192 affected loot-table resources; targeted errors absent in the corrected server log |
| 3 | Create Kinetic missing/stale loot-table item references | `IronWoven-Create-Kinetic-Fix` | 5 affected loot-table resources; targeted errors absent in the corrected server log |
| 4 | Create Deco placard recipe invalid ingredient key | `IronWoven-Recipe-Fixes` | 1 recipe defect; targeted error absent in the corrected server log |
| 5 | Sable / Copycats+ Catwalk physics selector points to an unregistered block | `IronWoven-Sable-Copycats-Fix` | 1 selector defect; targeted error absent in the corrected server log |

<!-- IRONWOVEN_CHRONOLOGY
{"record_id":"IRONWOVEN-BETA-CHANGELOG-FIX-0001","record_type":"beta_accepted_fix_design_n_decor","created_at":"unknown","updated_at":"unknown","verified_at":"2026-11-13T13:52:01Z","migrated_at":"2026-11-13T13:52:01Z","source_ref":["Beta CHANGELOG.md — accepted bug-fix entry: Create: Design n' Decor optional Dye Depot loot-table decoding. Private accepted-bug-fixes.json confirms exact ID design-n-decor-optional-loot-tables remains status accepted and active; no new acceptance/test decision was made."],"timezone_display":"Europe/Amsterdam","chronology_status":"CURRENT"}
-->

<!-- IRONWOVEN_CHRONOLOGY
{"record_id":"IRONWOVEN-BETA-CHANGELOG-FIX-0002","record_type":"beta_accepted_fix_steam_n_rails","created_at":"unknown","updated_at":"unknown","verified_at":"2026-11-13T13:52:01Z","migrated_at":"2026-11-13T13:52:01Z","source_ref":["Beta CHANGELOG.md — accepted bug-fix entry: Create: Steam 'n' Rails optional track loot-table decoding. Private accepted-bug-fixes.json confirms exact ID steam-n-rails-optional-track-loot-tables remains status accepted and active; no new acceptance/test decision was made."],"timezone_display":"Europe/Amsterdam","chronology_status":"CURRENT"}
-->

<!-- IRONWOVEN_CHRONOLOGY
{"record_id":"IRONWOVEN-BETA-CHANGELOG-FIX-0003","record_type":"beta_accepted_fix_create_kinetic","created_at":"unknown","updated_at":"unknown","verified_at":"2026-11-13T13:52:01Z","migrated_at":"2026-11-13T13:52:01Z","source_ref":["Beta CHANGELOG.md — accepted bug-fix entry: Create Kinetic missing/stale loot-table item references. Private accepted-bug-fixes.json confirms exact ID create-kinetic-missing-loot-items remains status accepted and active; no new acceptance/test decision was made."],"timezone_display":"Europe/Amsterdam","chronology_status":"CURRENT"}
-->

<!-- IRONWOVEN_CHRONOLOGY
{"record_id":"IRONWOVEN-BETA-CHANGELOG-FIX-0004","record_type":"beta_accepted_fix_createdeco","created_at":"unknown","updated_at":"unknown","verified_at":"2026-11-13T13:52:01Z","migrated_at":"2026-11-13T13:52:01Z","source_ref":["Beta CHANGELOG.md — accepted bug-fix entry: Create Deco placard recipe invalid ingredient key. Private accepted-bug-fixes.json confirms exact ID createdeco-placard-recipe-ingredient remains status accepted and active; no new acceptance/test decision was made."],"timezone_display":"Europe/Amsterdam","chronology_status":"CURRENT"}
-->

<!-- IRONWOVEN_CHRONOLOGY
{"record_id":"IRONWOVEN-BETA-CHANGELOG-FIX-0005","record_type":"beta_accepted_fix_sable_copycats","created_at":"unknown","updated_at":"unknown","verified_at":"2026-11-13T13:52:01Z","migrated_at":"2026-11-13T13:52:01Z","source_ref":["Beta CHANGELOG.md — accepted bug-fix entry: Sable / Copycats+ Catwalk physics selector points to an unregistered block. Private accepted-bug-fixes.json confirms exact ID sable-copycats-catwalk-selector remains status accepted and active; no new acceptance/test decision was made."],"timezone_display":"Europe/Amsterdam","chronology_status":"CURRENT"}
-->

These five defects affect 455 individual resources in total, but contribute **5** to the bug-fix component. Four maintained datapacks address the five defects. Their targeted log-level retests passed; this does not claim every affected in-game feature has completed full functional testing.

<!-- IRONWOVEN_CHRONOLOGY
{"record_id":"IRONWOVEN-BETA-CHANGELOG-0004","record_type":"beta_every_compat_moonlight_accepted_pair","created_at":"unknown","updated_at":"unknown","verified_at":"2026-11-13T13:52:01Z","migrated_at":"2026-11-13T13:52:01Z","source_ref":["Beta CHANGELOG.md — accepted baseline pair Every Compat 2.11.57 / file 9468938 and Moonlight Lib 3.8.2 / file 9458248. Current accepted pair checked against private Master Mod List, Project Status and Current Work Plan; Golden Cherry Leaves duplicate remains open."],"timezone_display":"Europe/Amsterdam","chronology_status":"CURRENT"}
-->

## Other accepted mod updates

- Every Compat (Wood Good) updated from 2.11.56 to 2.11.57 (CurseForge file 9468938).
- Required Moonlight Lib (Selene) dependency updated from 3.8.1 to 3.8.2 (CurseForge file 9458248).

These are version updates to existing mod files. Their byte changes are detected by the content fingerprint when those files are present in the selected server `mods/` folder.

## Accepted mod updates — 10–11 November 2026

<!-- IRONWOVEN_CHRONOLOGY
{"record_id":"IRONWOVEN-BETA-CHANGELOG-0005","record_type":"beta_sophisticated_backpacks_core_accepted_pair","created_at":"unknown","updated_at":"unknown","verified_at":"2026-11-13T13:52:01Z","migrated_at":"2026-11-13T13:52:01Z","source_ref":["Beta CHANGELOG.md — Sophisticated Backpacks 3.26.21.2249 / file 9524812 and Sophisticated Core 1.5.32.2464 / file 9524669 accepted as a coordinated pair after authorised shared smoke and exact client/server SHA-256 parity. Backpacks feature actions remain Pending; Core has no standalone feature result. Checked against current private status."],"timezone_display":"Europe/Amsterdam","chronology_status":"CURRENT"}
-->

- Sophisticated Backpacks updated from 3.26.20.2244 (CurseForge file 9431839) to 3.26.21.2249 (file 9524812); authorised shared smoke PASS and exact client/server SHA-256 parity confirmed.
- Sophisticated Core dependency updated from 1.5.28.2458 (file 9431812) to 1.5.32.2464 (file 9524669); validated in the same coordinated Backpacks smoke test and hash-matched on both sides.
<!-- IRONWOVEN_CHRONOLOGY
{"record_id":"IRONWOVEN-BETA-CHANGELOG-0006","record_type":"beta_tfmg_accepted_update","created_at":"unknown","updated_at":"unknown","verified_at":"2026-11-13T13:52:01Z","migrated_at":"2026-11-13T13:52:01Z","source_ref":["Beta CHANGELOG.md — TFMG Community Edition 1.3.3a / file 9482161 accepted after authorised shared smoke and exact client/server hash parity; feature/visual actions remain Pending and Custom License review is a separate distribution gate."],"timezone_display":"Europe/Amsterdam","chronology_status":"CURRENT"}
-->

- Create: The Factory Must Grow Community Edition updated from 1.3.3 (file 9413167) to 1.3.3a (file 9482161); authorised shared smoke PASS and exact client/server SHA-256 parity confirmed.
<!-- IRONWOVEN_CHRONOLOGY
{"record_id":"IRONWOVEN-BETA-CHANGELOG-0007","record_type":"beta_fastsuite_placebo_accepted_pair","created_at":"unknown","updated_at":"unknown","verified_at":"2026-11-13T13:52:01Z","migrated_at":"2026-11-13T13:52:01Z","source_ref":["Beta CHANGELOG.md — FastSuite 6.0.7 / file 7527945 and Placebo 9.9.4 / file 9153039 accepted after exact preflight, matching client/server profile hashes and authorised combined smoke; feature/performance actions remain for beta testers."],"timezone_display":"Europe/Amsterdam","chronology_status":"CURRENT"}
-->

<!-- IRONWOVEN_CHRONOLOGY
{"record_id":"IRONWOVEN-BETA-CHANGELOG-0008","record_type":"beta_fastfurnace_preflight_and_release_freeze_gate","created_at":"unknown","updated_at":"unknown","verified_at":"2026-11-13T13:52:01Z","migrated_at":"2026-11-13T13:52:01Z","source_ref":["Beta CHANGELOG.md — FastFurnace 9.0.1 / file 6751551 exact 1.21.1 NeoForge Release/dependency/side preflight and combined-profile smoke are PASS; explicit mod-set/package disposition remains for release freeze and is not implied by profile presence."],"timezone_display":"Europe/Amsterdam","chronology_status":"CURRENT"}
-->

- FastSuite 6.0.7 (CurseForge file 7527945) and Placebo 9.9.4 (file 9153039) accepted into the active mod set after exact-file/dependency preflight, matching client/server hashes, and authorised combined-profile smoke PASS on 11 November. No isolated optimizer run is required; recipe-behavior and optional performance checks remain Pending for beta testers. FastFurnace 9.0.1 (CurseForge file 6751551) also passed exact 1.21.1 NeoForge file/dependency/side preflight and loaded on both sides in the same combined-profile smoke PASS. Do not add a duplicate or repeat the smoke. Its explicit mod-set/package disposition remains for release freeze; feature/performance validation belongs to beta testers.

<!-- IRONWOVEN_CHRONOLOGY
{"record_id":"IRONWOVEN-BETA-CHANGELOG-0009","record_type":"beta_feature_license_and_deployment_gates","created_at":"unknown","updated_at":"unknown","verified_at":"2026-11-13T13:52:01Z","migrated_at":"2026-11-13T13:52:01Z","source_ref":["Beta CHANGELOG.md — current separation of smoke from feature/function validation, TFMG Custom License review, and deployment of accepted working-profile updates to the selected clean versioned v.0.1 server. Private Project Status preserves these gates; version remains unchanged until the selected server is updated and updater previewed."],"timezone_display":"Europe/Amsterdam","chronology_status":"CURRENT"}
-->

Feature/function checks remain pending and are not marked Pass from smoke testing. TFMG's Custom License distribution review remains a separate release gate. The versioned clean v.0.1 server has not been re-scanned after deployment of these test-profile updates; retain its recorded automatic version until the selected server itself is updated and the private updater is previewed.

<!-- IRONWOVEN_CHRONOLOGY
{"record_id":"IRONWOVEN-BETA-CHANGELOG-0010","record_type":"beta_gadgets_gizmos_hold","created_at":"unknown","updated_at":"unknown","verified_at":"2026-11-13T13:52:01Z","migrated_at":"2026-11-13T13:52:01Z","source_ref":["Beta CHANGELOG.md — Create Aeronautics: Gadgets & Gizmos 2.0.0-Pre-Release-4 is ON HOLD; bundled 1.2.10 stays unchanged until stable 2.x and exact review plus separate approval. Current private status/hold/compatibility boundary retained; no test, hold, exclusion, or distribution approval changed."],"timezone_display":"Europe/Amsterdam","chronology_status":"CURRENT"}
-->

<!-- IRONWOVEN_CHRONOLOGY
{"record_id":"IRONWOVEN-BETA-CHANGELOG-0011","record_type":"beta_aeronautics_structures_test_only_fix","created_at":"unknown","updated_at":"unknown","verified_at":"2026-11-13T13:52:01Z","migrated_at":"2026-11-13T13:52:01Z","source_ref":["Beta CHANGELOG.md — Aeronautics Structures uniform-loot override remains test-only, not an accepted distributed pack fix or permission to resume the held candidate. Current private status/hold/compatibility boundary retained; no test, hold, exclusion, or distribution approval changed."],"timezone_display":"Europe/Amsterdam","chronology_status":"CURRENT"}
-->

<!-- IRONWOVEN_CHRONOLOGY
{"record_id":"IRONWOVEN-BETA-CHANGELOG-0012","record_type":"beta_struts_patch_not_distributed","created_at":"unknown","updated_at":"unknown","verified_at":"2026-11-13T13:52:01Z","migrated_at":"2026-11-13T13:52:01Z","source_ref":["Beta CHANGELOG.md — local Struts JAR patch is not part of the accepted pack; the standard-install/release-safe fix requirement remains open. Current private status/hold/compatibility boundary retained; no test, hold, exclusion, or distribution approval changed."],"timezone_display":"Europe/Amsterdam","chronology_status":"CURRENT"}
-->

<!-- IRONWOVEN_CHRONOLOGY
{"record_id":"IRONWOVEN-BETA-CHANGELOG-0013","record_type":"beta_powergrid_workaround_not_distributed","created_at":"unknown","updated_at":"unknown","verified_at":"2026-11-13T13:52:01Z","migrated_at":"2026-11-13T13:52:01Z","source_ref":["Beta CHANGELOG.md — PowerGrid native DLL workaround is not an accepted distributed pack fix; the release packaging path remains open. Current private status/hold/compatibility boundary retained; no test, hold, exclusion, or distribution approval changed."],"timezone_display":"Europe/Amsterdam","chronology_status":"CURRENT"}
-->

<!-- IRONWOVEN_CHRONOLOGY
{"record_id":"IRONWOVEN-BETA-CHANGELOG-0014","record_type":"beta_sbt_workaround_not_distributed","created_at":"unknown","updated_at":"unknown","verified_at":"2026-11-13T13:52:01Z","migrated_at":"2026-11-13T13:52:01Z","source_ref":["Beta CHANGELOG.md — Shulker Box Tooltip / Supplementaries config workaround is not an accepted distributed pack fix; the documented preview trade-off remains separate. Current private status/hold/compatibility boundary retained; no test, hold, exclusion, or distribution approval changed."],"timezone_display":"Europe/Amsterdam","chronology_status":"CURRENT"}
-->

## Not counted as accepted bug fixes

- Create Aeronautics: Gadgets & Gizmos 2.0.0-Pre-Release-4 (CurseForge file 9260191) is **ON HOLD**. Do not install or test this prerelease; keep bundled 1.2.10 (file 9141062) unchanged until a stable 2.x release and exact dependency/side/version review are available, followed by separate maintainer approval.
- The Aeronautics Structures uniform-loot override remains test-only.
- The local Struts JAR patch is not part of the accepted pack.
- The PowerGrid native DLL workaround and Shulker Box Tooltip / Supplementaries config workaround are not accepted distributed pack fixes.

<!-- IRONWOVEN_CHRONOLOGY
{"record_id":"IRONWOVEN-BETA-CHANGELOG-0015","record_type":"beta_changelog_release_status","created_at":"unknown","updated_at":"unknown","verified_at":"2026-11-13T13:52:01Z","migrated_at":"2026-11-13T13:52:01Z","source_ref":["Beta CHANGELOG.md — internal development only; no downloadable public beta package has been published. Current NOT READY state checked against private Project Status and Beta Release Checklist."],"timezone_display":"Europe/Amsterdam","chronology_status":"CURRENT"}
-->

**Release status:** internal development. No downloadable public beta package has been published.
