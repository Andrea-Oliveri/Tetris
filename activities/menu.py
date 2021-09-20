from pygame.locals import K_UP, K_DOWN, K_RETURN

from constants.activities import MENU_TEXT_LINES
from activities.activity import Activity


class Menu(Activity):
    """Class Menu. Implements screen update and reaction to key presses
    when the program is showing the main menu."""
    
    def __init__(self, window, sound):
        """Constructor for the class MenuControls."""
        Activity.__init__(self, window, sound)
        
        self.menu_line_selected = 0
        self.need_to_redraw = True
    
    
    def event_update_screen(self, fps):
        """Override of method from Activity class, drawing the controls menu
        on the screen. This method is called several times per second, but
        the screen is only redrawn if an action causing it to change occurred."""
        if self.need_to_redraw:
            self._window.draw_menu(MENU_TEXT_LINES, self.menu_line_selected)
            self.need_to_redraw = False
        
    
    def event_key_pressed(self, key):
        """Override of method from Activity class, reacting to key presses.
        If a key to move from one menu line to the other is pressed, it plays
        a sound effect and returns a tuple of form (False, None). 
        If a key to change activity on screen is pressed, it plays a sound effect
        (except if user requested to exit the program) and returns a tuple of
        form (True, str) where str is the text line selected by the user."""
        self.need_to_redraw = True
        
        change_activity = (key == K_RETURN)
        text_pressed = None
        
        if key == K_UP:
            self.menu_line_selected = (self.menu_line_selected - 1) % len(MENU_TEXT_LINES)
            self._sound.play_sound_effect('menu_move')
        elif key == K_DOWN:
            self.menu_line_selected = (self.menu_line_selected + 1) % len(MENU_TEXT_LINES)
            self._sound.play_sound_effect('menu_move')
        elif key == K_RETURN:
            text_pressed = MENU_TEXT_LINES[self.menu_line_selected]
            
            if text_pressed != "Exit":
                self._sound.play_sound_effect('menu_select')
        
        return change_activity, text_pressed
                    