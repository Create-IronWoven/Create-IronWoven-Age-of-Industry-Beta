# Beta Status

<!-- IRONWOVEN_AUTO_VERSION -->
**Current Ironwoven pack version:** `v0.1.101.5` — release `0`, content revision `1`, `101` top-level server mod JARs, and `5` active accepted bug fixes.
**Release status:** Internal development; no downloadable public beta has been published.  
**Last updated:** 11 November 2026  
**Minecraft:** 1.21.1 · **NeoForge:** 21.1.265 · **Java:** 21

## Current status

The previous numbered installation-batch sequence has been retired by the maintainer. Historical batch labels in dated records are evidence only, not active tasks or a queue to restart. The public [Testing Checklist](TESTING_CHECKLIST.md) remains the place for beta testers to record feature/function results.

The latest working-profile reconciliation is newer than the older folder snapshots listed in historical inventory notes. Those working archives include test-only and held files, so they are not an approved release manifest. The final public mod inventory will be published only after the exact CurseForge client export and dedicated-server package have been reconciled and the release candidate frozen.

The generated `v0.1.101.5` version is based on the separate clean Windows server baseline recorded on 7 November: 101 top-level server JARs and five active accepted bug fixes. Do not infer a release version from client-profile counts or older test-folder snapshots. See [CHANGELOG](CHANGELOG.md) for version rules.

## Active mod-set updates — verified 10–11 November 2026

The following exact versions passed their authorised, scope-appropriate shared smoke tests and are accepted into the active mod set. This does **not** mark their feature tests complete or grant downloadable-beta/release approval.

| Mod | Previous version / CurseForge file | Accepted version / CurseForge file | Smoke evidence | Feature / release state |
|---|---|---|---|---|
| FastSuite / Placebo | New active mod-set addition | 6.0.7 / file 7527945 + 9.9.4 / file 9153039 | Exact-file/dependency preflight, matching client/server profile hashes, and authorised 11 November combined-profile smoke PASS | Accepted into active mod set; recipe/JEI/performance actions Pending for beta testers |
| Sophisticated Backpacks | 3.26.20.2244 / [9431839](https://www.curseforge.com/minecraft/mc-mods/sophisticated-backpacks/files/9431839) | 3.26.21.2249 / [9524812](https://www.curseforge.com/minecraft/mc-mods/sophisticated-backpacks/files/9524812) | Shared startup/login/clean-shutdown PASS, 10 November; client/server SHA-256 matched | Feature actions Pending — beta testers |
| Sophisticated Core (support dependency) | 1.5.28.2458 / [9431812](https://www.curseforge.com/minecraft/mc-mods/sophisticated-core/files/9431812) | 1.5.32.2464 / [9524669](https://www.curseforge.com/minecraft/mc-mods/sophisticated-core/files/9524669) | Same coordinated Backpacks smoke; exact client/server SHA-256 match | Tested through Backpacks; no standalone gameplay row |
| Create: The Factory Must Grow Community Edition | 1.3.3 / [9413167](https://www.curseforge.com/minecraft/mc-mods/tfmg-community-edition/files/9413167) | 1.3.3a / [9482161](https://www.curseforge.com/minecraft/mc-mods/tfmg-community-edition/files/9482161) | Shared startup/login/clean-shutdown PASS, 10 November; exact client/server SHA-256 match | Feature/visual actions Pending; Custom License distribution review remains a separate release gate |

The 10 November active-profile archive audit found 102 JARs in each test-profile archive: 101 shared non-WITS JARs have identical hashes. WITS is a temporary testing utility and is excluded from the mod set. Railways `0.3.0-beta.2` and Supplementaries `4.0.2` also appear in both archives with matching hashes, but remain observations pending their own exact CurseForge/dependency review and maintainer update disposition. Waystones `21.1.46` is present despite the core-Waystones deferral; base Sable `2.0.6` is a separate SubLevel physics library. The distinct Waystones: Sable `1.0.7` integration addon is absent and remains optional/deferred. These profiles are not the selected clean v.0.1 release server.

## Recent smoke-test evidence

- **FastSuite 6.0.7 (file 7527945) / Placebo 9.9.4 (file 9153039) — 11 November:** accepted into the active mod set after exact-file/dependency preflight, matching client/server hashes, and authorised combined-profile smoke PASS. No isolated optimizer run is required; recipe/JEI/performance actions remain Pending for beta testers. **FastFurnace 9.0.1 (file 6751551)** also passed exact CurseForge file/dependency/side preflight and loaded on both sides in the same combined-profile smoke PASS. Do not add a duplicate or repeat the smoke test; record its explicit mod-set/package disposition at release freeze.
- **Sophisticated Backpacks 3.26.21.2249 (file 9524812) / Sophisticated Core 1.5.32.2464 (file 9524669) — 10 November:** accepted into the active mod set after authorised shared smoke PASS and exact client/server SHA-256 parity. Backpack feature actions remain Pending for beta testers; Core is validated through Backpacks.
- **Create: The Factory Must Grow Community Edition 1.3.3a (file 9482161) — 10 November:** accepted into the active mod set after authorised shared smoke PASS and exact client/server SHA-256 parity. Feature/visual actions remain Pending; Custom License distribution review remains a separate release gate.
- **Every Compat 2.11.57 / Moonlight Lib 3.8.2:** accepted baseline pair; fresh clean-server smoke passed. The Golden Cherry Leaves duplicate registration remains an open compatibility finding.

A smoke-test pass does not prove feature behavior, compatibility with every installed mod, performance improvement, or release approval.

## Holds and safeguards

- **Create Aeronautics Structures 1.1.0-Beta-3.1:** ON HOLD; the known loot-table and crashed-airship chest issues remain unresolved. It is not eligible for the beta package.
- **Create Aeronautics: Gadgets & Gizmos 2.0.0-Pre-Release-4:** ON HOLD; keep bundled 1.2.10 unchanged. Do not install or test the prerelease.
- **Lithium 0.15.4:** ON HOLD / deferred.
- The End workstream and Terralith investigation remain paused. Preserve the existing BYG 2.6.3 / Regions Unexplored 0.6.3 setup and existing worlds.
- Existing explicit exclusions remain in force.

## Testing responsibilities

The maintainer's internal scope is exact CurseForge file/dependency/side preflight, routine smoke testing, and evidence/log review. Beta testers perform feature/function actions for every installed feature/content mod, whether server-only, shared client/server, or client-only. Pending feature actions are expected during the initial beta when represented in the checklist; they are not passes. Complete the full functional matrix before a later stable/final release.

## Server platform

Windows is the current development/test environment. Linux server compatibility and runtime behavior are NOT TESTED / NOT VERIFIED.

## Release readiness

**NOT READY.** No downloadable beta has been published. Exact final client/server package inventories, FastFurnace's final mod-set/package disposition, compatibility and licence decisions, clean final-package smoke testing, and explicit release approval remain required.
