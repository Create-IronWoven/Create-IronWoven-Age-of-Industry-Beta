# Testing Checklist — Mods and Compatibility

**Last updated:** 5 November 2026  
**Target:** Minecraft 1.21.1 / NeoForge 21.1.265 / Java 21  
**Mod download source:** CurseForge only

This is the live queue of unfinished tests. It does not approve mods for the production pack or public release. Dated technical evidence and historical research remain in the private development repository.

## Routine batch test

1. Start the dedicated test server and confirm it reaches `Done`.
2. Confirm the disposable test world loads.
3. Join with the matching client.
4. Review the relevant logs.

Manual crafting, extended gameplay, and feature-by-feature playtests are not required by default. Deeper testing needs a specific unresolved issue and maintainer agreement.

## Current batch position

- **Batches A, B, and C:** routine startup, world-load, matching-client login, and log-review smoke tests passed.
- **Batch D — Create Aeronautics Structures 1.1.0-Beta-3.1:** partial. The disposable server reached `Done`, loaded the test world, accepted a client login, and shut down cleanly. A candidate-specific loot-table parsing ERROR remains unresolved. Exact CurseForge file provenance and structure generation are unverified.
- **Batch E — performance tests:** started by the maintainer while Batch D remains partial. The first combined server smoke test passed, but four client-only visual mods were also present in the server folder and no performance measurements were captured. Batch E remains partial; see the active tests below.

Batch D startup message:
`Мод Create Aeronautics Structures загружается!`
**English translation:** “Create Aeronautics Structures is loading!” (informational only; not a blocker).

## Active tests

### Create Aeronautics Structures — Batch D

- [x] Disposable Overworld server/world test.
- [x] Server startup, world load, matching client login, and clean shutdown.
- [ ] Investigate the `cr_aero_structures:chests/uniform` loot-table parsing error.
- [ ] Verify the exact CurseForge 1.21.1 NeoForge file and dependency declarations.
- [ ] Confirm actual Overworld structure generation; the server log does not prove structures generated.

#### Batch E — performance — 5 November 2026

**Status: PARTIAL — combined server smoke test passed; baseline and isolated client tests remain open.**

- [x] spark 1.10.124 loaded on the disposable server and started its background profiler.
- [x] Server reached `Done (1.718s)!`, loaded the disposable world, accepted a matching client login, and shut down with all dimensions saved.
- [ ] Repeat the baseline with spark alone on the dedicated server and record actual TPS/MSPT, CPU, memory, GC, and saved profiler output. The first log only confirms that the built-in Java engine was selected; async-profiler is unsupported on Windows 11 / amd64, and no metrics were recorded.
- [ ] Keep ImmediatelyFast 1.6.15, Flerovium, Entity Culling 1.10.4, and More Culling 1.0.11 out of the dedicated-server `mods` folder; test them on the matching client one at a time.
- [ ] Reconcile Flerovium: the log detected 1.1.3 Beta, while the planned candidate is stable 1.1.2. Do not count the planned stable test as complete.
- [ ] Verify More Culling 1.0.11's exact CurseForge file provenance; Cloth Config API 15.0.140 was detected as its dependency.
- [ ] Review the matching client log and record whether any new client-side rendering errors occur.

The log contains broader pack issues, including the existing Struts, PowerGrid, Every Compat, loot-table, and Create Deco errors. Do not attribute these pack-level entries to Batch E without specific evidence. This combined test is not production or release approval.
## Curios add-on group

**Targeted checks are reported working; matching client/server log review remains open.**

- [x] New-world config displays two Back slots and one Head slot.
- [x] Backpack + standard Create Backtank use reported working.
- [x] Aviator Goggles and Linked Typewriter reported working in their assigned slots.
- [ ] Review matching client/server logs for registration or synchronization errors.

More Curios Slots 1.4 was intentionally removed. Craftable slot upgrades are not wanted; do not reinstall it unless the maintainer changes that decision.

### Botany Pots 21.1.44

**Server startup passed; feature validation remains open.**

- [ ] Check planting, growth, harvesting, drops, and relevant JEI visibility.
- [ ] Review Herbs & Harvest integration recipes. Forty-seven optional recipes remain suppressed by temporary `neoforge:false` overrides; test any conditional datapack change in a disposable copy only.

### Construction Sticks 1.5.0

**Server startup passed; feature validation remains open.**

- [ ] Check representative vanilla/modded placement, orientation, item consumption, and FTB Chunks claim behavior.

### Lootr 1.11.38.127

- [x] Maintainer confirmed a test chest opens and contains loot.
- [ ] Have a second player open the same Lootr chest and verify independent personal loot.

The earlier BetterEnd ship limitation is historical. End research/testing is paused and BetterEnd is not in the current reviewed test folders.

## Outstanding compatibility issues

- **World-scoped compatibility datapacks:** confirm required IronWoven datapacks are loaded in each disposable world before interpreting related Design n' Decor, Steam 'n' Rails, Create Kinetic, Create Deco, or Sable / Copycats errors.
- **Struts 1.3.1:** investigate its attempt to load client-only `com.mojang.blaze3d.systems.RenderSystem` on the dedicated server.
- **Create: Power Grid 0.6.2:** confirm core behavior with the fallback solver and investigate the unavailable optional `powergridNative7` library.

## Future batches

Batch E is now in progress and remains partial. Batches F–H have not started and are not approved. Follow the [private active batch plan](https://github.com/alexth110987/Create-IronWoven/blob/main/docs/ACTIVE_INSTALLATION_BATCH_PLAN_2026-11-05.md).

| Batch | Scope | Candidates |
|---|---|---|
| E | Performance — in progress | spark 1.10.124 server baseline; then separate client-only tests for ImmediatelyFast 1.6.15, Flerovium (planned stable 1.1.2; 1.1.3 Beta was detected), Entity Culling 1.10.4, and More Culling 1.0.11. More Culling's exact file ID needs reconciliation. |
| F | Server/recipe optimizers | Lithium 0.15.4, FastSuite 6.0.7, FastFurnace 9.0.1. |
| G | World utilities/generation | Chunk-Pregenerator 4.5.4 and Tectonic 3.0.28 in separate disposable worlds. |
| H | Travel system | Waystones 21.1.46 after review of AeroPortals 1.3.6 and Balm. |

## On hold and safeguards

- End content and Terralith remain on hold. Do not resume without explicit approval.
- Colony ecosystem work remains research only; no colony component is installed or approved.
- Keep the production world and BYG 2.6.3 / Regions Unexplored 0.6.3 setup unchanged.
- Use disposable worlds for world-generation/structure tests and keep client-only mods out of the dedicated server.
- CurseForge is the only approved mod download source.
- A smoke-test pass does not mean production or release approval.
