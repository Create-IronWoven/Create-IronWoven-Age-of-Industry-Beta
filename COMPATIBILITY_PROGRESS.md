# Compatibility Progress

Last updated: 4 November 2026  
Test target: Minecraft 1.21.1 / NeoForge 21.1.265 / Java 21

This page summarizes compatibility work from the internal Create IronWoven test environment. A local test fix does not automatically mean that a public beta release is ready.

## Confirmed in internal smoke tests

The following corrections removed their recorded startup or data-loading errors during the standard test sequence (server startup, disposable test-world load, matching client login, and log review):

| Component | Finding | Internal result |
|---|---|---|
| Steam 'n' Rails | 192 optional compat-track loot-table parsing errors | No matching errors after the IronWoven datapack added item-existence load conditions |
| Create Kinetic | 5 missing-item loot-table parsing errors | No matching errors after the IronWoven datapack added item-existence load conditions |
| Create Kinetic | Client-only Minecraft mixin loaded on dedicated server | No matching invalid-dist or mixin-target errors after moving the mixin to the client list in the test server and client JARs |
| Copycats+ / Sable | Sable cannot resolve the Copycat Catwalk selector | No unknown-block or physics-property errors after the selector override |
| Create Deco | White Dye placard recipe uses an invalid ingredient key | No placard recipe parsing error after the datapack correction |
| Create: Design n' Decor | 256 Dye Depot-dependent loot tables fail when Dye Depot is absent | Errors suppressed in the internal pack with temporary disabled-resource overrides |
| Mama's Herbs and Harvest | 47 Botany Pots integration recipes fail when Botany Pots is absent | Errors suppressed in the internal pack with temporary disabled-resource overrides |
| In Control! | areas.json write error | No recurrence after correcting the server configuration |
| Create: Enchantment Industry | Six optional loot-table parsing errors in the earlier 2.4.2 build | No matching errors after a separate test of 2.5.4b |

These are log-based smoke-test results. They do not claim full gameplay validation of every recipe, loot drop, physics interaction, or feature.

## Important optional-mod behavior

Two internal datapack workarounds use NeoForge's always-false condition to skip files while optional companion mods are absent:

- 256 Design n' Decor loot tables are skipped while Dye Depot is absent.
- 47 Herbs & Harvest Botany Pots recipes are skipped while Botany Pots is absent.

These temporary overrides are **not intended as upstream source fixes**. They suppress those files unconditionally while present in the pack. If Dye Depot or Botany Pots is added in a future pack revision, the corresponding overrides must be removed and the content re-tested.

The desired upstream behavior is conditional loading: the optional files should load when their companion mod is present and be skipped cleanly when it is absent.

## Remaining findings

| Component | Current observation | Status |
|---|---|---|
| Struts | Dedicated server attempts to load client-only RenderSystem mixin | Still present in the latest recorded test log; upstream has an existing report: https://github.com/cakeGit/StrutYourStuff/issues/6 |
| Power Grid | Optional native solver library powergridNative7 fails to load; non-accelerated solver remains available | Cause not yet confirmed; needs a fresh full exception and OS/architecture details |
| Create Liquid Fuel | A nonfatal data-map warning is recorded | Need full warning context before attributing it to a mod defect |
| Food tag | Nonfatal c:foods/pork warning | Consumer/owner not yet identified |
| Regions Unexplored | Nonfatal ocelot mob-category warnings | Need full warning context and source trace |

## Upstream correction work

The private development repository contains the technical ownership register, report drafts, and candidate patch files. The public-facing handovers will use the correct owning mod repository and existing issue/PR thread where one already exists.

Relevant existing upstream discussions identified so far:

- Steam 'n' Rails: https://github.com/Porters-of-Railways/Railway-1.21.1/pull/393
- Create Kinetic: no matching open issue found yet for the two findings
- Copycats+: https://github.com/copycats-plus/copycats/issues/437
- Create Deco: https://github.com/talrey/CreateDeco/issues/268
- Design n' Decor: https://github.com/DrMango14/Create-Design-n-Decor/issues/139
- Struts: https://github.com/cakeGit/StrutYourStuff/issues/6

No external developer report or patch has been submitted from this project yet. Upstream patches are being prepared and reviewed first. No personal credit or payment is requested for these contributions.

## Test and world safeguards

- Testing used the disposable world world_biome_balance_test2.
- The production world and its BYG 2.6.3 / Regions Unexplored setup were not changed.
- Do not add, remove, or update mods based only on this progress page.
- Batch 7 and the requested End-mod additions remain on hold.
- The internal test report is not a public beta release declaration.
