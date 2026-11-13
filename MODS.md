# Mods in Create IronWoven: Age of Industry

**Inventory status:** The dated test-folder tables were moved to [the historical snapshot archive](archive/MODS_HISTORICAL_TEST_FOLDER_SNAPSHOT_2026-11-11.md). This page now summarizes accepted mod-set updates and unresolved working-profile observations; it is not the complete current file inventory or a release manifest.
<!-- IRONWOVEN_AUTO_VERSION -->
**Current Ironwoven pack version:** `v0.1.101.5` — release `0`, content revision `1`, `101` top-level server mod JARs, and `5` active accepted bug fixes.

**This page is not a final release manifest.** It summarizes smoke-qualified mod-set updates and unresolved working-profile observations; it does not publish the final CurseForge client/server package inventory.

## Active mod-set updates — verified 10–11 November 2026

The following exact versions passed their authorised, scope-appropriate shared smoke tests and are accepted into the active mod set. This does **not** mark their feature tests complete or grant downloadable-beta/release approval.

| Mod | Previous version / CurseForge file | Accepted version / CurseForge file | Smoke evidence | Feature / release state |
|---|---|---|---|---|
| FastSuite / Placebo | New active mod-set addition | 6.0.7 / file 7527945 + 9.9.4 / file 9153039 | Exact-file/dependency preflight, matching client/server profile hashes, and authorised 11 November combined-profile smoke PASS | Accepted into active mod set; recipe behavior and optional performance actions Pending for beta testers |
| Sophisticated Backpacks | 3.26.20.2244 / [9431839](https://www.curseforge.com/minecraft/mc-mods/sophisticated-backpacks/files/9431839) | 3.26.21.2249 / [9524812](https://www.curseforge.com/minecraft/mc-mods/sophisticated-backpacks/files/9524812) | Shared startup/login/clean-shutdown PASS, 10 November; exact client/server SHA-256 match | Feature actions Pending — beta testers |
| Sophisticated Core (support dependency) | 1.5.28.2458 / [9431812](https://www.curseforge.com/minecraft/mc-mods/sophisticated-core/files/9431812) | 1.5.32.2464 / [9524669](https://www.curseforge.com/minecraft/mc-mods/sophisticated-core/files/9524669) | Same coordinated Backpacks smoke; exact client/server SHA-256 match | Accepted support dependency; tested through Backpacks; no standalone gameplay row |
| Create: The Factory Must Grow Community Edition | 1.3.3 / [9413167](https://www.curseforge.com/minecraft/mc-mods/tfmg-community-edition/files/9413167) | 1.3.3a / [9482161](https://www.curseforge.com/minecraft/mc-mods/tfmg-community-edition/files/9482161) | Shared startup/login/clean-shutdown PASS, 10 November; exact client/server SHA-256 match | Feature/visual actions Pending; Custom License distribution review remains a separate release gate |

The 10 November active-profile archive audit found 102 JARs in each test-profile archive: 101 shared non-WITS JARs have identical hashes. WITS is a temporary testing utility and is excluded from the mod set. Railways `0.3.0-beta.2` and Supplementaries `4.0.2` also appear in both archives with matching hashes. Exact CurseForge file reviews are complete; their remaining gates are separate: Railways remains a Beta-channel observation pending explicit mod-set/package disposition against the older accepted `0.3.0-alpha.2` baseline; Supplementaries `4.0.2` remains an active-profile observation, not an accepted update, with exact Moonlight version closure and final Custom License review still open. Neither profile presence nor file review is a feature-test PASS or package approval. These profiles are not the selected clean v.0.1 release server. Waystones 21.1.46 appears in the 10 November working profile, but its prior core-Waystones package deferral remains unresolved. Base Sable 2.0.6 is a separate SubLevel physics library already present for Create/Aeronautics. The distinct Waystones: Sable 1.0.7 compatibility addon (CurseForge project 1524471, MIT, Client & Server) is absent and remains optional/deferred; declared requirements are Waystones 21.1.36+, Sable 2.0.3+, and Create 6.0.10+. Do not add it until core Waystones is explicitly retained and AeroPortals/travel overlap is resolved.



## Present in the tested profile — mod-set/package disposition pending

- **FastFurnace 9.0.1 · CurseForge file 6751551:** exact 1.21.1 NeoForge Release, MIT, Client & Server metadata, and required Placebo relation are verified. Placebo 9.9.4 (file 9153039) satisfies the upstream 9.0.1 dependency baseline. Exact-file/dependency/side preflight PASS; combined-profile startup/world/login/shutdown smoke PASS on 11 November. It is already present—do not add a duplicate. Its explicit mod-set/package disposition remains for release freeze; no feature or performance claims are made from smoke evidence.

## Recent shared-profile smoke observations

- **FastSuite 6.0.7 / Placebo 9.9.4 — 11 November:** accepted into the active mod set after exact-file/dependency preflight, matching client/server hashes and combined-profile smoke PASS. No isolated optimizer test is required; feature actions remain for beta testers. FastFurnace 9.0.1 (file 6751551) also loaded in that session and passed exact CurseForge file/dependency/side preflight; its final mod-set/package disposition remains pending.
- **Sophisticated Backpacks 3.26.21.2249 (file 9524812) / Sophisticated Core 1.5.32.2464 (file 9524669) — 10 November:** accepted into the active mod set after authorised shared smoke PASS and exact client/server SHA-256 parity. Backpack feature actions remain Pending for beta testers; Core is validated through Backpacks.
- **Create: The Factory Must Grow Community Edition 1.3.3a (file 9482161) — 10 November:** accepted into the active mod set after authorised shared smoke PASS and exact client/server SHA-256 parity. Feature/visual actions remain Pending; Custom License distribution review remains a separate release gate.
- **Every Compat 2.11.57 / Moonlight Lib 3.8.2:** accepted baseline pair; fresh clean-server smoke passed. The Golden Cherry Leaves duplicate registration remains open.

The 101-JAR clean Windows server baseline is a separate 7 November test installation. It is the source for the generated development version above, not a final release package. The numbered installation-batch sequence has since been retired; use [Beta Status](BETA_STATUS.md) and [Mod Plans](MOD_PLANS.md) for current decisions.

## Active-profile observations — exact file review (11 November 2026)

- **Railways 0.3.0-beta.2:** the 10 November profiles contain the same JAR/hash. Exact [CurseForge Beta file 8522154](https://www.curseforge.com/minecraft/mc-mods/steam-n-rails-neoforge/files/8522154) is Client & Server for 1.21.1 NeoForge (LGPLv3); the required Create dependency and source version minima are met by the recorded Create 6.0.10 / NeoForge 21.1.265. Blocks & Bogies' 1.21.1 menu-compat restoration was merged upstream ([PR #31](https://github.com/WeidosOddities/Blocks-And-Bogies/pull/31)); the later bogey-menu report closed after the reporter updated both mods ([issue #181](https://github.com/Porters-of-Railways/Railway-1.21.1/issues/181)). This is not an IronWoven feature-test result. The observed file remains a **Beta**, older accepted record is alpha.2, and mod-set/package disposition remains separate. Steam 'n' Rails' optional track-loot-table fix remains in its existing workstream.
- **Supplementaries 4.0.2:** exact [CurseForge Release file 9211734](https://www.curseforge.com/minecraft/mc-mods/supplementaries/files/9211734) is Client & Server for 1.21.1 NeoForge and requires Moonlight Lib. The 10 November profile contains Moonlight 3.8.2; current [Moonlight 3.8.3 Release file 9519534](https://www.curseforge.com/minecraft/mc-mods/selene/files/9519534) is newer. No matching public source metadata was found to establish the exact 4.0.2 Moonlight minimum, so do not assume 3.8.3 is mandatory. The Shulker Box Tooltip provider issue and tested client workaround remain a separate compatibility limitation; remote/server-supplied preview extras are unavailable with that workaround. Custom License review remains separate.
- **Create Aeronautics Curios Compat:** exact [CurseForge Release file 9076258](https://www.curseforge.com/minecraft/mc-mods/create-aeronautics-x-curios-api-compat/files/9076258) is version 2.3. Its matching upstream source sets the build version to 2.3 but hard-codes NeoForge descriptor metadata to 2.0, explaining the observed filename/metadata difference. Do not treat this as evidence of an outdated JAR or change the file on that basis.
- **Waystones 21.1.46:** present in the 10 November profile, but core-Waystones package inclusion remains deferred. **Base Sable 2.0.6** is a separate SubLevel physics library already present for Create/Aeronautics; it is not the Waystones compatibility addon. The distinct Waystones: Sable 1.0.7 add-on is absent and remains optional/deferred pending a core-Waystones decision and AeroPortals overlap review.
- **FastFurnace 9.0.1:** exact CurseForge file/dependency/side preflight and combined-profile smoke both PASS. Do not add a duplicate or repeat the test. Record its explicit mod-set/package disposition at release freeze.

## Holds and exclusions

- **Create Aeronautics Structures 1.1.0-Beta-3.1:** ON HOLD; not eligible for the beta package.
- **Create Aeronautics: Gadgets & Gizmos 2.0.0-Pre-Release-4:** ON HOLD; keep bundled 1.2.10 unchanged.
- **Lithium 0.15.4:** ON HOLD / deferred.
- End expansion and Terralith investigation remain paused. Preserve BYG 2.6.3, Regions Unexplored 0.6.3, and existing worlds.
- Explicit exclusions remain: Carry On, Easy Villagers, Immersive Paintings, Bigger Better End Cities, Create: Sophisticated Exoskeleton 1.0, and Distant Horizons 3.3.3.

## Required additions

**No additional mod is currently approved or evidenced as a mandatory addition.** Waystones: Sable 1.0.7 is an optional compatibility candidate, not a required missing dependency: base Sable 2.0.6 is already present, while the add-on is absent and deferred. Optional ideas and prerequisite-dependent candidates are listed in [Mod Plans](MOD_PLANS.md). Do not install candidates or change the mod set without explicit maintainer approval.

## Historical inventory archive

The former detailed test-folder tables are preserved in [the historical snapshot archive](archive/MODS_HISTORICAL_TEST_FOLDER_SNAPSHOT_2026-11-11.md). They are retained for relevant historical comparison only and must not be used to construct a current or release package.


<!-- IRONWOVEN_CHRONOLOGY
{
  "record_id": "IRONWOVEN-BETA-PUBLIC-0002",
  "record_type": "public_mod_inventory_summary",
  "created_at": "2026-11-03T22:20:33Z",
  "updated_at": "2026-11-13T13:04:33Z",
  "verified_at": "2026-11-13T13:04:33Z",
  "migrated_at": "2026-11-13T13:04:33Z",
  "source_ref": [
    "Git history: MODS.md first added in commit bd2f320edf737f18a659ca69f7f237cccb444014 (2026-11-03T22:20:33Z); latest pre-migration update 985e790ed29c0318847632c9d02e5bbb243229b1 (2026-11-11T20:41:54Z). These are repository record timestamps only.",
    "Source: MODS.md — inventory status, generated development version, final-release-manifest limitation, and historical inventory archive pointer.",
    "Cross-check: BETA_STATUS.md, MOD_PLANS.md, TESTING_CHECKLIST.md, and CHANGELOG.md. This page is a current summary, not a complete current file inventory or release manifest; no mod selection or release approval is implied."
  ],
  "timezone_display": "Europe/Amsterdam",
  "chronology_status": "CURRENT"
}
-->

<!-- IRONWOVEN_CHRONOLOGY
{
  "record_id": "IRONWOVEN-BETA-PUBLIC-0003",
  "record_type": "active_modset_update",
  "created_at": "unknown",
  "updated_at": "unknown",
  "verified_at": "2026-11-13T13:04:33Z",
  "migrated_at": "2026-11-13T13:04:33Z",
  "source_ref": [
    "Source: MODS.md — Active mod-set updates — FastSuite / Placebo row; Recent shared-profile smoke observations — FastSuite / Placebo entry.",
    "Cross-check: BETA_STATUS.md — Active mod-set updates and TESTING_CHECKLIST.md — current verification snapshot. Exact-file/dependency preflight, matching client/server hashes, and the authorised 11 November combined-profile smoke PASS are preserved as recorded; recipe/function and optional performance actions remain Pending for beta testers. The smoke was not rerun."
  ],
  "timezone_display": "Europe/Amsterdam",
  "chronology_status": "CURRENT"
}
-->

<!-- IRONWOVEN_CHRONOLOGY
{
  "record_id": "IRONWOVEN-BETA-PUBLIC-0004",
  "record_type": "active_modset_update",
  "created_at": "unknown",
  "updated_at": "unknown",
  "verified_at": "2026-11-13T13:04:33Z",
  "migrated_at": "2026-11-13T13:04:33Z",
  "source_ref": [
    "Source: MODS.md — Active mod-set updates — Sophisticated Backpacks row; Recent shared-profile smoke observations — Backpacks / Core entry.",
    "Cross-check: BETA_STATUS.md and TESTING_CHECKLIST.md. The 10 November shared startup/login/clean-shutdown PASS and exact client/server SHA-256 parity are preserved; feature actions remain Pending for beta testers. The smoke was not rerun."
  ],
  "timezone_display": "Europe/Amsterdam",
  "chronology_status": "CURRENT"
}
-->

<!-- IRONWOVEN_CHRONOLOGY
{
  "record_id": "IRONWOVEN-BETA-PUBLIC-0005",
  "record_type": "active_modset_support_dependency_update",
  "created_at": "unknown",
  "updated_at": "unknown",
  "verified_at": "2026-11-13T13:04:33Z",
  "migrated_at": "2026-11-13T13:04:33Z",
  "source_ref": [
    "Source: MODS.md — Active mod-set updates — Sophisticated Core support-dependency row; Recent shared-profile smoke observations — Backpacks / Core entry.",
    "Cross-check: BETA_STATUS.md and TESTING_CHECKLIST.md. Core is validated through the coordinated Backpacks smoke and has no standalone gameplay row; the 10 November shared smoke PASS is preserved and was not rerun."
  ],
  "timezone_display": "Europe/Amsterdam",
  "chronology_status": "CURRENT"
}
-->

<!-- IRONWOVEN_CHRONOLOGY
{
  "record_id": "IRONWOVEN-BETA-PUBLIC-0006",
  "record_type": "active_modset_update",
  "created_at": "unknown",
  "updated_at": "unknown",
  "verified_at": "2026-11-13T13:04:33Z",
  "migrated_at": "2026-11-13T13:04:33Z",
  "source_ref": [
    "Source: MODS.md — Active mod-set updates — Create: The Factory Must Grow Community Edition row; Recent shared-profile smoke observations — TFMG entry.",
    "Cross-check: BETA_STATUS.md and TESTING_CHECKLIST.md. The 10 November shared startup/login/clean-shutdown PASS and exact client/server SHA-256 parity are preserved; feature/visual actions remain Pending and the Custom License distribution review remains a separate release gate. No smoke test was rerun."
  ],
  "timezone_display": "Europe/Amsterdam",
  "chronology_status": "CURRENT"
}
-->

<!-- IRONWOVEN_CHRONOLOGY
{
  "record_id": "IRONWOVEN-BETA-PUBLIC-0007",
  "record_type": "active_profile_preflight_and_disposition",
  "created_at": "unknown",
  "updated_at": "unknown",
  "verified_at": "2026-11-13T13:04:33Z",
  "migrated_at": "2026-11-13T13:04:33Z",
  "source_ref": [
    "Source: MODS.md — Present in the tested profile — FastFurnace 9.0.1; Recent shared-profile smoke observations — FastFurnace entry; Active-profile observations — FastFurnace entry.",
    "Cross-check: BETA_STATUS.md and TESTING_CHECKLIST.md. Exact CurseForge file/dependency/side preflight and combined-profile startup/world/login/shutdown smoke PASS on 11 November remain recorded. FastFurnace is already present; do not add a duplicate or repeat the smoke. Its explicit mod-set/package disposition remains open for release freeze. No feature or performance claim is made."
  ],
  "timezone_display": "Europe/Amsterdam",
  "chronology_status": "CURRENT"
}
-->

<!-- IRONWOVEN_CHRONOLOGY
{
  "record_id": "IRONWOVEN-BETA-PUBLIC-0008",
  "record_type": "active_profile_observation",
  "created_at": "unknown",
  "updated_at": "unknown",
  "verified_at": "2026-11-13T13:04:33Z",
  "migrated_at": "2026-11-13T13:04:33Z",
  "source_ref": [
    "Source: MODS.md — Active-profile observations — Railways 0.3.0-beta.2; BETA_STATUS.md — 10 November active-profile archive audit; MOD_PLANS.md — active-profile observations.",
    "The exact CurseForge file review is recorded as complete in the public Beta evidence. The observed file remains a Beta-channel version; the older accepted baseline is 0.3.0-alpha.2 and explicit mod-set/package disposition remains open. The 3 November alpha.2 feature result is historical and is not a beta.2 feature-test PASS. This chronology check did not rerun a test or reopen the external source page."
  ],
  "timezone_display": "Europe/Amsterdam",
  "chronology_status": "CURRENT"
}
-->

<!-- IRONWOVEN_CHRONOLOGY
{
  "record_id": "IRONWOVEN-BETA-PUBLIC-0009",
  "record_type": "active_profile_observation",
  "created_at": "unknown",
  "updated_at": "unknown",
  "verified_at": "2026-11-13T13:04:33Z",
  "migrated_at": "2026-11-13T13:04:33Z",
  "source_ref": [
    "Source: MODS.md — Active-profile observations — Supplementaries 4.0.2; BETA_STATUS.md — 10 November active-profile archive audit; MOD_PLANS.md — active-profile observations.",
    "The exact CurseForge file review is recorded as complete. Supplementaries 4.0.2 remains an active-profile observation, not an accepted update. The exact Moonlight minimum is not established; the 10 November profile contained Moonlight 3.8.2, while 3.8.3 is newer but not proven mandatory. Final Custom License review remains open. The older 3.4.0 evidence and separate Shulker Box Tooltip provider limitation are preserved; no feature test was rerun."
  ],
  "timezone_display": "Europe/Amsterdam",
  "chronology_status": "CURRENT"
}
-->

<!-- IRONWOVEN_CHRONOLOGY
{
  "record_id": "IRONWOVEN-BETA-PUBLIC-0010",
  "record_type": "source_metadata_reconciliation",
  "created_at": "unknown",
  "updated_at": "unknown",
  "verified_at": "2026-11-13T13:04:33Z",
  "migrated_at": "2026-11-13T13:04:33Z",
  "source_ref": [
    "Source: MODS.md — Active-profile observations — Create Aeronautics Curios Compat.",
    "The public record identifies CurseForge Release file 9076258 as version 2.3 and explains the filename/build-version 2.3 versus NeoForge descriptor metadata 2.0 discrepancy. No JAR change is indicated. This is source-metadata reconciliation, not a feature-test PASS; final All Rights Reserved terms/package review remains separate. The external source was not reopened during this chronology migration."
  ],
  "timezone_display": "Europe/Amsterdam",
  "chronology_status": "CURRENT"
}
-->

<!-- IRONWOVEN_CHRONOLOGY
{
  "record_id": "IRONWOVEN-BETA-PUBLIC-0011",
  "record_type": "active_profile_disposition",
  "created_at": "unknown",
  "updated_at": "unknown",
  "verified_at": "2026-11-13T13:04:33Z",
  "migrated_at": "2026-11-13T13:04:33Z",
  "decision_at": "unknown",
  "source_ref": [
    "Source: MODS.md — Active-profile observations — Waystones 21.1.46, Base Sable 2.0.6, and Waystones: Sable 1.0.7; MOD_PLANS.md — Waystones deferral and optional candidate notes.",
    "Core-Waystones package inclusion remains deferred. Base Sable 2.0.6 is a separate SubLevel physics library already present; the distinct Waystones: Sable 1.0.7 addon is absent and remains optional/deferred pending an explicit core-Waystones decision and overlap review. Profile presence is not approval."
  ],
  "timezone_display": "Europe/Amsterdam",
  "chronology_status": "CURRENT"
}
-->

<!-- IRONWOVEN_CHRONOLOGY
{
  "record_id": "IRONWOVEN-BETA-PUBLIC-0012",
  "record_type": "active_mod_hold",
  "created_at": "unknown",
  "updated_at": "unknown",
  "verified_at": "2026-11-13T13:04:33Z",
  "migrated_at": "2026-11-13T13:04:33Z",
  "decision_at": "unknown",
  "source_ref": [
    "Source: MODS.md — Holds and exclusions — Create Aeronautics Structures 1.1.0-Beta-3.1; BETA_STATUS.md — Holds and safeguards; KNOWN_ISSUES.md.",
    "The candidate remains ON HOLD because the known loot-table and crashed-airship chest issues are unresolved. It is not eligible for the Beta package. Existing test-only evidence and the hold are preserved; no new test was run."
  ],
  "timezone_display": "Europe/Amsterdam",
  "chronology_status": "CURRENT"
}
-->

<!-- IRONWOVEN_CHRONOLOGY
{
  "record_id": "IRONWOVEN-BETA-PUBLIC-0013",
  "record_type": "active_mod_hold",
  "created_at": "unknown",
  "updated_at": "unknown",
  "verified_at": "2026-11-13T13:04:33Z",
  "migrated_at": "2026-11-13T13:04:33Z",
  "decision_at": "unknown",
  "source_ref": [
    "Source: MODS.md — Holds and exclusions — Create Aeronautics: Gadgets & Gizmos 2.0.0-Pre-Release-4; BETA_STATUS.md — Holds and safeguards.",
    "The 2.0.0 prerelease remains ON HOLD. Keep bundled 1.2.10 unchanged; do not install or test the prerelease. The hold is not cleared by the chronology migration."
  ],
  "timezone_display": "Europe/Amsterdam",
  "chronology_status": "CURRENT"
}
-->

<!-- IRONWOVEN_CHRONOLOGY
{
  "record_id": "IRONWOVEN-BETA-PUBLIC-0014",
  "record_type": "active_mod_hold",
  "created_at": "unknown",
  "updated_at": "unknown",
  "verified_at": "2026-11-13T13:04:33Z",
  "migrated_at": "2026-11-13T13:04:33Z",
  "decision_at": "unknown",
  "source_ref": [
    "Source: MODS.md — Holds and exclusions — Lithium 0.15.4; BETA_STATUS.md — Holds and safeguards.",
    "Lithium 0.15.4 remains ON HOLD / deferred. No mod-set change or test was performed."
  ],
  "timezone_display": "Europe/Amsterdam",
  "chronology_status": "CURRENT"
}
-->

<!-- IRONWOVEN_CHRONOLOGY
{
  "record_id": "IRONWOVEN-BETA-PUBLIC-0015",
  "record_type": "paused_worldgen_workstream",
  "created_at": "unknown",
  "updated_at": "unknown",
  "verified_at": "2026-11-13T13:04:33Z",
  "migrated_at": "2026-11-13T13:04:33Z",
  "decision_at": "unknown",
  "source_ref": [
    "Source: MODS.md — Holds and exclusions — End expansion and Terralith investigation; BETA_STATUS.md — Holds and safeguards; DIMENSIONS.md.",
    "The End workstream and Terralith investigation remain paused. Preserve BYG 2.6.3, Regions Unexplored 0.6.3, and existing worlds. No world-generation, datapack, server, or world change was made."
  ],
  "timezone_display": "Europe/Amsterdam",
  "chronology_status": "CURRENT"
}
-->

<!-- IRONWOVEN_CHRONOLOGY
{
  "record_id": "IRONWOVEN-BETA-PUBLIC-0016",
  "record_type": "explicit_mod_exclusions",
  "created_at": "unknown",
  "updated_at": "unknown",
  "verified_at": "2026-11-13T13:04:33Z",
  "migrated_at": "2026-11-13T13:04:33Z",
  "decision_at": "unknown",
  "source_ref": [
    "Source: MODS.md — Holds and exclusions — Explicit exclusions.",
    "The current explicit exclusion group remains Carry On, Easy Villagers, Immersive Paintings, Bigger Better End Cities, Create: Sophisticated Exoskeleton 1.0, and Distant Horizons 3.3.3. No exclusion was cleared or reclassified."
  ],
  "timezone_display": "Europe/Amsterdam",
  "chronology_status": "CURRENT"
}
-->

<!-- IRONWOVEN_CHRONOLOGY
{
  "record_id": "IRONWOVEN-BETA-PUBLIC-0017",
  "record_type": "mod_selection_approval_boundary",
  "created_at": "unknown",
  "updated_at": "unknown",
  "verified_at": "2026-11-13T13:04:33Z",
  "migrated_at": "2026-11-13T13:04:33Z",
  "decision_at": "unknown",
  "source_ref": [
    "Source: MODS.md — Required additions; MOD_PLANS.md — candidate and prerequisite-dependent work.",
    "No additional mod is currently approved or evidenced as a mandatory addition. Waystones: Sable 1.0.7 remains optional/deferred; candidate research does not authorize installation or mod-set changes. Explicit maintainer approval remains required."
  ],
  "timezone_display": "Europe/Amsterdam",
  "chronology_status": "CURRENT"
}
-->

<!-- IRONWOVEN_CHRONOLOGY
{
  "record_id": "IRONWOVEN-BETA-PUBLIC-0018",
  "record_type": "historical_profile_archive_snapshot",
  "created_at": "unknown",
  "updated_at": "unknown",
  "verified_at": "unknown",
  "migrated_at": "2026-11-13T13:04:33Z",
  "source_ref": [
    "Source: MODS.md — 10 November active-profile archive audit.",
    "Historical observation: each test-profile archive contained 102 JARs; 101 shared non-WITS JARs had identical hashes. WITS was a temporary testing utility excluded from the mod set. Exact event time is not recorded; the archived profile was not reopened during this migration. This snapshot is not the selected clean release server or a release manifest."
  ],
  "timezone_display": "Europe/Amsterdam",
  "chronology_status": "HISTORICAL"
}
-->

<!-- IRONWOVEN_CHRONOLOGY
{
  "record_id": "IRONWOVEN-BETA-PUBLIC-0019",
  "record_type": "accepted_baseline_pair_smoke_observation",
  "created_at": "unknown",
  "updated_at": "unknown",
  "verified_at": "2026-11-13T13:04:33Z",
  "migrated_at": "2026-11-13T13:04:33Z",
  "source_ref": [
    "Source: MODS.md — Recent shared-profile smoke observations — Every Compat 2.11.57 / Moonlight Lib 3.8.2.",
    "The accepted baseline pair remains recorded after a fresh clean-server smoke PASS. The Golden Cherry Leaves duplicate-registration finding remains open and is not cleared by that smoke result. The exact smoke time is not recorded and the test was not rerun during chronology migration."
  ],
  "timezone_display": "Europe/Amsterdam",
  "chronology_status": "CURRENT"
}
-->