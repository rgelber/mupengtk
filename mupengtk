#!/usr/bin/env python3

import sys
import os
import mupengtksettings
import gi
import subprocess
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from pynput.keyboard import Key, Controller


# Global Vars
read_mupensettings = mupengtksettings.read_settings()
set_mupensettings = mupengtksettings.set_settings()
available_plugins = mupengtksettings.available_settings()


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
            save_state_rad.connect("activate", self.keyboard_signals, str(i)) # Add logic to see if emulator is running.
            save_state_menu.append(save_state_rad)
        file_menu.append(save_state)

        # File Save Menu Option
        save_rom = Gtk.MenuItem.new_with_label("Save State...")
        save_rom.connect("activate", self.keyboard_signals, "F5")
        file_menu.append(save_rom)

        # File Load Menu Option
        load_rom = Gtk.MenuItem.new_with_label("Load State...")
        load_rom.connect("activate", self.keyboard_signals, "F7")
        file_menu.append(load_rom)

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
        pause_rom.connect("activate", self.keyboard_signals, "p")
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
        self.context = self.statusbar.get_context_id("Status")
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

        # Settings Rom Menu Options
        settings_options_menu = Gtk.Menu()
        plugins_option = Gtk.MenuItem.new_with_label("Plugins")
        plugins_option.set_submenu(settings_options_menu)

        # Graphics Plugins
        settings_graphics_menu = Gtk.Menu()
        graphics_plugin = Gtk.MenuItem.new_with_label("Graphics")
        graphics_plugin.set_submenu(settings_graphics_menu)

        gfx_rad_group = Gtk.RadioMenuItem(
            group=None,
            label="gfx_radio_group"
        )
        graphics = available_plugins.get_video_plugins()
        for i in graphics:
            gfx_rad = Gtk.RadioMenuItem(
                group=gfx_rad_group,
                label=f"{i}"
            )
            if i == read_mupensettings.get_plugin_gfx():
                gfx_rad.set_active(i)
            gfx_rad.connect("toggled", self.set_gfx)
            settings_graphics_menu.append(gfx_rad)
        settings_options_menu.append(graphics_plugin)

        # Audio Plugins
        settings_audio_menu = Gtk.Menu()
        audio_plugin = Gtk.MenuItem.new_with_label("Audio")
        audio_plugin.set_submenu(settings_audio_menu)

        audio_rad_group = Gtk.RadioMenuItem(
            group=None,
            label="audio_radio_group"
        )

        audio = available_plugins.get_audio_plugins()
        for i in audio:
            audio_rad = Gtk.RadioMenuItem(
                group=audio_rad_group,
                label=f"{i}"
            )
            if i == read_mupensettings.get_plugin_audio():
                audio_rad.set_active(i)
            audio_rad.connect("toggled", self.set_audio)
            settings_audio_menu.append(audio_rad)
        settings_options_menu.append(audio_plugin)
     
        # Input Plugins
        settings_input_menu = Gtk.Menu()
        input_plugin = Gtk.MenuItem.new_with_label("Input")
        input_plugin.set_submenu(settings_input_menu)

        input_rad_group = Gtk.RadioMenuItem(
            group=None,
            label="input_radio_group"
        )

        input = available_plugins.get_input_plugins()
        for i in input:
            input_rad = Gtk.RadioMenuItem(
                group=input_rad_group,
                label=f"{i}"
            )
            if i == read_mupensettings.get_plugin_input():
                input_rad.set_active(i)
            input_rad.connect("toggled", self.set_input)
            settings_input_menu.append(input_rad)
        settings_options_menu.append(input_plugin)

        # Rsp Plugins
        settings_rsp_menu = Gtk.Menu()
        rsp_plugin = Gtk.MenuItem.new_with_label("Rsp")
        rsp_plugin.set_submenu(settings_rsp_menu)

        rsp_rad_group = Gtk.RadioMenuItem(
            group=None,
            label="rsp_radio_group"
        )

        rsp = available_plugins.get_rsp_plugins()
        for i in rsp:
            rsp_rad = Gtk.RadioMenuItem(
                group=rsp_rad_group,
                label=f"{i}"
            )
            if i == read_mupensettings.get_plugin_rsp():
                rsp_rad.set_active(i)
            rsp_rad.connect("toggled", self.set_rsp)
            settings_rsp_menu.append(rsp_rad)
        settings_options_menu.append(rsp_plugin)

        settings_menu.append(plugins_option)


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
        try:
            self.process.terminate()
            self.process = subprocess.Popen(cmd)
        except AttributeError:
            self.process = subprocess.Popen(cmd)
        msg = f"{read_mupensettings.get_rom().split('/')[-1]} has started"
        self.statusbar.push(self.context, msg)

    # Send Keyboard Signal to Emulator
    def keyboard_signals(self, widget, signal):
        try:
            pid = self.process.pid
            window_id = os.popen(f'xdotool search --pid {pid}').read().strip()
            if len(window_id) == 0:
                print("No window id found")
            else:
                pid = self.process.pid
                window_id = os.popen(f'xdotool search --pid {pid}').read().strip()
                os.popen(f'xdotool windowactivate --sync {window_id} key "{signal}"')
        except AttributeError:
            pass

    # Stop Emulation
    def stop_emulation(self, widget):
        try:
            self.process.terminate()
            if self.process.returncode is None:
                print("Emulation has received stop signal.")
        except AttributeError:
            pass

    # Select Resolution
    def set_resolution(self, widget):
        set_mupensettings.set_resolution(widget.get_label())
        print(f'Resolution Set: {widget.get_label()}')

    # Set Graphics Plugin
    def set_gfx(self, widget):
        set_mupensettings.set_gfx(widget.get_label())
        print(f'Graphics Engine Set: {widget.get_label()}')

    # Set Audio Plugin
    def set_audio(self, widget):
        set_mupensettings.set_audio(widget.get_label())
        print(f'Audio Engine Set: {widget.get_label()}')

    # Set Input Plugin
    def set_input(self, widget):
        set_mupensettings.set_input(widget.get_label())
        print(f'Input Engine Set: {widget.get_label()}')

    # Set Input Plugin
    def set_rsp(self, widget):
        set_mupensettings.set_rsp(widget.get_label())
        print(f'Rsp Engine Set: {widget.get_label()}')

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
        self.win.set_icon_from_file('/usr/share/mupengtk/n64.png')
        self.win.show_all()

    def do_startup(self):
        Gtk.Application.do_startup(self)


app = Application()
app.run(sys.argv)
