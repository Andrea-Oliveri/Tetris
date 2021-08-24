# -*- coding: utf-8 -*-

from constants.graphics import FPS_FONT_SIZE
from graphics.regions.region import Region
from graphics import utils


class FPSRegion(Region):
    """Class FPSRegion. Class representing the region of the window where the fps counter is (optionally) displayed."""
    
    def __init__(self):
        """Overload of constructor for FPSRegion class."""
        Region.__init__(self)
        self._text = utils.draw_text("FPS: ", FPS_FONT_SIZE)
    
    def update(self, **kwargs):
        """Implementation of the update method for the QueueRegion."""
        self._update_kwargs_test(kwargs, ["fps"])
                
        fps_text = utils.draw_text("{:.1f}".format(kwargs["fps"]), FPS_FONT_SIZE)
        self._surface = utils.merge_surfaces_horizontally([self._text, fps_text])