# -*- coding: utf-8 -*-

import pygame

from constants.graphics import *
from constants import grid
from graphics.hold_region import HoldRegion
from graphics.grid_region import GridRegion


class Window:
    """Class Window. Class dealing with all graphical output."""
    
    def __init__(self):
        """Constructor for the class Window."""
        screen_size = {"width": HOLD_SIZE_PIXELS["width"]+GRID_SIZE_PIXELS["width"]+QUEUE_SIZE_PIXELS["width"],
                       "height": GRID_SIZE_PIXELS["height"]}
        
        self._screen = pygame.display.set_mode((screen_size["width"], screen_size["height"]))
        pygame.display.set_caption("Tetris")
        
        self._hold_region = HoldRegion(HOLD_SIZE_PIXELS)
        self._grid_region = GridRegion(GRID_SIZE_PIXELS)
    
    
    def draw_all(self, current_grid, current_tetromino, queue, held, score, level, goal):
        """Redraws the whole window when called."""
        self._screen.fill(COLORS["background"])
        
        self._hold_region.update(held=held)
        self._grid_region.update(current_grid=current_grid, current_tetromino=current_tetromino)
        
        self._screen.blit(self._hold_region.surface, HOLD_POSITION_PIXELS)
        self._screen.blit(self._grid_region.surface, GRID_POSITION_PIXELS)
    
        pygame.display.update()
    
    
    
    
    
    
   