# Testing Checklist — Mods and Compatibility

**Last updated:** 4 November 2026  
**Target:** Minecraft 1.21.1 / NeoForge 21.1.265 / Java 21  
**Mod download source:** CurseForge only

This is the living queue of mod features and compatibility checks that still need testing for Create IronWoven. It is separate from the installed-mod inventory and does not approve a mod for the production pack or a public release.

## Recommended work order — 4 November 2026

1. Finish the YUNG's Better End Island 2A test in the intentionally selected disposable `world_lootr_test`; first verify its End-generation state and the IronWoven compatibility datapacks.
2. Complete the remaining Botany Pots, Construction Sticks and Lootr multiplayer feature checks.
3. Investigate the outstanding Struts dedicated-server error, PowerGrid optional native backend, and unattributed chunk/world-load messages.
4. Test BetterEnd: New Dawn, Bigger Better End Cities and Ender Villages separately, after 2A is documented.
5. Research Create Big Cannons and the full colony ecosystem as separate candidate groups; do not install either until the dependency and compatibility reviews are complete.
6. Complete the remaining pack validation and clean-install checks before any public beta package.

This is an order of work, not permission to install or approve additional mods. Keep production worlds unchanged.


## Status meanings

- **Gameplay test pending** — the mod loads, but its actual feature has not been checked.
- **Partial pass** — the specific test described as passed is confirmed; other behavior remains untested.
- **Retest needed** — a known fix must be checked in a correctly prepared disposable world.
- **Research gate** — verify the exact CurseForge NeoForge file and dependency chain before installing anything.
- **On hold** — do not start testing until the project owner resumes it.


## Installed baseline: startup passed, feature testing still required

The 4 November dedicated-server test reached `Done`, loaded the test world, accepted a client login, and shut down cleanly with the recorded server mod set discovered/loaded. This is a **pack-level startup/load pass** for that server configuration. It does not mean every installed mod has passed its own feature tests.

- [ ] Work through the installed baseline mod list in `MODS.md` and validate each mod's core feature(s) that are relevant to this pack.
- [ ] Check representative recipes, blocks/items, machines, structures, entities, progression, and integrations where the mod provides them.
- [ ] Check key cross-mod interactions, especially Create/Create Aeronautics integrations and world-generation/structure mods, in disposable test worlds.
- [ ] Run a matching client startup test and review the client log; the dedicated-server log does not validate client-only graphics mods such as Sodium, Iris, or Sodium Extra.
- [ ] Record individual results as **passed**, **partial**, **failed**, or **not yet tested**. Do not infer a feature pass from the server reaching `Done`.

**Known startup exceptions that remain open:** Struts 1.3.1 attempts to load client-only `RenderSystem` on the dedicated server; Create: Power Grid 0.6.2 cannot load its optional `powergridNative7` accelerated solver in the tested Windows environment. Neither prevented the 4 November server startup, but both require follow-up.

## Active tests

### 1. Botany Pots — 21.1.44

**Status: Gameplay test pending; feature checks are expected to be possible.** Botany Pots 21.1.44, Bookshelf 21.1.81 and Prickle 21.1.11 loaded in the 4 November test group. Botany Pots reported one plugin loaded, and the server parsed 14,444 recipes without recipe-parsing failures. This confirms the mod and its dependencies load, but not in-game planting, growth, harvesting or the optional Herbs & Harvest integration.

- [ ] Place Botany Pots and test planting with supported vanilla seeds.
- [ ] Test growth and harvesting, and verify the expected drops.
- [ ] Check supported Herbs & Harvest crops and recipes in JEI.
- [ ] The 47 Herbs & Harvest Botany Pots integration recipes remain hidden by temporary `neoforge:false` overrides. Even with Botany Pots installed, those conditions still suppress the recipes.
- [ ] In a disposable test copy only, replace those suppressions with a conditional `neoforge:mod_loaded` check for `botanypots`, reload recipes, and verify the recipes appear in JEI.
- [ ] Test representative Herbs & Harvest crops through planting, growth and harvesting, and verify expected drops.
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

### 9. End-generation candidates — Batch 2

**2A status: Partial smoke-test pass — gameplay checks still pending.** The 4 November 2026 logs confirm that both JARs were installed in the separate test server, discovered, and listed as loaded mods. The server reached Done, accepted the local player, and shut down cleanly with all dimensions saved. No YUNG-specific dependency or startup failure was found.

**2A — YUNG's Better End Island 3.1.2**
- Main file: `YungsBetterEndIsland-1.21.1-NeoForge-3.1.2.jar` — [CurseForge file 6300968](https://www.curseforge.com/minecraft/mc-mods/yungs-better-end-island-neoforge/files/6300968).
- Required library: `YungsApi-1.21.1-NeoForge-5.1.9.jar` — [CurseForge file 8894736](https://www.curseforge.com/minecraft/mc-mods/yungs-api-neoforge/files/8894736).
- [x] Both JARs discovered and loaded by the separate test server.
- [x] YUNG's API dependency resolved; no YUNG-specific startup failure found.
- [x] Dedicated server reached Done, local client joined, and all dimensions saved on shutdown.
- [x] Load the user's intentionally selected disposable `world_lootr_test` world. The user chose it because its End had not yet been generated; there is no need to create or rename a world solely because the level name differs from the original plan.
- [ ] Confirm the End had not been generated before YUNG's Better End Island was installed; then enter the End and inspect the new generation.
- [ ] Check `/datapack list enabled` in `world_lootr_test`. The uploaded logs did not evidently show the custom IronWoven compatibility packs, and known loot-table, placard recipe and Catwalk selector errors returned. If packs are missing, copy only those folders into `world_lootr_test/datapacks`, preserving other datapacks.
- [ ] Restart and verify the IronWoven compatibility packs are enabled before continuing.
- [ ] Inspect the redesigned central island, spawn platform, portal, pillars and gateways.
- [ ] Approach the central bell tower and check dragon summon behavior.
- [ ] Complete the dragon fight and test respawning with the four crystals in the tower's intended positions.
- [ ] Save, restart and rejoin to verify the arena persists.

The logs show 459 ERROR entries and 160 WARN entries. The 453 loot-table errors, one Create Deco placard recipe error and three Sable/Copycats selector errors are known IronWoven compatibility-datapack issues; separate Struts and PowerGrid errors also remain. They are not attributed to YUNG's mods. The world-name choice was intentional, not a test failure. Do not run `/end_island reset` on an existing or production world.

**2B — BetterEnd: New Dawn 21.0.39**
- Main file: `BetterEnd-21.0.39.jar` — [CurseForge file 9306604](https://www.curseforge.com/minecraft/mc-mods/betterend-neoforge/files/9306604).
- Required libraries: BCLib 21.0.28, WorldWeaver 21.0.30, WunderLib 21.0.11. See the relevant [CurseForge files](https://www.curseforge.com/minecraft/mc-mods/bclib-neoforge/files), [WorldWeaver files](https://www.curseforge.com/minecraft/mc-mods/worldweaver-neoforge/files), and [WunderLib file 9172421](https://www.curseforge.com/minecraft/mc-mods/wunderlib-neoforge/files/9172421).
- [ ] Test alone in a fresh disposable world after 2A has been documented.
- [ ] Check biomes, terrain, caves, structures, resources, mobs, recipes and progression.
- [ ] Validate compatibility with BYG, Regions Unexplored, TerraBlender, Lithostitched and IronWoven datapacks.

**WorldWeaver optional patch warning:** [WorldWeaver Registry Synchronization 1.0.0, file 9389941](https://www.curseforge.com/minecraft/mc-mods/worldweaver-registry-synchronization/files/9389941) targets WorldWeaver 21.0.30, Minecraft 1.21.1, NeoForge 21.1.265 and Java 21. It is not a required BetterEnd dependency and is not approved. Only evaluate it in a separate test if its specific registration race reproduces.

**Bigger Better End Cities 1.0.0**
- Exact file: `biggerbetterendcities-1.21.1-1.0.0.jar` — [CurseForge file 6461536](https://www.curseforge.com/minecraft/mc-mods/bigger-better-end-cities/files/6461536).
- [ ] Test alone in a fresh disposable End world, checking city size, branching, tower height, bridges, ships, shulkers, loot and chunk-boundary generation.

**Ender Villages 2.0**
- Exact file: `endervillages-2.0-1.21.1.jar` — [CurseForge file 6741737](https://www.curseforge.com/minecraft/mc-mods/ender-villages/files/6741737).
- [ ] Test alone in a fresh disposable End world, checking village generation, structure overlap, villagers, professions, trades, breeding, End Cats and persistence.
- Note: this file is older and its license is All Rights Reserved; do not mirror or redistribute its JAR.

Do not combine the central-island overhauls in the first test. Keep production world and BYG / Regions Unexplored generation unchanged.

### 10. Colony ecosystem candidates

**Status: Research gate — no installation or gameplay test has been approved.**

| Candidate | Role | Next step |
|---|---|---|
| MineColonies | Main colony system | Select the exact stable 1.21.1 NeoForge release and build its complete dependency chain |
| CreateColonies | Create/MineColonies integration | Verify exact project/release and Create 6.0.10 compatibility |
| Create: MineColonies Link | Separate Create integration | Establish distinct functionality and whether it can coexist with CreateColonies |
| Structurize | MineColonies support component | Match the version required by the selected MineColonies release |
| Domum Ornamentum | MineColonies support component | Match the version required by the selected MineColonies release |
| BlockUI | MineColonies support component | Match the version required by the selected MineColonies release |
| Multi-Piston | Possible supporting dependency | Verify whether the selected MineColonies release requires it |
| TownTalk | Optional colony integration | Verify exact project, loader support and distinct functionality |
| Dynamic Trees | Separate world/ecology candidate | Verify NeoForge 1.21.1 and compatibility with BYG 2.6.3 / Regions Unexplored 0.6.3 |
| Colony building styles and schematics | Content research, not automatically mods | Check file format, dependencies, MineColonies/Structurize compatibility and permissions |

- [ ] Select and verify the exact MineColonies NeoForge 1.21.1 release first.
- [ ] Build the dependency list from that exact CurseForge release; do not guess versions.
- [ ] Verify Create 6.0.10 compatibility and whether CreateColonies and Create: MineColonies Link are separate integrations that can safely coexist.
- [ ] Only after the full stack is reviewed and approved, test it on a disposable dedicated server and disposable world.
- [ ] Test colony creation, starter placement, buildings/schematics, worker behavior, requests, raids/defense, Create integration, multiplayer, save/restart and performance.
- [ ] Keep Dynamic Trees as a separate optional test; do not change production world generation.

### 11. Create Big Cannons 5.11.7

**Status: Research candidate — not installed for IronWoven testing and not approved.** Exact 1.21.1 NeoForge release and required library verified on CurseForge.

- Main file: `createbigcannons-5.11.7+mc.1.21.1.jar` — [CurseForge file 8303106](https://www.curseforge.com/minecraft/mc-mods/create-big-cannons/files/8303106).
- Required library: Ritchie's Projectile Library 2.1.2, `ritchiesprojectilelib-2.1.2-mc.1.21.1-neoforge.jar` — [CurseForge file 7587771](https://www.curseforge.com/minecraft/mc-mods/ritchies-projectile-library/files/7587771).
- Required Create dependency: Create 6.0.7+; the current recorded pack has Create 6.0.10, satisfying the published minimum.
- CBC 5.11.7 changelog lists Sable 2.0.0 support and a shell-impact compatibility fix. Validate that against the current pack's Sable build.
- [ ] Recheck exact CurseForge files/dependencies before installation.
- [ ] Check recipes and JEI visibility; build cannon and autocannon multiblocks.
- [ ] Test breeches, materials, kinetic loading/aiming, ammunition, fuzes, firing and projectile damage.
- [ ] Test Sable shell impacts, multiplayer synchronization, server performance and save/restart.
- [ ] Test Create Aeronautics vehicle/ship integration separately; do not assume support.
- [ ] Bronze and steel cannon materials may need an ingot-provider mod. CBC upstream recommends IngotCraft, but it is not listed as a required dependency; research separately before adding.

Only test on a disposable dedicated server and world after explicit approval. Do not alter the production mod list or world.

## Performance test queue — separate tests only

**Current baseline already includes:** ModernFix 5.27.27 and FerriteCore 7.0.3 in the recorded server inventory; Sodium 0.8.13, Sodium Extra 0.9.5 and Iris 1.8.14-beta.1 in the client graphics profile. Do not add duplicate renderer or memory mods.

### Diagnostic first

**spark 1.10.124 — diagnostic tool, not an FPS boost**
- CurseForge 1.21.1 NeoForge file: [file 6225208](https://www.curseforge.com/minecraft/mc-mods/spark/files/6225208).
- [ ] Use the test server to capture a baseline profile under normal load and during a known laggy area/contraption.
- [ ] Record TPS/MSPT, CPU hotspots and memory/GC behavior before adding optimizers.

### Client rendering candidates

**ImmediatelyFast 1.6.15 — client**
- [CurseForge file 9165518](https://www.curseforge.com/minecraft/mc-mods/immediatelyfast/files/9165518).
- [ ] Test by itself in the matching test client with the existing Sodium/Iris profile.
- [ ] Compare FPS/frame pacing, GUI/HUD, particles and Create screens.

**Entity Culling 1.11.3 — client**
- [CurseForge 1.21.1 NeoForge file](https://www.curseforge.com/minecraft/mc-mods/entityculling/files/all).
- [ ] Test by itself after ImmediatelyFast is recorded.
- [ ] Check Create pulleys, moving contraptions, extended block-entity render bounds and animated entities.
- [ ] Whitelist any renderers that are incorrectly hidden; do not accept missing visual parts as a performance pass.

### Server/game-logic candidates

**Lithium 0.15.4 — NeoForge 1.21.1**
- [CurseForge file 8330365](https://www.curseforge.com/minecraft/mc-mods/lithium/files/8330365).
- [ ] Back up/copy a disposable world and test Lithium alone.
- [ ] Test Create contraptions, kinetic networks, trains, Aeronautics, block updates, entities, chunk save/load and restart.
- [ ] Review full server/client logs and compare spark profiles.

**FastSuite 6.0.7 — NeoForge 1.21.1**
- [CurseForge file 7527945](https://www.curseforge.com/minecraft/mc-mods/fastsuite/files/7527945).
- [ ] Test recipe lookup in JEI and with representative Create machines.
- [ ] Verify custom IronWoven recipes/datapacks and recipe-conflict behavior.

**FastFurnace 9.0.1 — NeoForge 1.21.1**
- [CurseForge file 6751551](https://www.curseforge.com/minecraft/mc-mods/fastfurnace/files/6751551).
- [ ] Test vanilla furnace, blast furnace, smoker and representative modded furnace recipes.
- [ ] Confirm no smelting behavior/recipe regressions; this optimizes recipe lookup, not smelting speed.

**Chunk-Pregenerator 4.5.4 — optional server/world utility**
- [CurseForge NeoForge files](https://www.curseforge.com/minecraft/mc-mods/chunkpregenerator/files/all).
- [ ] Consider only after deciding the test world's intended border/radius.
- [ ] Trial a small area in a disposable world; monitor disk growth, CPU, memory and generation errors.
- [ ] Do not run uncontrolled pre-generation on the production world.

Do not install C2ME or ServerCore in this first wave. Their chunk-threading/behavior changes require separate compatibility research for this Create/Aeronautics and BYG/Regions Unexplored stack. Do not add Embeddium or another renderer alongside Sodium without a specific compatibility reason.

## Quality-of-life candidate queue — compare with installed mods

**Already present:** JEI 19.64.0.455, Jade 15.10.6, AppleSkin 3.0.9, Mouse Tweaks 2.26.1, FTB Chunks/Teams and Sophisticated Backpacks 3.26.19. FTB Chunks already supplies claims/team-map functionality. AeroPortals 1.3.6 is also installed and must be compared with Waystones before selecting a travel system.

- [ ] **Just Enough Resources (JER) 1.6.0.57 — client-side JEI addon** — [CurseForge file 9311693](https://www.curseforge.com/minecraft/mc-mods/just-enough-resources-jer/files/9311693). Adds mob drops, dungeon loot, villager trades, plant drops and ore/worldgen information to JEI; it complements, not replaces, JEI. Check BYG/RU and custom loot-table coverage.
- [ ] **Shulker Box Tooltip 5.1.9+1.21.1 — client & server supported** — [CurseForge file 7768285](https://www.curseforge.com/minecraft/mc-mods/shulkerboxtooltip/files/7768285). Preview shulker/container contents. Distinct from Sophisticated Backpacks; test shulker previews, Sophisticated storage and generic container support.
- [ ] **Enchantment Descriptions 21.1.11 — NeoForge 1.21.1** — [CurseForge file 8693034](https://www.curseforge.com/minecraft/mc-mods/enchantment-descriptions/files/8693034). No current equivalent found. Requires Bookshelf and Prickle; both appeared in the separate Botany Pots test group, but neither should be assumed present in the main profile. Confirm exact main-profile dependency files first.
- [ ] **Nature's Compass 3.4.0 — client & server** — [CurseForge file 7892954](https://www.curseforge.com/minecraft/mc-mods/natures-compass/files/7892954). Search vanilla, BYG and Regions Unexplored biomes. No equivalent compass is listed; test biome registration/visibility and XP/durability settings.
- [ ] **Explorer's Compass 3.4.0 — client & server** — [CurseForge file 7892943](https://www.curseforge.com/minecraft/mc-mods/explorers-compass/files/7892943). Search registered structures. FTB Chunks is not a structure locator. Test End and modded structures, locator tags, search cost and exploration balance.
- [ ] **Waystones 21.1.46 — client & server** — [CurseForge 1.21.1 NeoForge files](https://www.curseforge.com/minecraft/mc-mods/waystones/files/all). Requires compatible Balm. AeroPortals 1.3.6 is already installed; first document its teleport behavior, then compare both systems in a disposable world. Check Balm's exact version and multiplayer costs, cooldowns, access rules and progression before deciding whether Waystones adds enough.

**Test order:** JER; Shulker Box Tooltip; Enchantment Descriptions after dependency confirmation; Nature's Compass; Explorer's Compass; Waystones only after the AeroPortals/Balm review. Keep tests isolated and record client/server placement and logs. These are candidates, not approved additions.

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


## Performance / LOD / Tectonic tests — separated by installation side (4 November 2026)

**Rules:** Use one candidate at a time. Keep client-only files out of the dedicated server. For both-side candidates use the same compatible release on both client and server. Startup/login smoke tests are not gameplay approval.

### 1. Dedicated server first

- [ ] Add spark 1.10.124 to the disposable dedicated server only for the initial server baseline. Record TPS/MSPT and CPU during idle, exploration, a busy Create factory, trains and Aeronautics activity. Remove it after capturing results unless continued profiling is needed.
- [ ] Later, test Chunk-Pregenerator 4.5.4 as a dedicated-server utility only in a disposable world, after selecting a defined generation radius. Monitor CPU, memory, disk use and world-generation correctness.

### 2. Client-only tests — player's CurseForge profile only

- [ ] Test ImmediatelyFast 1.6.15 alone. Check GUI, HUD, particles, entities and block entities.
- [ ] Reset to baseline; test Flerovium 1.1.2 stable alone. Sodium is already present. Check dropped items, Create depots, belts, particles, mobs and Aeronautics visuals.
- [ ] Reset; test Entity Culling 1.10.4 alone. Check moving Create block entities, pulleys, Sable sublevels, trains and visual culling errors; whitelist only as needed.
- [ ] Reset; test Distant Horizons 3.3.3 alone with shaders disabled. Then test only an explicitly DH-compatible Iris shader. Record terrain LOD quality, performance, and the distance at which Aeronautics sublevels disappear.
- [ ] Do not add Voxy/Roxy under the current CurseForge-only rule. Do not add SSRD unless a CurseForge download is verified.

### 3. Both-side tests — matching version on client and dedicated server

- [ ] Test Lithium 0.15.4 on both sides in a disposable environment with a full world backup. Verify Create contraptions, Sable physics, trains, inventories, redstone, farms, mob AI and chunk ticking.
- [ ] Reset; test FastSuite 6.0.7 on both sides. Verify JEI, every Create/custom recipe, datapack override and modded workstation.
- [ ] Reset; test More Culling **1.0.9** (correct 1.21.1 NeoForge version) on both sides. Check leaves, glass, connected textures, Create blocks and modded decorative blocks.
- [ ] FastFurnace 9.0.1 is lower priority; if tested, use its matching 1.21.1 NeoForge build on both sides and verify furnace, blast furnace and smoker recipes.

### 4. Both-side world-generation test

- [ ] Test Tectonic v3.0.28 ~ NeoForge 21.1 on client and server in a new disposable world. Use a copy of current worldgen JSON only. Check BYG/RU biome distribution, biome sizes, terrain, structures, rivers/oceans and End generation.
- [ ] Never use the production world for this test. Do not alter production BYG 2.6.3, RU 0.6.3 or current JSON before explicit approval.

Nothing in this checklist authorizes installation into the production profile or production server.

### 11. End structure alternatives — selected for separate tests

**Status: Selected for test planning; exact dependency gate remains open for Better End Cities Better End. No mods installed or approved.** Use three separate disposable test worlds/iterations; never use the production world.

**Candidate A — Better End Cities Better End**
- File: `BetterEndCities-Raijin-structure-1.21.1.jar` — [CurseForge file 8105176](https://www.curseforge.com/minecraft/mc-mods/better-end-cities-better-end/files/8105176).
- Minecraft 1.21.1, NeoForge; server-side structure mod.
- Adds more intricate End Cities and extra loot using BetterEnd blocks.
- CurseForge project relations list three required BetterEnd-family dependencies (BetterEnd, BetterEnd Forge, BetterEnd: New Dawn). The project-level list is not enough to establish the exact compatible files for this specific NeoForge file. Resolve exact 1.21.1 NeoForge dependencies before any installation. Do not assume the BetterEnd: New Dawn 21.0.39 stack alone satisfies all requirements.
- [ ] Confirm exact dependency declarations for file 8105176 and resolve any conflicting/duplicate BetterEnd implementations.
- [ ] Test the required BetterEnd dependency stack by itself in a fresh disposable world; check startup, client login, End entry and logs.
- [ ] In a second fresh disposable world, add Better End Cities Better End with only its exact required dependency set.
- [ ] Inspect End City complexity, loot-room/chest count, structure integrity, spawner/entity behavior, placement frequency, overlaps and chunk boundaries.
- [ ] Save, restart, revisit generated areas and compare client/server logs.

**Candidate B — MES / Moog's End Structures**
- Exact 1.21.1 NeoForge file: `mes-1.3.5-1.21.jar` — [CurseForge file 5872117](https://www.curseforge.com/minecraft/mc-mods/moogs-end-structures/files/5872117).
- CurseForge lists client & server; project description says it can be installed server-side only.
- Earlier file 6918257 / `mes-1.4.6-1.21.jar` reference was wrong for this target; use file 5872117 for the 1.21.1 NeoForge candidate.
- [ ] Test MES alone in a separate fresh disposable End world.
- [ ] Locate and inspect each new End structure; record structure types, frequency, placement and overlap with vanilla End Cities.
- [ ] Inspect ship structures, loot tables, hostile entities/challenges and traversal.
- [ ] Check chunk-boundary generation, save/restart persistence and client/server logs.

**Combined test — only after both isolated candidates pass**
- [ ] Decide whether a combined test adds value; do not combine them automatically.
- [ ] If approved, create another fresh disposable world with only the individually passing candidates and their required dependencies.
- [ ] Check structure overlap, generation frequency, loot balance, startup and chunk errors.

**Safeguards:** CurseForge only. Keep production world and BYG 2.6.3 / Regions Unexplored 0.6.3 unchanged. Do not modify the installed inventory or production server. Test selection is not production approval.
