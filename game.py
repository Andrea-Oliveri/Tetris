# -*- coding: utf-8 -*-

import random

import pygame
from pygame.locals import QUIT

from grid import Grid
from graphics import Graphics


class Game:
    """Class Game. Class representing the game engine."""

    def __init__(self):
        """Constructor for the class Game."""
        self._grid = Grid()
        self._graphics = Graphics(self._grid)
        
        pygame.init()
        
    def __del__(self):
        """Destructor for the class Game."""
        pygame.quit()
        
    def run(self):
        """Runs a complete game."""
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
            
            self._graphics.draw_grid(self._grid)
            pygame.display.update()