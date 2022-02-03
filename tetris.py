# -*- coding: utf-8 -*-

import os
import sys

# Needed for compatibility with pyinstaller.
if getattr(sys, 'frozen', False):
    os.chdir(sys._MEIPASS)


from src.gui import Gui

# Run application.
app_gui = Gui()
app_gui.run()
del app_gui