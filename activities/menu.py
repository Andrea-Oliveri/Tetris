from pygame.locals import K_UP, K_DOWN, K_RETURN

from constants.activities import MENU_TEXT_LINES
from activities.activity import Activity


class Menu(Activity):
    
    def __init__(self, window):
        Activity.__init__(self, window)
        
        self.menu_line_selected = 0
        self.need_to_redraw = True
    
    
    def event_update_screen(self, fps):
        if self.need_to_redraw:
            self._window.draw_menu(MENU_TEXT_LINES, self.menu_line_selected)
            self.need_to_redraw = False
        
    
    def event_key_pressed(self, key):
        self.need_to_redraw = True
        
        change_activity = (key == K_RETURN)
        text_pressed = None
        
        if key == K_UP:
            self.menu_line_selected = (self.menu_line_selected - 1) % len(MENU_TEXT_LINES)
        elif key == K_DOWN:
            self.menu_line_selected = (self.menu_line_selected + 1) % len(MENU_TEXT_LINES)
        elif key == K_RETURN:
            text_pressed = MENU_TEXT_LINES[self.menu_line_selected]
        
        return change_activity, text_pressed
                    