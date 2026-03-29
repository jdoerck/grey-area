// LZW encoder for GIF (LSB-first bit packing, min code size 2)
function lzwEncode(indices, minCodeSize) {
  const clearCode = 1 << minCodeSize;
  const eoiCode = clearCode + 1;
  const bytes = [];
  let bitBuffer = 0, bitsInBuffer = 0;
  let codeSize = minCodeSize + 1;
  let nextCode = eoiCode + 1;
  const table = new Map();

  const resetTable = () => {
    table.clear();
    for (let i = 0; i < clearCode; i++) table.set(`${i}`, i);
    codeSize = minCodeSize + 1;
    nextCode = eoiCode + 1;
  };

  const emit = (code) => {
    bitBuffer |= code << bitsInBuffer;
    bitsInBuffer += codeSize;
    while (bitsInBuffer >= 8) {
      bytes.push(bitBuffer & 0xFF);
      bitBuffer >>>= 8;
      bitsInBuffer -= 8;
    }
  };

  resetTable();
  emit(clearCode);

  let buf = `${indices[0]}`;
  for (let i = 1; i < indices.length; i++) {
    const combined = `${buf}|${indices[i]}`;
    if (table.has(combined)) {
      buf = combined;
    } else {
      emit(table.get(buf));
      if (nextCode <= 4095) {
        table.set(combined, nextCode++);
        if (nextCode > (1 << codeSize) && codeSize < 12) codeSize++;
      } else {
        emit(clearCode);
        resetTable();
      }
      buf = `${indices[i]}`;
    }
  }
  emit(table.get(buf));
  emit(eoiCode);
  if (bitsInBuffer > 0) bytes.push(bitBuffer & 0xFF);
  return bytes;
}

// Encode a B&W pixel array as a GIF file.
// indices: array/Uint8Array of 0 (white) or 1 (black), row-major order.
export function encodeGIF(width, height, indices) {
  const b = [];
  const u16 = (v) => [v & 0xFF, (v >> 8) & 0xFF];

  b.push(0x47, 0x49, 0x46, 0x38, 0x39, 0x61);             // Header: GIF89a
  b.push(...u16(width), ...u16(height), 0x80, 0x00, 0x00); // Screen descriptor (2-color gct)
  b.push(0xFF, 0xFF, 0xFF, 0x00, 0x00, 0x00);              // GCT: white=0, black=1
  b.push(0x2C, ...u16(0), ...u16(0), ...u16(width), ...u16(height), 0x00); // Image descriptor

  const minCodeSize = 2;
  b.push(minCodeSize);
  const lzw = lzwEncode(indices, minCodeSize);
  for (let i = 0; i < lzw.length; i += 255) {
    const chunk = lzw.slice(i, Math.min(i + 255, lzw.length));
    b.push(chunk.length, ...chunk);
  }
  b.push(0x00, 0x3B); // block terminator + trailer

  return new Uint8Array(b);
}

// Browser-only: render an SVG string to a GIF Uint8Array via canvas.
export async function svgToGIF(svgString) {
  const blob = new Blob([svgString], { type: 'image/svg+xml' });
  const url = URL.createObjectURL(blob);

  const img = await new Promise((resolve, reject) => {
    const el = new Image();
    el.onload = () => resolve(el);
    el.onerror = reject;
    el.src = url;
  });
  URL.revokeObjectURL(url);

  const { naturalWidth: w, naturalHeight: h } = img;
  const canvas = Object.assign(document.createElement('canvas'), { width: w, height: h });
  const ctx = canvas.getContext('2d');
  ctx.fillStyle = '#fff';
  ctx.fillRect(0, 0, w, h);
  ctx.drawImage(img, 0, 0);

  const { data } = ctx.getImageData(0, 0, w, h);
  const indices = new Uint8Array(w * h);
  for (let i = 0; i < w * h; i++) {
    indices[i] = data[i * 4] < 128 ? 1 : 0; // threshold red channel
  }

  return encodeGIF(w, h, indices);
}
