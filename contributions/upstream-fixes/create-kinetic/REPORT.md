# Create Kinetic — client-only Minecraft mixin placement

**Target source branch:** `main_aeronautics_1.21.1`  
**Target:** Minecraft 1.21.1 / NeoForge / Java 21  
**Relevant source:** [createkinetic.mixins.json](https://github.com/Lightning323/Create-Kinetic/blob/main_aeronautics_1.21.1/src/main/resources/createkinetic.mixins.json), [MinecraftMixin.java](https://github.com/Lightning323/Create-Kinetic/blob/main_aeronautics_1.21.1/src/main/java/org/lightning323/createkinetic/mixin/client/MinecraftMixin.java)

## Problem

The source class `client.MinecraftMixin` is annotated with `@Mixin(Minecraft.class)` and imports `net.minecraft.client.Minecraft`. It is therefore a client-only mixin.

The current mixin configuration places `client.MinecraftMixin` in the common `mixins` array, while the same configuration already has a separate `client` array for client-only mixins. A dedicated server can consequently attempt to load a client class.

## Proposed minimal change

Move only `client.MinecraftMixin` from the common `mixins` array into the existing `client` array. Leave all other mixin entries unchanged.

The proposed diff is in [createkinetic.mixins.json.patch](createkinetic.mixins.json.patch).

## Validation requested

- Build the target 1.21.1 source branch.
- Start a dedicated server and verify there is no invalid-distribution error or missing target for `net.minecraft.client.Minecraft`.
- Join with a matching client.
- Test the client behavior that uses the mixin, including joystick screen handling.

## Status and scope

This is a source-level proposal based on the current public branch. It has not been built or runtime-tested in the upstream project. It does not include a modified JAR or claim that the defect is fixed.

The proposed change is deliberately limited to the single client-only mixin entry.
