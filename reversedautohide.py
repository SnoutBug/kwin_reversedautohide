# KWin Script Reversed Auto Hide
# (C) 2021 Friedrich Schriewer <friedrich.schriewer@gmx.net>
# GNU General Public License v3.0

from pynput import mouse
import os

shown = True
is_mouse_down = False

#Top Left
panel_start_x = 384
panel_start_y = 180
#Bottom Right
panel_end_x   = 1216
panel_end_y   = 225

panel_extend_on_mouse_down = 35

panel_index = 0

def on_move(x,y):
    global shown
    if is_mouse_down:
        extend_by = panel_extend_on_mouse_down
    else:
        extend_by = 0

    if y <= panel_end_y + extend_by and y >= panel_start_y - extend_by and x <= panel_end_x + extend_by and x >= panel_start_x - extend_by and shown == True:
        os.system('qdbus org.kde.plasmashell /PlasmaShell evaluateScript "panel = panelById(panelIds['+str(panel_index)+']); if (panel.height > 0) {panel.height = panel.height * -1;}";')
        shown = False
    elif (y > panel_end_y + extend_by or y < panel_start_y - extend_by or x > panel_end_x + extend_by  or x < panel_start_x - extend_by) and shown == False:
        os.system('qdbus org.kde.plasmashell /PlasmaShell evaluateScript "panel = panelById(panelIds['+str(panel_index)+']); if (panel.height < 0) {panel.height = panel.height * -1;}";')
        shown = True

def on_click(*args):
    global is_mouse_down

    if args[-1]:
        if not is_mouse_down:
            is_mouse_down = True

    elif not args[-1]:
        if is_mouse_down:
            is_mouse_down = False

try:
    with mouse.Listener( on_move = on_move, on_click = on_click ) as listener:
        listener.join()
except:
    os.system('qdbus org.kde.plasmashell /PlasmaShell evaluateScript "panel = panelById(panelIds['+str(panel_index)+']); if (panel.height < 0) {panel.height = panel.height * -1;}";')
