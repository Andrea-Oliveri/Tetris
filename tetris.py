# -*- coding: utf-8 -*-

#import ctypes
#ctypes.windll.user32.SetProcessDPIAware()


# TODO:
#    Implemet top out by lock out (piece locked out entirely in non-visible region)
#    Implement top out by block out (piece cannot be spawned because block occupied)
#    Clean a bit code: tetromino detect collisions has a +1, grid_region.update has -1, lock_down has -1 ...
#    Start implementing actual gameplay, starting from methods of tetrominos

#   Up arrow: Rotating 90 degrees clockwise, Down arrow key: Non-locking soft drop, Space bar: Locking hard drop, C key / Shift key: Hold piece, Z key: Rotating 90 degrees counterclockwise


from game import Game


current_game = Game()
current_game.run()
del current_game