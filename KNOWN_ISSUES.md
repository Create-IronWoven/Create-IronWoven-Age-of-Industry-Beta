# Known Issues

This page lists current, unresolved issues. Completed fixes are documented in the testing checklist and compatibility records.

## Under investigation

### Curios Back-slot count for an existing player

A newly created test world displays the configured two Back slots. One existing player's saved allocation still showed three after the config change. On a disposable server, move any item out of the third slot, run `/curios set back <player> 2` as an operator, and confirm the inventory afterward. Do not use `/curios reset` or edit player data.

### World-scoped compatibility datapacks

Some compatibility fixes require IronWoven datapacks to be loaded by each test world. Errors returned in a fresh disposable world where those datapacks were not present. Confirm the relevant datapacks are loaded before treating the errors as a mod failure or a failed fix.

### Struts dedicated-server client class

The tested dedicated server reports that Struts attempts to load the client-only class `com.mojang.blaze3d.systems.RenderSystem`. Server startup and client login still completed in maintainer smoke tests. Investigation is ongoing.

### PowerGrid optional native solver

The tested Windows server could not load the optional `powergridNative7` native library, so PowerGrid's accelerated solver is unavailable.

## Reporting a new issue

Please check the [issue tracker](../../issues) before opening a new report. Include the exact error, what you were doing, and steps to reproduce it.
