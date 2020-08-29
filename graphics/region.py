# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
import pygame


class Region(ABC):
    """Class Region. Class representing a region of the whole graphical window."""
    
    def __init__(self, size):
        """Constructor for the class Region."""
        self._size = dict(size)
        self._surface = pygame.Surface((size["width"], size["height"]))
        
    @abstractmethod
    def update(self, **kwargs):
        """Redraws the surface when called."""
        pass
    
    def _get_size(self):
        """Special function that allows to get the attribute _size from the exterior."""
        return dict(self._size)
    
    def _get_surface(self):
        """Special function that allows to get the attribute _surface from the exterior."""
        return self._surface
    
    """Definition of a properties for parameter _size. This parameter can
    only be get from the exteriour, not set nor deleted."""
    size = property(_get_size)
    
    """Definition of a properties for parameter _surface. This parameter can
    only be get from the exteriour, not set nor deleted."""
    surface = property(_get_surface)