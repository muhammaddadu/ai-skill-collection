# Processes & typed IPC

## The split

- **main** (`src/main/`): lifecycle, windows, all privileged I/O. Registers `ipcMain.handle` handlers.
- **preload** (`src/preload/`): the bridge. Imports the shared channel names + API type; exposes named methods via `contextBridge`.
- **renderer** (`src/renderer/`): UI. Calls `window.<api>.method()`. Imports from the shared module **type-only** (erased at build) — never at runtime, and never `fs`.

## One shared contract

Put channel names and the exposed API type in a single module imported by all three. This is the one-source-of-truth that stops the contract drifting.

```ts
// shared/ipc.ts
import type { Note } from '@app/core';

export const IPC = {
  readNote: 'vault:read-note',
  saveBlocks: 'vault:save-blocks',
} as const;

export interface VaultApi {
  readNote(path: string): Promise<Note>;
  saveBlocks(path: string, blocks: unknown[], baseHash: string): Promise<{ ok: boolean }>;
}
```

```ts
// preload/index.ts
import { contextBridge, ipcRenderer } from 'electron';
import { IPC, type VaultApi } from '../shared/ipc.js';

const api: VaultApi = {
  readNote: (path) => ipcRenderer.invoke(IPC.readNote, path),
  saveBlocks: (path, blocks, baseHash) => ipcRenderer.invoke(IPC.saveBlocks, path, blocks, baseHash),
};
contextBridge.exposeInMainWorld('vault', api);
```

```ts
// main/index.ts
ipcMain.handle(IPC.readNote, (_e, path: string) => core.readNote(path)); // validate input!
```

```ts
// renderer — window typing
import type { VaultApi } from '../../shared/ipc';
declare global {
  interface Window { vault: VaultApi }
}
```

## invoke vs. send vs. push

- **Request/response** (renderer needs a result): `ipcRenderer.invoke` ↔ `ipcMain.handle`. Prefer this.
- **Fire-and-forget** (renderer → main, no reply): `ipcRenderer.send` ↔ `ipcMain.on`.
- **Main → renderer push** (events, e.g. file changed, theme changed): `webContents.send(channel, payload)`; renderer subscribes via a preload-exposed `on…(cb)` that returns an unsubscribe:

```ts
// preload
onThemeChange: (cb: (t: 'light' | 'dark') => void) => {
  const h = (_e: unknown, t: 'light' | 'dark') => cb(t);
  ipcRenderer.on('app:theme', h);
  return () => ipcRenderer.removeListener('app:theme', h);
},
```

Return an unsubscribe function from every subscription so React effects can clean up.
