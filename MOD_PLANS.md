# Mod Plans

This page summarizes optional content decisions, current holds, and candidate ideas. It is not the installed-mod list or a release approval list.

- [Current mod inventory status](MODS.md)
- [Beta status](BETA_STATUS.md)
- [Beta-tester feature checklist](TESTING_CHECKLIST.md)

**Target:** Minecraft 1.21.1 · NeoForge 21.1.265  
**Mod source policy:** CurseForge only

## Current work status

The previous numbered installation-batch sequence has been retired by the maintainer. There is no active numbered batch queue. Historical batch labels in older evidence are not outstanding tasks. New candidate work requires a specific current reason and maintainer authorization.

| Area | Current disposition |
|---|---|
| FastSuite 6.0.7 / Placebo 9.9.4 / FastFurnace 9.0.1 | FastSuite and Placebo are accepted into the active mod set after exact-file/dependency preflight, matching client/server hashes, and authorised 11 November combined-profile smoke PASS. No isolated optimizer test is required. FastFurnace loaded in the same session but its exact CurseForge file/dependency/side preflight remains open; it is not yet accepted. Feature/recipe/JEI/performance actions belong to beta testers. |
| Sophisticated Backpacks / Core coordinated update | Backpacks 3.26.21.2249 (file 9524812) + Core 1.5.32.2464 (file 9524669) passed authorised shared smoke; client/server SHA-256 parity confirmed. Accepted into active mod set. Backpacks feature actions remain Pending for beta testers; Core is tested through Backpacks. |
| Create: The Factory Must Grow Community Edition 1.3.3a | Accepted into the active mod set after authorised shared smoke PASS and exact client/server SHA-256 parity. Feature/visual actions remain Pending; Custom License distribution review remains a separate release gate. |
| Every Compat 2.11.57 / Moonlight Lib 3.8.2 | Accepted baseline pair; fresh server smoke passed. Golden Cherry Leaves duplicate registration remains an open issue; feature actions belong to beta testers. |
| Create Aeronautics Structures 1.1.0-Beta-3.1 | **ON HOLD.** Do not test, update, or package until the official defects are resolved in a reviewed file or an explicit documented exception is approved. |
| Create Aeronautics: Gadgets & Gizmos 2.0.0-Pre-Release-4 | **ON HOLD.** Keep bundled 1.2.10 unchanged; reconsider only after a stable 2.x file and exact dependency review, followed by explicit approval. |
| Lithium 0.15.4 | **ON HOLD / deferred.** Do not install or test the current file. |
| Linux dedicated server | Not tested; do not claim support or verification. |

## Status meanings

| Status | Meaning |
|---|---|
| In testing | Present in a working profile; feature checks may remain open. |
| Candidate | Considered only; not selected, installed, or approved. |
| Partial | Some evidence exists, but a stated issue or check remains open. |
| On hold | Work is paused; do not install, update, or test until the hold is explicitly lifted. |
| Excluded | The maintainer has decided the content is not wanted. |
| Accepted mod-set version | The exact maintainer-authorised version passed its required smoke test; feature checks and release approval remain separate. |

## Optional candidate ideas — not approved additions

The 7 November candidate review identified possible additions, but none was selected, installed, or approved by that report. Recheck exact current CurseForge files, dependencies, sides, licence/terms, and pack fit before any future decision.

- **Create / Aeronautics content:** Create Propulsion: Simulated, Create: Aeroworks, Create: Aquatic Ambitions.
- **Server utilities:** FTB Essentials and Crash Utilities.
- **Gameplay and recipe options:** FTB Ultimine, Fuel Goes Here, Polymorph, Torchmaster, and FastWorkbench.
- **Small client or convenience options:** Exposure, Fireproof Boats, Just Zoom, and Toast Control.
- **Questing:** FTB Quests is a separate optional gameplay-system decision. Do not select addons before choosing the base system and checking its complete dependency chain.

These are ideas, not a missing-mod list. No candidate is a required addition based on the available evidence.

## Active-profile observations requiring recheck

- **Railways 0.3.0-beta.2** and **Supplementaries 4.0.2** appear on both 10 November profiles with matching hashes; older accepted records show 0.3.0-alpha.2 and 3.4.0 respectively. Recheck exact CurseForge files/dependencies and obtain an explicit update disposition.
- **Create Aeronautics Curios Compat:** active JAR filename reports 2.3 while embedded metadata reports 2.0; reconcile exact file and loaded metadata.
- **Waystones 21.1.46 / Sable 2.0.6:** both appear in the 10 November profile despite the earlier deferred travel-system decision. Confirm intended disposition and AeroPortals/Balm compatibility before release; do not add duplicates.

## Conditional candidates

- **Connected Glass:** requires Fusion and SuperMartijn642's Core Lib; Config Lib is not a substitute.
- **NetherPortalFix:** requires Balm and may overlap with existing portal/travel behavior.
- **Waystones / Waystones: Sable:** already observed in the 10 November profile (21.1.46 / 2.0.6); the earlier deferred travel-system decision conflicts with this presence. Reconcile intended disposition, AeroPortals overlap, and exact Balm compatibility before release. Do not treat them as missing mods.
- **Sound Physics Remastered:** the surfaced target file was beta; stability and client-audio decision required.
- **Accessories:** would be a migration from the current Curios equipment system, not an additive slot mod.

## Paused ideas

- End expansion and Terralith investigation remain paused.
- Settlement, town, and MineColonies ecosystem ideas remain paused. Do not resume this research without explicit maintainer instruction.

## Existing replacement

- **Create: Blocks & Bogies 1.0.8** is already recorded in the pack and its bogie UI action was reported passed in multiplayer. Do not add deprecated Create: Extended Bogeys (Borked); it has no 1.21.1 NeoForge file and points to Blocks & Bogies.

## Explicit exclusions

Do not reintroduce Carry On, Easy Villagers, Immersive Paintings, Bigger Better End Cities, Create: Sophisticated Exoskeleton 1.0, or Distant Horizons 3.3.3.

## Important

A mod being researched, appearing in a working profile, or passing a smoke test does not make it accepted or release-approved. Only CurseForge-hosted files are eligible for consideration. The production world and installed production pack must not be changed as part of candidate research.
