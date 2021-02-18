# -*- coding: utf-8 -*-

from constants.grid import SIZE, VISIBLE_SIZE

class Grid:
    """Class Grid. Class storing the current state of the grid and its parameters.
    Coordinate system chosen: (0,0) is at bottom left, first coordinate is row and
    second coordinate is column."""
    
    def __init__(self):
        """Constructor for the class Grid."""
        self._grid = [[" " for _ in range(SIZE["width"])] for _ in range(SIZE["height"])] 
        self._grid[0] = ["O","O","O","O"," ","O","O","O","O","O"]
        self._grid[1] = ["O","O","O"," "," "," ","O","O","O","O"]
        self._grid[2] = [" "," "," "," "," ","O","O"," "," "," "]


    def __getitem__(self, index):
        """Special function that allows to get items of attribute _grid from the exterior."""
        return list(self._grid[index])
    
    def is_empty(self, line, col):
        """Function that returns True if the case described by indeces parameter is empty,
        False otherwise."""
        if line < 0 or line >= SIZE["height"] or col < 0 or col >= SIZE["width"]:
            return False
        
        return self._grid[line][col] == " "
    
    def lock_down(self, tetromino, level, score_keeper):
        """Locks the tetromino in the grid into place.
        Calls methods of score_keeper to add score obtained with this move, returns
        the cleared number of lines and True if the tetromino locked down outside 
        the visible area (Lock Out), False otherwise."""       
        lock_out = True
        
        for line in range(tetromino.MAPS_SIZE["height"]):
            for col in range(tetromino.MAPS_SIZE["width"]):
                grid_line = tetromino.position[0]-line
                grid_col = tetromino.position[1]+col
                if tetromino[line][col]:
                    self._grid[grid_line][grid_col] = tetromino.letter
                    if grid_line < VISIBLE_SIZE["height"]:
                        lock_out = False
                
        reward_tspin = tetromino.detect_3_corner_T_spin(self)
        lines_cleared = self._clear_lines()
        
        if lines_cleared:
            score_actions = {(1, False): "single", (2, False): "double", 
                             (3, False): "triple", (4, False): "tetris",
                             (1, True): "tspin_single", (2, True): "tspin_double", 
                             (3, True): "tspin_triple", (4, True): "tspin_tetris"}
            
            action = score_actions[lines_cleared, reward_tspin]
                        
            score_keeper.add_to_score(action, {"level": level})
        
            if self._all_empty():
                score_keeper.add_perfect_bonus_to_score(lines_cleared, level)       
        
        return lines_cleared, lock_out
    
    
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