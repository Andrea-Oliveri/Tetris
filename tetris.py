# -*- coding: utf-8 -*-

#import ctypes
#ctypes.windll.user32.SetProcessDPIAware()


# TODO:
#    Implement correct lock delay: right now it is 30 frames + time taken to fall down one row. Should be 0.5 secs constant. Must reset with "move reset": each successful shifting or rotation resets (with no move limit: infinity)
#    Implemet top out by lock out (piece locked out entirely in non-visible region)
#    Implement top out by block out (piece cannot be spawned because block occupied)
#    Clean a bit code: tetromino detect collisions has a +1, grid_region.update has -1, lock_down has -1 ...


from game import Game


current_game = Game()
current_game.run()
del current_game