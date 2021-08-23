# -*- coding: utf-8 -*-

from pygame.locals import K_RETURN, K_ESCAPE

from constants.activities import MENU_CONTROLS_TEXT_LINES
from activities.activity import Activity


class MenuControls(Activity): 
    
    def __init__(self, window, sound):
        Activity.__init__(self, window, sound)
        
        self.need_to_redraw = True
    
    def event_update_screen(self, fps):
        if self.need_to_redraw:
            self._window.draw_menu_controls(MENU_CONTROLS_TEXT_LINES)
            self.need_to_redraw = False
        
    
    def event_key_pressed(self, key):
        change_activity = key in [K_RETURN, K_ESCAPE]
        
        if change_activity:
            self._sound.play_sound_effect('menu_back')
        
        return change_activity