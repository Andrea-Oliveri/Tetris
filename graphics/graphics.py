# -*- coding: utf-8 -*-

import pygame

from constants.graphics import WINDOW_SIZE, COLORS
from graphics import utils
from graphics.region import Region
from graphics.hold_region import HoldRegion
from graphics.grid_region import GridRegion
from graphics.queue_region import QueueRegion


class Window(Region):
    """Class Window. Class dealing with all graphical output."""
    
    def __init__(self):
        """Constructor for the class Window."""
        self._screen = pygame.display.set_mode(WINDOW_SIZE)
        pygame.display.set_caption("Tetris")
        
        self._hold_region = HoldRegion()
        self._grid_region = GridRegion()
        self._queue_region = QueueRegion()
        
        Region.__init__(self)

    def update(self, **kwargs):
        """Implementation of the update method for the Window."""
        if len(kwargs.keys()) != 7 or not all([key in kwargs for key in ["current_grid", "current_tetromino", "queue", "held", "score", "level", "goal"]]):
            raise TypeError("Window.update() takes exactly 7 kwarg: current_grid, current_tetromino, queue, held, score, level, goal")
            
        current_grid = kwargs["current_grid"]
        current_tetromino = kwargs["current_tetromino"]
        queue = kwargs["queue"]
        held = kwargs["held"]
        score = kwargs["score"]
        level = kwargs["level"]
        goal = kwargs["goal"]

        self._hold_region.update(held=held)
        self._grid_region.update(current_grid=current_grid, current_tetromino=current_tetromino)
        self._queue_region.update(queue=queue)

        self._surface = utils.merge_surfaces_horizontally([self._hold_region.surface, self._grid_region.surface, self._queue_region.surface])
        #self._screen.set_mode(self._surface.get_size())
        self._screen.fill(COLORS["background"])
        self._screen.blit(self._surface, ((self._screen.get_width()-self._surface.get_width())/2,
                                          (self._screen.get_height()-self._surface.get_height())/2))
        pygame.display.update()
    
    
   