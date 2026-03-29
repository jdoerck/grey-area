#!/usr/bin/env node
import { buildSvg } from './core.js';
import { readFileSync, writeFileSync, mkdirSync } from 'fs';
import { join } from 'path';

function getInput() {
  const args = process.argv.slice(2);
  if (args.length === 0) {
    process.stdout.write('Enter text to convert: ');
    return readFileSync('/dev/stdin', 'utf8').trim();
  }
  const arg = args.join(' ');
  try {
    return readFileSync(arg, 'utf8');
  } catch {
    return arg;
  }
}

const raw = getInput();
const svgContent = buildSvg(raw);

const outputDir = join(process.cwd(), 'output');
mkdirSync(outputDir, { recursive: true });

const timestamp = new Date().toISOString().replace(/\D/g, '').slice(0, 14);
const slug = raw.slice(0, 10).replace(/\s+/g, '_');
const filename = join(outputDir, `${timestamp}-${slug}.svg`);

writeFileSync(filename, svgContent);
console.log(`Created: ${filename}`);
