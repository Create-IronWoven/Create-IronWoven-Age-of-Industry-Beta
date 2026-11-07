# Create Deco — white-dye placard recipe ingredient

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
