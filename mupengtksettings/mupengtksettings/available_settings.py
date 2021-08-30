import os
import re
import yaml
from shutil import copyfile


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
