# Dimension Mod Guide — Create IronWoven

**Target:** Minecraft 1.21.1 · NeoForge 21.1.265  
**Mod download source:** CurseForge only

This page explains how world-generation and exploration work is grouped. It is a navigation guide, not a second mod inventory:

- Installed/test inventory: [MODS.md](MODS.md)
- Candidate, on-hold, and excluded status: [MOD_PLANS.md](MOD_PLANS.md)
- Unfinished tests: [TESTING_CHECKLIST.md](TESTING_CHECKLIST.md)

## Overworld

**Coverage:** biomes, terrain, caves, vegetation, structures, villages, mobs, ores/resources, and exploration.

The recorded world-generation baseline includes BYG 2.6.3 and Regions Unexplored 0.6.3, with their supporting components. The production world and its current world-generation setup must remain unchanged during candidate research.

**Create Aeronautics Structures 1.1.0-Beta-3.1** is an Overworld test candidate, not an End mod. The 5 November disposable-server run completed startup, world load, client login, and clean shutdown, but its `cr_aero_structures:chests/uniform` loot table failed to parse. Its Russian startup message is informational only and is not a blocker. Exact CurseForge file provenance and structure generation remain unverified. See [Mod Plans](MOD_PLANS.md) and [Testing Checklist](TESTING_CHECKLIST.md).

## Nether

**Coverage:** Nether biomes and terrain, fortresses and other structures, mobs, ores/resources, and Nether-specific progression.

No Nether candidate is currently promoted or approved. Additions must be researched and tested separately in fresh disposable worlds.

## End

**Status: PAUSED by maintainer.**

End-mod research and testing are paused because no suitable CurseForge-only Minecraft 1.21.1 / NeoForge mod has been found for the desired Create-style abandoned-industrial End.

The saved future direction is an abandoned industrial civilisation with derelict factories, refineries, mines, industrial settlements, broken railways, cargo infrastructure, and Create-inspired engineering. This is a future concept, not an active search or test queue.

The 5 November screenshots of the disposable server and client mod folders visually verified that End-specific content/generation mods and the listed End-only support libraries were absent from those folders. Lootr remains a general-purpose mod and is not an End overhaul.

- Do not resume End searches, shortlist additions, installations, or tests unless the maintainer explicitly reopens this workstream.
- Previously researched End candidates are historical only; none is approved by this pause.
- Preserve the production world and existing world-generation settings.

## Shared / multi-dimension

Mods that intentionally affect multiple dimensions are recorded once as shared/multi-dimension, with the affected dimensions named. General libraries, performance mods, UI mods, and pack-wide utilities remain in the main inventory rather than being duplicated across dimension sections.

## Organisation rules

- Keep Overworld, Nether, and End records separate.
- Test active dimension-generation candidates in fresh disposable worlds.
- Do not duplicate a mod's status across dimension pages.
- Keep installed/test, candidate, partial-pass, on-hold, and excluded statuses distinct.
- A startup pass does not prove gameplay features or compatibility.
- Do not change the production world or installed pack as part of documentation organisation.

For exact status and test steps, use [MOD_PLANS.md](MOD_PLANS.md) and [TESTING_CHECKLIST.md](TESTING_CHECKLIST.md).
