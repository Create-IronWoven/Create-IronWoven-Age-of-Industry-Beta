# Beta Status — v0.1.112-R002

**Current development version:** `v0.1.112-R002` (not yet a downloadable public beta)  
**Last updated:** 7 November 2026  
**Minecraft:** 1.21.1 · **NeoForge:** 21.1.265 · **Java:** 21

## Current status

The 6 November server-folder screenshot is an inventory observation only. It does not confirm runtime loading, compatibility, feature testing, or release approval. The visible Railways, Supplementaries, and Sophisticated Backpacks Create Integration version differences, plus the unversioned `cr_aero_structures.jar`, remain to be reconciled. The current accepted content version is `v0.1.112-R002`.

The current development version `v0.1.112-R002` uses content-change counter `112` as the retroactive baseline from the 5 November 2026 CurseForge screenshot (`Mods (110)`). Removal counter `R002` records two client-only removals: Sodium 0.8.13 and Sodium Extra 0.9.5. The latest profile screenshot shows `Mods (108)`. The latest dedicated-server folder screenshot on 6 November shows 106 visible JAR files, superseding the earlier 104-file server-folder screenshot. The client inventory remains separate and is not updated by this server-only screenshot. This is not a claim of 110 public releases. No downloadable beta package exists. The accepted updates are Every Compat 2.11.57 (`v0.1.111-R002`) and its required Moonlight Lib 3.8.2 dependency (`v0.1.112-R002`). The latest supplied screenshots confirm both JARs are now present in the original Create World client profile and normal MinecraftServer-Test dedicated-server folder. Folder deployment is complete; startup/login verification on this updated baseline remains pending.

## Fresh dedicated-server installation — v.0.1

The next dedicated server is being prepared as a **brand-new, clean installation** named `IronWoven Age Of Industry v.0.1` (Windows folder name; no trailing period). Target content version: `v0.1.112-R002` on Minecraft 1.21.1 / NeoForge 21.1.265 / Java 21.

**Current state:** the maintainer created the new folder on 7 November 2026; screenshot confirms it is empty (`0 items`). Initial installed mod count: **0 JAR files**. The folder has not yet had NeoForge or mods installed. The final top-level `mods/*.jar` count and NeoForge loaded-mod count will be recorded separately after installation and first startup.

The earlier `MinecraftServer-Test` folder contained 106 visible JAR files. That is a historical count for the old test folder only; it is not the new installation's count or expected target. The clean installation will use the reconciled approved server-required/shared inventory, and it is not a copy of the old test server. No downloadable server package has been published.

Ironwoven: Age of Industry is in **internal compatibility and functional testing**. There is currently no public downloadable beta package and no release date has been announced.

- [Current test-pack inventory](MODS.md)
- [Functional testing progress](TESTING_CHECKLIST.md)
- [Planned mods and project decisions](MOD_PLANS.md)
- [Known player-relevant issues](KNOWN_ISSUES.md)

## Server platform status

Windows is the current development and test environment. Linux is a planned server target, but the maintainer has not yet set up a Linux system. Linux compatibility and runtime behavior are not tested or verified. Linux validation will be added to release preparation once a test system is available.

## Testing progress

**Every Compat 2.11.57 + Moonlight Lib 3.8.2 paired update smoke test — 6 November 2026, 23:40–23:46 CET:** the exact pair loaded on a disposable Windows dedicated server and matching client. The server reached Done, enabled all four IronWoven datapacks, accepted the client, and shut down with all dimensions saved. The duplicate Golden Cherry Leaves registration remains in both client and server logs. This is a routine startup/world-load/client-login/clean-shutdown smoke-test pass only; no block, recipe, JEI, model, texture, drop or gameplay feature was tested by the maintainer. Those feature checks remain assigned to beta testers through the public checklist. The pair was accepted by the maintainer on 7 November 2026. The accepted content version is v0.1.112-R002. The original Create World client profile and standard MinecraftServer-Test dedicated-server baseline now both contain the accepted pair, confirmed by the latest screenshots. A startup/login smoke test on this updated baseline is the next step. The CurseForge test entry mapped to a separate IronWoven Age Of Industry instance folder; the original Create World profile remained separate on the accepted pair.


**Latest corrected compatibility datapack retest — 6 November 2026, 15:54:** all four IronWoven world-scoped compatibility datapacks were enabled in the disposable test world. Dedicated-server startup, world load, matching client login, and clean shutdown with all dimensions saved passed. The corrected log contains no targeted Design n' Decor, Steam 'n' Rails, Create Kinetic, Sable Catwalk, or Create Deco placard errors. This is a log-level compatibility retest, not proof of every gameplay drop or recipe function. The log has 6 ERROR-level records and 172 WARN-level records; the remaining error findings are Struts, PowerGrid, Every Compat, Create Aeronautics Structures, and the Shulker Box Tooltip / Supplementaries integration. InControl read `areas.json`.

**Struts local test workaround — 6 November 2026:** the guarded Struts 1.3.1 mixin-side patch was applied and script-verified on matching disposable server and CurseForge client JARs; original backups were preserved. The 16:29–16:34 and 16:40–16:47 server/client/debug logs contain no `RenderSystem` or `StrutRenderSystemAccessor` messages. The server accepted the matching client and saved cleanly. The 16:46 screenshots show the tested Struts beams/girders rendering visibly. Two `girder_strut_structure` waterlogged-variant model warnings remain, but the shown pieces render. This passes local runtime and visual smoke checks; the release-level issue remains open because the modified JAR is not included in the official CurseForge file or modpack manifest.
**Shulker Box Tooltip / Supplementaries config and visual retest — 6 November 2026, 17:20–17:41:** setting only the CurseForge client's `preview.serverIntegration=false` suppresses the login handshake. The 17:29–17:41 server log again contains no `PreviewRenderer` invalid-dist or failed Supplementaries provider registration; the client registers 3 Supplementaries providers and 31 Shulker Box Tooltip providers locally, and the player joins and leaves before server shutdown. Screenshots at 17:39–17:40 visually confirm the Sack's nine-stack preview and the Lunch Basket's food contents/state preview. Local Supplementaries preview behavior passes. Remote Ender Chest/server-supplied preview extras are disabled by this workaround; it is not an upstream fix, so keep the compatibility issue open pending a release trade-off decision or server-safe upstream fix.

**PowerGrid 0.6.2 native solver investigation — 6 November 2026:** upstream [PowerGrid issue #1165](https://github.com/patryk3211/PowerGrid/issues/1165) confirms 0.6.2 accidentally omitted the Windows and Linux native binaries present in 0.6.1. The official 0.6.1 Windows DLL was copied to the disposable server and CurseForge `.pg-native` folders; the 0.6.2 JAR remains unchanged. Both the 18:29 server log and 18:34 client log report `Native backend loaded successfully`; the server reaches `Done (1.837s)` and the client connects to the test server and enters the world. Both internal Windows native-loading checks and the client connection pass. Functional PowerGrid electrical-network/component testing is assigned to beta testers, not an internal maintainer step. Linux testing remains a separate future platform check. The local `.pg-native` DLL copies are not in the distributable beta package; decide the native-resource packaging path before release.

**Create Aeronautics Structures status — 6 November 2026:** the maintainer-supplied JAR metadata identifies version 1.1.0-Beta-3.1 and matches official CurseForge file 8399115 by version (the downloaded file was not hash-compared). The official `uniform.json` loot table contains an invalid `minecraft:dyed_color.rgb` number-provider value. A test-only world datapack override using a 16-color vanilla dye palette passed runtime testing in disposable Windows `world_lootr_test`; the official mod JAR remains unchanged and the override is not release-approved. All 11 valid Overworld structure IDs now have locate/visual-presence evidence, including visually accepted crashed-airship hillside placement; `cr_aero_structures:plane` is invalid. Maintainer spot checks found items in the engineering-house standard barrel and Lootr barrel. One crashed-airship vanilla chest has `Items: []` and no `LootTable` / `LootTableSeed`, confirming a specific loot-assignment defect. Remaining structure/container loot coverage is delegated to beta testers. The candidate remains test-only; investigation of that chest defect and a release-safe uniform-table correction/distribution decision remain open.


- **Batches A, B, and C:** routine dedicated-server startup, disposable-world load, matching-client login, and log-review smoke tests passed. These checks do not prove individual mod features work.
- **Batch D — Create Aeronautics Structures:** partial. All 11 valid Overworld structure IDs have locate/visual-presence evidence; crashed-airship hillside placement was visually accepted and `plane` is invalid. The test-only uniform-loot override passed runtime testing. Engineering-house standard and Lootr barrels produced items in maintainer spot checks; one crashed-airship vanilla chest has no assigned loot table. Remaining container-loot coverage is delegated to beta testers. The official JAR remains unchanged; the release-safe correction/distribution decision and the specific missing chest loot assignment remain open.
- **Batch E — optional client rendering:** Entity Culling was removed from the current CurseForge client profile and is no longer an active candidate. ImmediatelyFast, Flerovium, and More Culling remain optional candidates only; confirm their presence in a fresh client inventory before isolated tests. The combined server smoke test is not client-rendering evidence. Test these only after the server-side and shared candidate queue is complete or explicitly deferred. spark profiling is deferred to beta testers and is not an internal release-preparation gate.
- **Latest disposable-server retest — 5 November, 22:27:** the server reached `Done (1.490s)`, a matching client joined, and the server shut down with all dimensions saved. Numismatics 1.0.20 was the only version active; Numismatics Plus was absent, so its addon pairing remains untested.
- **Integrated Villages 1.3.3+1.21.1:** the corrected server profile loaded its Supplementaries 3.4.0 and Integrated API 1.9.1 dependencies. Several village structure IDs were locatable, but full structure validation and vanilla-village replacement are not confirmed. Some locate searches caused server tick-delay warnings; the candidate remains under testing.
- **Memory observation:** a short G1 GC trace showed heap reclamation after allocation peaks. This is not a long-term memory-leak assessment or a measured TPS/MSPT/CPU baseline.
- **Regions Unexplored 0.6.3:** its official project description covers both Overworld and Nether biome generation. A dedicated Nether generation check has been added to the functional checklist; current IronWoven Nether behavior remains unverified in a disposable world.
- **Functional testing:** the [Full Installed-Mod Functional Testing Checklist](TESTING_CHECKLIST.md) tracks feature-level coverage. Most checks remain pending. Full functional validation is required before beta release.

## Release readiness

**Not ready for public release.** Outstanding compatibility and functional checks, a reconciled CurseForge client manifest and server inventory, clean-install validation, and final release review remain.

## Project direction

The pack focuses on Create and Create Aeronautics, with engineering, transport, trains, automation, building, and exploration. The mod download and distribution policy is **CurseForge only**.

The production world and its existing BYG 2.6.3 / Regions Unexplored 0.6.3 setup remain unchanged and protected during testing.

## Where to get help

Read [Support and Troubleshooting](SUPPORT.md), review [Known Issues](KNOWN_ISSUES.md), or use the [public issue tracker](../../issues). Share only sanitized logs and screenshots.
