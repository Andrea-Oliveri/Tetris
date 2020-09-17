# -*- coding: utf-8 -*-

# TODO:
#   change grid_region so that it has two variables: grid and tetromino. Tetromino generated with utils.draw_tetromino (new name for draw_outside tetromino). Surface is tetromino blit onto grid and then lines drawn. This will allow caching of the grid when only tetromino is changed.
#   caching in Window class: add a dictionary self._cached = {"hold_region": False, ....} which will be updated by a method: notify_event(event) that can take either: movement, lines_cleared, hold_swap and will be called by game when these things change. Method will verify argument is one of these and throw exception otherwise. Any other case needed?
#   once this caching is implemented, we can distinguish between movement and line clears for caching in grid_region class


from game import Game


current_game = Game()
current_game.run()
del current_game