# Create Deco — white-dye placard recipe ingredient
<!-- IRONWOVEN_CHRONOLOGY
{
  "record_id": "IRONWOVEN-BETA-UPSTREAM-CREATEDECO-0001",
  "record_type": "createdeco_placard_ingredient_status",
  "created_at": "unknown",
  "updated_at": "unknown",
  "verified_at": "2026-11-13T14:33:30Z",
  "migrated_at": "2026-11-13T14:33:30Z",
  "source_ref": [
    "Beta contributions/upstream-fixes/create-deco/UPSTREAM_STATUS.md — historical placard ingredient investigation. Issue #268 remains OPEN; PR #271 remains OPEN and unmerged; issue #282 remains OPEN with comments suggesting it may duplicate #268. Current 1.21-neo placard recipe blob ee37ff2bcafa3b1916b3ace59df5eada7bc4d7e2 still uses id for minecraft:white_dye. Historical local recipe/startup smoke evidence was not rerun."
  ],
  "timezone_display": "Europe/Amsterdam",
  "chronology_status": "HISTORICAL"
}
-->

**Upstream issue:** [talrey/CreateDeco #268](https://github.com/talrey/CreateDeco/issues/268)  
**Existing proposed correction:** [PR #271](https://github.com/talrey/CreateDeco/pull/271)  
**Relevant source:** [placard.json](https://github.com/talrey/CreateDeco/blob/1.21-neo/src/main/resources/data/createdeco/recipe/placard.json)

## Finding

The reported shapeless recipe encodes the white-dye ingredient with an `id` property where the ingredient codec expects an `item` property.

PR #271 already proposes the exact one-field correction from `id` to `item` for the white-dye ingredient. A related earlier PR #238 was merged, but the current open PR #271 covers the remaining malformed ingredient entry.

## Contribution decision

Do not create a duplicate issue or PR. Review and support the existing PR #271 if further evidence or validation is useful.

## Status

Existing upstream PR is open. This handoff contains no copied mod assets or binaries and does not claim that the correction has been merged or released.
