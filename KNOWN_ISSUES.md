# Known Issues

This page lists current, unresolved issues. Completed fixes are documented in the testing checklist and compatibility records.

## Test setup note

IronWoven compatibility datapacks are world-scoped. The 6 November 15:12 disposable-world log repeated several targeted errors because that newly created world's datapacks folder was empty. A corrected 15:54 retest enabled all four IronWoven datapacks; the targeted Design n' Decor, Steam 'n' Rails, Create Kinetic, Sable Catwalk, and Create Deco placard log errors were absent. When creating a new test world, confirm the required IronWoven datapacks are present and enabled before reviewing compatibility errors.

## Under investigation

### Struts dedicated-server client class

A local Struts 1.3.1 mixin-side workaround was applied and script-verified on matching disposable server and CurseForge client JARs; original backups were preserved. The 6 November 16:40–16:47 server/client/debug logs contain no `RenderSystem` or `StrutRenderSystemAccessor` messages. The server reached `Done`, accepted the matching client, and saved all dimensions on shutdown. Screenshots from 16:46 show the tested Struts beams/girders rendering visibly. Two client warnings remain for the `waterlogged=false` and `waterlogged=true` variants in `struts:blockstates/girder_strut_structure.json`, but the shown parts render. The local patched test profile passes; this issue stays open for standard modpack installs because the official CurseForge Struts JAR and modpack manifest have not been changed. A release-safe fix or upstream release is still required.

### PowerGrid optional native solver

The tested Windows server and matching CurseForge client both could not load the optional `powergridNative7` native library from PowerGrid 0.6.2; the mod continues with the Java fallback. This matches upstream [PowerGrid issue #1165](https://github.com/patryk3211/PowerGrid/issues/1165): the official 0.6.2 NeoForge JAR accidentally omitted the Windows and Linux native binaries shipped in 0.6.1, and the maintainer confirms the binaries did not change. A reversible test is prepared to copy only the 0.6.1 Windows DLL into the disposable server/client `.pg-native` folders while keeping 0.6.2 installed. Not yet applied or verified; Linux will need the `.so` in a later Linux test.

### Every Compat duplicate block registration

Every Compat reports a duplicate registration for `everycomp:ch/herbsandharvest/golden_cherry_fruit_leaves`. Other compatibility blocks register, but this duplicate remains unresolved.

### Create Aeronautics Structures loot table

The `cr_aero_structures:chests/uniform` loot table fails to parse its `minecraft:dyed_color` provider. Exact file provenance and structure generation also remain under review.

### Shulker Box Tooltip / Supplementaries integration

The default client setting reproduced the client-only Shulker Box Tooltip `PreviewRenderer` invalid-dist error when Supplementaries providers were registered on the dedicated server. This matches the open upstream [ShulkerBoxTooltip issue #263](https://github.com/MisterPeModder/ShulkerBoxTooltip/issues/263). A reversible client-only workaround (`preview.serverIntegration=false`) passed log-level and visual tests on 6 November 2026: fresh server logs contain no `PreviewRenderer` or failed Supplementaries provider registration, and the matching client registers all 3 Supplementaries providers and all 31 Shulker Box Tooltip providers locally. Screenshots confirm the Sack's nine-stack preview and Lunch Basket's food-content/state preview render correctly. With this setting disabled, server-supplied extras such as Ender Chest synchronization are unavailable. This is a local config workaround, not an upstream fix; keep the issue open until the release trade-off is assessed or a server-safe upstream fix is available.

## Reporting a new issue

Please check the [issue tracker](../../issues) before opening a new report. Include the exact error, what you were doing, and steps to reproduce it.
