# Mods Planned, On Hold, and Excluded

This page separates confirmed installed mods from ideas for future versions. **A mod listed as planned or on hold is not part of the current pack unless it also appears on [Mods in the Pack](MODS.md).**

The [Testing Checklist](TESTING_CHECKLIST.md) is the live list of gameplay checks, compatibility retests, and research still required. A test listed there does not mean the mod is approved for release.

## Requested candidates — compatibility review 3 November 2026

Target platform: Minecraft 1.21.1, NeoForge 21.1.265, Java 21.

These are requested candidates only. Botany Pots and Construction Sticks are now present in the 4 November dedicated-server test inventory. Their smoke-test loading is confirmed; full feature validation and final release inclusion remain pending. Bookshelf appeared twice in the submitted list and is recorded once.

| Mod | Review status | Notes |
|---|---|---|
| Botany Pots | Present in 4 Nov server test; feature review pending | Server loaded Botany Pots 21.1.44 with Bookshelf 21.1.81 and Prickle 21.1.11; one Botany Pots plugin loaded and 14,444 recipes parsed without parser failures. Basic features and Herbs & Harvest integration are expected to be testable. The 47 optional integration recipes remain suppressed by unconditional `neoforge:false` overrides; enable them only through a conditional `botanypots` test in a disposable copy, then verify in JEI and in-game. |
| Create Deco 2.1.3 | Already in current test inventory | No addition needed; current server inventory already records 2.1.3. |
| Construction Sticks | Present in 4 Nov server test; feature review pending | Server loaded 1.5.0. Placement with modded blocks has not yet been tested. |
| Lootr | Present in 4 Nov test; partial manual check | Lootr 1.11.38.127 loaded and the user confirmed a chest opened with loot. Two-player independent personal loot is still unverified; see [Testing Checklist](TESTING_CHECKLIST.md). |
| Create Big Cannons | Research candidate; not installed or approved | `createbigcannons-5.11.7+mc.1.21.1.jar` (CurseForge 8303106); requires Create 6.0.7+ and Ritchie's Projectile Library 2.1.2 (CurseForge 7587771). Current Create 6.0.10 meets the published minimum; test Sable 2.0.x compatibility and gameplay in a disposable server/world. |
| YUNG's Better End Island | 2A partial smoke-test pass; End gameplay pending | Both exact JARs discovered and loaded. Server reached Done, client joined, clean shutdown. The user intentionally selected `world_lootr_test` because its End had not yet been generated; there was no world-selection mistake. Verify the End-generation state and custom datapack setup before End exploration. See [Testing Checklist](TESTING_CHECKLIST.md). |
| BetterEnd: New Dawn | Exact CurseForge file verified; gameplay test pending | `BetterEnd-21.0.39.jar` (file 9306604); requires BCLib 21.0.28, WorldWeaver 21.0.30, WunderLib 21.0.11. Test separately in a fresh disposable world; review BYG / Regions Unexplored / TerraBlender / Lithostitched compatibility. |
| Bigger Better End Cities | Exact CurseForge NeoForge file verified; gameplay test pending | `biggerbetterendcities-1.21.1-1.0.0.jar` (file 6461536); valid server-side NeoForge 1.21.1 release. Test End City generation alone. |
| Ender Villages | Exact CurseForge NeoForge file verified; gameplay test pending | `endervillages-2.0-1.21.1.jar` (file 6741737); NeoForge 1.21.1, uploaded 7 July 2025. Project license All Rights Reserved; verify client/server placement and test village, villager, trade and persistence behavior. |
| Bookshelf | Conditional dependency; load check passed | Required by Botany Pots on 1.21.1; 21.1.81 loaded with the test group. |
| Prickle | Conditional dependency; load check passed | Required by Botany Pots on 1.21.1; 21.1.11 loaded with the test group. |

### Important test safeguards

- Keep the production world and its current BYG 2.6.3 / Regions Unexplored 0.6.3 setup unchanged.
- Test End world-generation candidates in separate disposable worlds. BetterEnd: New Dawn and YUNG's Better End Island both change the central End island; combined compatibility has not been established.
- Botany Pots and its dependencies load in the test group; basic features and the optional Herbs & Harvest integration are ready for gameplay validation. The 47 Herbs & Harvest recipes remain suppressed by `neoforge:false`; they need a conditional `botanypots` test in a disposable copy before being described as restored.
- Batch 7 has not started. Candidate mods are not approved additions.

## Confirmed current client-only additions

These are recorded as installed in the client profile, not as dedicated-server mods:

| Mod | Version recorded | Status |
|---|---|---|
| Sodium | 0.8.13 | Client only |
| Iris | 1.8.14-beta.1 | Client only |
| Sodium Extra | 0.9.5 NeoForge | Client only |

## On hold / under investigation

| Mod | Status | Notes |
|---|---|---|
| Terralith | On hold — not installed | A possible world-generation option. Compatibility investigation was paused. The current BYG 2.6.3 and Regions Unexplored 0.6.3 setup and existing worlds must remain unchanged while this is on hold. |

## Explicitly excluded from the current plan

These mods remain specifically recorded as not wanted for this project:

- Carry On
- Easy Villagers
- Immersive Paintings
- Just Create SMP Pops

## How players can suggest a mod

Use the [feature suggestion form](https://github.com/alexth110987/Create-IronWoven-Beta/issues/new?template=feature_suggestion.yml). Please include the exact mod name, its official project page, supported Minecraft / NeoForge versions, and why it fits Create IronWoven.

Suggestions are reviewed, not automatically accepted. The pack's existing compatibility and world-preservation decisions take priority over adding more mods.

## Requested colony ecosystem candidates — 4 November 2026

Target platform: Minecraft 1.21.1, NeoForge 21.1.265, Java 21.

These are requested candidates and content ideas for compatibility research only. **None have been installed or approved.** Exact 1.21.1 NeoForge files, versions, dependencies, and compatibility with the current pack still need verification.

| Candidate | Review status | Notes |
|---|---|---|
| CreateColonies | Candidate — review pending | Verify exact project, 1.21.1 NeoForge file, MineColonies dependency, and Create 6.0.10 compatibility. |
| MineColonies | Candidate — review pending | Proposed main colony system. Verify current NeoForge release and complete dependency chain. |
| Create: MineColonies Link | Candidate — review pending | Verify exact project and compatibility with the selected MineColonies and Create versions. |
| Structurize | Supporting dependency candidate | Match the version required by the selected MineColonies release. |
| Domum Ornamentum | Supporting dependency candidate | Match the version required by the selected MineColonies release. |
| BlockUI | Supporting dependency candidate | Match the version required by the selected MineColonies release. |
| Multi-Piston | Supporting dependency candidate | Verify whether required by the selected MineColonies release and match its declared version. |
| TownTalk | Optional integration candidate | Verify exact project, loader support, and distinct functionality. |
| Dynamic Trees | Optional world/ecology candidate | Verify NeoForge 1.21.1 support and compatibility with existing BYG / Regions Unexplored world generation. |
| Additional colony building styles and schematics | Content research item — not necessarily a mod | Check format, dependencies, MineColonies/Structurize compatibility, and permissions. |

### Colony ecosystem test safeguards

- Select the exact MineColonies release first and use its declared dependency versions.
- Verify whether CreateColonies and Create: MineColonies Link are separate compatible integrations before considering both.
- Keep Dynamic Trees optional; do not change the current BYG 2.6.3 / Regions Unexplored 0.6.3 setup.
- Test the complete selected stack on a disposable dedicated server and copied world, only after approval.
- No main-world changes or installations are authorized by this candidate list.
- Batch 7 has not started. All entries remain under review, not approved additions.


## Batch 2 End-content review — 4 November 2026

Exact CurseForge Minecraft 1.21.1 NeoForge files have now been verified for all four End candidates. The detailed feature checklist and separate test order are in [TESTING_CHECKLIST.md](TESTING_CHECKLIST.md).

The earlier “Bigger Better End Cities is Fabric-only” and “Ender Villages has no 1.21.1 NeoForge file” statements are superseded. BetterEnd: New Dawn 21.0.39 is newer than the previous 21.0.34 / 21.0.36 notes.

A separate optional WorldWeaver Registry Synchronization 1.0.0 patch exists for WorldWeaver 21.0.30 / NeoForge 21.1.265 / Java 21. This is not a required dependency and is not approved for install; evaluate only if the exact race reproduces.

All four remain candidates, not installed or approved additions. Use one candidate group per fresh disposable End world, then test combinations only after separate tests pass. Preserve production world and existing BYG / Regions Unexplored generation.


## Batch 2A runtime update — 4 November 2026

The first dedicated-server run confirms YUNG's API 5.1.9 and YUNG's Better End Island 3.1.2 loaded and the server completed startup, client login and clean shutdown. However, the user intentionally selected `world_lootr_test` because its End had not yet been generated. The central End island and dragon features remain untested. The world-scoped IronWoven compatibility datapacks were not evidently loaded and known errors returned. This is a partial smoke-test pass only, not production approval. Follow the next steps in [TESTING_CHECKLIST.md](TESTING_CHECKLIST.md).


## Create Big Cannons — additional candidate — 4 November 2026

Create Big Cannons 5.11.7 has an exact Minecraft 1.21.1 NeoForge release. Required components are Create (already recorded at 6.0.10) and Ritchie's Projectile Library 2.1.2. The current release changelog includes Sable 2.0.0 support and a shell-impact compatibility fix; validate against the pack's current Sable version.

- Main file: [Create Big Cannons 5.11.7 — CurseForge file 8303106](https://www.curseforge.com/minecraft/mc-mods/create-big-cannons/files/8303106).
- Required library: [Ritchie's Projectile Library 2.1.2 — CurseForge file 7587771](https://www.curseforge.com/minecraft/mc-mods/ritchies-projectile-library/files/7587771).
- [ ] Verify recipe/JEI visibility and material progression.
- [ ] Test cannon/autocannon multiblock assembly, breeches, kinetic loading/aiming, ammunition, fuzes, firing and shell damage.
- [ ] Test client/server synchronization, Sable shell impacts, performance and save/restart.
- [ ] Evaluate Create Aeronautics vehicle integration separately. Do not assume it works without testing.
- [ ] Bronze and steel materials may require a separate ingot provider; upstream recommends IngotCraft, but it is not a required dependency in the CurseForge relation list. Research separately before adding.

**Status:** research candidate only. Not in the current installed inventory, not installed for IronWoven testing and not production-approved. Use a disposable test server/world after explicit approval.

## Colony ecosystem — complete candidate register

The complete candidate list remains:

| Candidate | Role | Status / next step |
|---|---|---|
| MineColonies | Main colony system | Verify exact stable 1.21.1 NeoForge release and its dependency chain |
| CreateColonies | Create/MineColonies integration | Verify exact project/release and Create 6.0.10 compatibility |
| Create: MineColonies Link | Separate Create integration | Verify distinct functionality and whether it coexists with CreateColonies |
| Structurize | MineColonies support component | Match the version required by selected MineColonies |
| Domum Ornamentum | MineColonies support component | Match the version required by selected MineColonies |
| BlockUI | MineColonies support component | Match the version required by selected MineColonies |
| Multi-Piston | Possible supporting dependency | Verify whether the selected MineColonies release requires it |
| TownTalk | Optional colony integration | Verify exact project, loader support and distinct functionality |
| Dynamic Trees | Separate world/ecology candidate | Verify NeoForge 1.21.1 and compatibility with BYG / Regions Unexplored |
| Colony building styles and schematics | Content research, not automatically mods | Check format, dependencies, compatibility and permissions |

No colony component is approved or installed by this list. Choose MineColonies and its exact required dependencies first, verify Create integrations, then test the selected stack only after approval on a disposable dedicated server and world. Keep Dynamic Trees as a separate test and preserve production world generation.


## Performance improvement candidates — 4 November 2026

**Current installed performance baseline:** ModernFix 5.27.27 and FerriteCore 7.0.3 are already in the recorded server inventory. Sodium 0.8.13, Sodium Extra 0.9.5 and Iris 1.8.14-beta.1 are client graphics components. Do not add a second renderer or duplicate memory optimizer.

| Candidate | Exact 1.21.1 NeoForge file/version | Scope | Purpose / test caution |
|---|---|---|---|
| spark | 1.10.124, CurseForge file 6225208 | Diagnostic profiler | Measures server tick/CPU/memory rather than increasing FPS. Use first to establish baseline and identify the real bottleneck. |
| ImmediatelyFast | 1.6.15, file 9165518 | Client | Optimizes GUI/HUD, text, particles, entities and block-entity rendering; complement to Sodium. |
| Entity Culling | 1.11.3, 1.21.1 NeoForge release | Client | Avoids drawing hidden entities/block entities. Test Create renderers carefully and whitelist pulleys/extended render bounds where needed. |
| Lithium | 0.15.4, file 8330365 | Server/game logic; confirm exact side requirements | General logic/tick optimization. Back up a disposable world and test alone against Create/Aeronautics and the current worldgen/data stack. |
| FastSuite | 6.0.7, file 7527945 | Recipe system | Optimizes JSON recipe lookup; check JEI, Create machines and custom recipe/datapack behavior. |
| FastFurnace | 9.0.1, file 6751551 | Furnace recipe processing | Optimizes furnace/blast furnace/smoker recipe matching, not smelting speed. Lower priority than FastSuite. |
| Chunk-Pregenerator | 4.5.4, NeoForge | Dedicated-server/world utility | Pre-generates a selected area to reduce first-exploration chunk-generation spikes. Does not improve FPS in already-generated chunks; plan disk usage/radius. |

Test one at a time and compare matching workloads. spark is diagnostics, not an optimization itself. C2ME and ServerCore are not in the first wave; assess experimental chunk threading and behavior-changing server optimizers separately. More Culling did not have a confirmed 1.21.1 NeoForge file in this review.

## Quality-of-life candidates — 4 November 2026

| Candidate | Exact 1.21.1 NeoForge file/version | Benefit | Notes |
|---|---|---|---|
| Just Enough Resources (JER) | 1.6.0.57, file 9311693 | Adds mob drops, ore generation and resource information to the existing JEI interface | Strong companion to already-installed JEI. |
| Shulker Box Tooltip | 5.1.9+1.21.1 | Shows shulker/container contents in tooltips | Small inventory QoL addition. |
| Enchantment Descriptions | 21.1.11 NeoForge 1.21.1 | Explains enchantments in tooltips | Requires Bookshelf. Bookshelf 21.1.81 loaded in the Botany Pots test group but is not confirmed in the main baseline. |
| Nature's Compass | 3.4.0 NeoForge 1.21.1 | Finds biomes | Useful with BYG and Regions Unexplored; decide whether its search ability fits exploration balance. |
| Explorer's Compass | 3.4.0 NeoForge 1.21.1 | Finds structures | Useful with modded structures, but can reduce exploration challenge. |
| Waystones | 21.1.46 NeoForge 1.21.1 | Player travel between placed waystones and scrolls | Requires compatible Balm. Optional; tune costs, visibility and cooldowns to suit multiplayer balance. |

### Existing QoL — no duplicate needed by default

- JEI, Jade, AppleSkin, Mouse Tweaks, FTB Chunks/Teams and Sophisticated Backpacks are already in the recorded inventory.
- FTB Chunks already supplies claims/team-map functionality; do not add another map/minimap by default.
- Sophisticated Backpacks is already present; another backpack mod is not a priority.
- JER extends JEI rather than replacing it.

These candidates are not installed or approved. Match exact CurseForge files/dependencies at the time of approval, use a separate test profile, and check client/server placement before adding them.


## Performance and long-distance/world-generation research — split by installation side (4 November 2026)

**Target:** Minecraft 1.21.1 / NeoForge 21.1.265 / Java 21. **Status:** research candidates only; none approved or installed.

### Client-side only — install in each player's CurseForge profile

| Candidate | Version | Purpose / test |
|---|---|---|
| ImmediatelyFast | 1.6.15 | Client render batching; test HUD, GUI, particles, entities and block entities. [CurseForge](https://www.curseforge.com/minecraft/mc-mods/immediatelyfast/files/9165518) |
| Flerovium | 1.1.2 stable | Requires the already-installed Sodium; item, particle and entity rendering improvements, potentially useful for Create depots/belts/dropped items. [CurseForge](https://www.curseforge.com/minecraft/mc-mods/flerovium) |
| Entity Culling | 1.10.4 | Hidden entity/block-entity culling; inspect Create contraptions, pulleys and Aeronautics/Sable sublevels. [CurseForge](https://www.curseforge.com/minecraft/mc-mods/entityculling/files/8274693) |
| Distant Horizons | 3.3.3 | Client LOD terrain rendering; test without shaders first, then only with an Iris shader pack that explicitly supports DH. [CurseForge](https://www.curseforge.com/minecraft/mc-mods/distant-horizons/files/9004764) |

Voxy/Roxy also belongs on the **client side only**, but is currently blocked: CurseForge-hosted Roxy 0.4.1 requires the original Voxy JAR; the only build its author identifies as verified is Voxy 0.2.16-beta for Minecraft 1.21.11, not a matching CurseForge 1.21.1 release. Do not install Roxy alone. SSRD may improve Aeronautics sublevel visibility with LOD, but no CurseForge download was verified.

### Server-side profiling / administration — install in the dedicated server for these tasks

| Candidate | Version | Purpose / test |
|---|---|---|
| spark | 1.10.124 | Server profiler for TPS/MSPT and CPU baselines; diagnostic only, not an FPS/TPS booster. Can also profile clients, but first use is server-side. [CurseForge](https://www.curseforge.com/minecraft/mc-mods/spark/files/6225208) |
| Chunk-Pregenerator | 4.5.4 | Dedicated-server world pre-generation utility; reduces first-exploration chunk-gen spikes, not FPS in existing chunks. Use only on a disposable world and defined radius. [CurseForge](https://www.curseforge.com/minecraft/mc-mods/chunkpregenerator/files/all) |

### Both client and server — use the matching version on both sides for paired tests

| Candidate | Version | Purpose / test |
|---|---|---|
| Lithium | 0.15.4 | Game-logic optimization, strong server-tick relevance; project supports client and server. Back up first and test Create, Sable, trains, inventories, redstone, mobs and farms. [CurseForge](https://www.curseforge.com/minecraft/mc-mods/lithium/files/8330365) |
| FastSuite | 6.0.7 | JSON recipe lookup optimization; project supports client and server. Test JEI, Create recipes and all custom datapacks. [CurseForge](https://www.curseforge.com/minecraft/mc-mods/fastsuite) |
| FastFurnace | 9.0.1 | Furnace recipe lookup optimization, not faster smelting; project marks Client & Server. Low priority for this Create-focused pack. [CurseForge](https://www.curseforge.com/minecraft/mc-mods/fastfurnace) |
| More Culling | **1.0.9** | Current 1.21.1 NeoForge file found; project marks Client & Server. Visual benefit is client-focused, but keep the paired deployment consistent and test both sides. Check leaves, glass, connected textures and modded blocks. [CurseForge files](https://www.curseforge.com/minecraft/mc-mods/moreculling/files/all) |

**Version correction:** an earlier note said More Culling 1.0.11. The matching 1.21.1 NeoForge release shown by CurseForge is **v1.0.9**. Do not use a later release intended for 1.21.11 or newer.

### Both client and server — world-generation test

| Candidate | Version | Purpose / safety |
|---|---|---|
| Tectonic | v3.0.28 ~ NeoForge 21.1 | CurseForge marks Client & Server; use the same version on both sides. Promising with BYG/RU via TerraBlender, but test only in a fresh disposable world with a copy of current JSON. Never change production world, BYG 2.6.3, RU 0.6.3 or active worldgen JSON. [CurseForge](https://www.curseforge.com/minecraft/mc-mods/tectonic/files/8855043) |

### Existing optimization baseline — already installed, grouped by side

- **Both client and server:** ModernFix 5.27.27; FerriteCore 7.0.3.
- **Client only:** Sodium 0.8.13; Sodium Extra 0.9.5; Iris 1.8.14-beta.1.
- Do not add another renderer such as Embeddium alongside Sodium or a duplicate memory optimizer.

For the full compatibility notes and evidence, see the private developer report [PERFORMANCE_VOXY_TECTONIC_RESEARCH_2026-11-04.md](https://github.com/alexth110987/Create-IronWoven/blob/docs/upstream-fix-ownership-register/docs/PERFORMANCE_VOXY_TECTONIC_RESEARCH_2026-11-04.md). The user's 88-mod count includes client-side files. No test candidate is production-approved.
