# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod


class Region(ABC):
    """Class Region. Class representing a region of the whole graphical window."""
    
    def __init__(self):
        """Constructor for the class Region."""
        self._surface = None
        
    @abstractmethod
    def update(self, **kwargs):
        """Redraws the surface when called."""
        pass
    
    def _get_surface(self):
        """Special function that allows to get the attribute _surface from the exterior."""
        return self._surface
    
    """Definition of a properties for parameter _surface. This parameter can
    only be get from the exteriour, not set nor deleted."""
    surface = property(_get_surface)