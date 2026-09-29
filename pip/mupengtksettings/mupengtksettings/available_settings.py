"""Discover installed mupen64plus plugins across common Linux plugin dirs."""

import os
import re
from pathlib import Path


PLUGIN_DIRS = (
    '/usr/lib/mupen64plus',
    '/usr/lib64/mupen64plus',
    '/usr/lib/x86_64-linux-gnu/mupen64plus',
    '/usr/lib/aarch64-linux-gnu/mupen64plus',
    '/usr/local/lib/mupen64plus',
    '/usr/local/lib64/mupen64plus',
    '/usr/local/lib/x86_64-linux-gnu/mupen64plus',
)

_KIND_PATTERNS = {
    'video': re.compile(r'video', re.IGNORECASE),
    'audio': re.compile(r'audio', re.IGNORECASE),
    'input': re.compile(r'input', re.IGNORECASE),
    'rsp': re.compile(r'-rsp-', re.IGNORECASE),
}


def _search_dirs():
    extra = os.environ.get('MUPEN64PLUS_PLUGIN_DIR')
    if extra:
        yield extra
    for d in PLUGIN_DIRS:
        yield d


class available_settings:
    def __init__(self):
        self._by_kind = {kind: [] for kind in _KIND_PATTERNS}
        for directory in _search_dirs():
            path = Path(directory)
            if not path.is_dir():
                continue
            for so in sorted(path.glob('*.so')):
                for kind, pattern in _KIND_PATTERNS.items():
                    if pattern.search(so.name):
                        self._by_kind[kind].append(str(so))
                        break

    def get_video_plugins(self):
        return list(self._by_kind['video'])

    def get_audio_plugins(self):
        return list(self._by_kind['audio'])

    def get_input_plugins(self):
        return list(self._by_kind['input'])

    def get_rsp_plugins(self):
        return list(self._by_kind['rsp'])


AvailableSettings = available_settings
