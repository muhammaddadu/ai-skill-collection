# Windows, menu, and the app name

## BrowserWindow essentials

```ts
const win = new BrowserWindow({
  width: 1160, height: 760, minWidth: 720, minHeight: 480,
  show: false,                       // show on 'ready-to-show' to avoid a flash
  backgroundColor: '#f6f1e7',        // matches theme; prevents white flash
  webPreferences: { preload, contextIsolation: true, nodeIntegration: false, sandbox: true },
});
win.once('ready-to-show', () => win.show());
```

For translucency / frameless title bars, see native-window-effects.md.

## The app name (fixing "Electron" in the menu / About / Quit)

On macOS the bold first menu item and the About/Hide/Quit labels come from the **app name**. In development the running binary is `Electron.app`, so it shows "Electron". Fix:

1. **Dev:** set the name before the app is ready, and install an explicit menu.

```ts
import { app, Menu } from 'electron';

app.setName('Second Brain'); // BEFORE app.whenReady()

function buildMenu() {
  const isMac = process.platform === 'darwin';
  const template: Electron.MenuItemConstructorOptions[] = [
    ...(isMac ? [{
      label: app.name, // ← now "Second Brain"
      submenu: [
        { role: 'about' }, { type: 'separator' },
        { role: 'hide' }, { role: 'hideOthers' }, { role: 'unhide' },
        { type: 'separator' }, { role: 'quit' },
      ],
    } as Electron.MenuItemConstructorOptions] : []),
    { role: 'fileMenu' },
    { role: 'editMenu' },
    { role: 'viewMenu' },
    { role: 'windowMenu' },
  ];
  Menu.setApplicationMenu(Menu.buildFromTemplate(template));
}
app.whenReady().then(buildMenu);
```

2. **Packaged:** the name comes from the bundle's `CFBundleName` → set `productName` in your packager config (see packaging.md). That's the durable fix across the OS (menu, Dock, About). `setName` only affects the running process in dev.

## Menu roles

Prefer built-in `role`s (`undo`, `copy`, `reload`, `toggleDevTools`, `minimize`, `close`, `about`, `quit`, or the composite `editMenu`/`viewMenu`/`windowMenu`) — they get correct labels, accelerators, and platform behavior for free. Add custom items with `accelerator` + `click` only where a role doesn't exist.

## Context menus

Build on demand in the renderer via a preload-exposed call, or in main with `menu.popup({ window })`. Keep actions wired to validated IPC, same as the rest of the app.
