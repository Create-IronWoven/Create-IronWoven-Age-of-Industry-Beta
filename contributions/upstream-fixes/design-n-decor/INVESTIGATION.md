# Create: Design n' Decor — optional Dye Depot loot tables

**Upstream issue:** [DrMango14/Create-Design-n-Decor #139](https://github.com/DrMango14/Create-Design-n-Decor/issues/139)  
**Previous proposal:** [PR #140](https://github.com/DrMango14/Create-Design-n-Decor/pull/140)  
**Relevant source area:** [generated block loot tables](https://github.com/DrMango14/Create-Design-n-Decor/tree/1.21.1/src/generated/resources/data/dndecor/loot_table/blocks)

## Finding

Issue #139 reports that optional Dye Depot-dependent blocks are not registered when Dye Depot is absent, while generated block loot tables referencing those blocks are still loaded. The issue reports 256 affected loot tables.

## Why no replacement patch is included

PR #140 attempted to add conditions to generated loot-table JSON after data generation by using an additional Gradle post-processing task. The PR was closed without merging, and a public comment on the PR described that implementation approach as poor.

Repeating the same post-processing design or republishing the same generated-resource changes would not be a constructive contribution.

## Work needed before proposing a correction

- Trace the native loot-table data-generation path for these blocks.
- Identify where optional Dye Depot registration is represented in the source providers.
- Determine whether the loot-table provider can emit the appropriate NeoForge load condition directly.
- Confirm the generated output is correct when Dye Depot is both present and absent.
- Ask the maintainers which source-level approach they prefer before opening another PR.

## Asset and source scope

This handoff contains no copied textures, models, generated loot-table assets, or mod binaries. It links to public source locations only.

## Status

Investigation only. No replacement patch is proposed and no fix is claimed.
