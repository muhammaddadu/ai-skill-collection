#!/usr/bin/env node
/**
 * ffmpeg-usage — validation script
 * Confirms ffmpeg/ffprobe are present, probes capabilities, checks where the
 * skill is installed across agents, runs a quick smoke test, and writes a JSON
 * report. No dependencies beyond Node's standard library.
 */

'use strict';

const { spawnSync } = require('node:child_process');
const os = require('node:os');
const fs = require('node:fs');
const path = require('node:path');

const C = {
  green: '\x1b[92m', yellow: '\x1b[93m', red: '\x1b[91m',
  blue: '\x1b[94m', bold: '\x1b[1m', end: '\x1b[0m',
};
const ok    = (m) => console.log(`${C.green}✓${C.end} ${m}`);
const warn  = (m) => console.log(`${C.yellow}⚠${C.end} ${m}`);
const err   = (m) => console.log(`${C.red}✗${C.end} ${m}`);
const info  = (m) => console.log(`${C.blue}ℹ${C.end} ${m}`);
const title = (m) => console.log(`\n${C.bold}${m}${C.end}\n`);

/** Run a command, capturing stdout/stderr; never throws. */
function run(cmd, args, timeout = 5000) {
  const r = spawnSync(cmd, args, { encoding: 'utf8', timeout });
  return {
    ok: r.status === 0 && !r.error,
    notFound: r.error && r.error.code === 'ENOENT',
    timedOut: r.error && r.error.code === 'ETIMEDOUT',
    stdout: r.stdout || '',
    stderr: r.stderr || '',
  };
}

function header() {
  const bar = '='.repeat(50);
  console.log(`\n${C.blue}${C.bold}${bar}${C.end}`);
  console.log(`${C.blue}${C.bold}  ffmpeg-usage — system validation${C.end}`);
  console.log(`${C.blue}${C.bold}${bar}${C.end}`);
}

function checkFfmpeg() {
  const r = run('ffmpeg', ['-version']);
  if (r.notFound) { err('ffmpeg not found in PATH'); return false; }
  if (r.timedOut) { err('ffmpeg timed out'); return false; }
  if (!r.ok)      { err('ffmpeg command failed'); return false; }
  ok(`ffmpeg installed: ${r.stdout.split('\n')[0]}`);
  return true;
}

function checkFfprobe() {
  const r = run('ffprobe', ['-version']);
  if (r.ok) { ok('ffprobe installed'); return true; }
  warn('ffprobe not found (optional but recommended)');
  return false;
}

function checkCodecs() {
  const r = run('ffmpeg', ['-codecs']);
  if (!r.ok) { warn('Could not retrieve codec information'); return; }
  const have = r.stdout.toLowerCase();
  const codecs = {
    h264: 'H.264/AVC', hevc: 'H.265/HEVC', vp9: 'VP9', av1: 'AV1',
    aac: 'AAC', mp3: 'MP3', opus: 'Opus',
  };
  const found = [], missing = [];
  for (const [id, name] of Object.entries(codecs)) {
    (have.includes(id) ? found : missing).push(name);
  }
  info(`Supported codecs: ${found.join(', ')}`);
  if (missing.length) warn(`Missing codecs: ${missing.join(', ')}`);
}

function checkFormats() {
  const r = run('ffmpeg', ['-formats']);
  if (!r.ok) { warn('Could not retrieve format information'); return; }
  const have = r.stdout.toLowerCase();
  const found = ['mp4', 'webm', 'mov', 'avi', 'mkv', 'gif'].filter((f) => have.includes(f));
  info(`Supported formats: ${found.join(', ')}`);
}

function checkHwAccel() {
  const r = run('ffmpeg', ['-hwaccels']);
  if (!r.ok) return;
  const have = r.stdout.toLowerCase();
  const methods = {
    videotoolbox: 'VideoToolbox (macOS)', cuda: 'NVIDIA CUDA',
    qsv: 'Intel Quick Sync', vaapi: 'VA-API (Linux)',
    dxva2: 'DXVA2 (Windows)', d3d11va: 'Direct3D 11 (Windows)',
  };
  const found = Object.entries(methods).filter(([m]) => have.includes(m)).map(([, n]) => n);
  if (found.length) ok(`Hardware acceleration: ${found.join(', ')}`);
  else info('No hardware acceleration detected');
}

function systemInfo() {
  info(`Operating system: ${os.type()} ${os.release()}`);
  info(`Architecture: ${os.arch()}`);
  info(`Node: ${process.version}`);
}

/** Look for the skill across every agent the installer targets. */
function checkSkillInstallation() {
  const home = os.homedir();
  const targets = [
    { label: 'Claude Code', kind: 'dir',  p: path.join(home, '.claude', 'skills', 'ffmpeg-usage') },
    { label: 'Codex CLI',   kind: 'dir',  p: path.join(home, '.codex',  'skills', 'ffmpeg-usage') },
    { label: 'Cursor',      kind: 'file', p: path.join(home, '.cursor', 'rules', 'ffmpeg-usage.md') },
  ];
  let any = false;
  for (const t of targets) {
    if (!fs.existsSync(t.p)) continue;
    const file = t.kind === 'dir' ? path.join(t.p, 'SKILL.md') : t.p;
    if (!fs.existsSync(file)) { err(`${t.label}: SKILL.md missing at ${file}`); continue; }
    const size = fs.statSync(file).size;
    if (size > 0) { ok(`${t.label}: installed (${size.toLocaleString()} bytes)`); any = true; }
    else err(`${t.label}: SKILL.md is empty`);
  }
  if (!any) {
    warn('Skill not installed for any detected agent');
    info('Run ./install.sh to install it');
  }
  return any;
}

function suggestInstallation() {
  title('Installation instructions:');
  switch (os.platform()) {
    case 'darwin':
      console.log('macOS detected:\n  brew install ffmpeg'); break;
    case 'linux':
      console.log('Linux detected:');
      console.log('  Debian/Ubuntu: sudo apt-get install ffmpeg');
      console.log('  Fedora:        sudo dnf install ffmpeg');
      console.log('  Arch:          sudo pacman -S ffmpeg'); break;
    case 'win32':
      console.log('Windows detected:\n  choco install ffmpeg');
      console.log('  or download from https://ffmpeg.org/download.html'); break;
    default:
      console.log('Visit https://ffmpeg.org/download.html');
  }
}

function runTestCommand() {
  title('Running test command:');
  const r = run('ffmpeg', ['-f', 'lavfi', '-i', 'color=c=blue:s=320x240:d=1', '-f', 'null', '-'], 10000);
  if (r.timedOut) { err('Test command timed out'); return false; }
  if (!r.ok)      { err('Test command failed'); console.log(`  ${r.stderr.slice(0, 200)}`); return false; }
  ok('Test command executed successfully');
  return true;
}

function generateReport(results) {
  const report = {
    ffmpeg_installed: !!results.ffmpeg,
    ffprobe_installed: !!results.ffprobe,
    skill_installed: !!results.skill,
    test_passed: !!results.test,
    system: { os: os.type(), release: os.release(), architecture: os.arch() },
  };
  const file = path.join(process.cwd(), 'validation_report.json');
  fs.writeFileSync(file, JSON.stringify(report, null, 2));
  info(`Report saved to: ${file}`);
}

function main() {
  header();
  const results = {};

  title('System information:');
  systemInfo();

  title('ffmpeg installation:');
  results.ffmpeg = checkFfmpeg();
  if (!results.ffmpeg) {
    suggestInstallation();
    err('\nffmpeg validation failed');
    return 1;
  }

  results.ffprobe = checkFfprobe();

  title('ffmpeg capabilities:');
  checkCodecs();
  checkFormats();
  checkHwAccel();

  title('Skill installation:');
  results.skill = checkSkillInstallation();

  results.test = runTestCommand();

  console.log();
  generateReport(results);

  title('Validation summary:');
  const allOk = results.ffmpeg && results.skill && results.test;
  if (allOk) {
    ok('All checks passed! ✨');
    info("You're ready to use the ffmpeg-usage skill");
  } else {
    warn('Some checks failed');
    if (!results.skill) info('Install the skill with: ./install.sh');
  }
  console.log();
  return allOk ? 0 : 1;
}

try {
  process.exit(main());
} catch (e) {
  console.log(`\n${C.red}Unexpected error: ${e.message}${C.end}`);
  process.exit(1);
}
