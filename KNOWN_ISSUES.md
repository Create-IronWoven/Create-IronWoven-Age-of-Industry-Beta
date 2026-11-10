# Known Issues

This page lists current, unresolved issues. Completed fixes are documented in the testing checklist and compatibility records.

## Test setup note

IronWoven compatibility datapacks are world-scoped. The 6 November 15:12 disposable-world log repeated several targeted errors because that newly created world's datapacks folder was empty. A corrected 15:54 retest enabled all four IronWoven datapacks; the targeted Design n' Decor, Steam 'n' Rails, Create Kinetic, Sable Catwalk, and Create Deco placard log errors were absent. When creating a new test world, confirm the required IronWoven datapacks are present and enabled before reviewing compatibility errors.

The separate clean Windows server baseline created on 7 November reached `Done` and generated `IronWoven Age Of Industry_v0.1.0`. The root-aware fresh-server installer successfully deployed the four maintained IronWoven packs; the 02:45 console screenshot lists all four as enabled among 12 datapacks. The later 02:44–02:58 server log confirms matching-client login, operator grant, Creative-mode command, and clean shutdown with all dimensions saved. The five targeted Design n' Decor, Steam 'n' Rails, Create Kinetic, Create Deco placard and Sable Catwalk errors are absent. The same log contains separate ERROR records for PowerGrid native loading, Every Compat duplicate registration, Aeronautics Structures uniform loot parsing, and SBT/Supplementaries server preview-provider loading. It also contains three unassigned entity-attachment warnings using `apotheosis:tier_augments_applied`. The fresh `mods/` folder screenshot contains no Apotheosis-named JAR, and the maintainer confirms Apotheosis is not installed or planned. Their source and impact are unknown, so keep these three warnings as monitor-only observations rather than an identified mod issue; do not install Apotheosis. Five DUMMY block-entity warnings near a generated structure area also need targeted inspection.

## Under investigation

### Struts dedicated-server client class

A local Struts 1.3.1 mixin-side workaround was applied and script-verified on matching disposable server and CurseForge client JARs; original backups were preserved. The 6 November 16:40–16:47 server/client/debug logs contain no `RenderSystem` or `StrutRenderSystemAccessor` messages. The server reached `Done`, accepted the matching client, and saved all dimensions on shutdown. Screenshots from 16:46 show the tested Struts beams/girders rendering visibly. Two client warnings remain for the `waterlogged=false` and `waterlogged=true` variants in `struts:blockstates/girder_strut_structure.json`, but the shown parts render. The local patched test profile passes; this issue stays open for standard modpack installs because the official CurseForge Struts JAR and modpack manifest have not been changed. A release-safe fix or upstream release is still required.

### PowerGrid optional native solver

The tested PowerGrid 0.6.2 package omitted its optional Windows and Linux native solver binaries, matching upstream [PowerGrid issue #1165](https://github.com/patryk3211/PowerGrid/issues/1165). A local test copied the official 0.6.1 Windows DLL into the disposable server and matching CurseForge `.pg-native` folders without changing the 0.6.2 JAR. On 6 November 2026, both the 18:29 dedicated-server log and 18:34 CurseForge client log reported `Native backend loaded successfully`; the server reached `Done (1.837s)`, and the client connected to the test server and entered the world. **Both internal Windows native-load checks passed, and the client entered the test world.** Electrical-network/component behavior is reserved for beta testers; it is not an outstanding internal fix-pass task. Linux is a separate future platform test and will require the `.so`. The local DLL copies used for this verification are not part of the distributable beta package; the release packaging path for the missing 0.6.2 native resources still needs to be decided.

### Every Compat duplicate block registration

Every Compat reports a duplicate registration for `everycomp:ch/herbsandharvest/golden_cherry_fruit_leaves`. The same duplicate appeared on both client and server during the 6 November 2026 disposable smoke test with the accepted Every Compat 2.11.57 + Moonlight Lib 3.8.2 pair. Other compatibility blocks register, but this duplicate remains unresolved; the update does not fix it.

### Shulker Box Tooltip / Supplementaries integration

The default client setting reproduced the client-only Shulker Box Tooltip `PreviewRenderer` invalid-dist error when Supplementaries providers were registered on the dedicated server. This matches the open upstream [ShulkerBoxTooltip issue #263](https://github.com/MisterPeModder/ShulkerBoxTooltip/issues/263). A reversible client-only workaround (`preview.serverIntegration=false`) passed log-level and visual tests on 6 November 2026: fresh server logs contain no `PreviewRenderer` or failed Supplementaries provider registration, and the matching client registers all 3 Supplementaries providers and all 31 Shulker Box Tooltip providers locally. Screenshots confirm the Sack's nine-stack preview and Lunch Basket's food-content/state preview render correctly. With this setting disabled, server-supplied extras such as Ender Chest synchronization are unavailable. This is a local config workaround, not an upstream fix; keep the issue open until the release trade-off is assessed or a server-safe upstream fix is available.

### Create Aeronautics Structures loot table

**Candidate status: ON HOLD — not eligible for the next beta; no further testing, updating, or packaging is active.** The tested `1.1.0-Beta-3.1` file has two unresolved defects: the official uniform armour loot table does not parse on Minecraft 1.21.1, and one crashed-airship chest had no assigned loot table. A private 16-colour datapack workaround passed a disposable test but changes the original full-range random colour behavior and is not approved for distribution. The specific chest diagnosis is complete; no repair or upstream resolution is recorded. All 11 valid Overworld structure IDs have locate/visual-presence evidence, and broader structure/container loot checks are not being continued while the candidate is held. The original JAR remains unchanged. Reconsider only after a new official CurseForge Minecraft 1.21.1 NeoForge file is reviewed and both issues are verified fixed, or the maintainer explicitly approves a documented exception. The hold is reversible, not a permanent rejection or exclusion.

## Reporting a new issue

Please check the [issue tracker](../../issues) before opening a new report. Include the exact error, what you were doing, and steps to reproduce it.
