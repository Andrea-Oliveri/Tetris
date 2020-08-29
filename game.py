# -*- coding: utf-8 -*-

import pygame
from pygame.locals import QUIT

from constants.game import *
from grid import Grid
from graphics import Graphics
from random_bag import RandomBag
from tetrominos.i_tetromino import I_Tetromino
from tetrominos.j_tetromino import J_Tetromino
from tetrominos.l_tetromino import L_Tetromino
from tetrominos.o_tetromino import O_Tetromino
from tetrominos.s_tetromino import S_Tetromino
from tetrominos.t_tetromino import T_Tetromino
from tetrominos.z_tetromino import Z_Tetromino



class Game:
    """Class Game. Class representing the game engine."""

    def __init__(self):
        """Constructor for the class Game."""
        self._update_period = 200
        
        self._grid = Grid()
        self._graphics = Graphics()
        self._random = RandomBag()
        
        self._next_queue = None
        self._current_tetromino = None
        self._update_queue_and_current_tetromino()
        
        pygame.init()
        pygame.time.set_timer(UPDATE_EVENT, self._update_period)
        
        
    def __del__(self):
        """Destructor for the class Game."""
        pygame.quit()
        
    
    def _update_queue_and_current_tetromino(self):
        current_piece, self._next_queue = self._random.next_pieces()
        
        if current_piece == "I":
            self._current_tetromino = I_Tetromino()
        elif current_piece == "O":
            self._current_tetromino = O_Tetromino()
        elif current_piece == "T":
            self._current_tetromino = T_Tetromino()        
        elif current_piece == "S":
            self._current_tetromino = S_Tetromino()
        elif current_piece == "Z":
            self._current_tetromino = Z_Tetromino()
        elif current_piece == "J":
            self._current_tetromino = J_Tetromino()            
        elif current_piece == "L":
            self._current_tetromino = L_Tetromino()      
        else:
            raise TypeError(current_piece + " not in [I, O, T, S, Z, J, L]")

            
    def run(self):
        """Runs a complete game."""
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                if event.type == UPDATE_EVENT:
                    self._current_tetromino.move("down", self._grid)
                    if self._current_tetromino.position[0] < 0:
                        self._update_queue_and_current_tetromino()
                        
            self._graphics.draw_all(self._grid, self._current_tetromino, self._next_queue, None, None, None, None)

