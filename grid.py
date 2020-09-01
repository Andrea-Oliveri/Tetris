# -*- coding: utf-8 -*-

from constants.grid import SIZE, VISIBLE_SIZE, SPAWN_ROW

class Grid:
    """Class Grid. Class storing the current state of the grid and its parameters.
    Coordinate system chosen: (0,0) is at bottom left, first coordinate is row and
    second coordinate is column."""
    
    def __init__(self):
        """Constructor for the class Grid."""
        self._grid = [[" " for _ in range(SIZE["width"])] for _ in range(SIZE["height"])]
    
    def __getitem__(self, index):
        """Special function that allows to get items of attribute _grid from the exterior."""
        return list(self._grid[index])
    
    def is_empty(self, line, col):
        """Function that returns True if the case described by indeces parameter is empty,
        False otherwise."""
        return self._grid[line][col] == " "
    
    def lock_down(self, tetromino):
        """Locks the tetromino in the grid into place. Returns True if the tetromino locked
        down inside the visible area, False otherwise (Lock Out)."""       
        for line in range(tetromino.MAPS_SIZE["height"]):
            for col in range(tetromino.MAPS_SIZE["width"]):
                grid_line = tetromino.position[0]-line-1
                grid_col = tetromino.position[1]+col
                if tetromino[line][col]:
                    self._grid[grid_line][grid_col] = tetromino.letter

    # DEBUG:
    def __repr__(self):
        lines = [",".join(line) for line in self._grid[::-1]]
        lines = [str(39-i) + "   " + line for i, line in enumerate(lines)]
        return "\n".join(lines)
            