# Create IronWoven — Beta Status

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
- **Batch D — Create Aeronautics Structures 1.1.0-Beta-3.1:** partial. The disposable server started, loaded the test world, accepted a client login, and shut down cleanly. Its startup message is informational only:  
  `Мод Create Aeronautics Structures загружается!`  
  **English translation:** “Create Aeronautics Structures is loading!”  
  The `cr_aero_structures:chests/uniform` loot table failed to parse. Exact CurseForge file provenance and structure generation remain unverified. Do not advance to Batch E until the issue and outstanding checks are reviewed.
- **Curios:** the maintainer reports two Back slots in a newly created test world. Backpack + standard Create Backtank, Aviator Goggles, and Linked Typewriter checks are reported working in their assigned slots. More Curios Slots 1.4 was intentionally removed; craftable slot upgrades are not planned. Matching client/server log review remains open.
- **Botany Pots and Construction Sticks:** server startup checks passed; feature validation remains open.
- **Lootr:** chest opening and loot presence were confirmed by the maintainer; independent per-player loot remains unverified.
- **Compatibility datapacks:** targeted fixes passed smoke tests when the required world-scoped datapacks were loaded. Confirm they are present in each new test world before interpreting related errors.
- **Dedicated server:** Struts still attempts to load a client-only class. PowerGrid's optional native solver did not load in the tested Windows environment.
- **End content:** research and testing are paused. The 5 November folder screenshots visually verified that End-specific content/generation mods were absent from the reviewed test folders. Do not resume without explicit maintainer approval.

## Latest Batch D test — 5 November 2026

The 05:48–05:58 disposable-server run reached `Done (1.589s)!`, loaded `world_lootr_test`, accepted one client login, and shut down with all dimensions saved. The candidate-specific loot-table error remains unresolved; the startup message is not a blocker. The server log also contains broader pack errors and warnings, so the Batch D result is partial, not a general pack-cleanliness pass.

## Project direction

Create IronWoven focuses on Create, Create Aeronautics, trains, automation, engineering, transport, and exploration. The production world and its existing BYG 2.6.3 / Regions Unexplored 0.6.3 setup remain protected.

## Release readiness

The pack is **not ready for release**. A fresh client manifest and server inventory, clean-install validation, outstanding compatibility checks, privacy review, and the release checklist remain outstanding.
