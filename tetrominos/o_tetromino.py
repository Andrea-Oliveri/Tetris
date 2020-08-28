# -*- coding: utf-8 -*-

from tetrominos.tetromino import Tetromino

class O_Tetromino(Tetromino):
    """Class O_Tetromino. Class inheriting from abstract class Tetromino representing
    the O tetromino."""
    
    def __init__(self, position, rotation):
        """Constructor for the class O_Tetromino."""
        maps = {"DEG_0"  : [[1,1],
                            [1,1]],
                
                "DEG_90" : [[1,1],
                            [1,1]],
                
                "DEG_180": [[1,1],
                            [1,1]],
                
                "DEG_270": [[1,1],
                            [1,1]],
        
        Tetromino.__init__(self, position, rotation, maps)

    def rotate(self, direction, grid):
        """Implementation of the rotate method for the O_Tetromino."""
        raise NotImplmentedError
    
    def move(self, direction, grid):
        """Implementation of the move method for the O_Tetromino."""
        raise NotImplmentedError
