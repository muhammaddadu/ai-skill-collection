# Native window effects & adaptive theming

Make an Electron app feel native: OS-appropriate translucency (macOS vibrancy, Windows Mica/Acrylic), automatic light/dark that tracks the system, and respect for accessibility (reduced transparency, reduced motion). Everything degrades gracefully to a clean opaque surface where an effect isn't available.

## Window creation (per platform)

```ts
import { BrowserWindow, nativeTheme } from 'electron';

const isMac = process.platform === 'darwin';
const isWin = process.platform === 'win32';

const win = new BrowserWindow({
  width: 1160,
  height: 760,
  show: false,
  // Backfills before the page paints so there's no white flash and the frame matches the theme.
  backgroundColor: nativeTheme.shouldUseDarkColors ? '#1a1815' : '#f6f1e7',

  // macOS: translucent "glass" behind the whole window + inset traffic lights.
  ...(isMac ? {
    vibrancy: 'sidebar',              // 'sidebar' | 'under-window' | 'fullscreen-ui' | 'menu' …
    visualEffectState: 'followWindow',
    titleBarStyle: 'hiddenInset',     // native traffic lights over your content
    trafficLightPosition: { x: 16, y: 18 },
  } : {}),

  // Windows 11: Mica/Acrylic material. Requires frame tweaks; falls back cleanly on Win10.
  ...(isWin ? {
    backgroundMaterial: 'mica',       // 'mica' | 'acrylic' | 'tabbed' | 'none'
    titleBarStyle: 'hidden',
    titleBarOverlay: { color: '#00000000', symbolColor: nativeTheme.shouldUseDarkColors ? '#ddd' : '#333' },
  } : {}),

  webPreferences: { preload, contextIsolation: true, nodeIntegration: false, sandbox: true },
});
```

Notes:
- **Transparency for vibrancy:** on macOS the effect shows through the *window background*; keep the renderer's root background transparent (or semi-transparent) where you want glass, opaque where you don't. Don't paint a fully opaque body over the whole window or you'll hide the vibrancy.
- **Windows `backgroundMaterial`** needs a frameless/hidden title bar to look right and is a no-op on unsupported OS versions — the `backgroundColor` shows instead (graceful fallback).
- **Linux / unsupported:** neither branch runs; the opaque `backgroundColor` + your CSS tokens are the whole look. That's the intended fallback, not a bug.

## Track the system theme live

`nativeTheme` is the source of truth; push changes to the renderer so CSS updates without a reload.

```ts
function currentTheme() {
  return nativeTheme.shouldUseDarkColors ? 'dark' : 'light';
}
nativeTheme.on('updated', () => {
  for (const w of BrowserWindow.getAllWindows()) w.webContents.send('app:theme', currentTheme());
});
// expose currentTheme() via an IPC handler the renderer reads on mount, plus the push above.
```

Renderer stamps the theme on the root so CSS variables switch:

```ts
window.app.onThemeChange((t) => document.documentElement.dataset.theme = t);
window.app.theme().then((t) => document.documentElement.dataset.theme = t);
```

## Accessibility: reduced transparency & motion

Honor the OS settings. In CSS, gate the translucency and animation:

```css
:root { --sidebar-bg: color-mix(in srgb, var(--surface) 72%, transparent); }

/* Opaque when the user (or platform) asks for reduced transparency. */
@media (prefers-reduced-transparency: reduce) {
  :root { --sidebar-bg: var(--surface); }
}
@media (prefers-reduced-motion: reduce) {
  * { animation: none !important; transition: none !important; }
}
```

On macOS you can also read `nativeTheme.prefersReducedTransparency` in main and, if set, create the window **without** `vibrancy` (so the OS effect itself is off, not just the CSS). Combine: main disables the native effect; CSS disables the fake translucency. Both paths land on the opaque fallback.

## Draggable regions (frameless / hidden title bar)

With a hidden title bar you must declare drag regions yourself, and mark interactive elements as no-drag:

```css
.titlebar, .sidebar-header { -webkit-app-region: drag; }
button, input, a, .no-drag { -webkit-app-region: no-drag; }
```

Leave room for the macOS traffic lights (top-left) in your header padding so buttons don't collide with them.

## Theme tokens

Drive everything from CSS variables keyed on `:root[data-theme="…"]` (or `@media (prefers-color-scheme)` as the default), so the same components work in light, dark, translucent, and opaque modes. Semi-transparent surfaces should use `color-mix(... transparent)` so they read correctly over both the vibrancy and the opaque fallback.
