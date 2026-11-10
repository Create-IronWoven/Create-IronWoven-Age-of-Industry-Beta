# Mod Plans

This page gives players a short overview of planned, considered, paused, and excluded content. It is not the installed-mod list or a release approval list.

- [Mods in the current test snapshot](MODS.md)
- [What still needs testing](TESTING_CHECKLIST.md)
- [Current project status](BETA_STATUS.md)

**Target:** Minecraft 1.21.1 · NeoForge 21.1.265  
**Mod source policy:** CurseForge only

## Project version policy — no backports

**Ironwoven is developed for its selected Minecraft version only. No backports to older Minecraft versions are made or planned.**

- Do not create or maintain older-Minecraft branches, legacy pack editions, or backported releases.
- Do not downgrade the modpack or choose obsolete mod files solely to support an older Minecraft version.
- Evaluate candidate mods, dependencies, compatibility, testing, and releases against the currently declared Minecraft / NeoForge target.
- If a mod or dependency has no suitable file for that target, mark it unavailable or reject it. Do not change the pack's target to accommodate it.
- A future target-version change must be an explicit forward migration decision, with its own compatibility and testing plan; it is not a backport.

This policy applies to mod research, dependency selection, issue triage, contributions, documentation, and release planning.

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
| Create Aeronautics Structures | **ON HOLD.** The tested 1.1.0-Beta-3.1 candidate has two unresolved loot defects: the uniform armour table fails on Minecraft 1.21.1, and one crashed-airship chest has no loot-table assignment. The 16-colour test override is not approved for release. No further tests or packaging while held; resume only after a new official CurseForge 1.21.1 NeoForge file is reviewed and both issues are verified fixed, or an explicit documented exception is approved. |
| Performance and rendering | Partial. No measured server performance baseline yet; client rendering candidates require separate client tests. |
| Botany Pots and Construction Sticks | Loaded in a test group; feature validation remains open. |
| Lootr | Partial compatibility observations; independent per-player loot still needs verification. |
| Every Compat (Wood Good) | Accepted baseline is 2.11.57 + Moonlight Lib 3.8.2 after the paired Windows disposable startup/world/login/shutdown smoke test. The Golden Cherry Leaves duplicate remains open. Feature-level block/recipe/model/texture/drop checks are delegated to beta testers. The original Create World client profile and normal MinecraftServer-Test dedicated-server baseline both contain the accepted JARs; startup/login verification on this updated baseline remains. |
| Create Aeronautics: Gadgets & Gizmos 2.0.0-Pre-Release-4 | **ON HOLD.** Keep bundled 1.2.10 (file 9141062) unchanged. Do not install or test Pre-Release-4 (file 9260191). Reconsider only after a stable 2.x release for 1.21.1 NeoForge passes exact bundled-content, dependency, side, version-range and upstream-issue review, followed by separate maintainer approval. |
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


## Extended candidate review — 7 November 2026

A large new candidate list has received an initial CurseForge / Minecraft 1.21.1 / NeoForge 21.1.265 compatibility triage. **No candidate from this list has been selected, installed, or approved for release.** Detailed internal dependency and file evidence remains in the private development repository.

### Best thematic matches identified for further review

- Create Propulsion: Simulated
- Create: Aeroworks
- Create: Aquatic Ambitions

These have surfaced 1.21.1 NeoForge files and match the Create / Aeronautics direction. Exact dependency ranges, current file eligibility and feature compatibility still need to be reconciled before any test decision.

### Separate optional utility and quest-system ideas

FTB Essentials, FTB Ultimine, Fuel Goes Here, Polymorph, and selected inventory / interface utilities have target-version files surfaced. They remain candidates only; gameplay changes and server/client roles must be considered individually.

The linked FTB Quests projects form a **new optional questing subsystem**, not independent standalone additions. FTB Quests itself would need to be considered first; dependent addons and resource packs should not be selected as a bundle. Accessories would require a separate migration decision from the current Curios-based equipment system.

### Existing work and holds remain unchanged

- FastSuite remains in its existing Batch F order.
- Waystones and Waystones: Sable remain subject to the Batch H travel-system decision.
- Structurize remains associated with paused Batch 7 settlement / MineColonies research.
- Existing Farmer's Delight, ModernFix, Resourceful Lib and Struts entries are not new additions.
- Some submitted projects still have no confirmed 1.21.1 NeoForge file or need missing libraries / exact dependency verification.

No installed mods, CurseForge manifest, server configuration, production world or world-generation settings were changed by this review.

### Extended Bogeys

The named Extended Bogeys entry was checked against its official CurseForge project. The available **Create: Extended Bogeys (Borked)** project is deprecated and has files only for Minecraft 1.20.1 on Forge/Fabric; there is no Minecraft 1.21.1 NeoForge file. The project page itself points users to Create: Blocks & Bogies as the replacement. **Do not add the deprecated project.** Create: Blocks & Bogies 1.0.8 is already recorded in Ironwoven and has a passed bogie UI multiplayer test.
