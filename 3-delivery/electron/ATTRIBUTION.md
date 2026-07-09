# Attribution

This skill was distilled and substantially rewritten from the community
`electron` skill in **full-stack-skills/electron-skills**
(https://github.com/full-stack-skills/electron-skills).

What was kept from the source: the topic map (main / renderer / preload / IPC /
BrowserWindow / menu / packaging / security) as the skeleton, and the intent of
its example set.

What was changed here: modernized to `contextIsolation`-safe, sandboxed,
TypeScript, ESM/electron-vite patterns; a security-first framing (the checklist
is the bar); a one-source-of-truth typed IPC contract; concrete app-name/menu
fixes; and a native-window-effects reference (macOS vibrancy, Windows Mica,
`nativeTheme` live theming, and reduced-transparency/motion accessibility) that
the source did not cover. The bilingual Chinese-doc references and the
`electron-egg` / `upgradeLink` framework skills from the source were dropped as
out of scope.

Upstream license: see the source repository. This adaptation is provided under
the same terms as the rest of this skills collection.
