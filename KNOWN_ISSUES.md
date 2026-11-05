# Known Issues

This page lists issues the maintainer is aware of. It is not an exhaustive list of every mod warning.

## Under investigation

### Curios Back-slot count for an existing player

The maintainer reports that a newly created test world displays two Back slots from the internal configuration. An existing player's inventory still showed three after the config-only restart, so this issue is limited to that saved player allocation. Curios may retain slots already assigned to a player, so the cause is not yet confirmed. More Curios Slots 1.4 was intentionally removed; its absence is expected.

Before retesting, move any item out of the third Back slot, then have an operator run `/curios set back <player> 2`. Reopen the inventory and confirm the result. The Backpack, Create Backtank, Aviator Goggles, and Aeronautics slot behavior still need testing.

### Fresh-world compatibility data

Some compatibility fixes depend on world-scoped datapacks. In the disposable `world_lootr_test`, earlier test logs recorded recurring optional loot-table errors and Sable / Copycats Catwalk selector errors; the 5 November log also recorded a Create Deco placard recipe parse error. Confirm the IronWoven compatibility datapacks are loaded in a disposable world before attributing these errors to a mod or treating the fixes as failed.

### Struts dedicated-server client class

The tested dedicated server reports that Struts attempts to load the client-only class `com.mojang.blaze3d.systems.RenderSystem`. The server has still completed startup and accepted a client connection in maintainer smoke tests. Investigation is ongoing.

### PowerGrid optional native solver

The tested Windows server cannot load the optional `powergridNative7` native library, so PowerGrid's accelerated solver is unavailable. This is being tracked separately from the Struts issue.

## Previously corrected in maintainer smoke tests

- Create Kinetic's client mixin was moved to the client-only mixin list; its dedicated-server invalid-dist error is absent from the reviewed logs.
- The Sable / Copycats Catwalk selector fix passed when the compatibility datapack was loaded. Catwalk errors returned in a fresh-world test; verify the datapack is enabled in that world.
- Targeted datapack corrections exist for several optional recipe and loot-table references. Check the relevant datapacks in each test world.

## Reporting a new issue

Please check the [issue tracker](../../issues) before opening a new report. Include the exact error, what you were doing, and steps to reproduce it.
