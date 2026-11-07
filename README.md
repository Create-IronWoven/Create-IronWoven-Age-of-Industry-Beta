# Create IronWoven: Age of Industry

![Create IronWoven: Age of Industry](assets/Ironwoven_%20Age%20of%20Industry.v2.png)

**Build. Engineer. Explore. Transport. Automate.**

**Beta access is limited:** participation is by invitation or approved application only. Public access to this repository does not automatically grant permission or access to beta testing builds, servers, or activities. Acceptance is confirmed separately by the project maintainer.

**Want to apply?** [Apply to become a beta tester](https://github.com/alexth110987/Create-IronWoven-Age-of-Industry-Beta/issues/new?template=beta_application.yml). Applications are reviewed manually; submitting one does not grant access.


Create IronWoven: Age of Industry is an industrial and steampunk Minecraft modpack built around **Create**, **Create Aeronautics**, trains, automation, engineering, transport, building, and exploration.

<!-- IRONWOVEN_AUTO_VERSION -->
**Current Ironwoven pack version:** `v0.1.101.5` — release `0`, content revision `1`, `101` top-level server mod JARs, and `5` active accepted bug fixes.

**Development status:** Internal testing. This is a development version, not a downloadable public beta release. The accepted Every Compat 2.11.57 + Moonlight Lib 3.8.2 pair is confirmed in both the original Create World client profile and normal MinecraftServer-Test dedicated-server folder; startup/login verification on that updated baseline remains pending. A separate clean Windows server installation named `IronWoven Age Of Industry v.0.1` has 101 top-level mod JAR files and 116 non-core NeoForge pack mod IDs. Its world `IronWoven Age Of Industry_v0.1.0` generated successfully; all four IronWoven datapacks are enabled; matching-client login, operator access, Creative-mode command, and clean shutdown all passed. Eight separate ERROR-level records remain in that fresh log: five attributed to PowerGrid, Every Compat, Create Aeronautics Structures, and Shulker Box Tooltip/Supplementaries, plus three unattributed entity-attachment warnings. Their source/effect is unknown; do not attribute them to an installed mod without evidence. No server download is available. **Gadgets & Gizmos 2.0.0-Pre-Release-4 is on hold; the bundled 1.2.10 baseline stays unchanged.**

<badge>PROJECT POLICY</badge>

> **NO BACKPORTS — THIS MODPACK SUPPORTS ITS SELECTED MINECRAFT VERSION ONLY.**
>
> Ironwoven does not create, maintain, or accept backports to older Minecraft versions. We do not downgrade the pack, maintain parallel legacy-version branches, or select outdated mod releases just to make the pack run on an older Minecraft version. Mod research, compatibility checks, testing, and releases target the Minecraft and NeoForge versions explicitly listed below. If a required mod is unavailable for the selected target, it is treated as unavailable; the pack will not be backported to accommodate it.

## Quick links

- [Apply to become a beta tester](https://github.com/alexth110987/Create-IronWoven-Age-of-Industry-Beta/issues/new?template=beta_application.yml)
- [Current beta status](BETA_STATUS.md)
- [Mods in the current test pack](MODS.md)
- [Planned mods and project decisions](MOD_PLANS.md)
- [Testing progress](TESTING_CHECKLIST.md)
- [Submit test results](https://github.com/alexth110987/Create-IronWoven-Age-of-Industry-Beta/issues/new?template=functional-test-report.yml)
- [Known issues](KNOWN_ISSUES.md)
- [Dimensions and exploration](DIMENSIONS.md)
- [Changelog](CHANGELOG.md)
- [Support and troubleshooting](SUPPORT.md)
- [Report a problem or suggest an idea](https://github.com/alexth110987/Create-IronWoven-Age-of-Industry-Beta/issues)

## Platform

| Component | Target |
|---|---|
| Minecraft | 1.21.1 |
| Mod loader | NeoForge 21.1.265 |
| Java | 21 |
| Mod source | CurseForge only |

**Server platform status:** Windows is the current development/test environment. Linux server support is planned but has not yet been tested; Linux setup and validation are pending. Do not interpret planned Linux support as a verified compatibility claim.

This repository is the public information and feedback hub. It does not host modpack downloads. When a beta is available, its release and installation instructions will be published here.

## Feedback

Before reporting a problem, check [Known Issues](KNOWN_ISSUES.md) and search the [issue tracker](../../issues). Include reproduction steps, Minecraft/NeoForge versions, and the modpack build if one was provided.

Remove usernames, private addresses, local paths, passwords, tokens, and personal information from logs or screenshots. Do not upload world saves, private backups, or third-party mod JARs.

A successful server startup does not prove every mod feature works. The [testing checklist](TESTING_CHECKLIST.md) separates startup checks from individual feature validation. Testers can submit one action at a time using the [Functional Test Result form](https://github.com/alexth110987/Create-IronWoven-Age-of-Industry-Beta/issues/new?template=functional-test-report.yml). Each report records whether the action was tested in Single-player, Multiplayer, or Both. The test-result forwarding path is active, but the first-time submission-to-checklist update path is still undergoing end-to-end verification. A submitted form does not by itself confirm that a checklist row changed; check the current checklist after submitting, and contact the maintainers when a result does not appear.
