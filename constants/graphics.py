# -*- coding: utf-8 -*-

from constants import grid

# Constants defining the sizes in pixels of several graphical elements. 
GRID_SQUARE_SIZE_PIXELS = 30
GRID_SIZE_PIXELS = {"width": grid.VISIBLE_SIZE["width"]*GRID_SQUARE_SIZE_PIXELS,
                    "height": grid.VISIBLE_SIZE["height"]*GRID_SQUARE_SIZE_PIXELS}

# Constants defining the positions in pixels of several graphical elements. 
GRID_POSITION_PIXELS = (10, 10)

# Constants defining the width in pixels of several graphical elements.
GRID_EXTERNAL_LINE_WIDTH_PIXELS = 3
GRID_INTERNAL_LINE_WIDTH_PIXELS = 1

# Constants storing colors of several graphical elements.
COLORS = {"background": (230, 230, 230), "grid_line": (30, 30, 30),
          "I": (0, 240, 240), "O": (240, 240, 0), "T": (160, 0, 240),
          "S": (0, 240, 0), "Z": (240, 0, 0), "J": (0, 0, 240), "L": (240, 160, 0)}
