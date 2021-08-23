# -*- coding: utf-8 -*-

import pygame

from constants.graphics import WINDOW_SIZE, COLORS, IMAGE_DIRECTORY, LOGO_IMAGE_NAME, CURSOR_IMAGE_NAME, MENU_LOGO_SURFACE_HEIGHT, MENU_TEXT_FONT_SIZE, MENU_TEXT_SURFACE_HEIGHT, MENU_CONTROLS_TEXT_FONT_SIZE
from graphics import utils
from graphics.regions.region import Region
from graphics.regions.hold_region import HoldRegion
from graphics.regions.grid_region import GridRegion
from graphics.regions.queue_region import QueueRegion
from graphics.regions.fps_region import FPSRegion
from graphics.regions.level_region import LevelRegion
from graphics.regions.score_region import ScoreRegion


class Window(Region):
    """Class Window. Class dealing with all graphical output."""
    
    def __init__(self):
        """Constructor for the class Window."""
        Region.__init__(self)
        
        self._screen = pygame.display.set_mode(WINDOW_SIZE)
        pygame.display.set_caption("Tetris")
        
        # Variable used to describe if the window was closed or not.
        self._closed = False
        
        
    def get_closed(self):
        return self._closed
    
    
    closed = property(get_closed)
    
    def close(self):
        self._closed = True
        
        
    def draw_menu(self, text_lines, idx_line_selected):
        # Load logo and cursor assets.
        logo = pygame.image.load(IMAGE_DIRECTORY + LOGO_IMAGE_NAME).convert_alpha()
        cursor = pygame.image.load(IMAGE_DIRECTORY + CURSOR_IMAGE_NAME).convert_alpha()

        # Convert color of menu cursor.
        color_selected = COLORS['menu_text_selected']
        array = pygame.surfarray.pixels3d(cursor)
        for color_component in range(len(color_selected)):
            array[:, :, color_component] = color_selected[color_component]
        del array

        # Generating text in menu.
        text_surfaces = []
        for idx, text in enumerate(text_lines):
            text_surface = utils.draw_text(text, MENU_TEXT_FONT_SIZE, 
                                           color = color_selected if idx == idx_line_selected else COLORS['text'])
            text_surfaces.append(text_surface)
        
        # Add cursor to selected line.
        text_surfaces[idx_line_selected] = utils.merge_surfaces_horizontally([cursor, text_surfaces[idx_line_selected]], True)
        
        ## Add padding to logo, cursor and text surfaces.
        logo          = utils.merge_surfaces_vertically([logo], False, MENU_LOGO_SURFACE_HEIGHT)
        text_surfaces = [utils.merge_surfaces_vertically([surface], False, MENU_TEXT_SURFACE_HEIGHT) for surface in text_surfaces]

        self._surface = utils.merge_surfaces_vertically([logo, *text_surfaces])
        
        self._screen.fill(COLORS["background"])
        self._screen.blit(self._surface, ((self._screen.get_width()-self._surface.get_width())/2,
                                          (self._screen.get_height()-self._surface.get_height())/2))        
        pygame.display.update()
        
    
    def draw_menu_controls(self, controls_lines):
        
        keys_surfaces = []
        text_surfaces = []
        for text, key_files in controls_lines.items():
            keys_surface = [pygame.image.load(IMAGE_DIRECTORY + key_file).convert_alpha() for key_file in key_files]
            
            keys_surfaces.append(utils.merge_surfaces_horizontally(keys_surface))
            text_surfaces.append(utils.draw_text(text, MENU_CONTROLS_TEXT_FONT_SIZE))
            
        self._surface = utils.merge_surfaces_in_table(keys_surfaces, text_surfaces)
        
        self._screen.fill(COLORS["background"])
        self._screen.blit(self._surface, ((self._screen.get_width()-self._surface.get_width())/2,
                                          (self._screen.get_height()-self._surface.get_height())/2))        
        pygame.display.update()
    
   
        
        
    def init_game(self):
        self._hold_region = HoldRegion()
        self._grid_region = GridRegion()
        self._queue_region = QueueRegion()
        self._fps_region   = FPSRegion()
        self._level_region = LevelRegion()
        self._score_region = ScoreRegion()
        
        
        
    def end_game(self):
        del self._hold_region
        del self._grid_region
        del self._queue_region
        del self._fps_region
        del self._level_region
        del self._score_region


    def update(self, **kwargs):
        """Implementation of the update method for the Window."""
        self._update_kwargs_test(kwargs, ["current_grid", "current_tetromino", "queue", "held", "score", "level", "goal", "lines", "fps", "show_fps"])

        self._hold_region.update(held=kwargs["held"])
        self._grid_region.update(current_grid=kwargs["current_grid"], current_tetromino=kwargs["current_tetromino"])
        self._queue_region.update(queue=kwargs["queue"])
        self._level_region.update(level=kwargs["level"], goal=kwargs["goal"], lines=kwargs["lines"])
        self._score_region.update(score=kwargs["score"])
        
        surfaces_right_column = [self._queue_region.surface, self._level_region.surface]
        if kwargs["show_fps"]:
            self._fps_region.update(fps=kwargs["fps"])
            surfaces_right_column.append(self._fps_region.surface)

        right_column = utils.merge_surfaces_vertically(surfaces_right_column, False)
        central_column = utils.merge_surfaces_vertically([self._grid_region.surface, self._score_region.surface])

        self._surface = utils.merge_surfaces_horizontally([self._hold_region.surface, central_column, right_column])
        
        self._screen.fill(COLORS["background"])
        self._screen.blit(self._surface, ((self._screen.get_width()-self._surface.get_width())/2,
                                          (self._screen.get_height()-self._surface.get_height())/2))        
        pygame.display.update()
    
   