# Testing order and responsibilities for beta candidates

**Maintainer scope:** exact CurseForge file/dependency/side preflight and routine smoke testing only (startup, world load, matching-client login, clean shutdown, and relevant log review). Do not treat this as feature validation.

**Beta-tester scope:** beta testers perform feature/function actions for every installed feature/content mod, whether server-only, shared client/server, or client-only. The action matrix below is the source for those tasks. Pending actions are expected during the initial beta and are not passes.

- Internal profile smoke follows the server-first order for any newly authorised candidate: server-only, then shared client/server, then client-only profile checks.
- This is not an active numbered-batch queue. The previous numbered sequence has been retired; do not restart historical batch work.
- Do not require isolated per-mod or one-optimizer-at-a-time runs unless a specific diagnostic is explicitly requested and approved.
- **spark profiling is deferred to beta testers.** It is not an internal development prerequisite.

# Full Installed-Mod Functional Testing Checklist

**Last reviewed:** 11 November 2026  
**Target:** Minecraft 1.21.1 · NeoForge 21.1.265 · Java 21  
**Approved download source:** CurseForge only

This checklist is a feature-test matrix, not a complete file manifest. For current accepted mod-set status and outstanding profile rechecks, use [MODS.md](MODS.md). The 10 November active-profile archive audit found 102 JARs in each test-profile archive, with 101 shared non-WITS JARs identical by SHA-256. This is not a final release manifest and does not prove deployment to the separate clean v.0.1 server. The 5–7 November screenshots and folder inventories below are dated historical observations, not current installation instructions.

## Current verification snapshot — 11 November 2026

| Area | Current verified status |
|---|---|
| Clean Windows dedicated-server baseline | PASS — 7 November fresh world, four IronWoven datapacks enabled, matching client login, operator/Creative command, and clean shutdown. This is a separate 101-JAR server baseline. |
| Active test-profile archive parity | PASS — 10 November client and server archives each contain 102 JARs; 101 shared non-WITS JARs have identical SHA-256. WITS is a temporary utility excluded from the mod set. These profiles are not the versioned v.0.1 server or final release package. |
| Sophisticated Backpacks 3.26.21.2249 / Sophisticated Core 1.5.32.2464 | Accepted into active mod set after authorised shared smoke PASS and exact client/server SHA-256 parity. Backpacks feature actions Pending for beta testers; Core validated through Backpacks. |
| TFMG Community Edition 1.3.3a | Accepted into active mod set after authorised shared smoke PASS and exact client/server SHA-256 parity. Feature/visual actions Pending; Custom License distribution review remains separate. |
| FastSuite 6.0.7 / Placebo 9.9.4 / FastFurnace 9.0.1 | FastSuite/Placebo accepted into active mod set after exact-file/dependency preflight, matching client/server hashes, and combined-profile smoke PASS. No isolated optimizer test required. FastFurnace loaded in the same session but exact CurseForge file/dependency/side preflight remains open; not yet accepted. Feature/recipe/JEI/performance actions belong to beta testers. |
| Every Compat 2.11.57 / Moonlight Lib 3.8.2 | Accepted baseline pair; fresh clean-server smoke PASS. Golden Cherry Leaves duplicate registration remains open; feature actions belong to beta testers. |
| Railways 0.3.0-beta.2 / Supplementaries 4.0.2 | Present in both 10 November profiles with matching hashes; exact CurseForge/dependency review and update disposition remain pending. |
| Create Aeronautics Curios Compat | Profile JAR filename reports 2.3 while embedded metadata reports 2.0; recheck exact file and loaded metadata. |
| Waystones 21.1.46 / Sable 2.0.6 | Present in the 10 November profile despite the earlier deferred travel-system decision; reconcile intended disposition, AeroPortals overlap and Balm compatibility before release. |
| Create Aeronautics Structures 1.1.0-Beta-3.1 | ON HOLD — not eligible for the beta package. |
| PowerGrid / Struts / Shulker Box Tooltip + Supplementaries | PARTIAL — known Windows workarounds and limits remain documented; feature actions belong to beta testers; Linux is untested. |
| Linux dedicated server | NOT TESTED / NOT VERIFIED. |
| Individual feature matrix | OPEN — beta testers own feature/function validation for every installed feature/content mod on every side. |
| Public beta / release | NOT APPROVED — no downloadable beta package exists. |

**Inventory boundary:** accepted updates observed in the 10 November active test profiles are not confirmed deployed to the separate clean v.0.1 server. Keep the recorded `v0.1.101.5` unchanged until that exact server is updated and the private updater is previewed. Do not infer release inclusion from profile presence.

**How to submit test results:**

1. Open the [Submit Test Result form](https://github.com/Create-IronWoven/Create-IronWoven-Age-of-Industry-Beta/issues/new?template=functional-test-report.yml).
2. Copy the mod heading text (including version, without the leading ### symbols) and the exact test-action text from the table below.
3. Select the test environment: Single-player, Multiplayer, or Both. Choose Both only when you actually tested the action in both environments.
4. Enter a tester nickname or pseudonym and the test date in DD-MM-YYYY format, choose the result, and describe what happened. Do not enter a legal/real name or GitHub username. Note: GitHub shows the account that opened the report as the public issue author, but the automation does not copy that account name into this checklist. Do not use your legal/real name or GitHub account username.
5. Submit the form. The Beta-to-private forwarding path and invalid-report safeguards have been verified. A valid, unique report updating a matching checklist row is still awaiting end-to-end verification. A submitted issue does not by itself confirm that a checklist row changed; check this page after submission and contact the maintainers if the result does not appear.

Submit one form for each test action. The processor is designed to match the mod/action text and preserve existing results. Duplicate reports are detected and do not overwrite the original result. Retests of completed actions require maintainer review; existing results are never silently overwritten.

A server startup or an item appearing in JEI is not, by itself, a function-test pass. Keep smoke-test evidence separate from feature tests. A maintainer-recorded smoke PASS may qualify the exact authorised version for active mod-set membership; it does not mark any feature row Pass or grant beta/release distribution approval.

## Smoke test is not a function test

The fresh Windows v.0.1 server reached `Done (4.440s)`, generated `IronWoven Age Of Industry_v0.1.0`, enabled all four IronWoven world-scoped datapacks among 12 total, accepted the matching client, granted operator permissions, accepted a Creative-mode command, and shut down with all dimensions saved. The five targeted Design n' Decor, Steam 'n' Rails, Create Kinetic, Sable Catwalk and Create Deco placard error families were absent from its log. This fresh-install smoke test is separate from the 6 November 15:54 corrected `world_lootr_test` retest, which also passed startup/world/login/shutdown with all four packs enabled. Later 6 November targeted retests confirmed the local Struts workaround, Shulker Box Tooltip / Supplementaries client workaround, and PowerGrid Windows native loading workaround; see the dated records below. The fresh 7 November log still contains eight ERROR-level records and five DUMMY block-entity warnings, including three unattributed entity-attachment warnings; review [KNOWN_ISSUES.md](KNOWN_ISSUES.md) and keep unknown sources unattributed. These are test-profile-specific results; **they do not prove every installed mod's functions work or establish Linux compatibility**.

- **Smoke test:** mod discovery, server/client startup as appropriate, world load, login, shutdown and log review.
- **Function test:** exercise the actual feature(s) that justify keeping the mod: item/block interaction, machine process, transport, GUI, world generation, rendering, recipe/loot behavior or synchronization.
- A combined smoke-test pass is not an individual mod-function pass. Do not mark a feature complete just because its mod ID appears in a server log.
- Client-only mods require a matching client launch and client-side review. A dedicated-server log cannot prove their client functions.
- Libraries/APIs are tested through the mod(s) that depend on them; they do not need invented standalone gameplay tests.

## Current pack-level smoke evidence

| Check | Evidence | Status |
|---|---|---|
| Dedicated-server startup | Fresh Windows v.0.1 reached `Done (4.440s)`; corrected 6 Nov disposable run reached `Done (1.413s)` | PASS — both profiles |
| Disposable-world load | Fresh v.0.1 world generated on 7 Nov; corrected `world_lootr_test` loaded on 6 Nov | PASS — both profiles |
| IronWoven compatibility datapacks | All four world-scoped packs enabled among 12 total in fresh v.0.1 and in corrected `world_lootr_test` | PASS — log-level retest |
| Targeted compatibility errors | Design n' Decor, Railways, Create Kinetic, Sable Catwalk, and Create Deco placard errors absent in fresh 7 Nov and corrected 6 Nov logs | PASS — log review only |
| Matching client login | Matching client joined in fresh 7 Nov and corrected 6 Nov runs; 7 Nov operator and Creative-mode commands also succeeded | PASS — smoke test only |
| Clean shutdown | All dimensions saved in the fresh 7 Nov run and corrected 6 Nov retest | PASS |
| TFMG 1.3.3a shared update smoke | Matching client/server loaded `tfmg-1.21.1-1.3.3a-community.jar`; client connected and completed SBT handshake; server saved all dimensions; exact client/server SHA-256 parity confirmed | PASS — accepted into active mod set; feature/visual actions Pending; Custom License review separate |
| FastSuite 6.0.7 / Placebo 9.9.4 combined-profile smoke | Exact files/dependency preflight and matching client/server hashes confirmed; both loaded with FastFurnace in the 11 November smoke session; startup/world/login/shutdown passed | PASS — FastSuite/Placebo accepted into active mod set; FastFurnace exact preflight remains open; no isolated optimizer test; feature actions Pending for beta testers |
| Sophisticated Backpacks 3.26.21.2249 + Sophisticated Core 1.5.32.2464 | Matching pair loaded on client and dedicated server; client joined; all dimensions saved on clean shutdown; exact client/server SHA-256 parity confirmed | PASS — accepted into active mod set; Backpack feature actions remain Pending for beta testers |
| Individual feature tests | Matrix below | OPEN — mostly not yet function-tested |
| Matching client-only mod startup | Targeted client evidence exists for PowerGrid and local Struts / tooltip workaround tests; no complete isolated optional-client candidate sweep | PARTIAL — optional candidates remain open |
| Remaining fresh-server log findings | 8 ERROR-level records (five attributed to PowerGrid, Every Compat, Create Aeronautics Structures and SBT/Supplementaries; three unattributed entity-attachment warnings) and five DUMMY block-entity warnings remain under review | OPEN — do not attribute unknown records to a mod without evidence |
| Production/release approval | Not granted | NOT APPROVED |


## PowerGrid Windows native-load retest — 6 November 2026, 18:29–18:34

**Result: internal Windows native loading and client connection passed. Electrical-network/component behavior is a beta-tester feature check, not another internal maintainer task.** The PowerGrid 0.6.2 JAR was not modified. The official 0.6.1 Windows DLL was copied into the disposable server and CurseForge client `.pg-native` directories. The 18:29 server log and 18:34 client log both reported `Native backend loaded successfully`. The server reached `Done (1.837s)`; the matching client connected to `localhost:25565` and entered the world. This workaround must not be mistaken for an official 0.6.2 package fix or an accepted modpack change.

- Windows server native load: PASS — disposable profile.
- Windows client native load: PASS — matching CurseForge profile.
- PowerGrid electrical network / component behavior: DEFERRED TO BETA TESTERS; not an internal fix-pass task.
- Linux native solver: NOT TESTED — Linux requires the Linux `.so`; do not use the Windows DLL.
- Production files and modpack manifest: unchanged.

## Corrected compatibility datapack smoke retest — 6 November 2026, 15:54

The disposable `world_lootr_test` run enabled all four IronWoven world-scoped datapacks. Server startup, world load, matching client login, and clean shutdown with all dimensions saved passed. The log-level checks found no targeted Design n' Decor (256), Steam 'n' Rails (192), Create Kinetic (5), Sable Catwalk selector, or Create Deco placard parsing errors. This does not mark the affected gameplay drops or recipes as function-tested.

The log contains 6 ERROR-level records and 172 WARN-level records. Remaining errors: Struts dedicated-server `RenderSystem`; PowerGrid optional `powergridNative7`; Every Compat duplicate Herbs & Harvest Golden Cherry Leaves registration; Create Aeronautics Structures `cr_aero_structures:chests/uniform`; and the Shulker Box Tooltip / Supplementaries dedicated-server `PreviewRenderer` integration failure. InControl read `areas.json`. See the private maintainer's detailed report for full triage.

## Existing partial function evidence — do not overstate it

- **Curios:** two Back slots and one Head slot appeared in a newly created test world. Backpack + standard Create Backtank, Aviator Goggles and Linked Typewriter use were reported working in their assigned slots. Full matching client/server synchronization and older-player saved-slot correction remain separate.
- **Lootr:** the maintainer confirmed a test chest opened and contained loot. Independent personal loot for a second player is not yet verified.
- **Every Compat:** Chipped Carpenter's Table modded-wood variants and the stone table were reported working. This is partial; duplicate Golden Cherry Leaves registration and the large compatibility-block footprint remain recorded.
- **Create Aeronautics Structures:** ON HOLD. Earlier disposable-world structure/loot evidence is preserved in the [historical evidence archive](archive/TESTING_CHECKLIST_HISTORICAL_EVIDENCE_2026-11-11.md); do not continue testing or ask beta testers to install this held candidate.
- **Just Enough Resources, Enchantment Descriptions and Shulker Box Tooltip:** the 6 November combined startup/login smoke passed. The Shulker Box Tooltip / Supplementaries server-provider issue remains separately documented; feature rendering/use is a beta-tester action.
- **Nature's Compass and Explorer's Compass:** shared startup/login smoke passed; actual biome and structure searches remain Pending for beta testers.
- **Create Big Cannons and Ritchie's Projectile Library:** shared startup/login smoke passed; cannon operation remains Pending for beta testers.
- **Optional client rendering candidates:** these are not confirmed in the 10 November active-profile inventory and are not current feature-test obligations. Do not add or test them as installed mods without a fresh exact client export, file/dependency/side preflight and maintainer authorization. spark 1.10.124 is present in the profile; profiling is deferred to beta testers.

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

### Create Aeronautics Structures 1.1.0-Beta-3.1 (test-only; ON HOLD)
**Current status: ON HOLD.** The candidate is not eligible for the next beta and no new tests are active. The previous test results below remain historical evidence only: the 16-colour override passed runtime testing, all 11 valid Overworld structure IDs have visual-presence evidence, and the specific crashed-airship chest was diagnosed without a loot-table assignment. The official JAR remains unchanged; the test-only override is not approved for distribution. Reopen only after a new official CurseForge 1.21.1 NeoForge file is reviewed and both loot defects are verified fixed, or a documented exception is explicitly approved. Do not submit new feature-test results for this candidate while it remains held.

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Enable the IronWoven Aeronautics Structures uniform-loot test datapack and confirm the uniform-table parse error is absent. | PASS — test-only override | Multiplayer — disposable dedicated server (`MinecraftServer-Test`) / `world_lootr_test`; Windows 11; Minecraft 1.21.1 / NeoForge 21.1.265 | Maintainer | 06-11-2026 | Enabled-pack list contained the ZIP alongside all four existing IronWoven packs; supplied server log contains no recurrence of the targeted parse error. |
| Run `/loot give @s loot cr_aero_structures:chests/uniform` repeatedly and inspect generated loot. | PASS — test-only override | Multiplayer — disposable dedicated server (`MinecraftServer-Test`) / `world_lootr_test` + matching client; Windows 11; Minecraft 1.21.1 / NeoForge 21.1.265 | Maintainer | 06-11-2026 | Repeated commands produced multiple differently dyed leather armour pieces plus iron sword/axe drops in supplied inventory screenshots. The override preserves the original sword/axe/spyglass pools; official JAR unchanged. |
| Fresh disposable Overworld: locate and inspect `cr_aero_structures:airship`. | PASS — airship located and visually confirmed | Disposable `MinecraftServer-Test` / `world_lootr_test`; Windows 11; Minecraft 1.21.1 / NeoForge 21.1.265 | Maintainer | 06-11-2026 | `/locate structure cr_aero_structures:airship` returned a nearest location about 2,575 blocks away; teleport to `(-2783.5, 82, -3375.5)` showed the generated airship deck and fittings in the supplied screenshot. This is one-variant evidence only. |
| Review presence and placement of all valid Overworld structure IDs. | VISUAL EVIDENCE RECORDED — 11 valid IDs; not credited as formal function pass because exact Single-player / Multiplayer mode was not recorded | Disposable Overworld; exact Single-player / Multiplayer mode not recorded | Maintainer | 06-11-2026 | Evidence in the private report covers `airship`, `boat`, `engineering_house`, `airballoon`, `crash_airballoon`, `crash_pillager_airballoon`, `crash_pillager_airship`, `crash_plane`, `pillager_airballoon`, `pillager_airship`, and `crash_airship`. Crashed-airship hillside placement was visually accepted. `cr_aero_structures:plane` is invalid and is not counted. |
| Inspect engineering-house standard and Lootr barrel contents. | OBSERVATION ONLY — items were visible; not credited as a formal feature pass because exact Single-player / Multiplayer mode was not recorded | Disposable Overworld; exact Single-player / Multiplayer mode not recorded | Maintainer | 06-11-2026 | Standard barrel contained items. Lootr barrel generated multiple item stacks after first opening. |
| Inspect the crashed-airship vanilla chest block entity. | FAIL — this specific chest has `Items: []` and no `LootTable` / `LootTableSeed` | Disposable Overworld; exact Single-player / Multiplayer mode not recorded | Maintainer | 06-11-2026 | Chest at `(-835, 105, -6752)` was inspected with `/data get block`; this is a specific loot-assignment failure, not evidence that every Aeronautics chest is affected. |
| Check remaining structure/container loot and trader behavior. | **PAUSED — candidate ON HOLD; do not test until re-opened** | Not recorded | Not recorded | DD-MM-YYYY | The previous beta-tester handoff is suspended while this candidate is held. Resume only after the exact updated CurseForge file and both known loot defects have been reviewed and the hold is lifted. |

### Create Aeronautics Curios Compat — JAR filename 2.3 / embedded metadata 2.0 (version reconciliation pending)
**Current status:** Partial — the active-profile JAR filename reports 2.3 while embedded metadata reports 2.0. Reconcile the exact CurseForge file and loaded mod metadata before treating this as a confirmed version. Assigned-slot behavior was user-reported working; repeatable synced test remains pending.

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

### Create: Steam 'n' Rails 0.3.0-beta.2 (active-profile observation; update disposition pending)
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
| Open bogie UI (crouch + right-click empty-handed) | Pass | Multiplayer | Ghosty | 03-11-2026 | Crouch + right-click while empty-handed to access different options. (submitted in issue #9) |
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

### Create: Gadgets & Gizmos 2.0.0-Pre-Release-4 — ON HOLD (not available for testing)

**Maintainer decision (7 November 2026): ON HOLD.** Keep the current bundled 1.2.10 installation (CurseForge file 9141062) unchanged. Do not install or test 2.0.0-Pre-Release-4 (file 9260191), do not add or update dependencies, and do not alter the CurseForge profile or manifest. The 2.0.0-Pre-Release-4 file is not a stable 2.x release.

Reconsider only after the author publishes a clearly stable, non-prerelease 2.x file for Minecraft 1.21.1 NeoForge. Before proposing a test, verify the exact artifact's embedded mod metadata, bundled-library contents, required and optional dependencies, version ranges, client/server sides, release notes, and known upstream issues. Resolve any incompatible or unclear dependency first. A separate explicit maintainer approval is required before any installation or disposable test begins.

**Current test status:** no 2.0.0-Pre-Release-4 installation, startup test, feature test, or acceptance is authorized. Rebuild this section from the exact stable release notes only if the hold is lifted.

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
| Restore 0.6.1 Windows native DLL to server and client `.pg-native` folders. | **Passed — server and client native loading** | Disposable server + matching CurseForge profile | Maintainer | 06-11-2026 | Server `latest(20261106-173022).log` (18:29) and client `latest(20261106-173558).log` (18:34) both report `Native backend loaded successfully`. Server reached `Done (1.837s)`; client connected to `localhost:25565` and entered the world. PowerGrid 0.6.2 JAR unchanged. |
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

### Create: The Factory Must Grow Community Edition 1.3.3a (accepted mod-set version; feature tests pending)
**Current status:** The authorised shared client/server smoke test passed on 10 November 2026 and exact client/server SHA-256 parity was confirmed in the active-profile archive audit. The 1.3.3a version is accepted into the active mod set. Feature tests and Electric Diode/Fuse Block visual checks remain Pending; Custom License distribution review is separate. The smoke result is not a feature pass.

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Run representative industrial processing: fluid/oil input, machine processing, outputs, power/kinetic requirements and fuel-burning machine. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Test Blast Furnace handling of one-result recipes; confirm it completes without crashing and produces the expected output. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Verify one-block engine fuel consumption. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Verify glass-pipe clone item-stack behavior. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
| Verify intended connection behavior between cast-iron and aluminium blocks. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Add result and evidence here |
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

### Sophisticated Backpacks 3.26.21.2249
**Current status:** Shared client/server smoke PASS — 10 November 2026; exact client/server SHA-256 parity confirmed in the active-profile archive audit. Backpacks 3.26.21.2249 with Core 1.5.32.2464 is accepted into the active mod set. Feature validation remains Pending — beta tester validation.

**Supporting library:** Sophisticated Core 1.5.32.2464 is required by this Backpacks version and is tested through the Backpack actions below; it has no separate player-facing gameplay test. Keep Create Integration 0.2.3.194 and Sophisticated Air Tank 1.0.1-beta unchanged while testing these actions. Their separate tests remain in their own sections.

| Test action | Result | Test environment | Tester nickname | Test date (DD-MM-YYYY) | Evidence / notes (log, screenshot, observations) |
|---|---|---|---|---|---|
| Craft or obtain a test backpack; store, retrieve and move items, then close and reopen it to confirm inventory contents and upgrade slots remain correct. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Use a test backpack; do not risk valuable items. |
| Install, remove and replace representative upgrades, including Tank, Battery and Stack combinations; confirm slot layouts recalculate without losing, duplicating or displacing items. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Check the backpack inventory before and after each change. |
| Configure representative Pickup, Deposit and Filter upgrades; verify allowed items are collected or moved and filtered/disallowed items remain in place. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Record which upgrades and filters were used. |
| Test backpack contents and upgrade persistence after relog and server restart; in multiplayer, confirm the backpack view and contents remain synchronized for its owner. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | Include the test environment and whether a restart or relog was used. |
| Test the Advanced Jukebox upgrade: start playback, die and respawn, then confirm playback stops and does not continue unexpectedly. | Not tested | Not recorded | Not recorded | DD-MM-YYYY | This checks the behavior addressed by the 3.26.21 update. |

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

## E. Client graphics and performance

No optional client rendering/performance mods are confirmed in the complete 10 November active-profile inventory. Earlier checklist rows for Sodium, Iris, Sodium Extra, ImmediatelyFast, Flerovium, Entity Culling and More Culling have therefore been removed from the current feature-test matrix and preserved in the archive above. Do not treat them as installed or pending beta tests. Entity Culling was explicitly removed from the client profile; Sodium and Sodium Extra were also removed. Reconsider any of these only after a fresh exact client export, CurseForge file/dependency/side review, and explicit maintainer authorization.

**spark 1.10.124:** present in the 10 November active-profile inventory. Profiling remains deferred to beta testers and is not an internal maintainer prerequisite.

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

### Gadgets & Gizmos Library 1.2.10 (bundled baseline)
**Current status:** Pending — the 2.0.0-Pre-Release-4 candidate is a replacement bundled parent JAR (CurseForge file 9260191); do not count the library as a separate independently selected mod update unless the exact bundled component/version is separately confirmed.

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

### Sophisticated Core 1.5.32.2464
**Current status:** Accepted support dependency — shared client/server smoke PASS with Sophisticated Backpacks 3.26.21.2249 on 10 November 2026 and exact client/server SHA-256 parity confirmed. Core is a library and has no separate gameplay test. Validate its support through the Sophisticated Backpacks test actions above; do not submit a separate standalone Core feature result.


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

## Historical evidence archive

The former dated smoke attempts, old inventory-folder observations, removed client-rendering candidate rows, and detailed Aeronautics Structures investigation are preserved in [Archived Beta Checklist Evidence — 11 November 2026](archive/TESTING_CHECKLIST_HISTORICAL_EVIDENCE_2026-11-11.md). Use that file only when the specific history is relevant; it is not a current test queue or release inventory.
