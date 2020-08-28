# -*- coding: utf-8 -*-

#import ctypes
#ctypes.windll.user32.SetProcessDPIAware()

from game import Game



current_game = Game()
current_game.run()
del current_game