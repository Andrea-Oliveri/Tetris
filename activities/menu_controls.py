# -*- coding: utf-8 -*-

from pygame.locals import K_RETURN, K_ESCAPE

from constants.activities import MENU_CONTROLS_TEXT_LINES
from activities.activity import Activity


class MenuControls(Activity): 
    
    def event_update_screen(self, fps):
        self._window.draw_menu_controls(MENU_CONTROLS_TEXT_LINES)
        
    
    def event_key_pressed(self, key):   
        change_activity = key in [K_RETURN, K_ESCAPE]
        
        return change_activity