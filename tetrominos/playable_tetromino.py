# -*- coding: utf-8 -*-

from math import floor

from tetrominos.tetromino import Tetromino
from tetrominos.ghost_tetromino import GhostTetromino
from constants import grid
from constants.tetromino import ROTATION_TESTS, GRAVITY


class PlayableTetromino(Tetromino):
    """Class PlayableTetromino. Class representing all playable tetrominos.
    Tetrominos spawn in rows 20 and 21, and are centered horizontally, eventually rounded to the left."""
    
    def __init__(self, letter, current_grid):
        """Constructor for the class Tetromino."""
        Tetromino.__init__(self, letter, "DEG_0")
        self._position = [grid.SPAWN_ROW, floor((grid.SIZE["width"]-self._MAPS_SIZE["width"])/2)]
        self._decimal_drop = 0.
        self._ghost_position = self._compute_ghost_position(current_grid)
        self._lock_counter = 0

    def _get_lock_counter(self):
        """Special function that allows to get the attribute _lock_counter from the exterior."""
        return int(self._lock_counter)
    
    def _get_ghost(self):
        """Special function that allows to get the corresponding GhostTetromino from the exterior."""
        return GhostTetromino(self._letter, self._ghost_position, self._rotation)
    
    """Definition of a properties for parameter _lock_counter. This parameter can
    only be get from the exteriour, not set nor deleted."""
    lock_counter = property(_get_lock_counter)

    """Definition of a properties for parameter _ghost. This parameter can
    only be get from the exteriour, not set nor deleted."""
    ghost = property(_get_ghost)

    def _collision(self, position, rotation, current_grid):
        """Returns True if moving the tetromino to the position and rotation 
        passed as parameter resulted in a collision, False otherwise."""
        for line in range(self.MAPS_SIZE["height"]):
            for col in range(self.MAPS_SIZE["width"]):
                grid_line = position[0]-line-1
                grid_col = position[1]+col
                if self._MAPS[rotation][line][col]:
                    if grid_line < 0 or grid_col < 0 or grid_col >= grid.SIZE["width"] or not current_grid.is_empty(grid_line, grid_col):
                        return True                
        return False

    def _compute_ghost_position(self, current_grid):
        """Returns the position that the ghost piece can take."""
        line = self._position[0]
        
        while line > 0:
            if not self._collision([line-1, self._position[1]], self._rotation, current_grid):
                line -= 1
            else:
                break
        
        return [line, self._position[1]]

    def rotate(self, direction, current_grid):
        """Rotates the tetromino in the desired direction ("clockwise" or "anticlockwise")."""
        new_rotation = None
        if direction == "clockwise":
            if self._rotation == "DEG_0":
                new_rotation = "DEG_90"
            elif self._rotation == "DEG_90":
                new_rotation = "DEG_180"
            elif self._rotation == "DEG_180":
                new_rotation = "DEG_270"
            elif self._rotation == "DEG_270":
                new_rotation = "DEG_0"
        elif direction == "anticlockwise":
            if self._rotation == "DEG_0":
                new_rotation = "DEG_270"
            elif self._rotation == "DEG_90":
                new_rotation = "DEG_0"
            elif self._rotation == "DEG_180":
                new_rotation = "DEG_90"
            elif self._rotation == "DEG_270":
                new_rotation = "DEG_180"
        
        if self._letter == "O":
            self._rotation = new_rotation
            return
    
        for delta_position in ROTATION_TESTS[self._letter][(self._rotation, new_rotation)]:
            new_position = [self._position[0] + delta_position[0], self._position[1] + delta_position[1]]
            if not self._collision(new_position, new_rotation, current_grid):
                self._position = new_position
                self._rotation = new_rotation
                self._ghost_position = self._compute_ghost_position(current_grid)
                break

    
    def move_down(self, current_grid, level):
        """Moves the tetromino down. The level parameter is needed to know what
        value of gravity to use. Returns True if the tetromino was moved and
        False if collisions did not allow it."""
        new_position = self.position
                
        new_decimal_drop = self._decimal_drop + GRAVITY[level]
        new_position[0] -= int(new_decimal_drop)
        new_decimal_drop -= int(new_decimal_drop)
        
        if not self._collision(new_position, self._rotation, current_grid):
            self._position = new_position
            self._decimal_drop = new_decimal_drop
            self._lock_counter = 0
            return True
        
        self._lock_counter += 1            
        return False
    
        
    def move_sideways(self, direction, current_grid):
        """Moves the tetromino either "left" or "right". Returns True if the
        tetromino was moved and False if collisions did not allow it."""
        new_position = self.position
                
        if direction == "left":
            new_position[1] -= 1
        elif direction == "right":
            new_position[1] += 1
        
        if not self._collision(new_position, self._rotation, current_grid):
            self._position = new_position
            self._ghost_position = self._compute_ghost_position(current_grid)
            return True
            
        return False
        