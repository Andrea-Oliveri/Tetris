# -*- coding: utf-8 -*-

from tetrominos.tetromino import Tetromino


class GhostTetromino(Tetromino):
    """Class GhostTetromino. Class representing the ghost tetrominos."""
    
    def __init__(self, letter, position, rotation):
        """Constructor for the class GhostTetromino."""
        Tetromino.__init__(self, letter, rotation)
        self._position = list(position)