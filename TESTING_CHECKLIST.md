# Full Installed-Mod Functional Testing Checklist

**Last updated:** 5 November 2026  
**Target:** Minecraft 1.21.1 · NeoForge 21.1.265 · Java 21  
**Approved download source:** CurseForge only

This is the full functional-test matrix for the recorded Create IronWoven test installation. It currently tracks 123 feature and support-module entries. It covers more than the active batch queue. The inventory basis is the 5 November dedicated-server mod list plus the client-only entries in the latest reviewed client inventory. This is a test snapshot, not a final release manifest.

## Smoke test is not a function test

The 5 November combined test reached Done (1.718s), loaded world_lootr_test, accepted a client login and shut down cleanly. Batches A, B and C also passed their recorded pack-level startup/login smoke tests. This proves the combined test profile can load and join; **it does not prove every installed mod's functions work**.

- **Smoke test:** mod discovery, server/client startup as appropriate, world load, login, shutdown and log review.
- **Function test:** exercise the actual feature(s) that justify keeping the mod: item/block interaction, machine process, transport, GUI, world generation, rendering, recipe/loot behavior or synchronization.
- A combined smoke-test pass is not an individual mod-function pass. Do not mark a feature complete just because its mod ID appears in a server log.
- Client-only mods require a matching client launch and client-side review. A dedicated-server log cannot prove their client functions.
- Libraries/APIs are tested through the mod(s) that depend on them; they do not need invented standalone gameplay tests.

## Current pack-level smoke evidence

| Check | Evidence | Status |
|---|---|---|
| Dedicated-server startup | 5 Nov log reached Done (1.718s) | PASS — combined profile |
| Disposable world load | world_lootr_test loaded | PASS |
| Matching client login | One client joined | PASS |
| Clean shutdown | All dimensions saved | PASS |
| Individual feature tests | Matrix below | OPEN — mostly not yet function-tested |
| Matching client-only mod startup | No matching current client log supplied for this snapshot | OPEN |
| Production/release approval | Not granted | NOT APPROVED |

## Existing partial function evidence — do not overstate it

- **Curios:** two Back slots and one Head slot appeared in a newly created test world. Backpack + standard Create Backtank, Aviator Goggles and Linked Typewriter use were reported working in their assigned slots. Full matching client/server synchronization and older-player saved-slot correction remain separate.
- **Lootr:** the maintainer confirmed a test chest opened and contained loot. Independent personal loot for a second player is not yet verified.
- **Every Compat:** Chipped Carpenter's Table modded-wood variants and the stone table were reported working. This is partial; duplicate Golden Cherry Leaves registration and the large compatibility-block footprint remain recorded.
- **Create Aeronautics Structures:** server smoke test passed, but structure generation was not established and its loot table has a parsing error.
- **Batch A:** JER, Enchantment Descriptions and Shulker Box Tooltip passed combined startup/login smoke testing; feature rendering/use remains to be checked.
- **Batch B:** Nature's Compass and Explorer's Compass passed combined startup/login smoke testing; actual biome/structure searches remain to be checked.
- **Batch C:** Create Big Cannons and Ritchie's Projectile Library passed combined startup/login smoke testing; cannon operation remains to be checked.
- **Batch E:** spark initialized, but no saved profiler report or numeric baseline was recorded. ImmediatelyFast, Flerovium, Entity Culling and More Culling were detected in the server mod list; their individual client tests have not been completed.

## How to complete this checklist

For each feature mod, mark its function complete only after the listed primary behavior works on the intended side(s). Where a mod adds several independent systems, test each system, not just one decorative block. For persistent machines, vehicles, storage, claims, portals and player data, include save/restart or relog. For multiplayer-dependent features, use a second player. Record exact version, test world/profile, relevant log and result.

Use JEI/creative inventory to locate representative items, but item visibility alone is not a functional pass. You do not need to test every recipe or decorative variant; test the primary function and each distinct subsystem.

**World-generation safeguard:** all biome/structure checks use a fresh disposable Overworld. Keep production world, BYG 2.6.3, Regions Unexplored 0.6.3 and active world-generation JSON unchanged. End research remains paused.

**Status meanings:** Pending = not function-tested; Partial = some behavior confirmed but listed test remains open; Pass = all listed primary functions have evidence; Failed/Blocked = reproducible failure or prerequisite prevents validation; N/A = support component checked through dependent mod.

## A. Create, Aeronautics, vehicles and transport

| Mod / version | Functional checks to complete | Status |
|---|---|---|
| Create 6.0.10 | Build a kinetic network; test speed/rotation control, one press/mixer/deployer chain, item/fluid transport and save/restart. | Pending |
| Create Aeronautics 1.3.2 | Assemble a vehicle; test propulsion/lift, steering, controls, collision/physics, disassembly/reassembly and second-player sync. | Pending |
| Create: Simulated 1.3.2 | Test assembly/disassembly, anchoring, controls, redstone interaction, collision and save/reload. | Pending |
| Create: Offroad 1.3.2 | Build a wheeled vehicle; test wheel power, steering, traction, stopping, collision and multiplayer sync. | Pending |
| Create Kinetic 1.4.3 | Test its Aeronautics utility/propulsion blocks and items; verify hitboxes, particles, controls and physics on client/server. Recheck existing loot-table and mixin findings. | Pending |
| Create Aeronautics Structures 1.1.0-Beta-3.1 (test-only) | Fresh disposable Overworld: confirm engineering houses, abandoned boats, airships and hot-air balloons generate; test engineer trader and chest loot; recheck cr_aero_structures:chests/uniform. | Partial — server smoke passed; generation unproven; one loot-table parse error remains. |
| Create Aeronautics Curios Compat 2.0 | Equip Aviator Goggles in Head slot; test overlay/engineer detection. Equip Linked Typewriter in Curios and activate (default Y) to operate linked typewriter/Redstone Links. | Partial — assigned-slot checks user-reported working; repeatable synced test still needed. |
| Create Aeronautics: Copycat Wing 1.0.4 | Use a Copycats+ block as a wing part; verify lift. Honeycomb should disable lift and axe restore it; test on a moving contraption. | Pending |
| Create Aeronautics: Transmission & Linkage 0.2.9 | Build a transmission/linkage assembly; verify it transfers the intended movement/control across running and assembled contraptions. | Pending |
| Create Big Cannons 5.11.7 | Assemble a multiblock cannon; load projectiles/fuzes; test Create-powered loading/aiming, firing, projectile effect/recoil, reload and autocannon if used. | Pending |
| Create: Steam 'n' Rails 0.3.0-alpha.2 | Assemble/run a train; test tracks, bogeys, schedules/stations, signals and installed railway interactions; verify save/restart. | Pending |
| Create: Blocks & Bogies 1.0.8 | Open bogie UI (crouch + right-click empty-handed); configure drivers/axles, assemble train and verify style and operation. | Pending |
| Create: Modern Train Parts 0.2.5 | Test pantograph deployment/retraction, shipping-container storage, wrench variants and train movement with parts attached. | Pending |
| Create: Pantographs & Wires 0.2.3-C6 Beta | Place masts/cantilevers and catenary; verify wire connection and pantograph height adjustment on a moving train, including slopes/turns. | Pending |
| Create: Rustic Structures 1.0.1 | Fresh disposable Overworld: find well, smithy, windmill and barn in intended biome groups; inspect placement, loot and generation. | Pending |
| Create: Structures Arise 176.49.50 | Fresh disposable Overworld: find multiple Create-themed structures; inspect integrity, placement, loot and chunk-edge generation. | Pending |
| Create: Aeronautical Diesel 1.1.0 | Use tank/fill port to move diesel, biodiesel, gasoline, ethanol, crude oil or plant oil into an Aeronautics portable engine; test wrench and automation. | Pending |
| Create: AeroPortals 1.3.6 | Move a complete airship through vanilla and supported modded portals; verify ship, pilot, passengers and decorations arrive intact. | Pending |
| Shield Generators 1.4.0 | Power a shield generator; test activation, energy draw, boundary visualization, protection/interaction and multiplayer consistency. | Pending |
| KineticGrip 1.0.5 | Test the Aeronautics handles from the player point of view; operate the handle controls and any player-usable tool (such as the chainsaw) included by the installed build. Verify movement/control and client/server interaction. | Pending |
| Sable 2.0.6 | Test Aeronautics physics: assembly, motion, forces, collision, sublevels and save/restart; inspect Copycats Catwalk physics-tag errors. | Pending |
| Strut Your Stuff 1.3.1 | Validate through dependent mods: spanning/collision structures, surface clipping, interaction and cable behavior/droop; check dedicated-server RenderSystem class-loading issue. | Pending — shared library; dependent integration and server-side issue remain open. |

## B. Create automation, energy, industry and build addons

| Mod / version | Functional checks to complete | Status |
|---|---|---|
| Create: Bits 'n' Bobs 2.3.5 | Test chain-drive transfer/carriage attachment, flywheel bearing rotation/battery behavior, wooden cogwheel swapping, dyeable fluid-pipe separation, chair and Nixie display. | Pending |
| Create Cobblestone 1.5.1 | Set generator to cobblestone, stone, basalt, limestone and scoria; verify outputs, type switching, SU use and disabled-generator behavior. | Pending |
| Create Crafts & Additions 1.6.0 | Run Electric Motor from FE and verify SU output; drive Alternator with SU and verify FE output; test rolling-mill rods/wires. | Pending |
| Create: Curios Backtank 1.0.2 | Equip Backtank with intended Curios/backpack setup; test air capacity, refill, consumption and rendering/slot behavior. | Partial — Backpack + standard Backtank use in configured Back slots was reported; refill/consumption still open. |
| Create Deco 2.1.3 | Test decorative blocks/variants, recipes, placement, rotation and drops; recheck placard fix and loot-table parsing. | Pending |
| Create: Diesel Generators 1.3.15 | Run an oil-to-fuel chain; start diesel generator and test FE output, fuel consumption, upgrades and a representative machine/tool. | Pending |
| Create Encased 1.10.0-fix1 | Apply casings to shafts, cogwheels and pipes; test rotation, power/fluid transfer and persistent casing visuals. | Pending |
| Create: Gadgets & Gizmos 1.2.10 (bundled) | Test installed gadgets/engine components used by Aeronautics: assembly, thrust/control, fuel/power consumption and contraption synchronization. | Pending |
| Create: Dragons Plus 1.11.9 | Use an Encased Fan to test Bulk Coloring with dye fluid, Bulk Freezing with Powder Snow, Bulk Ending with Dragon Head or Dragon's Breath fluid, and Bulk Sanding with Quicksand/supported block tag. Test Fluid Hatch take/deposit behavior on tanks and supported addon recipe integrations. | Pending |
| Create: Liquid Fuel 3.0.0 | Feed supported liquid fuel to a Blaze Burner; verify normal/superheated operation, duration, consumption and rejection of invalid fluids. | Pending |
| Create: Fluids Be Gone! 1.0.1 | Run a Create Drill and a Simulated Rock Cutting Wheel into fluid-containing terrain; verify fluids in the mined path are voided when enabled, separate drill/rock-wheel config switches work, and fluids outside the mining path remain unchanged. | Pending |
| Create: Framed 1.8.2 | Build framed blocks, apply a supported material/appearance and shape; verify placement, rotation, breaking and reload. | Pending |
| Create: Enchantment Industry 2.5.4b | Run automated enchanting/disenchanting and XP-fluid processing; verify inputs, outputs, XP/fluid handling, recipes and automation. | Pending |
| Create: Numismatics 1.0.20 | Obtain coins; use Vendor for buy/sell, Bank Terminal for deposit/withdraw, and Depositor price/redstone pulse for coin/card payments. | Pending |
| Create: Numismatics Plus 1.0.1 | Buy from a Create shop with coins and a Numismatics card; verify deduction, stock, recipient account and missing-Depositor/card behavior. | Pending |
| Create: Pattern Schematics 2.0.10 | Create/obtain a repeating schematic; print in creative or use Schematicannon; verify placement, orientation, repeat behavior and resource requirements. | Pending |
| Create: Power Grid 0.6.2 | Build a small electrical network with source, wires, transformer and consumers; test components and fallback solver; record native solver separately. | Partial — server loads; optional native solver unavailable in tested Windows environment; fallback function not yet verified. |
| Create: Sound of Steam / Pipe Organs 0.9.2.1 | Place/configure a pipe organ; trigger notes manually and by supported controls/redstone; test pitch, sound, range, persistence and multiplayer audio. | Pending |
| Create: The Factory Must Grow 1.3.2a-community | Run representative industrial processing: fluid/oil input, machine processing, outputs, power/kinetic requirements and fuel-burning machine; test Unified Fuels integration. | Pending |
| Create: Unified Fuels 1.0.4 | Cross-feed fuels between supported addons and compatible engines, burners and trains; verify shared values/consumption, gas-vs-liquid rules, toggles and config after restart. | Pending |
| Create: Vibrant Vaults 0.3.2 | Build/connect vaults and shipping containers; insert/extract items, change color/orientation and test package frogport/stock link/packager features present. | Pending |
| Create Slice & Dice 4.3.4 | Automate a Farmer's Delight cutting-board recipe with Create saw; verify ingredients, output, transport and recipe visibility. | Pending |
| Create: Bells & Whistles 0.4.7 | Test representative decorative train/building blocks, variants, placement, rotation, collision and rendering on moving contraptions. | Pending |
| Create: Copycats+ 3.0.9 | Use copycat shapes with multiple source materials; verify appearance, shape/state, rotation and moving-contraption rendering. | Pending |
| Copycats+ Additions 1.5.0 | Test added copycat shapes/variants, material application and placement; verify Aeronautics Copycat Wing integration. | Pending |
| Design n' Decor 2.2b | Test representative decoration families, recipes and drops; specifically verify dyed cogwheel/loot-table entries and intended block drops. | Pending — startup passed; logs contain many loot-table parse errors. Drop behavior remains open. |

## C. Building, food, storage, world generation and exploration

| Mod / version | Functional checks to complete | Status |
|---|---|---|
| Chipped 4.0.2 | Use workstations on vanilla/modded wood and stone; craft several variants, place/break them and verify drops/models. | Pending |
| Farmer's Delight 1.3.4 | Run a food chain: ingredients, cutting-board processing, cooking pot, finished meal and food effects; test container interactions. | Pending |
| Mama's Herbs and Harvest 1.21.1-24 | Plant/harvest representative crops and herbs; test growth stages, drops, food/processing recipes and Botany Pots integration. | Pending |
| Botany Pots 21.1.44 | Plant vanilla, BYG/RU and Herbs & Harvest crops; test growth/harvest, drops, hopper input/output automation and JEI. | Pending |
| Construction Sticks 1.5.0 | Place a small wall/floor pattern; verify direction, range, item use, limits, claim protection and stop/undo behavior. | Pending |
| Every Compat 2.11.56 | Test Chipped Carpenter's Table variants for several modded woods plus supported Create/Farmer's Delight/RU compat; verify recipes, models, drops and client/server registry sync. | Partial — Carpenter's Table variants and stone table user-reported working; duplicate Golden Cherry Leaves registration and large block footprint remain. |
| Lootr 1.11.38.127 | Have two players open the same generated Lootr chest; verify independent personal loot, container persistence and multiplayer synchronization. | Partial — chest opening and loot presence user-confirmed; second-player personal loot unverified. |
| Sophisticated Backpacks 3.26.19 | Craft/open backpack; test storage, upgrades, filters/automation, pickup and save/relog persistence. | Pending |
| Sophisticated Backpacks Create Integration 0.2.3 | Test supported Create inventory/item transport with backpack; verify insertion/extraction and normal backpack behavior. | Pending |
| Sophisticated Air Tank 1.0.1-beta | Equip/refill air tank; test air supply/consumption, capacity indicator and supported backpack/Curios interactions. | Pending |
| Oh The Biomes We've Gone 2.6.3 | Fresh disposable Overworld: verify representative BYG biomes, vegetation/trees, structures and biome-specific terrain; check configs/datapacks. | Pending |
| Regions Unexplored 0.6.3 | Fresh disposable Overworld: verify representative RU biomes, vegetation, trees and biome blocks; check biome edges and Create integration. | Pending |
| Oh The Trees You'll Grow 5.3.5 | Grow representative added trees; test sapling growth, leaves/log drops, wood sets and leaves decay. | Pending |
| Atmosphere 1.0.18 | Fresh disposable world: verify its advertised environment/atmosphere changes; check day/night, weather, visuals/audio and client/server consistency. | Pending |
| Create Oh The Biomes We've Gone Compatibility 0.0NONE | Check compatibility items/recipes/blocks for BYG and Create; test JEI presence, placement, drops and wood/biome integration. | Pending |
| Nature's Compass 3.4.0 | Search for a known biome in disposable world; verify result, distance/direction, no-result message and repeat search. | Smoke-only — Batch B startup/login passed; actual search behavior not tested. |
| Explorer's Compass 3.4.0 | Search for a known generated structure; verify correct result, distance/direction and updated search after discovery. | Smoke-only — Batch B startup/login passed; actual search behavior not tested. |
| Create Structures Arise 176.49.50 | Fresh disposable Overworld: find multiple Create-themed structures; inspect integrity, loot, biome placement and chunk-edge generation. | Pending |

## D. Player interface, server tools and information mods

| Mod / version | Functional checks to complete | Status |
|---|---|---|
| AppleSkin 3.0.9 | Check hunger, saturation and exhaustion HUD while eating, sprinting and regenerating; compare to expected vanilla values. | Pending |
| FTB Chunks 2101.1.23 | Claim/unclaim test chunk; verify map, team permissions, boundaries, force-load controls, protection and reconnect persistence. | Pending |
| FTB Teams 2101.1.11 | Create team; invite/remove second player; check ownership/permissions and FTB Chunks team-claim behavior. | Pending |
| InControl! 10.3.1 | Test active spawn/loot/experience rules under controlled conditions; verify allowed/blocked mobs/loot and restart persistence. | Pending |
| Jade 15.10.6 | Inspect vanilla/modded blocks and entities; verify tooltips, states, inventories/fluid data and Create/Aeronautics compatibility. | Pending |
| Just Enough Items 19.64.0.455 | Search representative items from each content group; inspect crafting/processing recipes, catalysts and fluid inputs. | Pending |
| Just Enough Resources 1.6.0.57 | Check known mob-drop, loot-table, villager-trade and world-generation entries against in-game sources. | Pending |
| Enchantment Descriptions 21.1.11 | Open tooltips for vanilla/modded enchanted books and items; verify accurate descriptions and layout. | Pending |
| Shulker Box Tooltip 5.1.9+1.21.1 | Hover filled shulkers; verify contents preview, item counts, scroll/page behavior and provider integrations. 31 providers registered is not visual proof. | Pending |
| Mouse Tweaks 2.26.1 | Test drag distribution, wheel scrolling and quick-move in player inventory, chests, backpacks and modded GUIs. | Pending |
| Memory Settings 6.0 | Verify settings apply and persist across restart; measure memory only in controlled same-workload comparison, not from startup alone. | Pending |
| ModernFix 5.27.27 | Verify selected optimization mixins/options on the same disposable test profile; review for mixin errors, changed gameplay behavior, save integrity and comparable startup/runtime metrics. | Pending |

## E. Client graphics and performance mods

| Mod / version | Functional checks to complete | Status |
|---|---|---|
| Sodium 0.8.13 (client-only) | Launch matching client; verify rendering of chunks, Create moving contraptions, Aeronautics ships and block entities; compare same-scene FPS/frame pacing. | Pending |
| Iris 1.8.14-beta.1 (client-only) | Toggle shader pack; inspect Create/Aeronautics models, ship sublevels, water, particles, HUD and shadows. Record known Aeronautics/Iris visual artifacts. | Pending |
| Sodium Extra 0.9.5 (client-only) | Change a Sodium Extra option; verify it applies, persists after restart and does not conflict with Iris/Sodium. | Pending |
| ImmediatelyFast 1.6.15 (client-only) | Compare identical GUI, HUD, particles, item/entity and block-entity scenes enabled/disabled; check visual parity and client log. | Pending |
| Flerovium 1.1.3 Beta (client-only; detected build) | Compare item, particle and entity rendering/FPS against same Sodium baseline; inspect artifacts. Stable 1.1.2 remains a separate planned candidate. | Pending |
| Entity Culling 1.10.4 (client-only) | Check culling of Create contraptions, Aeronautics ships/sublevels, entities and block entities; hidden objects must reappear when visible. | Pending |
| More Culling 1.0.11 (client-only) | Check leaves, glass, connected textures and modded blocks across chunk boundaries; ensure no missing faces/transparency errors. Test Cloth Config options. | Pending |
| spark 1.10.124 (server profiler) | Record spark-only baseline: TPS, MSPT, memory/GC, CPU under repeatable load and a saved 2–5 minute profile; note Windows Java-engine fallback. | Partial — profiler initialized; no numeric baseline or saved report captured. |

## F. Libraries, APIs and shared support components

| Mod / version | Functional checks to complete | Status |
|---|---|---|
| Apollib 1.2.0 | Verify dependent mod registries/content and related GUI/network interaction; record owner mod. | Pending |
| Architectury 13.0.11 | Verify dependent mods initialize on client/server and shared event/network hooks work during login and interaction. | Pending |
| Athena 4.0.6 | Verify dependent content models/textures render; check for missing model/texture errors. | Pending |
| Azimuth 1.4.10 | Verify mods depending on Azimuth load and shared utility/render behavior works; check class-loading logs. | Pending |
| Bookshelf 21.1.81 | Verify dependent features (e.g. Enchantment Descriptions/Botany Pots) load and work; dependency-only. | Pending |
| Cloth Config API 15.0.140 | Open More Culling config; change/save option, relaunch and verify persistence. | Pending |
| CodecUI 1.4.7 | Open dependent settings/config interface; verify widgets, values and save/cancel behavior. | Pending |
| Conditional Mixin 0.6.4 | Verify dependent mixins activate under intended mod/config conditions; check mixin apply failures. | Pending |
| CorgiLib 5.0.0.10 | Verify dependent mod initializes and required shared utilities work; check missing-class/registration errors. | Pending |
| Cupboard 4.2 | Verify Memory Settings and other dependent config integrations initialize and read/write settings. | Pending |
| Curios API 9.5.1 | Verify slot registry, counts, equip/unequip, client/server sync and persistence with Aeronautics/Backtank. | Partial — two Back + one Head slot and selected item uses were reported in new-world checks; full sync/older-player data still open. |
| DragonLib 3.0.29 | Verify dependent DragonLib consumers (including Pantographs & Wires) register, render and execute their behavior. | Pending |
| Ferrite Core 7.0.3 | Capture memory baseline and compare same workload in disposable clone; check startup/registry stability. Do not alter production based only on benchmark. | Pending |
| Flywheel 1.0.6 | Verify Create contraption rendering, instancing, moving block entities and animation on matching client. | Pending |
| Forge Config API Port 21.1.1 | Open dependent mod config GUI, change value, save/restart and verify persistence. | Pending |
| Forgified Fabric API Base 0.4.42 | Verify bundled/using mods load and required API calls work; dependency-only. | Pending |
| Forgified Fabric BlockView API 1.0.10 | Verify renderer/block-view integration used by Flerovium loads and block rendering stays correct. | Pending |
| Forgified Fabric Renderer API 3.4.1 | Verify renderer-dependent mod integration and item/block rendering; dependency-only. | Pending |
| Forgified Fabric Rendering Data Attachment 0.3.48 | Verify renderer data attachments survive chunk/entity render updates without visual corruption. | Pending |
| FTB Library 2101.1.39 | Verify FTB Chunks/Teams menus, shared data, keybinds and networking; dependency-only. | Pending |
| FTB XMod Compat 21.1.14 | Verify selected team/stage/permission integration is detected and behaves correctly. | Pending |
| Gadgets & Gizmos Library 1.2.10 | Verify bundled G&G content registers and dependent contraption controller/graph utilities work. | Pending |
| GeckoLib 4 4.9.3 | Verify animated entities/blocks and Aeronautics Structures visuals animate correctly on client. | Pending |
| Kotlin for Forge 5.12.0 | Verify Kotlin-based dependent mods initialize and execute entry points; dependency-only. | Pending |
| Lithostitched 1.8.1 | Verify BYG/RU biome and feature registration in fresh disposable Overworld; check registry conflicts. Preserve production worldgen. | Pending |
| MezzConfig 0.6.10 | Verify config interface opens and dependent config screens load/save; standalone and bundled copies must not duplicate. | Pending |
| Moonlight Lib 3.8.1 | Verify dependent features (including Every Compat) register resources/models without duplicate registry errors. | Pending |
| Ponder 1.0.82 | Open Ponder scenes for representative Create/addon blocks; confirm scenes render and advance. | Pending |
| PrickleMC 21.1.11 | Verify Botany Pots dependency/plugin initialization and crop/soil compatibility; dependency-only otherwise. | Pending |
| Resourceful Lib 3.0.12 | Verify dependent resource registries/config/content load; check missing resource errors. | Pending |
| Ritchie's Projectile Library 2.1.2 | Verify through Create Big Cannons: projectile and fuze definitions register, load and fire correctly; confirm client/server projectile synchronization. | Pending |
| Sable Companion 1.6.0 | Verify dependent Sable integrations load and register expected physics behavior; no separate feature assumed. | Pending |
| Sophisticated Core 1.5.23 | Verify backpack upgrade/inventory modules initialize and retain data after close/reopen, relog and restart. | Pending |
| TerraBlender 4.1.0.8 | Verify BYG/RU biome providers register in intended dimensions of fresh disposable world; no missing/duplicate regions. | Pending |
| TRansition 1.0.21 | Verify Entity Culling transition/render hooks when entities/block entities enter/leave view. | Pending |
| TRender 1.0.15 | Verify dependent render integration and UI/model path; no missing renderer/client crash. | Pending |
| Veil 4.3.2 | Verify Veil-dependent rendering/effects initialize on client and remain correct with Sodium/Iris. | Pending |

## Global functional-test completion gate

- [ ] Every feature/content mod above has a recorded function result (Pass, Partial, Failed or Blocked); no feature row may be assumed complete from smoke testing.
- [ ] Every distinct primary subsystem within multi-feature mods has been checked.
- [ ] Client-only functions have matching client test evidence.
- [ ] World-generation and structure mods have fresh disposable-world evidence.
- [ ] Multiplayer, persistence, inventory, transport and permission features have relevant second-player/restart checks.
- [ ] Partial/Blocked/Failed entries have a short issue note and next action.
- [ ] Library/API checks link to the dependent mod test that exercises them.
- [ ] Final client and dedicated-server inventories are reconciled before release.

## Notes on the inventory snapshot

- The 5 November server log contains the server's loaded mod list, including dependencies and bundled/nested components. Bundled Aeronautics and Gadgets & Gizmos modules are listed once by feature rather than duplicated as separate installations.
- Sodium, Iris and Sodium Extra are client-only entries from the reviewed client inventory and are not expected in the dedicated-server list.
- Batch E detected Flerovium 1.1.3 Beta; the earlier plan called for stable 1.1.2. Record the selected file before closing that row.
- This checklist does not authorize installing, removing, updating or approving any mod. Test candidates remain test-only until the maintainer approves them.
