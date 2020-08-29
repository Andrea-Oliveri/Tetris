# -*- coding: utf-8 -*-

import pygame

from constants.graphics import *
from constants import grid
from graphics.region import Region


class GridRegion(Region):
    """Class GridRegion. Class representing the region of the window where the grid is displayed."""
        
    def update(self, **kwargs):
        """Implementation of the update method for the HoldRegion."""
        if len(kwargs.keys()) != 2 or "current_grid" not in kwargs or "current_tetromino" not in kwargs:
            raise TypeError("GridRegion.update() takes exactly two kwarg: current_grid and current_tetromino")
            
        self._surface.fill(COLORS["background"])

        self._draw_current_grid(kwargs["current_grid"])
        self._draw_current_tetromino(kwargs["current_tetromino"])
        self._draw_borders()
                
    
    def _draw_current_grid(self, current_grid):
        """Draws the whole grid on the screen."""
        for line in range(grid.VISIBLE_SIZE["height"]):
            for col in range(grid.VISIBLE_SIZE["width"]):
                if current_grid[line, col] != " ":
                    pygame.draw.rect(self._surface, COLORS[current_grid[line, col]],
                                     (GRID_SIZE_PIXELS["width"]+col*GRID_SQUARE_SIZE_PIXELS,
                                      GRID_SIZE_PIXELS["height"]+line*GRID_SQUARE_SIZE_PIXELS,
                                      GRID_SQUARE_SIZE_PIXELS, GRID_SQUARE_SIZE_PIXELS))
                

    def _draw_current_tetromino(self, tetromino):
        """Draws the current tetromino on the grid."""
        
        for line in range(tetromino.MAPS_SIZE["height"]):
            for col in range(tetromino.MAPS_SIZE["width"]):
                if tetromino[line, col]:
                    square_col = tetromino.position[1]+col
                    square_line = grid.VISIBLE_SIZE["height"]-tetromino.position[0]+line
                    if square_line >= 0: 
                        pygame.draw.rect(self._surface, COLORS[tetromino.letter],
                                         (square_col*GRID_SQUARE_SIZE_PIXELS,
                                          square_line*GRID_SQUARE_SIZE_PIXELS,
                                          GRID_SQUARE_SIZE_PIXELS, GRID_SQUARE_SIZE_PIXELS))
    

    def _draw_borders(self):
        """Draws the borders between cases in the grid and around the grid."""
        for line in range(1, grid.VISIBLE_SIZE["height"]):
            pygame.draw.line(self._surface, COLORS["grid_line"], (0, line*GRID_SQUARE_SIZE_PIXELS), (GRID_SIZE_PIXELS["width"], line*GRID_SQUARE_SIZE_PIXELS), GRID_INTERNAL_LINE_WIDTH_PIXELS)

        for col in range(1, grid.VISIBLE_SIZE["width"]):
            pygame.draw.line(self._surface, COLORS["grid_line"], (+col*GRID_SQUARE_SIZE_PIXELS, 0), (col*GRID_SQUARE_SIZE_PIXELS, GRID_SIZE_PIXELS["height"]), GRID_INTERNAL_LINE_WIDTH_PIXELS)

        pygame.draw.rect(self._surface, COLORS["grid_line"], (0, 0, GRID_SIZE_PIXELS["width"], GRID_SIZE_PIXELS["height"]), GRID_EXTERNAL_LINE_WIDTH_PIXELS)


