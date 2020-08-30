# -*- coding: utf-8 -*-

# Constants defining the sizes in pixels of several graphical elements. 
WINDOW_SIZE = (540,600)
HOLD_SQUARE_SIZE_PIXELS = 20
GRID_SQUARE_SIZE_PIXELS = 30
QUEUE_SQUARE_SIZE_PIXELS = HOLD_SQUARE_SIZE_PIXELS
ELEMENTS_MARGIN_PIXELS = 8

# Constants defining the width in pixels of several graphical elements.
GRID_EXTERNAL_LINE_WIDTH_PIXELS = 3
GRID_INTERNAL_LINE_WIDTH_PIXELS = 1

# Constant storing colors of several graphical elements.
COLORS = {"background": (230, 230, 230), "grid_line": (50, 50, 50), "text": (30, 30, 30),
          "I": (0, 240, 240), "O": (240, 240, 0), "T": (160, 0, 240),
          "S": (0, 240, 0), "Z": (240, 0, 0), "J": (0, 0, 240), "L": (240, 160, 0)}

# Constant storing the font used in the game window.
FONT = "comicsansms" 

# Constants storing the size of fonts used by several graphical elements. 
HOLD_FONT_SIZE = 20
QUEUE_FONT_SIZE = 20