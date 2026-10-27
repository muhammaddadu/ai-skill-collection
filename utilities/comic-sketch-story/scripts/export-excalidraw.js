#!/usr/bin/env node
// Write a .excalidraw file from a comic-sketch-story page without a browser.
// Usage: node export-excalidraw.js <page.html> <out.excalidraw>
// It runs the page's own inline script against a stub DOM. Shape recording does not depend on
// rough.js, so the stub falls back to plain shapes and the element list matches the browser's.
const fs = require('fs');

const [, , src, out] = process.argv;
if (!src || !out) {
  console.error('Usage: node export-excalidraw.js <page.html> <out.excalidraw>');
  process.exit(1);
}
const html = fs.readFileSync(src, 'utf8');
const blocks = html.split('<script>').slice(1).map((b) => b.split('</script>')[0]);
if (!blocks.length) {
  console.error('No inline <script> found in ' + src);
  process.exit(1);
}

function stub() {
  return { setAttribute() {}, appendChild() {}, addEventListener() {}, set innerHTML(v) {}, style: {} };
}
global.window = {};
global.document = { createElementNS: stub, getElementById: stub };
global.navigator = {};
blocks.forEach((code) => eval(code));

if (typeof window.__excalidrawFile !== 'function') {
  console.error('The page does not expose window.__excalidrawFile; is it built from assets/template.html?');
  process.exit(1);
}
const file = window.__excalidrawFile();
fs.writeFileSync(out, JSON.stringify(file, null, 1));
const counts = file.elements.reduce((a, e) => ((a[e.type] = (a[e.type] || 0) + 1), a), {});
console.log(`${out}: ${file.elements.length} elements`, counts);
