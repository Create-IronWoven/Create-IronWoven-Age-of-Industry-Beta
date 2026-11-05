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

| Status | Meaning |
|---|---|
| Candidate — research pending | Exact file, dependencies, side, or compatibility still needs checking. |
| Selected for isolated test | Chosen for a disposable test; not installed or approved for production. |
| Loaded — feature test pending | Appeared in a test server/profile; gameplay checks remain. |
| Testing | Installed in a test setup; smoke-test evidence is pending. Not approved for release. |
| Smoke test passed | Server startup, test-world load, and matching client login passed; no feature-by-feature behavior is implied. Not approved for production or release. |
| Partial test pass | Only the explicitly recorded checks passed. |
| On hold | Do not resume without a new decision. |
| Excluded | Explicitly not wanted for this project. |
| Already in test inventory | No new addition is required; see [MODS.md](MODS.md). |

## Active installation batch order

The private project has a detailed test plan. Batches use disposable test copies. The standard pass before moving to the next batch is server startup (`Done`), test-world load, matching client login, and log review. Feature examples in the private plan are optional follow-ups, not mandatory requirements for the routine smoke test; deeper tests are added only for a specific unresolved issue after maintainer agreement. The active order is: client information and tooltips; exploration locators; Create Big Cannons; Create Aeronautics Structures; measured performance tests; server/recipe optimizers; isolated world utility and world generation; then the Waystones travel-system decision. Colony candidates, unverified-source candidates, and all paused End content are not installation batches.

**Batches A, B, and C have passed the routine startup/login smoke test.** Batch A's 5 November log verifies the combined server startup, world load, client login, and clean shutdown; Shulker Box Tooltip registered 31 providers. Batch B's 5 November log verifies Nature's Compass 3.4.0 and Explorer's Compass 3.4.0 were present together, the server reached `Done`, the world loaded, the client joined, and shutdown saved all dimensions. A Nature's Compass INFO search message is noted, without a feature verdict. **Batch C — Create Big Cannons 5.11.7 with Ritchie's Projectile Library 2.1.2 — passed its routine smoke test on 5 November 2026.** **Batch D — Create Aeronautics Structures 1.1.0-Beta-3.1 — was attempted in a disposable server on 5 November.** The server started, loaded the test world, accepted a client login, and shut down cleanly. The Russian startup message is informational only and is not a blocker. One candidate-specific loot-table parsing ERROR remains unresolved; exact CurseForge file provenance and structure generation remain unverified. Do not advance to Batch E until the technical issue and outstanding verification are reviewed. No candidate is approved for production/release. See [Testing Checklist](TESTING_CHECKLIST.md) for the live queue.

## Recently requested candidates

These six candidates came from the maintainer's 4 November shortlist. They were compared with the existing inventory and are retained here as potential additions only.

| Candidate | Candidate file/version | Existing overlap and assessment | Status |
|---|---|---|---|
| Just Enough Resources (JER) | 1.6.0.57 · [CurseForge file 9311693](https://www.curseforge.com/minecraft/mc-mods/just-enough-resources/files/9311693) | JEI 19.64.0.455 is installed. JER complements JEI with mob drops, loot, trades, plants, and world-generation information. Batch A routine startup/world-load/client-login smoke test passed. | Smoke test passed — no feature-by-feature test claimed |
| Shulker Box Tooltip | 5.1.9+1.21.1 · [CurseForge file 7768285](https://www.curseforge.com/minecraft/mc-mods/shulkerboxtooltip/files/7768285) | Sophisticated Backpacks does not provide the same shulker-box preview feature. Batch A routine startup/world-load/client-login smoke test passed; the server log also records protocol version 2.0 and 31 registered providers. | Smoke test passed — no feature-by-feature test claimed |
| Enchantment Descriptions | 21.1.11 · [CurseForge file 8693034](https://www.curseforge.com/minecraft/mc-mods/enchantment-descriptions/files/8693034) | Requires Bookshelf; Bookshelf 21.1.81 was present in the same server run. Prickle is not required for Enchantment Descriptions. Batch A routine startup/world-load/client-login smoke test passed. | Smoke test passed — no feature-by-feature test claimed |
| Nature's Compass | 3.4.0 · [CurseForge file 7892954](https://www.curseforge.com/minecraft/mc-mods/natures-compass/files/7892954) | Batch B routine startup/world-load/client-login smoke test passed. The server log contains one INFO biome-search message ending without a result; no target context is available, so no feature verdict is recorded. | Smoke test passed — no feature-by-feature test claimed |
| Explorer's Compass | 3.4.0 · [CurseForge file 7892943](https://www.curseforge.com/minecraft/mc-mods/explorers-compass/files/7892943) | Batch B routine startup/world-load/client-login smoke test passed. No feature-by-feature structure search is claimed or required by default. | Smoke test passed — no feature-by-feature test claimed |
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
| Create: Curios Backtank | 1.0.2 · [CurseForge file 9207977](https://www.curseforge.com/minecraft/mc-mods/create-curios-backtank/files/9207977) | Minecraft 1.21.1 NeoForge client/server addon that makes the standard Create Backtank usable in the existing Curios `back` slot; it does not create a dedicated `backtank` slot. Requires Create and Curios API, both present in the master inventory. The maintainer intentionally removed More Curios Slots 1.4 because slot counts should be controlled in config rather than by crafting. Its MISSING status and old upgrade-recipe messages in the 5 Nov server log are expected. The internal config sets the total Back-slot count to two, and the maintainer reports that a newly created test world displays two Back slots. Backpack + standard Create Backtank, Aviator Goggles, and Linked Typewriter checks are reported working in their assigned slots. Matching client/server log review remains open. Support for Create: Sophisticated Air Tank or other Aeronautics gear is not established. | **Testing — targeted checks reported working; matching log review pending** |
| More Curios Slots | 1.4 · [CurseForge file 8170156](https://www.curseforge.com/minecraft/mc-mods/more-curios-slots/files/8170156) | Removed from the test setup by maintainer decision. Craftable slot upgrades are not wanted; slot counts are managed through Curios config. Do not reinstall unless the maintainer changes this decision. | **Removed from test setup — not wanted** |
| Create Big Cannons | 5.11.7 · [CurseForge file 8303106](https://www.curseforge.com/minecraft/mc-mods/create-big-cannons/files/8303106) | Requires Create 6.0.7+ and Ritchie's Projectile Library 2.1.2 ([file 7587771](https://www.curseforge.com/minecraft/mc-mods/ritchies-projectile-library/files/7587771)). Both were present in Batch C; the routine startup/world-load/client-login/log-review smoke test passed. Cannon features were not separately tested. | Smoke test passed — not production/release approved |

## End generation and structure candidates — historical research / paused

**Workstream status: PAUSED.** No End candidate is active, approved, or queued for testing. The maintainer paused this work because no suitable CurseForge-only Create-style abandoned-industrial End solution was found for Minecraft 1.21.1 / NeoForge 21.1.265. The entries below are retained only as a record of previously considered ideas; they are not a testing queue.

| Historical candidate | Recorded status |
|---|---|
| YUNG's Better End Island 3.1.2 | Previously smoke-tested with YUNG's API 5.1.9; absent from the reviewed 5 November test folders. |
| BetterEnd: New Dawn 21.0.39 | Previously partially tested; its ship/Lootr limitation is historical. Absent from the reviewed 5 November test folders. |
| Ender Villages 2.0 | CurseForge file 6741737 was identified; licence and gameplay review remain incomplete. |
| Better End Cities Better End | CurseForge file 8105176 was identified; dependency review was not completed. |
| MES — Moog's End Structures | Historical crash due to missing Moog's Structure Lib; no retry is active. |
| The Beyond, Isleweaver, Stellarity, Unusual End, Extended End, End Beyond | Historical shortlist only; no current search or test is active. |

Do not resume End searches, installs, or tests unless the maintainer explicitly reopens the workstream. Preserve the production world and the current BYG 2.6.3 / Regions Unexplored 0.6.3 setup.

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
| More Culling | **1.0.11** | CurseForge lists a Minecraft 1.21.1 NeoForge release; project metadata identifies it as client-only. Test leaves, glass, connected textures, and modded blocks on the client only. Exact file ID still needs reconciliation. [CurseForge 1.21.1 files](https://www.curseforge.com/minecraft/mc-mods/moreculling/files/all?page=1&version=1.21.1) |
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
- Distant Horizons 3.3.3 — reviewed as a performance/rendering option, but the maintainer does not want it in Create IronWoven. Do not test, install, or reintroduce unless the maintainer explicitly changes this decision.

## Test and approval safeguards

1. CurseForge is the only approved mod download source.
2. Verify the exact Minecraft 1.21.1 NeoForge file, dependencies, optional integrations, client/server side, maintenance status, and overlap before recommending installation.
3. Test candidates separately in a disposable profile/server/world. World-generation and structure candidates always require fresh disposable worlds.
4. Keep the production world and current BYG / Regions Unexplored configuration unchanged.
5. A test selection or successful startup does not approve a candidate for production or release.
6. Update this register when candidate status changes; update [MODS.md](MODS.md) only when the installed/test inventory is supported by evidence. Keep the detailed test steps in [TESTING_CHECKLIST.md](TESTING_CHECKLIST.md).
7. Follow the lettered batch order in the private active installation plan. Batch E must not begin until the Batch D decision gate is resolved.

## Suggest a mod

Players can use the [feature suggestion form](../../issues/new?template=feature_suggestion.yml). Include the official project page, exact supported Minecraft / NeoForge versions, required dependencies, and why the mod fits Create IronWoven. Suggestions are reviewed, not automatically accepted.

## Every Compat (Wood Good) — research complete; test pending

**Status: Candidate only. Not installed or approved.** Exact CurseForge 1.21.1 NeoForge file: everycomp-1.21-2.11.56-neoforge.jar (file 9336749). Required library: Moonlight Lib; author's minimum is 1.21.1-3.7.2. Current 1.21.1 NeoForge CurseForge release is moonlight-1.21.1-3.8.1-neoforge.jar (file 9436226). Chipped 4.0.2 is already present and is listed as an optional Every Compat integration; Chipped-specific fixes are documented in the author's changelog.

**Pythadendron is not confirmed:** BetterEnd / Pythadendron is not named in the reviewed Every Compat build metadata or changelog. Verify it in a separate follow-up rather than assuming automatic support.

- [ ] Stage A: in a disposable copy of the current pack, add only Every Compat 2.11.56 and Moonlight 3.8.1 on both client and server. Keep existing Chipped 4.0.2, RU 0.6.3 and BYG 2.6.3 unchanged.
- [ ] Verify Chipped Carpenter's Table variants and recipes for multiple installed modded wood types; check JEI, textures/models, drops, placement, client/server consistency, logs and save/restart.
- [ ] Stage B (BetterEnd / Pythadendron) is on hold while End research/testing is paused. Do not resume unless the maintainer explicitly reopens the End workstream.
- [ ] Record any missing wood support, duplicate recipes, visual errors or registry conflicts.

Do not change the production inventory or world. Full details: Every Compat Research and Test Plan.

## Lootr Compatibility: BetterEnd — historical research, on hold

**Status: ON HOLD — End workstream paused. Not installed or approved.** This datapack was researched as a possible response to the historical BetterEnd + Lootr limitation.

- CurseForge project: [Lootr Compatibility: BetterEnd](https://www.curseforge.com/minecraft/data-packs/lootr-compat-betterend), MIT licence.
- The published project information describes Lootr conversion for BetterEnd chest/barrel blocks; it does not establish compatibility with BetterEnd ship structures as a whole.
- The reviewed CurseForge file listing did not show an exact Minecraft 1.21.1 file. Do not use 1.21.4 or 1.21.7 files for this pack.
- Do not resume research, install, or test this datapack unless the maintainer explicitly reopens End work.

## Overworld addition — Create Aeronautics Structures

**Selected for the Overworld, not the End.** Create Aeronautics Structures adds abandoned engineering buildings, boats, airships and balloon structures that fit the pack's Create/Aeronautics exploration theme.

- CurseForge: [Create Aeronautics Structures](https://www.curseforge.com/minecraft/mc-mods/create-aeronautics-structures)
- Target: Minecraft 1.21.1 / NeoForge 21.1.265.
- Detected test version: 1.1.0-Beta-3.1. The exact CurseForge file ID/provenance and dependency declarations still need verification. Create Aeronautics 1.3.2, Sable 2.0.6, and GeckoLib 4.9.3 were present in the test log.
- Keep its structure placement in the Overworld; it is not an End content candidate.
- Startup message observed in the test log: `Мод Create Aeronautics Structures загружается!`  
  **English translation:** “Create Aeronautics Structures is loading!” (informational startup message).  
- Status: test attempted in a disposable profile; partial pending review of a candidate-specific loot-table error. Exact CurseForge file provenance and structure generation remain unverified. The message language is not a blocker. Not production-approved.
