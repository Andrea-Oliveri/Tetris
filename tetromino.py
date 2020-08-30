# -*- coding: utf-8 -*-

from math import floor

from constants import grid
from constants.tetromino import *


class Tetromino:
    """Class Tetromino. Class defining the general interface of all tetrominos.
    Tetrominos spawn in rows 20 and 21, and are centered horizontally, eventually rounded to the left."""
    
    def __init__(self, letter):
        """Constructor for the class Tetromino."""
        self._letter = str(letter)
        self._MAPS = MAPS[letter]
        self._MAPS_SIZE = {"height": len(self._MAPS["DEG_0"]), "width": len(self._MAPS["DEG_0"][0])}
        self._rotation = "DEG_0"
        self._position = [grid.SPAWN_ROW, floor((grid.SIZE["width"]-self._MAPS_SIZE["width"])/2)]

    def _get_MAPS_SIZE(self):
        """Special function that allows to get the attribute _MAPS_SIZE from the exterior."""
        return dict(self._MAPS_SIZE)

    def _get_position(self):
        """Special function that allows to get the attribute _position from the exterior."""
        return list(self._position)
    
    def _get_letter(self):
        """Special function that allows to get the attribute _letter from the exterior."""
        return str(self._letter)

    def __getitem__(self, indeces):
        """Special function that allows to get items of attribute _MAPS from the exterior."""
        return self._MAPS[self._rotation][indeces[0]][indeces[1]]

    """Definition of a properties for parameter _MAPS_SIZE. This parameter can
    only be get from the exteriour, not set nor deleted."""
    MAPS_SIZE = property(_get_MAPS_SIZE)
    
    """Definition of a properties for parameter _position. This parameter can
    only be get from the exteriour, not set nor deleted."""
    position = property(_get_position)

    """Definition of a properties for parameter _letter. This parameter can
    only be get from the exteriour, not set nor deleted."""
    letter = property(_get_letter)
    
    def rotate(self, direction, grid):
        """Rotates the tetromino in the desired direction ("clockwise" or "anticlockwise")."""
        raise NotImplementedError
    
    def move(self, direction, grid):
        """Moves the tetromino in the desired direction ("left" or "right" or "down").
        Returns True if the tetromino was moved and False if collisions did not allow it."""
        self._position[0]-=1