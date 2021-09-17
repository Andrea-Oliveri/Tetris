# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod


class Region(ABC):
    """Class Region. Class representing a region of the game screen."""
    
    def __init__(self):
        """Constructor for the class Region."""
        self._surface = None
        
    @abstractmethod
    def update(self, **kwargs):
        """Redraws the surface when called."""
        pass
    
    def _update_kwargs_test(self, kwargs, keys_list):
        """Tests if kwargs contains all keys in keys_list and no more."""
        if len(kwargs.keys()) != len(keys_list) or not all([key in kwargs for key in keys_list]):
            raise TypeError("{}.update() takes exactly {} kwarg: {}".format(self.__class__.__name__, len(keys_list), ", ".join(keys_list)))
    
    def _get_surface(self):
        """Getter for the attribute _surface."""
        return self._surface
    
    """Definition of a properties for parameter _surface. This parameter can
    only be get from the exteriour, not set nor deleted."""
    surface = property(_get_surface)