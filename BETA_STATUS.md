# Create IronWoven — Beta Status

**Current modpack version:** `v0.1.000` · Internal development version; no downloadable beta package has been published.

**Last updated:** 5 November 2026  
**Minecraft:** 1.21.1 · **NeoForge:** 21.1.265 · **Java:** 21  

## Current stage

**Internal compatibility testing and public feedback.** No downloadable beta package or release date has been announced.

- [Installed/test inventory](MODS.md)
- [Mod plans and exclusions](MOD_PLANS.md)
- [Open tests](TESTING_CHECKLIST.md)
- [Known issues](KNOWN_ISSUES.md)
- [Support and privacy guidance](SUPPORT.md)
- [CurseForge release checks](CURSEFORGE_RELEASE_CHECK.md)

## Current test status

- **Batches A, B, and C:** routine server startup, disposable-world load, matching client login, and log-review smoke tests passed. These results do not claim feature-by-feature gameplay testing or production/release approval.
- **Batch D — Create Aeronautics Structures 1.1.0-Beta-3.1:** remains partial. The `cr_aero_structures:chests/uniform` loot-table error, exact CurseForge file provenance, and structure generation remain unresolved. Its Russian startup message is informational only and is not a blocker.
- **Batch E — performance:** the first combined server smoke test passed. A later 14:09 update-trial run also completed the full routine sequence (`Done`, disposable-world load, matching client login, clean shutdown), but the four client-only rendering mods were still in the server folder. spark selected the built-in Java engine; no performance measurements or saved profile were captured. Flerovium 1.1.3 Beta was detected instead of the planned stable 1.1.2. Batch E remains partial and is not production/release approval.
- **Functional coverage:** the [Full Installed-Mod Functional Testing Checklist](TESTING_CHECKLIST.md) now records the primary function test for each installed feature mod and integration checks for support libraries. Most function tests remain pending; combined smoke-test passes are not feature passes. Full functional coverage is required before beta release.
- **Curios:** the maintainer reports two Back slots in a newly created test world. Backpack + standard Create Backtank, Aviator Goggles, and Linked Typewriter checks are reported working in their assigned slots. More Curios Slots 1.4 was intentionally removed; craftable slot upgrades are not planned. Matching client/server log review remains open.
- **Botany Pots and Construction Sticks:** server startup checks passed; feature validation remains open.
- **Lootr:** chest opening and loot presence were confirmed by the maintainer; independent per-player loot remains unverified.
- **Compatibility datapacks:** targeted fixes passed smoke tests when the required world-scoped datapacks were loaded. Confirm they are present in each new test world before interpreting related errors.
- **Dedicated server:** Struts still attempts to load a client-only class. PowerGrid's optional native solver did not load in the tested Windows environment.
- **End content:** research and testing are paused. The 5 November folder screenshots visually verified that End-specific content/generation mods were absent from the reviewed test folders. Do not resume without explicit maintainer approval.

## Latest Batch D test — 5 November 2026

The 05:48–05:58 disposable-server run reached `Done (1.589s)!`, loaded `world_lootr_test`, accepted one client login, and shut down with all dimensions saved. The candidate-specific loot-table error remains unresolved; the startup message is not a blocker. The server log also contains broader pack errors and warnings, so the Batch D result is partial, not a general pack-cleanliness pass.

## Latest Batch E test — 5 November 2026

The 07:15–07:30 disposable-server run reached `Done (1.718s)!`, loaded the test world, accepted one client login, and shut down cleanly with all dimensions saved. spark 1.10.124 initialized and selected the built-in Java engine on Windows 11 / amd64; no TPS/MSPT, CPU, memory, GC baseline values, or saved profiler report were captured. ImmediatelyFast 1.6.15, Flerovium 1.1.3 Beta, Entity Culling 1.10.4, More Culling 1.0.11, and Cloth Config 15.0.140 were detected. The four rendering mods are client-only and must be tested on the matching client separately, one at a time. The log contains broader existing pack errors; the combined run does not verify individual visual features or performance improvement.



## Latest existing-mod update trial — 5 November 2026

A separate disposable-server attempt at 13:43 failed during mod loading, before `Done`, world load, client login, or normal shutdown. FTB Teams was missing while FTB Chunks required it, and Numismatics 1.1.0 did not satisfy Numismatics Plus 1.0.1's exact Numismatics 1.0.20 dependency. The next test must restore Numismatics 1.0.20, add FTB Teams 2101.1.12, and keep client-only rendering mods out of the server folder. The other newer files were detected but are not accepted or release-approved. See [Testing Checklist](TESTING_CHECKLIST.md) and [Mod Plans](MOD_PLANS.md).


## Previous existing-mod update retry — 5 November 2026, 13:58 (historical)

The later disposable-server retry detected and initialized FTB Teams 2101.1.12, clearing the earlier missing-FTB-Teams blocker for this server attempt. The server reached `Done (1.493s)` and prepared the test world. The logs do not show client login or clean shutdown, so this is a partial server startup/world-load pass only.

Both Numismatics 1.0.20 and 1.1.0 JARs were present; the loader selected 1.1.0. Numismatics Plus 1.0.1 was absent from the runtime list, so its compatibility was not tested. Do not keep both Numismatics versions in one profile. Use 1.0.20 only with Numismatics Plus 1.0.1, or test 1.1.0 separately without Plus until compatibility is verified. Client-only rendering mods remain in the server folder and still require separate client tests. See [Testing Checklist](TESTING_CHECKLIST.md) and [Mod Plans](MOD_PLANS.md).

## Project direction

Create IronWoven focuses on Create, Create Aeronautics, trains, automation, engineering, transport, and exploration. The production world and its existing BYG 2.6.3 / Regions Unexplored 0.6.3 setup remain protected.

## Release readiness

The pack is **not ready for release**. A fresh client manifest and server inventory, clean-install validation, outstanding compatibility checks, privacy review, and the release checklist remain outstanding.

## Latest existing-mod update smoke test — 5 November 2026, 14:09

The later disposable-server run reached `Done (1.822s)`, loaded the test world, accepted a matching client login, and shut down cleanly with all dimensions saved. FTB Teams 2101.1.12 was present and initialized; the earlier missing-FTB-Teams blocker did not recur.

Both Numismatics 1.0.20 and 1.1.0 JARs were still present, and 1.1.0 was active. Numismatics Plus 1.0.1 was absent, so neither the Plus pairing nor the 1.0.20 runtime was tested. Use exactly one Numismatics version per test profile. ImmediatelyFast 1.6.15, Flerovium 1.1.3, Entity Culling 1.11.3, and More Culling 1.0.11 were still present in the dedicated-server folder; their client functions remain untested.

The log contains 463 ERROR-level and 172 WARN-level entries, including recurring loot-table and existing compatibility errors. spark selected its built-in Java engine, but no measured performance baseline or saved profile was captured. This was a routine smoke-test pass only, not a feature test or update approval. Batch D and Batch E remain partial. No update is approved for production or beta release. See [Testing Checklist](TESTING_CHECKLIST.md), [Mod Plans](MOD_PLANS.md), and the private [server test report](https://github.com/alexth110987/Create-IronWoven/blob/main/docs/SERVER_TEST_2026-11-05.md).