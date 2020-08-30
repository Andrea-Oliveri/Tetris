# -*- coding: utf-8 -*-

import random

from constants.random_bag import *


class RandomBag:
    """Class RandomBag. Class representing the tetrominos random generator."""

    def __init__(self):
        """Constructor for the class RandomBag."""
        self._list = []
        
    def next_pieces(self):
        """Returns the current and next PREVIEW_LENGTH pieces and, if needed, draws another bag."""
        if len(self._list) <= QUEUE_LENGTH:
            self._list += random.sample(TETROMINOS_LIST, len(TETROMINOS_LIST))
        
        current = self._list[0]
        self._list = self._list[1:]
        
        return current, self._list[:QUEUE_LENGTH]