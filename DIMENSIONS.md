# Dimension Mod Guide — Create IronWoven

**Target:** Minecraft 1.21.1 · NeoForge 21.1.265  
**Mod download source:** CurseForge only

The mod project is organised into three dimension areas so that world-generation and exploration additions can be researched and tested separately.

This page is a navigation guide, not a second mod inventory. The installed/test inventory stays in [MODS.md](MODS.md), candidate status stays in [MOD_PLANS.md](MOD_PLANS.md), and unfinished work stays in [TESTING_CHECKLIST.md](TESTING_CHECKLIST.md).

## Overworld

**Coverage:** biomes, terrain, caves, vegetation, structures, villages, mobs, ores/resources, and exploration.

The recorded world-generation baseline includes BYG 2.6.3 and Regions Unexplored 0.6.3, with their supporting world-generation components. The production world and its current world-generation setup are to remain unchanged during candidate research.

New Overworld candidates will be listed in [MOD_PLANS.md](MOD_PLANS.md) and tested separately in disposable worlds. **Create Aeronautics Structures 1.1.0-Beta-3.1 has been tested in a disposable server but is blocked from acceptance** by a Russian startup message and a candidate-specific loot-table error. Exact CurseForge provenance and structure generation remain unverified. It is not an End mod.

## Nether

**Coverage:** Nether biomes and terrain, fortresses and other structures, mobs, ores/resources, and Nether-specific progression.

Nether-specific additions will have their own research and test grouping. No Nether candidate is promoted or approved by this documentation change.

## End

<badge>PAUSED</badge>

**Status:** End mod research and testing are paused by maintainer.

**Reason:** No suitable CurseForge-only Minecraft 1.21.1 / NeoForge mod has been found that delivers the desired Create-style, abandoned-industrial End. The available candidates researched so far do not meet that goal.

The future design concept is saved: an abandoned industrial civilisation with derelict factories, refineries, mines, industrial settlements, broken railways, cargo infrastructure and Create-inspired engineering. This is a future direction only, not an active search or test queue.

- Do not continue End-mod searches, shortlist additions, installations or tests unless the maintainer explicitly reopens this workstream.
- Previously recorded End candidates are historical research only; none is approved by this pause.
- Existing End compatibility notes, including the partial BetterEnd ship/Lootr limitation, remain historical records and are not active testing tasks.
- This pause does not authorize changes to the installed inventory, production server/world or world-generation settings.

## Shared / multi-dimension

Mods that intentionally affect multiple dimensions are recorded once as shared/multi-dimension, with the affected dimensions named. General libraries, performance mods, UI mods, and pack-wide utilities remain in the main inventory rather than being duplicated in all three dimension sections.

## Organisation rules

- Keep Overworld, Nether, and End records separate.
- Test active dimension-generation candidates in fresh disposable worlds.
- Do not duplicate a mod's status across dimension pages.
- Keep candidate, installed/test, partial-pass, on-hold, and excluded statuses distinct.
- A startup pass does not prove gameplay features or compatibility.
- Do not change the production world or installed pack as part of documentation organisation.

For exact status and test steps, use [MOD_PLANS.md](MOD_PLANS.md) and [TESTING_CHECKLIST.md](TESTING_CHECKLIST.md).

## End folder cleanup verification — 5 November 2026

The supplied screenshots of both `MinecraftServer-Test/mods` and the CurseForge `Create World/mods` folders show no End-specific content/generation JARs or End-only support libraries. The End cleanup is visually verified at screenshot level; the later 5 November server log confirms the End remains a loaded vanilla dimension, but does not identify End-specific content mods. The End workstream remains paused. Existing End candidate/test records are historical only, not an active queue. Lootr remains as a general-purpose mod. Create Aeronautics Structures was detected in a later disposable-server log as an Overworld candidate; its acceptance is blocked by a Russian startup message and a loot-table error.

