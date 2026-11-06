# Known Issues

This page lists current, unresolved issues. Completed fixes are documented in the testing checklist and compatibility records.

## Test setup note

IronWoven compatibility datapacks are world-scoped. The 6 November 15:12 disposable-world log repeated several targeted errors because that newly created world's datapacks folder was empty. A corrected 15:54 retest enabled all four IronWoven datapacks; the targeted Design n' Decor, Steam 'n' Rails, Create Kinetic, Sable Catwalk, and Create Deco placard log errors were absent. When creating a new test world, confirm the required IronWoven datapacks are present and enabled before reviewing compatibility errors.

## Under investigation

### Struts dedicated-server mixin / visual verification

A local Struts 1.3.1 mixin-side workaround was applied and script-verified on matching disposable server and CurseForge client JARs. Fresh server and client logs from 6 November contain no `RenderSystem` or `StrutRenderSystemAccessor` messages; the server reached `Done`, accepted the matching client, and shut down with all dimensions saved. The dedicated-server mixin error therefore passes log-level retest. The client log still warns that `struts:blockstates/girder_strut_structure.json` has no model for either `waterlogged=false` or `waterlogged=true`. Visual confirmation of the affected Struts block is still required before this item can be closed.

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
