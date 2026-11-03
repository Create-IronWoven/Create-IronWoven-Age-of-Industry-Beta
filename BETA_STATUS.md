# Create IronWoven — Beta Status

**Last updated:** 3 November 2026  
**Minecraft:** 1.21.1  
**Loader:** NeoForge 21.1.265  
**Java:** 21

## Current stage

**Current stage: Internal testing / public feedback hub**

The pack is undergoing compatibility and dedicated-server testing. This repository is open for collecting feedback and documenting progress. A public downloadable beta build has **not** been announced here.

## Mod list and future plans

- [Mods in the current test pack](MODS.md)
- [Mods planned, on hold, or excluded](MOD_PLANS.md)

The current mod inventory is a dated test snapshot. Batch 7 has not started, and no Batch 7 additions are approved yet. Terralith remains on hold.

## Project direction

Create IronWoven aims to combine:
- Create and Create Aeronautics
- Trains, transport, and engineering
- Automation and industrial building
- Exploration and world discovery

## Internal test progress snapshot

The maintainer's dedicated-server smoke tests have confirmed the following targeted fixes:

| Area | Current status |
|---|---|
| Create Deco placard recipe correction | Passed smoke test |
| Optional Herbs & Harvest Botany Pots recipe references | Suppressed; passed smoke test |
| Optional Design n' Decor Dye Depot loot references | Suppressed; passed smoke test |
| Steam 'n' Rails missing-item loot references | Passed smoke test |
| Create: Enchantment Industry optional integration loot references | Passed smoke test |
| Create Kinetic missing-item loot references | Passed smoke test |
| Sable / Copycats Catwalk physics selector | Passed smoke test |
| Create Kinetic dedicated-server client mixin | Passed smoke test |

These are maintainer-side smoke-test results, not a guarantee that every feature has been fully playtested.

## Remaining internal work

- Struts dedicated-server client-class mixin warning/error investigation.
- PowerGrid optional native accelerated solver does not currently load in the tested Windows server environment.
- Review remaining nonfatal data-map, item-tag, and biome mob-category warnings.
- Continue compatibility and client/server testing.

## Release readiness

No public beta package or release date is confirmed in this status file. The maintainer will update this page when a build is ready for external testers.

## How players can help now

You can report reproducible issues and suggest improvements through the [issue tracker](https://github.com/alexth110987/Create-IronWoven-Beta/issues). Please state clearly which Minecraft, NeoForge, and modpack build you are using.
