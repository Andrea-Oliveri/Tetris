# -*- coding: utf-8 -*-

from tetrominos.tetromino import Tetromino

class J_Tetromino(Tetromino):
    """Class J_Tetromino. Class inheriting from abstract class Tetromino representing
    the J tetromino."""
    
    def __init__(self):
        """Constructor for the class J_Tetromino."""
        maps = {"DEG_0"  : [[1,0,0],
                            [1,1,1],
                            [0,0,0]],
                
                "DEG_90" : [[0,1,1],
                            [0,1,0],
                            [0,1,0]],
                
                "DEG_180": [[0,0,0],
                            [1,1,1],
                            [0,0,1]],
                
                "DEG_270": [[0,1,0],
                            [0,1,0],
                            [1,1,0]] }
        
        Tetromino.__init__(self, maps, "J")

    def rotate(self, direction, grid):
        """Implementation of the rotate method for the J_Tetromino."""
        raise NotImplementedError
    