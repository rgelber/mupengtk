"""Read MupenGTK user settings, populating sensible defaults on first run."""

import os

import yaml

from .available_settings import available_settings


CONFIG_DIR = os.path.join(
    os.environ.get('XDG_CONFIG_HOME') or os.path.expanduser('~/.config'),
    'mupengtk',
)
CONFIG_PATH = os.path.join(CONFIG_DIR, 'settings.yaml')


def _first(items):
    return items[0] if items else ''


def _default_settings():
    plugins = available_settings()
    return {
        'settings': {
            'fullscreen': False,
            'plugins': {
                'audio': _first(plugins.get_audio_plugins()),
                'gfx': _first(plugins.get_video_plugins()),
                'input': _first(plugins.get_input_plugins()),
                'rsp': _first(plugins.get_rsp_plugins()),
            },
            'resolution': '1920x1080',
            'rom': '',
        }
    }


def ensure_config():
    os.makedirs(CONFIG_DIR, exist_ok=True)
    if not os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, 'w') as f:
            yaml.safe_dump(_default_settings(), f)


class read_settings:
    def __init__(self):
        ensure_config()
        with open(CONFIG_PATH) as f:
            data = yaml.safe_load(f) or {}
        settings = data.get('settings', {}) or {}
        plugins = settings.get('plugins', {}) or {}
        self.rom = settings.get('rom', '')
        self.gfx = plugins.get('gfx', '')
        self.audio = plugins.get('audio', '')
        self.input = plugins.get('input', '')
        self.rsp = plugins.get('rsp', '')
        self.resolution = settings.get('resolution', '1920x1080')
        self.fullscreen = bool(settings.get('fullscreen', False))

    def get_rom(self):
        return self.rom

    def get_plugin_gfx(self):
        return self.gfx

    def get_plugin_audio(self):
        return self.audio

    def get_plugin_input(self):
        return self.input

    def get_plugin_rsp(self):
        return self.rsp

    def get_resolution(self):
        return self.resolution

    def get_fullscreen(self):
        return self.fullscreen


Settings = read_settings
