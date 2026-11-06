# Known Issues

This page lists current, unresolved issues. Completed fixes are documented in the testing checklist and compatibility records.

## Test setup note

IronWoven compatibility datapacks are world-scoped. The 6 November 15:12 disposable-world log repeated several targeted errors because that newly created world's datapacks folder was empty. A corrected 15:54 retest enabled all four IronWoven datapacks; the targeted Design n' Decor, Steam 'n' Rails, Create Kinetic, Sable Catwalk, and Create Deco placard log errors were absent. When creating a new test world, confirm the required IronWoven datapacks are present and enabled before reviewing compatibility errors.

## Under investigation

### Struts dedicated-server mixin / visual verification

A local Struts 1.3.1 mixin-side workaround was applied and script-verified on matching disposable server and CurseForge client JARs; original backups were preserved. The 6 November 16:40–16:47 server/client/debug logs contain no `RenderSystem` or `StrutRenderSystemAccessor` messages. The server reached `Done`, accepted the matching client, and saved all dimensions on shutdown. Screenshots from 16:46 show the tested Struts beams/girders rendering visibly. Two client warnings remain for the `waterlogged=false` and `waterlogged=true` variants in `struts:blockstates/girder_strut_structure.json`, but the shown parts render. The local patched test profile passes; this issue stays open for standard modpack installs because the official CurseForge Struts JAR and modpack manifest have not been changed. A release-safe fix or upstream release is still required.

### PowerGrid optional native solver

The tested Windows server could not load the optional `powergridNative7` native library. PowerGrid's accelerated solver is unavailable; the log does not show that the entire mod failed to start.

### Every Compat duplicate block registration

Every Compat reports a duplicate registration for `everycomp:ch/herbsandharvest/golden_cherry_fruit_leaves`. Other compatibility blocks register, but this duplicate remains unresolved.

### Create Aeronautics Structures loot table

The `cr_aero_structures:chests/uniform` loot table fails to parse its `minecraft:dyed_color` provider. Exact file provenance and structure generation also remain under review.

### Shulker Box Tooltip / Supplementaries integration

During dedicated-server client login, the Supplementaries plugin attempts to load the client-only Shulker Box Tooltip `PreviewRenderer` class and fails to register Supplementaries providers. Shulker Box Tooltip still registers its own 31 providers in the test log; the Supplementaries integration remains unresolved.

## Reporting a new issue

Please check the [issue tracker](../../issues) before opening a new report. Include the exact error, what you were doing, and steps to reproduce it.
