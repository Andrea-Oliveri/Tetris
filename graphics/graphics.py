# -*- coding: utf-8 -*-

import pygame

from constants.graphics import WINDOW_SIZE, COLORS
from graphics import utils
from graphics.regions.region import Region
from graphics.regions.hold_region import HoldRegion
from graphics.regions.grid_region import GridRegion
from graphics.regions.queue_region import QueueRegion
from graphics.regions.level_region import LevelRegion
from graphics.regions.score_region import ScoreRegion


class Window(Region):
    """Class Window. Class dealing with all graphical output."""
    
    def __init__(self):
        """Constructor for the class Window."""
        self._screen = pygame.display.set_mode(WINDOW_SIZE)
        pygame.display.set_caption("Tetris")
        
        self._hold_region = HoldRegion()
        self._grid_region = GridRegion()
        self._queue_region = QueueRegion()
        self._level_region = LevelRegion()
        self._score_region = ScoreRegion()
        
        Region.__init__(self)


    def update(self, **kwargs):
        """Implementation of the update method for the Window."""
        self._update_kwargs_test(kwargs, ["current_grid", "current_tetromino", "queue", "held", "score", "level", "goal", "lines"])

        self._hold_region.update(held=kwargs["held"])
        self._grid_region.update(current_grid=kwargs["current_grid"], current_tetromino=kwargs["current_tetromino"])
        self._queue_region.update(queue=kwargs["queue"])
        self._level_region.update(level=kwargs["level"], goal=kwargs["goal"], lines=kwargs["lines"])
        self._score_region.update(score=kwargs["score"])
        
        central_column = utils.merge_surfaces_vertically([self._grid_region.surface, self._score_region.surface])
        right_column = utils.merge_surfaces_vertically([self._queue_region.surface, self._level_region.surface], False)
        
        self._surface = utils.merge_surfaces_horizontally([self._hold_region.surface, central_column, right_column])
        
        self._screen.fill(COLORS["background"])
        self._screen.blit(self._surface, ((self._screen.get_width()-self._surface.get_width())/2,
                                          (self._screen.get_height()-self._surface.get_height())/2))        
        pygame.display.update()
    
   