# Known Issues

This page lists issues the maintainer is aware of. It is not an exhaustive list of every mod warning.

## Under investigation

### Struts dedicated-server client class

The tested dedicated server reports that Struts attempts to load the client-only class `com.mojang.blaze3d.systems.RenderSystem`. The server has still completed startup and accepted a client connection in the maintainer's smoke test. Investigation is ongoing.

### PowerGrid optional native solver

The tested Windows server cannot load the optional `powergridNative7` native library, so PowerGrid's accelerated solver is unavailable. This is being tracked separately from the Struts issue.

## Previously corrected in maintainer smoke tests

- Create Kinetic client mixin was moved to the client-only mixin list; the dedicated-server invalid-dist error is no longer present in the latest maintainer test log.
- Sable / Copycats Catwalk physics selector was corrected with a separate datapack; the unknown Catwalk block error is no longer present in the latest maintainer test log.
- Several optional recipe and loot-table references have targeted datapack corrections.

## Reporting a new issue

Please check the [issue tracker](https://github.com/alexth110987/Create-IronWoven-Beta/issues) before opening a new report. Include the exact error, what you were doing, and steps to reproduce it.
