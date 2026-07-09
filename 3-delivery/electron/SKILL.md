---
name: electron
description: "Build, secure, and package Electron desktop apps — main/preload/renderer split, contextIsolation-safe typed IPC over a preload bridge, BrowserWindow + application menu + app naming, a strict CSP, and distribution (electron-builder/Forge, productName, code signing). Use when building an Electron app, wiring IPC, hardening security, fixing the app/menu name, or packaging. Do NOT use for web-only React UI (use cleanui) or Expo/React Native."
type: component
domain: 3-delivery
tested_date: 2026-07-09
requires: "electron >= 28"
---

# Electron — desktop app architecture, security, and packaging

## Purpose

Produce a correct, secure, well-structured Electron app. This skill encodes the non-negotiables (process split, `contextIsolation`, sandbox, CSP, a narrow typed IPC bridge) and the boring-but-easy-to-get-wrong details (ESM preload paths, app/menu naming, packaging `productName`), so the result is safe by construction rather than retrofitted.

## When to use

- Scaffolding or reviewing an Electron app's main/preload/renderer layout.
- Exposing main-process capability to the renderer over IPC without breaking `contextIsolation`.
- Hardening security (the checklist below is the bar; treat any deviation as a bug).
- Fixing the macOS app/menu name showing as "Electron", or window titles.
- Packaging/distribution (`electron-builder` or Forge), icons, code signing, `productName`.

Do **not** use for: general web React UI/styling (`cleanui`), design-system lookups (`ui-design-system-search`), or Expo / React Native (those have their own skills).

## The architecture (one rule)

Three processes, one direction of trust:

- **Main** (Node): owns the app lifecycle, windows, and *all* privileged I/O (fs, DB, network, native). The only place with full Node access.
- **Preload** (isolated bridge): the *only* code that touches both worlds. Exposes a **narrow, explicit** API to the renderer via `contextBridge.exposeInMainWorld`. No raw `ipcRenderer`, no `require`, no `fs` leaked to the page.
- **Renderer** (web): your UI. Treat it as untrusted. It reaches the main process **only** through the preload bridge — never `nodeIntegration`, never direct fs.

Keep IPC channel names and the exposed API's TypeScript types in **one shared module** imported by main, preload, and (type-only) the renderer, so the contract can't drift. See `references/processes-and-ipc.md`.

## Security checklist (the bar — every item, every window)

Load `references/security.md` for rationale and code. The minimum:

- [ ] `contextIsolation: true` (default; never disable).
- [ ] `nodeIntegration: false` (default; never enable in a window that loads app/remote content).
- [ ] `sandbox: true` where possible (drop only when the preload genuinely needs Node built-ins, and know why).
- [ ] Preload exposes a **small, explicit** surface — specific functions, not `ipcRenderer` or whole modules.
- [ ] **Validate every IPC argument** in the main handler; treat renderer input as hostile. Never interpolate renderer strings into fs paths without containment checks.
- [ ] A strict **Content-Security-Policy** (no remote `script-src`, no `unsafe-eval`). Ship all assets locally.
- [ ] Block new-window/navigation to untrusted origins (`setWindowOpenHandler`, `will-navigate`).
- [ ] Don't load remote URLs as app UI; if you must show remote content, use a sandboxed `<webview>`/child window with its own isolation.
- [ ] Keep Electron **up to date** — security fixes land in majors/minors.

## Windows, menu, and the app name

`references/windows-menu-and-app-name.md` covers `BrowserWindow` options and the application menu. The most common gotcha:

- **macOS menu shows "Electron"** (or the wrong name): the bold first menu item and the About/Quit labels come from the app name. In **dev** the running binary is `Electron.app`, so:
  - Call `app.setName('Your App')` **before** `app.whenReady()`.
  - Build an explicit application `Menu` whose first submenu label is your app name (don't rely on the default template picking it up in dev).
  - For **packaged** builds the name comes from the bundle's `CFBundleName` — set `productName` in your packager config (electron-builder/Forge). That's the durable fix; `setName` covers dev.
- Set each window's `title` and a `backgroundColor` matching your theme to avoid a white flash on load.

## ESM / electron-vite gotchas

- With `"type": "module"`, electron-vite emits the **preload as `.mjs`** — reference it as `index.mjs` in `webPreferences.preload`, not `.js`.
- `__dirname`/`__filename` are shimmed by electron-vite for ESM main (`import.meta.dirname`), so `join(__dirname, ...)` works in the bundle.
- Load the renderer from `process.env.ELECTRON_RENDERER_URL` in dev, and `loadFile(.../renderer/index.html)` in production.

## Packaging

`references/packaging.md`: `electron-builder` vs. Forge, `productName`, icons per platform, code signing/notarization basics, and auto-update wiring. Packaging is usually deferred until the app works; when you do it, set `productName` (fixes the app name everywhere) and platform icons first.

## Workflow

1. Confirm the process split and that the security checklist holds — fix violations before adding features.
2. For any new renderer→main capability: add the channel + types to the shared IPC module, a validated handler in main, and one thin method on the preload bridge. Never widen the bridge to raw `ipcRenderer`.
3. For app-identity issues, apply the app-name fixes above (dev: `setName` + explicit menu; packaged: `productName`).
4. Verify by running the built app (e.g. Playwright `_electron`), not just unit tests.

## Attribution

Distilled and modernized (ESM/electron-vite, security-first, TypeScript) from the community `electron` skill at https://github.com/full-stack-skills/electron-skills — see `ATTRIBUTION.md`.
