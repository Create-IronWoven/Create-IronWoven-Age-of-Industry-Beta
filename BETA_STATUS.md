# Create IronWoven — Beta Status

**Last updated:** 4 November 2026  
**Minecraft:** 1.21.1  
**Loader:** NeoForge 21.1.265  
**Java:** 21

## Current stage

**Current stage: Internal testing / public feedback hub**

The pack is undergoing compatibility and dedicated-server testing. This repository is open for collecting feedback and documenting progress. A public downloadable beta build has **not** been announced here.

## Mod list and future plans

- [Mods in the current test pack](MODS.md)
- [Mods planned, on hold, or excluded](MOD_PLANS.md)
- [Compatibility progress and known test results](COMPATIBILITY_PROGRESS.md)
- [Known issues](KNOWN_ISSUES.md)

The current mod inventory is a dated test snapshot. New requested candidates have been researched and recorded in MOD_PLANS.md. They are not installed or approved; Batch 7 has not started. Terralith remains on hold.

## Project direction

Create IronWoven aims to combine:
- Create and Create Aeronautics
- Trains, transport, and engineering
- Automation and industrial building
- Exploration and world discovery

## Internal test progress snapshot

The maintainer's latest available dedicated-server smoke test (latest(9).log, 3 November 2026, 22:57–22:58) confirms:

| Area | Current status |
|---|---|
| Create Deco placard recipe correction | Passed smoke test |
| Optional Herbs & Harvest Botany Pots recipe references | Suppressed by temporary pack workaround; passed log smoke test |
| Optional Design n' Decor Dye Depot loot references | Suppressed by temporary pack workaround; passed log smoke test |
| Steam 'n' Rails missing-item loot references | Passed smoke test |
| Create: Enchantment Industry optional integration loot references | Passed smoke test after separately testing version 2.5.4b |
| Create Kinetic missing-item loot references | Passed smoke test |
| Sable / Copycats Catwalk physics selector | Passed smoke test |
| Create Kinetic dedicated-server client mixin | Passed smoke test |

These are maintainer-side smoke-test results, not a guarantee that every feature has been fully playtested. The Botany Pots and Dye Depot suppressions are temporary pack workarounds, not upstream fixes; they must be revisited if those optional mods are added.

## Remaining internal work

- **Struts:** dedicated-server client-class error for RenderSystem remains. An exact upstream report already exists: [Struts issue #6](https://github.com/cakeGit/StrutYourStuff/issues/6).
- **PowerGrid:** optional native accelerated solver does not currently load in the tested Windows server environment; the non-accelerated solver remains available. The exact current cause is not yet confirmed.
- Review remaining nonfatal data-map, item-tag, and biome mob-category warnings.
- Continue compatibility and client/server testing.
- Review the requested planned mods one at a time; do not add them to the active inventory until approved and tested.

## Upstream handover status

Technical ownership, report drafts, and candidate corrections are being prepared for the mod developers who own the affected files. Existing destinations have been identified for Steam 'n' Rails, Copycats+, Create Deco, Design n' Decor, and Struts.

**No external mod developer report or patch has been submitted yet.** The current work is still in review. No personal credit, payment, or publicity is being requested. See [Compatibility Progress](COMPATIBILITY_PROGRESS.md) for the current upstream discussion links and test safeguards.

## Release readiness

No public beta package or release date is confirmed in this status file. The maintainer will update this page when a build is ready for external testers.

## How players can help now

You can report reproducible issues and suggest improvements through the [issue tracker](https://github.com/alexth110987/Create-IronWoven-Beta/issues). Please state clearly which Minecraft, NeoForge, and modpack build you are using.
