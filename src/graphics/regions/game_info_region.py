# -*- coding: utf-8 -*-

from src.constants.graphics import GAME_INFO_FONT_SIZE
from src.graphics.regions.region import Region
from src.graphics import utils


class GameInfoRegion(Region):
    """Class GameInfoRegion. Class representing the region of the game screen where the
    game state is displayed."""
    
    def update(self, **kwargs):
        """Implementation of the update method for the GameInfoRegion."""
        self._update_kwargs_test(kwargs, ["game_state_text"])
        
        self._surface = utils.draw_text(kwargs["game_state_text"], GAME_INFO_FONT_SIZE)