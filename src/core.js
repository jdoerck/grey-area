export const BYTE_ROWS = 2;
export const BYTE_SIZE = 10;
export const BYTE_LENGTH = 7;
export const WORD_CONSTANT = 3;

export function textToBinary(text) {
  return Array.from(new TextEncoder().encode(text))
    .map(b => b.toString(2))
    .join('');
}

function defineClass(bit) {
  return bit === '0' ? 'st0' : 'st1';
}

function svgHeader(w, h) {
  w = w * 10;
  h = h + 30;
  return (
    `<?xml version="1.0" encoding="utf-8"?>\n` +
    `<svg version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg"\n` +
    `    xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"\n` +
    `    width="${w}" height="${h}" viewBox="0 0 ${w} ${h}" xml:space="preserve">\n` +
    `<style type="text/css">\n` +
    `    .st0{fill:#FFFFFF;padding:0;margin:0;border:0;stroke:0}\n` +
    `    .st1{padding:0;margin:0;border:0;stroke:0}\n` +
    `</style>`
  );
}

export function buildSvg(text) {
  let data = textToBinary(text);
  const originalLen = data.length;
  while (data.length % 9 !== 0) data = ' ' + data;

  const letterSize = BYTE_SIZE * WORD_CONSTANT;
  const rowLength = BYTE_ROWS * BYTE_LENGTH;
  const b = originalLen - BYTE_LENGTH;

  const offsets = [
    [0, 0],  [10, 0],  [20, 0],
    [0, 10], [10, 10], [20, 10],
    [0, 20], [10, 20], [20, 20],
  ];

  let x = 0, y = 0, col = 0;
  const parts = [];

  for (let z = 0; z < b; z++) {
    for (let idx = 0; idx < 9; idx++) {
      const [dx, dy] = offsets[idx];
      const css = defineClass(data[z + idx]);
      parts.push(`<rect x="${x + dx}" y="${y + dy}" class="${css}" width="${BYTE_SIZE}" height="${BYTE_SIZE}"/>`);
    }
    x += letterSize;
    if (++col === rowLength) {
      col = 0;
      x = 0;
      y += letterSize;
    }
  }

  return svgHeader(rowLength * WORD_CONSTANT, y) + '\n' + parts.join('\n') + '\n</svg>';
}
