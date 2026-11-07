# Steam 'n' Rails — optional compatibility track loot tables

**Public upstream reports:** [Issue #302](https://github.com/Porters-of-Railways/Railway-1.21.1/issues/302), [Issue #378](https://github.com/Porters-of-Railways/Railway-1.21.1/issues/378)  
**Existing upstream proposals:** [PR #339](https://github.com/Porters-of-Railways/Railway-1.21.1/pull/339), [PR #393](https://github.com/Porters-of-Railways/Railway-1.21.1/pull/393)

## Finding

The public reports describe optional compatibility track loot tables that reference items not registered when their companion wood/content mod is absent. They also identify an ineffective root-level `conditions` structure. NeoForge data conditions need to use the `neoforge:conditions` key and the appropriate condition object schema.

PR #339 addresses mod-ID prefix matching for underscore-containing IDs, but its discussion identifies that the condition schema in that proposal is still incorrect.

PR #393 is a later, broader data-generation proposal that changes the generated condition structure and should be reviewed as the primary existing upstream work.

## Contribution decision

Do not open a duplicate PR while #393 remains open. Review the current PR and provide a focused technical comment only if a concrete gap remains after checking its latest diff and target branch.

## Status

Existing upstream work is open. This page records the public handoff only; it does not claim that the PR has merged or that the defect is resolved in a released file.
