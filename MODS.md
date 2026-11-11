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

The 10 November active-profile archive audit found 102 JARs in each test-profile archive: 101 shared non-WITS JARs have identical hashes. WITS is a temporary testing utility and is excluded from the mod set. Railways `0.3.0-beta.2` and Supplementaries `4.0.2` also appear in both archives with matching hashes, but remain observations pending their own exact CurseForge/dependency review and maintainer update disposition. These profiles are not the selected clean v.0.1 release server. Waystones 21.1.46 appears in the 10 November working profile, but its prior core-Waystones package deferral remains unresolved. Base Sable 2.0.6 is a separate SubLevel physics library already present for Create/Aeronautics. The distinct Waystones: Sable 1.0.7 compatibility addon (CurseForge project 1524471, MIT, Client & Server) is absent and remains optional/deferred; declared requirements are Waystones 21.1.36+, Sable 2.0.3+, and Create 6.0.10+. Do not add it until core Waystones is explicitly retained and AeroPortals/travel overlap is resolved.



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
