# Known Issues

This page lists current, unresolved issues. Completed fixes are documented in the testing checklist and compatibility records.

## Test setup note

IronWoven compatibility datapacks are world-scoped. The 6 November 15:12 disposable-world log repeated several targeted errors because that newly created world's datapacks folder was empty. A corrected 15:54 retest enabled all four IronWoven datapacks; the targeted Design n' Decor, Steam 'n' Rails, Create Kinetic, Sable Catwalk, and Create Deco placard log errors were absent. When creating a new test world, confirm the required IronWoven datapacks are present and enabled before reviewing compatibility errors.

## Under investigation

### Struts dedicated-server client class

The tested dedicated server attempts to load the client-only class `com.mojang.blaze3d.systems.RenderSystem` through Struts' `StrutRenderSystemAccessor`. A local mixin-side workaround has now been applied and script-verified on matching disposable server and CurseForge client JARs; original backups were preserved. Fresh runtime logs and client-side rendering verification are still pending, so this issue remains open.

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
