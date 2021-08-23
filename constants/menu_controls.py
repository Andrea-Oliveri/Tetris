# -*- coding: utf-8 -*-

# Constant defining the text lines and path of icons present in the controls menu. 
# Keys are the description of what the key performs and values are a tuple with
# filenames of the corresponding key icons.
MENU_CONTROLS_TEXT_LINES = {'Move tetromino to the left': ('key_left.png', ),
                            'Move tetromino to the right': ('key_right.png', ),
                            'Rotate tetromino clockwise': ('key_x.png', 'key_up.png'),
                            'Rotate tetromino anti-clockwise': ('key_z.png', 'key_ctrl_left.png', 'key_ctrl_right.png'),
                            'Soft drop': ('key_down.png', ),
                            'Hard drop': ('key_space.png', ),
                            'Swap current tetromino with held one': ('key_c.png', 'key_shift_left.png', 'key_shift_right.png'),
                            'Change music track': ('key_r.png', ),
                            'Pause / Resume': ('key_esc.png', 'key_f1.png', ),
                            'Show / Hide FPS counter': ('key_f2.png', )}