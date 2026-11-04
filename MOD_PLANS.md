# Mods Planned, On Hold, and Excluded

This page separates confirmed installed mods from ideas for future versions. **A mod listed as planned or on hold is not part of the current pack unless it also appears on [Mods in the Pack](MODS.md).**

## Requested candidates — compatibility review 3 November 2026

Target platform: Minecraft 1.21.1, NeoForge 21.1.265, Java 21.

These are requested candidates only. **None of the new candidates below have been installed or approved.** Bookshelf appeared twice in the submitted list and is recorded once.

| Mod | Review status | Notes |
|---|---|---|
| Botany Pots | Candidate — compatible with required libraries | 1.21.1 NeoForge file found. Requires Bookshelf and Prickle. Existing datapack skips 47 optional Herbs & Harvest Botany Pots recipes; revisit those before enabling the mod. |
| Create Deco 2.1.3 | Already in current test inventory | No addition needed; current server inventory already records 2.1.3. |
| Construction Sticks | Candidate — compatible | 1.21.1 NeoForge file 1.5.0 found. Test placement with modded blocks. |
| Lootr | Candidate — compatible | 1.21.1 NeoForge file 1.11.38.127 found. Test on a copied world because it changes loot-container behaviour. |
| YUNG's Better End Island | Candidate — dependencies required | 1.21.1 NeoForge file 3.1.2; requires YUNG's API. Overlaps the central End island with BetterEnd: New Dawn; test separately. |
| BetterEnd: New Dawn | Candidate — dependencies and End test required | 1.21.1 NeoForge file 21.0.36; requires BCLib: New Dawn, WunderLib: New Dawn, and WorldWeaver: New Dawn. Adds its own End generator and central-island content. Test separately from YUNG's Better End Island and check the existing BYG / Regions Unexplored setup. |
| Bigger Better End Cities | Not compatible as currently published | Reviewed 1.21.x project build is Fabric, not NeoForge. Do not add unless a NeoForge 1.21.1 port is verified. |
| Ender Villages | On hold — exact file not confirmed | Adds End structures and villagers. A matching 1.21.1 NeoForge file was not confirmed in the reviewed release listings. |
| Bookshelf | Conditional dependency | Required by Botany Pots on 1.21.1. Add only with the compatible Botany Pots dependency version. |
| Prickle | Conditional dependency | Required by Botany Pots on 1.21.1. Add only with the compatible Botany Pots dependency version. |

### Important test safeguards

- No installation or world changes were made as part of this review.
- Keep the production world and its current BYG 2.6.3 / Regions Unexplored 0.6.3 setup unchanged.
- Test End world-generation candidates in disposable world copies. BetterEnd: New Dawn and YUNG's Better End Island both change the central End island; combined compatibility has not been established.
- If Botany Pots is added later, revisit the 47 intentionally skipped Herbs & Harvest Botany Pots recipes in the IronWoven recipe-fix datapack.
- Batch 7 has not started. These candidates are under review and are not approved additions.

## Confirmed current client-only additions

These are recorded as installed in the client profile, not as dedicated-server mods:

| Mod | Version recorded | Status |
|---|---|---|
| Sodium | 0.8.13 | Client only |
| Iris | 1.8.14-beta.1 | Client only |
| Sodium Extra | 0.9.5 NeoForge | Client only |

## On hold / under investigation

| Mod | Status | Notes |
|---|---|---|
| Terralith | On hold — not installed | A possible world-generation option. Compatibility investigation was paused. The current BYG 2.6.3 and Regions Unexplored 0.6.3 setup and existing worlds must remain unchanged while this is on hold. |

## Explicitly excluded from the current plan

These mods remain specifically recorded as not wanted for this project:

- Carry On
- Easy Villagers
- Immersive Paintings

## How players can suggest a mod

Use the [feature suggestion form](https://github.com/alexth110987/Create-IronWoven-Beta/issues/new?template=feature_suggestion.yml). Please include the exact mod name, its official project page, supported Minecraft / NeoForge versions, and why it fits Create IronWoven.

Suggestions are reviewed, not automatically accepted. The pack's existing compatibility and world-preservation decisions take priority over adding more mods.


## Requested colony ecosystem candidates — 4 November 2026

Target platform: Minecraft 1.21.1, NeoForge 21.1.265, Java 21.

These are requested candidates and content ideas for compatibility research only. **None have been installed or approved.** Exact 1.21.1 NeoForge files, versions, dependencies, and compatibility with the current pack still need verification.

| Candidate | Review status | Notes |
|---|---|---|
| CreateColonies | Candidate — review pending | Verify exact project, 1.21.1 NeoForge file, MineColonies dependency, and Create 6.0.10 compatibility. |
| MineColonies | Candidate — review pending | Proposed main colony system. Verify current NeoForge release and complete dependency chain. |
| Create: MineColonies Link | Candidate — review pending | Verify exact project and compatibility with the selected MineColonies and Create versions. |
| Structurize | Supporting dependency candidate | Match the version required by the selected MineColonies release. |
| Domum Ornamentum | Supporting dependency candidate | Match the version required by the selected MineColonies release. |
| BlockUI | Supporting dependency candidate | Match the version required by the selected MineColonies release. |
| Multi-Piston | Supporting dependency candidate | Verify whether required by the selected MineColonies release and match its declared version. |
| TownTalk | Optional integration candidate | Verify exact project, loader support, and distinct functionality. |
| Dynamic Trees | Optional world/ecology candidate | Verify NeoForge 1.21.1 support and compatibility with existing BYG / Regions Unexplored world generation. |
| Additional colony building styles and schematics | Content research item — not necessarily a mod | Check format, dependencies, MineColonies/Structurize compatibility, and permissions. |

### Colony ecosystem test safeguards

- Select the exact MineColonies release first and use its declared dependency versions.
- Verify whether CreateColonies and Create: MineColonies Link are separate compatible integrations before considering both.
- Keep Dynamic Trees optional; do not change the current BYG 2.6.3 / Regions Unexplored 0.6.3 setup.
- Test the complete selected stack on a disposable dedicated server and copied world.
- No main-world changes or installations are authorized by this candidate list.
- Batch 7 has not started. All entries remain under review, not approved additions.
