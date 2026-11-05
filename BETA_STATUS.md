# Create IronWoven — Beta Status

**Last updated:** 5 November 2026  
**Minecraft:** 1.21.1 · **NeoForge:** 21.1.265 · **Java:** 21

## Current stage
**Internal testing and public feedback.** No downloadable beta package or release date has been announced.

- [Installed/test inventory](MODS.md)
- [Mod plans and exclusions](MOD_PLANS.md)
- [Open tests](TESTING_CHECKLIST.md)
- [Known issues](KNOWN_ISSUES.md)
- [Support and privacy guidance](SUPPORT.md)

## Current testing highlights
- **Curios:** the maintainer reports that a newly created test world displays two Back slots with the internal config. Backpack + standard Create Backtank work together in the Back slots, and Aviator Goggles and Linked Typewriter work in their assigned slots. More Curios Slots 1.4 was intentionally removed; craftable slot upgrades are not planned. Raw config files will be included with the first beta package.
- **Compatibility datapacks:** targeted fixes passed smoke tests when loaded. Some errors reappeared in a fresh test world without the world-scoped datapacks; verify those datapacks before attributing errors to a mod.
- **Batch A — information and tooltip mods:** the maintainer reports the batch tested. The 5 November dedicated-server log confirms JER, Shulker Box Tooltip, and Enchantment Descriptions loaded together, a client joined, and shutdown saved all dimensions. Client-facing JEI/tooltip feature results are not detailed by that server log; these additions remain separate from production/release approval.
- **Botany Pots and Construction Sticks:** startup passed; feature checks remain open.
- **Lootr:** chest opening and loot presence were confirmed by the maintainer; independent per-player loot remains unverified.
- **Dedicated server:** Struts attempts to load a client-only class; PowerGrid's optional native solver did not load in the tested Windows environment.
- **End content:** research/testing is paused. The test-profile cleanup was visually checked. Do not resume until the maintainer reopens this workstream.

## Project direction
Create IronWoven focuses on Create, Create Aeronautics, trains, automation, engineering, transport, and exploration. Create Aeronautics Structures is planned for the Overworld but is not installed or approved.

## Release readiness
The pack is not release-ready. Client/server manifests, clean-install validation, feature checks, privacy review, and the release checklist remain outstanding.
