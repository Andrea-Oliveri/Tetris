# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod

from constants.tetromino import MAPS


class Tetromino(ABC):
    """Class Tetromino. Abtract class defining the general interface of all tetrominos, both
    playable and solid."""
    
    @abstractmethod
    def __init__(self, letter, rotation):
        """Constructor for the class Tetromino."""
        self._letter = str(letter)
        self._MAPS = MAPS[letter]
        self._MAPS_SIZE = {"height": len(self._MAPS["DEG_0"]), "width": len(self._MAPS["DEG_0"][0])}
        self._rotation = str(rotation)
        self._position = None

    def _get_MAPS_SIZE(self):
        """Special function that allows to get the attribute _MAPS_SIZE from the exterior."""
        return dict(self._MAPS_SIZE)

    def _get_position(self):
        """Special function that allows to get the attribute _position from the exterior."""
        return list(self._position)
    
    def _get_letter(self):
        """Special function that allows to get the attribute _letter from the exterior."""
        return str(self._letter)

    def __getitem__(self, index):
        """Special function that allows to get items of attribute _MAPS from the exterior."""
        return tuple(self._MAPS[self._rotation][index])

    """Definition of a properties for parameter _MAPS_SIZE. This parameter can
    only be get from the exteriour, not set nor deleted."""
    MAPS_SIZE = property(_get_MAPS_SIZE)
    
    """Definition of a properties for parameter _position. This parameter can
    only be get from the exteriour, not set nor deleted."""
    position = property(_get_position)

    """Definition of a properties for parameter _letter. This parameter can
    only be get from the exteriour, not set nor deleted."""
    letter = property(_get_letter)