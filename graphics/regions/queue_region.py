# -*- coding: utf-8 -*-

import pygame

from constants.graphics import COLORS, QUEUE_SQUARE_SIZE_PIXELS, QUEUE_FONT_SIZE
from constants.random_bag import QUEUE_LENGTH
from graphics.regions.region import Region
from graphics import utils


class QueueRegion(Region):
    """Class QueueRegion. Class representing the region of the window where the next pieces are displayed."""
        
    def _update_kwargs_test(self, kwargs, keys_list):
        """Performs the test by Region._update_kwargs_test and additionally checks
        the size of the list in parameter is correct."""
        Region._update_kwargs_test(self, kwargs, keys_list)
        if len(kwargs["queue"]) != QUEUE_LENGTH:
            raise TypeError("{}.update() parameter queue has size {}, {} expected".format(self.__class__.__name__, len(kwargs["queue"]), QUEUE_LENGTH))
          
    
    def update(self, **kwargs):
        """Implementation of the update method for the QueueRegion."""
        self._update_kwargs_test(kwargs, ["queue"])
        
        queue = kwargs["queue"]
    
        text = utils.draw_text("Next Pieces", QUEUE_FONT_SIZE)
        pieces = [utils.draw_outside_tetromino(piece, QUEUE_SQUARE_SIZE_PIXELS) for piece in queue]
        self._surface = utils.merge_surfaces_vertically([text, *pieces])