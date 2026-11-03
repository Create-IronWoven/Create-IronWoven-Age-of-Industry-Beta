# Known Issues

This page lists issues the maintainer is aware of. It is not an exhaustive list of every mod warning. Results below refer to the latest available internal smoke-test log, latest(9).log from 3 November 2026, 22:57–22:58.

## Under investigation

### Struts dedicated-server client class

The tested dedicated server reports that Struts attempts to load the client-only class `com.mojang.blaze3d.systems.RenderSystem`. The server still completed startup and accepted a client connection in the maintainer's smoke test.

An exact upstream report already exists: [Struts issue #6](https://github.com/cakeGit/StrutYourStuff/issues/6). A candidate correction to move the RenderSystem accessor into the client-only mixin list has been prepared, but it has **not yet been tested**.

### PowerGrid optional native solver

The tested Windows server cannot load the optional `powergridNative7` native library, so PowerGrid's accelerated solver is unavailable. The mod falls back to its non-accelerated solver. The exact cause for the current 0.6.2 build has not yet been established; an older closed issue about a Linux GLIBC requirement is not assumed to be the same problem.

### Remaining nonfatal warnings

The latest available log also contains nonfatal warnings involving Create Liquid Fuel's data-map type, the `c:foods/pork` tag, and Regions Unexplored ocelot mob categories. The responsible source component has not yet been confirmed for each warning, so they are not being attributed to a developer prematurely.

## Previously corrected in maintainer smoke tests

- Create Kinetic client mixin was moved to the client-only mixin list; the dedicated-server invalid-dist error is no longer present in the latest maintainer test log.
- Create Kinetic's five missing-item loot-table parse errors are no longer present after the temporary compatibility datapack was loaded.
- Steam 'n' Rails optional track loot-table errors are no longer present after the temporary compatibility datapack was loaded.
- Sable / Copycats Catwalk physics selector was corrected with a separate datapack; the unknown Catwalk block error is no longer present.
- The Create Deco placard recipe parse error is no longer present after the recipe override.
- Optional Herbs & Harvest Botany Pots recipes and Design n' Decor Dye Depot loot tables are suppressed by temporary pack overrides. These suppressions are not upstream fixes and must be revisited if the optional dependencies are added.

## Upstream report status

The internal technical handover is being prepared for the correct mod maintainers. **No external developer report or patch has been submitted yet.** Existing upstream reports are linked in [Compatibility Progress](COMPATIBILITY_PROGRESS.md).

## Reporting a new issue

Please check the [issue tracker](https://github.com/alexth110987/Create-IronWoven-Beta/issues) before opening a new report. Include the exact error, what you were doing, and steps to reproduce it. Please remove personal paths, IPs, account details, and other private information from logs before sharing them.
