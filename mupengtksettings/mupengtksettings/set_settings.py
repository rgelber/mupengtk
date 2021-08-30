import os
import re
import yaml
from shutil import copyfile


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
