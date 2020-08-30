# -*- coding: utf-8 -*-

import pygame

from constants.graphics import COLORS, ELEMENTS_MARGIN_PIXELS, FONT
from constants.tetromino import MAPS


def draw_outside_tetromino(tetromino, square_size_pixels):
    """Function that returns a pygame.Surface containing the tetromino passed
    as parameter and using the square size passed as parameter."""
    tetromino_map = MAPS[tetromino]["DEG_0"]
    tetromino_size = {"width": len(tetromino_map[0]), "height": 2}

    if tetromino == 'I':
        tetromino_map = tetromino_map[1:]
        tetromino_size["height"] = 1
    
    surface = pygame.Surface((tetromino_size["width"]*square_size_pixels, 
                              tetromino_size["height"]*square_size_pixels))
    surface.fill(COLORS["background"])    
    
    for line in range(tetromino_size["height"]):
        for col in range(tetromino_size["width"]):
            if tetromino_map[line][col]:
                pygame.draw.rect(surface, COLORS[tetromino], 
                                 (col*square_size_pixels, line*square_size_pixels,
                                  square_size_pixels, square_size_pixels))
    return surface
    

def draw_text(message, font_size):
    """Function that returns a pygame.Surface containing the rendered text 
    with message and size passed as parameters."""
    return pygame.font.SysFont(FONT, font_size).render(message, True, COLORS["text"])
                
            
def merge_surfaces_horizontally(surfaces):
    """Returns a surfaces in which all surfaces passed as parameter are stacked horizontally
    and aligned on top."""
    merged_surface_size = {"width": sum([surface.get_width() for surface in surfaces])+(len(surfaces)-1)*ELEMENTS_MARGIN_PIXELS,
                           "height": max([surface.get_height() for surface in surfaces])}
    
    merged_surface = pygame.Surface((merged_surface_size["width"], merged_surface_size["height"]))
    merged_surface.fill(COLORS["background"])

    current_width = 0
    for surface in surfaces:
        merged_surface.blit(surface, (current_width, 0))
        current_width += surface.get_width() + ELEMENTS_MARGIN_PIXELS
    
    return merged_surface


def merge_surfaces_vertically(surfaces, center=True, total_height=None):
    """Returns a surfaces in which all surfaces passed as parameter are stacked vertically
    and either centered or aligned left depending on the center parameter. If a total_height
    is specified, final surface will have that height (no guarantee that everything will fit),
    otherwise final surface will have smallest height to fit everything."""
        
    merged_surface_size = {"width": max([surface.get_width() for surface in surfaces]),
                           "height": sum([surface.get_height() for surface in surfaces])+(len(surfaces)-1)*ELEMENTS_MARGIN_PIXELS}
    
    if total_height:
        merged_surface_size["height"] = total_height
    
    merged_surface = pygame.Surface((merged_surface_size["width"], merged_surface_size["height"]))
    merged_surface.fill(COLORS["background"])
    
    current_height = 0
    for surface in surfaces:
        if center:
            merged_surface.blit(surface, ((merged_surface_size["width"]-surface.get_width())/2, current_height))
        else:
            merged_surface.blit(surface, ((0, current_height)))
                                
        current_height += surface.get_height() + ELEMENTS_MARGIN_PIXELS
    
    return merged_surface


