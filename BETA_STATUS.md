# Beta Status

<!-- IRONWOVEN_AUTO_VERSION -->
**Current IronWoven pack version:** `v0.1.101.5` — release `0`, content revision `1`, `101` top-level server mod JARs, and `5` active accepted bug fixes.  
**Release status:** Internal development; no downloadable public beta has been published.  
**Last updated:** 11 November 2026  
**Minecraft:** 1.21.1 · **NeoForge:** 21.1.265 · **Java:** 21

## Current status

The previous numbered installation-batch sequence has been retired by the maintainer. Historical batch labels in dated records are evidence only, not active tasks or a queue to restart. The public [Testing Checklist](TESTING_CHECKLIST.md) remains the place for beta testers to record feature/function results.

The latest working-profile reconciliation is newer than the older folder snapshots listed in historical inventory notes. Those working archives include test-only and held files, so they are not an approved release manifest. The final public mod inventory will be published only after the exact CurseForge client export and dedicated-server package have been reconciled and the release candidate frozen.

The generated `v0.1.101.5` version is based on the separate clean Windows server baseline recorded on 7 November: 101 top-level server JARs and five active accepted bug fixes. Do not infer a release version from client-profile counts or older test-folder snapshots. See [CHANGELOG](CHANGELOG.md) for version rules.

## Recent smoke-test evidence

- **FastSuite 6.0.7 / Placebo 9.9.4 / FastFurnace 9.0.1 — 11 November:** the matching files were loaded on both sides in a combined-profile session. Server startup, world load, matching-client login, and clean shutdown passed. This is a profile-level smoke result, not feature or performance validation. FastFurnace's exact CurseForge file/dependency/side preflight remains before package inclusion.
- **Sophisticated Backpacks 3.26.21.2249 / Sophisticated Core 1.5.32.2464 — 10 November:** shared startup/login/clean-shutdown smoke passed. Backpack feature actions remain for beta testers.
- **Create: The Factory Must Grow Community Edition 1.3.3a — 10 November:** shared startup/login/clean-shutdown smoke passed. It remains a test candidate, not an accepted baseline; visual asset warnings and licence review remain open.
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

**NOT READY.** No downloadable beta has been published. Exact final client/server package inventories, FastFurnace preflight, compatibility and licence decisions, clean final-package smoke testing, and explicit release approval remain required.
