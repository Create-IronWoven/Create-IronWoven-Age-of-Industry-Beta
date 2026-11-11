# Testing order and responsibilities for beta candidates

**Maintainer scope:** exact CurseForge file/dependency/side preflight and routine smoke testing only (startup, world load, matching-client login, and relevant log review). Do not treat this as feature validation.

**Beta-tester scope:** beta testers perform feature/function actions for every installed feature/content mod, whether server-only, shared client/server, or client-only. The action matrix below is the source of those tasks. Pending actions are expected during the initial beta and are not passes.

- Internal profile-smoke work follows the server-first order: server-only mods, then shared client/server mods, then client-only profile checks.
- Resolve or explicitly disposition server-only/shared dependency, startup, world-load, or matching-client login blockers before moving the internal profile-smoke queue to client-only mods.
- Split mixed mod sets by side. Keep client-only JARs out of the dedicated-server mods folder.
- Client-only profile smoke checks use the matching client after server/shared smoke work; beta-tester feature actions for all sides are submitted through the checklist and do not require internal one-at-a-time optimizer isolation.
- **spark profiling is deferred to beta testers.** It is not an internal development prerequisite; beta testers may capture performance baselines during the beta phase.

# Full Installed-Mod Functional Testing Checklist

**Last reviewed:** 11 November 2026  
**Target:** Minecraft 1.21.1 · NeoForge 21.1.265 · Java 21  
**Approved download source:** CurseForge only

This checklist is a feature-test matrix, not a live installed-mod manifest. It follows the recorded test inventory and separately labels current client-only candidates, completed checks, holds, and dated historical evidence. For current file inventories and versions, use [MODS.md](MODS.md): the 6 November `MinecraftServer-Test` snapshot is historical and separate from the 7 November clean v.0.1 server and latest CurseForge client-profile screenshot. Do not treat historical snapshot tables below as current installation instructions. This is not a final release manifest.

## Current verification snapshot — 10 November 2026

This section is the current status summary. Dated trial tables later in this file are historical evidence and must not be read as the current installed inventory.

| Area | Current verified status |
|---|---|
| Dedicated-server smoke test | PASS — the fresh Windows v.0.1 server reached `Done (4.440s)`, generated its world, accepted a matching client, and shut down with all dimensions saved; the separate corrected 6 Nov disposable-profile retest also passed |
| Fresh dedicated-server installation v.0.1 | PASS — clean Windows server; 101 top-level mod JARs; 116 non-core mod IDs in NeoForge Mod List; world generated; all four IronWoven datapacks enabled among 12; target Design n' Decor, Steam 'n' Rails, Create Kinetic, Create Deco placard and Sable Catwalk errors absent; matching client login, OP grant, Creative command and clean shutdown with all dimensions saved. Separate compatibility ERROR records remain under investigation: five are attributed to PowerGrid, Every Compat, Create Aeronautics Structures, and Shulker Box Tooltip/Supplementaries; three unassigned entity-attachment warnings use `apotheosis:tier_augments_applied`. The fresh `mods/` folder screenshot contains no Apotheosis-named JAR, and the maintainer confirms Apotheosis is not installed or planned. Keep those three warnings monitor-only; do not install Apotheosis or attribute them to an installed mod without evidence. Feature-level testing remains separate. |
| World-scoped compatibility datapacks | PASS at log level — all four packs were enabled among 12 in the fresh 7 Nov world; the five targeted Design n' Decor, Steam 'n' Rails, Create Kinetic, Sable Catwalk and Create Deco placard errors were absent in the fresh 7 Nov log and corrected 6 Nov retest |
| Struts | PARTIAL — local patched server/client runtime and visible test pieces passed; official CurseForge JAR remains unpatched, so standard-install/release issue remains open |
| Shulker Box Tooltip / Supplementaries | PARTIAL — client-only `preview.serverIntegration=false` workaround passed local join/log/visual checks; remote server-provided preview extras are disabled; upstream/release decision remains open |
| PowerGrid 0.6.2 | PARTIAL — internal Windows native loading and client join passed with restored 0.6.1 DLL; electrical-network behavior reserved for beta testers; Linux untested |
| Every Compat | PARTIAL — accepted pair 2.11.57 + Moonlight 3.8.2 passed Windows disposable startup/world/login/shutdown smoke test; duplicate Golden Cherry Leaves registration remains open; feature-level checks are assigned to beta testers; client and server folder deployment confirmed; updated-baseline startup/login verification pending |
| Create Aeronautics Structures | **ON HOLD** — not eligible for the next beta. Previous disposable-world observations and the test-only 16-colour override result are retained as history; the official uniform table remains malformed and one crashed-airship chest had no loot-table assignment. Do not perform further tests or package this candidate until a new official CurseForge 1.21.1 NeoForge file is reviewed and both defects are verified fixed, or an explicitly approved documented exception exists. |
| Integrated Villages | PARTIAL — server load and structure-ID lookups observed; generation completeness, vanilla-village behavior and performance remain unverified |
| Create: The Factory Must Grow 1.3.3a | SMOKE PASS — matching client/server loaded the same candidate filename/version and completed login; TFMG feature actions remain NOT TESTED; Electric Diode/Fuse Block visual checks pending; candidate not accepted |
| Entity Culling | REMOVED from current CurseForge client profile; confirmed absent in 6 Nov client-folder screenshot; not an active test candidate |
| ImmediatelyFast / Flerovium / More Culling | Optional client candidates only; not confirmed as currently installed by latest client screenshot; do not treat as current installed mods |
| Linux dedicated server | NOT TESTED — Linux system has not yet been set up |
| Individual feature matrix | OPEN — pending rows remain pending until the specific behavior is tested and evidence is recorded |
| Public beta / release | NOT APPROVED — no downloadable beta package exists |

**Current inventory source:** [MODS.md](MODS.md) holds separate server and client observations. The latest 6 November Windows client screenshot confirms Entity Culling is absent from the CurseForge `Create World/mods` folder. The 6 November server inventory screenshot is not a client inventory. A separate 10 November TFMG update test confirms the same candidate filename/version was loaded on the active client and dedicated server; this is not a full inventory/hash reconciliation. No production world or production world-generation configuration was changed.

**How to submit test results:**

1. Open the [Submit Test Result form](https://github.com/Create-IronWoven/Create-IronWoven-Age-of-Industry-Beta/issues/new?template=functional-test-report.yml).
2. Copy the mod heading text (including version, without the leading ### symbols) and the exact test-action text from the table below.
3. Select the test environment: Single-player, Multiplayer, or Both. Choose Both only when you actually tested the action in both environments.
4. Enter a tester nickname or pseudonym and the test date in DD-MM-YYYY format, choose the result, and describe what happened. Do not enter a legal/real name or GitHub username. Note: GitHub shows the account that opened the report as the public issue author, but the automation does not copy that account name into this checklist. Do not use your legal/real name or GitHub account username.
5. Submit the form. The Beta-to-private forwarding path and invalid-report safeguards have been verified. A valid, unique report updating a matching checklist row is still awaiting end-to-end verification. A submitted issue does not by itself confirm that a checklist row changed; check this page after submission and contact the maintainers if the result does not appear.

Submit one form for each test action. The processor is designed to match the mod/action text and preserve existing results. Duplicate reports are detected and do not overwrite the original result. Retests of completed actions require maintainer review; existing results are never silently overwritten.

A server startup or an item appearing in JEI is not, by itself, a function-test pass. Keep smoke-test evidence separate from feature tests.

## Smoke test is not a function test

The fresh Windows v.0.1 server reached `Done (4.440s)`, generated `IronWoven Age Of Industry_v0.1.0`, enabled all four IronWoven world-scoped datapacks among 12 total, accepted the matching client, granted operator permissions, accepted a Creative-mode command, and shut down with all dimensions saved. The five targeted Design n' Decor, Steam 'n' Rails, Create Kinetic, Sable Catwalk and Create Deco placard error families were absent from its log. This fresh-install smoke test is separate from the 6 November 15:54 corrected `world_lootr_test` retest, which also passed startup/world/login/shutdown with all four packs enabled. Later 6 November targeted retests confirmed the local Struts workaround, Shulker Box Tooltip / Supplementaries client workaround, and PowerGrid Windows native loading workaround; see the dated records below. The fresh 7 November log still contains eight ERROR-level records and five DUMMY block-entity warnings, including three unattributed entity-attachment warnings; review [KNOWN_ISSUES.md](KNOWN_ISSUES.md) and keep unknown sources unattributed. These are test-profile-specific results; **they do not prove every installed mod's functions work or establish Linux compatibility**.

- **Smoke test:** mod discovery, server/client startup as appropriate, world load, login, shutdown and log review.
- **Function test:** exercise the actual feature(s) that justify keeping the mod: item/block interaction, machine process, transport, GUI, world generation, rendering, recipe/loot behavior or synchronization.
- A combined smoke-test pass is not an individual mod-function pass. Do not mark a feature complete just because its mod ID appears in a server log.
- Client-only mods require a matching client launch and client-side review. A dedicated-server log cannot prove their client functions.
- Libraries/APIs are tested through the mod(s) that depend on them; they do not need invented standalone gameplay tests.

## Current pack-level smoke evidence

| Check | Evidence | Status |
|---|---|---|
| Dedicated-server startup | Fresh Windows v.0.1 reached `Done (4.440s)`; corrected 6 Nov disposable run reached `Done (1.413s)` | PASS — both profiles |
| Disposable-world load | Fresh v.0.1 world generated on 7 Nov; corrected `world_lootr_test` loaded on 6 Nov | PASS — both profiles |
| IronWoven compatibility datapacks | All four world-scoped packs enabled among 12 total in fresh v.0.1 and in corrected `world_lootr_test` | PASS — log-level retest |
| Targeted compatibility errors | Design n' Decor, Railways, Create Kinetic, Sable Catwalk, and Create Deco placard errors absent in fresh 7 Nov and corrected 6 Nov logs | PASS — log review only |
| Matching client login | Matching client joined in fresh 7 Nov and corrected 6 Nov runs; 7 Nov operator and Creative-mode commands also succeeded | PASS — smoke test only |
| Clean shutdown | All dimensions saved in the fresh 7 Nov run and corrected 6 Nov retest | PASS |
| TFMG 1.3.3a shared update smoke | Matching client/server loaded `tfmg-1.21.1-1.3.3a-community.jar`; client connected and completed SBT handshake; server saved all dimensions | PASS — smoke only; hash equality and feature behavior not tested |
| Sophisticated Backpacks 3.26.21.2249 + Sophisticated Core 1.5.32.2464 | Matching pair loaded on client and dedicated server; client joined; all dimensions saved on clean shutdown | PASS — shared smoke only; Backpack feature actions remain Pending for beta testers |
| Individual feature tests | Matrix below | OPEN — mostly not yet function-tested |
| Matching client-only mod startup | Targeted client evidence exists for PowerGrid and local Struts / tooltip workaround tests; no complete isolated optional-client candidate sweep | PARTIAL — optional candidates remain open |
| Remaining fresh-server log findings | 8 ERROR-level records (five attributed to PowerGrid, Every Compat, Create Aeronautics Structures and SBT/Supplementaries; three unattributed entity-attachment warnings) and five DUMMY block-entity warnings remain under review | OPEN — do not attribute unknown records to a mod without evidence |
| Production/release approval | Not granted | NOT APPROVED |


## PowerGrid Windows native-load retest — 6 November 2026, 18:29–18:34

**Result: internal Windows native loading and client connection passed. Electrical-network/component behavior is a beta-tester feature check, not another internal maintainer task.** The PowerGrid 0.6.2 JAR was not modified. The official 0.6.1 Windows DLL was copied into the disposable server and CurseForge client `.pg-native` directories. The 18:29 server log and 18:34 client log both reported `Native backend loaded successfully`. The server reached `Done (1.837s)`; the matching client connected to `localhost:25565` and entered the world. This workaround must not be mistaken for an official 0.6.2 package fix or an accepted modpack change.

- Windows server native load: PASS — disposable profile.
- Windows client native load: PASS — matching CurseForge profile.
- PowerGrid electrical network / component behavior: DEFERRED TO BETA TESTERS; not an internal fix-pass task.
- Linux native solver: NOT TESTED — Linux requires the Linux `.so`; do not use the Windows DLL.
- Production files and modpack manifest: unchanged.

## Historical snapshot — existing-mod update trial, 5 November 2026, 13:43

**Historical record only — not the current installed-mod list.** The Entity Culling entry below records detection in this old disposable-server folder. Entity Culling was subsequently removed from the current CurseForge `Create World/mods` client profile; the maintainer's 6 November 2026 screenshot confirms it is absent. Do not interpret this old row as a current installation or active test candidate.

**Result: FAILED before server startup completed.** This was a separate disposable-server update attempt, not a replacement for the earlier successful combined smoke test.

| Mod | Version detected | Result |
|---|---:|---|
| Sophisticated Core | 1.5.28.2458 | Detected |
| Sophisticated Backpacks | 3.26.20.2244 | Detected |