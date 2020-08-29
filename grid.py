# -*- coding: utf-8 -*-

from constants.grid import *

class Grid:
    """Class Grid. Class storing the current state of the grid and its parameters.
    Coordinate system chosen: (0,0) is at bottom left, first coordinate is row and
    second coordinate is column."""
    
    def __init__(self):
        """Constructor for the class Grid."""
        self._grid = [[" " for col in range(SIZE["width"])] for line in range(SIZE["height"])]
    
    def __getitem__(self, indeces):
        """Special function that allows to get items of attribute _grid from the exterior."""
        return self._grid[indeces[0]][indeces[1]]
     

    ######### JUST FOR DEBUG
    def __repr__(self):
        return "\n".join([",".join(line) for line in self._grid[::-1]])



    
