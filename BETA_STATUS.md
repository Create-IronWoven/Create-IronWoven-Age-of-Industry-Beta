# Create IronWoven — Beta Status

**Last updated:** 4 November 2026  
**Minecraft:** 1.21.1  
**Loader:** NeoForge 21.1.265  
**Java:** 21

## Current stage

**Current stage: Internal testing / public feedback hub**

The pack is undergoing compatibility and dedicated-server testing. This repository is open for collecting feedback and documenting progress. A public downloadable beta build has **not** been announced here.

## Mod list, plans, and test queue

- [Mods in the current test pack](MODS.md)
- [Mods planned, on hold, or excluded](MOD_PLANS.md)
- [Testing checklist — mods and what still needs testing](TESTING_CHECKLIST.md)

The testing checklist is the current queue for unfinished gameplay tests, compatibility retests, and research gates. Batch 2A (YUNG's Better End Island 3.1.2 + YUNG's API 5.1.9) has passed server mod discovery, startup, client login and clean shutdown. Gameplay checks remain pending. The user intentionally selected `world_lootr_test` because its End had not yet been generated; the world name is not a setup error. The world-scoped IronWoven compatibility datapacks also need to be checked and restored in the disposable test world if absent. It is not a release approval list. A mod can pass startup and still need feature testing.

## Project direction

Create IronWoven aims to combine:
- Create and Create Aeronautics
- Trains, transport, and engineering
- Automation and industrial building
- Exploration and world discovery

## Internal test progress snapshot

The maintainer's dedicated-server smoke tests have confirmed the following targeted fixes in the tested configuration:

| Area | Current status |
|---|---|
| Create Deco placard recipe correction | Passed smoke test; include the compatibility datapack in fresh test worlds |
| Optional Herbs & Harvest Botany Pots recipe references | Suppressed; 47 optional integration recipes remain disabled pending review |
| Optional Design n' Decor Dye Depot loot references | Passed smoke test when the IronWoven compatibility datapack is loaded |
| Steam 'n' Rails missing-item loot references | Passed smoke test when the IronWoven compatibility datapack is loaded |
| Create: Enchantment Industry optional integration loot references | Passed smoke test |
| Create Kinetic missing-item loot references | Passed smoke test when the IronWoven compatibility datapack is loaded |
| Sable / Copycats Catwalk physics selector | Passed smoke test when the IronWoven compatibility datapack is loaded |
| Create Kinetic dedicated-server client mixin | Passed smoke test |

These are maintainer-side smoke-test results, not a guarantee that every feature has been fully playtested. A fresh Lootr test world did not automatically include the custom IronWoven compatibility datapacks; the earlier errors reappeared in that test world.

## Remaining test work

- **Botany Pots 21.1.44:** loaded with Bookshelf 21.1.81 and Prickle 21.1.11; one Botany Pots plugin initialized and 14,444 recipes parsed without parser failures. Basic features and the Herbs & Harvest integration are expected to be testable. Planting, growth and harvesting still need in-game validation; 47 optional integration recipes remain suppressed by `neoforge:false` until a conditional `botanypots` test is completed in a disposable copy.
- **Construction Sticks 1.5.0:** startup passed; placement with modded blocks and FTB Chunks claim protections still needs testing.
- **Lootr 1.11.38.127:** the player confirmed opening a chest and finding loot; a second-player independent-loot test remains.
- **Struts 1.3.1:** dedicated-server attempt to load client-only `RenderSystem` remains under investigation.
- **PowerGrid 0.6.2:** optional `powergridNative7` accelerated solver did not load in the tested Windows server environment; fallback behavior and native-library availability need review.
- Review the unattributed world/chunk-generation messages after the compatibility datapacks are correctly loaded in a disposable world.
- Review requested End-generation and colony candidates only after exact CurseForge NeoForge files and dependencies are verified.

See the [full testing checklist](TESTING_CHECKLIST.md) for each test step and its current status.

## Batch 2 End-content review — 4 November 2026

Exact 1.21.1 NeoForge CurseForge files have been verified for YUNG's Better End Island, BetterEnd: New Dawn 21.0.39, Bigger Better End Cities, and Ender Villages 2.0. Their feature checks and dependencies are recorded in the [testing checklist](TESTING_CHECKLIST.md). These are candidates only; no files have been installed or approved. Test individually in disposable End worlds and preserve the production world.

## Release readiness

No public beta package or release date is confirmed in this status file. A test pass does not automatically approve a mod for release. The final client and server manifests, clean-install checks, and release validation remain outstanding.

## How players can help now

You can report reproducible issues and suggest improvements through the [issue tracker](https://github.com/alexth110987/Create-IronWoven-Beta/issues). Please state clearly which Minecraft, NeoForge, and modpack build you are using.


## Batch 2A runtime status — 4 November 2026

YUNG's API 5.1.9 and YUNG's Better End Island 3.1.2 were discovered and loaded on the separate test server. Server startup, client login and clean shutdown passed. The user clarified that `world_lootr_test` was selected intentionally because its End had not yet been generated. The earlier world-name mismatch assessment is corrected. The End-generation gameplay checks remain pending, and the custom IronWoven compatibility datapacks must be verified (and restored in this disposable world if absent) before continuing. See the [testing checklist](TESTING_CHECKLIST.md). No production changes or approval.


## Botany Pots update — 4 November 2026

The separate test server successfully loaded Botany Pots 21.1.44 with Bookshelf 21.1.81 and Prickle 21.1.11. Botany Pots reported one plugin loaded and the recipe manager parsed 14,444 recipes without recipe-parsing failures. This makes basic Botany Pots features and the optional Herbs & Harvest integration expected to be testable; it does not yet prove planting, growth, harvesting or integration behavior in-game.

The 47 Herbs & Harvest Botany Pots recipes remain suppressed by the temporary `neoforge:false` overrides. In a disposable test copy only, validate replacing those unconditional suppressions with a conditional `neoforge:mod_loaded` check for `botanypots`, then confirm the recipes in JEI and test representative crops. The production datapack remains unchanged until that test passes.


## Inventory, performance and QoL review — 4 November 2026

The current recorded baseline already has ModernFix and FerriteCore, plus client-side Sodium, Sodium Extra and Iris. The maintainer review has added candidate testing for ImmediatelyFast, Entity Culling, Lithium, FastSuite and FastFurnace, with spark as the diagnostic profiler. QoL candidates include JER, Shulker Box Tooltip, Enchantment Descriptions, Nature's Compass, Explorer's Compass and Waystones. None have been installed or approved by this review. Exact versions and test steps are in [MOD_PLANS.md](MOD_PLANS.md) and [TESTING_CHECKLIST.md](TESTING_CHECKLIST.md).
