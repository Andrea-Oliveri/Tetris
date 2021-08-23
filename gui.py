import pygame
from pygame.locals import QUIT, KEYDOWN, KEYUP

from constants.gui import FRAME_EVENT, REFRESH_PERIOD, DAS_DELAY, DAS_RATE
from sound import SoundEngine
from graphics.graphics import Window
from activities.menu import Menu
from activities.menu_controls import MenuControls
from activities.game import Game



class Gui():
    def __init__(self):
        # First initialize sound engine, such that constructor sets desired
        # values for the pygame.mixer.init function.
        self._sound = SoundEngine()
        
        # Initialize all pygame modules. pygame.mixer will not be re-initialized
        # and hence the desired values for pygame.mixer.init will be kept.
        pygame.init()
        
        # Open a pygame window.
        self._window = Window()

        # Store current activity.
        self._current_activity = Menu(self._window)
        
        # Set a timer firing a frame event at desired rate.
        pygame.time.set_timer(FRAME_EVENT, REFRESH_PERIOD)
    
        
    def __del__(self):
        pygame.quit()
        
    
    def run(self):
        
        # Variable used to count the fps at which screen is really being updated.
        fps_counter_clock = pygame.time.Clock()
        
        # Variable needed to prevent redrawing the screen multiple times
        # in one while loop iteration in case FRAME_EVENTS accumulated due
        # to slow hardware.
        frame_updated = False
        
        while not self._window.closed:
            frame_updated = False
            
            for event in pygame.event.get():    
                if event.type == QUIT:
                    self._window.close()
                
                if event.type == KEYDOWN:
                    output = self._current_activity.event_key_pressed(event.key)
                    
                    if isinstance(self._current_activity, Menu):
                        change_activity, text_pressed = output
                        
                        if change_activity:
                            if text_pressed == 'Play':
                                # Enable Delayed Auto Shift.
                                pygame.key.set_repeat(DAS_DELAY, DAS_RATE)
                                
                                self._current_activity = Game(self._window, self._sound)
                            elif text_pressed == 'Controls':
                                self._current_activity = MenuControls(self._window)
                            elif text_pressed == 'Exit':
                                self._window.close()
                            else:
                                raise RuntimeError("Unknown selected menu option")
                                
                    elif isinstance(self._current_activity, MenuControls) or isinstance(self._current_activity, Game):
                        change_activity = output
                        
                        if change_activity:
                            self._current_activity = Menu(self._window)
                            
                            # Disable Delayed Auto Shift.
                            pygame.key.set_repeat()

                
                elif event.type == KEYUP:
                    self._current_activity.event_key_released(event.key)
                
                elif event.type == FRAME_EVENT:
                    if not frame_updated:
                        fps_counter_clock.tick()
                        self._current_activity.event_update_screen(fps_counter_clock.get_fps())
                        frame_updated = True