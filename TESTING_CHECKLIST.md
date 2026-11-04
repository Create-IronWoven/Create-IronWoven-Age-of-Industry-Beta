# Testing Checklist — Mods and Compatibility

**Last updated:** 4 November 2026  
**Target:** Minecraft 1.21.1 / NeoForge 21.1.265 / Java 21  
**Mod download source:** CurseForge only

This is the living queue of mod features and compatibility checks that still need testing for Create IronWoven. It is separate from the installed-mod inventory and does not approve a mod for the production pack or a public release.

## Status meanings

- **Gameplay test pending** — the mod loads, but its actual feature has not been checked.
- **Partial pass** — the specific test described as passed is confirmed; other behavior remains untested.
- **Retest needed** — a known fix must be checked in a correctly prepared disposable world.
- **Research gate** — verify the exact CurseForge NeoForge file and dependency chain before installing anything.
- **On hold** — do not start testing until the project owner resumes it.

## Active tests

### 1. Botany Pots — 21.1.44

**Status: Gameplay test pending.** Server loading passed in the 4 November test group. Bookshelf 21.1.81 and Prickle 21.1.11 were also discovered and loaded as its supporting libraries.

- [ ] Place Botany Pots and test planting with supported vanilla seeds.
- [ ] Test growth and harvesting, and verify the expected drops.
- [ ] Check supported Herbs & Harvest crops and recipes in JEI.
- [ ] Review the 47 Herbs & Harvest Botany Pots integration recipes that are currently suppressed by the IronWoven compatibility datapack. They have **not** been restored; do not enable them until a safe conditional fix is ready.
- [ ] Confirm there are no new recipe, registry, or server errors during the gameplay test.

**Do not call this feature-tested just because the server starts.**

### 2. Construction Sticks — 1.5.0

**Status: Gameplay test pending.** Server loading passed in the 4 November test group.

- [ ] Test placement with vanilla blocks.
- [ ] Test placement with representative Create, Copycats, and other modded blocks.
- [ ] Test placement inside an FTB Chunks claimed area and across a claim boundary.
- [ ] Check block orientation, placement limits, item consumption, and that protected or restricted blocks are not changed unexpectedly.

### 3. Lootr — 1.11.38.127

**Status: Partial pass.** Lootr loaded on the test server, the fresh test world started, the client joined, and shutdown saved cleanly. The player has confirmed opening a chest and finding loot inside.

- [x] Load Lootr on the separate test server and matching client.
- [x] Create and load the disposable `world_lootr_test` world.
- [x] Open a chest in-game and confirm that it contains loot (user-confirmed).
- [ ] Have a second player open the **same Lootr chest** and verify that they receive their own independent personal loot.
- [ ] Where practical, repeat with a newly generated modded-structure chest to check compatibility beyond a vanilla chest.

Keep Lootr in the test installation until the multiplayer personal-loot check is complete. Do not test it in the production world.

### 4. Bookshelf 21.1.81 and Prickle 21.1.11

**Status: Dependency load check passed; no separate gameplay task.**

- [x] Both libraries were discovered and loaded with Botany Pots in the 4 November test group.
- [ ] Keep both matching dependencies present on the client and server during Botany Pots feature testing; confirm there are no missing-dependency errors.

These are support libraries for the Botany Pots test, not separate gameplay additions.

## Fresh-world compatibility retest

### 5. IronWoven compatibility datapacks

**Status: Retest needed.** The new `world_lootr_test` world did not load the custom IronWoven world-scoped compatibility datapacks that were active in the earlier fixed test world. The related parsing errors reappeared in that fresh world. This is a test-world setup discrepancy; it is not evidence that Lootr caused them.

- [ ] In the disposable test world only, copy the existing IronWoven compatibility datapack folders from the previously fixed test world into `world_lootr_test/datapacks`. Keep the new world's own datapacks; do not replace the whole folder.
- [ ] Restart and verify that the IronWoven packs are listed as loaded.
- [ ] Confirm the earlier Design n' Decor, Steam 'n' Rails, and Create Kinetic missing-item loot-table errors no longer appear.
- [ ] Confirm the Create Deco placard recipe parsing error and Sable / Copycats Catwalk selector errors no longer appear.
- [ ] Keep the world disposable and leave the production world and its BYG / Regions Unexplored setup unchanged.

Mods affected by this retest include Design n' Decor, Steam 'n' Rails, Create Kinetic, Create Deco, Sable, and Copycats. The fixes passed earlier smoke tests in the correctly prepared test world; this retest checks that the required datapacks are also present in a newly created world.

## Outstanding dedicated-server and runtime checks

### 6. Struts — 1.3.1

**Status: Compatibility investigation required.** The dedicated server still reports an attempt to load the client-only Minecraft class `com.mojang.blaze3d.systems.RenderSystem`.

- [ ] Isolate the Struts client-only mixin/class-loading issue.
- [ ] After a proposed correction, test dedicated-server startup and client login.
- [ ] Confirm client-side Struts behavior still works and the server no longer attempts to load the client-only class.

### 7. PowerGrid — 0.6.2

**Status: Optional native solver unavailable in the tested Windows server environment.** The optional `powergridNative7` library did not load; the server continued with the fallback solver.

- [ ] Confirm the core PowerGrid features work using the fallback solver.
- [ ] Record OS, CPU architecture, and native-library loading details for diagnosis.
- [ ] Verify whether the native solver is expected to be available for this environment. Do not treat the optional native failure as a startup failure.

### 8. Unattributed world/chunk-generation messages

**Status: Recheck after the datapack setup is corrected; source not established.**

The fresh-world debug log also recorded skipped Apotheosis data attachments, invalid `minecraft:air` item stacks, one invalid block-attached entity position, and failed Create block-entity loads for tracks, copper doors, and blaze burners.

- [ ] Review these messages in a fresh log after the compatibility datapacks are loaded.
- [ ] Check whether they reproduce in newly generated chunks.
- [ ] Identify a responsible mod only when a reproducible error or stack trace supports the attribution.

Do not assign these messages to Lootr based on the current evidence.

## Candidate mods — research before any install/test

These entries are not in the active test installation. First confirm an exact Minecraft 1.21.1 NeoForge file and all required dependencies on CurseForge. Do not install them until the compatibility review is complete and the project owner approves the test.

### 9. End-generation candidates

**YUNG's Better End Island — 3.1.2; YUNG's API required**
- [ ] Confirm exact CurseForge NeoForge 1.21.1 files and dependency version.
- [ ] Test alone in a disposable End world.
- [ ] Check central-island generation, structures, dimension entry/exit, and server/client errors.

**BetterEnd: New Dawn — 21.0.36; BCLib: New Dawn, WunderLib: New Dawn, and WorldWeaver: New Dawn required**
- [ ] Confirm the complete matching CurseForge dependency set.
- [ ] Test alone in a separate disposable End world.
- [ ] Check central-island generation, biomes, structures, dimension entry/exit, and compatibility with the existing BYG / Regions Unexplored setup.

Do not combine these two End generators until each has been tested separately and their combined behavior has been reviewed.

**Bigger Better End Cities**
- [ ] Reconfirm an exact CurseForge Minecraft 1.21.1 NeoForge artifact before considering a test. Do not use a Fabric file.

**Ender Villages**
- [ ] Confirm whether an exact CurseForge Minecraft 1.21.1 NeoForge file exists. It remains on hold until verified.

### 10. Colony ecosystem candidates

**Status: Research gate — no installation or gameplay test has been approved.**

Candidates: MineColonies, CreateColonies, Create: MineColonies Link, Structurize, Domum Ornamentum, BlockUI, Multi-Piston, and TownTalk.

- [ ] Select and verify the exact MineColonies NeoForge 1.21.1 release first.
- [ ] Build its dependency list from the selected CurseForge release.
- [ ] Verify Create 6.0.10 compatibility and whether CreateColonies and Create: MineColonies Link are separate integrations that can safely coexist.
- [ ] Only after the full stack is reviewed and approved, test it on a disposable dedicated server and a disposable world.
- [ ] Test colony creation, building placement, worker behavior, save/restart, and Create integration.

**Dynamic Trees** is a separate optional world/ecology candidate:
- [ ] Verify NeoForge 1.21.1 support and compatibility with BYG 2.6.3 and Regions Unexplored 0.6.3 before considering a disposable-world test.
- [ ] Do not change existing world generation or the production world.

Additional colony building styles and schematics are content research, not automatically separate mods; check format, dependencies, compatibility, and permissions before adding them.

## On hold

### Terralith

**Status: On hold by project decision.** Do not install or test Terralith, change world-generation settings, or alter the production world unless the project owner explicitly resumes this investigation.

## Test and update rules

- Use the separate test installation and disposable worlds. Never use the production world for candidate testing.
- CurseForge is the only approved mod download source.
- A successful startup/login smoke test does not count as a gameplay-feature pass.
- A candidate or dependency listed here is not automatically approved for the modpack or release.
- When a new log, screenshot, or manual test result is reviewed, update this checklist: record the date, move only the proven checks to passed, add newly discovered tests, and remove completed items only when the evidence supports it.
- Keep this page aligned with the maintainer's latest test records. Publish only concise, player-safe summaries here; do not publish raw logs, private paths, IPs, tokens, or other personal/system details.
- Do not change the production mod list or world as part of updating this documentation.
