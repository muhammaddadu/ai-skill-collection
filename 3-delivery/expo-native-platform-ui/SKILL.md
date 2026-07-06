---
name: expo-native-platform-ui
description: "Use native platform views in Expo apps via @expo/ui — SwiftUI views and modifiers on iOS (`@expo/ui/swift-ui`) and Jetpack Compose views and modifiers on Android (`@expo/ui/jetpack-compose`). Use when rendering true native platform UI (Host, VStack, Column, LazyColumn, native modifiers) from React in an Expo app."
---

# Expo Native Platform UI (@expo/ui)

The `@expo/ui` package lets you render true native platform views — SwiftUI on iOS, Jetpack Compose on Android — directly from your Expo app. Pick the section for the platform you're targeting.

> The instructions in this skill apply to SDK 55 only. For other SDK versions, refer to the Expo UI docs for that version for the most accurate information.

## Installation (both platforms)

```bash
npx expo install @expo/ui
```

A native rebuild is required after installation (`npx expo run:ios` / `npx expo run:android`).

## iOS — SwiftUI (`@expo/ui/swift-ui`)

### Instructions

- Expo UI's API mirrors SwiftUI's API. Use SwiftUI knowledge to decide which components or modifiers to use.
- Components are imported from `@expo/ui/swift-ui`, modifiers from `@expo/ui/swift-ui/modifiers`.
- When about to use a component, fetch its docs to confirm the API - https://docs.expo.dev/versions/v55.0.0/sdk/ui/swift-ui/{component-name}/index.md
- When unsure about a modifier's API, refer to the docs - https://docs.expo.dev/versions/v55.0.0/sdk/ui/swift-ui/modifiers/index.md
- Every SwiftUI tree must be wrapped in `Host`.
- `RNHostView` is specifically for embedding RN components inside a SwiftUI tree. Example:

```jsx
import { Host, VStack, RNHostView } from "@expo-ui/swift-ui";
import { Pressable } from "react-native";

<Host matchContents>
  <VStack>
    <RNHostView matchContents>
      // Here, `Pressable` is an RN component so it is wrapped in `RNHostView`.
      <Pressable />
    </RNHostView>
  </VStack>
</Host>;
```

- If a required modifier or View is missing in Expo UI, it can be extended via a local Expo module. See: https://docs.expo.dev/guides/expo-ui-swift-ui/extending/index.md. Confirm with the user before extending.

## Android — Jetpack Compose (`@expo/ui/jetpack-compose`)

### Instructions

- Expo UI's API mirrors Jetpack Compose's API. Use Jetpack Compose and Material Design 3 knowledge to decide which components or modifiers to use. If you need deeper Jetpack Compose or Material 3 guidance (e.g. which component to pick, layout patterns, theming), spawn a subagent to research [Jetpack Compose](https://developer.android.com/develop/ui/compose/components) and [Material Design 3](https://m3.material.io/) best practices.
- Components are imported from `@expo/ui/jetpack-compose`, modifiers from `@expo/ui/jetpack-compose/modifiers`.
- **Always read the `.d.ts` type files** to confirm the exact API before using a component or modifier. Run `node -e "console.log(path.dirname(require.resolve('@expo/ui/jetpack-compose')))"` to locate the package, then read the relevant `{ComponentName}/index.d.ts` files. This is the most reliable source of truth.
- When about to use a component, fetch its docs to confirm the API - https://docs.expo.dev/versions/v55.0.0/sdk/ui/jetpack-compose/{component-name}/index.md
- When unsure about a modifier's API, refer to the docs - https://docs.expo.dev/versions/v55.0.0/sdk/ui/jetpack-compose/modifiers/index.md
- Every Jetpack Compose tree must be wrapped in `Host`. Use `<Host matchContents>` for intrinsic sizing, or `<Host style={{ flex: 1 }}>` when you need explicit size (e.g. as a parent of `LazyColumn`). Example:

```jsx
import { Host, Column, Button, Text } from "@expo/ui/jetpack-compose";
import { fillMaxWidth, paddingAll } from "@expo/ui/jetpack-compose/modifiers";

<Host matchContents>
  <Column verticalArrangement={{ spacedBy: 8 }} modifiers={[fillMaxWidth(), paddingAll(16)]}>
    <Text style={{ typography: "titleLarge" }}>Hello</Text>
    <Button onPress={() => alert("Pressed!")}>Press me</Button>
  </Column>
</Host>;
```

### Key Components

- **LazyColumn** — Use instead of react-native `ScrollView`/`FlatList` for scrollable lists. Wrap in `<Host style={{ flex: 1 }}>`.
- **Icon** — Use `<Icon source={require('./icon.xml')} size={24} />` with Android XML vector drawables. To get icons: go to [Material Symbols](https://fonts.google.com/icons), select an icon, choose the Android platform, and download the XML vector drawable. Save these as `.xml` files in your project's `assets/` directory (e.g. `assets/icons/wifi.xml`). Metro bundles `.xml` assets automatically — no metro config changes needed.
