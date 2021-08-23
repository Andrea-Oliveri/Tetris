# -*- coding: utf-8 -*-

import pygame
from pygame.locals import QUIT, KEYDOWN, K_RETURN, K_ESCAPE

from constants.menu_controls import MENU_CONTROLS_TEXT_LINES


class MenuControls:
    """Class MenuControls. Class representing the menu page showing the controls."""

    def __init__(self, window):
        """Constructor for the class MenuControls."""        
        self._window = window
        self._window.draw_menu_controls(MENU_CONTROLS_TEXT_LINES)
        

    def run(self):
        """Waits for any key to be pressed then returns."""
        
        # Remove any events trailing from previous screen.
        pygame.event.clear()
        
        # Variable used to know if any key was pressed.
        quit_key_pressed = False
        
        while not quit_key_pressed and not self._window.closed:
            
            for event in pygame.event.get():    
                if event.type == QUIT:
                    self._window.close()
                
                if event.type == KEYDOWN:
                    if event.key in [K_RETURN, K_ESCAPE]:
                        quit_key_pressed = True