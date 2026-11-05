# Create IronWoven versioning

**Current modpack version: `v0.1.000`**  
**Update counter: `000`**  
**Release state:** internal development; no public beta package has been published.

## Format

Use `vMAJOR.MINOR.UPDATE`, with the update component always three digits.

- `v0.1.000` — initial development baseline.
- `v0.1.001` — first accepted modpack content update.
- `v0.1.002` — second accepted modpack content update.
- `v0.1.010` — tenth accepted modpack content update.
- `v0.2.000` — deliberate move to the next minor development stage; reset the update counter.
- `v1.0.000` — first stable major release; reset the update counter.

## What counts as a modpack update

Increment the final three-digit counter by exactly one when an update is accepted into the actual modpack contents, such as:
- adding, removing, or updating a mod in the approved pack;
- changing an included pack manifest, config, datapack, or resource pack;
- another intentional content change that alters the distributed client/server pack.

Do **not** increment for:
- documentation, README, checklist, or GitHub workflow edits;
- research or compatibility checks;
- disposable test attempts, failed trials, or changes that are reverted before acceptance;
- candidate mods that are not accepted into the pack.

One accepted update event increments the counter once, even if several mods or files change together. Never count individual Git commits as modpack updates.

## Release and synchronization rules

1. Keep this file, the private project status, public README, public beta status, and public changelog synchronized.
2. When an accepted modpack update is made, increment the counter once and record the new version and concise contents summary in the public changelog.
3. Keep the same version on client and server packages built from the same pack state.
4. Do not advance the version merely because a test passed; acceptance into the pack is the trigger.
5. Before publishing, verify the version in the CurseForge manifest/package metadata and the server package metadata.

## Baseline accounting

The project records document development and test activity but do not establish a reliable count of previously accepted, distributed modpack updates. Therefore `v0.1.000` is the explicit versioning baseline from adoption of this scheme; earlier development/test changes are not retroactively counted as released updates.
