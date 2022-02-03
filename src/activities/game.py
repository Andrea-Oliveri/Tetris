# -*- coding: utf-8 -*-

from pygame.locals import K_c, K_x, K_z, K_SPACE, K_LEFT, K_RIGHT, K_UP, K_DOWN, K_LSHIFT, K_RSHIFT, K_LCTRL, K_RCTRL, K_ESCAPE, K_RETURN, K_F1, K_F2
from math import ceil

from src.constants.activities import LOCK_DELAY, FIXED_GOAL, LEVEL_CAP, COUNTDOWN_FRAMES
from src.constants.gui import REFRESH_RATE
from src.activities.activity import Activity

from src.grid import Grid
from src.random_bag import RandomBag
from src.tetriminos.playable_tetrimino import PlayableTetrimino
from src.score import Score


class Game(Activity):
    """Class MenuControls. Implements screen update, reaction to key presses
    and releases and game engine when the program is showing the game."""
    
    def __init__(self, window, sound):
        """Constructor for the class Game."""
        Activity.__init__(self, window, sound)

        self._window.init_game()
        self._sound.use_game_music()
        
        self._grid = Grid()
        self._random = RandomBag()
        self._score_keeper = Score()
        
        self._state = "countdown"
        self._countdown_timer = COUNTDOWN_FRAMES
        self._swap_allowed = True
        self._show_fps_counter = False
        self._keys_down = {}
        
        self._held_tetrimino = None
        self._next_queue = None
        self._current_tetrimino = None
        self._level = 1
        self._goal = FIXED_GOAL
        self._lines_cleared = 0
        self._spawn_tetrimino()        
        
                
        
    def __del__(self):
        """Destructor for the class Game."""
        self._sound.use_menu_music()
        self._window.end_game()
        
    
    def _spawn_tetrimino(self):
        """Gets the next tetrimino to be spawned from the random generator, and
        attempts spawning it. If collisions do not allow it to spawn there (block out), 
        changes the game state to gameover and plays a sound effect."""
        current_piece, self._next_queue = self._random.next_pieces()
        self._current_tetrimino = PlayableTetrimino(current_piece, self._grid)      
        if self._current_tetrimino.blocked_out:
            self._state = "gameover"
            self._sound.play_sound_effect('game_gameover')


    def _fall_tetrimino(self):
        """Method called once per screen update when the game state is running.
        This method makes the current tetromino fall by the right amount if possible
        (accounting for level, soft drops, hard drops, ...), and calls method to 
        lock it into place if it stayed on the ground long enough. Also plays sound 
        effects on hard drops, soft drops and landing."""
        if self._keys_down.get(K_SPACE, False):
            n_lines_dropped, landed = self._current_tetrimino.move_down(self._grid, self._level, "hard")
            self._score_keeper.add_to_score("hard_drop", {"n_lines": n_lines_dropped})
            
            if n_lines_dropped:
                self._sound.play_sound_effect('game_hard_drop')
                
                # Remove the landing aound effect as the hard drop one covers it.
                landed = False
            
        elif self._keys_down.get(K_DOWN, False):
            n_lines_dropped, landed = self._current_tetrimino.move_down(self._grid, self._level, "soft")
            self._score_keeper.add_to_score("soft_drop", {"n_lines": n_lines_dropped})
            
            if n_lines_dropped:
                self._sound.play_sound_effect('game_soft_drop')
            
        else:
            _, landed = self._current_tetrimino.move_down(self._grid, self._level, "normal")        
                
        if landed:
            self._sound.play_sound_effect('game_landing')
            
        if self._current_tetrimino.lock_counter >= LOCK_DELAY:
            self._lock_down()


    def _lock_down(self):
        """Method called when the current tetromino stayed on the ground longer than
        its lock delay. Locks it into the current grid, and updates score, goal, level
        and lines cleared. Also spawns a new tetrimino and plays a sound effect. If
        lock out occurred, updates game state to gameover and plays corresponding sound
        effect."""
        lines_cleared, lock_out, all_empty, reward_tspin = self._grid.lock_down(self._current_tetrimino)
        
        sound_effect = 'game_lock'
        
        if lines_cleared:
            score_lines_cleared_actions = {(1, False): "single", (2, False): "double", 
                                           (3, False): "triple", (4, False): "tetris",
                                           (1, True): "tspin_single", (2, True): "tspin_double", 
                                           (3, True): "tspin_triple", (4, True): "tspin_tetris"}
                        
            action = score_lines_cleared_actions[lines_cleared, reward_tspin]            
            self._score_keeper.add_to_score(action, {"level": self._level})
            
            sound_effects_cleared_actions = {1: "game_single", 2: "game_double", 3: "game_triple", 4: "game_tetris"}
            sound_effect = sound_effects_cleared_actions[lines_cleared]
                    
            if all_empty:
                self._score_keeper.add_perfect_bonus_to_score(lines_cleared, self._level)
                sound_effect = 'game_perfect'
                
        elif reward_tspin:
            self._score_keeper.add_to_score("tspin_no_lines", {"level": self._level})
    
        
        self._lines_cleared += lines_cleared
        self._goal -= lines_cleared
        if self._goal <= 0:
            if self._level < LEVEL_CAP:
                self._level += 1
                self._goal = FIXED_GOAL
            else:
                self._goal = 0
        
        if lock_out:
            self._state = "gameover"
            sound_effect = 'game_gameover'
        else:
            self._spawn_tetrimino()
            self._swap_allowed = True
            
        self._sound.play_sound_effect(sound_effect)


    def _tick_countdown(self):
        """Method called once per frame when counting down from paused state to
        running state. Decreases the remaining countdown timer, and if the 
        timer elapsed, it changes the game state to running."""
        self._countdown_timer -= 1
        
        if self._countdown_timer <= 0:
            self._state = "running"


    def _swap_held_tetrimino(self):
        """Performs the swap beween the current tetrimino and the held tetrimino,
        if it is currently allowed."""             
        if self._swap_allowed:
            old_held = self._held_tetrimino
            self._held_tetrimino = self._current_tetrimino.letter

            if old_held == None:
                self._spawn_tetrimino()
            else:
                self._current_tetrimino = PlayableTetrimino(old_held, self._grid)
            
            self._swap_allowed = False
            
            self._sound.play_sound_effect('game_hold')
    
    
    def event_update_screen(self, fps):
        """Override of method from Activity class, drawing the controls menu
        on the screen. This method updates the game state, and then the graphics
        on the screen."""
        game_state_text = ""
        
        if self._state == "running":
            self._fall_tetrimino()
        elif self._state == "countdown":
            game_state_text = "Resuming in {}".format(ceil(self._countdown_timer / REFRESH_RATE))
            self._tick_countdown()
        elif self._state == "paused":
            game_state_text = "Paused"
            
        self._window.update_game(current_grid = self._grid,
                                 current_tetrimino = self._current_tetrimino,
                                 queue = self._next_queue, held = self._held_tetrimino,
                                 score = self._score_keeper.score, level = self._level,
                                 goal = self._goal, lines = self._lines_cleared,
                                 fps = fps, show_fps = self._show_fps_counter,
                                 game_state_text = game_state_text)
    
    
    def event_key_pressed(self, key):
        """Override of method from Activity class, reacting to key being pressed.
        Keeps track of which keys are being held (as key down events are repeated
        with a set rate when in game mode) and ignores key down events of keys that
        are being held except for right and left arrows. All other keys will only
        trigger one change in the game until they are released."""
        key_held = self._keys_down.get(key, False)
        self._keys_down[key] = True
        
        if self._state == "running":
            rotation_success = False
            move_success = False
            hit_wall = False
            
            if key == K_LEFT:
                move_success, hit_wall = self._current_tetrimino.move_sideways("left", self._grid)
            elif key == K_RIGHT:
                move_success, hit_wall = self._current_tetrimino.move_sideways("right", self._grid)
            elif not key_held:
                if key in (K_c, K_LSHIFT, K_RSHIFT):
                    self._swap_held_tetrimino()
                elif key in (K_x, K_UP):
                    rotation_success = self._current_tetrimino.rotate("clockwise", self._grid)
                elif key in (K_z, K_LCTRL, K_RCTRL):
                    rotation_success = self._current_tetrimino.rotate("anticlockwise", self._grid)
                        
            if rotation_success:
                self._sound.play_sound_effect('game_rotate')
                
            if move_success:
                self._sound.play_sound_effect('game_move')
                
            if hit_wall:
                self._sound.play_sound_effect('game_alert')
        
        
        if key == K_ESCAPE or key == K_F1:            
            # If game is running or counting down to resume, we allow pausing it.
            # If the game is paused, we start counting down to resume it.
            # If game is finished, we don't change the state.
            if self._state == "running":
                self._state = "paused"
                self._sound.play_sound_effect('game_pause')
            elif self._state == "paused":
                self._state = "countdown"
                self._sound.play_sound_effect('game_pause')
                self._countdown_timer = COUNTDOWN_FRAMES
            
        elif key == K_F2:
            self._show_fps_counter = not self._show_fps_counter
        
        change_activity = self._state == "gameover" and key in [K_RETURN, K_ESCAPE]
        
        if change_activity:
            self._sound.play_sound_effect('menu_back')
        
        return change_activity
                
        
    def event_key_released(self, key):
        """Override of method from Activity class, reacting to key release."""
        self._keys_down[key] = False


