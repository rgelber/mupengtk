"""Write MupenGTK user settings back to the YAML config."""

import yaml

from .read_settings import CONFIG_PATH, ensure_config


_KEY_PATHS = {
    'rom': ('rom',),
    'gfx': ('plugins', 'gfx'),
    'audio': ('plugins', 'audio'),
    'input': ('plugins', 'input'),
    'rsp': ('plugins', 'rsp'),
    'resolution': ('resolution',),
    'fullscreen': ('fullscreen',),
}


class set_settings:
    def __init__(self):
        ensure_config()
        self.default_path = CONFIG_PATH

    def _update(self, key, value):
        with open(self.default_path) as f:
            data = yaml.safe_load(f) or {}
        node = data.setdefault('settings', {})
        path = _KEY_PATHS[key]
        for step in path[:-1]:
            node = node.setdefault(step, {})
        node[path[-1]] = value
        with open(self.default_path, 'w') as f:
            yaml.safe_dump(data, f)

    def set_rom(self, value):
        self._update('rom', value)

    def set_gfx(self, value):
        self._update('gfx', value)

    def set_audio(self, value):
        self._update('audio', value)

    def set_input(self, value):
        self._update('input', value)

    def set_rsp(self, value):
        self._update('rsp', value)

    def set_resolution(self, value):
        self._update('resolution', value)

    def set_fullscreen(self, value):
        self._update('fullscreen', bool(value))


SettingsWriter = set_settings
