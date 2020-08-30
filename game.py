# -*- coding: utf-8 -*-

import pygame
from pygame.locals import QUIT, KEYDOWN, K_c, K_LEFT, K_RIGHT, K_UP, K_DOWN

from constants.game import UPDATE_EVENT
from grid import Grid
from graphics.graphics import Window
from random_bag import RandomBag
from tetromino import Tetromino


class Game:
    """Class Game. Class representing the game engine."""

    def __init__(self):
        """Constructor for the class Game."""
        self._update_period = 200
        
        self._grid = Grid()
        self._window = Window()
        self._random = RandomBag()
        
        self._held_tetromino = None
        self._next_queue = None
        self._current_tetromino = None
        self._spawn_tetromino()
        self._score = 0
        self._level = 1
        self._goal = 5*self._level
        
        pygame.init()
        pygame.time.set_timer(UPDATE_EVENT, self._update_period)
        
        
    def __del__(self):
        """Destructor for the class Game."""
        pygame.quit()
        
    
    def _spawn_tetromino(self):
        """Gets the next tetromino to be spawned from the random generator,
        spawns it and updates the queue."""
        current_piece, self._next_queue = self._random.next_pieces()
        self._current_tetromino = Tetromino(current_piece)

            
    def run(self):
        """Runs a complete game."""
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                if event.type == KEYDOWN:
                    if event.key == K_c:
                        old_held = self._held_tetromino
                        self._held_tetromino = self._current_tetromino.letter

                        if old_held == None:
                            self._spawn_tetromino()
                        else:
                            self._current_tetromino = Tetromino(old_held)
                    elif event.key == K_LEFT:
                        self._current_tetromino.move("left", self._grid)
                    elif event.key == K_RIGHT:
                        self._current_tetromino.move("right", self._grid)
                    elif event.key == K_UP:
                        self._spawn_tetromino()
                        
                if event.type == UPDATE_EVENT:
                    self._current_tetromino.move("down", self._grid)
                        
            self._window.update(current_grid=self._grid,
                                current_tetromino=self._current_tetromino,
                                queue=self._next_queue, held=self._held_tetromino,
                                score=self._score, level=self._level, goal=self._goal)

