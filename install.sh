#!/usr/bin/env bash
# MupenGTK installer — works on Arch, Debian/Ubuntu, Fedora/RHEL, openSUSE, Alpine.
set -euo pipefail

PREFIX="${PREFIX:-/usr/local}"
BINDIR="${BINDIR:-$PREFIX/bin}"
DATADIR="${DATADIR:-$PREFIX/share}"
SUDO="${SUDO-sudo}"

repo_root="$(cd "$(dirname "$0")" && pwd)"

pm_detect() {
    for pm in pacman apt-get dnf zypper apk; do
        if command -v "$pm" >/dev/null 2>&1; then
            printf '%s\n' "$pm"
            return
        fi
    done
    printf ''
}

pip_flags() {
    if pip3 install --help 2>&1 | grep -q -- '--break-system-packages'; then
        printf -- '--break-system-packages'
    fi
}

install_deps() {
    local pm; pm="$(pm_detect)"
    case "$pm" in
        pacman)
            $SUDO pacman -S --needed --noconfirm \
                xdotool mupen64plus python-yaml python-gobject gtk3
            ;;
        apt-get)
            $SUDO apt-get update
            $SUDO apt-get install -y --no-install-recommends \
                xdotool mupen64plus mupen64plus-ui-console \
                python3-yaml python3-gi gir1.2-gtk-3.0 python3-pip
            ;;
        dnf)
            $SUDO dnf install -y \
                xdotool mupen64plus python3-pyyaml python3-gobject gtk3 python3-pip
            ;;
        zypper)
            $SUDO zypper install -y \
                xdotool mupen64plus python3-PyYAML python3-gobject \
                typelib-1_0-Gtk-3_0 python3-pip
            ;;
        apk)
            $SUDO apk add --no-cache \
                xdotool mupen64plus py3-yaml py3-gobject3 gtk+3.0 py3-pip
            ;;
        *)
            cat <<EOF >&2
Warning: no supported package manager detected.
Please install manually:
  - mupen64plus (with plugins)
  - xdotool (X11 only; keyboard-signal integration will be disabled without it)
  - Python 3 with PyYAML and PyGObject (GTK 3)
EOF
            ;;
    esac
}

install_files() {
    $SUDO install -Dm755 "$repo_root/bin/mupengtk"        "$BINDIR/mupengtk"
    $SUDO install -Dm644 "$repo_root/assets/n64.png"      "$DATADIR/mupengtk/n64.png"
    $SUDO install -Dm644 "$repo_root/assets/n64.png"      "$DATADIR/pixmaps/mupengtk.png"
    $SUDO install -Dm644 "$repo_root/assets/n64.png"      "$DATADIR/icons/hicolor/512x512/apps/mupengtk.png"
    $SUDO install -Dm644 "$repo_root/assets/mupengtk.desktop" "$DATADIR/applications/mupengtk.desktop"
}

install_python() {
    local flags; flags="$(pip_flags)"
    $SUDO pip3 install $flags "$repo_root/pip/mupengtksettings"
}

refresh_caches() {
    if command -v gtk-update-icon-cache >/dev/null 2>&1; then
        $SUDO gtk-update-icon-cache -q "$DATADIR/icons/hicolor" 2>/dev/null || true
    fi
    if command -v update-desktop-database >/dev/null 2>&1; then
        $SUDO update-desktop-database -q "$DATADIR/applications" 2>/dev/null || true
    fi
}

install_func() {
    install_deps
    install_python
    install_files
    refresh_caches
    echo "MupenGTK installed to $PREFIX"
}

uninstall_func() {
    $SUDO rm -f  "$BINDIR/mupengtk"
    $SUDO rm -rf "$DATADIR/mupengtk"
    $SUDO rm -f  "$DATADIR/pixmaps/mupengtk.png"
    $SUDO rm -f  "$DATADIR/icons/hicolor/512x512/apps/mupengtk.png"
    $SUDO rm -f  "$DATADIR/applications/mupengtk.desktop"
    local flags; flags="$(pip_flags)"
    $SUDO pip3 uninstall -y $flags mupengtksettings || true
    refresh_caches
    echo "MupenGTK uninstalled"
}

usage() {
cat <<EOF
Usage: $0 [option]

  -h, --help       Show this help.
  -i, --install    Install MupenGTK (default prefix: /usr/local).
  -u, --uninstall  Uninstall MupenGTK.

Environment:
  PREFIX  install prefix         (default: /usr/local)
  BINDIR  binary directory       (default: \$PREFIX/bin)
  DATADIR shared data directory  (default: \$PREFIX/share)
  SUDO    privilege wrapper      (default: sudo; set SUDO= to disable)
EOF
}

case "${1:-}" in
    -i|--install)   install_func ;;
    -u|--uninstall) uninstall_func ;;
    -h|--help|"")   usage ;;
    *)              usage; exit 1 ;;
esac
