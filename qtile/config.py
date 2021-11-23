
from libqtile import hook, layout, bar, widget
from os import path
import subprocess

from libqtile.config import Key, Group, Drag, Click, Screen
from libqtile.command import lazy

## Autostart

@hook.subscribe.startup_once
def autostart():
  home = path.expanduser('~')
  subprocess.Popen([home + '/.config/qtile/autostart.sh'])

## Atajos de teclado

mod = "mod4"

keys = [
  # Cambiar entre ventanas
  Key([mod], "j", lazy.layout.down()),
  Key([mod], "k", lazy.layout.up()),
  Key([mod], "h", lazy.layout.left()),
  Key([mod], "l", lazy.layout.right()),
  # Cambiar tamaño ventana
  Key([mod, "shift"], "l", lazy.layout.grow()),
  Key([mod, "shift"], "h", lazy.layout.shrink()),
  # Cambiar posicion ventana
  Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
  Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
  # Cambiar distribucion de ventanas
  Key([mod], "Tab", lazy.next_layout()),
  Key([mod, "shift"], "Tab", lazy.prev_layout()),
  # Cerrar ventana
  Key([mod], "w", lazy.window.kill()),
  Key([mod, "shift"], "q", lazy.window.kill()),
  # Cambiar de pantalla
  Key([mod], "period", lazy.next_screen()),
  Key([mod], "comma", lazy.prev_screen()),
  # Reiniciar Qtile
  Key([mod, "control"], "r", lazy.restart()),
  # Cerrar Qtile
  Key([mod, "control"], "q", lazy.shutdown()),
  # Bloquear pantalla
  Key([mod, "control"], "l", lazy.spawm("light-locker-command -l")),
  # Linea de comandos en el panel
  Key([mod], "r", lazy.spawncmd()),
  # Menu
  Key([mod], "d", lazy.spawn("rofi -show drun")),
  # Listar ventanas
  Key([mod, "shift"], "d", lazy.spawn("rofi -show")),
  # Menu ssh
  Key([mod], "s", lazy.spawn("rofi -show ssh")),
  # Browser
  Key([mod], "b", lazy.spawn("brave")),
  # File Explorer
  Key([mod], "f", lazy.spawn("thunar")),
  # Terminal
  Key([mod], "Return", lazy.spawn("alacritty")),
  # Volume
  Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%")),
  Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%")),
  Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),
  # Brightness
  Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
  Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
]

## Teclas raton

mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position()
    ),
    Drag(
        [mod],
        "Button3",
        lazy.window.set_size_floating(),
        start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

## Grupos

groups = [Group(i) for i in [
    " 1:  "," 2:  ", " 3:  ", " 4  ", " 5  ", " 6  ", " 7  ", " 8  ", " 9  ", 
]]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        # Switch to workspace N
        Key([mod], actual_key, lazy.group[group.name].toscreen()),
        # Send window to workspace N
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))
    ])

## Distribuciones de ventanas

layouts = [
    layout.Max(),
    layout.MonadTall(),
    layout.MonadWide(),
    layout.Bsp(),
    layout.Matrix(),
    layout.RatioTile(),
    layout.Columns(),
    layout.Tile(),
    layout.TreeTab(),
    layout.VerticalTile(),
    layout.Zoomy(),
]

## Definimos Barra

screens = [
  Screen(
    top=bar.Bar([
      widget.GroupBox(),
      widget.WindowName()
      ], 30))
]


## Variables

main = None
dgroups_key_binder = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = True
auto_fullscreen = True
focus_on_window_activation = 'urgent'
wmname = 'LG3D'
