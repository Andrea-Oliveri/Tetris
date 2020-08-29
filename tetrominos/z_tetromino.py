# -*- coding: utf-8 -*-

from tetrominos.tetromino import Tetromino

class Z_Tetromino(Tetromino):
    """Class Z_Tetromino. Class inheriting from abstract class Tetromino representing
    the Z tetromino."""
    
    def __init__(self):
        """Constructor for the class Z_Tetromino."""
        maps = {"DEG_0"  : [[1,1,0],
                            [0,1,1],
                            [0,0,0]] ,
                
                "DEG_90" : [[0,0,1],
                            [0,1,1],
                            [0,1,0]] ,
                
                "DEG_180": [[0,0,0],
                            [1,1,0],
                            [0,1,1]] ,
                
                "DEG_270": [[0,1,0],
                            [1,1,0],
                            [1,0,0]] }
        
        Tetromino.__init__(self, maps, "Z")

    def rotate(self, direction, grid):
        """Implementation of the rotate method for the Z_Tetromino."""
        raise NotImplementedError