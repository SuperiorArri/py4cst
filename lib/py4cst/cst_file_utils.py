from __future__ import annotations
import struct, zlib, binascii, pathlib
from dataclasses import dataclass
from typing import List, Dict, Optional
import json

SIG_LOCAL = b'DE\x03\x04'

@dataclass
class Entry:
    name: str
    content: bytes
    compression: int = 8 # 0: store, 8: deflate
    version: int = 20
    platform: int = 6 # 0 also seen on some entries
    unk1: int = 0 # unknown 32-bit field
    timestamp: int = 0 # DOS date/time

@dataclass
class Parameter:
    name: str
    expression: str
    description: Optional[str]
    value: str

@dataclass
class HistoryListItem:
    caption: str
    code: str
    type: str
    hidden: bool
    version: str


def decode(path: str, verify: bool = True) -> Dict[str, Entry]:
    blob = pathlib.Path(path).read_bytes()
    entries: Dict[str, Entry] = {}
    pos = 0

    while True:
        j = blob.find(SIG_LOCAL, pos)
        if j == -1:
            break

        p = j + 4
        if p + 30 > len(blob):
            break
        ver, = struct.unpack_from('<H', blob, p); p += 2
        platform, = struct.unpack_from('<H', blob, p); p += 2
        comp, = struct.unpack_from('<H', blob, p); p += 2
        unk1, = struct.unpack_from('<I', blob, p); p += 4
        ts, = struct.unpack_from('<I', blob, p); p += 4
        crc_hdr, = struct.unpack_from('<I', blob, p); p += 4
        csize, = struct.unpack_from('<I', blob, p); p += 4
        usize_hdr, = struct.unpack_from('<I', blob, p); p += 4
        name_len, = struct.unpack_from('<I', blob, p); p += 4
        name = blob[p:p+name_len].decode('utf-8', errors='ignore'); p += name_len
        filedata = blob[p:p+csize]

        if len(filedata) != csize:
            raise ValueError(
                f'{name}: truncated/overflow data (expected {csize}, got {len(filedata)})')
        try:
            content = _decompress(comp, filedata)
        except Exception as e:
            raise ValueError(f'{name}: decompress failed: {e}')

        if verify:
            _verify_entry(name, content, usize_hdr, crc_hdr)

        entries[name] = Entry(
            name=name, content=content, compression=comp,
            version=ver, platform=platform, unk1=unk1, timestamp=ts
        )

        pos = p + csize

    if not entries:
        raise ValueError('No entries found; not a recognized CST container.')

    return entries


def get_parameters(decoded_file: Dict[str, Entry]) -> List[Parameter]:
    jp = json.loads(decoded_file['Model/Parameters.json'].content)
    params = []
    for jitem in jp['parameters']:
        name = jitem['name']
        expression = jitem['expr'] if 'expr' in jitem else ''
        description = jitem['descr'] if 'descr' in jitem else None
        value = jitem['value']
        params.append(Parameter(name, expression, description, value))
    return params


def get_history_list(decoded_file: Dict[str, Entry]) -> List[HistoryListItem]:
    jhl = json.loads(decoded_file['Model/3D/ModelHistory.json'].content)
    history_list = []
    for jitem in jhl['history']:
        if not jitem['hidden'] and jitem['type'] == 'vba':
            caption = jitem['caption']
            code = '\n'.join(jitem['code'])
            kind = jitem['type']
            hidden = jitem['hidden']
            version = jitem['version']
            history_list.append(HistoryListItem(caption, code, kind, hidden, version))
    return history_list


def _decompress(comp: int, raw: bytes) -> bytes:
    if comp == 0:
        return raw
    if comp == 8:
        try:
            return zlib.decompress(raw)
        except Exception:
            return zlib.decompress(raw, -15)
    raise ValueError(f'Unsupported compression method {comp}')


def _verify_entry(name: str, content: bytes, usize_hdr: int, crc_hdr: int) -> None:
    if usize_hdr != len(content):
        raise ValueError(f'{name}: size mismatch (header {usize_hdr} vs actual {len(content)})')
    crc_calc = binascii.crc32(content) & 0xFFFFFFFF
    if crc_hdr != crc_calc:
        raise ValueError(f'{name}: CRC32 mismatch (header 0x{crc_hdr:08X} vs calc 0x{crc_calc:08X})')
