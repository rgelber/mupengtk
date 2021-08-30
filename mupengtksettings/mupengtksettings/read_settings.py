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
