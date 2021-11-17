# KWin Script Reversed Auto Hide
# (C) 2021 Friedrich Schriewer <friedrich.schriewer@gmx.net>
# GNU General Public License v3.0

from pynput import mouse
import os

shown = True

#Top Left
panel_start_x = 384
panel_start_y = 180
#Bottom Right
panel_end_x   = 1216
panel_end_y   = 205

panel_index = 0

def on_move(x,y):
    global shown

    if y <= panel_end_y and y >= panel_start_y and x <= panel_end_x and x >= panel_start_x and shown == True:
        os.system('qdbus org.kde.plasmashell /PlasmaShell evaluateScript "panel = panelById(panelIds['+str(panel_index)+']); if (panel.height > 0) {panel.height = panel.height * -1;}";')
        shown = False
    elif (y > panel_end_y or y < panel_start_y or x > panel_end_x or x < panel_start_x) and shown == False:
        os.system('qdbus org.kde.plasmashell /PlasmaShell evaluateScript "panel = panelById(panelIds['+str(panel_index)+']); if (panel.height < 0) {panel.height = panel.height * -1;}";')
        shown = True

try:
    with mouse.Listener( on_move = on_move ) as listener:
        listener.join()
except:
    os.system('qdbus org.kde.plasmashell /PlasmaShell evaluateScript "panel = panelById(panelIds['+str(panel_index)+']); if (panel.height < 0) {panel.height = panel.height * -1;}";')
