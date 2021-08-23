# -*- coding: utf-8 -*-

import pygame

from constants.graphics import COLORS, ELEMENTS_MARGIN_PIXELS, FONT
from constants.tetrimino import MAPS


def draw_outside_tetrimino(tetrimino, square_size_pixels):
    """Function that returns a pygame.Surface containing the tetrimino passed
    as parameter and using the square size passed as parameter.
    Only draws non-ghost tetriminos, vertically centered and at DEG_0 rotation."""
    tetrimino_map = MAPS[tetrimino]["DEG_0"]
    tetrimino_size = {"width": len(tetrimino_map[0]), "height": 2}

    if tetrimino == 'I':
        tetrimino_map = tetrimino_map[1:]
        tetrimino_size["height"] = 1
    
    surface = pygame.Surface((tetrimino_size["width"]*square_size_pixels, 
                              tetrimino_size["height"]*square_size_pixels))
    surface.fill(COLORS["background"])    
    
    for line in range(tetrimino_size["height"]):
        for col in range(tetrimino_size["width"]):
            if tetrimino_map[line][col]:
                pygame.draw.rect(surface, COLORS[tetrimino], 
                                 (col*square_size_pixels, line*square_size_pixels,
                                  square_size_pixels, square_size_pixels))
    return surface
    

def draw_text(message, font_size, color = COLORS["text"]):
    """Function that returns a pygame.Surface containing the rendered text 
    with message and size passed as parameters."""
    return pygame.font.SysFont(FONT, font_size).render(message, True, color, COLORS["background"])
                

def merge_surfaces_horizontally(surfaces, center=False):
    """Returns a surfaces in which all surfaces passed as parameter are stacked horizontally
    and aligned on top."""

    merged_surface_size = {"width": sum([surface.get_width() for surface in surfaces])+(len(surfaces)-1)*ELEMENTS_MARGIN_PIXELS,
                           "height": max([surface.get_height() for surface in surfaces])}

    merged_surface = pygame.Surface((merged_surface_size["width"], merged_surface_size["height"]))
    merged_surface.fill(COLORS["background"])
    
    current_width = 0
    for surface in surfaces:
        if center:
            merged_surface.blit(surface, (current_width, (merged_surface_size["height"]-surface.get_height())/2))
        else:
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


def merge_surfaces_in_table(left_col_surfaces, right_col_surfaces):
    """Returns a surfaces in which all surfaces passed as parameter in left_col_surfaces
    are stacked vertically and right-aligned, whereas all surfaces passed in right_col_surfaces
    are stacked vertically and left-aligned. Each element in left_col_surfaces is also 
    vertically aligned to be centered with the corresponding one in right_column_surfaces."""
    
    left_col_width = max([line.get_width() for line in left_col_surfaces])
    right_col_width = max([line.get_width() for line in right_col_surfaces])
        
    total_line_width = left_col_width + right_col_width + ELEMENTS_MARGIN_PIXELS
    
    line_surfaces = []
    for left_col_surface, right_col_surface in zip(left_col_surfaces, right_col_surfaces):
        line_surface = merge_surfaces_horizontally([left_col_surface, right_col_surface], True)
        
        line_surface_padded = pygame.Surface((total_line_width, line_surface.get_height()))
        line_surface_padded.fill(COLORS["background"])

        line_surface_padded.blit(line_surface, (left_col_width - left_col_surface.get_width(), 0))
        
        line_surfaces.append(line_surface_padded)
        
    table_surface = merge_surfaces_vertically(line_surfaces)
    
    return table_surface