from src.constants.gui import REFRESH_RATE

# Constant defining the text lines present in the menu. Position in list corresponds to 
# position in menu and content are the sentences.
MENU_TEXT_LINES = ['Play', 'Controls', 'Exit']

# Constant defining the text lines and path of icons present in the controls menu. 
# Keys are the description of what the key performs and values are a tuple with
# filenames of the corresponding key icons.
MENU_CONTROLS_TEXT_LINES = {'Move Tetrimino to the left': ('key_left.png', ),
                            'Move Tetrimino to the right': ('key_right.png', ),
                            'Rotate Tetrimino clockwise': ('key_x.png', 'key_up.png'),
                            'Rotate Tetrimino anti-clockwise': ('key_z.png', 'key_ctrl_left.png', 'key_ctrl_right.png'),
                            'Soft drop': ('key_down.png', ),
                            'Hard drop': ('key_space.png', ),
                            'Swap current Tetrimino with held one': ('key_c.png', 'key_shift_left.png', 'key_shift_right.png'),
                            'Change music track': ('key_r.png', ),
                            'Mute / Unmute': ('key_m.png', ),
                            'Pause / Resume': ('key_esc.png', 'key_f1.png', ),
                            'Show / Hide FPS counter': ('key_f2.png', )}


# ---------------- Game constants: ----------------


# Constant defining the delay to wait before locking a tetrimino in place in frames.
LOCK_DELAY = 0.5 * REFRESH_RATE

# Constant defining the fixed goal to increase by one level.
FIXED_GOAL = 10

# Constant defining the maximum level that can be reached.
LEVEL_CAP = 15

# constant defining how many frames the countdown is shown when starting or resuming a game.
COUNTDOWN_FRAMES = 3 * REFRESH_RATE