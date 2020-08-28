# -*- coding: utf-8 -*-

import pygame


class Graphics:
    """Class Graphics. Class dealing with all graphical output."""
    
    def __init__(self, grid):
        """Constructor for the class Graphics."""
        self._grid_case_size_pixels = 30
        self._grid_size_pixels = {"width": grid.visible_size["width"]*self._grid_case_size_pixels, "height": grid.visible_size["height"]*self._grid_case_size_pixels}
        self._grid_position_pixels = (10, 10)
        self._grid_external_line_width = 3
        self._grid_internal_line_width = 1
        screen_size = {"width": self._grid_size_pixels["width"]+2*self._grid_position_pixels[0], "height": self._grid_size_pixels["height"]+2*self._grid_position_pixels[1]}
        
        self._colors = {"background": (230, 230, 230), "grid_line": (30, 30, 30), "I": (0, 240, 240), "O": (240, 240, 0), "T": (160, 0, 240), "S": (0, 240, 0), "Z": (240, 0, 0), "J": (0, 0, 240), "L": (240, 160, 0)}

        self._screen = pygame.display.set_mode((screen_size["width"], screen_size["height"]))
        pygame.display.set_caption("Tetris")
        
        self._screen.fill(self._colors["background"])
        
    
    # Can be made faster: draw the colors first, then the external rectangle and the internal grid using pygame.draw.lines (less redundancy in drawing lines: gain approx 0.3 ms per redraw)
    def draw_grid(self, grid):
        """Draws the whole grid on the screen."""
        for line in range(grid.visible_size["height"]):
            for col in range(grid.visible_size["width"]):
                if grid[line, col] != " ":
                    pygame.draw.rect(self._screen, self._colors[grid[line, col]], (self._grid_position_pixels[0]+col*self._grid_case_size_pixels, self.grid_position_pixels[1]+line*self._grid_case_size_pixels, self._grid_case_size_pixels, self._grid_case_size_pixels), 0)
                
                pygame.draw.rect(self._screen, self._colors["grid_line"], (self._grid_position_pixels[0]+col*self._grid_case_size_pixels, self._grid_position_pixels[1]+line*self._grid_case_size_pixels, self._grid_case_size_pixels, self._grid_case_size_pixels), self._grid_internal_line_width)
    
        pygame.draw.rect(self._screen, self._colors["grid_line"], (*self._grid_position_pixels, self._grid_size_pixels["width"], self._grid_size_pixels["height"]), self._grid_external_line_width)



