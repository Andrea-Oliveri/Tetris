# -*- coding: utf-8 -*-

from tetriminos.tetrimino import Tetrimino


class GhostTetrimino(Tetrimino):
    """Class GhostTetrimino. Class representing the ghost tetriminos."""
    
    def __init__(self, letter, position, rotation):
        """Constructor for the class GhostTetrimino."""
        Tetrimino.__init__(self, letter, rotation)
        self._position = list(position)