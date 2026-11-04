# Dimension Mod Guide — Create IronWoven

**Target:** Minecraft 1.21.1 · NeoForge 21.1.265  
**Mod download source:** CurseForge only

The mod project is now organised into three dimension areas so that world-generation and exploration additions can be researched and tested separately.

This page is a navigation guide, not a second mod inventory. The installed/test inventory stays in [MODS.md](MODS.md), candidate status stays in [MOD_PLANS.md](MOD_PLANS.md), and unfinished work stays in [TESTING_CHECKLIST.md](TESTING_CHECKLIST.md).

## Overworld

**Coverage:** biomes, terrain, caves, vegetation, structures, villages, mobs, ores/resources, and exploration.

The recorded world-generation baseline includes BYG 2.6.3 and Regions Unexplored 0.6.3, with their supporting world-generation components. The production world and its current world-generation setup are to remain unchanged during candidate research.

New Overworld candidates will be listed in [MOD_PLANS.md](MOD_PLANS.md) and tested separately in disposable worlds.

## Nether

**Coverage:** Nether biomes and terrain, fortresses and other structures, mobs, ores/resources, and Nether-specific progression.

Nether-specific additions will have their own research and test grouping. No Nether candidate is promoted or approved by this documentation change.

## End

**Coverage:** End islands and biomes, central island, outer-island structures, End Cities and ships, mobs, bosses, ores/resources, loot, and progression.

The current End research includes the BetterEnd and YUNG's Better End Island lines, plus separate End structure candidates. Their exact versions, dependencies, test results, and outstanding checks are recorded in [MOD_PLANS.md](MOD_PLANS.md) and [TESTING_CHECKLIST.md](TESTING_CHECKLIST.md).

The recorded BetterEnd ship/Lootr limitation remains documented: normal End City chests and ships worked in the maintainer's test, while BetterEnd-generated ships did not. This is a known partial compatibility result, not a general conclusion about all End containers.

## Shared / multi-dimension

Mods that intentionally affect multiple dimensions are recorded once as shared/multi-dimension, with the affected dimensions named. General libraries, performance mods, UI mods, and pack-wide utilities remain in the main inventory rather than being duplicated in all three dimension sections.

## Organisation rules

- Keep Overworld, Nether, and End research and test worlds separate.
- Test each dimension-generation candidate alone in a fresh disposable world before testing combinations.
- Do not duplicate a mod's status across dimension pages.
- Keep candidate, installed/test, partial-pass, on-hold, and excluded statuses distinct.
- A startup pass does not prove gameplay features or compatibility.
- Do not change the production world or installed pack as part of documentation organisation.

For exact status and test steps, use [MOD_PLANS.md](MOD_PLANS.md) and [TESTING_CHECKLIST.md](TESTING_CHECKLIST.md).
