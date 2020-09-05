# -*- coding: utf-8 -*-

import pygame
from pygame.locals import QUIT, KEYDOWN, KEYUP, K_c, K_x, K_z, K_LEFT, K_RIGHT, K_UP, K_LSHIFT, K_RSHIFT, K_LCTRL, K_RCTRL

from constants.game import REFRESH_PERIOD, UPDATE_EVENT, DAS_DELAY, DAS_RATE, LOCK_DELAY, FIXED_GOAL
from grid import Grid
from graphics.graphics import Window
from random_bag import RandomBag
from tetromino import Tetromino


class Game:
    """Class Game. Class representing the game engine."""

    def __init__(self):
        """Constructor for the class Game."""        
        self._grid = Grid()
        self._window = Window()
        self._random = RandomBag()
        
        self._swap_allowed = True
        self._keys_down = {}
        
        self._held_tetromino = None
        self._next_queue = None
        self._current_tetromino = None
        self._spawn_tetromino()
        self._score = 0
        self._level = 1
        self._goal = FIXED_GOAL
                
        pygame.init()
        pygame.time.set_timer(UPDATE_EVENT, REFRESH_PERIOD)
        pygame.key.set_repeat(DAS_DELAY, DAS_RATE)

        
        
    def __del__(self):
        """Destructor for the class Game."""
        pygame.quit()
        
    
    def _spawn_tetromino(self):
        """Gets the next tetromino to be spawned from the random generator, and
        attenpts spawning it. If coullisions allow it to spawn there, returns True, 
        otherwise returns False (block out)."""
        current_piece, self._next_queue = self._random.next_pieces()
        self._current_tetromino = Tetromino(current_piece)  
        self._fall_tetromino()


    def _fall_tetromino(self):
        """If possible, moves the tetromino down. If not possible, starts a timer
        that when reaches LOCK_DELAY locks the tetromino in place."""
        if not self._current_tetromino.move("down", self._grid):
            if self._current_tetromino.lock_counter >= LOCK_DELAY:
                score = self._grid.lock_down(self._current_tetromino)
                self._score += score
                self._goal -= score
                if self._goal <= 0:
                    self._level += 1
                    self._goal = FIXED_GOAL
                self._spawn_tetromino()
                self._swap_allowed = True

    
    def _swap_held_tetromino(self):
        """Performs the swap beween the current tetromino and the held tetromino,
        if it is currently allowed."""             
        if self._swap_allowed:
            old_held = self._held_tetromino
            self._held_tetromino = self._current_tetromino.letter

            if old_held == None:
                self._spawn_tetromino()
            else:
                self._current_tetromino = Tetromino(old_held)
            
            self._swap_allowed = False
    
    
    def _key_pressed(self, key):
        """Reacts to key being pressed, except if it is being held (with the
        only exception of right and left arrow). Updates self._keys_down to
        say key is being pressed."""
        key_held = self._keys_down.get(key, False)
        self._keys_down[key] = True
        
        if key == K_LEFT:
            self._current_tetromino.move("left", self._grid)
        elif key == K_RIGHT:
            self._current_tetromino.move("right", self._grid)
        elif not key_held:
            if key == K_c or key == K_LSHIFT or key == K_RSHIFT:
                self._swap_held_tetromino()
            elif key == K_x or key == K_UP:
                self._current_tetromino.rotate("clockwise", self._grid)
            elif key == K_z or key == K_LCTRL or key == K_RCTRL:
                self._current_tetromino.rotate("anticlockwise", self._grid)
                
        
    def _key_released(self, key):
        """Reacts to the user releasing a key."""
        self._keys_down[key] = False


    def run(self):
        """Runs a complete game."""
        running = True
        
        # DEBUG:
        a = pygame.time.Clock()
        l = []
        ####################
        
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                if event.type == KEYDOWN:
                    self._key_pressed(event.key)
                elif event.type == KEYUP:
                    self._key_released(event.key) 
                elif event.type == UPDATE_EVENT:
                    self._fall_tetromino()
                
                #DEBUG
                l.append(a.tick())
                print(a.get_fps())
                ###################
                
            self._window.update(current_grid=self._grid,
                                current_tetromino=self._current_tetromino,
                                queue=self._next_queue, held=self._held_tetromino,
                                score=self._score, level=self._level, goal=self._goal)
        
        # DEBUG:
        print("Min: {}".format(min(l)))
        print("Max: {}".format(max(l)))
        print("Mean: {}".format(sum(l)/len(l)))
        ####################

