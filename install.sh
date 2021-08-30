#!/bin/bash

function install_func () {
    sudo pacman -S xdotool
    if [[ ! -d '/usr/share/mupengtk/' ]]; then
       sudo mkdir '/usr/share/mupengtk/'
    fi
    sudo cp -f n64.png /usr/share/mupengtk/
    sudo cp -f n64.png /usr/share/icons/mupengtk.png
    sudo cp -f mupengtk /usr/local/bin/
    sudo cp -f mupengtk.desktop /usr/share/applications/
    cd mupengtksettings
    pip3 install -e .
    echo "MupenGTK Installed"
}
function uninstall_func () {
    sudo rm -r /usr/share/mupengtk/
    sudo rm /usr/share//icons/mupengtk.png
    sudo rm /usr/local/bin/mupengtk
    sudo rm /usr/share/applications/mupengtk.desktop
    cd mupengtksettings
    echo "MupenGTK Uninstalled"
}

function usage () {
cat <<EOF
Usage: $0 [options]

-h| --help      Usage.

-i|--install    Install MupenGTK.
-u|--uninstall  Uninstall MupenGTK.
EOF
}

case "$1" in
    '-i'|'--install')
        install_func
        ;;
    '-u'|'--uninstall')
        uninstall_func
        ;;
    *)
        usage
        ;;
esac
