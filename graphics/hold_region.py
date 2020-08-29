# -*- coding: utf-8 -*-

import pygame

from constants.graphics import COLORS
from graphics.region import Region


class HoldRegion(Region):
    """Class HoldRegion. Class representing the region of the window where the held piece is displayed."""
        
    def update(self, **kwargs):
        """Implementation of the update method for the HoldRegion."""
        if len(kwargs.keys()) != 1 or "held" not in kwargs:
            raise TypeError("HoldRegion.update() takes exactly one kwarg: held")
            
        held = kwargs["held"]
        
        self._surface.fill(COLORS["background"])

        if held != None:
            self._surface.fill(COLORS[held])