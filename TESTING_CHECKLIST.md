# Testing order for beta candidates

- Test server-only mods first, then shared client/server mods, and client-only mods last.
- Complete pending server-side and shared candidates before starting client-only candidates, unless the maintainer explicitly defers, holds, or rejects a specific candidate.
- Split mixed batches by side. Keep client-only JARs out of the dedicated-server mods folder.
- Test client-only mods one at a time on the matching client after the server/shared queue is complete.
- **spark profiling is deferred to beta testers.** It is not an internal development prerequisite; beta testers may capture performance baselines during the beta phase.

# Full Installed-Mod Functional Testing Checklist

**Last updated:** 5 November 2026  
**Target:** Minecraft 1.21.1 · NeoForge 21.1.265 · Java 21  
**Approved download source:** CurseForge only

This is the full functional-test matrix for the recorded Create IronWoven test installation. It currently tracks 123 feature and support-module entries. It covers more than the active batch queue. The inventory basis is the 5 November dedicated-server mod list plus the client-only entries in the latest reviewed client inventory. This is a test snapshot, not a final release manifest.

**How to use the checklist:** each `[ ]` is an individual action. Tick it only after that exact behavior has been tested on the intended client/server side and the result is recorded. A mod can remain **Partial** while some boxes are checked and others are open. Keep smoke-test evidence separate from feature tests.

## Smoke test is not a function test

The 5 November combined test reached Done (1.718s), loaded world_lootr_test, accepted a client login and shut down cleanly. A later 14:09 update-trial run also completed Done (1.822s), disposable-world load, matching client login and clean shutdown. Batches A, B and C also passed their recorded pack-level startup/login smoke tests. This proves the combined test profile can load and join; **it does not prove every installed mod's functions work**.

- **Smoke test:** mod discovery, server/client startup as appropriate, world load, login, shutdown and log review.
- **Function test:** exercise the actual feature(s) that justify keeping the mod: item/block interaction, machine process, transport, GUI, world generation, rendering, recipe/loot behavior or synchronization.
- A combined smoke-test pass is not an individual mod-function pass. Do not mark a feature complete just because its mod ID appears in a server log.
- Client-only mods require a matching client launch and client-side review. A dedicated-server log cannot prove their client functions.
- Libraries/APIs are tested through the mod(s) that depend on them; they do not need invented standalone gameplay tests.

## Current pack-level smoke evidence

| Check | Evidence | Status |
|---|---|---|
| Dedicated-server startup | 5 Nov logs reached Done (1.718s) and Done (1.822s) | PASS — combined disposable profiles |
| Disposable world load | world_lootr_test loaded in both runs | PASS |
| Matching client login | One matching client joined in both runs | PASS |
| Clean shutdown | All dimensions saved in both runs | PASS |
| Individual feature tests | Matrix below | OPEN — mostly not yet function-tested |
| Matching client-only mod startup | No isolated client log for the 14:09 test folder supplied | OPEN |
| Production/release approval | Not granted | NOT APPROVED |


## Existing-mod update trial — 5 November 2026, 13:43

**Result: FAILED before server startup completed.** This was a separate disposable-server update attempt, not a replacement for the earlier successful combined smoke test.

| Mod | Version detected | Result |
|---|---:|---|
| Sophisticated Core | 1.5.28.2458 | Detected |
| Sophisticated Backpacks | 3.26.20.2244 | Detected |
| Entity Culling | 1.11.3 | Detected in the server folder; client-only |
| Create Crafts & Additions | 1.7.2 | Detected |
| Create: Numismatics | 1.1.0 | Dependency conflict with Numismatics Plus 1.0.1 |
| Create: TFMG Community Edition | 1.3.3 | Detected |
| FTB Teams | Missing | Required by FTB Chunks 2101.1.23 |
| Create: Steam 'n' Rails | 0.3.0-alpha.2 | Beta 2 was not present in this test |

### Startup blockers

- **FTB Teams missing:** FTB Chunks 2101.1.23 requires FTB Teams 2101.1.9 or newer. CurseForge NeoForge 1.21.1 release 2101.1.12 is available as [file 9434081](https://www.curseforge.com/minecraft/mc-mods/ftb-teams-forge/files/9434081).
- **Numismatics mismatch:** Numismatics Plus 1.0.1 requires exactly Numismatics 1.0.20. Restore [Numismatics 1.0.20, CurseForge file 7948018](https://www.curseforge.com/minecraft/mc-mods/numismatics/files/7948018) for the next test, retaining [Numismatics Plus 1.0.1, file 8839718](https://www.curseforge.com/minecraft/mc-mods/create-numismatics-plus/files/8839718).

The server did not reach `Done`, load a world, accept a client, or complete a normal shutdown. ImmediatelyFast, Flerovium, Entity Culling, and More Culling were also detected in the dedicated-server folder; these rendering mods belong on the client and need separate client testing.

**Next gate:** restore the Numismatics dependency pair, add FTB Teams to matching client/server profiles, remove client-only rendering mods from the server folder, then retry the disposable-server smoke test. No update from this attempt is approved for release.


## Previous existing-mod update retry — 5 November 2026, 13:58 (historical)

**Result: Partial server startup/world-load pass.** The retry used a disposable server. FTB Teams 2101.1.12 was detected and initialized, and the server reached `Done (1.493s)!` after preparing `world_lootr_test`. The supplied server/debug logs do not show a matching client login or a clean shutdown.

| Mod | Detected version | Result |
|---|---:|---|
| Sophisticated Core | 1.5.28.2458 | Detected |
| Sophisticated Backpacks | 3.26.20.2244 | Detected |
| Entity Culling | 1.11.3 | Client-only; still present in server folder |
| Create Crafts & Additions | 1.7.2 | Detected |
| Create: The Factory Must Grow Community Edition | 1.3.3 | Detected |
| FTB Teams | 2101.1.12 | Detected and initialized |
| Create: Numismatics | 1.0.20 and 1.1.0 JARs found; 1.1.0 selected | 1.0.20 was not active in this run |
| Numismatics Plus | Not present in runtime list | Compatibility not tested |
| Create: Steam 'n' Rails | 0.3.0-alpha.2 | Beta 2 not tested |

Do not keep both Numismatics versions in one `mods` folder. Test Numismatics Plus 1.0.1 with Numismatics 1.0.20 only. Test Numismatics 1.1.0 separately without Plus until a compatible Plus release is verified.

ImmediatelyFast, Flerovium, Entity Culling, and More Culling are client-only and must be tested on the matching client, not in the dedicated-server folder. The server log contains 463 ERROR-level entries, mostly recurring Design n' Decor / Steam 'n' Rails loot-table parsing entries, plus the already tracked Sable, Struts, PowerGrid, Every Compat and Create Deco findings. Verify the world-scoped compatibility datapacks in the disposable world before assigning the recurring entries to a mod regression.

**Next gate at the time of this retry:** use one Numismatics version per profile; include Numismatics Plus only with 1.0.20; keep client-only rendering mods out of the server; then provide client login and clean-shutdown evidence. The 14:09 follow-up below completed the routine smoke sequence; the correct Numismatics pair, isolated client tests, and performance baseline remain open. This retry itself was not a complete smoke-test pass or release approval.


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

### Create 6.0.10
**Current status:** Pending
- [ ] Build a kinetic network.
- [ ] Test speed/rotation control, one press/mixer/deployer chain, item/fluid transport and save/restart.

### Create Aeronautics 1.3.2
**Current status:** Pending
- [ ] Assemble a vehicle.
- [ ] Test propulsion/lift, steering, controls, collision/physics, disassembly/reassembly and second-player sync.

### Create: Simulated 1.3.2
**Current status:** Pending
- [ ] Test assembly/disassembly, anchoring, controls, redstone interaction, collision and save/reload.

### Create: Offroad 1.3.2
**Current status:** Pending
- [ ] Build a wheeled vehicle.
- [ ] Test wheel power, steering, traction, stopping, collision and multiplayer sync.

### Create Kinetic 1.4.3
**Current status:** Pending
- [ ] Test its Aeronautics utility/propulsion blocks and items.
- [ ] Verify hitboxes, particles, controls and physics on client/server. Recheck existing loot-table and mixin findings.

### Create Aeronautics Structures 1.1.0-Beta-3.1 (test-only)
**Current status:** Partial — server smoke passed; generation unproven; one loot-table parse error remains.
- [ ] Fresh disposable Overworld: confirm engineering houses, abandoned boats, airships and hot-air balloons generate.
- [ ] Test engineer trader and chest loot.
- [ ] Recheck cr_aero_structures:chests/uniform.

### Create Aeronautics Curios Compat 2.0
**Current status:** Partial — assigned-slot checks user-reported working; repeatable synced test still needed.
- [ ] Equip Aviator Goggles in Head slot.
- [ ] Test overlay/engineer detection. Equip Linked Typewriter in Curios and activate (default Y) to operate linked typewriter/Redstone Links.

### Create Aeronautics: Copycat Wing 1.0.4
**Current status:** Pending
- [ ] Use a Copycats+ block as a wing part.
- [ ] Verify lift. Honeycomb should disable lift and axe restore it.
- [ ] Test on a moving contraption.

### Create Aeronautics: Transmission & Linkage 0.2.9
**Current status:** Pending
- [ ] Build a transmission/linkage assembly.
- [ ] Verify it transfers the intended movement/control across running and assembled contraptions.

### Create Big Cannons 5.11.7
**Current status:** Pending
- [ ] Assemble a multiblock cannon.
- [ ] Load projectiles/fuzes.
- [ ] Test Create-powered loading/aiming, firing, projectile effect/recoil, reload and autocannon if used.

### Create: Steam 'n' Rails 0.3.0-alpha.2
**Current status:** Pending
- [ ] Assemble/run a train.
- [ ] Test tracks, bogeys, schedules/stations, signals and installed railway interactions.
- [ ] Verify save/restart.

### Create: Blocks & Bogies 1.0.8
**Current status:** Pending
- [ ] Open bogie UI (crouch + right-click empty-handed)
- [ ] Configure drivers/axles, assemble train and verify style and operation.

### Create: Modern Train Parts 0.2.5
**Current status:** Pending
- [ ] Test pantograph deployment/retraction, shipping-container storage, wrench variants and train movement with parts attached.

### Create: Pantographs & Wires 0.2.3-C6 Beta
**Current status:** Pending
- [ ] Place masts/cantilevers and catenary.
- [ ] Verify wire connection and pantograph height adjustment on a moving train, including slopes/turns.

### Create: Rustic Structures 1.0.1
**Current status:** Pending
- [ ] Fresh disposable Overworld: find well, smithy, windmill and barn in intended biome groups.
- [ ] Inspect placement, loot and generation.

### Create: Structures Arise 176.49.50
**Current status:** Pending
- [ ] Fresh disposable Overworld: find multiple Create-themed structures.
- [ ] Inspect integrity, placement, loot and chunk-edge generation.

### Create: Aeronautical Diesel 1.1.0
**Current status:** Pending
- [ ] Use tank/fill port to move diesel, biodiesel, gasoline, ethanol, crude oil or plant oil into an Aeronautics portable engine.
- [ ] Test wrench and automation.

### Create: AeroPortals 1.3.6
**Current status:** Pending
- [ ] Move a complete airship through vanilla and supported modded portals.
- [ ] Verify ship, pilot, passengers and decorations arrive intact.

### Shield Generators 1.4.0
**Current status:** Pending
- [ ] Power a shield generator.
- [ ] Test activation, energy draw, boundary visualization, protection/interaction and multiplayer consistency.

### KineticGrip 1.0.5
**Current status:** Pending
- [ ] Test the Aeronautics handles from the player point of view.
- [ ] Operate the handle controls and any player-usable tool (such as the chainsaw) included by the installed build. Verify movement/control and client/server interaction.

### Sable 2.0.6
**Current status:** Pending
- [ ] Test Aeronautics physics: assembly, motion, forces, collision, sublevels and save/restart.
- [ ] Inspect Copycats Catwalk physics-tag errors.

### Strut Your Stuff 1.3.1
**Current status:** Pending — shared library; dependent integration and server-side issue remain open.
- [ ] Validate through dependent mods: spanning/collision structures, surface clipping, interaction and cable behavior/droop.
- [ ] Check dedicated-server RenderSystem class-loading issue.

## B. Create automation, energy, industry and build addons

### Create: Bits 'n' Bobs 2.3.5
**Current status:** Pending
- [ ] Test chain-drive transfer/carriage attachment, flywheel bearing rotation/battery behavior, wooden cogwheel swapping, dyeable fluid-pipe separation, chair and Nixie display.

### Create Cobblestone 1.5.1
**Current status:** Pending
- [ ] Set generator to cobblestone, stone, basalt, limestone and scoria.
- [ ] Verify outputs, type switching, SU use and disabled-generator behavior.

### Create Crafts & Additions 1.6.0
**Current status:** Pending
- [ ] Run Electric Motor from FE and verify SU output.
- [ ] Drive Alternator with SU and verify FE output.
- [ ] Test rolling-mill rods/wires.

### Create: Curios Backtank 1.0.2
**Current status:** Partial — Backpack + standard Backtank use in configured Back slots was reported; refill/consumption still open.
- [ ] Equip Backtank with intended Curios/backpack setup.
- [ ] Test air capacity, refill, consumption and rendering/slot behavior.

### Create Deco 2.1.3
**Current status:** Pending
- [ ] Test decorative blocks/variants, recipes, placement, rotation and drops.
- [ ] Recheck placard fix and loot-table parsing.

### Create: Diesel Generators 1.3.15
**Current status:** Pending
- [ ] Run an oil-to-fuel chain.
- [ ] Start diesel generator and test FE output, fuel consumption, upgrades and a representative machine/tool.

### Create Encased 1.10.0-fix1
**Current status:** Pending
- [ ] Apply casings to shafts, cogwheels and pipes.
- [ ] Test rotation, power/fluid transfer and persistent casing visuals.

### Create: Gadgets & Gizmos 1.2.10 (bundled)
**Current status:** Pending
- [ ] Test installed gadgets/engine components used by Aeronautics: assembly, thrust/control, fuel/power consumption and contraption synchronization.

### Create: Dragons Plus 1.11.9
**Current status:** Pending
- [ ] Use an Encased Fan to test Bulk Coloring with dye fluid, Bulk Freezing with Powder Snow, Bulk Ending with Dragon Head or Dragon's Breath fluid, and Bulk Sanding with Quicksand/supported block tag. Test Fluid Hatch take/deposit behavior on tanks and supported addon recipe integrations.

### Create: Liquid Fuel 3.0.0
**Current status:** Pending
- [ ] Feed supported liquid fuel to a Blaze Burner.
- [ ] Verify normal/superheated operation, duration, consumption and rejection of invalid fluids.

### Create: Fluids Be Gone! 1.0.1
**Current status:** Pending
- [ ] Run a Create Drill and a Simulated Rock Cutting Wheel into fluid-containing terrain.
- [ ] Verify fluids in the mined path are voided when enabled, separate drill/rock-wheel config switches work, and fluids outside the mining path remain unchanged.

### Create: Framed 1.8.2
**Current status:** Pending
- [ ] Build framed blocks, apply a supported material/appearance and shape.
- [ ] Verify placement, rotation, breaking and reload.

### Create: Enchantment Industry 2.5.4b
**Current status:** Pending
- [ ] Run automated enchanting/disenchanting and XP-fluid processing.
- [ ] Verify inputs, outputs, XP/fluid handling, recipes and automation.

### Create: Numismatics 1.0.20
**Current status:** Pending
- [ ] Obtain coins.
- [ ] Use Vendor for buy/sell, Bank Terminal for deposit/withdraw, and Depositor price/redstone pulse for coin/card payments.

### Create: Numismatics Plus 1.0.1
**Current status:** Pending
- [ ] Buy from a Create shop with coins and a Numismatics card.
- [ ] Verify deduction, stock, recipient account and missing-Depositor/card behavior.

### Create: Pattern Schematics 2.0.10
**Current status:** Pending
- [ ] Create/obtain a repeating schematic.
- [ ] Print in creative or use Schematicannon.
- [ ] Verify placement, orientation, repeat behavior and resource requirements.

### Create: Power Grid 0.6.2
**Current status:** Partial — server loads; optional native solver unavailable in tested Windows environment; fallback function not yet verified.
- [ ] Build a small electrical network with source, wires, transformer and consumers.
- [ ] Test components and fallback solver.
- [ ] Record native solver separately.

### Create: Sound of Steam / Pipe Organs 0.9.2.1
**Current status:** Pending
- [ ] Place/configure a pipe organ.
- [ ] Trigger notes manually and by supported controls/redstone.
- [ ] Test pitch, sound, range, persistence and multiplayer audio.

### Create: The Factory Must Grow 1.3.2a-community
**Current status:** Pending
- [ ] Run representative industrial processing: fluid/oil input, machine processing, outputs, power/kinetic requirements and fuel-burning machine.
- [ ] Test Unified Fuels integration.

### Create: Unified Fuels 1.0.4
**Current status:** Pending
- [ ] Cross-feed fuels between supported addons and compatible engines, burners and trains.
- [ ] Verify shared values/consumption, gas-vs-liquid rules, toggles and config after restart.

### Create: Vibrant Vaults 0.3.2
**Current status:** Pending
- [ ] Build/connect vaults and shipping containers.
- [ ] Insert/extract items, change color/orientation and test package frogport/stock link/packager features present.

### Create Slice & Dice 4.3.4
**Current status:** Pending
- [ ] Automate a Farmer's Delight cutting-board recipe with Create saw.
- [ ] Verify ingredients, output, transport and recipe visibility.

### Create: Bells & Whistles 0.4.7
**Current status:** Pending
- [ ] Test representative decorative train/building blocks, variants, placement, rotation, collision and rendering on moving contraptions.

### Create: Copycats+ 3.0.9
**Current status:** Pending
- [ ] Use copycat shapes with multiple source materials.
- [ ] Verify appearance, shape/state, rotation and moving-contraption rendering.

### Copycats+ Additions 1.5.0
**Current status:** Pending
- [ ] Test added copycat shapes/variants, material application and placement.
- [ ] Verify Aeronautics Copycat Wing integration.

### Design n' Decor 2.2b
**Current status:** Pending — startup passed; logs contain many loot-table parse errors. Drop behavior remains open.
- [ ] Test representative decoration families, recipes and drops.
- [ ] Specifically verify dyed cogwheel/loot-table entries and intended block drops.

## C. Building, food, storage, world generation and exploration

### Chipped 4.0.2
**Current status:** Pending
- [ ] Use workstations on vanilla/modded wood and stone.
- [ ] Craft several variants, place/break them and verify drops/models.

### Farmer's Delight 1.3.4
**Current status:** Pending
- [ ] Run a food chain: ingredients, cutting-board processing, cooking pot, finished meal and food effects.
- [ ] Test container interactions.

### Mama's Herbs and Harvest 1.21.1-24
**Current status:** Pending
- [ ] Plant/harvest representative crops and herbs.
- [ ] Test growth stages, drops, food/processing recipes and Botany Pots integration.

### Botany Pots 21.1.44
**Current status:** Pending
- [ ] Plant vanilla, BYG/RU and Herbs & Harvest crops.
- [ ] Test growth/harvest, drops, hopper input/output automation and JEI.

### Construction Sticks 1.5.0
**Current status:** Pending
- [ ] Place a small wall/floor pattern.
- [ ] Verify direction, range, item use, limits, claim protection and stop/undo behavior.

### Every Compat 2.11.56
**Current status:** Partial — Carpenter's Table variants and stone table user-reported working; duplicate Golden Cherry Leaves registration and large block footprint remain.
- [ ] Test Chipped Carpenter's Table variants for several modded woods plus supported Create/Farmer's Delight/RU compat.
- [ ] Verify recipes, models, drops and client/server registry sync.

### Lootr 1.11.38.127
**Current status:** Partial — chest opening and loot presence user-confirmed; second-player personal loot unverified.
- [ ] Have two players open the same generated Lootr chest.
- [ ] Verify independent personal loot, container persistence and multiplayer synchronization.

### Sophisticated Backpacks 3.26.19
**Current status:** Pending
- [ ] Craft/open backpack.
- [ ] Test storage, upgrades, filters/automation, pickup and save/relog persistence.

### Sophisticated Backpacks Create Integration 0.2.3
**Current status:** Pending
- [ ] Test supported Create inventory/item transport with backpack.
- [ ] Verify insertion/extraction and normal backpack behavior.

### Sophisticated Air Tank 1.0.1-beta
**Current status:** Pending
- [ ] Equip/refill air tank.
- [ ] Test air supply/consumption, capacity indicator and supported backpack/Curios interactions.

### Oh The Biomes We've Gone 2.6.3
**Current status:** Pending
- [ ] Fresh disposable Overworld: verify representative BYG biomes, vegetation/trees, structures and biome-specific terrain.
- [ ] Check configs/datapacks.

### Regions Unexplored 0.6.3
**Current status:** Pending
- [ ] Fresh disposable Overworld: verify representative RU biomes, vegetation, trees and biome blocks.
- [ ] Check biome edges and Create integration.

### Oh The Trees You'll Grow 5.3.5
**Current status:** Pending
- [ ] Grow representative added trees.
- [ ] Test sapling growth, leaves/log drops, wood sets and leaves decay.

### Atmosphere 1.0.18
**Current status:** Pending
- [ ] Fresh disposable world: verify its advertised environment/atmosphere changes.
- [ ] Check day/night, weather, visuals/audio and client/server consistency.

### Create Oh The Biomes We've Gone Compatibility 0.0NONE
**Current status:** Pending
- [ ] Check compatibility items/recipes/blocks for BYG and Create.
- [ ] Test JEI presence, placement, drops and wood/biome integration.

### Nature's Compass 3.4.0
**Current status:** Smoke-only — Batch B startup/login passed; actual search behavior not tested.
- [ ] Search for a known biome in disposable world.
- [ ] Verify result, distance/direction, no-result message and repeat search.

### Explorer's Compass 3.4.0
**Current status:** Smoke-only — Batch B startup/login passed; actual search behavior not tested.
- [ ] Search for a known generated structure.
- [ ] Verify correct result, distance/direction and updated search after discovery.

### Create Structures Arise 176.49.50
**Current status:** Pending
- [ ] Fresh disposable Overworld: find multiple Create-themed structures.
- [ ] Inspect integrity, loot, biome placement and chunk-edge generation.

## D. Player interface, server tools and information mods

### AppleSkin 3.0.9
**Current status:** Pending
- [ ] Check hunger, saturation and exhaustion HUD while eating, sprinting and regenerating.
- [ ] Compare to expected vanilla values.

### FTB Chunks 2101.1.23
**Current status:** Pending
- [ ] Claim/unclaim test chunk.
- [ ] Verify map, team permissions, boundaries, force-load controls, protection and reconnect persistence.

### FTB Teams 2101.1.11
**Current status:** Pending
- [ ] Create team.
- [ ] Invite/remove second player.
- [ ] Check ownership/permissions and FTB Chunks team-claim behavior.

### InControl! 10.3.1
**Current status:** Pending
- [ ] Test active spawn/loot/experience rules under controlled conditions.
- [ ] Verify allowed/blocked mobs/loot and restart persistence.

### Jade 15.10.6
**Current status:** Pending
- [ ] Inspect vanilla/modded blocks and entities.
- [ ] Verify tooltips, states, inventories/fluid data and Create/Aeronautics compatibility.

### Just Enough Items 19.64.0.455
**Current status:** Pending
- [ ] Search representative items from each content group.
- [ ] Inspect crafting/processing recipes, catalysts and fluid inputs.

### Just Enough Resources 1.6.0.57
**Current status:** Pending
- [ ] Check known mob-drop, loot-table, villager-trade and world-generation entries against in-game sources.

### Enchantment Descriptions 21.1.11
**Current status:** Pending
- [ ] Open tooltips for vanilla/modded enchanted books and items.
- [ ] Verify accurate descriptions and layout.

### Shulker Box Tooltip 5.1.9+1.21.1
**Current status:** Pending
- [ ] Hover filled shulkers.
- [ ] Verify contents preview, item counts, scroll/page behavior and provider integrations. 31 providers registered is not visual proof.

### Mouse Tweaks 2.26.1
**Current status:** Pending
- [ ] Test drag distribution, wheel scrolling and quick-move in player inventory, chests, backpacks and modded GUIs.

### Memory Settings 6.0
**Current status:** Pending
- [ ] Verify settings apply and persist across restart.
- [ ] Measure memory only in controlled same-workload comparison, not from startup alone.

### ModernFix 5.27.27
**Current status:** Pending
- [ ] Verify selected optimization mixins/options on the same disposable test profile.
- [ ] Review for mixin errors, changed gameplay behavior, save integrity and comparable startup/runtime metrics.

## E. Client graphics and performance mods

### Sodium 0.8.13 (client-only)
**Current status:** Pending
- [ ] Launch matching client.
- [ ] Verify rendering of chunks, Create moving contraptions, Aeronautics ships and block entities.
- [ ] Compare same-scene FPS/frame pacing.

### Iris 1.8.14-beta.1 (client-only)
**Current status:** Pending
- [ ] Toggle shader pack.
- [ ] Inspect Create/Aeronautics models, ship sublevels, water, particles, HUD and shadows. Record known Aeronautics/Iris visual artifacts.

### Sodium Extra 0.9.5 (client-only)
**Current status:** Pending
- [ ] Change a Sodium Extra option.
- [ ] Verify it applies, persists after restart and does not conflict with Iris/Sodium.

### ImmediatelyFast 1.6.15 (client-only)
**Current status:** Pending
- [ ] Compare identical GUI, HUD, particles, item/entity and block-entity scenes enabled/disabled.
- [ ] Check visual parity and client log.

### Flerovium 1.1.3 Beta (client-only; detected build)
**Current status:** Pending
- [ ] Compare item, particle and entity rendering/FPS against same Sodium baseline.
- [ ] Inspect artifacts. Stable 1.1.2 remains a separate planned candidate.

### Entity Culling 1.10.4 (client-only)
**Current status:** Pending
- [ ] Check culling of Create contraptions, Aeronautics ships/sublevels, entities and block entities.
- [ ] Hidden objects must reappear when visible.

### More Culling 1.0.11 (client-only)
**Current status:** Pending
- [ ] Check leaves, glass, connected textures and modded blocks across chunk boundaries.
- [ ] Ensure no missing faces/transparency errors. Test Cloth Config options.

### spark 1.10.124 (server profiler)
**Current status:** Deferred to beta testers — not required during internal development.
- [ ] During beta testing, record TPS, MSPT, memory/GC, and CPU under a repeatable load; save a 2–5 minute profile.
- [ ] Record the selected profiler engine and any platform-specific fallback.

## F. Libraries, APIs and shared support components

### Apollib 1.2.0
**Current status:** Pending
- [ ] Verify dependent mod registries/content and related GUI/network interaction.
- [ ] Record owner mod.

### Architectury 13.0.11
**Current status:** Pending
- [ ] Verify dependent mods initialize on client/server and shared event/network hooks work during login and interaction.

### Athena 4.0.6
**Current status:** Pending
- [ ] Verify dependent content models/textures render.
- [ ] Check for missing model/texture errors.

### Azimuth 1.4.10
**Current status:** Pending
- [ ] Verify mods depending on Azimuth load and shared utility/render behavior works.
- [ ] Check class-loading logs.

### Bookshelf 21.1.81
**Current status:** Pending
- [ ] Verify dependent features (e.g. Enchantment Descriptions/Botany Pots) load and work.
- [ ] Dependency-only.

### Cloth Config API 15.0.140
**Current status:** Pending
- [ ] Open More Culling config.
- [ ] Change/save option, relaunch and verify persistence.

### CodecUI 1.4.7
**Current status:** Pending
- [ ] Open dependent settings/config interface.
- [ ] Verify widgets, values and save/cancel behavior.

### Conditional Mixin 0.6.4
**Current status:** Pending
- [ ] Verify dependent mixins activate under intended mod/config conditions.
- [ ] Check mixin apply failures.

### CorgiLib 5.0.0.10
**Current status:** Pending
- [ ] Verify dependent mod initializes and required shared utilities work.
- [ ] Check missing-class/registration errors.

### Cupboard 4.2
**Current status:** Pending
- [ ] Verify Memory Settings and other dependent config integrations initialize and read/write settings.

### Curios API 9.5.1
**Current status:** Partial — two Back + one Head slot and selected item uses were reported in new-world checks; full sync/older-player data still open.
- [ ] Verify slot registry, counts, equip/unequip, client/server sync and persistence with Aeronautics/Backtank.

### DragonLib 3.0.29
**Current status:** Pending
- [ ] Verify dependent DragonLib consumers (including Pantographs & Wires) register, render and execute their behavior.

### Ferrite Core 7.0.3
**Current status:** Pending
- [ ] Capture memory baseline and compare same workload in disposable clone.
- [ ] Check startup/registry stability. Do not alter production based only on benchmark.

### Flywheel 1.0.6
**Current status:** Pending
- [ ] Verify Create contraption rendering, instancing, moving block entities and animation on matching client.

### Forge Config API Port 21.1.1
**Current status:** Pending
- [ ] Open dependent mod config GUI, change value, save/restart and verify persistence.

### Forgified Fabric API Base 0.4.42
**Current status:** Pending
- [ ] Verify bundled/using mods load and required API calls work.
- [ ] Dependency-only.

### Forgified Fabric BlockView API 1.0.10
**Current status:** Pending
- [ ] Verify renderer/block-view integration used by Flerovium loads and block rendering stays correct.

### Forgified Fabric Renderer API 3.4.1
**Current status:** Pending
- [ ] Verify renderer-dependent mod integration and item/block rendering.
- [ ] Dependency-only.

### Forgified Fabric Rendering Data Attachment 0.3.48
**Current status:** Pending
- [ ] Verify renderer data attachments survive chunk/entity render updates without visual corruption.

### FTB Library 2101.1.39
**Current status:** Pending
- [ ] Verify FTB Chunks/Teams menus, shared data, keybinds and networking.
- [ ] Dependency-only.

### FTB XMod Compat 21.1.14
**Current status:** Pending
- [ ] Verify selected team/stage/permission integration is detected and behaves correctly.

### Gadgets & Gizmos Library 1.2.10
**Current status:** Pending
- [ ] Verify bundled G&G content registers and dependent contraption controller/graph utilities work.

### GeckoLib 4 4.9.3
**Current status:** Pending
- [ ] Verify animated entities/blocks and Aeronautics Structures visuals animate correctly on client.

### Kotlin for Forge 5.12.0
**Current status:** Pending
- [ ] Verify Kotlin-based dependent mods initialize and execute entry points.
- [ ] Dependency-only.

### Lithostitched 1.8.1
**Current status:** Pending
- [ ] Verify BYG/RU biome and feature registration in fresh disposable Overworld.
- [ ] Check registry conflicts. Preserve production worldgen.

### MezzConfig 0.6.10
**Current status:** Pending
- [ ] Verify config interface opens and dependent config screens load/save.
- [ ] Standalone and bundled copies must not duplicate.

### Moonlight Lib 3.8.1
**Current status:** Pending
- [ ] Verify dependent features (including Every Compat) register resources/models without duplicate registry errors.

### Ponder 1.0.82
**Current status:** Pending
- [ ] Open Ponder scenes for representative Create/addon blocks.
- [ ] Confirm scenes render and advance.

### PrickleMC 21.1.11
**Current status:** Pending
- [ ] Verify Botany Pots dependency/plugin initialization and crop/soil compatibility.
- [ ] Dependency-only otherwise.

### Resourceful Lib 3.0.12
**Current status:** Pending
- [ ] Verify dependent resource registries/config/content load.
- [ ] Check missing resource errors.

### Ritchie's Projectile Library 2.1.2
**Current status:** Pending
- [ ] Verify through Create Big Cannons: projectile and fuze definitions register, load and fire correctly.
- [ ] Confirm client/server projectile synchronization.

### Sable Companion 1.6.0
**Current status:** Pending
- [ ] Verify dependent Sable integrations load and register expected physics behavior.
- [ ] No separate feature assumed.

### Sophisticated Core 1.5.23
**Current status:** Pending
- [ ] Verify backpack upgrade/inventory modules initialize and retain data after close/reopen, relog and restart.

### TerraBlender 4.1.0.8
**Current status:** Pending
- [ ] Verify BYG/RU biome providers register in intended dimensions of fresh disposable world.
- [ ] No missing/duplicate regions.

### TRansition 1.0.21
**Current status:** Pending
- [ ] Verify Entity Culling transition/render hooks when entities/block entities enter/leave view.

### TRender 1.0.15
**Current status:** Pending
- [ ] Verify dependent render integration and UI/model path.
- [ ] No missing renderer/client crash.

### Veil 4.3.2
**Current status:** Pending
- [ ] Verify Veil-dependent rendering/effects initialize on client and remain correct with Sodium/Iris.

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

## Existing-mod update smoke-test pass — 5 November 2026, 14:09

**Result: Full routine smoke-test sequence passed for this combined disposable profile.** The server reached `Done (1.822s)`, loaded the disposable world, accepted a matching client login, and shut down with all dimensions saved. This is not an individual mod-function test, nor release approval.

| Mod / component | Version / result |
|---|---|
| Sophisticated Core | 1.5.28.2458 — detected |
| Sophisticated Backpacks | 3.26.20.2244 — detected |
| Create Crafts & Additions | 1.7.2 — detected |
| Create: The Factory Must Grow Community Edition | 1.3.3 — detected |
| FTB Teams | 2101.1.12 — initialized; missing dependency blocker resolved in this test folder |
| Create: Numismatics | Both 1.0.20 and 1.1.0 JARs were scanned; 1.1.0 was active |
| Numismatics Plus | Absent; compatibility not tested |
| Create: Steam 'n' Rails | 0.3.0-alpha.2; Beta 2 not present |
| ImmediatelyFast / Flerovium / Entity Culling / More Culling | 1.6.15 / 1.1.3 / 1.11.3 / 1.0.11; all client-only and still present in the dedicated-server folder |
| spark | 1.10.124 initialized; built-in Java engine selected on Windows 11 / amd64; no numeric baseline or saved profile |

Do not leave both Numismatics JARs in one test folder. Test Numismatics Plus 1.0.1 with Numismatics 1.0.20 only; test Numismatics 1.1.0 separately without Plus until a compatible Plus release is verified. Move the four client-only rendering mods out of the dedicated-server folder and test them on the matching client, one at a time.

### Error review

The log contains **463 ERROR-level entries and 172 WARN-level entries**. The errors include 454 loot-table parse errors (Design n' Decor 256, Steam 'n' Rails 192, Create Kinetic 5, Create Aeronautics Structures 1), three Sable unknown Catwalk selectors, one Struts dedicated-server `RenderSystem` error, one PowerGrid optional native-backend error, three Every Compat registration/block-count messages, and one Create Deco placard recipe error. Verify relevant world-scoped compatibility datapacks before treating recurring loot-table or Sable errors as regressions. The Aeronautics Structures chest-table issue remains unresolved and Batch D remains partial. The 12,288 MB allocation warning exceeds the pack's stated 8,500 MB recommendation but did not block this run.

spark did not produce TPS/MSPT, CPU, memory/GC measurements, or a saved profiler report. Batch E remains partial. Individual feature tests remain open in the matrix below; no function row is passed by this smoke test.
