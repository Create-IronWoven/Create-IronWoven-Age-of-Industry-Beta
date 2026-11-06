# Mods in Ironwoven: Age of Industry

**Latest dedicated-server folder snapshot:** 6 November 2026 — 106 visible JAR files. Client inventory is separate and unchanged by this server-only screenshot.
**Accepted baseline target:** `v0.1.112-R002` includes Every Compat 2.11.57 and Moonlight Lib 3.8.2. The latest screenshot confirms both accepted JARs are now physically present in the original `Create World/mods` client profile. The normal dedicated-server baseline still needs the same pair; the 6 November server file listing below is a pre-deployment snapshot.  
**Minecraft:** 1.21.1  
**Loader:** NeoForge 21.1.265  
**Java:** 21

This page records the latest reviewed test-folder inventory snapshot and identifies client-only additions. Accepted version targets may be ahead of physical folder snapshots while an approved update is awaiting local deployment. It is not a final release manifest. The latest CurseForge profile shows **108 mod entries**. The latest client `mods` folder snapshot shows **104 JAR files**; the latest dedicated-server `MinecraftServer-Test/mods` screenshot (6 November 2026) shows **106 JAR files**. The server screenshot supersedes its earlier 104-file observation; the client count remains unchanged. These are different counting methods: CurseForge entries and physical JAR files are not interchangeable, especially where mods bundle components. Matching folder counts do not by themselves prove exact filename equality. A later disposable-server log detected Create Aeronautics Structures 1.1.0-Beta-3.1 as an Overworld test candidate; it is not part of the accepted inventory. The maintainer-supplied JAR metadata matches official CurseForge file 8399115 by version (not hash-compared). Its test-only 16-color uniform-loot override passed runtime testing in a disposable Windows world; the official JAR remains unchanged. All 11 valid Overworld structure IDs now have locate/visual-presence evidence, with the crashed-airship hillside placement visually accepted; `plane` is invalid. Maintainer spot checks found items in the engineering-house standard and Lootr barrels; one crashed-airship vanilla chest has no assigned loot table. Remaining structure/container loot coverage is delegated to beta testers; the chest defect and release-safe correction/distribution decision remain open. Its Russian startup message is informational only.

Some entries below are libraries, APIs, or bundled components required by other mods. They are listed for transparency even though they do not add a standalone gameplay feature.

## Main Create, engineering, transport, and automation mods

| Mod | Version in test snapshot |
|---|---|
| Create | 6.0.10 |
| Create Aeronautics | 1.3.2 |
| Create Aeronautics: Curios Compat | 2.0 |
| Create: Curios Backtank | 1.0.2 — test installation; Backpack + Backtank use in the Curios Back slots reported working; broader release validation remains open |
| Create Aeronautics: Copycat Wing | 1.0.4 |
| Create Aeronautics: Transmission & Linkage | 0.2.9 |
| Create Bits 'n' Bobs | 2.3.5 |
| Create Cobblestone | 1.5.1+neoforge-1.21.1-160 |
| Create Crafts & Additions | 1.7.2 — latest test-folder file; acceptance pending |
| Create Deco | 2.1.3 |
| Create Diesel Generators | 1.3.15 |
| Create Encased | 1.10.0-fix1 |
| Create Gadgets & Gizmos | 1.2.10 |
| Create Kinetic | 1.4.3 |
| Create Liquid Fuel | 3.0.0 |
| Create Offroad | 1.3.2 |
| Create: Simulated | 1.3.2 |
| Create Slice & Dice | 4.3.4 |
| Create: Bells & Whistles | 0.4.7 |
| Create: Blocks & Bogies | 1.0.8 |
| Create: Copycats+ | 3.0.9 |
| Copycats+ Additions | 1.5.0 |
| Create: Dragons Plus | 1.11.9 |
| Create: Enchantment Industry | 2.5.4b |
| Create: Fluids Be Gone! | 1.0.1 |
| Create: Framed | 1.8.2 |
| Create: Numismatics | 1.0.20 |
| Create: Pantographs & Wires | 0.2.3-C6 beta |
| Create: Pattern Schematics | 2.0.10 |
| Create: Power Grid | 0.6.2 |
| Create: Rustic Structures | 1.0.1 |
| Create: Sound of Steam / Pipe Organs | 0.9.2.1 |
| Create: Steam 'n' Rails | 0.3.0-alpha.2 |
| Create: Structures Arise | 176.49.50 |
| Create: The Factory Must Grow | 1.3.3-community — latest test-folder file; acceptance pending |
| Create: Unified Fuels | 1.0.4 |
| Create: Vibrant Vaults | 0.3.2 |
| Botany Pots | 21.1.44 |
| Construction Sticks | 1.5.0 |
| Modern Train Parts | 0.2.5 |
| KineticGrip | 1.0.5 |
| Aeronautical Diesel | 1.1.0 |
| AeroPortals | 1.3.6 |
| Strut Your Stuff | 1.3.1 |
| Shield Generators | 1.4.0 |

## Building, decoration, food, and storage

| Mod | Version / status |
|---|---|
| Every Compat (Wood Good) | 2.11.57 — accepted baseline target; paired with Moonlight Lib 3.8.2; local baseline deployment pending |
| Chipped | 4.0.2 |
| Design n' Decor | 2.2b |
| Farmer's Delight | 1.3.4 |
| Mama's Herbs and Harvest | 1.21.1-24 |
| Supplementaries | 3.4.0 — Integrated Villages dependency; validated present in corrected server test profile |
| Sophisticated Backpacks | 3.26.20.2244 — latest test-folder file; acceptance pending |
| Sophisticated Backpacks Create Integration | 0.2.3 |
| Sophisticated Air Tank | 1.0.1-beta |
| Sophisticated Core | 1.5.28.2458 — latest test-folder file; acceptance pending |

## World generation and exploration

| Mod | Version in test snapshot |
|---|---|
| Oh The Biomes We've Gone (BYG) | 2.6.3 |
| Regions Unexplored | 0.6.3 — official scope includes Overworld and Nether biome generation; Nether behavior still needs a disposable-world check |
| Oh The Trees You'll Grow | 5.3.5 |
| TerraBlender | 4.1.0.8 |
| Lithostitched | 1.8.1 |
| Atmosphere | 1.0.18 |
| Integrated Villages | 1.3.3+1.21.1 — server test candidate; structure and performance validation pending |
| Create Oh The Biomes We've Gone Compatibility | 0.0NONE |

## Player interface, teams, and utility

| Mod | Version in test snapshot |
|---|---|
| AppleSkin | 3.0.9 |
| FTB Chunks | 2101.1.23 |
| FTB Library | 2101.1.39 |
| FTB Teams | 2101.1.12 — latest test-folder file; initialized in 14:09 smoke test |
| FTB XMod Compat | 21.1.14 |
| InControl! | 10.3.1 |
| Jade | 15.10.6 |
| Just Enough Items (JEI) | 19.64.0.455 |
| Mouse Tweaks | 2.26.1 |
| Memory Settings | 6.0 |
| MezzConfig | 0.6.10 |
| Sable | 2.0.6 |

## Optional client-side mods — separate client tests

These are optional client-side additions/candidates. They are not required for the dedicated server and **must not be placed in the dedicated-server `mods` folder**. Test each one individually on the matching client, after the server/shared testing queue is complete. Their inclusion here does not mean the tests have passed or that they are mandatory for the pack.

| Mod | Version in latest observed test files | Side / status |
|---|---|---|
| ImmediatelyFast | 1.6.15 | Optional client-only rendering/performance candidate — isolated client test pending |
| Flerovium | 1.1.3 Beta | Optional client-only rendering/performance candidate — observed file; stable 1.1.2 was the original plan, so decide which exact release to test before proceeding |
| More Culling | 1.0.11 | Optional client-only rendering/performance candidate — isolated client test pending; exact CurseForge file provenance still to reconcile |

**Supporting dependency:** Cloth Config API 15.0.140 was detected with More Culling. Keep it client-side with the More Culling test where required; it is a dependency, not a separate optional gameplay mod.

**Iris:** 1.8.14-beta.1 is recorded in historical inventory/archive notes, but its presence in the latest 108-entry CurseForge profile has not been reconfirmed. Do not count it as a confirmed current client-profile mod until a fresh profile export or screenshot confirms it.

**Testing order:** one candidate at a time; do not combine these rendering candidates during their first tests. Inspect Create screens, contraptions, Aeronautics, Sable visuals, HUD, GUI, particles, entities, block entities, leaves, glass, and connected textures as relevant. This is an optional follow-up test group, not a requirement for the server to run.

## Libraries, APIs, and support components

These support other mods and may not appear as separate gameplay features.

| Component | Version in test snapshot |
|---|---|
| Apollib | 1.2.0 |
| Architectury | 13.0.11 |
| Athena | 4.0.6 |
| Azimuth | 1.4.10 | 1.4.10 |
| Conditional Mixin | 0.6.4 |
| CorgiLib | 5.0.0.10 |
| Cupboard | 4.2 |
| Curios API | 9.5.1 |
| DragonLib | 3.0.29 |
| Ferrite Core | 7.0.3 |
| Flywheel | 1.0.6 |
| Forge Config API Port | 21.1.1 |
| Gadgets & Gizmos Library | 1.2.10 |
| GeckoLib 4 | 4.9.3 |
| Integrated API | 1.9.1 — Integrated Villages dependency; validated present in corrected server test profile |
| Kotlin for Forge | 5.12.0 |
| MezzConfig | 0.6.10 |
| Moonlight Lib (Selene) | 3.8.2 — accepted required dependency for Every Compat 2.11.57; local baseline deployment pending |
| ModernFix | 5.27.27 |
| Ponder | 1.0.82 |
| Resourceful Lib | 3.0.12 |
| Sable Companion | 1.6.0 |
| Veil | 4.3.2 |

## Important notes

- The server inventory was reconciled against the successful dedicated-server test on 4 November 2026. It is not a promise that every item above will remain in the public release.
- Some Create Aeronautics and Gadgets & Gizmos components are bundled inside parent mod JARs.
- Sodium 0.8.13 and Sodium Extra 0.9.5 were removed from the CurseForge profile on 5 November 2026. Iris remains listed as a client-only entry in the historical inventory; its presence in the latest profile has not been reconfirmed.
- The 4 November server smoke test confirms Botany Pots 21.1.44 and Construction Sticks 1.5.0 are loaded. This confirms server loading, not full feature testing. The final client and server manifests will be published with the beta release after a fresh inventory and clean-install test.
- The internal server config sets two Back slots and one Head slot; the maintainer reports a newly created test world displays two Back slots. Config files will be included with the first beta package. Create Aeronautics Curios Compat supplies the Linked Typewriter slot. More Curios Slots 1.4 was intentionally removed and is not part of the current test inventory; slot counts are controlled by config, not crafting.
- Third-party mods remain the property of their authors. This page identifies the tested components; it does not redistribute their JARs.

See [Mods planned, on hold, and excluded](MOD_PLANS.md) for the difference between installed mods and future candidates.


## Inventory notes before release

- Create: Sophisticated Exoskeleton 1.0 was previously installed/tested as a Batch 5 entry, then **REJECTED and removed** because it did not meet the maintainer's expectations. It is not part of the current test inventory or intended beta release; see [MOD_PLANS.md](MOD_PLANS.md) for the explicit exclusion.
- The current server inventory and client-only additions were drawn from different project records. A fresh client manifest and server JAR inventory will be published with the beta release.


## Performance baseline and test-only candidates — 4 November 2026

The recorded performance baseline includes ModernFix 5.27.27 and FerriteCore 7.0.3 in the server inventory. Sodium 0.8.13 and Sodium Extra 0.9.5 were subsequently removed from the CurseForge profile. Iris 1.8.14-beta.1 remains a historical client-graphics entry whose current profile presence has not been reconfirmed.

Botany Pots, Construction Sticks, Lootr, and YUNG's Better End Island + YUNG's API have also been exercised in separate test-server runs. Their appearance in test notes does not make them production-approved or part of a final release manifest. See [MOD_PLANS.md](MOD_PLANS.md) and [TESTING_CHECKLIST.md](TESTING_CHECKLIST.md) for the status and outstanding tests.

New performance and quality-of-life recommendations remain candidates only. They are not installed in the confirmed baseline.


## Newer user-supplied mods-folder snapshot — 4 November 2026

This 4 November 2026 screenshot is a historical snapshot and is superseded by the 5 November profile screenshot showing `Mods (110)`, followed by the latest screenshot showing `Mods (108)` after Sodium and Sodium Extra were removed. Do not use the historical 88-entry count as the current profile count.


## Failed update-trial snapshot — 5 November 2026, 13:43

The following versions were detected in a later disposable-server attempt. This failed run is **not** the approved inventory snapshot above and does not establish that these versions are release-ready.

| Mod | Trial version |
|---|---:|
| Sophisticated Core | 1.5.28.2458 |
| Sophisticated Backpacks | 3.26.20.2244 |
| Entity Culling | 1.11.3 — client-only |
| Create Crafts & Additions | 1.7.2 |
| Create: Numismatics | 1.1.0 — blocked by Numismatics Plus 1.0.1 dependency |
| Create: TFMG Community Edition | 1.3.3 |
| FTB Teams | Missing from server folder |
| Create: Steam 'n' Rails | 0.3.0-alpha.2; Beta 2 not present |

The server failed before completing mod loading because FTB Teams was missing and Numismatics Plus 1.0.1 required Numismatics 1.0.20. See [Testing Checklist](TESTING_CHECKLIST.md) for repair steps and evidence.

 
## Later disposable update retry — 5 November 2026, 13:58

The latest server/debug logs are a separate test-folder snapshot and do not replace the accepted inventory above.

| Mod | Version detected | Interpretation |
|---|---:|---|
| Sophisticated Core | 1.5.28.2458 | Detected |
| Sophisticated Backpacks | 3.26.20.2244 | Detected |
| Entity Culling | 1.11.3 | Client-only; detected in server folder |
| Create Crafts & Additions | 1.7.2 | Detected |
| Create: The Factory Must Grow Community Edition | 1.3.3 | Detected |
| FTB Teams | 2101.1.12 | Detected and initialized |
| Create: Numismatics | Both 1.0.20 and 1.1.0 JARs scanned; 1.1.0 selected | 1.0.20 was not active |
| Numismatics Plus | Not in runtime mod list | Not tested |
| Create: Steam 'n' Rails | 0.3.0-alpha.2 | Beta 2 not present |

The server reached `Done (1.493s)` and prepared the disposable world. Client login and clean shutdown are not shown. Do not put both Numismatics versions in one `mods` folder; test Plus only with 1.0.20. This is not an accepted final inventory or release manifest.

## Later disposable update smoke-test snapshot — 5 November 2026, 14:09

This is a later test-folder snapshot only and does not replace the accepted inventory above or establish a final release manifest.

| Mod / component | Version detected | Interpretation |
|---|---:|---|
| Sophisticated Core | 1.5.28.2458 | Detected |
| Sophisticated Backpacks | 3.26.20.2244 | Detected |
| Create Crafts & Additions | 1.7.2 | Detected |
| Create: The Factory Must Grow Community Edition | 1.3.3 | Detected |
| FTB Teams | 2101.1.12 | Detected and initialized |
| Create: Numismatics | Both 1.0.20 and 1.1.0 JARs scanned; 1.1.0 active | 1.0.20 was not active |
| Numismatics Plus | Absent from runtime list | Compatibility not tested |
| Create: Steam 'n' Rails | 0.3.0-alpha.2 | Beta 2 not present |
| ImmediatelyFast / Flerovium / Entity Culling / More Culling | 1.6.15 / 1.1.3 / 1.11.3 / 1.0.11 | Client-only files still detected in dedicated-server folder |

The server reached `Done (1.822s)`, loaded the disposable world, accepted a matching client login, and shut down with all dimensions saved. This confirms the routine smoke sequence only. The log contained 463 ERROR-level and 172 WARN-level entries; see [Testing Checklist](TESTING_CHECKLIST.md) for the summary. No feature-function pass or production/release approval is implied.


## Latest server-folder snapshot — 5 November 2026, 18:49

The maintainer supplied a newer screenshot of `MinecraftServer-Test/mods`. This section records the visible test-folder contents and supersedes the 14:09 folder snapshot for the current visible server-folder state. It is not a final release manifest and does not imply feature validation or release approval.

### Updated file versions observed

| Mod | Previous recorded version | New folder version | Status |
|---|---:|---:|---|
| Create Crafts & Additions | 1.6.0 | 1.7.2 | Installed in test folder; acceptance pending |
| Sophisticated Backpacks | 3.26.19.2243 | 3.26.20.2244 | Installed in test folder; acceptance pending |
| Sophisticated Core | 1.5.23.2446 | 1.5.28.2458 | Installed in test folder; acceptance pending |
| FTB Teams | 2101.1.11 | 2101.1.12 | Installed; initialized in earlier 14:09 smoke test |
| Create: The Factory Must Grow Community Edition | 1.3.2a-community | 1.3.3-community | Installed in test folder; acceptance pending |

The screenshot also shows Bookshelf 21.1.81, FastFurnace 9.0.1, FastSuite 6.0.7, Integrated API 1.9.1, Integrated Villages 1.3.3+1.21.1, Lootr 1.11.38.127, Prickle 1.1.11, Supplementaries 3.4.0, and spark 1.10.124 in the server folder.

### Important test-folder observations

- At the earlier 17:48 active-folder snapshot, both Numismatics 1.0.20 and 1.1.0 were visible. The later 17:58 `mods-disabled` screenshot shows Numismatics 1.1.0 and Numismatics Plus 1.0.1 in the archive. The intended active server profile is Numismatics 1.0.20 only; verify the active `mods` folder before the next run. Never keep both Numismatics versions in one profile.
- The 6 November 2026 CurseForge `Create World/mods` client-profile screenshot confirms Entity Culling is absent from the current client mod folder. It is removed from the current optional-candidate list; older server-folder and archive references below are historical observations.
- The screenshot is an inventory observation, not proof of each mod's features or acceptance into the final pack.

**Current modpack version: `v0.1.112-R002`.** The `R001` and `R002` removal increments record the two maintainer-approved client-only removals, Sodium and Sodium Extra. `v0.1.111-R002` records the Every Compat 2.11.57 update; `v0.1.112-R002` records the required Moonlight Lib 3.8.2 dependency update. The approved pair is confirmed in the original `Create World` client folder. The normal dedicated-server baseline remains pending, and the exact visible server JAR list below preserves the earlier 6 November snapshot rather than claiming a server update. Future additions/updates use the `UPDATE` counter; future mod removals use the separate `R` counter.


## Disabled/archive server-folder snapshot — 5 November 2026, 17:58

The maintainer supplied a screenshot of `MinecraftServer-Test/mods-disabled`. The following files are archived outside the active server `mods` folder. This is a record of the disabled folder, not a live filesystem scan of the active folder or a final client-profile manifest.

### End workstream — paused / excluded from the current test setup

| Archived file | Classification |
|---|---|
| `BetterEnd-21.0.39.jar` | End content; End research/testing is paused and the mod is not in the active test setup |
| `YungsBetterEndIsland-1.21.1-NeoForge-3.1.2.jar` | End content; paused with the End workstream |
| `YungsApi-1.21.1-NeoForge-5.1.9.jar` | Support library archived with the End-only test set; keep archived unless a current dependency requires it |

### Client-only rendering / performance candidates — not active on the dedicated server

| Archived file | Classification |
|---|---|
| `entityculling-neoforge-1.10.4-mc1.21.1.jar` | Older Entity Culling candidate |
| `entityculling-neoforge-1.11.3-mc1.21.1.jar` | Newer Entity Culling candidate |
| `flerovium-neoforge-1.21.1-1.1.3-all.jar` | Client rendering/performance candidate |
| `ImmediatelyFast-NeoForge-1.6.15+1.21.1.jar` | Client rendering/performance candidate |
| `moreculling-neoforge-1.21.1-1.0.11.jar` | Client rendering/performance candidate |
| `iris-neoforge-1.8.14-beta.1+mc1.21.1.jar` | Client-only graphics mod; archive location is under the server test folder |
| `sodium-neoforge-0.8.13+mc1.21.1.jar` | Client-only graphics mod; archive location is under the server test folder |
| `sodium-extra-neoforge-0.9.5+mc1.21.1.jar` | Client-only graphics mod; archive location is under the server test folder |

The screenshot proves these files are in the server's disabled archive, not whether matching client-side copies remain in the CurseForge client profile. Keep client-profile inventory decisions separate. Batch E's isolated client tests remain pending; no performance result or rejection is inferred from the archive screenshot alone.

### Superseded versions — retain only as rollback/archive copies

| Archived file | Newer version already recorded in the active test inventory |
|---|---|
| `createaddition-1.6.0.jar` | Create Crafts & Additions 1.7.2 |
| `create-enchantment-industry-2.4.2.jar` | Create: Enchantment Industry 2.5.4b |
| `ftb-teams-neoforge-2101.1.11.jar` | FTB Teams 2101.1.12 |
| `lithostitched-1.7.11-neoforge-21.1.jar` | Lithostitched 1.8.1 |
| `sophisticatedbackpacks-1.21.1-3.26.19.2243.jar` | Sophisticated Backpacks 3.26.20.2244 |
| `sophisticatedcore-1.21.1-1.5.23.2446.jar` | Sophisticated Core 1.5.28.2458 |
| `tfmg-1.21.1-1.3.2a-community.jar` | Create: The Factory Must Grow Community Edition 1.3.3 |

### Other archived test files — reason not established by the screenshot

| Archived file | Classification |
|---|---|
| `tracks-neoforge-1.21.1-1.0.1.jar` | Archived track/rail candidate; no current selection or rejection reason recorded |
| `tracks_plus-1.0.6b7.jar` | Archived track/rail candidate; no current selection or rejection reason recorded |

### Numismatics files

| Archived file | Classification |
|---|---|
| `CreateNumismatics-1.1.0+neoforge-mc1.21.1.jar` | Alternate version archived; use only one Numismatics version per profile. Keep the established 1.0.20 baseline in the active server test profile unless a separately approved 1.1.0 test is opened |
| `numismatics_plus-1.0.1.jar` | Addon archived; absent from the 14:09 runtime list and not currently part of the active server test profile. Reintroduce only for a separate compatibility test with Numismatics 1.0.20 |

`createkinetic-1.4.3.jar.original.bak` is a backup copy, not an active mod JAR. It is recorded here only to distinguish it from an installable mod file.

**Versioning:** this archive reconciliation did not itself increase the modpack version at the time. Superseded JAR copies, unaccepted candidates, client-only files parked outside the server, and the paused End test set are not counted as new accepted content removals. The current development version is now `v0.1.112-R002` following the separately accepted Every Compat and Moonlight updates.


## Latest dedicated-server retest — 5 November 2026, 22:27–22:31

The latest disposable-server log reached `Done (1.490s)`, prepared the test world, accepted a matching client login, and stopped cleanly with all dimensions saved. This is a routine smoke-test pass only, not feature validation or release approval.

- **Create: Numismatics:** 1.0.20 was the only version detected and initialized. Numismatics 1.1.0 and Numismatics Plus 1.0.1 were absent from the runtime list. The duplicate-version issue is absent from this test snapshot; the Plus + 1.0.20 pairing remains untested.
- **Integrated Villages 1.3.3+1.21.1:** loaded with required Create 6.0.10, Integrated API 1.9.1, and Supplementaries 3.4.0 present. Several structure IDs were returned by disposable-world lookups, but this does not establish complete structure generation or replacement of vanilla villages.
- Some Integrated Villages locate searches took roughly 10–37 seconds and triggered tick-delay warnings. An Integrated API warning also identified an empty Cabin Village decoration pool. Keep the candidate under testing until representative structures and performance are checked.
- **Java GC observation:** the accompanying short GC trace shows heap reclamation after allocation peaks. It does not establish a long-term memory baseline or prove the absence of native/long-session memory issues.
- **Maintainer-reported GPU-memory observation:** GPU-memory usage appeared lower after Culling / More Culling candidates were disabled or parked. This is unquantified and not a controlled client A/B test; do not treat it as a proven performance gain or memory fix.
- Struts' dedicated-server RenderSystem issue and PowerGrid's unavailable optional native solver remain open.

The production world and its BYG 2.6.3 / Regions Unexplored 0.6.3 setup remain unchanged. No modpack version increment or release approval is implied by this documentation update.


## Latest dedicated-server folder inventory — 6 November 2026

The maintainer confirmed this screenshot is from the dedicated-server `mods` folder. It shows **106 visible JAR files**, superseding the older 104-file server-folder screenshot as the latest visual observation. This is not a runtime log, final release manifest, CurseForge export, compatibility pass, or feature-test result. The client inventory is separate and is not updated by this screenshot. A later supplied `Create World/mods` screenshot now confirms Every Compat 2.11.57 and Moonlight Lib 3.8.2 in the original client baseline; this does not update or verify the dedicated-server folder listing below.

### Exact visible server JAR filenames

- `aeronautical_diesel-1.1.0.jar`
- `aeroportals-1.21.1-1.3.6.jar`
- `appleskin-neoforge-mc1.21-3.0.9.jar`
- `architectury-13.0.11-neoforge.jar`
- `athena-neoforge-1.21.1-4.0.6.jar`
- `azimuth-1.4.10.jar`
- `balm-neoforge-1.21.1-21.0.67.jar`
- `bellsandwhistles-0.4.7-1.21.1.jar`
- `bits_n_bobs-2.3.5.jar`
- `bookshelf-neoforge-1.21.1-21.1.81.jar`
- `botanypots-neoforge-1.21.1-21.1.44.jar`
- `chipped-neoforge-1.21.1-4.0.2.jar`
- `cloth-config-15.0.140-neoforge.jar`
- `ConstructionSticks-1.21.1-1.5.0.jar`
- `copycats-3.0.9+mc.1.21.1-neoforge.jar`
- `copycats-plus-additions-1.5.0-neo.jar`
- `Corgilib-NeoForge-1.21.1-5.0.0.10.jar`
- `cr_aero_structures.jar`
- `Create Encased-1.21.1-1.10.0-fix1.jar`
- `create_aeronautics_transmission_linkage-0.2.9.jar`
- `create_bb-1.0.8-1.21.1.jar`
- `create_curios_backtank-neoforge-1.21.1-1.0.2.jar`
- `create_pattern_schematics-2.0.10.jar`
- `create_rustic_structures-1.0.1-neoforge-1.21.1.jar`
- `create_unified_fuels-1.0.4.jar`
- `create_vibrant_vaults-0.3.2.jar`
- `create-1.21.1-6.0.10.jar`
- `createaddition-1.7.2.jar`
- `create-aeronautics-bundled-1.21.1-1.3.2.jar`
- `CreateAeronauticsCopycatWing-1.21.1-1.0.4.jar`
- `createaeronauticscurios-neoforge-1.21.1-2.3.jar`
- `createbigcannons-5.11.7+mc.1.21.1.jar`
- `createcobblestone-1.5.1+neoforge-1.21.1-160.jar`
- `createdeco-2.1.3.jar`
- `createdieselgenerators-1.21.1-1.3.15.jar`
- `CreateDragonsPlus-1.11.9.jar`
- `create-enchantment-industry-2.5.4b.jar`
- `createframed-1.21.1-1.8.2.jar`
- `createkinetic-1.4.3.jar`
- `createliquidfuel-3.0.0-1.21.1.jar`
- `CreateNumismatics-1.0.20+neoforge-mc1.21.1.jar`
- `create-otbwg-compat-1.0.jar`
- `Create-Structures-Arise-1.21.1-NeoForge-176.49.50.jar`
- `cupboard-1.21.1-4.2.jar`
- `curios-neoforge-9.5.1+1.21.1.jar`
- `Design-n-Decor-1.21.1-2.2b.jar`
- `dragonlib-3.0.29+mc1.21.1-neoforge.jar`
- `enchdesc-neoforge-1.21.1-21.1.11.jar`
- `everycomp-1.21-2.11.56-neoforge.jar`
- `ExplorersCompass-1.21.1-3.4.0-neoforge.jar`
- `FarmersDelight-1.21.1-1.3.4.jar`
- `FastFurnace-1.21.1-9.0.1.jar`
- `FastSuite-1.21.1-6.0.7.jar`
- `ferritecore-7.0.3-neoforge.jar`
- `fluid_be_gone-1.0.1.jar`
- `ftb-chunks-neoforge-2101.1.23.jar`
- `ftb-jei-extras-21.1.7.jar`
- `ftb-library-neoforge-2101.1.39.jar`
- `ftb-teams-neoforge-2101.1.12.jar`
- `ftb-xmod-compat-neoforge-21.1.14.jar`
- `gadgets-and-gizmos-bundled-V1.2.10.jar`
- `geckolib-neoforge-1.21.1-4.9.3.jar`
- `herbsandharvest-1.21.1-24.jar`
- `incontrol-1.21-10.3.1.jar`
- `integrated_api-neoforge-1.21.1-1.9.1.jar`
- `integrated_villages-1.3.3+1.21.1-neoforge.jar`
- `Jade-1.21.1-NeoForge-15.10.6.jar`
- `jei-1.21.1-neoforge-19.64.0.455.jar`
- `jeistuff-1.21.1-1.3.0.jar`
- `JustEnoughResources-NeoForge-1.21.1-1.6.0.57.jar`
- `KineticGrip-1.21.1-1.0.5.jar`
- `kotlinforforge-5.12.0-all.jar`
- `lithostitched-1.8.1-neoforge-21.1.jar`
- `lootr-neoforge-1.21.1-1.11.38.127.jar`
- `memorysettings-1.21-6.0.jar`
- `mezz_config-1.21.1-neoforge-0.6.10-standalone.jar`
- `modernfix-neoforge-5.27.27+mc1.21.1.jar`
- `moderntrainparts-0.2.5-neoforge-mc1.21.1-cr6.0.10.jar`
- `moonlight-1.21.1-3.8.1-neoforge.jar`
- `MouseTweaks-neoforge-mc1.21-2.26.1.jar`
- `NaturesCompass-1.21.1-3.4.0-neoforge.jar`
- `Oh-The-Biomes-Weve-Gone-NeoForge-2.6.3.jar`
- `Oh-The-Trees-Youll-Grow-neoforge-1.21.1-5.3.5.jar`
- `pantographsandwires-neoforge-1.21.1-beta-0.2.3-C6.jar`
- `pipeorgans-0.9.2.1+1.21.1.jar`
- `Placebo-1.21.1-9.9.4.jar`
- `powergrid-mc1.21.1-0.6.2.jar`
- `prickle-neoforge-1.21.1-21.1.11.jar`
- `railways-0.3.0-beta.2+neoforge-mc1.21.1.jar`
- `regions-unexplored-0.6.3-neoforge-21.1.jar`
- `resourcefullib-neoforge-1.21-3.0.12.jar`
- `ritchiesprojectilelib-2.1.2-mc.1.21.1-neoforge.jar`
- `sable-neoforge-1.21.1-2.0.6.jar`
- `shield_generators-1.4.0.jar`
- `shulkerboxtooltip-neoforge-5.1.9+1.21.1.jar`
- `sliceanddice-4.3.4-neoforge.jar`
- `sophisticatedairtank-1.0.1-beta+1.21.1.jar`
- `sophisticatedbackpacks-1.21.1-3.26.20.2244.jar`
- `sophisticatedbackpackscreateintegration-1.21.1-0.2.3.194.jar`
- `sophisticatedcore-1.21.1-1.5.28.2458.jar`
- `spark-1.10.124-neoforge.jar`
- `struts-1.3.1.jar`
- `supplementaries-1.21.1-4.0.2-neoforge.jar`
- `TerraBlender-neoforge-1.21.1-4.1.0.8.jar`
- `tfmg-1.21.1-1.3.3-community.jar`
- `waystones-neoforge-1.21.1-21.1.46.jar`

### Items requiring reconciliation

- `cr_aero_structures.jar` has no visible version, but the supplied JAR metadata identifies 1.1.0-Beta-3.1 and matches official CurseForge file 8399115 by version (downloaded bytes not hash-compared). The test-only 16-color uniform-loot override passed runtime testing; the official JAR remains unchanged. All 11 valid Overworld structure IDs have locate/visual-presence evidence; one crashed-airship vanilla chest has no assigned loot table, while engineering-house standard and Lootr barrels produced items. Remaining container-loot coverage is delegated to beta testers; the specific chest defect and release-safe correction/distribution decision remain open.
- Railways appears as `0.3.0-beta.2`, compared with earlier `0.3.0-alpha.2` notes. Runtime selection and exact file provenance remain to be checked.
- Supplementaries appears as `4.0.2`, compared with earlier `3.4.0` dependency notes. Verify the exact file and dependency compatibility.
- Sophisticated Backpacks Create Integration appears as `0.2.3.194`; verify against prior records.
- The folder listing does not prove successful loading or feature behavior. Later 6 November disposable-profile tests passed the local Struts server/client workaround for the shown components and passed PowerGrid Windows native loading on both server and client. The standard-install Struts release issue remains open because the official JAR is unchanged. PowerGrid electrical-network/component behavior is reserved for beta testers; Linux native loading is a separate future platform test. The local PowerGrid DLL copies are not part of the distributable beta package, so native-resource packaging remains a release decision. See `TESTING_CHECKLIST.md` and `KNOWN_ISSUES.md` for current player-facing status.
- No additional installation/removal decision is implied by this 6 November folder screenshot. Its physical JAR list predates the 7 November accepted Every Compat/Moonlight update; the current accepted development version is `v0.1.112-R002`; the original client is updated, while normal dedicated-server deployment is pending.
