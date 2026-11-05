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

**How to submit test results — the checklist updates automatically:**

1. Open the [Submit Test Result form](https://github.com/alexth110987/Create-IronWoven-Beta/issues/new?template=functional-test-report.yml).
2. Copy the exact mod heading and exact test-action text from the table below.
3. Enter your name, test date, choose the result, and describe what happened.
4. Submit the form. Once the repository's one-time Actions write permission is configured, the matching checklist row is updated automatically and the report issue is closed when the update succeeds.

Submit one form for each test action. If the row already has a result, or the mod/action text does not match exactly, the automation will leave the checklist unchanged and explain what needs review. Retests of completed actions require maintainer review; existing results are never silently overwritten.

A server startup or an item appearing in JEI is not, by itself, a function-test pass. Keep smoke-test evidence separate from feature tests.

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

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Build a kinetic network. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Test speed/rotation control, one press/mixer/deployer chain, item/fluid transport and save/restart. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Create Aeronautics 1.3.2
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Assemble a vehicle. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Test propulsion/lift, steering, controls, collision/physics, disassembly/reassembly and second-player sync. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Create: Simulated 1.3.2
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Test assembly/disassembly, anchoring, controls, redstone interaction, collision and save/reload. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Create: Offroad 1.3.2
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Build a wheeled vehicle. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Test wheel power, steering, traction, stopping, collision and multiplayer sync. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Create Kinetic 1.4.3
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Test its Aeronautics utility/propulsion blocks and items. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Verify hitboxes, particles, controls and physics on client/server. Recheck existing loot-table and mixin findings. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Create Aeronautics Structures 1.1.0-Beta-3.1 (test-only)
**Current status:** Partial — server smoke passed; generation unproven; one loot-table parse error remains.

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Fresh disposable Overworld: confirm engineering houses, abandoned boats, airships and hot-air balloons generate. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Test engineer trader and chest loot. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Recheck cr_aero_structures:chests/uniform. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Create Aeronautics Curios Compat 2.0
**Current status:** Partial — assigned-slot checks user-reported working; repeatable synced test still needed.

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Equip Aviator Goggles in Head slot. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Test overlay/engineer detection. Equip Linked Typewriter in Curios and activate (default Y) to operate linked typewriter/Redstone Links. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Create Aeronautics: Copycat Wing 1.0.4
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Use a Copycats+ block as a wing part. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Verify lift. Honeycomb should disable lift and axe restore it. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Test on a moving contraption. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Create Aeronautics: Transmission & Linkage 0.2.9
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Build a transmission/linkage assembly. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Verify it transfers the intended movement/control across running and assembled contraptions. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Create Big Cannons 5.11.7
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Assemble a multiblock cannon. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Load projectiles/fuzes. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Test Create-powered loading/aiming, firing, projectile effect/recoil, reload and autocannon if used. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Create: Steam 'n' Rails 0.3.0-alpha.2
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Assemble/run a train. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Test tracks, bogeys, schedules/stations, signals and installed railway interactions. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Verify save/restart. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Create: Blocks & Bogies 1.0.8
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Open bogie UI (crouch + right-click empty-handed) | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Configure drivers/axles, assemble train and verify style and operation. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Create: Modern Train Parts 0.2.5
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Test pantograph deployment/retraction, shipping-container storage, wrench variants and train movement with parts attached. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Create: Pantographs & Wires 0.2.3-C6 Beta
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Place masts/cantilevers and catenary. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Verify wire connection and pantograph height adjustment on a moving train, including slopes/turns. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Create: Rustic Structures 1.0.1
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Fresh disposable Overworld: find well, smithy, windmill and barn in intended biome groups. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Inspect placement, loot and generation. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Create: Structures Arise 176.49.50
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Fresh disposable Overworld: find multiple Create-themed structures. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Inspect integrity, placement, loot and chunk-edge generation. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Create: Aeronautical Diesel 1.1.0
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Use tank/fill port to move diesel, biodiesel, gasoline, ethanol, crude oil or plant oil into an Aeronautics portable engine. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Test wrench and automation. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Create: AeroPortals 1.3.6
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Move a complete airship through vanilla and supported modded portals. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Verify ship, pilot, passengers and decorations arrive intact. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Shield Generators 1.4.0
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Power a shield generator. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Test activation, energy draw, boundary visualization, protection/interaction and multiplayer consistency. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### KineticGrip 1.0.5
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Test the Aeronautics handles from the player point of view. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Operate the handle controls and any player-usable tool (such as the chainsaw) included by the installed build. Verify movement/control and client/server interaction. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Sable 2.0.6
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Test Aeronautics physics: assembly, motion, forces, collision, sublevels and save/restart. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Inspect Copycats Catwalk physics-tag errors. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Strut Your Stuff 1.3.1
**Current status:** Pending — shared library; dependent integration and server-side issue remain open.

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Validate through dependent mods: spanning/collision structures, surface clipping, interaction and cable behavior/droop. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Check dedicated-server RenderSystem class-loading issue. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

## B. Create automation, energy, industry and build addons

### Create: Bits 'n' Bobs 2.3.5
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Test chain-drive transfer/carriage attachment, flywheel bearing rotation/battery behavior, wooden cogwheel swapping, dyeable fluid-pipe separation, chair and Nixie display. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Create Cobblestone 1.5.1
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Set generator to cobblestone, stone, basalt, limestone and scoria. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Verify outputs, type switching, SU use and disabled-generator behavior. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Create Crafts & Additions 1.7.2
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Run Electric Motor from FE and verify SU output. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Drive Alternator with SU and verify FE output. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Test rolling-mill rods/wires. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Create: Curios Backtank 1.0.2
**Current status:** Partial — Backpack + standard Backtank use in configured Back slots was reported; refill/consumption still open.

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Equip Backtank with intended Curios/backpack setup. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Test air capacity, refill, consumption and rendering/slot behavior. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Create Deco 2.1.3
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Test decorative blocks/variants, recipes, placement, rotation and drops. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Recheck placard fix and loot-table parsing. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Create: Diesel Generators 1.3.15
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Run an oil-to-fuel chain. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Start diesel generator and test FE output, fuel consumption, upgrades and a representative machine/tool. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Create Encased 1.10.0-fix1
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Apply casings to shafts, cogwheels and pipes. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Test rotation, power/fluid transfer and persistent casing visuals. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Create: Gadgets & Gizmos 1.2.10 (bundled)
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Test installed gadgets/engine components used by Aeronautics: assembly, thrust/control, fuel/power consumption and contraption synchronization. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Create: Dragons Plus 1.11.9
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Use an Encased Fan to test Bulk Coloring with dye fluid, Bulk Freezing with Powder Snow, Bulk Ending with Dragon Head or Dragon's Breath fluid, and Bulk Sanding with Quicksand/supported block tag. Test Fluid Hatch take/deposit behavior on tanks and supported addon recipe integrations. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Create: Liquid Fuel 3.0.0
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Feed supported liquid fuel to a Blaze Burner. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Verify normal/superheated operation, duration, consumption and rejection of invalid fluids. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Create: Fluids Be Gone! 1.0.1
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Run a Create Drill and a Simulated Rock Cutting Wheel into fluid-containing terrain. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Verify fluids in the mined path are voided when enabled, separate drill/rock-wheel config switches work, and fluids outside the mining path remain unchanged. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Create: Framed 1.8.2
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Build framed blocks, apply a supported material/appearance and shape. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Verify placement, rotation, breaking and reload. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Create: Enchantment Industry 2.5.4b
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Run automated enchanting/disenchanting and XP-fluid processing. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Verify inputs, outputs, XP/fluid handling, recipes and automation. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Create: Numismatics 1.0.20
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Obtain coins. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Use Vendor for buy/sell, Bank Terminal for deposit/withdraw, and Depositor price/redstone pulse for coin/card payments. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Create: Numismatics Plus 1.0.1
**Current status:** Hold — JAR is archived in `MinecraftServer-Test/mods-disabled`; not installed in the current server test profile. Reintroduce only for a separate pairing test with Numismatics 1.0.20.


| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Buy from a Create shop with coins and a Numismatics card. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Verify deduction, stock, recipient account and missing-Depositor/card behavior. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Create: Pattern Schematics 2.0.10
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Create/obtain a repeating schematic. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Print in creative or use Schematicannon. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Verify placement, orientation, repeat behavior and resource requirements. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Create: Power Grid 0.6.2
**Current status:** Partial — server loads; optional native solver unavailable in tested Windows environment; fallback function not yet verified.

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Build a small electrical network with source, wires, transformer and consumers. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Test components and fallback solver. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Record native solver separately. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Create: Sound of Steam / Pipe Organs 0.9.2.1
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Place/configure a pipe organ. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Trigger notes manually and by supported controls/redstone. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Test pitch, sound, range, persistence and multiplayer audio. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Create: The Factory Must Grow Community Edition 1.3.3
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Run representative industrial processing: fluid/oil input, machine processing, outputs, power/kinetic requirements and fuel-burning machine. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Test Unified Fuels integration. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Create: Unified Fuels 1.0.4
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Cross-feed fuels between supported addons and compatible engines, burners and trains. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Verify shared values/consumption, gas-vs-liquid rules, toggles and config after restart. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Create: Vibrant Vaults 0.3.2
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Build/connect vaults and shipping containers. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Insert/extract items, change color/orientation and test package frogport/stock link/packager features present. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Create Slice & Dice 4.3.4
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Automate a Farmer's Delight cutting-board recipe with Create saw. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Verify ingredients, output, transport and recipe visibility. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Create: Bells & Whistles 0.4.7
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Test representative decorative train/building blocks, variants, placement, rotation, collision and rendering on moving contraptions. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Create: Copycats+ 3.0.9
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Use copycat shapes with multiple source materials. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Verify appearance, shape/state, rotation and moving-contraption rendering. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Copycats+ Additions 1.5.0
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Test added copycat shapes/variants, material application and placement. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Verify Aeronautics Copycat Wing integration. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Design n' Decor 2.2b
**Current status:** Pending — startup passed; logs contain many loot-table parse errors. Drop behavior remains open.

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Test representative decoration families, recipes and drops. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Specifically verify dyed cogwheel/loot-table entries and intended block drops. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

## C. Building, food, storage, world generation and exploration

### Chipped 4.0.2
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Use workstations on vanilla/modded wood and stone. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Craft several variants, place/break them and verify drops/models. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Farmer's Delight 1.3.4
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Run a food chain: ingredients, cutting-board processing, cooking pot, finished meal and food effects. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Test container interactions. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Mama's Herbs and Harvest 1.21.1-24
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Plant/harvest representative crops and herbs. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Test growth stages, drops, food/processing recipes and Botany Pots integration. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Botany Pots 21.1.44
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Plant vanilla, BYG/RU and Herbs & Harvest crops. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Test growth/harvest, drops, hopper input/output automation and JEI. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Construction Sticks 1.5.0
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Place a small wall/floor pattern. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Verify direction, range, item use, limits, claim protection and stop/undo behavior. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Every Compat 2.11.56
**Current status:** Partial — Carpenter's Table variants and stone table user-reported working; duplicate Golden Cherry Leaves registration and large block footprint remain.

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Test Chipped Carpenter's Table variants for several modded woods plus supported Create/Farmer's Delight/RU compat. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Verify recipes, models, drops and client/server registry sync. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Lootr 1.11.38.127
**Current status:** Partial — chest opening and loot presence user-confirmed; second-player personal loot unverified.

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Have two players open the same generated Lootr chest. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Verify independent personal loot, container persistence and multiplayer synchronization. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Sophisticated Backpacks 3.26.20.2244
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Craft/open backpack. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Test storage, upgrades, filters/automation, pickup and save/relog persistence. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Sophisticated Backpacks Create Integration 0.2.3
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Test supported Create inventory/item transport with backpack. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Verify insertion/extraction and normal backpack behavior. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Sophisticated Air Tank 1.0.1-beta
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Equip/refill air tank. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Test air supply/consumption, capacity indicator and supported backpack/Curios interactions. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Oh The Biomes We've Gone 2.6.3
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Fresh disposable Overworld: verify representative BYG biomes, vegetation/trees, structures and biome-specific terrain. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Check configs/datapacks. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Regions Unexplored 0.6.3
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Fresh disposable Overworld: verify representative RU biomes, vegetation, trees and biome blocks. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Check biome edges and Create integration. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Fresh disposable Nether: use biome lookup and explore new chunks to confirm representative Regions Unexplored Nether biomes generate; keep the production world unchanged. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Oh The Trees You'll Grow 5.3.5
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Grow representative added trees. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Test sapling growth, leaves/log drops, wood sets and leaves decay. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
 
### Integrated Villages 1.3.3+1.21.1 (Overworld candidate)
**Current status:** Partial — corrected dependencies load; multiple village IDs are locatable, but full structure and performance validation remain open.

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Inspect representative generated structures (including Airship and Mediterranean villages) in a fresh disposable Overworld. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Check Cabin Village decoration pool warning and verify that structures are complete, populated, and have intended loot. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Compare locate/generation responsiveness; prior structure searches took roughly 10–37 seconds and caused server tick-delay warnings. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Confirm whether vanilla village generation is intentionally retained. Do not assume Integrated Villages replaces every vanilla village. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Save/restart the disposable world and review the matching server/client logs. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

Dependency evidence: the first startup attempt lacked Supplementaries and Integrated API 1.6.2+. The corrected test profile used Create 6.0.10, Supplementaries 3.4.0, and Integrated API 1.9.1 and reached `Done`. Validate these libraries through Integrated Villages; no standalone function test is required.

### Atmosphere 1.0.18
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Fresh disposable world: verify its advertised environment/atmosphere changes. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Check day/night, weather, visuals/audio and client/server consistency. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Create Oh The Biomes We've Gone Compatibility 0.0NONE
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Check compatibility items/recipes/blocks for BYG and Create. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Test JEI presence, placement, drops and wood/biome integration. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Nature's Compass 3.4.0
**Current status:** Smoke-only — Batch B startup/login passed; actual search behavior not tested.

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Search for a known biome in disposable world. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Verify result, distance/direction, no-result message and repeat search. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Explorer's Compass 3.4.0
**Current status:** Smoke-only — Batch B startup/login passed; actual search behavior not tested.

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Search for a known generated structure. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Verify correct result, distance/direction and updated search after discovery. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Create Structures Arise 176.49.50
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Fresh disposable Overworld: find multiple Create-themed structures. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Inspect integrity, loot, biome placement and chunk-edge generation. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

## D. Player interface, server tools and information mods

### AppleSkin 3.0.9
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Check hunger, saturation and exhaustion HUD while eating, sprinting and regenerating. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Compare to expected vanilla values. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### FTB Chunks 2101.1.23
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Claim/unclaim test chunk. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Verify map, team permissions, boundaries, force-load controls, protection and reconnect persistence. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### FTB Teams 2101.1.12
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Create team. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Invite/remove second player. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Check ownership/permissions and FTB Chunks team-claim behavior. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### InControl! 10.3.1
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Test active spawn/loot/experience rules under controlled conditions. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Verify allowed/blocked mobs/loot and restart persistence. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Jade 15.10.6
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Inspect vanilla/modded blocks and entities. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Verify tooltips, states, inventories/fluid data and Create/Aeronautics compatibility. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Just Enough Items 19.64.0.455
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Search representative items from each content group. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Inspect crafting/processing recipes, catalysts and fluid inputs. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Just Enough Resources 1.6.0.57
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Check known mob-drop, loot-table, villager-trade and world-generation entries against in-game sources. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Enchantment Descriptions 21.1.11
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Open tooltips for vanilla/modded enchanted books and items. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Verify accurate descriptions and layout. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Shulker Box Tooltip 5.1.9+1.21.1
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Hover filled shulkers. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Verify contents preview, item counts, scroll/page behavior and provider integrations. 31 providers registered is not visual proof. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Mouse Tweaks 2.26.1
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Test drag distribution, wheel scrolling and quick-move in player inventory, chests, backpacks and modded GUIs. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Memory Settings 6.0
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Verify settings apply and persist across restart. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Measure memory only in controlled same-workload comparison, not from startup alone. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### ModernFix 5.27.27
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Verify selected optimization mixins/options on the same disposable test profile. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Review for mixin errors, changed gameplay behavior, save integrity and comparable startup/runtime metrics. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

## E. Client graphics and performance mods

### Sodium 0.8.13 (client-only)
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Launch matching client. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Verify rendering of chunks, Create moving contraptions, Aeronautics ships and block entities. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Compare same-scene FPS/frame pacing. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Iris 1.8.14-beta.1 (client-only)
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Toggle shader pack. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Inspect Create/Aeronautics models, ship sublevels, water, particles, HUD and shadows. Record known Aeronautics/Iris visual artifacts. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Sodium Extra 0.9.5 (client-only)
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Change a Sodium Extra option. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Verify it applies, persists after restart and does not conflict with Iris/Sodium. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### ImmediatelyFast 1.6.15 (client-only)
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Compare identical GUI, HUD, particles, item/entity and block-entity scenes enabled/disabled. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Check visual parity and client log. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Flerovium 1.1.3 Beta (client-only; detected build)
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Compare item, particle and entity rendering/FPS against same Sodium baseline. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Inspect artifacts. Stable 1.1.2 remains a separate planned candidate. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Entity Culling 1.10.4 (client-only)
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Check culling of Create contraptions, Aeronautics ships/sublevels, entities and block entities. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Hidden objects must reappear when visible. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### More Culling 1.0.11 (client-only)
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Check leaves, glass, connected textures and modded blocks across chunk boundaries. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Ensure no missing faces/transparency errors. Test Cloth Config options. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### spark 1.10.124 (server profiler)
**Current status:** Deferred to beta testers — not required during internal development.

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| During beta testing, record TPS, MSPT, memory/GC, and CPU under a repeatable load; save a 2–5 minute profile. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Record the selected profiler engine and any platform-specific fallback. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

## F. Libraries, APIs and shared support components

### Apollib 1.2.0
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Verify dependent mod registries/content and related GUI/network interaction. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Record owner mod. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Architectury 13.0.11
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Verify dependent mods initialize on client/server and shared event/network hooks work during login and interaction. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Athena 4.0.6
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Verify dependent content models/textures render. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Check for missing model/texture errors. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Azimuth 1.4.10
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Verify mods depending on Azimuth load and shared utility/render behavior works. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Check class-loading logs. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Bookshelf 21.1.81
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Verify dependent features (e.g. Enchantment Descriptions/Botany Pots) load and work. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Dependency-only. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Cloth Config API 15.0.140
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Open More Culling config. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Change/save option, relaunch and verify persistence. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### CodecUI 1.4.7
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Open dependent settings/config interface. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Verify widgets, values and save/cancel behavior. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Conditional Mixin 0.6.4
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Verify dependent mixins activate under intended mod/config conditions. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Check mixin apply failures. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### CorgiLib 5.0.0.10
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Verify dependent mod initializes and required shared utilities work. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Check missing-class/registration errors. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Cupboard 4.2
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Verify Memory Settings and other dependent config integrations initialize and read/write settings. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Curios API 9.5.1
**Current status:** Partial — two Back + one Head slot and selected item uses were reported in new-world checks; full sync/older-player data still open.

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Verify slot registry, counts, equip/unequip, client/server sync and persistence with Aeronautics/Backtank. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### DragonLib 3.0.29
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Verify dependent DragonLib consumers (including Pantographs & Wires) register, render and execute their behavior. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Ferrite Core 7.0.3
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Capture memory baseline and compare same workload in disposable clone. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Check startup/registry stability. Do not alter production based only on benchmark. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Flywheel 1.0.6
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Verify Create contraption rendering, instancing, moving block entities and animation on matching client. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Forge Config API Port 21.1.1
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Open dependent mod config GUI, change value, save/restart and verify persistence. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Forgified Fabric API Base 0.4.42
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Verify bundled/using mods load and required API calls work. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Dependency-only. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Forgified Fabric BlockView API 1.0.10
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Verify renderer/block-view integration used by Flerovium loads and block rendering stays correct. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Forgified Fabric Renderer API 3.4.1
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Verify renderer-dependent mod integration and item/block rendering. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Dependency-only. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Forgified Fabric Rendering Data Attachment 0.3.48
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Verify renderer data attachments survive chunk/entity render updates without visual corruption. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### FTB Library 2101.1.39
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Verify FTB Chunks/Teams menus, shared data, keybinds and networking. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Dependency-only. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### FTB XMod Compat 21.1.14
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Verify selected team/stage/permission integration is detected and behaves correctly. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Gadgets & Gizmos Library 1.2.10
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Verify bundled G&G content registers and dependent contraption controller/graph utilities work. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### GeckoLib 4 4.9.3
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Verify animated entities/blocks and Aeronautics Structures visuals animate correctly on client. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Kotlin for Forge 5.12.0
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Verify Kotlin-based dependent mods initialize and execute entry points. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Dependency-only. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Lithostitched 1.8.1
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Verify BYG/RU biome and feature registration in fresh disposable Overworld. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Check registry conflicts. Preserve production worldgen. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### MezzConfig 0.6.10
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Verify config interface opens and dependent config screens load/save. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Standalone and bundled copies must not duplicate. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Moonlight Lib 3.8.1
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Verify dependent features (including Every Compat) register resources/models without duplicate registry errors. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Ponder 1.0.82
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Open Ponder scenes for representative Create/addon blocks. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Confirm scenes render and advance. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### PrickleMC 21.1.11
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Verify Botany Pots dependency/plugin initialization and crop/soil compatibility. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Dependency-only otherwise. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Resourceful Lib 3.0.12
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Verify dependent resource registries/config/content load. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Check missing resource errors. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Ritchie's Projectile Library 2.1.2
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Verify through Create Big Cannons: projectile and fuze definitions register, load and fire correctly. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| Confirm client/server projectile synchronization. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Sable Companion 1.6.0
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Verify dependent Sable integrations load and register expected physics behavior. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| No separate feature assumed. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Sophisticated Core 1.5.28.2458
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Verify backpack upgrade/inventory modules initialize and retain data after close/reopen, relog and restart. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### TerraBlender 4.1.0.8
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Verify BYG/RU biome providers register in intended dimensions of fresh disposable world. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| No missing/duplicate regions. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### TRansition 1.0.21
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Verify Entity Culling transition/render hooks when entities/block entities enter/leave view. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### TRender 1.0.15
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Verify dependent render integration and UI/model path. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |
| No missing renderer/client crash. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

### Veil 4.3.2
**Current status:** Pending

| Test action | Result | Tester name | Test date | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|
| Verify Veil-dependent rendering/effects initialize on client and remain correct with Sodium/Iris. | Not tested | Not recorded | YYYY-MM-DD | Add result and evidence here |

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

Do not leave both Numismatics JARs in one test folder. The later `mods-disabled` screenshot shows Numismatics 1.1.0 and Numismatics Plus 1.0.1 archived; keep Numismatics 1.0.20 only in the active server test folder. Reintroduce Numismatics Plus only for a separate pairing test with 1.0.20. The four client-only rendering candidates are also now shown in `mods-disabled`; their client tests remain pending and must be performed on the matching client, one at a time.

### Error review

The log contains **463 ERROR-level entries and 172 WARN-level entries**. The errors include 454 loot-table parse errors (Design n' Decor 256, Steam 'n' Rails 192, Create Kinetic 5, Create Aeronautics Structures 1), three Sable unknown Catwalk selectors, one Struts dedicated-server `RenderSystem` error, one PowerGrid optional native-backend error, three Every Compat registration/block-count messages, and one Create Deco placard recipe error. Verify relevant world-scoped compatibility datapacks before treating recurring loot-table or Sable errors as regressions. The Aeronautics Structures chest-table issue remains unresolved and Batch D remains partial. The 12,288 MB allocation warning exceeds the pack's stated 8,500 MB recommendation but did not block this run.

spark did not produce TPS/MSPT, CPU, memory/GC measurements, or a saved profiler report. Batch E remains partial. Individual feature tests remain open in the matrix below; no function row is passed by this smoke test.


## Disabled server-folder archive reconciliation — 5 November 2026, 17:58

A new screenshot shows `MinecraftServer-Test/mods-disabled`. It confirms the following files are archived outside the active dedicated-server mods folder:

- End test files: BetterEnd 21.0.39, YUNG's Better End Island 3.1.2 and YUNG's API 5.1.9. End testing remains paused.
- Client-only rendering/performance files: Entity Culling 1.10.4 and 1.11.3, Flerovium 1.1.3, ImmediatelyFast 1.6.15, More Culling 1.0.11, Sodium 0.8.13, Sodium Extra 0.9.5 and Iris 1.8.14-beta.1. Their presence in a server-side archive does not determine whether matching client-side files remain installed. Batch E feature/performance testing remains pending.
- Superseded older copies: Create Crafts & Additions 1.6.0, Create: Enchantment Industry 2.4.2, FTB Teams 2101.1.11, Lithostitched 1.7.11, Sophisticated Backpacks 3.26.19.2243, Sophisticated Core 1.5.23.2446 and TFMG 1.3.2a-community. Newer versions are recorded in the active test inventory.
- Numismatics 1.1.0 and Numismatics Plus 1.0.1 are archived. The current server test is to keep Numismatics 1.0.20 only; Plus is not active and its pairing test is on hold.
- Tracks 1.0.1 and Tracks Plus 1.0.6b7 are archived legacy candidates; the screenshot does not establish their original reason for removal.
- `createkinetic-1.4.3.jar.original.bak` is a backup file, not an active mod.

This is an archive-folder observation, not a fresh filesystem scan. It does not establish a client-profile inventory or a performance improvement. Do not mark any functional test passed or rejected solely because a JAR is archived.


## Latest server retest — 5 November 2026, 22:27–22:31

**Result: Full routine smoke test passed** for the disposable server profile. The server reached `Done (1.490s)`, loaded the test world, accepted a matching client login, disconnected the client, and saved all dimensions during clean shutdown. This is not a feature-level test or release approval.

### Numismatics runtime correction

| Mod | Latest runtime evidence | Status |
|---|---|---|
| Create: Numismatics | 1.0.20 detected and initialized; 1.1.0 absent | **Runtime selection confirmed** |
| Create: Numismatics Plus | Absent from the runtime list | **Pairing not tested** |

The 22:27 log supersedes the older 14:09 runtime observation for the latest profile, where Numismatics 1.1.0 had been selected. Keep one Numismatics JAR per profile. The Plus 1.0.1 + Numismatics 1.0.20 pairing still requires its own deliberate test.

### Integrated Villages status

Integrated Villages 1.3.3+1.21.1 loaded after the missing Supplementaries / Integrated API dependency issue was corrected. Multiple Integrated Villages IDs were found by disposable-world lookups, but vanilla village IDs were also present. Structure completeness and the intended vanilla-village behavior remain unconfirmed. Some locate searches took roughly 10–37 seconds and produced tick-delay warnings; the Cabin Village decoration pool warning is also unresolved. See the candidate's checklist above.

### GC observation — separate from a performance benchmark

The accompanying `gc.log` shows G1 garbage collection reclaiming heap after allocation peaks. The run ended after about 4 minutes 27 seconds with about 2.5 GiB used in an 8 GiB committed heap (Java heap maximum 12 GiB). This short trace is evidence of heap reclamation, not proof that no long-session or native-memory leak exists. It is not a TPS/MSPT or CPU performance baseline. spark profiling remains deferred to beta testers.

### Issues still open

- Struts still attempted to load client-only `RenderSystem` on the dedicated server.
- PowerGrid's optional `powergridNative7` accelerated solver still could not load; the server used its fallback.
- Batch D's Aeronautics Structures loot-table / provenance / structure-generation review remains partial.
- World-scoped datapack-dependent errors still need to be interpreted only in worlds where the relevant packs are enabled.

No production world or configuration was changed.
