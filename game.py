# -*- coding: utf-8 -*-

import pygame
from pygame.locals import QUIT, KEYDOWN, KEYUP, K_c, K_x, K_z, K_r, K_SPACE, K_LEFT, K_RIGHT, K_UP, K_DOWN, K_LSHIFT, K_RSHIFT, K_LCTRL, K_RCTRL

from constants.game import REFRESH_PERIOD, FRAME_EVENT, DAS_DELAY, DAS_RATE, LOCK_DELAY, FIXED_GOAL, LEVEL_CAP
from grid import Grid
from graphics.graphics import Window
from random_bag import RandomBag
from tetrominos.playable_tetromino import PlayableTetromino
from sound import SoundEngine


class Game:
    """Class Game. Class representing the game engine."""

    def __init__(self):
        """Constructor for the class Game."""        
        self._grid = Grid()
        self._window = Window()
        self._random = RandomBag()
        self._sound = SoundEngine()
        
        self._running = True
        self._finished = False
        self._swap_allowed = True
        self._keys_down = {}
        
        self._held_tetromino = None
        self._next_queue = None
        self._current_tetromino = None
        self._score = 0
        self._level = 1
        self._goal = FIXED_GOAL
        self._lines_cleared = 0
        self._spawn_tetromino()        
        
        pygame.init()
        pygame.time.set_timer(FRAME_EVENT, REFRESH_PERIOD)
        pygame.key.set_repeat(DAS_DELAY, DAS_RATE)
        
        
    def __del__(self):
        """Destructor for the class Game."""
        pygame.quit()
        
    
    def _spawn_tetromino(self):
        """Gets the next tetromino to be spawned from the random generator, and
        attenpts spawning it. If collisions allow it to spawn there, returns True, 
        otherwise returns False (block out)."""
        current_piece, self._next_queue = self._random.next_pieces()
        self._current_tetromino = PlayableTetromino(current_piece, self._grid)      


    def _fall_tetromino(self):
        """Calls a method so that tetromino moves down if possible, then 
        checks the lock counter of the tetromino and, if larger than LOCK_DELAY,
        locks it into place, updates score, goal, level and lines cleared
        and spawns new tetromino."""
        if self._keys_down.get(K_SPACE, False):
            self._current_tetromino.move_down(self._grid, self._level, "hard")
        elif self._keys_down.get(K_DOWN, False):
            self._current_tetromino.move_down(self._grid, self._level, "soft")
        else:
            self._current_tetromino.move_down(self._grid, self._level, "normal")        
                
        if self._current_tetromino.lock_counter >= LOCK_DELAY:
            score, lines_cleared, lock_out = self._grid.lock_down(self._current_tetromino)
            self._score += score
            self._lines_cleared += lines_cleared
            self._goal -= lines_cleared
            if self._goal <= 0:
                if self._level < LEVEL_CAP:
                    self._level += 1
                    self._goal = FIXED_GOAL
                else:
                    self._goal = 0
            
            if lock_out:
                self._finished = True
            
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
                self._current_tetromino = PlayableTetromino(old_held, self._grid)
            
            self._swap_allowed = False
    
    
    def _key_pressed(self, key):
        """Reacts to key being pressed, except if it is being held (with the
        only exception of right and left arrow). Updates self._keys_down to
        say key is being pressed."""
        key_held = self._keys_down.get(key, False)
        self._keys_down[key] = True
        
        if key == K_LEFT:
            self._current_tetromino.move_sideways("left", self._grid)
        elif key == K_RIGHT:
            self._current_tetromino.move_sideways("right", self._grid)
        elif not key_held:
            if key == K_c or key == K_LSHIFT or key == K_RSHIFT:
                self._swap_held_tetromino()
            elif key == K_x or key == K_UP:
                self._current_tetromino.rotate("clockwise", self._grid)
            elif key == K_z or key == K_LCTRL or key == K_RCTRL:
                self._current_tetromino.rotate("anticlockwise", self._grid)
            elif key == K_r:
                self._sound.change_music()
                
        
    def _key_released(self, key):
        """Reacts to the user releasing a key."""
        self._keys_down[key] = False


    def run(self):
        """Runs a complete game."""
        
        # DEBUG:
        a = pygame.time.Clock()
        l = []
        ####################
        
        while self._running and not self._finished:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self._running = False
                if event.type == KEYDOWN:
                    self._key_pressed(event.key)
                elif event.type == KEYUP:
                    self._key_released(event.key) 
                elif event.type == FRAME_EVENT:
                    self._fall_tetromino()
                    self._window.update(current_grid=self._grid,
                                        current_tetromino=self._current_tetromino,
                                        queue=self._next_queue, held=self._held_tetromino,
                                        score=self._score, level=self._level,
                                        goal=self._goal, lines=self._lines_cleared)
                    
                #DEBUG
                a.tick()
                l.append(a.get_fps())
                #print(a.get_fps())
                ###################
        
        # DEBUG:
        l = [val for val in l if val != 0]
        print("Min: {}".format(min(l)))
        print("Max: {}".format(max(l)))
        print("Mean: {}".format(sum(l)/len(l)))
        ####################

