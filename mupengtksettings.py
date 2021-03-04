import os
import re
import yaml
from shutil import copyfile


class read_settings:
    def __init__(self):
        default_dir = os.path.expanduser('~/.config/mupengtk')
        default_path = default_dir + "/settings.yaml"
        if not os.path.exists(default_dir):
            os.makedirs(default_dir)
            src = 'default_settings.yaml'
            dst = default_path
            copyfile(src, dst)
        try:
            with open(default_path) as settings:
                settings = yaml.load(settings, Loader=yaml.FullLoader)
                self.rom = settings["settings"]["rom"]
                self.gfx = settings["settings"]["plugins"]["gfx"]
                self.audio = settings["settings"]["plugins"]["audio"]
                self.input = settings["settings"]["plugins"]["input"]
                self.rsp = settings["settings"]["plugins"]["rsp"]
                self.resolution = settings["settings"]["resolution"]
                self.fullscreen = settings["settings"]["fullscreen"]
        except FileNotFoundError:
            pass

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


class set_settings:
    def __init__(self):
        default_dir = os.path.expanduser('~/.config/mupengtk')
        self.default_path = default_dir + "/settings.yaml"
        self.rom = 'data["settings"]["rom"]'
        self.gfx = 'data["settings"]["plugins"]["gfx"]'
        self.audio = 'data["settings"]["plugins"]["audio"]'
        self.input = 'data["settings"]["plugins"]["input"]'
        self.rsp = 'data["settings"]["plugins"]["rsp"]'
        self.resolution = 'data["settings"]["resolution"]'
        self.fullscreen = 'data["settings"]["fullscreen"]'

    def set_rom(self, value):
        try:
            with open(self.default_path) as settings:
                data = yaml.load(settings, Loader=yaml.FullLoader)
                data["settings"]["rom"] = value
            with open(self.default_path, 'w') as settings:
                yaml.dump(data, settings)
        except FileNotFoundError:
            print('error')
            pass

    def set_gfx(self, value):
        try:
            with open(self.default_path) as settings:
                data = yaml.load(settings, Loader=yaml.FullLoader)
                data["settings"]["plugins"]["gfx"] = value
            with open(self.default_path, 'w') as settings:
                yaml.dump(data, settings)
        except FileNotFoundError:
            print('error')
            pass

    def set_audio(self, value):
        try:
            with open(self.default_path) as settings:
                data = yaml.load(settings, Loader=yaml.FullLoader)
                data["settings"]["plugins"]["audio"] = value
            with open(self.default_path, 'w') as settings:
                yaml.dump(data, settings)
        except FileNotFoundError:
            print('error')
            pass

    def set_input(self, value):
        try:
            with open(self.default_path) as settings:
                data = yaml.load(settings, Loader=yaml.FullLoader)
                data["settings"]["plugins"]["input"] = value
            with open(self.default_path, 'w') as settings:
                yaml.dump(data, settings)
        except FileNotFoundError:
            print('error')
            pass

    def set_rsp(self, value):
        try:
            with open(self.default_path) as settings:
                data = yaml.load(settings, Loader=yaml.FullLoader)
                data["settings"]["plugins"]["rsp"] = value
            with open(self.default_path, 'w') as settings:
                yaml.dump(data, settings)
        except FileNotFoundError:
            print('error')
            pass

    def set_resolution(self, value):
        try:
            with open(self.default_path) as settings:
                data = yaml.load(settings, Loader=yaml.FullLoader)
                data["settings"]["resolution"] = value
            with open(self.default_path, 'w') as settings:
                yaml.dump(data, settings)
        except FileNotFoundError:
            print('error')
            pass

    def set_fullscreen(self, value):
        try:
            with open(self.default_path) as settings:
                data = yaml.load(settings, Loader=yaml.FullLoader)
                data["settings"]["fullscreen"] = value
            with open(self.default_path, 'w') as settings:
                yaml.dump(data, settings)
        except FileNotFoundError:
            print('error')
            pass


class available_settings:
    def __init__(self):
        dir_path = '/usr/lib64/mupen64plus/'
        self.gfx_plugins = []
        self.audio_plugins = []
        self.input_plugins = []
        self.rsp_plugins = []
        for root, dirs, files in os.walk(dir_path):
            for f in files:
                gfx = re.search(".+video.+.so", str(f))
                audio = re.search(".+audio.+.so", str(f))
                input = re.search(".+input.+.so", str(f))
                rsp = re.search(".+rsp.+.so", str(f))
                try:
                    self.gfx_plugins.append(dir_path + gfx.group(0))
                except AttributeError:
                    pass
                try:
                    self.audio_plugins.append(dir_path + audio.group(0))
                except AttributeError:
                    pass
                try:
                    self.input_plugins.append(dir_path + input.group(0))
                except AttributeError:
                    pass
                try:
                    self.rsp_plugins.append(dir_path + rsp.group(0))
                except AttributeError:
                    pass

    def get_video_plugins(self):
        return self.gfx_plugins

    def get_audio_plugins(self):
        return self.audio_plugins

    def get_input_plugins(self):
        return self.input_plugins

    def get_rsp_plugins(self):
        return self.rsp_plugins
