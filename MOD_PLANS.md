# Mod Plans

This page gives players a short overview of planned, considered, paused, and excluded content. It is not the installed-mod list or a release approval list.

- [Mods in the current test snapshot](MODS.md)
- [What still needs testing](TESTING_CHECKLIST.md)
- [Current project status](BETA_STATUS.md)

**Target:** Minecraft 1.21.1 · NeoForge 21.1.265  
**Mod source policy:** CurseForge only

## Status meanings

| Status | Meaning |
|---|---|
| In testing | Present in a test profile; feature checks may be incomplete. |
| Candidate | Being considered; not installed or approved for release. |
| Partial | Some checks passed, but a problem or unanswered check remains. |
| On hold | Work is paused; do not assume it is being researched or tested. |
| Excluded | The maintainer has decided this content is not wanted. |

## Current testing and follow-ups

| Area | Public status |
|---|---|
| Create Aeronautics Structures | Partial test. Loot-table issue, exact CurseForge file provenance, and structure generation remain unresolved. |
| Performance and rendering | Partial. No measured server performance baseline yet; client rendering candidates require separate client tests. |
| Botany Pots and Construction Sticks | Loaded in a test group; feature validation remains open. |
| Lootr | Partial compatibility observations; independent per-player loot still needs verification. |
| Every Compat (Wood Good) | Candidate only; not installed or approved. |
| Exploration tools and Create Big Cannons | Routine startup/login smoke tests passed; this is not feature validation or release approval. |

Detailed technical evidence, exact file/dependency checks, and test history are maintained in the private development repository. The public [testing checklist](TESTING_CHECKLIST.md) is the place to see current testing tasks.

## Future ideas

These are ideas for possible future investigation, not commitments or installation plans:

- Colony building and settlement systems, including MineColonies integrations.
- Additional world-generation and ecology options, subject to compatibility with the existing world-generation setup.
- More exploration content and structures.
- Additional performance and client-rendering improvements, tested independently for this modpack.

## Paused work

- **End expansion:** paused by the maintainer. Historical End candidates are not an active shortlist or test queue.
- **Terralith:** world-generation investigation is paused. The current BYG 2.6.3 / Regions Unexplored 0.6.3 setup and existing worlds must remain unchanged.

## Explicit exclusions

The following content is not wanted and must not be reintroduced unless the maintainer explicitly changes the decision:

- Carry On
- Easy Villagers
- Immersive Paintings
- Bigger Better End Cities
- Create: Sophisticated Exoskeleton 1.0
- Distant Horizons 3.3.3

## Important

A mod being suggested, researched, or present in a disposable test profile does not mean it is compatible, accepted, or approved for public release. Only CurseForge-hosted mods are eligible for consideration. The production world and installed production pack must not be changed as part of candidate testing.
