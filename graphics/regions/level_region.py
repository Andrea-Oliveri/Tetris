# -*- coding: utf-8 -*-

import pygame

from constants.graphics import COLORS, LEVEL_FONT_SIZE
from graphics.regions.region import Region
from graphics import utils


class LevelRegion(Region):
    """Class LevelRegion. Class representing the region of the window where the 
    level and goal are displayed."""
    
    def update(self, **kwargs):
        """Implementation of the update method for the LevelRegion."""
        self._update_kwargs_test(kwargs, ["level", "goal"])
        
        level_text = utils.draw_text("Level: {}".format(kwargs["level"]), LEVEL_FONT_SIZE)
        goal_text = utils.draw_text("Goal:  {}".format(kwargs["goal"]), LEVEL_FONT_SIZE)
        self._surface = utils.merge_surfaces_vertically([level_text, goal_text], False)