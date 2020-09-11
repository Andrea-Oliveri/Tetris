# -*- coding: utf-8 -*-

import pygame

from constants.graphics import COLORS, GHOST_COLOR_FACTOR, GRID_SQUARE_SIZE_PIXELS, GRID_INTERNAL_LINE_WIDTH_PIXELS, GRID_EXTERNAL_LINE_WIDTH_PIXELS
from constants import grid
from graphics.regions.region import Region


class GridRegion(Region):
    """Class GridRegion. Class representing the region of the window where the grid is displayed."""
        
    def __init__(self):
        """Overload of constructor for GridRegion class."""
        GRID_SIZE_PIXELS = {"width": grid.VISIBLE_SIZE["width"]*GRID_SQUARE_SIZE_PIXELS,
                            "height": grid.VISIBLE_SIZE["height"]*GRID_SQUARE_SIZE_PIXELS}
        self._surface = pygame.Surface((GRID_SIZE_PIXELS["width"], GRID_SIZE_PIXELS["height"]))
        
    
    def update(self, **kwargs):
        """Implementation of the update method for the HoldRegion."""
        self._update_kwargs_test(kwargs, ["current_grid", "current_tetromino"])
        
        self._surface.fill(COLORS["background"])
        self._draw_current_grid(kwargs["current_grid"])
        self._draw_tetromino(kwargs["current_tetromino"].ghost, True)
        self._draw_tetromino(kwargs["current_tetromino"], False)
        self._draw_borders()
                
    
    def _draw_current_grid(self, current_grid):
        """Draws the whole grid on the screen. Must account for different
        coordinate systems used by pygame and grid."""        
        for line in range(grid.VISIBLE_SIZE["height"]):
            for col in range(grid.VISIBLE_SIZE["width"]):
                if not current_grid.is_empty(line, col):
                    pygame.draw.rect(self._surface, COLORS[current_grid[line][col]],
                                     (col*GRID_SQUARE_SIZE_PIXELS,
                                      (grid.VISIBLE_SIZE["height"]-1-line)*GRID_SQUARE_SIZE_PIXELS,
                                      GRID_SQUARE_SIZE_PIXELS, GRID_SQUARE_SIZE_PIXELS))


    def _draw_tetromino(self, tetromino, ghost=False):
        """Draws either the current tetromino or its ghost on the grid."""
        for line in range(tetromino.MAPS_SIZE["height"]):
            for col in range(tetromino.MAPS_SIZE["width"]):
                if tetromino[line][col]:
                    square_col = tetromino.position[1]+col
                    square_line = grid.VISIBLE_SIZE["height"]-1-tetromino.position[0]+line
                    if square_line >= 0:
                        color = COLORS[tetromino.letter]
                        if ghost:
                            color = [val*GHOST_COLOR_FACTOR for val in color]
                            
                        pygame.draw.rect(self._surface, color,
                                         (square_col*GRID_SQUARE_SIZE_PIXELS,
                                          square_line*GRID_SQUARE_SIZE_PIXELS,
                                          GRID_SQUARE_SIZE_PIXELS, GRID_SQUARE_SIZE_PIXELS))
    

    def _draw_borders(self):
        """Draws the borders between cases in the grid and around the grid."""
        for line in range(1, grid.VISIBLE_SIZE["height"]):
            pygame.draw.line(self._surface, COLORS["grid_line"], (0, line*GRID_SQUARE_SIZE_PIXELS), (self._surface.get_width(), line*GRID_SQUARE_SIZE_PIXELS), GRID_INTERNAL_LINE_WIDTH_PIXELS)

        for col in range(1, grid.VISIBLE_SIZE["width"]):
            pygame.draw.line(self._surface, COLORS["grid_line"], (col*GRID_SQUARE_SIZE_PIXELS, 0), (col*GRID_SQUARE_SIZE_PIXELS, self._surface.get_height()), GRID_INTERNAL_LINE_WIDTH_PIXELS)

        pygame.draw.rect(self._surface, COLORS["grid_line"], (0, 0, self._surface.get_width(), self._surface.get_height()), GRID_EXTERNAL_LINE_WIDTH_PIXELS)


