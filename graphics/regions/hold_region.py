# -*- coding: utf-8 -*-

from constants.graphics import HOLD_SQUARE_SIZE_PIXELS, HOLD_FONT_SIZE
from graphics.regions.region import Region
from graphics import utils


class HoldRegion(Region):
    """Class HoldRegion. Class representing the region of the window where the held piece is displayed."""
        
    def __init__(self):
        """Overload of constructor for HoldRegion class."""
        Region.__init__(self)
        self._text = utils.draw_text("Held Piece", HOLD_FONT_SIZE)
        
    
    def update(self, **kwargs):
        """Implementation of the update method for the HoldRegion."""
        if len(kwargs.keys()) != 1 or "held" not in kwargs:
            raise TypeError("HoldRegion.update() takes exactly one kwarg: held")
            
        held = kwargs["held"]
    
        if held != None:
            piece = utils.draw_outside_tetromino(held, HOLD_SQUARE_SIZE_PIXELS)
            self._surface = utils.merge_surfaces_vertically([self._text, piece])
        else:
            self._surface = self._text
