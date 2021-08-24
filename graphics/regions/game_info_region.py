# -*- coding: utf-8 -*-

from constants.graphics import GAME_INFO_FONT_SIZE
from graphics.regions.region import Region
from graphics import utils


class GameInfoRegion(Region):
    """Class FPSRegion. Class representing the region of the window where the fps counter is (optionally) displayed."""
    
    def update(self, **kwargs):
        """Implementation of the update method for the QueueRegion."""
        self._update_kwargs_test(kwargs, ["game_state_text"])
        
        self._surface = utils.draw_text(kwargs["game_state_text"], GAME_INFO_FONT_SIZE)