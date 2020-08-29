# -*- coding: utf-8 -*-

import pygame

from constants.graphics import *
from constants import grid


class Graphics:
    """Class Graphics. Class dealing with all graphical output."""
    
    def __init__(self):
        """Constructor for the class Graphics."""
        screen_size = {"width": GRID_SIZE_PIXELS["width"]+2*GRID_POSITION_PIXELS[0],
                       "height": GRID_SIZE_PIXELS["height"]+2*GRID_POSITION_PIXELS[1]}
        
        self._screen = pygame.display.set_mode((screen_size["width"], screen_size["height"]))
        pygame.display.set_caption("Tetris")
        
    
    def draw_grid(self, current_grid):
        """Draws the whole grid on the screen."""
        self._screen.fill(COLORS["background"])
        
        for line in range(grid.VISIBLE_SIZE["height"]):
            for col in range(grid.VISIBLE_SIZE["width"]):
                if current_grid[line, col] != " ":
                    pygame.draw.rect(self._screen, COLORS[current_grid[line, col]],
                                     (GRID_SIZE_PIXELS["width"]+col*GRID_SQUARE_SIZE_PIXELS,
                                      GRID_SIZE_PIXELS["height"]+line*GRID_SQUARE_SIZE_PIXELS,
                                      GRID_SQUARE_SIZE_PIXELS, GRID_SQUARE_SIZE_PIXELS))
                

    def draw_current_tetromino(self, tetromino):
        """Draws the current tetromino on the screen."""
        
        for line in range(tetromino.MAPS_SIZE["height"]):
            for col in range(tetromino.MAPS_SIZE["width"]):
                if tetromino[line, col]:
                    square_col = tetromino.position[1]+col
                    square_line = grid.VISIBLE_SIZE["height"]-tetromino.position[0]+line
                    if square_line >= 0: 
                        pygame.draw.rect(self._screen, COLORS[tetromino.letter],
                                         (GRID_POSITION_PIXELS[0]+square_col*GRID_SQUARE_SIZE_PIXELS,
                                          GRID_POSITION_PIXELS[1]+square_line*GRID_SQUARE_SIZE_PIXELS,
                                          GRID_SQUARE_SIZE_PIXELS, GRID_SQUARE_SIZE_PIXELS))
    

    # Can be made faster: draw the colors first, then the external rectangle and the internal grid using pygame.draw.lines (less redundancy in drawing lines: gain approx 0.3 ms per redraw)
    def draw_borders(self):
        """Draws the borders between cases in the grid and around the grid."""
        for line in range(grid.VISIBLE_SIZE["height"]):
            for col in range(grid.VISIBLE_SIZE["width"]):
                pygame.draw.rect(self._screen, COLORS["grid_line"], (GRID_POSITION_PIXELS[0]+col*GRID_SQUARE_SIZE_PIXELS, GRID_POSITION_PIXELS[1]+line*GRID_SQUARE_SIZE_PIXELS, GRID_SQUARE_SIZE_PIXELS, GRID_SQUARE_SIZE_PIXELS), GRID_INTERNAL_LINE_WIDTH_PIXELS)
    
        pygame.draw.rect(self._screen, COLORS["grid_line"], (*GRID_POSITION_PIXELS, GRID_SIZE_PIXELS["width"], GRID_SIZE_PIXELS["height"]), GRID_EXTERNAL_LINE_WIDTH_PIXELS)


