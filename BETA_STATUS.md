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
- **Batch C — Create Big Cannons + Ritchie's Projectile Library:** the 5 November routine server startup/world-load/client-login smoke test passed with Create Big Cannons 5.11.7 and Ritchie's Projectile Library 2.1.2 present. The server shut down cleanly and saved all dimensions. The log contains existing pack-level errors and warnings; no candidate-specific runtime error was identified. Cannon features were not separately tested, and neither mod is approved for production/release.
- **Curios:** the maintainer reports that a newly created test world displays two Back slots with the internal config. Backpack + standard Create Backtank work together in the Back slots, and Aviator Goggles and Linked Typewriter work in their assigned slots. More Curios Slots 1.4 was intentionally removed; craftable slot upgrades are not planned. Raw config files will be included with the first beta package.
- **Compatibility datapacks:** targeted fixes passed smoke tests when loaded. Some errors reappeared in a fresh test world without the world-scoped datapacks; verify those datapacks before attributing errors to a mod.
- **Batch A — information and tooltip mods:** the standard server startup/world-load/client-login smoke test passed. JER, Shulker Box Tooltip, and Enchantment Descriptions were present together; Shulker Box Tooltip registered 31 providers. No feature-by-feature playtest is claimed or required by default. These additions are not production/release approved.
- **Batch B — exploration locators:** the standard server startup/world-load/client-login smoke test passed with Nature's Compass 3.4.0 and Explorer's Compass 3.4.0 present. The server reached `Done`, the client joined, and shutdown saved all dimensions. A Nature's Compass INFO search message is recorded without a feature verdict. These additions are not production/release approved.
- **Botany Pots and Construction Sticks:** startup passed; feature checks remain open.
- **Lootr:** chest opening and loot presence were confirmed by the maintainer; independent per-player loot remains unverified.
- **Dedicated server:** Struts attempts to load a client-only class; PowerGrid's optional native solver did not load in the tested Windows environment.
- **End content:** research/testing is paused. The test-profile cleanup was visually checked. Do not resume until the maintainer reopens this workstream.

## Latest disposable server smoke test — Batch C, 5 November 2026
The server reached `Done (1.589s)!`, loaded the disposable test world, accepted one client login, and shut down cleanly with all dimensions saved. Create Big Cannons 5.11.7 and Ritchie's Projectile Library 2.1.2 were present. The log still contains existing pack-level errors and warnings; no candidate-specific runtime error was identified. This is a routine smoke-test pass only, not cannon feature validation or production/release approval.
## Project direction
Create IronWoven focuses on Create, Create Aeronautics, trains, automation, engineering, transport, and exploration. Create Aeronautics Structures is planned for the Overworld but is not installed or approved.

## Release readiness
The pack is not release-ready. Client/server manifests, clean-install validation, feature checks, privacy review, and the release checklist remain outstanding.
