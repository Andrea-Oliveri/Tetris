# -*- coding: utf-8 -*-

import pygame
from pygame.locals import QUIT, KEYDOWN, KEYUP, K_c, K_x, K_z, K_r, K_SPACE, K_LEFT, K_RIGHT, K_UP, K_DOWN, K_LSHIFT, K_RSHIFT, K_LCTRL, K_RCTRL, K_ESCAPE, K_F1

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
        pygame.init()
        
        self._grid = Grid()
        self._window = Window()
        self._random = RandomBag()
        self._sound = SoundEngine()
        
        self._running = True
        self._topped_out = False
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
        if self._current_tetromino.blocked_out:
            self._topped_out = True


    def _fall_tetromino(self):
        """If the game is running, calls a method so that tetromino moves down
        if possible, then checks the lock counter of the tetromino and, if
        larger than LOCK_DELAY, locks it into place, updates score, goal,
        level and lines cleared and spawns new tetromino."""
        if not self._running:
            return 
        
        self._window.notify_event("movement")
        
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
            
            self._window.notify_event("lines_cleared")
            self._window.notify_event("score_increased")
            
            if lock_out:
                self._topped_out = True
            else:
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
        only exception of right and left arrow) and, depending on the key,
        if the game is paused. Updates self._keys_down to say key is being pressed."""
        key_held = self._keys_down.get(key, False)
        self._keys_down[key] = True
        
        if key == K_LEFT and self._running:
            self._current_tetromino.move_sideways("left", self._grid)
            self._window.notify_event("movement")
        elif key == K_RIGHT and self._running:
            self._current_tetromino.move_sideways("right", self._grid)
            self._window.notify_event("movement")
        elif not key_held:
            if (key == K_c or key == K_LSHIFT or key == K_RSHIFT) and self._running:
                self._swap_held_tetromino()
                self._window.notify_event("held_swap")
            elif (key == K_x or key == K_UP) and self._running:
                self._current_tetromino.rotate("clockwise", self._grid)
                self._window.notify_event("movement")
            elif (key == K_z or key == K_LCTRL or key == K_RCTRL) and self._running:
                self._current_tetromino.rotate("anticlockwise", self._grid)
                self._window.notify_event("movement")
            elif key == K_r:
                self._sound.change_music()
            elif key == K_ESCAPE or key == K_F1:
                self._running = not self._running
                
        
    def _key_released(self, key):
        """Reacts to the user releasing a key."""
        self._keys_down[key] = False


    def run(self):
        """Runs a complete game."""
        
        # DEBUG:
        a = pygame.time.Clock()
        l = []
        update_time = []
        ####################
        
        window_open = True
        
        while not self._topped_out and window_open:
            frame_updated = False
            for event in pygame.event.get():
                if event.type == QUIT:
                    window_open = False
                if event.type == KEYDOWN:
                    self._key_pressed(event.key)
                elif event.type == KEYUP:
                    self._key_released(event.key) 
                elif event.type == FRAME_EVENT:
                    self._fall_tetromino()
                    if not frame_updated:
                        #DEBUG
                        c = pygame.time.Clock()
                        c.tick()
                        ###########
                        self._window.update(current_grid=self._grid,
                                            current_tetromino=self._current_tetromino,
                                            queue=self._next_queue, held=self._held_tetromino,
                                            score=self._score, level=self._level,
                                            goal=self._goal, lines=self._lines_cleared)
                        #DEBUG
                        update_time.append(c.tick())
                        ###########
                        frame_updated = True
                    
        
                #DEBUG
                l.append(a.tick())
                ###################
        
        while window_open:
            frame_updated = False
            for event in pygame.event.get():
                if event.type == QUIT:
                    window_open = False
                elif event.type == FRAME_EVENT and not frame_updated:
                    self._window.update(current_grid=self._grid,
                                        current_tetromino=self._current_tetromino,
                                        queue=self._next_queue, held=self._held_tetromino,
                                        score=self._score, level=self._level,
                                        goal=self._goal, lines=self._lines_cleared)
                    frame_updated = True
                    
        
        # DEBUG:    
        import matplotlib.pyplot as plt
        string = "Total:\n"
        string += "    Min: {}\n".format(min(l))
        string += "    Max: {} ({})\n".format(max(l), len([1 for e in l if e == max(l)]))
        string += "    Mean: {}\n".format(sum(l)/len(l))
        string += "    Number measures: {}\n".format(len(l))
        string += "Update Time:\n"
        string += "    Min: {}\n".format(min(update_time))
        string += "    Max: {} ({})\n".format(max(update_time), len([1 for e in update_time if e == max(update_time)]))
        string += "    Mean: {}\n".format(sum(update_time)/len(update_time))
        string += "    Number measures: {}\n\n\n".format(len(update_time))
        print(string)
        plt.hist(l, 100)
        ####################

