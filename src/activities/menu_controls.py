# -*- coding: utf-8 -*-

from pygame.locals import K_RETURN, K_ESCAPE

from src.constants.activities import MENU_CONTROLS_TEXT_LINES
from src.activities.activity import Activity


class MenuControls(Activity):
    """Class MenuControls. Implements screen update and reaction to key presses
    when the program is showing the controls menu."""
    
    def __init__(self, window, sound):
        """Constructor for the class MenuControls."""
        Activity.__init__(self, window, sound)
        
        self.need_to_redraw = True
    
    
    def event_update_screen(self, fps):
        """Override of method from Activity class, drawing the controls menu
        on the screen. This method is called several times per second, but
        the screen is only redrawn if an action causing it to change occurred."""
        if self.need_to_redraw:
            self._window.draw_menu_controls(MENU_CONTROLS_TEXT_LINES)
            self.need_to_redraw = False
        
    
    def event_key_pressed(self, key):
        """Override of method from Activity class, reacting to key presses.
        Returns True and plays a sound effect if the pressed key is one
        of the allowed ones to exit controls menu, otherwise just returns
        False."""
        change_activity = key in [K_RETURN, K_ESCAPE]
        
        if change_activity:
            self._sound.play_sound_effect('menu_back')
        
        return change_activity