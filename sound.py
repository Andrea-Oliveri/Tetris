# -*- coding: utf-8 -*-

import pygame
import os

from constants.sound import MUSICS_DIRECTORY, EFFECTS_DIRECTORY, GAME_MUSIC, MENU_MUSIC, SOUND_EFFECTS


class SoundEngine:
    """Class SoundEngine. Class representing the sound engine."""

    def __init__(self):
        """Constructor for the class SoundEngine."""
        pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)
        
        self._game_tracks = [MUSICS_DIRECTORY + name for name in GAME_MUSIC]
        self._menu_tracks = [MUSICS_DIRECTORY + name for name in MENU_MUSIC]

        self.use_menu_music()
        
        self._effects_library = {name: pygame.mixer.Sound(EFFECTS_DIRECTORY + file) for name, file in SOUND_EFFECTS.items()}


    def __del__(self):
        """Destructor for the class SoundEngine."""
        pygame.mixer.quit()

        
    def use_game_music(self):
        self._current_tracks = self._game_tracks
        self._current_track_idx = 0
        self._play_music_current()
        
        
    def use_menu_music(self):
        self._current_tracks = self._menu_tracks
        self._current_track_idx = 0
        self._play_music_current()
        
        
    def change_track(self):
        """Function that changes the music track being played, while remaining
        coherent to if the music is a menu or game music."""
        old_track_idx = self._current_track_idx
        self._current_track_idx = (self._current_track_idx + 1) % len(self._current_tracks)
        
        if not old_track_idx == self._current_track_idx:
            self._play_music_current()
        
        
    def _play_music_current(self):
        """Function that loads and plays in a loop attribute _music_current."""
        pygame.mixer.music.load(self._current_tracks[self._current_track_idx])
        pygame.mixer.music.play(-1)
        
    
    def play_sound_effect(self, effect):
        self._effects_library[effect].play()