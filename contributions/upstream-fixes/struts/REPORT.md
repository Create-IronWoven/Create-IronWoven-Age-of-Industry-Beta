# Strut Your Stuff — dedicated-server mixin side
<!-- IRONWOVEN_CHRONOLOGY
{
  "record_id": "IRONWOVEN-BETA-UPSTREAM-STRUTS-0001",
  "record_type": "struts_dedicated_server_client_mixin_report",
  "created_at": "unknown",
  "updated_at": "unknown",
  "verified_at": "2026-11-13T14:33:30Z",
  "migrated_at": "2026-11-13T14:33:30Z",
  "source_ref": [
    "Beta contributions/upstream-fixes/struts/REPORT.md — historical dedicated-server mixin report. Existing issue #6 remains OPEN; current struts.mixins.json blob 2df756d36229dbda10de40ab0846538df33c68ae still lists StrutRenderSystemAccessor in common mixins and the accessor class targets RenderSystem. Historical local patch smoke evidence was not rerun."
  ],
  "timezone_display": "Europe/Amsterdam",
  "chronology_status": "HISTORICAL"
}
-->

**Target:** Minecraft 1.21.1 / NeoForge / Java 21  
**Upstream issue:** [cakeGit/StrutYourStuff #6](https://github.com/cakeGit/StrutYourStuff/issues/6)  
**Relevant source:** [struts.mixins.json](https://github.com/cakeGit/StrutYourStuff/blob/main/src/main/resources/struts.mixins.json), [StrutRenderSystemAccessor.java](https://github.com/cakeGit/StrutYourStuff/blob/main/src/main/java/com/cake/struts/mixin/StrutRenderSystemAccessor.java)

## Problem

The existing report describes a dedicated-server attempt to load the client-only class `com.mojang.blaze3d.systems.RenderSystem`, followed by a Mixin target-not-found message for `StrutRenderSystemAccessor`.

The upstream accessor is annotated with `@Mixin(RenderSystem.class)`. The current mixin configuration lists `StrutRenderSystemAccessor` in the common `mixins` array, so it is eligible for loading on a dedicated server.

## Proposed minimal change

Move only `StrutRenderSystemAccessor` from the common `mixins` array into the Mixin configuration's `client` array.

Keep these Create integration mixins in the common list:

- `compat.create.StrutTransformCompat`
- `compat.create.StrutWrenchCompat`

The proposed diff is in [struts.mixins.json.patch](struts.mixins.json.patch).

## Validation requested

- Build the upstream 1.21.1 NeoForge source.
- Start a dedicated server and confirm the Struts RenderSystem invalid-distribution and missing-target errors are absent.
- Join with a matching client.
- Confirm Strut rendering still works on the client.
- Confirm both Create compatibility mixins remain active.

## Status and scope

This is a source-level proposal based on the public upstream source and existing issue. The proposal has not been built or runtime-tested in the upstream project. It does not include a patched JAR or claim that the defect is fixed.

No duplicate issue is proposed; use the existing upstream issue #6 for discussion.
