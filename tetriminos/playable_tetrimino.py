# -*- coding: utf-8 -*-

from math import floor

from tetriminos.tetrimino import Tetrimino
from tetriminos.ghost_tetrimino import GhostTetrimino
from constants import grid
from constants.tetrimino import ROTATION_TESTS, GRAVITY, SOFT_DROP_FACTOR, HARD_DROP_GRAVITY


class PlayableTetrimino(Tetrimino):
    """Class PlayableTetrimino. Class representing all playable tetriminos.
    Tetriminos spawn in rows 20 and 21, and are centered horizontally, eventually rounded to the left.
    If possible, they immediately drop one block upon spawning.
    _blocked_out attribute is only needed to see if the tetrimino already collides with a block upon
    spawning, which resuts in the game ending."""
    
    def __init__(self, letter, current_grid):
        """Constructor for the class Tetrimino."""
        Tetrimino.__init__(self, letter, "DEG_0")
        self._position = [grid.SPAWN_ROW, floor((grid.SIZE["width"]-self._MAPS_SIZE["width"])/2)]
        self._blocked_out = self._collision(self._position, self._rotation, current_grid)
        if not self._blocked_out:
            self._initial_drop(current_grid)
        self._decimal_drop = 0.
        self._ghost_position = self._compute_ghost_position(current_grid)
        self._lock_counter = 0
        self._last_movement_is_rotation = False
        
    def _get_lock_counter(self):
        """Special function that allows to get the attribute _lock_counter from the exterior."""
        return int(self._lock_counter)
    
    def _get_ghost(self):
        """Special function that allows to get the corresponding GhostTetrimino from the exterior."""
        return GhostTetrimino(self._letter, self._ghost_position, self._rotation)
    
    def _get_blocked_out(self):
        """Special function that allows to get the attribute _blocked_out from the exterior."""
        return self._blocked_out
    
    """Definition of a properties for parameter _lock_counter. This parameter can
    only be get from the exteriour, not set nor deleted."""
    lock_counter = property(_get_lock_counter)

    """Definition of a properties for parameter _ghost. This parameter can
    only be get from the exteriour, not set nor deleted."""
    ghost = property(_get_ghost)
    
    """Definition of a properties for parameter _blocked_out. This parameter can
    only be get from the exteriour, not set nor deleted."""
    blocked_out = property(_get_blocked_out)

    def _collision(self, position, rotation, current_grid):
        """Returns True if moving the tetrimino to the position and rotation 
        passed as parameter resulted in a collision, False otherwise."""
        for line in range(self.MAPS_SIZE["height"]):
            for col in range(self.MAPS_SIZE["width"]):
                grid_line = position[0]-line
                grid_col = position[1]+col
                if self._MAPS[rotation][line][col]:
                    if grid_line < 0 or grid_col < 0 or grid_col >= grid.SIZE["width"] or not current_grid.is_empty(grid_line, grid_col):
                        return True                
        return False
    
    def _touching(self, current_grid):
        """Returns True if the tetrimino is touching the a block of the grid which
        would impede his movement down, False otherwise."""
        return self._collision([self.position[0]-1, self.position[1]], self._rotation, current_grid)
        
    def _compute_ghost_position(self, current_grid):
        """Returns the position that the ghost piece can take."""
        line = self._position[0]
        
        while line > 0:
            if not self._collision([line-1, self._position[1]], self._rotation, current_grid):
                line -= 1
            else:
                break
        
        return [line, self._position[1]]

    def _initial_drop(self, current_grid):
        """Function that drops the tetrimino one case if collisions allow it.
        Only called when the tetrimino is spawned."""
        new_position = self.position
        new_position[0] -= 1
        
        if not self._collision(new_position, self._rotation, current_grid):
            self._position = new_position

    def rotate(self, direction, current_grid):
        """Rotates the tetrimino in the desired direction ("clockwise" or "anticlockwise")."""
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
        
        rotation_success = False
        
        if self._letter == "O":
            self._rotation = new_rotation
            self._lock_counter = 0
            self._last_movement_is_rotation = True
            rotation_success = True
        
        else:
            for delta_position in ROTATION_TESTS[self._letter][(self._rotation, new_rotation)]:
                new_position = [self._position[0] + delta_position[0], self._position[1] + delta_position[1]]
                if not self._collision(new_position, new_rotation, current_grid):
                    self._position = new_position
                    self._rotation = new_rotation
                    self._ghost_position = self._compute_ghost_position(current_grid)
                    self._lock_counter = 0
                    self._last_movement_is_rotation = True 
                    rotation_success = True
                    break
                
        return rotation_success
    
    
    def move_sideways(self, direction, current_grid):
        """Moves the tetrimino either "left" or "right" if collision allow it."""
        new_position = self.position
                
        if direction == "left":
            new_position[1] -= 1
        elif direction == "right":
            new_position[1] += 1
            
        move_success = False
        
        if not self._collision(new_position, self._rotation, current_grid):
            self._position = new_position
            self._ghost_position = self._compute_ghost_position(current_grid)
            self._lock_counter = 0
            self._last_movement_is_rotation = False
            move_success = True
            
        return move_success
    
    
    def move_down(self, current_grid, level, drop_type="normal"):
        """Moves the tetrimino down if collisions allow it.
        The level parameter is needed to know what value of gravity to use.
        We can move with three types of drops: "normal", "soft" or "hard"."""
        gravity = None
        if drop_type == "normal":
            gravity = GRAVITY[level]
        elif drop_type == "soft":
            gravity = SOFT_DROP_FACTOR*GRAVITY[level]
        elif drop_type == "hard":
            gravity = HARD_DROP_GRAVITY
        else:
            raise TypeError("PlayableTetrimino.move_down() parameter drop_type must be either normal, soft or hard")
        
        old_line_position = self.position[0]
        
        total_decimal_drop = self._decimal_drop + gravity
        integer_drop = int(total_decimal_drop)
        self._decimal_drop = total_decimal_drop - integer_drop
        
        if self._touching(current_grid):
            self._lock_counter += 1
        else:
            dropping = True
            while integer_drop > 0 and dropping:
                new_position = self.position
                new_position[0] -= 1
                
                if not self._collision(new_position, self._rotation, current_grid):
                    self._position = new_position
                    self._last_movement_is_rotation = False
                else:
                    dropping = False
                    
                integer_drop -= 1
                
            self._lock_counter = 0
        
        return old_line_position - self.position[0], False
    
    def detect_3_corner_T_spin(self, current_grid):
        """Returns True if the tetrimino is a T, last movement was rotation and
        center piece of T has 3 diagonally adjacent blocks."""
        
        if not (self._letter == "T" and self._last_movement_is_rotation):
            return False
        
        n_filled_corners = 4
        for relative_line in (0, 2):
            for relative_col in (0, 2):
                if current_grid.is_empty(self._position[0] - relative_line, self._position[1] + relative_col):
                    n_filled_corners -= 1
        
        return n_filled_corners >= 3