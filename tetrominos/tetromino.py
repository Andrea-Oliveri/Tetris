# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod


class Tetromino(ABC):
    """Class Tetromino. Abstract class defining the general interface of all tetrominos."""
    
    def __init__(self, position, rotation, maps):
        """Constructor for the class Tetromino."""
        self._position = list(position)
        self._rotation = list(rotation)
        self._maps = dict(maps)

    @abstractmethod
    def rotate(self, direction, grid):
        """Rotates the tetromino in the desired direction ("clockwise" or "anticlockwise")."""
        pass
    
    @abstractmethod
    def move(self, direction, grid):
        """Moves the tetromino in the desired direction ("left" or "right" or "down").
        Returns True if the tetromino was moved and False if collisions did not allow it."""
        pass
    
    def fall(self, grid):
        """Moves the tetromino to the lowest spot in the grid allowed by collisions."""
        while self.move("down", grid):
            pass        