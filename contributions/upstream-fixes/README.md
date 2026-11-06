# Upstream Compatibility Fix Contributions

This folder is a public technical handoff area for compatibility issues that may be useful to the maintainers of the original projects.

It contains short, source-focused explanations and minimal proposed changes. It is not an alternate distribution of any mod, does not contain modified JARs, and does not claim that any proposal has been accepted upstream.

## Privacy and publication scope

Only information needed for public technical review is included here. This folder intentionally excludes private project records, private repository links, local computer paths, local account or machine identifiers, private server or world names, save files, raw logs, screenshots, credentials, and private conversations.

The environment is described only at the general compatibility level: Minecraft 1.21.1, NeoForge 1.21.x, and Java 21. Each report links to the relevant public upstream source, issue, or pull request.

See [PRIVACY_REVIEW.md](PRIVACY_REVIEW.md) for the scope and limits of the content check.

## Contribution status

| Project | Public upstream reference | Status in this handoff |
|---|---|---|
| Strut Your Stuff | [Issue #6](https://github.com/cakeGit/StrutYourStuff/issues/6) | Minimal mixin-side proposal prepared; upstream build and runtime validation required |
| Create Kinetic | [Source repository](https://github.com/Lightning323/Create-Kinetic) | Minimal client-mixin placement proposal prepared; upstream build and runtime validation required |
| Copycats+ | [Issue #437](https://github.com/copycats-plus/copycats/issues/437), [PR #443](https://github.com/copycats-plus/copycats/pull/443) | Investigation only; previous PR closed without merging |
| Create: Design n' Decor | [Issue #139](https://github.com/DrMango14/Create-Design-n-Decor/issues/139), [PR #140](https://github.com/DrMango14/Create-Design-n-Decor/pull/140) | Investigation only; previous PR closed without merging and its approach should not be repeated |
| Steam 'n' Rails | [Issues #302](https://github.com/Porters-of-Railways/Railway-1.21.1/issues/302) and [#378](https://github.com/Porters-of-Railways/Railway-1.21.1/issues/378), [PR #393](https://github.com/Porters-of-Railways/Railway-1.21.1/pull/393) | Existing upstream work is open; review and support that work rather than duplicate it |
| Create Deco | [Issue #268](https://github.com/talrey/CreateDeco/issues/268), [PR #271](https://github.com/talrey/CreateDeco/pull/271) | Existing PR addresses the malformed white-dye ingredient; no duplicate proposal |

## How to use these notes

1. Read the relevant report before applying or adapting a proposal.
2. Confirm the target branch and source files have not changed since the report was prepared.
3. Run the upstream project's own build and tests.
4. Validate both dedicated-server and client behavior where relevant.
5. Discuss proposals in the existing upstream issue or pull request before creating overlapping work.

No proposal in this folder should be treated as an official upstream fix or a released mod update.
