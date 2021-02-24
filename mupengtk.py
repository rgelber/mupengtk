#!/usr/bin/env python3

import sys
import os
import mupengtksettings
import gi
import subprocess
import threading
import logging
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from pynput.keyboard import Key, Controller


# Global Vars
read_mupensettings = mupengtksettings.read_settings()
set_mupensettings = mupengtksettings.set_settings()


class Window(Gtk.ApplicationWindow):
    def __init__(self, app):
        super(Window, self).__init__(title="MupenGTK", application=app)

        # MenuBar Headers Declatations
        grid = Gtk.Grid()
        menubar = Gtk.MenuBar()
        file_menu = Gtk.Menu()
        file_header = Gtk.MenuItem.new_with_label("File")
        file_header.set_submenu(file_menu)

        emulation_menu = Gtk.Menu()
        emulation_header = Gtk.MenuItem.new_with_label("Emulation")
        emulation_header.set_submenu(emulation_menu)

        view_menu = Gtk.Menu()
        view_header = Gtk.MenuItem.new_with_label("View")
        view_header.set_submenu(view_menu)

        settings_menu = Gtk.Menu()
        settings_header = Gtk.MenuItem.new_with_label("Settings")
        settings_header.set_submenu(settings_menu)

        # File Rom Menu Options
        rom_menu = Gtk.Menu()
        open_rom = Gtk.MenuItem.new_with_label("Open ROM")
        open_rom.set_submenu(rom_menu)

        open_rom_man = Gtk.MenuItem.new_with_label("Manually...")
        open_rom_man.connect("activate", self.select_rom_manually)
        open_rom_list = Gtk.MenuItem.new_with_label("List..")

        rom_menu.append(open_rom_man)
        rom_menu.append(open_rom_list)
        file_menu.append(open_rom)

        # File Rom Menu Options
        rom_recent_menu = Gtk.MenuItem.new_with_label('Open Recent')
        file_menu.append(rom_recent_menu)
        recentchoosermenu = Gtk.RecentChooserMenu()
        filter = Gtk.RecentFilter()
        filter.add_pattern("*.n64")
        recentchoosermenu.set_filter(filter)
        recentchoosermenu.connect('item-activated', self.select_rom_recent)
        rom_recent_menu.set_submenu(recentchoosermenu)

        # File Save State Menu Options
        save_state_menu = Gtk.Menu()
        save_state = Gtk.MenuItem.new_with_label("Save Slots")
        save_state.set_submenu(save_state_menu)
        save_state_rad_group = Gtk.RadioMenuItem(
            group=None,
            label="save_radio_group"
        )
        for i in range(0, 10):
            save_state_rad = Gtk.RadioMenuItem(
                group=save_state_rad_group,
                label=f"Slot {i}"
            )
            save_state_menu.append(save_state_rad)
        file_menu.append(save_state)

        # File Save Menu Option
        save_rom = Gtk.MenuItem.new_with_label("Save State...")
        file_menu.append(save_rom)

        # File Load Menu Option
        save_rom = Gtk.MenuItem.new_with_label("Load State...")
        file_menu.append(save_rom)

        # Emulation Start Menu Option
        start_rom = Gtk.MenuItem.new_with_label("Start")
        start_rom.connect("activate", self.start_emulator)
        emulation_menu.append(start_rom)

        # Emulation Stop Menu Option
        stop_rom = Gtk.MenuItem.new_with_label("Stop")
        stop_rom.connect("activate", self.stop_emulation)
        emulation_menu.append(stop_rom)

        # Emulation Pause Menu Option
        pause_rom = Gtk.MenuItem.new_with_label("Pause")
        pause_rom.connect("activate", self.pause_emulation)
        emulation_menu.append(pause_rom)

        # View Resolution Menu Option
        res_menu = Gtk.Menu()
        res_label = Gtk.MenuItem.new_with_label("Resolution")
        res_label.set_submenu(res_menu)
        res_rad_group = Gtk.RadioMenuItem(
            group=None,
            label="res_radio_group"
        )
        resolutions = [
            '640x360', '800x600', '1024x768', '1280x720',
            '1280x800', '1280x1024', '1360x768', '1366x768',
            '1440x900', '1536x864', '1600x900', '1680x1050',
            '1920x1080', '1920x1200', '2048x1152', '2560x1080',
            '2560x1440', '3440x1440', '3840x2160'
        ]
        for i in resolutions:
            res_rad = Gtk.RadioMenuItem(
                group=res_rad_group,
                label=f"{i}"
            )
            if i == read_mupensettings.get_resolution():
                res_rad.set_active(i)
            res_rad.connect("toggled", self.set_resolution)
            res_menu.append(res_rad)
        view_menu.append(res_label)

        # View Fullscreen Menu Option
        fullscreen_label = Gtk.CheckMenuItem.new_with_label("Fullscreen")
        fullscreen_label.set_active(read_mupensettings.get_fullscreen())
        fullscreen_label.connect("activate", self.is_fullscreen)
        view_menu.append(fullscreen_label)

        # Status Bar
        self.statusbar = Gtk.Statusbar()
        self.context = self.statusbar.get_context_id("example")
        grid.attach(self.statusbar, 0, 1, 2, 2)
        self.count = 0

        # Menu Bar
        menubar.add(file_header)
        menubar.add(emulation_header)
        menubar.add(view_header)
        menubar.add(settings_header)

        grid.attach(menubar, 0, 0, 1, 1)
        self.add(grid)
        self.set_default_size(400, 300)

    # Move these to a seperate library
    # Select rom manually
    def select_rom_manually(self, widget):
        filechooserdialog = Gtk.FileChooserDialog(
            title="Select ROM...",
            parent=None,
            action=Gtk.FileChooserAction.OPEN
        )
        filter = Gtk.FileFilter()
        filter.add_pattern("*.n64")
        filechooserdialog.set_filter(filter)
        filechooserdialog.add_buttons("_Open", Gtk.ResponseType.OK)
        filechooserdialog.add_buttons("_Cancel", Gtk.ResponseType.CANCEL)
        filechooserdialog.set_default_response(Gtk.ResponseType.OK)

        response = filechooserdialog.run()

        if response == Gtk.ResponseType.OK:
            set_mupensettings.set_rom(filechooserdialog.get_filename())
            print(f'File selected: {filechooserdialog.get_filename()}')
        filechooserdialog.destroy()

    # Select ROM from recent list
    def select_rom_recent(self, widget):
        selected = widget.get_current_item()
        print(f'ROM Selected: {selected.get_uri_display()}')
        set_mupensettings.set_rom(selected.get_uri_display())

    # Start Emulation
    def start_emulator(self, event):
        read_mupensettings = mupengtksettings.read_settings()
        fullscreen = read_mupensettings.get_fullscreen()
        print(fullscreen)
        if fullscreen is True:
            fullscreen = '--fullscreen'
        else:
            fullscreen = '--windowed'
        cmd = [
                'mupen64plus',
                '--gfx', f'{read_mupensettings.get_plugin_gfx()}',
                '--audio', f'{read_mupensettings.get_plugin_audio()}',
                '--input', f'{read_mupensettings.get_plugin_input()}',
                '--rsp', f'{read_mupensettings.get_plugin_rsp()}',
                '--resolution', f'{read_mupensettings.get_resolution()}',
                f'{fullscreen}',
                f'{read_mupensettings.get_rom()}'
              ]
        print(cmd)
        self.process = subprocess.Popen(cmd)
        msg = f"{read_mupensettings.get_rom().split('/')[-1]} has started"
        self.statusbar.push(self.context, msg)

    def keyboard_signals(self, signal):
        keyboard = Controller()
        keyboard.press(signal)
        keyboard.release(signal)


    # Stop Emulation
    def stop_emulation(self, widget):
        try:
            self.process.terminate()
            if self.process.returncode is None:
                print("Emulation has received stop signal.")
        except AttributeError:
            pass

    # Pause Emulation
    def pause_emulation(self, widget):
        pid = self.process.pid
        window_id = os.popen(f'xdotool search --pid {pid}').read().strip()
        if len(window_id) == 0:
            print("No window id found")
        else:
            os.popen(f'xdotool windowactivate --sync {window_id} key "p"')

    # Select Resolution
    def set_resolution(self, widget):
        set_mupensettings.set_resolution(widget.get_label())
        print(f'Resolution Set: {widget.get_label()}')

    # Select Fullscreen
    def is_fullscreen(self, widget):
        if widget.get_active():
            print("Fullscreen: On")
            set_mupensettings.set_fullscreen(True)
        else:
            print("Fullscreen: Off")
            set_mupensettings.set_fullscreen(False)


class Application(Gtk.Application):
    def __init__(self):
        super(Application, self).__init__()

    def do_activate(self):
        self.win = Window(self)
        self.win.set_icon_from_file('/home/rgelber/Downloads/n64vapor.png')
        self.win.show_all()

    def do_startup(self):
        Gtk.Application.do_startup(self)


app = Application()
app.run(sys.argv)
