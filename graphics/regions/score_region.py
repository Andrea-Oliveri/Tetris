# -*- coding: utf-8 -*-

from constants.graphics import SCORE_FONT_SIZE
from graphics.regions.region import Region
from graphics import utils


class ScoreRegion(Region):
    """Class ScoreRegion. Class representing the region of the game screen where the
    score is displayed."""
    
    def update(self, **kwargs):
        """Implementation of the update method for the ScoreRegion."""
        self._update_kwargs_test(kwargs, ["score"])
        
        self._surface = utils.draw_text("{}".format(kwargs["score"]), SCORE_FONT_SIZE)