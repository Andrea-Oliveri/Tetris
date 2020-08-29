# -*- coding: utf-8 -*-

#import ctypes
#ctypes.windll.user32.SetProcessDPIAware()


# TODO:
#    As of now, tetrominos lock instantly into place when can't descend anymore. There should be 0.5 sec delay after lock, reset if piece manages to move down a row
#    Hold piece
#    3 next pieces preview
#    ....... add tetris guidelines

#   right-left arrows: move, Up arrow: Rotating 90 degrees clockwise, Down arrow key: Non-locking soft drop, Space bar: Locking hard drop, C key / Shift key: Hold piece, Z key: Rotating 90 degrees counterclockwise


from game import Game


current_game = Game()
current_game.run()
del current_game