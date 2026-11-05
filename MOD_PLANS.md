# Mod Plans — Create IronWoven

**Last reviewed:** 5 November 2026  
**Target:** Minecraft 1.21.1 · NeoForge 21.1.265 · Java 21  
**Download policy:** CurseForge only

This page is the public register of requested additions, research candidates, paused ideas, and explicit exclusions. It is **not** an installed-mod inventory or an approval list.

- [Current test-pack inventory](MODS.md) records what is present in the latest documented test snapshot.
- [Testing checklist](TESTING_CHECKLIST.md) is the single task queue for unfinished tests and research.
- A candidate remains **not installed / not approved** unless the current inventory and a separate maintainer decision explicitly say otherwise.
- A startup pass proves only the specific startup/load steps recorded; it does not prove every feature or integration.

## Status definitions

  Status   Meaning |
|---|---|
| Candidate — research pending | Exact file, dependencies, side, or compatibility still needs checking. |
| Selected for isolated test | Chosen for a disposable test; not installed or approved for production. |
| Loaded — feature test pending | Appeared in a test server/profile; gameplay checks remain. |
| Testing | Installed in a test setup; smoke-test evidence is pending. Not approved for release. |
| Partial test pass | Only the explicitly recorded checks passed. |
| On hold | Do not resume without a new decision. |
| Excluded | Explicitly not wanted for this project. |
| Already in test inventory | No new addition is required; see [MODS.md](MODS.md). |

## Recently requested candidates

These six candidates came from the maintainer's 4 November shortlist. They were compared with the existing inventory and are retained here as potential additions only.

| Candidate | Candidate file/version | Existing overlap and assessment | Status |
|---|---|---|---|
| Just Enough Resources (JER) | 1.6.0.57 · [CurseForge file 9311693](https://www.curseforge.com/minecraft/mc-mods/just-enough-resources/files/9311693) | JEI 19.64.0.455 is installed. JER is a JEI addon for mob drops, loot, trades, plants, and world-generation information; it complements rather than replaces JEI. Check BYG / Regions Unexplored and custom loot coverage. | Candidate — test pending |
| Shulker Box Tooltip | 5.1.9+1.21.1 · [CurseForge file 7768285](https://www.curseforge.com/minecraft/mc-mods/shulkerboxtooltip/files/7768285) | Sophisticated Backpacks is installed but does not provide the same shulker-box preview feature. Client/server placement and supported container previews need checking. | Candidate — test pending |
| Enchantment Descriptions | 21.1.11 · [CurseForge file 8693034](https://www.curseforge.com/minecraft/mc-mods/enchantment-descriptions/files/8693034) | No equivalent tooltip mod is recorded. Requires Bookshelf and Prickle. Those libraries loaded in the separate Botany Pots test group but are not confirmed in the main client inventory. | Candidate — dependency/profile check |
| Nature's Compass | 3.4.0 · [CurseForge file 7892954](https://www.curseforge.com/minecraft/mc-mods/natures-compass/files/7892954) | BYG and Regions Unexplored add biomes, not a biome-search compass. Check modded-biome registration and locator balance. | Candidate — test pending |
| Explorer's Compass | 3.4.0 · [CurseForge file 7892943](https://www.curseforge.com/minecraft/mc-mods/explorers-compass/files/7892943) | Existing structure/world-generation mods and FTB Chunks do not provide the same structure-search function. Check modded structure tags and whether locating structures undermines exploration. | Candidate — test pending |
| Waystones | 21.1.46 · [CurseForge project](https://www.curseforge.com/minecraft/mc-mods/waystones) | Requires a compatible Balm. AeroPortals 1.3.6 is the nearest existing travel-system overlap, but a functional duplicate/conflict has not been established. Check the full Balm inventory and compare both systems in a disposable world. | Candidate — dependency and overlap review |

## Other requested additions

| Mod | Exact recorded candidate | Current evidence and next gate | Status |
|---|---|---|---|
| Botany Pots | 21.1.44 | Loaded with Bookshelf 21.1.81 and Prickle 21.1.11 in the 4 November test group. One plugin initialized and the test server parsed 14,444 recipes. Planting, growth, harvesting, and Herbs & Harvest integration remain unverified. Forty-seven optional integration recipes remain suppressed by temporary `neoforge:false` overrides; test a conditional `neoforge:mod_loaded` gate for `botanypots` in a disposable copy only. | Loaded — feature test pending |
| Construction Sticks | 1.5.0 | Loaded in the 4 November test group. Test vanilla/modded block placement, orientation, item consumption, and FTB Chunks claim protection. | Loaded — feature test pending |
| Lootr | 1.11.38.127 | User-confirmed: normal End City chests and ships work; BetterEnd-generated ships do not work with Lootr in the observed test. Second-player independent loot remains for beta testers. | Partial test pass — compatibility limitation recorded |
| Create Deco | 2.1.3 | Already present in the recorded test inventory. | Already in test inventory |
| Bookshelf | 21.1.81 | Conditional library dependency for Botany Pots and Enchantment Descriptions. Loaded in the Botany Pots test group; not thereby confirmed in the main client profile. | Conditional dependency |
| Prickle | 21.1.11 | Conditional library dependency for Botany Pots and Enchantment Descriptions. Loaded in the Botany Pots test group; not thereby confirmed in the main client profile. | Conditional dependency |
| Create: Curios Backtank | 1.0.2 · [CurseForge file 9207977](https://www.curseforge.com/minecraft/mc-mods/create-curios-backtank/files/9207977) | Minecraft 1.21.1 NeoForge client/server addon that makes the standard Create Backtank usable in the existing Curios `back` slot; it does not create a dedicated `backtank` slot. Requires Create and Curios API, both present in the master inventory. The maintainer intentionally removed More Curios Slots 1.4 because slot counts should be controlled in config rather than by crafting. Its MISSING status and old upgrade-recipe messages in the 5 Nov server log are expected. The internal config now sets the total Back-slot count to exactly two. Verify after restarting the disposable server; Create Backtank behavior remains to be tested. Support for Create: Sophisticated Air Tank or Aeronautics gear is not established. | **Testing — config updated; runtime retest pending** |
| More Curios Slots | 1.4 · [CurseForge file 8170156](https://www.curseforge.com/minecraft/mc-mods/more-curios-slots/files/8170156) | Minecraft 1.21.1 NeoForge client/server addon that provides craftable +1 slot upgrade items; it does not add accessory items. Requires Curios API. The maintainer intentionally removed this mod because players should not need to craft slot upgrades. Internal Curios config has been changed to set two Back slots and one Head slot. Restart and verify the layout; the previous client showed three Back slots. This mod is not planned for the current setup. | **Removed from test setup by maintainer — slot counts handled in config** |
| Create Big Cannons | 5.11.7 · [CurseForge file 8303106](https://www.curseforge.com/minecraft/mc-mods/create-big-cannons/files/8303106) | Requires Create 6.0.7+ and Ritchie's Projectile Library 2.1.2 ([file 7587771](https://www.curseforge.com/minecraft/mc-mods/ritchies-projectile-library/files/7587771)). Current Create 6.0.10 meets the published minimum. Check Sable compatibility, multiblocks, ammunition, recipes, damage, client/server sync, and Aeronautics separately. | Candidate — research/test pending |

## End generation and structure candidates — historical research / paused

**Workstream status: PAUSED.** The entries below preserve historical research and test evidence only. No End candidate is active, approved, or queued for testing. The maintainer paused this work because no suitable CurseForge-only Create-style abandoned-industrial End solution was found for Minecraft 1.21.1 / NeoForge 21.1.265.

| Candidate | Exact recorded file | Evidence / test gate | Status |
|---|---|---|---|
| YUNG's Better End Island | 3.1.2; YUNG's API 5.1.9 | Historical 4 November Batch 2A run: startup, client login and shutdown passed. Current 5 November server/client screenshots show the mod is no longer present. | On hold — End workstream paused; not in current test folders |
| BetterEnd: New Dawn | 21.0.39 · `BetterEnd-21.0.39.jar` | Historical 4 November partial test and Lootr ship limitation; YUNG's Better End Island was also loaded. Current 5 November server/client screenshots show the mod and its End-only libraries are no longer present. | On hold — End workstream paused; not in current test folders | 
| Ender Villages | `endervillages-2.0-1.21.1.jar` | CurseForge file 6741737; exact NeoForge 1.21.1 file verified. Project license is All Rights Reserved. No test is active. | On hold — End workstream paused; absent from current folder screenshots |
| Better End Cities Better End | `BetterEndCities-Raijin-structure-1.21.1.jar` | CurseForge file 8105176; dependency gate was never completed. No test is active. | On hold — End workstream paused; absent from current folder screenshots |
| MES — Moog's End Structures | `MoogsEndStructures-universal-1.21-2.1.1.jar` | Actual test file, Minecraft 1.21.1 / NeoForge. Crash report: required `moogs_structures` >=1.1.0 was missing. Add [Moog's Structure Lib 1.1.0 NeoForge file 7238573](https://www.curseforge.com/minecraft/mc-mods/moogs-structure-lib/files/7238573) before retrying. BetterEnd and YUNG's Better End Island were still loaded, so isolate them for the structure-generation test. | On hold — End workstream paused; absent from current folder screenshots |

**Historical End test order (paused; do not run):** the earlier proposed test stages are retained as research notes only. The End workstream is paused; preserve the production world and current BYG 2.6.3 / Regions Unexplored 0.6.3 setup.

## Batch 2B preliminary result — 4 November 2026

BetterEnd: New Dawn 21.0.39 and its required libraries loaded in the separate test installation. The user confirmed this Lootr compatibility result:

- Lootr works with normal End City chests and ships.
- Lootr does **not** work with ships generated by BetterEnd in the observed test.
- No use for the Ender Ore has been identified by the maintainer yet; this is recorded as unknown, not proof that the ore has no use.
- The uploaded server log shows YUNG's Better End Island 3.1.2 and YUNG's API 5.1.9 were also loaded, so this was not an isolated BetterEnd world-generation test.
- Remaining checks for BetterEnd biome variety, structures, resources, mobs, recipes/progression, and broader compatibility are deferred to beta testers.

**Status:** partial test only; beta feedback pending. BetterEnd is not production-approved. The current test result does not change the installed-mod inventory.

See [TESTING_CHECKLIST.md](TESTING_CHECKLIST.md) for the current test handover and [MODS.md](MODS.md) for the test inventory.

## Colony ecosystem research

No colony component is installed or approved by this register. Choose an exact stable MineColonies 1.21.1 NeoForge release first, then resolve its declared dependencies and integrations.

| Candidate | Role | Research gate |
|---|---|---|
| MineColonies | Main colony system | Verify exact NeoForge file and complete dependency chain. |
| CreateColonies | Create / MineColonies integration | Verify exact project, release, and Create 6.0.10 compatibility. |
| Create: MineColonies Link | Separate Create integration | Establish distinct functionality and whether it coexists with CreateColonies. |
| Structurize | MineColonies support component | Match the selected MineColonies release. |
| Domum Ornamentum | MineColonies support component | Match the selected MineColonies release. |
| BlockUI | MineColonies support component | Match the selected MineColonies release. |
| Multi-Piston | Possible support dependency | Confirm whether the selected MineColonies release requires it. |
| TownTalk | Optional colony integration | Verify exact project, loader support, and distinct functionality. |
| Dynamic Trees | Optional ecology/world-generation mod | Verify NeoForge 1.21.1 and compatibility with BYG / Regions Unexplored. |
| Colony building styles / schematics | Content research, not automatically a mod | Check format, dependencies, compatibility, and permissions. |

Test a selected colony stack only after its exact dependency set is established and after explicit authorization, using a disposable dedicated server and copied world. Keep Dynamic Trees as a separate world-generation investigation.

## Performance and rendering candidates

These are independent IronWoven candidates. Do not copy decisions from another modpack or test environment. Match the listed 1.21.1 NeoForge file and the correct installation side before any test.

### Client only

| Candidate | Version | Purpose / gate |
|---|---|---|
| ImmediatelyFast | 1.6.15 | Render batching; inspect HUD, GUI, particles, entities, and block entities. [CurseForge file 9165518](https://www.curseforge.com/minecraft/mc-mods/immediatelyfast/files/9165518) |
| Flerovium | 1.1.2 stable | Requires Sodium; test item, particle, and entity rendering. [CurseForge project](https://www.curseforge.com/minecraft/mc-mods/flerovium) |
| Entity Culling | 1.10.4 | Check Create contraptions, pulleys, Aeronautics, and Sable sublevels. [CurseForge file 8274693](https://www.curseforge.com/minecraft/mc-mods/entityculling/files/8274693) |
| Distant Horizons | 3.3.3 | Test LOD without shaders first; shader use requires a compatible Iris shader pack. [CurseForge file 9004764](https://www.curseforge.com/minecraft/mc-mods/distant-horizons/files/9004764) |
| Voxy / Roxy | No matching verified CurseForge 1.21.1 Voxy file | Blocked by source/version gate: Roxy 0.4.1 requires the original Voxy JAR, while the author-identified verified Voxy build is for Minecraft 1.21.11. Do not install Roxy alone. |
| SSRD | No verified CurseForge file | Research only; do not source or install outside the CurseForge-only policy. |

### Dedicated-server profiling / administration

| Candidate | Version | Purpose / gate |
|---|---|---|
| spark | 1.10.124 | Diagnostic profiler for TPS/MSPT and CPU baselines; not an FPS/TPS booster. [CurseForge file 6225208](https://www.curseforge.com/minecraft/mc-mods/spark/files/6225208) |
| Chunk-Pregenerator | 4.5.4 | Pre-generation utility, not an FPS fix. Use only on a disposable world and defined radius. [CurseForge project](https://www.curseforge.com/minecraft/mc-mods/chunkpregenerator) |

### Both client and server

| Candidate | Version | Purpose / gate |
|---|---|---|
| Lithium | 0.15.4 | Game-logic optimization. Test Create, Sable, trains, inventories, redstone, mobs, and farms. [CurseForge file 8330365](https://www.curseforge.com/minecraft/mc-mods/lithium/files/8330365) |
| FastSuite | 6.0.7 | Recipe lookup optimization. Test JEI, Create recipes, and custom datapacks. [CurseForge project](https://www.curseforge.com/minecraft/mc-mods/fastsuite) |
| FastFurnace | 9.0.1 | Furnace recipe lookup optimization, not faster smelting; lower priority for this pack. [CurseForge project](https://www.curseforge.com/minecraft/mc-mods/fastfurnace) |
| More Culling | **1.0.9** | Correct recorded NeoForge 1.21.1 version; earlier 1.0.11 note was superseded. Inspect leaves, glass, connected textures, and modded blocks. [CurseForge project](https://www.curseforge.com/minecraft/mc-mods/moreculling) |
| Tectonic | 3.0.28 · NeoForge 21.1 | World-generation candidate; test in a fresh disposable world with a copy of the current JSON. Never change production worldgen, BYG, Regions Unexplored, or active JSON. [CurseForge file 8855043](https://www.curseforge.com/minecraft/mc-mods/tectonic/files/8855043) |

**Recorded optimization baseline (not candidates):** ModernFix 5.27.27 and FerriteCore 7.0.3 on both sides; Sodium 0.8.13, Sodium Extra 0.9.5, and Iris 1.8.14-beta.1 on the client. Do not add a duplicate renderer alongside Sodium or another duplicate memory optimizer.

## On hold

| Mod / topic | Hold reason |
|---|---|
| Terralith | World-generation investigation is paused. Do not install it or dependencies, change the current BYG 2.6.3 / Regions Unexplored 0.6.3 setup, or alter existing worlds while on hold. Resume only when explicitly requested. |

## Explicit exclusions

These mods are not wanted for Create IronWoven and must not be reintroduced as candidates unless the maintainer explicitly changes the decision:

- Carry On
- Easy Villagers
- Immersive Paintings
- Bigger Better End Cities — larger vanilla-style End Cities do not fit the project's goal of adding more exploration variety.
- Create: Sophisticated Exoskeleton 1.0 — **REJECTED / removed** after Batch 5 testing because it did not meet the maintainer's expectations. Do not re-add unless the maintainer changes this decision.

## Test and approval safeguards

1. CurseForge is the only approved mod download source.
2. Verify the exact Minecraft 1.21.1 NeoForge file, dependencies, optional integrations, client/server side, maintenance status, and overlap before recommending installation.
3. Test candidates separately in a disposable profile/server/world. World-generation and structure candidates always require fresh disposable worlds.
4. Keep the production world and current BYG / Regions Unexplored configuration unchanged.
5. A test selection or successful startup does not approve a candidate for production or release.
6. Update this register when candidate status changes; update [MODS.md](MODS.md) only when the installed/test inventory is supported by evidence. Keep the detailed test steps in [TESTING_CHECKLIST.md](TESTING_CHECKLIST.md).
7. Batch 7 has not started unless a later dated project record explicitly updates that status.

## Suggest a mod

Players can use the [feature suggestion form](https://github.com/alexth110987/Create-IronWoven-Beta/issues/new?template=feature_suggestion.yml). Include the official project page, exact supported Minecraft / NeoForge versions, required dependencies, and why the mod fits Create IronWoven. Suggestions are reviewed, not automatically accepted.


## Every Compat (Wood Good) — research complete; test pending

**Status: Candidate only. Not installed or approved.** Exact CurseForge 1.21.1 NeoForge file: everycomp-1.21-2.11.56-neoforge.jar (file 9336749). Required library: Moonlight Lib; author's minimum is 1.21.1-3.7.2. Current 1.21.1 NeoForge CurseForge release is moonlight-1.21.1-3.8.1-neoforge.jar (file 9436226). Chipped 4.0.2 is already present and is listed as an optional Every Compat integration; Chipped-specific fixes are documented in the author's changelog.

**Pythadendron is not confirmed:** BetterEnd / Pythadendron is not named in the reviewed Every Compat build metadata or changelog. Verify it in a separate follow-up rather than assuming automatic support.

- [ ] Stage A: in a disposable copy of the current pack, add only Every Compat 2.11.56 and Moonlight 3.8.1 on both client and server. Keep existing Chipped 4.0.2, RU 0.6.3 and BYG 2.6.3 unchanged.
- [ ] Verify Chipped Carpenter's Table variants and recipes for multiple installed modded wood types; check JEI, textures/models, drops, placement, client/server consistency, logs and save/restart.
- [ ] Stage B only after Stage A passes: use a new separate disposable world/profile with the exact BetterEnd: New Dawn 21.0.39 dependency stack to test Pythadendron wood registration and Chipped variants. Do not reuse the 2B test world.
- [ ] Record any missing wood support, duplicate recipes, visual errors or registry conflicts.

Do not change the production inventory or world. Full details: [Every Compat Research and Test Plan](https://github.com/alexth110987/Create-IronWoven/blob/main/docs/EVERY_COMPAT_RESEARCH_2026-11-04.md).

## Lootr Compatibility: BetterEnd — new candidate (4 November 2026)

**Status: Candidate — exact 1.21.1 file / compatibility research pending. Not installed or approved.** Requested by the maintainer as a possible addition to address the observed BetterEnd + Lootr compatibility limitation.

- CurseForge project: [Lootr Compatibility: BetterEnd](https://www.curseforge.com/minecraft/data-packs/lootr-compat-betterend) — datapack by Noobanidus, MIT license.
- The datapack registers BetterEnd chest and barrel block types (including Pythadendron and other BetterEnd wood variants) as eligible for Lootr conversion when the blocks have associated loot tables.
- **Version gate:** the official CurseForge file listing currently shows the main file for Minecraft 1.21.7 and an earlier file for 1.21.4; it does not currently show an exact 1.21.1 file. The pack target is Minecraft 1.21.1 / NeoForge 21.1.265 and CurseForge-only. Do not install the 1.21.7 or 1.21.4 file or treat the generic “1.20 and later” description as proof of exact compatibility.
- **Scope gate:** the published compatibility list covers BetterEnd chest/barrel blocks, not BetterEnd ship structures as a whole. Verify the actual ship container block IDs and loot-table behavior before assuming this fixes the reported ship issue.
- [ ] Check the official CurseForge files again for an exact 1.21.1 release, or obtain explicit author confirmation for 1.21.1.
- [ ] Inspect a BetterEnd-generated ship in a disposable world and identify the exact container block(s) and whether each has a loot table.
- [ ] If the version gate is cleared, test the datapack alone with the existing Lootr + BetterEnd stack in a fresh disposable world; verify Lootr conversion and loot.
- [ ] Test the same converted container with a second player to confirm independent personal loot.
- [ ] Check normal End City loot is unchanged and inspect logs, save/restart, and datapack load priority.

Keep the current Lootr/BetterEnd ship incompatibility recorded until these checks pass. This is a data pack candidate, not a new mod JAR; do not add it to the installed-mod inventory yet.


## End expansion shortlist — 4 November 2026

**Target:** Minecraft 1.21.1 / NeoForge 21.1.265 / Java 21. **CurseForge only.** Every entry below is a potential candidate only; none is approved or installed.

| Candidate | Proposed role | Research / test gate |
|---|---|---|
| The Beyond 1.0.1 | Main End terrain and biome overhaul; new mobs and exploration | Test alone first. |
| Isleweaver 0.0.3b-InDev | Compatibility layer for combining The Beyond with other End biome mods | Test with The Beyond before adding other content. |
| Stellarity | Additional End fantasy content, structures and items | Confirm exact 1.21.1 NeoForge file; test after The Beyond + Isleweaver. |
| Unusual End 2.3.1b | More biomes, vegetation, mobs, resources and decorative block variants | Verify dependencies and test as a separate stage. |
| Extended End 0.9 | Obscurite ore, Void Bark wood, tools/armour, biome and decorative blocks | Older beta; verify exact file and recipes; test separately. |
| End Beyond 1.0.4 | Alternative End overhaul with Enderite progression, structures and boss | Separate alternative branch; do not combine with The Beyond without evidence. |

Existing End candidates remain: YUNG's Better End Island, BetterEnd: New Dawn, Bigger Better End Cities, Ender Villages, Better End Cities Better End, and MES — Moog's End Structures.

**Compatibility cautions:** Isleweaver's BetterEnd / WorldWeaver support has instability caveats; Stellarity lists BetterEnd as incompatible. End Ores' matching 1.21.1 file is Forge rather than NeoForge, and Dimensional Ores: End has no confirmed 1.21.1 NeoForge file. Do not add either based on a different loader/version.

**Test sequence:** The Beyond alone → The Beyond + Isleweaver → Stellarity after exact-file verification → Unusual End → Extended End → structure mods one at a time. Keep End Beyond as a separate comparison branch. Use a fresh disposable world for every stage. Check biomes, ore generation, mobs, structures, loot, recipes, building variants, chunk borders, client/server sync, save/restart and logs. Preserve the production world, BYG 2.6.3, Regions Unexplored 0.6.3 and current world-generation JSON.

Detailed findings and CurseForge links: [private maintainer research report](https://github.com/alexth110987/Create-IronWoven/blob/main/docs/END_EXPANSION_RESEARCH_2026-11-04.md).


### Stage A result — 4 November 2026

**Partial feature pass; not approved.** Maintainer confirms modded planks work in Chipped's Carpenter's Table and the stone table works. The supplied server log confirms Every Compat and Moonlight loaded, Chipped modules/dynamic resources generated, and the dedicated server reached Done.

Open concerns from the log:
- 9,480 compatibility blocks (36.22% of all registered blocks); Every Compat warns of increased memory use/load time, with Chipped the largest contributor (2,537 blocks).
- Duplicate block registration ERROR: `everycomp:ch/herbsandharvest/golden_cherry_fruit_leaves`.
- Test log includes BetterEnd, YUNG's Better End Island and the wider modpack; this is not an isolated test and does not prove Pythadendron support.

Continue checking recipes, JEI, models/textures, drops, more modded wood types, duplicate-leaf impact, client/server sync and save/restart. Keep candidate only; no production inventory changes.


### Full mod-list world test — 4 November 2026

Maintainer confirms the world works with the complete mod set shown in the latest test-installation screenshot, including Every Compat 2.11.56 + Moonlight 3.8.1, Chipped, BetterEnd and YUNG's Better End Island alongside the wider Create/Aeronautics pack. This is a user-confirmed pack-level world-playability result. It does not mean every mod feature/integration is fully tested or grant production approval. Every Compat remains a partial pass while recipe/JEI/visual/drop checks, the duplicate Golden Cherry registration, registry-size impact, Pythadendron and save/restart/client-server checks remain open.

## End design direction — abandoned industrial world (4 November 2026)

The maintainer's preferred End identity is an **abandoned industrial world**, rather than a strongly magical/fantasy dimension. Future End candidates should be assessed for derelict factories, refineries, mines, industrial outposts, abandoned small settlements, broken railways, cargo bridges, cranes, pipes, gears, turbines, laboratories and large industrial complexes. Prefer weathered metal, copper, brass and dark stone, with desolate landscapes and restrained End colours. Create-style engineering is the visual inspiration; functional Create machinery is not required.

This is a design preference, not a claim that any installed or shortlisted mod already adds these features. MES is a structure-variety candidate, not a confirmed town mod. Town/settlement generation remains a separate research need. No installation, approval or production-world change is implied.

## Superseding End direction — abandoned industrial civilisation (4 November 2026)

The maintainer has now chosen a firm visual/gameplay direction: the End should become the remains of a long-abandoned industrial civilisation, not a colourful fantasy biome overhaul or a collection of generic vanilla-style structures. Create-style engineering is the visual reference.

### Remove from the End test setup (proposed cleanup; not production approval)

The latest uploaded server log latest(20261104-225334).log confirms these End-generation mods are currently loaded:

| Mod | Current recorded version | Action | Reason |
|---|---:|---|---|
| BetterEnd: New Dawn | 21.0.39 | Remove from the End test profile | Its colourful fantasy biomes, plants and natural features do not match the selected abandoned-industrial aesthetic. |
| YUNG's Better End Island | 3.1.2 | Remove from the End test profile | Central-island overhaul is not an industrial-world feature and is not needed for the new direction. |
| MES / Moog's End Structures | 2.1.1 | Remove from the End test profile | Vanilla-styled generic End structures do not meet the industrial-ruin/factory target. The dependency now loads successfully, but this does not make MES thematically suitable. |

### Dependency cleanup — check before deleting

- Moog's Structure Lib 1.1.0 (moogs_structures) was added solely to satisfy MES in the recorded test. Remove it together with MES only after confirming no other installed mod requires it.
- BetterEnd's BCLib 21.0.28 and related BetterEnd support libraries were part of its stack. Remove a library only after checking the full current dependency graph; do not delete shared libraries blindly.
- YUNG's API 5.1.9 may be shared by other YUNG mods. Remove it only if no remaining installed mod requires it.
- Do not remove Lootr, Ender Ore or general-purpose libraries based on this aesthetic decision alone; they are not End terrain/structure overhauls in the evidence reviewed.

### Keep separate from the removal decision

- The user has not asked to delete the existing world or change the production server. Existing generated chunks cannot be visually transformed simply by removing mods.
- This is a proposed cleanup for the disposable/current test profile. Do not alter the authoritative installed inventory (MODS.md), production world, BYG 2.6.3, Regions Unexplored 0.6.3 or world-generation JSON without explicit approval.
- The Beyond, Isleweaver, Stellarity, Unusual End, Extended End, End Beyond, Ender Villages and other earlier fantasy/vanilla-style candidates are not automatically suitable. Reassess or pause them against the industrial theme; do not carry them forward just because they were previously shortlisted.
- Current research has not verified a CurseForge 1.21.1 NeoForge mod that directly supplies abandoned industrial End factories or towns. Do not claim one exists until exact files and feature evidence are found.

### New research priority

Find CurseForge-only Minecraft 1.21.1 NeoForge content that actually generates derelict factories, mining/processing facilities, industrial outposts, abandoned settlements, cargo infrastructure, cranes, pipes, machinery and weathered metal structures in the End. If no End-specific option exists, investigate whether structure datapacks or configurable structure-generation tools can achieve this without introducing an unrelated fantasy overhaul. Record exact files, dependencies, licensing, dimension placement and actual structure previews before adding anything to the test queue.

## Overworld addition — Create Aeronautics Structures

**Selected for the Overworld, not the End.** Create Aeronautics Structures adds abandoned engineering buildings, boats, airships and balloon structures that fit the pack's Create/Aeronautics exploration theme.

- CurseForge: [Create Aeronautics Structures](https://www.curseforge.com/minecraft/mc-mods/create-aeronautics-structures)
- Target: Minecraft 1.21.1 / NeoForge 21.1.265.
- Exact CurseForge file version/ID and dependency versions still need verification before installation. Reported dependencies: Create Aeronautics, Sable and GeckoLib.
- Keep its structure placement in the Overworld; it is not an End content candidate.
- Status: selected planned addition / test queue; not installed or production-approved. Test in a disposable world/profile first.

## End mod workstream — paused

The maintainer has paused End-mod research and testing for now. No suitable CurseForge-only Minecraft 1.21.1 / NeoForge mod has been identified that provides the desired Create-style abandoned industrial End.

- Keep the abandoned-industrial End concept as a future direction, but do not actively search, shortlist, install or test End overhaul/structure mods until the maintainer reopens this workstream.
- Previously recorded End candidates remain historical research only; this pause does not approve any of them.
- This does not change the installed mod list, production world or world-generation settings.
- Overworld additions, including Create Aeronautics Structures, remain a separate active workstream.

## End test-profile cleanup — 5 November 2026

The maintainer has explicitly instructed that all End-specific mods be removed from the active disposable test setup while End development is paused. This supersedes the previous instruction to keep Ender Ore in the test setup.

- Remove any present End-only content JARs from the disposable test server and matching client: YUNG's Better End Island, BetterEnd: New Dawn, Ender Ore, Ender Villages, Better End Cities Better End, MES / Moog's End Structures, and any other End-only generation/content mods.
- Bigger Better End Cities is excluded and must also be removed if present in the test folders. The Beyond, Isleweaver, Stellarity, Unusual End, Extended End, End Beyond and other uninstalled candidates must stay out.
- Remove libraries used only by removed End mods only after checking the dependency graph; keep shared libraries. Lootr is general-purpose and is not included in this End-specific removal instruction.
- End research and testing remain paused until the maintainer explicitly reopens the workstream.

**Physical removal not yet verified:** GitHub access does not expose the live Minecraft test server/client mods folders. A current directory listing and clean startup log are required before cleanup can be reported as complete. Historical test notes are retained as historical evidence only.

## End test-profile cleanup — visually verified 5 November 2026

The maintainer supplied current screenshots of both the disposable dedicated-server `MinecraftServer-Test/mods` folder and the CurseForge client `Create World/mods` folder. No End-specific content/generation JARs are visible in either. BetterEnd, YUNG's Better End Island, Ender Ore, Ender Villages, Better End Cities Better End, MES / Moog's End Structures and Bigger Better End Cities are absent; no End-only support libraries are visible either. Lootr remains as a general-purpose mod.

This visually verifies the current cleanup at screenshot level, not through a live filesystem scan or fresh startup log. All End entries above remain historical research only; the End workstream stays paused. Do not add End mods back or resume tests unless the maintainer explicitly asks. Create Aeronautics Structures remains a planned Overworld addition, not an installed mod in these screenshots.

