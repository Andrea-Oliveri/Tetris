# -*- coding: utf-8 -*-

from tetrominos.tetromino import Tetromino

class S_Tetromino(Tetromino):
    """Class S_Tetromino. Class inheriting from abstract class Tetromino representing
    the S tetromino."""
    
    def __init__(self):
        """Constructor for the class S_Tetromino."""
        maps = {"DEG_0"  : [[0,1,1],
                            [1,1,0],
                            [0,0,0]] ,
                
                "DEG_90" : [[0,1,0],
                            [0,1,1],
                            [0,0,1]] ,
                
                "DEG_180": [[0,0,0],
                            [0,1,1],
                            [1,1,0]] ,
                
                "DEG_270": [[1,0,0],
                            [1,1,0],
                            [0,1,0]] }
        
        Tetromino.__init__(self, maps, "S")

    def rotate(self, direction, grid):
        """Implementation of the rotate method for the S_Tetromino."""
        raise NotImplementedError
    