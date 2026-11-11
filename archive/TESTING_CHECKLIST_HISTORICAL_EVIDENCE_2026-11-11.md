# Archived Beta Checklist Evidence — 11 November 2026

This file preserves dated and superseded evidence removed from the live beta-tester checklist. It is for historical comparison and issue diagnosis only. It is **not** a current installed-mod inventory, active testing queue, setup instruction, or release manifest.

Use [the current functional checklist](../../TESTING_CHECKLIST.md), [current mod summary](../../MODS.md), and [current plans](../../MOD_PLANS.md) for active decisions. The active-profile snapshot and its full file/hash inventory remain private development evidence.

## Historical failed / partial update trials — 5 November 2026

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

## Superseded client-rendering candidate rows

The following rows came from an earlier client-profile review and are retained only as history. The 10 November complete working-profile inventory does not contain these rendering candidates. Do not use these rows as current installation or beta-testing instructions.

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

## Earlier numbered smoke-group notes — 6 November 2026

These notes describe the former smoke-test grouping. The numbered sequence is retired; the current checklist is organized by mod and feature.

- **Batch A:** JER, Enchantment Descriptions and Shulker Box Tooltip passed combined startup/login smoke testing. A later 6 November test exposed a dedicated-server error in the Shulker Box Tooltip / Supplementaries provider integration; Shulker Box Tooltip's own providers still registered. Feature rendering/use remains to be checked.
- **Batch B:** Nature's Compass and Explorer's Compass passed combined startup/login smoke testing; actual biome/structure searches remain to be checked.
- **Batch C:** Create Big Cannons and Ritchie's Projectile Library passed combined startup/login smoke testing; cannon operation remains to be checked.
- **Client-only rendering candidates:** Entity Culling is removed from the current CurseForge client profile (confirmed by the 6 November screenshot) and is not in the active test queue. ImmediatelyFast, Flerovium and More Culling remain optional candidates only; verify their presence against a fresh client export before testing. spark profiling is deferred to beta testers and is not an internal development gate.

## Historical inventory, smoke and Aeronautics Structures evidence

The detailed records below are preserved from the former checklist. The current Aeronautics Structures decision is ON HOLD; do not resume testing from these historical instructions. Other observations below remain historical evidence and do not override the current status pages.

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


## Superseded client graphics/performance action matrix

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


