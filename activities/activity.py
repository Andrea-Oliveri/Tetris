from abc import ABC, abstractmethod


class Activity(ABC):
    """Class Activity. Class representing a program state that can be shown on the window."""
         
    
    def __init__(self, window):
        """Constructor for the class Activity."""
        self._window = window
    
    @abstractmethod
    def event_update_screen(self, fps):
        """Redraws the activity in the window."""
        return
    
    @abstractmethod
    def event_key_pressed(self, key):
        """Reacts to key being pressed."""
        return

    def event_key_released(self, key):
        """Reacts to key being released."""
        return