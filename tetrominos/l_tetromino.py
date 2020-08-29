# -*- coding: utf-8 -*-

from tetrominos.tetromino import Tetromino

class L_Tetromino(Tetromino):
    """Class L_Tetromino. Class inheriting from abstract class Tetromino representing
    the L tetromino."""
    
    def __init__(self):
        """Constructor for the class L_Tetromino."""
        maps = {"DEG_0"  : [[0,0,1],
                            [1,1,1],
                            [0,0,0]],
                
                "DEG_90" : [[0,1,0],
                            [0,1,0],
                            [0,1,1]],
                
                "DEG_180": [[0,0,0],
                            [1,1,1],
                            [1,0,0]],
                
                "DEG_270": [[1,1,0],
                            [0,1,0],
                            [0,1,0]] }
        
        Tetromino.__init__(self, maps, "L")

    def rotate(self, direction, grid):
        """Implementation of the rotate method for the L_Tetromino."""
        raise NotImplementedError
    
