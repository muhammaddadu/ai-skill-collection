# Electron security

Electron ships a full Node runtime next to a browser. A single XSS in the renderer becomes remote code execution on the user's machine unless the boundaries hold. Treat the renderer as untrusted, always.

## Window defaults (safe)

```ts
new BrowserWindow({
  webPreferences: {
    preload: join(__dirname, '../preload/index.mjs'), // .mjs under "type": "module" + electron-vite
    contextIsolation: true,   // default — isolate preload/page worlds
    nodeIntegration: false,   // default — no Node in the renderer
    sandbox: true,            // OS sandbox; drop only if preload needs Node built-ins
  },
});
```

Never set `nodeIntegration: true` or `contextIsolation: false` on a window that loads app or remote content. If a dependency "requires" it, isolate that content in its own window/webview instead.

## Preload: expose a narrow surface

Bad — leaks the whole IPC channel to the page:

```ts
contextBridge.exposeInMainWorld('ipc', ipcRenderer); // ❌ renderer can invoke anything
```

Good — specific, named operations only:

```ts
contextBridge.exposeInMainWorld('vault', {
  readNote: (path: string) => ipcRenderer.invoke('vault:read-note', path),
  saveBlocks: (path: string, blocks: unknown[], baseHash: string) =>
    ipcRenderer.invoke('vault:save-blocks', path, blocks, baseHash),
});
```

## Validate IPC input in main

The renderer can send anything. Validate types and contain paths before touching the filesystem:

```ts
ipcMain.handle('vault:read-note', (_e, path: unknown) => {
  if (typeof path !== 'string') throw new Error('bad path');
  const abs = resolve(vaultRoot, path);
  const rel = relative(vaultRoot, abs);
  if (rel.startsWith('..') || isAbsolute(rel)) throw new Error('path escapes vault');
  return readNote(abs);
});
```

## Content-Security-Policy

Ship a strict CSP (meta tag in the renderer HTML or via `onHeadersReceived`). No remote scripts, no `unsafe-eval`:

```html
<meta http-equiv="Content-Security-Policy"
  content="default-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; font-src 'self'; script-src 'self'" />
```

`style-src 'unsafe-inline'` is a pragmatic allowance for injected `<style>` (Vite/UI libs); avoid `unsafe-inline` for `script-src`.

## Navigation & new windows

```ts
window.webContents.setWindowOpenHandler(({ url }) => {
  // open external links in the OS browser, never a nodeful window
  if (url.startsWith('https:')) shell.openExternal(url);
  return { action: 'deny' };
});
window.webContents.on('will-navigate', (e, url) => {
  if (!url.startsWith(devServerOrigin)) e.preventDefault();
});
```

## Keep current

Track Electron releases; Chromium/Node CVEs are fixed in Electron majors/minors. Pin a supported major and upgrade regularly.
