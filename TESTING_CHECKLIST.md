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

This is the full functional-test matrix for the recorded Create IronWoven test installation. It currently tracks 124 feature and support-module entries. It covers more than the active batch queue. The inventory basis is the 5 November dedicated-server mod list plus the client-only entries in the latest reviewed client inventory. This is a test snapshot, not a final release manifest.

**How to use the checklist:** each `[ ]` is an individual action. Tick it only after that exact behavior has been tested on the intended client/server side and the result is recorded. For every mod entry, complete the **Tester name** and **Test date** fields below its status before marking any function checkbox complete. A checkbox must never be marked complete without an identifiable tester and recorded result/evidence. If different people test different functions within one mod, identify the tester beside the relevant evidence in the notes. A mod can remain **Partial** while some boxes are checked and others are open. Keep smoke-test evidence separate from feature tests.

**Required per-mod test record:**
- **Tester name (required):** `Enter full name`
- **Test date (required):** `YYYY-MM-DD`
- **Result/evidence:** `Pass / Partial / Failed / Blocked` — briefly record what was observed and link or name the supporting log/report where applicable.

Do not use a GitHub username, initials, or an assumed identity as a substitute for the tester's name. Leave the fields explicitly marked `Not recorded` until the tester supplies the information.

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
| Dedicated-server startup | 5 Nov logs reached Done (1.718s), Done (1.822s), and latest Done (1.490s) | PASS — disposable profiles |
| Disposable world load | world_lootr_test loaded in the latest run | PASS |
| Matching client login | Matching client joined in the latest run | PASS |
| Clean shutdown | All dimensions saved in the 22:27 run | PASS |
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
- **Batch E:** spark initialized, but no saved profiler report or numeric baseline was recorded. ImmediatelyFast, Flerovium, Entity Culling and More Culling are now shown in the server's `mods-disabled` archive; their individual client tests have not been completed.

## How to complete this checklist

For each feature mod, mark its function complete only after the listed primary behavior works on the intended side(s). Where a mod adds several independent systems, test each system, not just one decorative block. For persistent machines, vehicles, storage, claims, portals and player data, include save/restart or relog. For multiplayer-dependent features, use a second player. Record exact version, test world/profile, relevant log and result.

Use JEI/creative inventory to locate representative items, but item visibility alone is not a functional pass. You do not need to test every recipe or decorative variant; test the primary function and each distinct subsystem.

**World-generation safeguard:** all biome/structure checks use a fresh disposable Overworld. Keep production world, BYG 2.6.3, Regions Unexplored 0.6.3 and active world-generation JSON unchanged. End research remains paused.

**Status meanings:** Pending = not function-tested; Partial = some behavior confirmed but listed test remains open; Pass = all listed primary functions have evidence; Failed/Blocked = reproducible failure or prerequisite prevents validation; N/A = support component checked through dependent mod.

## A. Create, Aeronautics, vehicles and transport

### Create 6.0.10
**Current status:** Pending
**Tester name (required):** Not recorded
**Test date (required):** Not recorded
**Result/evidence:** Not recorded
- [ ] Build a kinetic network.
- [ ] Test speed/rotation control, one press/mixer/deployer chain, item/fluid transport and save/restart.

### Create Aeronautics 1.3.2
**Current status:** Pending
**Tester name (required):** Not recorded
**Test date (required):** Not recorded
**Result/evidence:** Not recorded
- [ ] Assemble a vehicle.
- [ ] Test propulsion/lift, steering, controls, collision/physics, disassembly/reassembly and second-player sync.

### Create: Simulated 1.3.2
**Current status:** Pending
**Tester name (required):** Not recorded
**Test date (required):** Not recorded
**Result/evidence:** Not recorded
- [ ] Test assembly/disassembly, anchoring, controls, redstone interaction, collision and save/reload.

### Create: Offroad 1.3.2
**Current status:** Pending
**Tester name (required):** Not recorded
**Test date (required):** Not recorded
**Result/evidence:** Not recorded
- [ ] Build a wheeled vehicle.
- [ ] Test wheel power, steering, traction, stopping, collision and multiplayer sync.

### Create Kinetic 1.4.3
**Current status:** Pending
**Tester name (required):** Not recorded
**Test date (required):** Not recorded
**Result/evidence:** Not recorded
- [ ] Test its Aeronautics utility/propulsion blocks and items.
- [ ] Verify hitboxes, particles, controls and physics on client/server. Recheck existing loot-table and mixin findings.

### Create Aeronautics Structures 1.1.0-Beta-3.1 (test-only)
**Current status:** Partial — server smoke passed; generation unproven; one loot-table parse error remains.
**Tester name (required):** Not recorded
**Test date (required):** Not recorded
**Result/evidence:** Not recorded
- [ ] Fresh disposable Overworld: confirm engineering houses, abandoned boats, airships and hot-air balloons generate.
- [ ] Test engineer trader and chest loot.
- [ ] Recheck cr_aero_structures:chests/uniform.

### Create Aeronautics Curios Compat 2.0
**Current status:** Partial — assigned-slot checks user-reported working; repeatable synced test still needed.
**Tester name (required):** Not recorded
**Test date (required):** Not recorded
**Result/evidence:** Not recorded
- [ ] Equip Aviator Goggles in Head slot.
- [ ] Test overlay/engineer detection. Equip Linked Typewriter in Curios and activate (default Y) to operate linked typewriter/Redstone Links.

### Create Aeronautics: Copycat Wing 1.0.4
**Current status:** Pending
**Tester name (required):** Not recorded
**Test date (required):** Not recorded
**Result/evidence:** Not recorded
- [ ] Use a Copycats+ block as a wing part.
- [ ] Verify lift. Honeycomb should disable lift and axe restore it.
- [ ] Test on a moving contraption.

### Create Aeronautics: Transmission & Linkage 0.2.9
**Current status:** Pending
**Tester name (required):** Not recorded
**Test date (required):** Not recorded
**Result/evidence:** Not recorded
- [ ] Build a transmission/linkage assembly.
- [ ] Verify it transfers the intended movement/control across running and assembled contraptions.

### Create Big Cannons 5.11.7
**Current status:** Pending
**Tester name (required):** Not recorded
**Test date (required):** Not recorded
**Result/evidence:** Not recorded
- [ ] Assemble a multiblock cannon.
- [ ] Load projectiles/fuzes.
- [ ] Test Create-powered loading/aiming, firing, projectile effect/recoil, reload and autocannon if used.

### Create: Steam 'n' Rails 0.3.0-alpha.2
**Current status:** Pending
**Tester name (required):** Not recorded
**Test date (required):** Not recorded
**Result/evidence:** Not recorded
- [ ] Assemble/run a train.
- [ ] Test tracks, bogeys, schedules/stations, signals and installed railway interactions.
- [ ] Verify save/restart.

### Create: Blocks & Bogies 1.0.8
**Current status:** Pending
**Tester name (required):** Not recorded
**Test date (required):** Not recorded
**Result/evidence:** Not recorded
- [ ] Open bogie UI (crouch + right-click empty-handed)
- [ ] Configure drivers/axles, assemble train and verify style and operation.

### Create: Modern Train Parts 0.2.5
**Current status:** Pending
**Tester name (required):** Not recorded
**Test date (required):** Not recorded
**Result/evidence:** Not recorded
- [ ] Test pantograph deployment/retraction, shipping-container storage, wrench variants and train movement with parts attached.

### Create: Pantographs & Wires 0.2.3-C6 Beta
**Current status:** Pending
**Tester name (required):** Not recorded
**Test date (required):** Not recorded
**Result/evidence:** Not recorded
- [ ] Place masts/cantilevers and catenary.
- [ ] Verify wire connection and pantograph height adjustment on a moving train, including slopes/turns.

### Create: Rustic Structures 1.0.1
**Current status:** Pending
**Tester name (required):** Not recorded
**Test date (required):** Not recorded
**Result/evidence:** Not recorded
- [ ] Fresh disposable Overworld: find well, smithy, windmill and barn in intended biome groups.
- [ ] Inspect placement, loot and generation.

### Create: Structures Arise 176.49.50
**Current status:** Pending
**Tester name (required):** Not recorded
**Test date (required):** Not recorded
**Result/evidence:** Not recorded
- [ ] Fresh disposable Overworld: find multiple Create-themed structures.
- [ ] Inspect integrity, placement, loot and chunk-edge generation.

### Create: Aeronautical Diesel 1.1.0
**Current status:** Pending
**Tester name (required):** Not recorded
**Test date (required):** Not recorded
**Result/evidence:** Not recorded
- [ ] Use tank/fill port to move diesel, biodiesel, gasoline, ethanol, crude oil or plant oil into an Aeronautics portable engine.
- [ ] Test wrench and automation.

### Create: AeroPortals 1.3.6
**Current status:** Pending
**Tester name (required):** Not recorded
**Test date (required):** Not recorded
**Result/evidence:** Not recorded
- [ ] Move a complete airship through vanilla and supported modded portals.
- [ ] Verify ship, pilot, passengers and decorations arrive intact.

### Shield Generators 1.4.0
**Current status:** Pending
**Tester name (required):** Not recorded
**Test date (required):** Not recorded
**Result/evidence:** Not recorded
- [ ] Power a shield generator.
- [ ] Test activation, energy draw, boundary visualization, protection/interaction and multiplayer consistency.

### KineticGrip 1.0.5
**Current status:** Pending
**Tester name (required):** Not recorded
**Test date (required):** Not recorded
**Result/evidence:** Not recorded
- [ ] Test the Aeronautics handles from the player point of view.
- [ ] Operate the handle controls and any player-usable tool (such as the chainsaw) included by the installed build. Verify movement/control and client/server interaction.

### Sable 2.0.6
**Current status:** Pending
**Tester name (required):** Not recorded
**Test date (required):** Not recorded
**Result/evidence:** Not recorded
- [ ] Test Aeronautics physics: assembly, motion, forces, collision, sublevels and save/restart.
- [ ] Inspect Copycats Catwalk physics-tag errors.

### Strut Your Stuff 1.3.1
**Current status:** Pending — shared library; dependent integration and server-side issue remain open.
**Tester name (required):** Not recorded
**Test date (required):** Not recorded
**Result/evidence:** Not recorded
- [ ] Validate through dependent mods: spanning/collision structures, surface clipping, interaction and cable behavior/droop.
- [ ] Check dedicated-server RenderSystem class-loading issue.

## B. Create automation, energy, industry and build addons

### Create: Bits 'n' Bobs 2.3.5
**Current status:** Pending
**Tester name (required):** Not recorded
**Test date (required):** Not recorded
**Result/evidence:** Not recorded
- [ ] Test chain-drive transfer/carriage attachment, flywheel bearing rotation/battery behavior, wooden cogwheel swapping, dyeable fluid-pipe separation, chair and Nixie display.

### Create Cobblestone 1.5.1
**Current status:** Pending
**Tester name (required):** Not recorded
**Test date (required):** Not recorded
**Result/evidence:** Not recorded
- [ ] Set generator to cobblestone, stone, basalt, limestone and scoria.
- [ ] Verify outputs, type switching, SU use and disabled-generator behavior.

### Create Crafts & Additions 1.7.2
**Current status:** Pending
**Tester name (required):** Not recorded
**Test date (required):** Not recorded
**Result/evidence:** Not recorded
- [ ] Run Electric Motor from FE and verify SU output.
- [ ] Drive Alternator with SU and verify FE output.
- [ ] Test rolling-mill rods/wires.

### Create: Curios Backtank 1.0.2
**Current status:** Partial — Backpack + standard Backtank use in configured Back slots was reported; refill/consumption still open.
**Tester name (required):** Not recorded
**Test date (required):** Not recorded
**Result/evidence:** Not recorded
- [ ] Equip Backtank with intended Curios/backpack setup.
- [ ] Test air capacity, refill, consumption and rendering/slot behavior.

### Create Deco 2.1.3
**Current status:** Pending
**Tester name (required):** Not recorded
**Test date (required):** Not recorded
**Result/evidence:** Not recorded
- [ ] Test decorative blocks/variants, recipes, placement, rotation and drops.
- [ ] Recheck placard fix and loot-table parsing.

### Create: Diesel Generators 1.3.15
**Current status:** Pending
**Tester name (required):** Not recorded
**Test date (required):** Not recorded
**Result/evidence:** Not recorded
- [ ] Run an oil-to-fuel chain.
- [ ] Start diesel generator and test FE output, fuel consumption, upgrades and a representative machine/tool.

### Create Encased 1.10.0-fix1
**Current status:** Pending
**Tester name (required):** Not recorded
**Test date (required):** Not recorded
**Result/evidence:** Not recorded
- [ ] Apply casings to shafts, cogwheels and pipes.
- [ ] Test rotation, power/fluid transfer and persistent casing visuals.

### Create: Gadgets & Gizmos 1.2.10 (bundled)
**Current status:** Pending
**Tester name (required):** Not recorded
**Test date (required):** Not recorded
**Result/evidence:** Not recorded
- [ ] Test installed gadgets/engine components used by Aeronautics: assembly, thrust/control, fuel/power consumption and contraption synchronization.

### Create: Dragons Plus 1.11.9
**Current status:** Pending
**Tester name (required):** Not recorded
**Test date (required):** Not recorded
**Result/evidence:** Not recorded
- [ ] Use an Encased Fan to test Bulk Coloring with dye fluid, Bulk Freezing with Powder Snow, Bulk Ending with Dragon Head or Dragon's Breath fluid, and Bulk Sanding with Quicksand/supported block tag. Test Fluid Hatch take/deposit behavior on tanks and supported addon recipe integrations.

### Create: Liquid Fuel 3.0.0
**Current status:** Pending
**Tester name (required):** Not recorded
**Test date (required):** Not recorded
**Result/evidence:** Not recorded
- [ ] Feed supported liquid fuel to a Blaze Burner.
- [ ] Verify normal/superheated operation, duration, consumption and rejection of invalid fluids.

### Create: Fluids Be Gone! 1.0.1
**Current status:** Pending
**Tester name (required):** Not recorded
**Test date (required):** Not recorded
**Result/evidence:** Not recorded
- [ ] Run a Create Drill and a Simulated Rock Cutting Wheel into fluid-containing terrain.
- [ ] Verify fluids in the mined path are voided when enabled, separate drill/rock-wheel config switches work, and fluids outside the mining path remain unchanged.

### Create: Framed 1.8.2
**Current status:** Pending
**Tester name (required):** Not recorded
**Test date (required):** Not recorded
**Result/evidence:** Not recorded
- [ ] Build framed blocks, apply a supported material/appearance and shape.
- [ ] Verify placement, rotation, breaking and reload.

### Create: Enchantment Industry 2.5.4b
**Current status:** Pending
**Tester name (required):** Not recorded
**Test date (required):** Not recorded
**Result/evidence:** Not recorded
- [ ] Run automated enchanting/disenchanting and XP-fluid processing.
- [ ] Verify inputs, outputs, XP/fluid handling, recipes and automation.

### Create: Numismatics 1.0.20
**Current status:** Pending
**Tester name (required):** Not recorded
**Test date (required):** Not recorded
**Result/evidence:** Not recorded
- [ ] Obtain coins.
- [ ] Use Vendor for buy/sell, Bank Terminal for deposit/withdraw, and Depositor price/redstone pulse for coin/card payments.

### Create: Numismatics Plus 1.0.1
**Current status:** Hold — JAR is archived in `MinecraftServer-Test/mods-disabled`; not installed in the current server test profile. Reintroduce only for a separate pairing test with Numismatics 1.0.20.
**Tester name (required):** Not recorded
**Test date (required):** Not recorded
**Result/evidence:** Not recorded

- [ ] Buy from a Create shop with coins and a Numismatics card.
- [ ] Verify deduction, stock, recipient account and missing-Depositor/card behavior.

### Create: Pattern Schematics 2.0.10
**Current status:** Pending
**Tester name (required):** Not recorded
**Test date (required):** Not recorded
**Result/evidence:** Not recorded
- [ ] Create/obtain a repeating schematic.
- [ ] Print in creative or use Schematicannon.
- [ ] Verify placement, orientation, repeat behavior and resource requirements.

[The rest of the existing checklist content remains unchanged. Every remaining per-mod `**Current status:**` entry has the same required tester/date/result fields inserted immediately below it.]
