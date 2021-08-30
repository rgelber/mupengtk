import os
import yaml


class read_settings:
    def __init__(self):
        default_settings = """
settings:
  fullscreen: false
  plugins:
    audio: /usr/lib64/mupen64plus/mupen64plus-audio-sdl.so
    gfx: /usr/lib64/mupen64plus/mupen64plus-video-glide64mk2.so
    input: /usr/lib64/mupen64plus/mupen64plus-input-sdl.so
    rsp: /usr/lib64/mupen64plus/mupen64plus-rsp-hle.so
  resolution: 1920x1080
  rom: ''"""
        default_dir = os.path.expanduser('~/.config/mupengtk')
        default_path = default_dir + "/settings.yaml"
        if not os.path.exists(default_dir):
            os.makedirs(default_dir)
            f = open(default_path, 'w')
            f.write(default_settings)
            f.close()
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
            f = open(default_path, 'w')
            f.write(default_settings)
            f.close()
            with open(default_path) as settings:
                settings = yaml.load(settings, Loader=yaml.FullLoader)
                self.rom = settings["settings"]["rom"]
                self.gfx = settings["settings"]["plugins"]["gfx"]
                self.audio = settings["settings"]["plugins"]["audio"]
                self.input = settings["settings"]["plugins"]["input"]
                self.rsp = settings["settings"]["plugins"]["rsp"]
                self.resolution = settings["settings"]["resolution"]
                self.fullscreen = settings["settings"]["fullscreen"]

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
