# -*- coding: utf-8 -*-

import pygame
import os

from constants.graphics import WINDOW_SIZE, COLORS, IMAGE_DIRECTORY, LOGO_IMAGE_NAME, ICON_IMAGE_NAME, CURSOR_IMAGE_NAME, MENU_LOGO_SURFACE_HEIGHT, MENU_TEXT_FONT_SIZE, MENU_TEXT_SURFACE_HEIGHT, MENU_CONTROLS_TEXT_FONT_SIZE
from graphics import utils
from graphics.regions.hold_region import HoldRegion
from graphics.regions.grid_region import GridRegion
from graphics.regions.queue_region import QueueRegion
from graphics.regions.fps_region import FPSRegion
from graphics.regions.level_region import LevelRegion
from graphics.regions.score_region import ScoreRegion
from graphics.regions.game_info_region import GameInfoRegion


class Window:
    """Class Window. Class dealing with all graphical output."""
    
    def __init__(self):
        """Constructor for the class Window."""        
        self._screen = pygame.display.set_mode(WINDOW_SIZE)
        icon = pygame.image.load(os.path.join(IMAGE_DIRECTORY, ICON_IMAGE_NAME)).convert_alpha()
        pygame.display.set_caption("Tetris")
        pygame.display.set_icon(icon)

        # Variable used to describe if the window was closed or not.
        self._closed = False
            
    def _get_closed(self):
        """Getter for the attribute _closed."""
        return self._closed
    
    def close(self):
        """method allowing to set the the value of _closed parameter to True."""
        self._closed = True
        
    """Definition of a properties for parameter _closed. This parameter can
    only be get from the exteriour, not set nor deleted."""
    closed = property(_get_closed)
        
        
    def draw_menu(self, text_lines, idx_line_selected):
        """Method drawing the main menu screen on the whole window, highlighting the currently
        selected line with a cursor and a different color."""
        # Load logo and cursor assets.
        logo = pygame.image.load(os.path.join(IMAGE_DIRECTORY, LOGO_IMAGE_NAME)).convert_alpha()
        cursor = pygame.image.load(os.path.join(IMAGE_DIRECTORY, CURSOR_IMAGE_NAME)).convert_alpha()

        # Convert color of menu cursor.
        color_selected = COLORS['menu_text_selected']
        width, height = cursor.get_size()
        for col in range(width):
            for line in range(height):
                _, _, _, transparency = cursor.get_at((col, line))
                cursor.set_at((col, line), (*color_selected, transparency))

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

        whole_surface = utils.merge_surfaces_vertically([logo, *text_surfaces])
        
        self._draw_whole_screen(whole_surface)
        
    
    def draw_menu_controls(self, controls_lines):
        """Method drawing the controls menu screen on the whole window."""        
        keys_surfaces = []
        text_surfaces = []
        for text, key_files in controls_lines.items():
            keys_surface = [pygame.image.load(os.path.join(IMAGE_DIRECTORY, key_file)).convert_alpha() for key_file in key_files]
            
            keys_surfaces.append(utils.merge_surfaces_horizontally(keys_surface))
            text_surfaces.append(utils.draw_text(text, MENU_CONTROLS_TEXT_FONT_SIZE))
            
        whole_surface = utils.merge_surfaces_in_table(keys_surfaces, text_surfaces)
        
        self._draw_whole_screen(whole_surface)  
        
        
    def init_game(self):
        """Method instanciating game screen regions as class attributes that will
        then be called at each screen update."""        
        self._hold_region = HoldRegion()
        self._grid_region = GridRegion()
        self._queue_region = QueueRegion()
        self._fps_region   = FPSRegion()
        self._level_region = LevelRegion()
        self._score_region = ScoreRegion()
        self._game_info_region = GameInfoRegion()
        
        
    def end_game(self):
        """Method deleting the game screen regions attributes.""" 
        del self._hold_region
        del self._grid_region
        del self._queue_region
        del self._fps_region
        del self._level_region
        del self._score_region
        del self._game_info_region


    def update_game(self, current_grid, current_tetrimino, queue, held, score,
                    level, goal, lines, fps, show_fps, game_state_text):
        """Window drawing the current game state on the whole window. Calls
        game regions attributes to update themselves and then merges them together
        into the whole frame."""
        self._hold_region.update(held = held)
        self._grid_region.update(current_grid = current_grid, current_tetrimino = current_tetrimino)
        self._queue_region.update(queue = queue)
        self._level_region.update(level = level, goal = goal, lines = lines)
        self._score_region.update(score = score)
        self._game_info_region.update(game_state_text = game_state_text)
        
        surfaces_right_column = [self._queue_region.surface, self._level_region.surface]
        if show_fps:
            self._fps_region.update(fps = fps)
            surfaces_right_column.append(self._fps_region.surface)

        right_column = utils.merge_surfaces_vertically(surfaces_right_column, False)
        central_column = utils.merge_surfaces_vertically([self._grid_region.surface, self._score_region.surface])
        left_column = utils.merge_surfaces_vertically([self._hold_region.surface, self._game_info_region.surface])

        whole_surface = utils.merge_surfaces_horizontally([left_column, central_column, right_column])
        
        self._draw_whole_screen(whole_surface)
        
    
    def _draw_whole_screen(self, surface):
        """Clears the whole window screen and then blits the surface passed as parameter
        in the window, centering it both horizontally and vertically."""
        self._screen.fill(COLORS["background"])
        self._screen.blit(surface, ((self._screen.get_width()-surface.get_width())/2,
                                    (self._screen.get_height()-surface.get_height())/2))        
        pygame.display.update()
   