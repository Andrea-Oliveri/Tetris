# -*- coding: utf-8 -*-

import pygame

from constants.graphics import COLORS, QUEUE_SQUARE_SIZE_PIXELS, QUEUE_FONT_SIZE
from constants.random_bag import QUEUE_LENGTH
from graphics.region import Region
from graphics import utils


class QueueRegion(Region):
    """Class QueueRegion. Class representing the region of the window where the next pieces are displayed."""
        
    def update(self, **kwargs):
        """Implementation of the update method for the QueueRegion."""
        if len(kwargs.keys()) != 1 or "queue" not in kwargs or len(kwargs["queue"]) != QUEUE_LENGTH:
            raise TypeError("QueueRegion.update() takes exactly one kwarg: queue of length {}".format(QUEUE_LENGTH))
            
        queue = kwargs["queue"]
    
        text = utils.draw_text("Next Pieces", QUEUE_FONT_SIZE)
        pieces = [utils.draw_outside_tetromino(piece, QUEUE_SQUARE_SIZE_PIXELS) for piece in queue]
        self._surface = utils.merge_surfaces_vertically([text, *pieces])