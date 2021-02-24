import yaml
from shutil import copyfile


class read_settings:
    def __init__(self):
        try:
            with open('/etc/mupengtk/settings.yaml') as settings:
                settings = yaml.load(settings, Loader=yaml.FullLoader)
                self.rom = settings["settings"]["rom"]
                self.gfx = settings["settings"]["plugins"]["gfx"]
                self.audio = settings["settings"]["plugins"]["audio"]
                self.input = settings["settings"]["plugins"]["input"]
                self.rsp = settings["settings"]["plugins"]["rsp"]
                self.resolution = settings["settings"]["resolution"]
                self.fullscreen = settings["settings"]["fullscreen"]
        except FileNotFoundError:
            src = 'default_settings.yaml'
            dst = '/etc/mupengtk/settings.yaml'
            copyfile(src, dst)

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
        self.rom = 'data["settings"]["rom"]'
        self.gfx = 'data["settings"]["plugins"]["gfx"]'
        self.audio = 'data["settings"]["plugins"]["audio"]'
        self.input = 'data["settings"]["plugins"]["input"]'
        self.rsp = 'data["settings"]["plugins"]["rsp"]'
        self.resolution = 'data["settings"]["resolution"]'
        self.fullscreen = 'data["settings"]["fullscreen"]'

    def set_rom(self, value):
        try:
            with open('/etc/mupengtk/settings.yaml') as settings:
                data = yaml.load(settings, Loader=yaml.FullLoader)
                data["settings"]["rom"] = value
            with open('/etc/mupengtk/settings.yaml', 'w') as settings:
                yaml.dump(data, settings)
        except FileNotFoundError:
            print('error')
            pass

    def set_gfx(self, value):
        try:
            with open('/etc/mupengtk/settings.yaml') as settings:
                data = yaml.load(settings, Loader=yaml.FullLoader)
                data["settings"]["plugins"]["gfx"] = value
            with open('/etc/mupengtk/settings.yaml', 'w') as settings:
                yaml.dump(data, settings)
        except FileNotFoundError:
            print('error')
            pass

    def set_resolution(self, value):
        try:
            with open('/etc/mupengtk/settings.yaml') as settings:
                data = yaml.load(settings, Loader=yaml.FullLoader)
                data["settings"]["resolution"] = value
            with open('/etc/mupengtk/settings.yaml', 'w') as settings:
                yaml.dump(data, settings)
        except FileNotFoundError:
            print('error')
            pass

    def set_fullscreen(self, value):
        try:
            with open('/etc/mupengtk/settings.yaml') as settings:
                data = yaml.load(settings, Loader=yaml.FullLoader)
                data["settings"]["fullscreen"] = value
            with open('/etc/mupengtk/settings.yaml', 'w') as settings:
                yaml.dump(data, settings)
        except FileNotFoundError:
            print('error')
            pass
