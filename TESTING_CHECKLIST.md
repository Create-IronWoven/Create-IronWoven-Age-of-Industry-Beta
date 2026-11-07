# Testing order for beta candidates

- Test server-only mods first, then shared client/server mods, and client-only mods last.
- Complete pending server-side and shared candidates before starting client-only candidates, unless the maintainer explicitly defers, holds, or rejects a specific candidate.
- Split mixed batches by side. Keep client-only JARs out of the dedicated-server mods folder.
- Test client-only mods one at a time on the matching client after the server/shared queue is complete.
- **spark profiling is deferred to beta testers.** It is not an internal development prerequisite; beta testers may capture performance baselines during the beta phase.

# Full Installed-Mod Functional Testing Checklist

**Last reviewed:** 7 November 2026  
**Target:** Minecraft 1.21.1 · NeoForge 21.1.265 · Java 21  
**Approved download source:** CurseForge only

This checklist is a feature-test matrix, not a live installed-mod manifest. It follows the recorded test inventory and separately labels current client-only candidates, completed checks, holds, and dated historical evidence. For current file inventories and versions, use [MODS.md](MODS.md): its 6 November server snapshot is separate from the latest CurseForge client-profile screenshot. Do not treat historical snapshot tables below as current installation instructions. This is not a final release manifest.

## Current verification snapshot — 7 November 2026

This section is the current status summary. Dated trial tables later in this file are historical evidence and must not be read as the current installed inventory.

| Area | Current verified status |
|---|---|
| Dedicated-server smoke test | PASS — corrected 6 Nov datapack-enabled disposable profile reached Done, loaded world, accepted matching client, and shut down cleanly |
| Fresh dedicated-server installation v.0.1 | NOT STARTED — clean folder `IronWoven Age Of Industry v.0.1` created 7 Nov 2026 and screenshot-confirmed empty; initial mod JAR count 0; NeoForge installation not started; final JAR and NeoForge loaded-mod counts pending |
| World-scoped compatibility datapacks | PASS at log level — four packs enabled; targeted Design n' Decor, Steam 'n' Rails, Create Kinetic, Sable Catwalk and Create Deco placard errors absent in corrected retest |
| Struts | PARTIAL — local patched server/client runtime and visible test pieces passed; official CurseForge JAR remains unpatched, so standard-install/release issue remains open |
| Shulker Box Tooltip / Supplementaries | PARTIAL — client-only `preview.serverIntegration=false` workaround passed local join/log/visual checks; remote server-provided preview extras are disabled; upstream/release decision remains open |
| PowerGrid 0.6.2 | PARTIAL — internal Windows native loading and client join passed with restored 0.6.1 DLL; electrical-network behavior reserved for beta testers; Linux untested |
| Every Compat | PARTIAL — accepted pair 2.11.57 + Moonlight 3.8.2 passed Windows disposable startup/world/login/shutdown smoke test; duplicate Golden Cherry Leaves registration remains open; feature-level checks are assigned to beta testers; client and server folder deployment confirmed; updated-baseline startup/login verification pending |
| Create Aeronautics Structures | PARTIAL — test-only uniform loot override passed runtime testing; all 11 valid structure IDs have locate/visual presence evidence in disposable Overworld; crashed-airship hillside placement visually accepted; maintainer spot checks: engineering-house standard and Lootr barrels generated loot; crashed-airship vanilla chest has no assigned loot table; remaining structure/container loot coverage is delegated to beta testers; release-safe fix/distribution decision remains open; `plane` ID rejected; original JAR unchanged |
| Integrated Villages | PARTIAL — server load and structure-ID lookups observed; generation completeness, vanilla-village behavior and performance remain unverified |
| Entity Culling | REMOVED from current CurseForge client profile; confirmed absent in 6 Nov client-folder screenshot; not an active test candidate |
| ImmediatelyFast / Flerovium / More Culling | Optional client candidates only; not confirmed as currently installed by latest client screenshot; do not treat as current installed mods |
| Linux dedicated server | NOT TESTED — Linux system has not yet been set up |
| Individual feature matrix | OPEN — pending rows remain pending until the specific behavior is tested and evidence is recorded |
| Public beta / release | NOT APPROVED — no downloadable beta package exists |

**Current inventory source:** [MODS.md](MODS.md) holds separate server and client observations. The latest 6 November Windows client screenshot confirms Entity Culling is absent from the CurseForge `Create World/mods` folder. The 6 November server inventory screenshot is not a client inventory. No production world or production world-generation configuration was changed.

**How to submit test results — the checklist updates automatically:**

1. Open the [Submit Test Result form](https://github.com/alexth110987/Create-IronWoven-Beta/issues/new?template=functional-test-report.yml).
2. Copy the mod heading text (including version, without the leading ### symbols) and the exact test-action text from the table below.
3. Select the test environment: Single-player, Multiplayer, or Both. Choose Both only when you actually tested the action in both environments.
4. Enter a tester nickname or pseudonym and the test date in DD-MM-YYYY format, choose the result, and describe what happened. Do not enter a legal/real name or GitHub username. Note: GitHub shows the account that opened the report as the public issue author, but the automation does not copy that account name into this checklist. Do not use your legal/real name or GitHub account username.
5. Submit the form. Once the repository's one-time Actions write permission is configured, the matching checklist row is updated automatically and the report issue is closed when the update succeeds.

Submit one form for each test action. If the row already has a result, or the mod/action text does not match exactly, the automation will leave the checklist unchanged and explain what needs review. Retests of completed actions require maintainer review; existing results are never silently overwritten.

A server startup or an item appearing in JEI is not, by itself, a function-test pass. Keep smoke-test evidence separate from feature tests.

## Smoke test is not a function test

The 6 November 15:54 datapack-enabled disposable-server retest reached `Done`, loaded `world_lootr_test`, accepted a matching client login, and shut down with all dimensions saved. All four IronWoven world-scoped compatibility datapacks were enabled; the targeted Design n' Decor, Steam 'n' Rails, Create Kinetic, Sable Catwalk, and Create Deco placard error entries were absent. Later same-day targeted retests also confirmed the local Struts workaround and the Shulker Box Tooltip / Supplementaries client workaround; see the dated records below. The 6 November 18:29 server and 18:34 client logs additionally confirmed PowerGrid's Windows native backend loads after restoring the 0.6.1 Windows DLL to the disposable `.pg-native` folders, while leaving the 0.6.2 JAR unchanged. These are test-profile-specific results; **they do not prove every installed mod's functions work or establish Linux compatibility**.

- **Smoke test:** mod discovery, server/client startup as appropriate, world load, login, shutdown and log review.
- **Function test:** exercise the actual feature(s) that justify keeping the mod: item/block interaction, machine process, transport, GUI, world generation, rendering, recipe/loot behavior or synchronization.
- A combined smoke-test pass is not an individual mod-function pass. Do not mark a feature complete just because its mod ID appears in a server log.
- Client-only mods require a matching client launch and client-side review. A dedicated-server log cannot prove their client functions.
- Libraries/APIs are tested through the mod(s) that depend on them; they do not need invented standalone gameplay tests.

## Current pack-level smoke evidence

| Check | Evidence | Status |
|---|---|---|
| Dedicated-server startup | 6 Nov corrected datapack-enabled run reached Done (1.413s) | PASS — disposable profile |
| Disposable world load | `world_lootr_test` loaded | PASS |
| IronWoven compatibility datapacks | All four expected world-scoped packs listed as enabled | PASS — log-level retest |
| Targeted compatibility errors | Design n' Decor, Railways, Create Kinetic, Sable Catwalk, and Create Deco placard errors absent | PASS — log review only |
| Matching client login | Matching client joined in the 6 Nov run | PASS |
| Clean shutdown | All dimensions saved in the 6 Nov run | PASS |
| Individual feature tests | Matrix below | OPEN — mostly not yet function-tested |
| Matching client-only mod startup | Targeted client evidence exists for PowerGrid and local Struts / tooltip workaround tests; no complete isolated optional-client candidate sweep | PARTIAL — optional candidates remain open |
| Production/release approval | Not granted | NOT APPROVED |


## PowerGrid Windows native-load retest — 6 November 2026, 18:29–18:34

**Result: internal Windows native loading and client connection passed. Electrical-network/component behavior is a beta-tester feature check, not another internal maintainer task.** The PowerGrid 0.6.2 JAR was not modified. The official 0.6.1 Windows DLL was copied into the disposable server and CurseForge client `.pg-native` directories. The 18:29 server log and 18:34 client log both reported `Native backend loaded successfully`. The server reached `Done (1.837s)`; the matching client connected to `127.0.0.1:25565` and entered the world. This workaround must not be mistaken for an official 0.6.2 package fix or an accepted modpack change.

- Windows server native load: PASS — disposable profile.
- Windows client native load: PASS — matching CurseForge profile.
- PowerGrid electrical network / component behavior: DEFERRED TO BETA TESTERS; not an internal fix-pass task.
- Linux native solver: NOT TESTED — Linux requires the Linux `.so`; do not use the Windows DLL.
- Production files and modpack manifest: unchanged.

## Historical snapshot — existing-mod update trial, 5 November 2026, 13:43

**Historical record only — not the current installed-mod list.** The Entity Culling entry below records detection in this old disposable-server folder. Entity Culling was subsequently removed from the current CurseForge `Create World/mods` client profile; the maintainer's 6 November 2026 screenshot confirms it is absent. Do not interpret this old row as a current installation or active test candidate.

**Result: FAILED before server startup completed.** This was a separate disposable-server update attempt, not a replacement for the earlier successful combined smoke test.

| Mod | Version detected | Result |
|---|---:|---|
| Sophisticated Core | 1.5.28.2458 | Detected |
| Sophisticated Backpacks | 3.26.20.2244 | Detected |
| Entity Culling | 1.11.3 | Historical detection in 5 Nov disposable server folder only; removed from current client profile on 6 Nov 2026 |
| Create Crafts & Additions | 1.7.2 | Detected |
| Create: Numismatics | 1.1.0 | Dependency conflict with Numismatics Plus 1.0.1 |
| Create: TFMG Community Edition | 1.3.3 | Detected |
| FTB Teams | Missing | Required by FTB Chunks 2101.1.23 |
| Create: Steam 'n' Rails | 0.3.0-alpha.2 | Beta 2 was not present in this test |

### Startup blockers

- **FTB Teams missing:** FTB Chunks 2101.1.23 requires FTB Teams 2101.1.9 or newer. CurseForge NeoForge 1.21.1 release 2101.1.12 is available as [file 9434081](https://www.curseforge.com/minecraft/mc-mods/ftb-teams-forge/files/9434081).
- **Numismatics mismatch:** Numismatics Plus 1.0.1 requires exactly Numismatics 1.0.20. Restore [Numismatics 1.0.20, CurseForge file 7948018](https://www.curseforge.com/minecraft/mc-mods/numismatics/files/7948018) for the next test, retaining [Numismatics Plus 1.0.1, file 8839718](https://www.curseforge.com/minecraft/mc-mods/create-numismatics-plus/files/8839718).

The server did not reach `Done`, load a world, accept a client, or complete a normal shutdown. ImmediatelyFast, Flerovium, Entity Culling, and More Culling were also detected in the dedicated-server folder; these rendering mods belong on the client and need separate client testing.

**Outcome of this historical attempt:** dependency and folder blockers were addressed in later disposable test profiles; see later dated retests and the current `MODS.md` inventory. Do not use this old next-gate text as current setup instructions.


## Historical snapshot — previous existing-mod update retry, 5 November 2026, 13:58

**Result: Partial server startup/world-load pass.** The retry used a disposable server. FTB Teams 2101.1.12 was detected and initialized, and the server reached `Done (1.493s)!` after preparing `world_lootr_test`. The supplied server/debug logs do not show a matching client login or a clean shutdown.

| Mod | Detected version | Result |
|---|---:|---|
| Sophisticated Core | 1.5.28.2458 | Detected |
| Sophisticated Backpacks | 3.26.20.2244 | Detected |
| Entity Culling | 1.11.3 | Historical detection in the 5 Nov disposable server folder; removed from current client profile on 6 Nov 2026 |
| Create Crafts & Additions | 1.7.2 | Detected |
| Create: The Factory Must Grow Community Edition | 1.3.3 | Detected |
| FTB Teams | 2101.1.12 | Detected and initialized |
| Create: Numismatics | 1.0.20 and 1.1.0 JARs found; 1.1.0 selected | 1.0.20 was not active in this run |
| Numismatics Plus | Not present in runtime list | Compatibility not tested |
| Create: Steam 'n' Rails | 0.3.0-alpha.2 | Beta 2 not tested |

Do not keep both Numismatics versions in one `mods` folder. Test Numismatics Plus 1.0.1 with Numismatics 1.0.20 only. Test Numismatics 1.1.0 separately without Plus until a compatible Plus release is verified.

At the time of this historical retry, ImmediatelyFast, Flerovium, Entity Culling, and More Culling were noted as client-only files found in the disposable dedicated-server folder. This does not describe the current client profile. The earlier 6 November 15:12 log contained 463 ERROR-level entries, but its new disposable world's `datapacks/` folder was empty, so the recurring Design n' Decor / Steam 'n' Rails / Create Kinetic / Sable / Create Deco entries did not test the maintained compatibility datapacks. The corrected 15:54 run enabled all four packs and those targeted errors were absent. The corrected run contains 6 ERROR-level records and 172 WARN-level records; remaining error findings are Struts, PowerGrid, Every Compat, Create Aeronautics Structures, and the Shulker Box Tooltip / Supplementaries integration.

**Historical next gate — superseded:** the 14:09 and 22:27–22:31 follow-ups below completed the routine smoke sequence and corrected Numismatics runtime selection for that disposable profile. This retry itself was not a complete smoke-test pass or release approval. Current inventory is maintained separately in `MODS.md`.


## Corrected compatibility datapack smoke retest — 6 November 2026, 15:54

The disposable `world_lootr_test` run enabled all four IronWoven world-scoped datapacks. Server startup, world load, matching client login, and clean shutdown with all dimensions saved passed. The log-level checks found no targeted Design n' Decor (256), Steam 'n' Rails (192), Create Kinetic (5), Sable Catwalk selector, or Create Deco placard parsing errors. This does not mark the affected gameplay drops or recipes as function-tested.

The log contains 6 ERROR-level records and 172 WARN-level records. Remaining errors: Struts dedicated-server `RenderSystem`; PowerGrid optional `powergridNative7`; Every Compat duplicate Herbs & Harvest Golden Cherry Leaves registration; Create Aeronautics Structures `cr_aero_structures:chests/uniform`; and the Shulker Box Tooltip / Supplementaries dedicated-server `PreviewRenderer` integration failure. InControl read `areas.json`. See the private maintainer's detailed report for full triage.

## Existing partial function evidence — do not overstate it

- **Curios:** two Back slots and one Head slot appeared in a newly created test world. Backpack + standard Create Backtank, Aviator Goggles and Linked Typewriter use were reported working in their assigned slots. Full matching client/server synchronization and older-player saved-slot correction remain separate.
- **Lootr:** the maintainer confirmed a test chest opened and contained loot. Independent personal loot for a second player is not yet verified.
- **Every Compat:** Chipped Carpenter's Table modded-wood variants and the stone table were reported working. This is partial; duplicate Golden Cherry Leaves registration and the large compatibility-block footprint remain recorded.
- **Create Aeronautics Structures:** the test-only uniform loot-table override passed runtime testing; one Overworld airship was located and visually confirmed in the disposable Windows world. Other structure variants remain unverified and the official JAR remains unchanged.
- **Batch A:** JER, Enchantment Descriptions and Shulker Box Tooltip passed combined startup/login smoke testing. A later 6 November test exposed a dedicated-server error in the Shulker Box Tooltip / Supplementaries provider integration; Shulker Box Tooltip's own providers still registered. Feature rendering/use remains to be checked.
- **Batch B:** Nature's Compass and Explorer's Compass passed combined startup/login smoke testing; actual biome/structure searches remain to be checked.
- **Batch C:** Create Big Cannons and Ritchie's Projectile Library passed combined startup/login smoke testing; cannon operation remains to be checked.
- **Client-only rendering candidates:** Entity Culling is removed from the current CurseForge client profile (confirmed by the 6 November screenshot) and is not in the active test queue. ImmediatelyFast, Flerovium and More Culling remain optional candidates only; verify their presence against a fresh client export before testing. spark profiling is deferred to beta testers and is not an internal development gate.

## How to complete this checklist

For each feature mod, mark its function complete only after the listed primary behavior works on the intended side(s). Where a mod adds several independent systems, test each system, not just one decorative block. For persistent machines, vehicles, storage, claims, portals and player data, include save/restart or relog. For multiplayer-dependent features, use a second player. Record exact version, test world/profile, relevant log and result.

Use JEI/creative inventory to locate representative items, but item visibility alone is not a functional pass. You do not need to test every recipe or decorative variant; test the primary function and each distinct subsystem.

**World-generation safeguard:** all biome/structure checks use a fresh disposable Overworld. Keep production world, BYG 2.6.3, Regions Unexplored 0.6.3 and active world-generation JSON unchanged. End research remains paused.

**Status meanings:** Pending = not function-tested; Partial = some behavior confirmed but listed test remains open; Pass = all listed primary functions have evidence; Failed/Blocked = reproducible failure or prerequisite prevents validation; N/A = support component checked through dependent mod.

## A. Create, Aeronautics, vehicles and transport

### Create 6.0.10
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Build a kinetic network. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Test speed/rotation control, one press/mixer/deployer chain, item/fluid transport and save/restart. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Create Aeronautics 1.3.2
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Assemble a vehicle. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Test propulsion/lift, steering, controls, collision/physics, disassembly/reassembly and second-player sync. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Create: Simulated 1.3.2
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Test assembly/disassembly, anchoring, controls, redstone interaction, collision and save/reload. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Create: Offroad 1.3.2
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Build a wheeled vehicle. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Test wheel power, steering, traction, stopping, collision and multiplayer sync. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Create Kinetic 1.4.3
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Test its Aeronautics utility/propulsion blocks and items. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Verify hitboxes, particles, controls and physics on client/server. Recheck existing loot-table and mixin findings. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Create Aeronautics Structures 1.1.0-Beta-3.1 (test-only)
**Current status:** Partial — the uploaded JAR metadata matches official CurseForge file 8399115 by version (not a hash comparison). The 16-color test-only datapack override passed runtime loot testing in disposable Windows `world_lootr_test`; the official JAR remains unchanged and the override is not release-approved. All 11 valid Overworld structure IDs have locate/visual-presence evidence, including visually accepted crashed-airship hillside placement; `cr_aero_structures:plane` is invalid. Maintainer spot checks found items in the engineering-house standard and Lootr barrels. One crashed-airship vanilla chest has `Items: []` and no `LootTable` / `LootTableSeed`. Remaining structure/container loot coverage is delegated to beta testers. The specific chest loot-assignment defect and a release-safe uniform-table correction/distribution decision remain open. Visual-presence observations with missing Single-player/Multiplayer attribution are recorded as evidence only, not credited as formal function-test passes.

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Enable the IronWoven Aeronautics Structures uniform-loot test datapack and confirm the uniform-table parse error is absent. | PASS — test-only override | Multiplayer — disposable dedicated server (`MinecraftServer-Test`) / `world_lootr_test`; Windows 11; Minecraft 1.21.1 / NeoForge 21.1.265 | Maintainer | 06-11-2026 | Enabled-pack list contained the ZIP alongside all four existing IronWoven packs; supplied server log contains no recurrence of the targeted parse error. |
| Run `/loot give @s loot cr_aero_structures:chests/uniform` repeatedly and inspect generated loot. | PASS — test-only override | Multiplayer — disposable dedicated server (`MinecraftServer-Test`) / `world_lootr_test` + matching client; Windows 11; Minecraft 1.21.1 / NeoForge 21.1.265 | Maintainer | 06-11-2026 | Repeated commands produced multiple differently dyed leather armour pieces plus iron sword/axe drops in supplied inventory screenshots. The override preserves the original sword/axe/spyglass pools; official JAR unchanged. |
| Fresh disposable Overworld: locate and inspect `cr_aero_structures:airship`. | PASS — airship located and visually confirmed | Disposable `MinecraftServer-Test` / `world_lootr_test`; Windows 11; Minecraft 1.21.1 / NeoForge 21.1.265 | Maintainer | 06-11-2026 | `/locate structure cr_aero_structures:airship` returned a nearest location about 2,575 blocks away; teleport to `(-2783.5, 82, -3375.5)` showed the generated airship deck and fittings in the supplied screenshot. This is one-variant evidence only. |
| Review presence and placement of all valid Overworld structure IDs. | VISUAL EVIDENCE RECORDED — 11 valid IDs; not credited as formal function pass because exact Single-player / Multiplayer mode was not recorded | Disposable Overworld; exact Single-player / Multiplayer mode not recorded | Maintainer | 06-11-2026 | Evidence in the private report covers `airship`, `boat`, `engineering_house`, `airballoon`, `crash_airballoon`, `crash_pillager_airballoon`, `crash_pillager_airship`, `crash_plane`, `pillager_airballoon`, `pillager_airship`, and `crash_airship`. Crashed-airship hillside placement was visually accepted. `cr_aero_structures:plane` is invalid and is not counted. |
| Inspect engineering-house standard and Lootr barrel contents. | OBSERVATION ONLY — items were visible; not credited as a formal feature pass because exact Single-player / Multiplayer mode was not recorded | Disposable Overworld; exact Single-player / Multiplayer mode not recorded | Maintainer | 06-11-2026 | Standard barrel contained items. Lootr barrel generated multiple item stacks after first opening. |
| Inspect the crashed-airship vanilla chest block entity. | FAIL — this specific chest has `Items: []` and no `LootTable` / `LootTableSeed` | Disposable Overworld; exact Single-player / Multiplayer mode not recorded | Maintainer | 06-11-2026 | Chest at `(-835, 105, -6752)` was inspected with `/data get block`; this is a specific loot-assignment failure, not evidence that every Aeronautics chest is affected. |
| Check remaining structure/container loot and trader behavior. | DELEGATED TO BETA TESTERS — pending individual reports | Not recorded | Not recorded | DD-MM-YYYY | Test during normal exploration. Report structure variant, container type, whether items appear after opening, approximate coordinates, and screenshot/log evidence where practical. |

### Create Aeronautics Curios Compat 2.0
**Current status:** Partial — assigned-slot checks user-reported working; repeatable synced test still needed.

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Equip Aviator Goggles in Head slot. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Test overlay/engineer detection. Equip Linked Typewriter in Curios and activate (default Y) to operate linked typewriter/Redstone Links. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Create Aeronautics: Copycat Wing 1.0.4
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Use a Copycats+ block as a wing part. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Verify lift. Honeycomb should disable lift and axe restore it. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Test on a moving contraption. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Create Aeronautics: Transmission & Linkage 0.2.9
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Build a transmission/linkage assembly. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Verify it transfers the intended movement/control across running and assembled contraptions. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Create Big Cannons 5.11.7
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Assemble a multiblock cannon. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Load projectiles/fuzes. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Test Create-powered loading/aiming, firing, projectile effect/recoil, reload and autocannon if used. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Create: Steam 'n' Rails 0.3.0-alpha.2
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Assemble/run a train. | Pass | Not recorded | Ghosty | 03-11-2026 | I made the train and drove it back and forth a couple of times. (submitted in issue #5) |
| Test tracks, bogeys, schedules/stations, signals and installed railway interactions. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Verify save/restart. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Create: Blocks & Bogies 1.0.8
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Open bogie UI (crouch + right-click empty-handed) | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Configure drivers/axles, assemble train and verify style and operation. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Create: Modern Train Parts 0.2.5
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Test pantograph deployment/retraction, shipping-container storage, wrench variants and train movement with parts attached. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Create: Pantographs & Wires 0.2.3-C6 Beta
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Place masts/cantilevers and catenary. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Verify wire connection and pantograph height adjustment on a moving train, including slopes/turns. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Create: Rustic Structures 1.0.1
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Fresh disposable Overworld: find well, smithy, windmill and barn in intended biome groups. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Inspect placement, loot and generation. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Create: Structures Arise 176.49.50
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Fresh disposable Overworld: find multiple Create-themed structures. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Inspect integrity, placement, loot and chunk-edge generation. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Create: Aeronautical Diesel 1.1.0
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Use tank/fill port to move diesel, biodiesel, gasoline, ethanol, crude oil or plant oil into an Aeronautics portable engine. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Test wrench and automation. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Create: AeroPortals 1.3.6
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Move a complete airship through vanilla and supported modded portals. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Verify ship, pilot, passengers and decorations arrive intact. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Shield Generators 1.4.0
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Power a shield generator. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Test activation, energy draw, boundary visualization, protection/interaction and multiplayer consistency. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### KineticGrip 1.0.5
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Test the Aeronautics handles from the player point of view. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Operate the handle controls and any player-usable tool (such as the chainsaw) included by the installed build. Verify movement/control and client/server interaction. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Sable 2.0.6
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Test Aeronautics physics: assembly, motion, forces, collision, sublevels and save/restart. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Inspect Copycats Catwalk physics-tag errors. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Strut Your Stuff 1.3.1
**Current status:** Partial — local patched server/client test passed for the dedicated-server mixin issue and the shown Struts components render, but dependent-mod feature tests remain pending. The official CurseForge file and modpack manifest are unchanged, so release-level resolution remains open.

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Validate through dependent mods: spanning/collision structures, surface clipping, interaction and cable behavior/droop. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Check dedicated-server RenderSystem class-loading issue. | Passed on local patched profile | Disposable MinecraftServer-Test + matching CurseForge Create World profile; Minecraft 1.21.1 / NeoForge 21.1.265 | Not recorded | 06-11-2026 | 16:40–16:47 server/client/debug logs contain no RenderSystem or StrutRenderSystemAccessor; server reached Done, client joined, clean shutdown. Local patched JAR is not part of official CurseForge manifest. |
| Inspect visible Struts beams/girders in-game. | Passed for shown examples | Disposable MinecraftServer-Test + matching CurseForge Create World profile | Not recorded | 06-11-2026 | 16:46 screenshots show metal Struts components rendering. Client log still warns that both waterlogged variants of girder_strut_structure have missing models; not every variant tested. |
## B. Create automation, energy, industry and build addons

### Create: Bits 'n' Bobs 2.3.5
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Test chain-drive transfer/carriage attachment, flywheel bearing rotation/battery behavior, wooden cogwheel swapping, dyeable fluid-pipe separation, chair and Nixie display. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Create Cobblestone 1.5.1
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Set generator to cobblestone, stone, basalt, limestone and scoria. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Verify outputs, type switching, SU use and disabled-generator behavior. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Create Crafts & Additions 1.7.2
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Run Electric Motor from FE and verify SU output. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Drive Alternator with SU and verify FE output. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Test rolling-mill rods/wires. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Create: Curios Backtank 1.0.2
**Current status:** Partial — Backpack + standard Backtank use in configured Back slots was reported; refill/consumption still open.

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Equip Backtank with intended Curios/backpack setup. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Test air capacity, refill, consumption and rendering/slot behavior. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Create Deco 2.1.3
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Test decorative blocks/variants, recipes, placement, rotation and drops. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Recheck placard fix and loot-table parsing. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Create: Diesel Generators 1.3.15
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Run an oil-to-fuel chain. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Start diesel generator and test FE output, fuel consumption, upgrades and a representative machine/tool. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Create Encased 1.10.0-fix1
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Apply casings to shafts, cogwheels and pipes. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Test rotation, power/fluid transfer and persistent casing visuals. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Create: Gadgets & Gizmos 1.2.10 (bundled)
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Test installed gadgets/engine components used by Aeronautics: assembly, thrust/control, fuel/power consumption and contraption synchronization. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Create: Dragons Plus 1.11.9
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Use an Encased Fan to test Bulk Coloring with dye fluid, Bulk Freezing with Powder Snow, Bulk Ending with Dragon Head or Dragon's Breath fluid, and Bulk Sanding with Quicksand/supported block tag. Test Fluid Hatch take/deposit behavior on tanks and supported addon recipe integrations. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Create: Liquid Fuel 3.0.0
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Feed supported liquid fuel to a Blaze Burner. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Verify normal/superheated operation, duration, consumption and rejection of invalid fluids. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Create: Fluids Be Gone! 1.0.1
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Run a Create Drill and a Simulated Rock Cutting Wheel into fluid-containing terrain. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Verify fluids in the mined path are voided when enabled, separate drill/rock-wheel config switches work, and fluids outside the mining path remain unchanged. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Create: Framed 1.8.2
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Build framed blocks, apply a supported material/appearance and shape. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Verify placement, rotation, breaking and reload. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Create: Enchantment Industry 2.5.4b
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Run automated enchanting/disenchanting and XP-fluid processing. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Verify inputs, outputs, XP/fluid handling, recipes and automation. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Create: Numismatics 1.0.20
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Obtain coins. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Use Vendor for buy/sell, Bank Terminal for deposit/withdraw, and Depositor price/redstone pulse for coin/card payments. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Create: Numismatics Plus 1.0.1
**Current status:** Hold — JAR is archived in `MinecraftServer-Test/mods-disabled`; not installed in the current server test profile. Reintroduce only for a separate pairing test with Numismatics 1.0.20.


| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Buy from a Create shop with coins and a Numismatics card. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Verify deduction, stock, recipient account and missing-Depositor/card behavior. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Create: Pattern Schematics 2.0.10
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Create/obtain a repeating schematic. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Print in creative or use Schematicannon. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Verify placement, orientation, repeat behavior and resource requirements. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Create: Power Grid 0.6.2
**Current status:** Partial — internal Windows native loading and client connection passed using the official 0.6.1 Windows DLL in disposable `.pg-native` folders while keeping PowerGrid 0.6.2 unchanged. Electrical-network/component behavior is reserved for beta testers, not another internal maintainer task. Linux is a separate future platform test requiring its own `.so`. The local DLL workaround is not part of the distributable beta package; a release-safe native-resource packaging decision remains open.

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Diagnose missing `powergridNative7` on server and client. | Root cause confirmed — 0.6.2 package omits native binaries | Disposable MinecraftServer-Test + CurseForge Create World; Windows 11 x64; Minecraft 1.21.1 / NeoForge 21.1.265 | Maintainer | 06-11-2026 | Matches upstream [PowerGrid issue #1165](https://github.com/patryk3211/PowerGrid/issues/1165). |
| Restore 0.6.1 Windows native DLL to server and client `.pg-native` folders. | **Passed — server and client native loading** | Disposable server + matching CurseForge profile | Maintainer | 06-11-2026 | Server `latest(20261106-173022).log` (18:29) and client `latest(20261106-173558).log` (18:34) both report `Native backend loaded successfully`. Server reached `Done (1.837s)`; client connected to `127.0.0.1:25565` and entered the world. PowerGrid 0.6.2 JAR unchanged. |
| Build and operate a small electrical network with source, compatible wires, transformer (if used), and consumers. | **Reserved for beta testers — not part of internal fix pass** | Beta release package / target test platform | Beta tester | During beta | Verify network formation, power delivery, stability, solver errors, and whether the beta package includes the platform-native library or uses Java fallback. Record logs and platform. |
| Test components and Java fallback separately. | **Reserved for beta testers** | Beta release package / target test platform | Beta tester | During beta | Exercise representative PowerGrid components with the release package. Record whether native or Java fallback is active and any behavior/errors. |
| Record Linux native solver separately. | Future platform validation — not yet available | Linux test host (not yet set up) | Maintainer / tester | When Linux host is ready | Linux requires `native/linux/libpowergridNative7.so`; never use the Windows DLL on Linux. |
### Create: Sound of Steam / Pipe Organs 0.9.2.1
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Place/configure a pipe organ. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Trigger notes manually and by supported controls/redstone. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Test pitch, sound, range, persistence and multiplayer audio. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Create: The Factory Must Grow Community Edition 1.3.3
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Run representative industrial processing: fluid/oil input, machine processing, outputs, power/kinetic requirements and fuel-burning machine. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Test Unified Fuels integration. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Create: Unified Fuels 1.0.4
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Cross-feed fuels between supported addons and compatible engines, burners and trains. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Verify shared values/consumption, gas-vs-liquid rules, toggles and config after restart. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Create: Vibrant Vaults 0.3.2
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Build/connect vaults and shipping containers. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Insert/extract items, change color/orientation and test package frogport/stock link/packager features present. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Create Slice & Dice 4.3.4
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Automate a Farmer's Delight cutting-board recipe with Create saw. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Verify ingredients, output, transport and recipe visibility. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Create: Bells & Whistles 0.4.7
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Test representative decorative train/building blocks, variants, placement, rotation, collision and rendering on moving contraptions. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Create: Copycats+ 3.0.9
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Use copycat shapes with multiple source materials. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Verify appearance, shape/state, rotation and moving-contraption rendering. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Copycats+ Additions 1.5.0
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Test added copycat shapes/variants, material application and placement. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Verify Aeronautics Copycat Wing integration. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Design n' Decor 2.2b
**Current status:** Pending — startup passed; logs contain many loot-table parse errors. Drop behavior remains open.

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Test representative decoration families, recipes and drops. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Specifically verify dyed cogwheel/loot-table entries and intended block drops. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

## C. Building, food, storage, world generation and exploration

### Chipped 4.0.2
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Use workstations on vanilla/modded wood and stone. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Craft several variants, place/break them and verify drops/models. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Farmer's Delight 1.3.4
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Run a food chain: ingredients, cutting-board processing, cooking pot, finished meal and food effects. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Test container interactions. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Mama's Herbs and Harvest 1.21.1-24
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Plant/harvest representative crops and herbs. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Test growth stages, drops, food/processing recipes and Botany Pots integration. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Botany Pots 21.1.44
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Plant vanilla, BYG/RU and Herbs & Harvest crops. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Test growth/harvest, drops, hopper input/output automation and JEI. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Construction Sticks 1.5.0
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Place a small wall/floor pattern. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Verify direction, range, item use, limits, claim protection and stop/undo behavior. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Every Compat 2.11.57
**Current status:** Partial — the paired 2.11.57 + Moonlight 3.8.2 runtime smoke test passed and was accepted for the baseline; duplicate Golden Cherry Leaves registration and large block footprint remain. Block/recipe/model/texture/drop feature checks are delegated to beta testers.

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Test Chipped Carpenter's Table variants for several modded woods plus supported Create/Farmer's Delight/RU compat. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Verify recipes, models, drops and client/server registry sync. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Lootr 1.11.38.127
**Current status:** Partial — chest opening and loot presence user-confirmed; second-player personal loot unverified.

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Have two players open the same generated Lootr chest. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Verify independent personal loot, container persistence and multiplayer synchronization. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Sophisticated Backpacks 3.26.20.2244
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Craft/open backpack. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Test storage, upgrades, filters/automation, pickup and save/relog persistence. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Sophisticated Backpacks Create Integration 0.2.3
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Test supported Create inventory/item transport with backpack. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Verify insertion/extraction and normal backpack behavior. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Sophisticated Air Tank 1.0.1-beta
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Equip/refill air tank. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Test air supply/consumption, capacity indicator and supported backpack/Curios interactions. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Oh The Biomes We've Gone 2.6.3
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Fresh disposable Overworld: verify representative BYG biomes, vegetation/trees, structures and biome-specific terrain. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Check configs/datapacks. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Regions Unexplored 0.6.3
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Fresh disposable Overworld: verify representative RU biomes, vegetation, trees and biome blocks. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Check biome edges and Create integration. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Fresh disposable Nether: use biome lookup and explore new chunks to confirm representative Regions Unexplored Nether biomes generate; keep the production world unchanged. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Oh The Trees You'll Grow 5.3.5
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Grow representative added trees. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Test sapling growth, leaves/log drops, wood sets and leaves decay. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
 
### Integrated Villages 1.3.3+1.21.1 (Overworld candidate)
**Current status:** Partial — corrected dependencies load; multiple village IDs are locatable, but full structure and performance validation remain open.

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Inspect representative generated structures (including Airship and Mediterranean villages) in a fresh disposable Overworld. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Check Cabin Village decoration pool warning and verify that structures are complete, populated, and have intended loot. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Compare locate/generation responsiveness; prior structure searches took roughly 10–37 seconds and caused server tick-delay warnings. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Confirm whether vanilla village generation is intentionally retained. Do not assume Integrated Villages replaces every vanilla village. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Save/restart the disposable world and review the matching server/client logs. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

Dependency evidence: the first startup attempt lacked Supplementaries and Integrated API 1.6.2+. The corrected test profile used Create 6.0.10, Supplementaries 3.4.0, and Integrated API 1.9.1 and reached `Done`. Validate these libraries through Integrated Villages; no standalone function test is required.

### Atmosphere 1.0.18
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Fresh disposable world: verify its advertised environment/atmosphere changes. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Check day/night, weather, visuals/audio and client/server consistency. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Create Oh The Biomes We've Gone Compatibility 0.0NONE
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Check compatibility items/recipes/blocks for BYG and Create. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Test JEI presence, placement, drops and wood/biome integration. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Nature's Compass 3.4.0
**Current status:** Smoke-only — Batch B startup/login passed; actual search behavior not tested.

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Search for a known biome in disposable world. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Verify result, distance/direction, no-result message and repeat search. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Explorer's Compass 3.4.0
**Current status:** Smoke-only — Batch B startup/login passed; actual search behavior not tested.

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Search for a known generated structure. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Verify correct result, distance/direction and updated search after discovery. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Create Structures Arise 176.49.50
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Fresh disposable Overworld: find multiple Create-themed structures. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Inspect integrity, loot, biome placement and chunk-edge generation. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

## D. Player interface, server tools and information mods

### AppleSkin 3.0.9
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Check hunger, saturation and exhaustion HUD while eating, sprinting and regenerating. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Compare to expected vanilla values. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### FTB Chunks 2101.1.23
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Claim/unclaim test chunk. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Verify map, team permissions, boundaries, force-load controls, protection and reconnect persistence. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### FTB Teams 2101.1.12
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Create team. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Invite/remove second player. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Check ownership/permissions and FTB Chunks team-claim behavior. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### InControl! 10.3.1
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Test active spawn/loot/experience rules under controlled conditions. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Verify allowed/blocked mobs/loot and restart persistence. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Jade 15.10.6
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Inspect vanilla/modded blocks and entities. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Verify tooltips, states, inventories/fluid data and Create/Aeronautics compatibility. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Just Enough Items 19.64.0.455
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Search representative items from each content group. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Inspect crafting/processing recipes, catalysts and fluid inputs. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Just Enough Resources 1.6.0.57
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Check known mob-drop, loot-table, villager-trade and world-generation entries against in-game sources. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Enchantment Descriptions 21.1.11
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Open tooltips for vanilla/modded enchanted books and items. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Verify accurate descriptions and layout. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Shulker Box Tooltip 5.1.9+1.21.1
**Current status:** Partial — local Supplementaries Sack and Lunch Basket previews now visually pass, and the client config workaround suppresses the dedicated-server `PreviewRenderer` error. Generic filled-shulker preview behavior and the release trade-off for disabling server integration remain untested. Upstream [issue #263](https://github.com/MisterPeModder/ShulkerBoxTooltip/issues/263) remains relevant.

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Hover filled vanilla/modded shulker boxes and verify contents, counts, scroll/page behavior. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Keep separate from Supplementaries provider tests; add screenshot evidence here. |
| Test dedicated-server login with client `preview.serverIntegration=false`. | Passed — repeated log-level handshake suppression | Disposable MinecraftServer-Test + matching CurseForge Create World profile; Minecraft 1.21.1 / NeoForge 21.1.265 | Not recorded | 06-11-2026 | Fresh server log has no PreviewRenderer or failed Supplementaries provider registration. Client registered 3 Supplementaries and 31 SBT providers locally; player joined and left before clean shutdown. |
| Test local Supplementaries Sack and Lunch Basket previews with server integration disabled. | **Passed — visual** | Disposable MinecraftServer-Test + matching CurseForge Create World profile; Minecraft 1.21.1 / NeoForge 21.1.265 | Not recorded | 06-11-2026 | Screenshots at 17:39–17:40 show Sack nine-stack 3×3 preview and opened Sack GUI; Lunch Basket shows stored food stacks, Closed state and four-stack summary. |
| Assess the release trade-off for disabling server integration. | Pending | Not recorded | Not recorded | DD-MM-YYYY | Remote/server-supplied extras such as Ender Chest synchronization are unavailable while `preview.serverIntegration=false`. Decide whether this is acceptable for the pack or wait for upstream server-safe fix. |

### Mouse Tweaks 2.26.1
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Test drag distribution, wheel scrolling and quick-move in player inventory, chests, backpacks and modded GUIs. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Memory Settings 6.0
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Verify settings apply and persist across restart. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Measure memory only in controlled same-workload comparison, not from startup alone. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### ModernFix 5.27.27
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Verify selected optimization mixins/options on the same disposable test profile. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Review for mixin errors, changed gameplay behavior, save integrity and comparable startup/runtime metrics. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

## E. Client graphics and performance mods

### Sodium 0.8.13 (client-only)
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Launch matching client. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Verify rendering of chunks, Create moving contraptions, Aeronautics ships and block entities. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Compare same-scene FPS/frame pacing. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Iris 1.8.14-beta.1 (client-only)
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Toggle shader pack. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Inspect Create/Aeronautics models, ship sublevels, water, particles, HUD and shadows. Record known Aeronautics/Iris visual artifacts. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Sodium Extra 0.9.5 (client-only)
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Change a Sodium Extra option. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Verify it applies, persists after restart and does not conflict with Iris/Sodium. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### ImmediatelyFast 1.6.15 (client-only)
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Compare identical GUI, HUD, particles, item/entity and block-entity scenes enabled/disabled. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Check visual parity and client log. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Flerovium 1.1.3 Beta (client-only; detected build)
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Compare item, particle and entity rendering/FPS against same Sodium baseline. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Inspect artifacts. Stable 1.1.2 remains a separate planned candidate. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Entity Culling — removed from current client profile

The 6 November 2026 CurseForge `Create World/mods` screenshot confirms Entity Culling is absent from the current client mod folder. No further client functional test is planned unless the maintainer explicitly re-adds it.

### More Culling 1.0.11 (client-only)
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Check leaves, glass, connected textures and modded blocks across chunk boundaries. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Ensure no missing faces/transparency errors. Test Cloth Config options. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### spark 1.10.124 (server profiler)
**Current status:** Deferred to beta testers — not required during internal development.

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| During beta testing, record TPS, MSPT, memory/GC, and CPU under a repeatable load; save a 2–5 minute profile. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Record the selected profiler engine and any platform-specific fallback. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

## F. Libraries, APIs and shared support components

### Apollib 1.2.0
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Verify dependent mod registries/content and related GUI/network interaction. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Record owner mod. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Architectury 13.0.11
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Verify dependent mods initialize on client/server and shared event/network hooks work during login and interaction. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Athena 4.0.6
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Verify dependent content models/textures render. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Check for missing model/texture errors. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Azimuth 1.4.10
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Verify mods depending on Azimuth load and shared utility/render behavior works. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Check class-loading logs. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Bookshelf 21.1.81
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Verify dependent features (e.g. Enchantment Descriptions/Botany Pots) load and work. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Dependency-only. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Cloth Config API 15.0.140
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Open More Culling config. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Change/save option, relaunch and verify persistence. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### CodecUI 1.4.7
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Open dependent settings/config interface. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Verify widgets, values and save/cancel behavior. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Conditional Mixin 0.6.4
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Verify dependent mixins activate under intended mod/config conditions. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Check mixin apply failures. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### CorgiLib 5.0.0.10
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Verify dependent mod initializes and required shared utilities work. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Check missing-class/registration errors. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Cupboard 4.2
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Verify Memory Settings and other dependent config integrations initialize and read/write settings. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Curios API 9.5.1
**Current status:** Partial — two Back + one Head slot and selected item uses were reported in new-world checks; full sync/older-player data still open.

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Verify slot registry, counts, equip/unequip, client/server sync and persistence with Aeronautics/Backtank. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### DragonLib 3.0.29
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Verify dependent DragonLib consumers (including Pantographs & Wires) register, render and execute their behavior. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Ferrite Core 7.0.3
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Capture memory baseline and compare same workload in disposable clone. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Check startup/registry stability. Do not alter production based only on benchmark. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Flywheel 1.0.6
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Verify Create contraption rendering, instancing, moving block entities and animation on matching client. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Forge Config API Port 21.1.1
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Open dependent mod config GUI, change value, save/restart and verify persistence. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Forgified Fabric API Base 0.4.42
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Verify bundled/using mods load and required API calls work. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Dependency-only. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Forgified Fabric BlockView API 1.0.10
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Verify renderer/block-view integration used by Flerovium loads and block rendering stays correct. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Forgified Fabric Renderer API 3.4.1
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Verify renderer-dependent mod integration and item/block rendering. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Dependency-only. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Forgified Fabric Rendering Data Attachment 0.3.48
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Verify renderer data attachments survive chunk/entity render updates without visual corruption. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### FTB Library 2101.1.39
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Verify FTB Chunks/Teams menus, shared data, keybinds and networking. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Dependency-only. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### FTB XMod Compat 21.1.14
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Verify selected team/stage/permission integration is detected and behaves correctly. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Gadgets & Gizmos Library 1.2.10
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Verify bundled G&G content registers and dependent contraption controller/graph utilities work. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### GeckoLib 4 4.9.3
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Verify animated entities/blocks and Aeronautics Structures visuals animate correctly on client. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Kotlin for Forge 5.12.0
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Verify Kotlin-based dependent mods initialize and execute entry points. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Dependency-only. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Lithostitched 1.8.1
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Verify BYG/RU biome and feature registration in fresh disposable Overworld. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Check registry conflicts. Preserve production worldgen. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### MezzConfig 0.6.10
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Verify config interface opens and dependent config screens load/save. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Standalone and bundled copies must not duplicate. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Moonlight Lib 3.8.2
**Current status:** Partial — accepted as Every Compat 2.11.57's required dependency after the paired Windows runtime smoke test; feature-level dependent behavior remains assigned to beta testers.

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Verify dependent features (including Every Compat) register resources/models without duplicate registry errors. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Ponder 1.0.82
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Open Ponder scenes for representative Create/addon blocks. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Confirm scenes render and advance. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### PrickleMC 21.1.11
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Verify Botany Pots dependency/plugin initialization and crop/soil compatibility. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Dependency-only otherwise. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Resourceful Lib 3.0.12
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Verify dependent resource registries/config/content load. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Check missing resource errors. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Ritchie's Projectile Library 2.1.2
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Verify through Create Big Cannons: projectile and fuze definitions register, load and fire correctly. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Confirm client/server projectile synchronization. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Sable Companion 1.6.0
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Verify dependent Sable integrations load and register expected physics behavior. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| No separate feature assumed. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Sophisticated Core 1.5.28.2458
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Verify backpack upgrade/inventory modules initialize and retain data after close/reopen, relog and restart. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### TerraBlender 4.1.0.8
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Verify BYG/RU biome providers register in intended dimensions of fresh disposable world. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| No missing/duplicate regions. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### TRansition 1.0.21
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|

### TRender 1.0.15
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Verify dependent render integration and UI/model path. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| No missing renderer/client crash. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

### Veil 4.3.2
**Current status:** Pending

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Verify Veil-dependent rendering/effects initialize on client and remain correct with Sodium/Iris. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |

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

## Historical smoke-test record — 5 November 2026, 14:09

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
| ImmediatelyFast / Flerovium / Entity Culling / More Culling | Historical 5 Nov server-folder detection; not a current client inventory |
| spark | 1.10.124 initialized; built-in Java engine selected on Windows 11 / amd64; no numeric baseline or saved profile |

Historical 5 November archive note. The later 22:27–22:31 runtime record confirmed Numismatics 1.0.20 alone in that disposable profile. Never combine two Numismatics versions in one profile. Do not infer current client installation from the old server-side `mods-disabled` archive.

### Error review

The log contains **463 ERROR-level entries and 172 WARN-level entries**. The errors include 454 loot-table parse errors (Design n' Decor 256, Steam 'n' Rails 192, Create Kinetic 5, Create Aeronautics Structures 1), three Sable unknown Catwalk selectors, one Struts dedicated-server `RenderSystem` error, one PowerGrid optional native-backend error, three Every Compat registration/block-count messages, and one Create Deco placard recipe error. Verify relevant world-scoped compatibility datapacks before treating recurring loot-table or Sable errors as regressions. The Aeronautics Structures chest-table issue remains unresolved and Batch D remains partial. The 12,288 MB allocation warning exceeds the pack's stated 8,500 MB recommendation but did not block this run.

spark did not produce TPS/MSPT, CPU, memory/GC measurements, or a saved profiler report. Batch E remains partial. Individual feature tests remain open in the matrix below; no function row is passed by this smoke test.


## Historical archive record — disabled server-folder snapshot, 5 November 2026, 17:58

A new screenshot shows `MinecraftServer-Test/mods-disabled`. It confirms the following files are archived outside the active dedicated-server mods folder:

- End test files: BetterEnd 21.0.39, YUNG's Better End Island 3.1.2 and YUNG's API 5.1.9. End testing remains paused.
- Historical server-side archive contents: Entity Culling 1.10.4 and 1.11.3, Flerovium 1.1.3, ImmediatelyFast 1.6.15, More Culling 1.0.11, Sodium 0.8.13, Sodium Extra 0.9.5 and Iris 1.8.14-beta.1. These archive records do not describe the current client profile. The 6 November 2026 client-folder screenshot confirms Entity Culling is now absent from the current profile.
- Superseded older copies: Create Crafts & Additions 1.6.0, Create: Enchantment Industry 2.4.2, FTB Teams 2101.1.11, Lithostitched 1.7.11, Sophisticated Backpacks 3.26.19.2243, Sophisticated Core 1.5.23.2446 and TFMG 1.3.2a-community. Newer versions are recorded in the active test inventory.
- Numismatics 1.1.0 and Numismatics Plus 1.0.1 are archived. The current server test is to keep Numismatics 1.0.20 only; Plus is not active and its pairing test is on hold.
- Tracks 1.0.1 and Tracks Plus 1.0.6b7 are archived legacy candidates; the screenshot does not establish their original reason for removal.
- `createkinetic-1.4.3.jar.original.bak` is a backup file, not an active mod.

This is an archive-folder observation, not a fresh filesystem scan. It does not establish a client-profile inventory or a performance improvement. Do not mark any functional test passed or rejected solely because a JAR is archived.


## Historical retest record — server run, 5 November 2026, 22:27–22:31

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

- Struts' dedicated-server `RenderSystem` issue does not recur in the 6 November 16:40–16:47 local patched-profile runtime test, and the shown components render. The standard-install/release issue remains open because the local JAR patch is not part of the official CurseForge file or modpack manifest; two `girder_strut_structure` waterlogged-variant model warnings remain.
- PowerGrid 0.6.2's packaged native solver binaries remain omitted upstream. Windows native loading passed in the disposable server and client after copying the official 0.6.1 Windows DLL into both `.pg-native` folders; this workaround is not part of the pack or official 0.6.2 JAR. Electrical circuit behavior remains untested, and Linux still needs a separate `.so` validation.
- Batch D's Aeronautics Structures loot-table / provenance / structure-generation review remains partial.
- World-scoped datapack-dependent errors still need to be interpreted only in worlds where the relevant packs are enabled.

No production world or configuration was changed.

## Every Compat 2.11.57 paired update — accepted 7 November 2026

**Status: accepted baseline target after routine Windows startup/world-load/client-login/clean-shutdown smoke test passed.** The new pair is Every Compat 2.11.57 + Moonlight Lib 3.8.2. The original Create World client profile and normal MinecraftServer-Test dedicated-server baseline are both screenshot-verified with the accepted pair; a startup/login smoke test on this updated baseline remains pending.

- Previous baseline: Every Compat 2.11.56 + Moonlight Lib 3.8.1.
- Accepted baseline target: Every Compat 2.11.57 + Moonlight Lib 3.8.2.
- Tested disposable pair: Every Compat 2.11.57 NeoForge (CurseForge file [9468938](https://www.curseforge.com/minecraft/mc-mods/every-compat/files/9468938)) + Moonlight Lib 3.8.2 NeoForge (file [9458248](https://www.curseforge.com/minecraft/mc-mods/selene/files/9458248)). The 2.11.57 release requires Moonlight 3.8.2 or newer.
- Both updated files loaded on the disposable Windows dedicated server and matching client. The server reached Done, all four IronWoven datapacks were enabled, the client joined, and the server saved all dimensions on shutdown.
- The duplicate Golden Cherry Leaves registration remains on both sides. This update does not resolve the existing duplicate registration issue.
- The CurseForge test entry named Ironwoven - Every Compat Update Test opened the separate IronWoven Age Of Industry instance folder. The original Create World client and normal MinecraftServer-Test server baseline have since been updated with the accepted pair, as confirmed by screenshots.
- The maintainer performed no block, recipe, JEI, model, texture, drop or gameplay feature checks. Those checks are assigned to beta testers and remain pending in the functional-test process. Do not mark any feature row passed from this smoke test.
- The maintainer accepted this pair on 7 November 2026. Feature checks remain untested and delegated to beta testers; do not mark any feature row passed from this smoke test. The local client and normal server baseline folders now both contain the two accepted JARs; the updated-baseline startup/login smoke test remains pending.
## Create Aeronautics Structures uniform loot-table runtime retest — 6 November 2026

**Result: test-only loot-table workaround passed runtime testing; Batch D remains partial.** The maintainer placed `IronWoven-Aeronautics-Structures-Loot-Fix.zip` in the disposable `world_lootr_test/datapacks` folder, keeping all four existing IronWoven packs. The server's enabled-pack list includes the new ZIP, the server reaches `Done (1.788s)`, the matching client logs in, and shutdown saves all dimensions. Repeated `/loot give @s loot cr_aero_structures:chests/uniform` commands produced differently dyed leather armour and iron sword/axe drops in the supplied inventory screenshots. The supplied 19:32–19:38 server log contains no recurrence of the targeted uniform loot-table parse error.

- Uniform loot table with test-only datapack override: **PASS — disposable Windows profile**.
- Official `cr_aero_structures.jar`: **UNCHANGED**; the override is not an upstream correction.
- Overworld structure generation: **NOT TESTED**.
- Release-safe correction / datapack distribution decision: **OPEN**.

The override substitutes a 16-color vanilla dye palette for the invalid full-range RGB number provider. Do not treat this test-only ZIP as an approved release artifact. The same server log also records a separate Every Compat duplicate Golden Cherry Leaves registration error; it is not caused by this Aeronautics Structures override.


## Create Aeronautics Structures boat-generation check — 6 November 2026, 20:00

**Result: abandoned boat structure visually confirmed in the disposable Overworld.** The maintainer supplied an in-game screenshot showing a small wooden boat structure floating on the water, with a deck and visible equipment / storage-like blocks. This confirms a boat structure is present in the tested world. The screenshot does not independently capture the `/locate` output or prove chest loot, trader behavior, or interactive features.

- Boat structure presence: **PASS — visual confirmation, disposable Windows world**.
- Boat chest contents / loot: **NOT TESTED**.
- Other structure variants: **PENDING**.
- Official mod JAR and production world: **UNCHANGED**.


## Create Aeronautics Structures — expanded Overworld generation checks — 6 November 2026

The maintainer supplied screenshots showing locate results, teleports and generated structures in the disposable Windows Overworld.

| Structure ID | Result | Evidence |
|---|---|---|
| `cr_aero_structures:engineering_house` | **PASS — visual** | Timber-and-stone house with teal roof, balcony and villager visible. |
| `cr_aero_structures:airballoon` | **PASS — visual** | Suspended hot-air balloon, envelope and basket visible. |
| `cr_aero_structures:crash_airballoon` | **PASS — visual** | Ground-level crash-site structure and wreckage visible. |
| `cr_aero_structures:crash_pillager_airballoon` | **PASS — visual** | Locate/teleport shown; crash-site pieces visible. |
| `cr_aero_structures:crash_pillager_airship` | **PASS — visual** | Locate/teleport shown; dark balloon craft and platform visible. |
| `cr_aero_structures:crash_plane` | **PASS — visual** | Locate/teleport shown; partially terrain-embedded aircraft wreckage visible. |
| `cr_aero_structures:pillager_airballoon` | **PASS — visual** | Locate/teleport shown; large pillager balloon craft visible. |
| `cr_aero_structures:pillager_airship` | **PASS — visual** | Locate/teleport shown; large pillager airship and gondola visible. |
| `cr_aero_structures:crash_airship` | **PENDING** | No result/evidence supplied yet. |
| `cr_aero_structures:plane` | **INVALID ID** | Minecraft explicitly returned: `There is no structure with type "cr_aero_structures:plane"`. This is not a generation failure; do not retry this ID. |

These passes confirm structure presence and visible generation only, not loot contents, generation frequency, entity behavior or all interactive features. The uniform-loot workaround remains a separate test-only datapack; the official mod JAR and production world remain unchanged.

**Next structure lookup:** `/locate structure cr_aero_structures:crash_airship`


## Create Aeronautics Structures — crashed-airship generation check — 6 November 2026

**Result: structure presence confirmed; terrain placement flagged for review.** The maintainer ran `/locate structure cr_aero_structures:crash_airship`. Minecraft reported a nearest result at approximately `[-848, ~-6768]`, 403 blocks away, and teleported the player to `(-847.5, 198.05, -6767.5)`. The screenshot shows an exposed section of the crash site with a chest and mechanical / track-like blocks, while most of the expected structure appears embedded in or occluded by the hillside.

- Structure ID lookup / presence: **PASS**.
- Visual placement quality: **REVIEW REQUIRED — appears partially buried / terrain-occluded**.
- Chest contents, loot and interactions: **NOT TESTED**.
- Official mod JAR and production world: **UNCHANGED**.

Do not call this a clean placement pass until the maintainer inspects the structure around the hill and confirms whether the partial burial is intentional.


## Create Aeronautics Structures — crashed-airship placement review — 6 November 2026

The maintainer supplied a wider follow-up screenshot of the `cr_aero_structures:crash_airship` site. The view shows the crash-site composition distributed across a hillside: a large broken upright section and debris are exposed on the upper slope, while a smaller hull/interior section with chest and mechanical/track-like blocks is partly embedded lower down.

**Result: visual placement accepted as a hillside crash site.** The wider view makes the partial burial read as intentional crashed-structure placement rather than a missing or wholly buried structure. No obvious generation failure is visible. This is a visual assessment only; loot contents and interactions remain untested.

- Structure generation / presence: **PASS**.
- Visual terrain placement: **PASS — accepted as partially buried hillside wreck**.
- Chest contents / loot / interactions: **NOT TESTED**.
- Official mod JAR and production world: **UNCHANGED**.


## Create Aeronautics Structures — crashed-airship chest loot check — 6 November 2026

The maintainer opened the chest visible in the `cr_aero_structures:crash_airship` wreck and reported that it contained no items.

- Crash-airship structure presence / placement: **PASS**.
- Tested crash-airship chest: **FAIL — empty / no items found**.
- Other structure chest loot: **NOT TESTED**.
- Official mod JAR and production world: **UNCHANGED**.

This result applies only to the chest inspected. It does not yet prove that every structure loot table is broken. Investigate the chest's loot-table initialization and active datapack/mod resources before changing the official JAR or beta package.


## Create Aeronautics Structures — crashed-airship chest block-entity diagnosis — 6 November 2026

The maintainer ran `/data get block -835 105 -6752` against the chest at the crashed-airship site. Minecraft returned the block-entity data:

```snbt
{x: -835, y: 105, z: -6752, Items: [], id: "minecraft:chest"}
```

**Finding: the chest has an empty `Items` list and no `LootTable` or `LootTableSeed` fields in the returned data.** This is stronger evidence than simply observing an empty inventory: the placed chest currently has no loot table assigned in its block-entity data. It points to the structure/template placement or loot-table assignment step, rather than a loot table that was assigned and rolled an empty result.

This finding is limited to this inspected chest. Do not conclude that every chest in every Aeronautics structure is affected until more examples are checked. Preserve the official mod JAR and test world state; do not manually populate the chest or edit the JAR. Next diagnostic: inspect another freshly generated Aeronautics structure chest and compare its block-entity data for a `LootTable` field.

- Crashed-airship chest: **FAIL — no loot table assigned; `Items: []`**.
- Other structure chests: **NOT TESTED**.
- Official mod JAR / production world: **UNCHANGED**.


## Engineering-house container comparison — 6 November 2026

The maintainer supplied two screenshots from the engineering house:

- One opened barrel GUI visibly contains several items. This confirms that at least one barrel container in the engineering house generated loot.
- A separate block is identified by Jade as `lootr:loot_barrel` at approximately `(524, 98, -3954)`; its tooltip reads **"Loot not generated yet"**. This container has not yet had its loot generation verified.

**Interpretation:** Engineering-house barrel loot is not uniformly absent. The populated barrel contrasts with the crashed-airship vanilla chest whose block entity had `Items: []` and no `LootTable` field. The Lootr barrel is a separate, still-pending check; its tooltip alone does not establish a failure because loot may be generated on first opening.

- Engineering-house opened barrel: **PASS — items visibly present**.
- Engineering-house Lootr barrel at `(524, 98, -3954)`: **PENDING — tooltip says loot not generated yet; open it to trigger/check generation**.
- Crashed-airship vanilla chest: **FAIL — no loot table assigned; `Items: []`**.
- Official mod JAR / production world: **UNCHANGED**.


## Engineering-house Lootr barrel — first-open loot generation — 6 November 2026

The maintainer opened the previously inspected `lootr:loot_barrel` at approximately `(524, 98, -3954)`. The new screenshot shows the barrel GUI populated with multiple item stacks.

**Result: PASS — Lootr generated loot when the barrel was opened.** The earlier Jade tooltip "Loot not generated yet" represented the unopened / not-yet-generated state, not a confirmed loot failure. This confirms that at least this Lootr barrel in the engineering house generates loot correctly on first opening.

- Engineering-house standard barrel: **PASS — items visible**.
- Engineering-house Lootr barrel: **PASS — multiple items visible after opening**.
- Crashed-airship vanilla chest: **FAIL — no loot table assigned; `Items: []`**.
- Other structure containers: **NOT TESTED**.
- Official mod JAR / production world: **UNCHANGED**.


## Create Aeronautics Structures — loot testing handoff to beta testers — 6 November 2026

**Maintainer instruction: do not continue exhaustive loot testing during the current maintainer test session. Remaining loot coverage is assigned to beta testers.**

### Maintainer spot-check evidence

| Structure / container | Result |
|---|---|
| Engineering house — standard barrel | **PASS** — items visibly present |
| Engineering house — Lootr barrel | **PASS** — multiple items appeared after first opening |
| Crashed airship — vanilla chest at `(-835, 105, -6752)` | **FAIL** — block data showed `Items: []` and no `LootTable` / `LootTableSeed` |

The Lootr tooltip **"Loot not generated yet"** is not itself a failure; testers must open the Lootr container before judging its loot.

### Beta tester tasks

During normal exploration, beta testers should check loot in the remaining Aeronautics structure variants and their containers. For each result, record:
- Structure variant and container type (vanilla chest, barrel, Lootr barrel, etc.).
- Whether items appeared after opening the container.
- Approximate coordinates.
- Screenshot evidence where practical; include relevant logs for errors.

Report empty containers only after opening them. Do not manually fill containers or modify the official mod JAR. The test-only uniform-loot override is not an approved release fix.

**Handoff:** remaining structure/container loot coverage — **DELEGATED TO BETA TESTERS**. The crashed-airship chest's missing loot-table assignment remains an open maintainer investigation; this handoff does not mark it fixed.
