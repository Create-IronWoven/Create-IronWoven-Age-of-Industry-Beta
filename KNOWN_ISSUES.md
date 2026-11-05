# Known Issues

This page lists current, unresolved issues. Completed fixes are documented in the testing checklist and compatibility records.

## Under investigation

### World-scoped compatibility datapacks

Some compatibility fixes require IronWoven datapacks to be loaded by each test world. Errors returned in a fresh disposable world where those datapacks were not present. Confirm the relevant datapacks are loaded before treating the errors as a mod failure or a failed fix.

### Struts dedicated-server client class

The tested dedicated server reports that Struts attempts to load the client-only class `com.mojang.blaze3d.systems.RenderSystem`. Server startup and client login still completed in maintainer smoke tests. Investigation is ongoing.

### PowerGrid optional native solver

The tested Windows server could not load the optional `powergridNative7` native library, so PowerGrid's accelerated solver is unavailable.

## Reporting a new issue

Please check the [issue tracker](../../issues) before opening a new report. Include the exact error, what you were doing, and steps to reproduce it.
