# Copycats+ — Sable Catwalk physics selector

**Upstream issue:** [copycats-plus/copycats #437](https://github.com/copycats-plus/copycats/issues/437)  
**Previous proposal:** [PR #443](https://github.com/copycats-plus/copycats/pull/443)  
**Relevant source files:** [copycat_catwalk.json](https://github.com/copycats-plus/copycats/blob/multiloader/common/src/main/resources/data/copycats/physics_block_properties/copycat_catwalk.json), [copycat_board.json](https://github.com/copycats-plus/copycats/blob/multiloader/common/src/main/resources/data/copycats/physics_block_properties/copycat_board.json)

## Finding

The Catwalk item is reported to place the registered `copycats:copycat_board` block, not a separate `copycats:copycat_catwalk` block. The current Catwalk physics resource selects `copycats:copycat_catwalk`, which Sable reports as an unknown block.

The existing Board physics resource already assigns mass and volume values of `0.25` to `copycats:copycat_board`.

## Existing upstream work

PR #443 proposed removing the Catwalk-specific physics resource and was closed without merging. The same deletion should not be resubmitted without first understanding the maintainer's reason for closing it.

## Suggested maintainer discussion

Confirm whether the Catwalk-specific resource is redundant because the item places the Board block, and whether removing it is the intended correction. If a distinct Catwalk physics identity is required, the implementation needs a different approach than selecting a non-registered block ID.

Do not change the shared Board mass or volume values as part of this investigation.

## Status

Investigation only. No replacement patch is proposed here, and no change is claimed as accepted or runtime-validated.
