# Changelog

Player-facing highlights for the current development pack. This is not a record of internal commits or a downloadable release archive.

## Current development version — `v0.1.108.5`

**Version format:** `v0.1.<installed CurseForge profile entries>.<accepted distinct bug fixes>`.

- **108 installed mod entries:** the 5 November 2026 CurseForge App profile showed `Mods (110)`. Sodium 0.8.13 and Sodium Extra 0.9.5 were subsequently removed from the selected profile, leaving 108 entries.
- **5 accepted compatibility bug-fix families:** the five distinct defects below are counted once each, even though the fixes affect 455 individual resource entries in total.

| # | Bug-fix family | Included pack fix |
|---:|---|---|
| 1 | Create: Design n' Decor loot-table errors when optional Dye Depot content is absent (256 affected tables) | `IronWoven-Recipe-Fixes` |
| 2 | Create: Steam 'n' Rails optional track loot-table errors when companion-mod items are absent (192 affected tables) | `IronWoven-Railways-Fix` |
| 3 | Create Kinetic missing/stale item references in block loot tables (5 affected tables) | `IronWoven-Create-Kinetic-Fix` |
| 4 | Create Deco placard recipe has an invalid ingredient entry (1 recipe) | `IronWoven-Recipe-Fixes` |
| 5 | Sable / Copycats+ Catwalk physics selector points to a non-registered block (1 selector) | `IronWoven-Sable-Copycats-Fix` |

The four maintained datapacks address these five distinct defects. All five targeted error signatures were absent in the corrected datapack-enabled server log-level retest. This is log-level compatibility evidence, not a claim that every affected in-game feature has completed full functional testing.

## Other accepted mod updates in this profile

- Every Compat (Wood Good) updated from 2.11.56 to 2.11.57 (CurseForge file 9468938).
- Required Moonlight Lib (Selene) dependency updated from 3.8.1 to 3.8.2 (CurseForge file 9458248).

These were updates to existing profile entries, so they do not change the mod-count component or add to the five distinct bug-fix count.

## Not included in `v0.1.108.5`

- Create Aeronautics: Gadgets & Gizmos 2.0.0-Pre-Release-4 (CurseForge file 9260191) remains an update candidate only; the observed installed baseline is 1.2.10. It has not been installed, tested, or accepted.
- Test-only Aeronautics Structures loot-table override, local Struts JAR patch, PowerGrid native DLL workaround, and Shulker Box Tooltip / Supplementaries config workaround are not counted as accepted distributed bug fixes.

**Release status:** internal testing. No downloadable public beta package has been published.

