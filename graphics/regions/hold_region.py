# -*- coding: utf-8 -*-

from constants.graphics import HOLD_SQUARE_SIZE_PIXELS, HOLD_FONT_SIZE, HOLD_SURFACE_HEIGHT
from graphics.regions.region import Region
from graphics import utils


class HoldRegion(Region):
    """Class HoldRegion. Class representing the region of the game screen where the 
    held piece is displayed."""
        
    def __init__(self):
        """Overload of constructor for HoldRegion class."""
        Region.__init__(self)
        self._text = utils.draw_text("Held Piece", HOLD_FONT_SIZE)
        
    
    def update(self, **kwargs):
        """Implementation of the update method for the HoldRegion."""
        if len(kwargs.keys()) != 1 or "held" not in kwargs:
            raise TypeError("HoldRegion.update() takes exactly one kwarg: held")
            
        held = kwargs["held"]
    
        surfaces = [self._text]
        if held != None:
            piece = utils.draw_outside_tetrimino(held, HOLD_SQUARE_SIZE_PIXELS)
            surfaces.append(piece)
            
        self._surface = utils.merge_surfaces_vertically(surfaces, total_height = HOLD_SURFACE_HEIGHT)