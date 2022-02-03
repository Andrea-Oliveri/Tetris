# -*- coding: utf-8 -*-

from src.constants.graphics import QUEUE_SQUARE_SIZE_PIXELS, QUEUE_FONT_SIZE, QUEUE_SURFACE_HEIGHT
from src.constants.random_bag import QUEUE_LENGTH
from src.graphics.regions.region import Region
from src.graphics import utils


class QueueRegion(Region):
    """Class QueueRegion. Class representing the region of the game screen where
    the next pieces are displayed."""
        
    def __init__(self):
        """Overload of constructor for QueueRegion class."""
        Region.__init__(self)
        self._text = utils.draw_text("Next Pieces", QUEUE_FONT_SIZE)
    
    
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
    
        pieces = [utils.draw_outside_tetrimino(piece, QUEUE_SQUARE_SIZE_PIXELS) for piece in queue]
        self._surface = utils.merge_surfaces_vertically([self._text, *pieces], total_height = QUEUE_SURFACE_HEIGHT)