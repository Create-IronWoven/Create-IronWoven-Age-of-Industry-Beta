# Mod Plans

This page gives players a short overview of planned, considered, paused, and excluded content. It is not the installed-mod list or a release approval list.

- [Mods in the current test snapshot](MODS.md)
- [What still needs testing](TESTING_CHECKLIST.md)
- [Current project status](BETA_STATUS.md)

**Target:** Minecraft 1.21.1 · NeoForge 21.1.265  
**Mod source policy:** CurseForge only

## Status meanings

| Status | Meaning |
|---|---|
| In testing | Present in a test profile; feature checks may be incomplete. |
| Candidate | Being considered; not installed or approved for release. |
| Partial | Some checks passed, but a problem or unanswered check remains. |
| On hold | Work is paused; do not assume it is being researched or tested. |
| Excluded | The maintainer has decided this content is not wanted. |

## Current testing and follow-ups

| Area | Public status |
|---|---|
| Create Aeronautics Structures | Partial. All 11 valid Overworld structure IDs have locate/visual-presence evidence; crashed-airship hillside placement was visually accepted and `plane` is invalid. Test-only uniform-loot override passed runtime testing. Engineering-house standard and Lootr barrels produced items; one crashed-airship vanilla chest has no assigned loot table. Remaining container-loot coverage is delegated to beta testers; the specific chest defect and release-safe uniform-table decision remain open; original JAR unchanged. |
| Performance and rendering | Partial. No measured server performance baseline yet; client rendering candidates require separate client tests. |
| Botany Pots and Construction Sticks | Loaded in a test group; feature validation remains open. |
| Lootr | Partial compatibility observations; independent per-player loot still needs verification. |
| Every Compat (Wood Good) | Accepted baseline target is 2.11.57 + Moonlight Lib 3.8.2 after the paired Windows disposable startup/world/login/shutdown smoke test. The Golden Cherry Leaves duplicate remains open. Feature-level block/recipe/model/texture/drop checks are delegated to beta testers. The original Create World client profile and normal MinecraftServer-Test dedicated-server baseline both contain the accepted JARs; startup/login verification on this updated baseline remains. |
| Exploration tools and Create Big Cannons | Routine startup/login smoke tests passed; this is not feature validation or release approval. |

Detailed technical evidence, exact file/dependency checks, and test history are maintained in the private development repository. The public [testing checklist](TESTING_CHECKLIST.md) is the place to see current testing tasks.

## Future ideas — Batch 7 (on hold)

**Batch 7 is postponed by the maintainer.** The following are possible future candidates only, not an active research or installation queue. No compatibility, dependency, feature, or release approval is implied.

- MineColonies and its potential dependency ecosystem: Structurize, Domum Ornamentum, BlockUI, and Multi-Piston.
- TownTalk as a possible settlement integration.
- Towns and Towers, Repurposed Structures, Moog's Voyager Structures, Moog's Soaring Structures, Better Villages, and Village Taverns.
- Create: New Beginnings and Create: Easy Structures.

If Batch 7 is resumed, every candidate must be rechecked for an exact CurseForge Minecraft 1.21.1 NeoForge file, dependencies, side requirements, licence/terms, compatibility with the existing BYG / Regions Unexplored setup, and fit with the pack's industrial/steampunk direction. The production world and current world-generation configuration must remain unchanged.

## Paused work

- **End expansion:** paused by the maintainer. Historical End candidates are not an active shortlist or test queue.
- **Terralith:** world-generation investigation is paused. The current BYG 2.6.3 / Regions Unexplored 0.6.3 setup and existing worlds must remain unchanged.

## Explicit exclusions

The following content is not wanted and must not be reintroduced unless the maintainer explicitly changes the decision:

- Carry On
- Easy Villagers
- Immersive Paintings
- Bigger Better End Cities
- Create: Sophisticated Exoskeleton 1.0
- Distant Horizons 3.3.3

## Important

A mod being suggested, researched, or present in a disposable test profile does not mean it is compatible, accepted, or approved for public release. Only CurseForge-hosted mods are eligible for consideration. The production world and installed production pack must not be changed as part of candidate testing.
