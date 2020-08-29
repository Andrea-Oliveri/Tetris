# -*- coding: utf-8 -*-

from tetrominos.tetromino import Tetromino

class T_Tetromino(Tetromino):
    """Class T_Tetromino. Class inheriting from abstract class Tetromino representing
    the T tetromino."""
    
    def __init__(self):
        """Constructor for the class T_Tetromino."""
        maps = {"DEG_0"  : [[0,1,0],
                            [1,1,1],
                            [0,0,0]] ,
                
                "DEG_90" : [[0,1,0],
                            [0,1,1],
                            [0,1,0]] ,
                
                "DEG_180": [[0,0,0],
                            [1,1,1],
                            [0,1,0]] ,
                
                "DEG_270": [[0,1,0],
                            [1,1,0],
                            [0,1,0]] }
        
        Tetromino.__init__(self, maps, "T")

    def rotate(self, direction, grid):
        """Implementation of the rotate method for the T_Tetromino."""
        raise NotImplementedError
    