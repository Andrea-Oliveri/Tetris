import pygame
from pygame.locals import QUIT, KEYDOWN, K_UP, K_DOWN, K_RETURN

from constants.menu import MENU_TEXT_LINES
from graphics.graphics import Window
from sound import SoundEngine
from game import Game
from menu_controls import MenuControls

class Menu():
    def __init__(self):
        # First initialize sound engine, such that constructor sets desired
        # values for the pygame.mixer.init function.
        self._sound = SoundEngine()
        
        # Initialize all pygame modules. pygame.mixer will not be re-initialized
        # and hence the desired values for pygame.mixer.init will be kept.
        pygame.init()
        
        # Open a pygame window and draw the menu.
        self._window = Window()
        self.menu_line_selected = 0
        self._update_menu_window()
        
    def __del__(self):
        pygame.quit()
    
    def _key_pressed(self, key):
        if key == K_UP:
            self.menu_line_selected = (self.menu_line_selected - 1) % len(MENU_TEXT_LINES)
            self._update_menu_window()
        elif key == K_DOWN:
            self.menu_line_selected = (self.menu_line_selected + 1) % len(MENU_TEXT_LINES)
            self._update_menu_window()
        elif key == K_RETURN:
            selected_text = MENU_TEXT_LINES[self.menu_line_selected]
            if selected_text == "Play":
                Game(self._window, self._sound).run()
            elif selected_text == "Controls":
                MenuControls(self._window).run()
            elif selected_text == "Exit":
                self._window.close()
            else:
                raise RuntimeError("Unknown selected menu option")
                
        return key == K_RETURN
        
        
    def _update_menu_window(self):
        self._window.draw_menu(MENU_TEXT_LINES, self.menu_line_selected)
    
    
    def _restart_menu_window(self):
        self.menu_line_selected = 0
        self._update_menu_window()
        
    
    def run(self):        
        while not self._window.closed:
            
            for event in pygame.event.get():    
                if event.type == QUIT:
                    self._window.close()
                
                if event.type == KEYDOWN:
                    window_changed = self._key_pressed(event.key)
                    
                    # If the whole window screen changed, we want to ignore the rest
                    # of the events in the queue as they come from previous screen
                    # and restart menu screen. If the window was closed, we do not
                    # redraw the main menu screen as it would only flicker a moment
                    # while the window closes.
                    if window_changed:
                        if not self._window.closed:
                            self._restart_menu_window()
                        pygame.event.clear()
                        break

                    