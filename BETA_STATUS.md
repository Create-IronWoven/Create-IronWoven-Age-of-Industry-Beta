# Beta Status — v0.1.110-R002

**Current development version:** `v0.1.110-R002` (not yet a downloadable public beta)  
**Last updated:** 5 November 2026  
**Minecraft:** 1.21.1 · **NeoForge:** 21.1.265 · **Java:** 21

## Current status

The current development version `v0.1.110-R002` uses content-change counter `110` as the retroactive baseline from the 5 November 2026 CurseForge screenshot (`Mods (110)`). Removal counter `R002` records two client-only removals: Sodium 0.8.13 and Sodium Extra 0.9.5. The latest profile screenshot shows `Mods (108)`. The client and server folders each show 104 JAR files; these are different inventory measures because bundled components may be counted separately by CurseForge. This is not a claim of 110 public releases. No downloadable beta package exists.

Create IronWoven is in **internal compatibility and functional testing**. There is currently no public downloadable beta package and no release date has been announced.

- [Current test-pack inventory](MODS.md)
- [Functional testing progress](TESTING_CHECKLIST.md)
- [Planned mods and project decisions](MOD_PLANS.md)
- [Known player-relevant issues](KNOWN_ISSUES.md)

## Testing progress

- **Batches A, B, and C:** routine dedicated-server startup, disposable-world load, matching-client login, and log-review smoke tests passed. These checks do not prove individual mod features work.
- **Batch D — Create Aeronautics Structures:** partial test. A candidate-specific loot-table error remains unresolved; exact CurseForge file provenance and structure generation have not been confirmed.
- **Batch E — client rendering:** the combined server smoke test is historical evidence only; the client-only rendering candidates remain pending and will be tested after the server-side and shared candidate queue. spark profiling is deferred to beta testers and is not an internal release-preparation gate.
- **Latest disposable-server retest — 5 November, 22:27:** the server reached `Done (1.490s)`, a matching client joined, and the server shut down with all dimensions saved. Numismatics 1.0.20 was the only version active; Numismatics Plus was absent, so its addon pairing remains untested.
- **Integrated Villages 1.3.3+1.21.1:** the corrected server profile loaded its Supplementaries 3.4.0 and Integrated API 1.9.1 dependencies. Several village structure IDs were locatable, but full structure validation and vanilla-village replacement are not confirmed. Some locate searches caused server tick-delay warnings; the candidate remains under testing.
- **Memory observation:** a short G1 GC trace showed heap reclamation after allocation peaks. This is not a long-term memory-leak assessment or a measured TPS/MSPT/CPU baseline.
- **Functional testing:** the [Full Installed-Mod Functional Testing Checklist](TESTING_CHECKLIST.md) tracks feature-level coverage. Most checks remain pending. Full functional validation is required before beta release.

## Release readiness

**Not ready for public release.** Outstanding compatibility and functional checks, a reconciled CurseForge client manifest and server inventory, clean-install validation, and final release review remain.

## Project direction

The pack focuses on Create and Create Aeronautics, with engineering, transport, trains, automation, building, and exploration. The mod download and distribution policy is **CurseForge only**.

The production world and its existing BYG 2.6.3 / Regions Unexplored 0.6.3 setup remain unchanged and protected during testing.

## Where to get help

Read [Support and Troubleshooting](SUPPORT.md), review [Known Issues](KNOWN_ISSUES.md), or use the [public issue tracker](../../issues). Share only sanitized logs and screenshots.
