# -*- coding: utf-8 -*-

import pygame

from constants.graphics import COLORS, QUEUE_SQUARE_SIZE_PIXELS, FONT, QUEUE_FONT_SIZE
from constants.tetromino import MAPS
from constants.random_bag import QUEUE_LENGTH
from graphics.region import Region


class QueueRegion(Region):
    """Class QueueRegion. Class representing the region of the window where the next pieces are displayed."""
        
    def update(self, **kwargs):
        """Implementation of the update method for the QueueRegion."""
        if len(kwargs.keys()) != 1 or "queue" not in kwargs or len(kwargs["queue"]) != QUEUE_LENGTH:
            raise TypeError("QueueRegion.update() takes exactly one kwarg: queue of length {}".format(QUEUE_LENGTH))
            
        queue = kwargs["queue"]
    
        self._surface.fill(COLORS["background"])
        font = pygame.font.SysFont(FONT, QUEUE_FONT_SIZE)
        text = font.render("Next Pieces", True, COLORS["text"])
        self._surface.blit(text, ((self._surface.get_width()-text.get_width())/2, 4))




        # for each case of the queue list, create a surface as did for held, center it etc. 

        # tetromino_map = MAPS[held]["DEG_0"]
        # held_tetromino_size = {"width": len(tetromino_map[0]), "height": 2}
        # tetromino_surface = pygame.Surface((held_tetromino_size["width"]*HOLD_SQUARE_SIZE_PIXELS, held_tetromino_size["height"]*HOLD_SQUARE_SIZE_PIXELS))
        # tetromino_surface.fill(COLORS["background"])
            
        # for line in range(held_tetromino_size["height"]):
        #     for col in range(held_tetromino_size["width"]):
        #         if tetromino_map[line][col]:
        #             pygame.draw.rect(tetromino_surface, COLORS[held],
        #                              (col*HOLD_SQUARE_SIZE_PIXELS,
        #                               line*HOLD_SQUARE_SIZE_PIXELS,
        #                               HOLD_SQUARE_SIZE_PIXELS, HOLD_SQUARE_SIZE_PIXELS))
        # self._surface.blit(tetromino_surface, ((self._surface.get_width()-tetromino_surface.get_width())/2, 40))