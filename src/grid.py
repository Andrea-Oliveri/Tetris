# -*- coding: utf-8 -*-

from src.constants.grid import SIZE, VISIBLE_SIZE

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
        if line < 0 or line >= SIZE["height"] or col < 0 or col >= SIZE["width"]:
            return False
        
        return self._grid[line][col] == " "
    
    def lock_down(self, tetrimino):
        """Locks the tetrimino in the grid into place.
        Returns the cleared number of lines, if the tetrimino locked down outside 
        the visible area (Lock Out), if the grid is empty as a result of the line
        clears and if the player did a T-spin."""       
        lock_out = True
        
        for line in range(tetrimino.MAPS_SIZE["height"]):
            for col in range(tetrimino.MAPS_SIZE["width"]):
                grid_line = tetrimino.position[0]-line
                grid_col = tetrimino.position[1]+col
                if tetrimino[line][col]:
                    self._grid[grid_line][grid_col] = tetrimino.letter
                    if grid_line < VISIBLE_SIZE["height"]:
                        lock_out = False
                
        reward_tspin = tetrimino.detect_3_corner_T_spin(self)
        lines_cleared = self._clear_lines()
        
        # Only compute all_empty if there were line clears as otherwise it 
        # is surely False.
        all_empty = lines_cleared and self._all_empty()
        
        return lines_cleared, lock_out, all_empty, reward_tspin
    
    
    def _clear_lines(self):
        """Function that clears the complete lines in the grid and returns the obtained score."""
        lines_cleared = []
        
        for line in range(SIZE["height"]):
            if all([not self.is_empty(line, col) for col in range(SIZE["width"])]):
                lines_cleared.append(line)
        
        for line in sorted(lines_cleared, reverse=True):
            del self._grid[line]
            self._grid.append([" " for _ in range(SIZE["width"])])
        
        return len(lines_cleared)
            
    
    def _all_empty(self):
        """Function that returns True if the whole grid is empty, False otherwise."""
        return all([self.is_empty(0, col) for col in range(SIZE["width"])])