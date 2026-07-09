# Packaging & distribution

Package only once the app runs correctly. Two mainstream tools:

- **electron-builder** — config-driven, batteries included (installers, auto-update, signing). Good default.
- **Electron Forge** — plugin-driven, integrates with Vite/Webpack templates.

## productName is the app name everywhere

The packaged app's display name (window, macOS menu bar, About/Quit, installer) comes from **`productName`**, not the npm `name`. Set it once:

```jsonc
// package.json (electron-builder reads productName here)
{
  "name": "app",              // npm package id — kebab, no spaces
  "productName": "Second Brain", // user-facing app name (may contain spaces)
  "build": {
    "appId": "com.example.secondbrain",
    "mac":   { "icon": "build/icon.icns", "category": "public.app-category.productivity" },
    "win":   { "icon": "build/icon.ico" },
    "linux": { "icon": "build/icon.png", "category": "Utility" }
  }
}
```

In **dev** the running binary is `Electron.app`, so also `app.setName('Second Brain')` before `app.whenReady()` and build an explicit menu (see windows-menu-and-app-name.md). `productName` fixes packaged builds; `setName` fixes dev.

## Icons

Provide per-platform icons: `.icns` (macOS), `.ico` (Windows), `.png` (Linux). Generate from a single 1024×1024 source.

## Code signing / notarization

- **macOS:** sign with a Developer ID cert and **notarize** (`afterSign` hook / `notarize` config), or Gatekeeper blocks the app. Set `hardenedRuntime: true`.
- **Windows:** sign with an Authenticode cert to avoid SmartScreen warnings.
- Keep signing creds in CI secrets, never in the repo.

## Auto-update

`electron-updater` (with electron-builder) checks a release feed and applies updates. Gate rollout and verify signatures. Wire this after the app is otherwise shippable.
