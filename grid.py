# -*- coding: utf-8 -*-

class Grid:
    """Class Grid. Class storing the current state of the grid and its parameters.
    Coordinate system chosen: (0,0) is at bottom left, first coordinate is row and
    second coordinate is column.
    Tetrominos spawn in rows 20 and 21 and only rows 0 to 19 are visible."""
    
    def __init__(self):
        """Constructor for the class Grid."""
        self._size = {"width": 10, "height": 40}
        self._grid = [[" " for col in range(self.size["width"])] for line in range(self.size["height"])]
        self._visible_size = {"width": 10, "height": 20}

    def _get_size(self):
        """Special function that allows to get the attribute _size from the exterior."""
        return self._size
    
    def _get_visible_size(self):
        """Special function that allows to get the attribute _visible_size from the exterior."""
        return self._visible_size
    
    def __getitem__(self, indeces):
        """Special function that allows to get items of attribute _grid from the exterior."""
        return self._grid[indeces[0]][indeces[1]]
    
    
    """Definition of a properties for parameter _size. This parameter can
    only be get from the exteriour, not set nor deleted."""
    size = property(_get_size)
    
    """Definition of a properties for parameter _visible_size. This parameter can
    only be get from the exteriour, not set nor deleted."""
    visible_size = property(_get_visible_size)
     

    ######### JUST FOR DEBUG
    def __repr__(self):
        return "\n".join([",".join(line) for line in grid[::-1]])



    
