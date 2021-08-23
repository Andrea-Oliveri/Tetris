# -*- coding: utf-8 -*-

from pygame.locals import K_c, K_x, K_z, K_r, K_SPACE, K_LEFT, K_RIGHT, K_UP, K_DOWN, K_LSHIFT, K_RSHIFT, K_LCTRL, K_RCTRL, K_ESCAPE, K_RETURN, K_F1, K_F2

from constants.activities import LOCK_DELAY, FIXED_GOAL, LEVEL_CAP
from activities.activity import Activity

from grid import Grid
from random_bag import RandomBag
from tetrominos.playable_tetromino import PlayableTetromino
from score import Score


class Game(Activity):
    """Class Game. Class representing the game engine."""

    def __init__(self, window, sound):
        """Constructor for the class Game."""
        Activity.__init__(self, window)

        self._window.init_game()
        self._sound = sound
        
        self._grid = Grid()
        self._random = RandomBag()
        self._score_keeper = Score()
        
        self._running = True
        self._topped_out = False
        self._swap_allowed = True
        self._show_fps_counter = False
        self._keys_down = {}
        
        self._held_tetromino = None
        self._next_queue = None
        self._current_tetromino = None
        self._level = 1
        self._goal = FIXED_GOAL
        self._lines_cleared = 0
        self._spawn_tetromino()        
        
                
        
    def __del__(self):
        """Destructor for the class Game."""
        self._window.end_game()

    
    def _spawn_tetromino(self):
        """Gets the next tetromino to be spawned from the random generator, and
        attenpts spawning it. If collisions allow it to spawn there, returns True, 
        otherwise returns False (block out)."""
        current_piece, self._next_queue = self._random.next_pieces()
        self._current_tetromino = PlayableTetromino(current_piece, self._grid)      
        if self._current_tetromino.blocked_out:
            self._topped_out = True
            self._running = False


    def _fall_tetromino(self):
        """If the game is running, calls a method so that tetromino moves down
        if possible, then checks the lock counter of the tetromino and, if
        larger than LOCK_DELAY, locks it into place, updates score, goal,
        level and lines cleared and spawns new tetromino."""
        if not self._running:
            return 
        
        if self._keys_down.get(K_SPACE, False):
            n_lines_dropped = self._current_tetromino.move_down(self._grid, self._level, "hard")
            self._score_keeper.add_to_score("hard_drop", {"n_lines": n_lines_dropped})
        elif self._keys_down.get(K_DOWN, False):
            n_lines_dropped = self._current_tetromino.move_down(self._grid, self._level, "soft")
            self._score_keeper.add_to_score("soft_drop", {"n_lines": n_lines_dropped})
        else:
            self._current_tetromino.move_down(self._grid, self._level, "normal")        
                
        if self._current_tetromino.lock_counter >= LOCK_DELAY:
            lines_cleared, lock_out = self._grid.lock_down(self._current_tetromino, self._level, self._score_keeper)
            self._lines_cleared += lines_cleared
            self._goal -= lines_cleared
            if self._goal <= 0:
                if self._level < LEVEL_CAP:
                    self._level += 1
                    self._goal = FIXED_GOAL
                else:
                    self._goal = 0
            
            if lock_out:
                self._topped_out = True
                self._running = False
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
    
    
    def event_update_screen(self, fps):
        self._fall_tetromino()
        self._window.update_game(current_grid = self._grid,
                                 current_tetromino = self._current_tetromino,
                                 queue = self._next_queue, held = self._held_tetromino,
                                 score = self._score_keeper.score, level = self._level,
                                 goal = self._goal, lines = self._lines_cleared,
                                 fps = fps, show_fps = self._show_fps_counter)
    
    
    def event_key_pressed(self, key):
        """Reacts to key being pressed, except if it is being held (with the
        only exception of right and left arrow) and, depending on the key,
        if the game is paused. Updates self._keys_down to say key is being pressed."""
        key_held = self._keys_down.get(key, False)
        self._keys_down[key] = True
        
        if self._running:
            if key == K_LEFT:
                self._current_tetromino.move_sideways("left", self._grid)
            elif key == K_RIGHT:
                self._current_tetromino.move_sideways("right", self._grid)
            elif not key_held:
                if key in (K_c, K_LSHIFT, K_RSHIFT):
                    self._swap_held_tetromino()
                elif key in (K_x, K_UP):
                    self._current_tetromino.rotate("clockwise", self._grid)
                elif key in (K_z, K_LCTRL, K_RCTRL):
                    self._current_tetromino.rotate("anticlockwise", self._grid)
        
        if key == K_r:
            self._sound.change_music()
        elif key == K_ESCAPE or key == K_F1:
            # Only allow changing running attribute to True if not topped out.
            self._running = not self._running and not self._topped_out
        elif key == K_F2:
            self._show_fps_counter = not self._show_fps_counter
        
        change_activity = self._topped_out and key in [K_RETURN, K_ESCAPE]
        return change_activity
                
        
    def event_key_released(self, key):
        """Reacts to the user releasing a key."""
        self._keys_down[key] = False