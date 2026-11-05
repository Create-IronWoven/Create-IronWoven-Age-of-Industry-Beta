# Changelog

Player-facing development highlights for Create IronWoven. This is a concise summary of notable changes, not a list of every internal commit.

## Unreleased — public beta preparation

- Batches A, B, and C passed their routine dedicated-server startup, disposable-world load, matching-client login, and log-review smoke tests.
- Batch D — Create Aeronautics Structures — remains partial because of a candidate-specific loot-table parsing error. Its non-English startup message is informational only and is not a blocker.
- Batch E performance testing has started. The first combined server smoke test passed, but no performance baseline was captured and the client-only rendering candidates still need separate client tests.
- Curios configuration now provides two Back slots and one Head slot in a new test world. The maintainer reports the Backpack + Backtank, Aviator Goggles, and Linked Typewriter checks working.
- More Curios Slots 1.4 was intentionally removed; craftable slot upgrades are not wanted.
- Distant Horizons 3.3.3 was reviewed and explicitly excluded by the maintainer.
- The public testing checklist was consolidated around current open work; historical evidence remains in private dated records.
- A full installed-mod functional test matrix now records 123 feature and support-module entries. Smoke-test success is explicitly separate from feature-function validation; the remaining checks are release gates.
- Remaining dedicated-server investigations include Struts client-class loading and PowerGrid's optional native solver.

## Release history

No public beta release has been published from this repository yet.
