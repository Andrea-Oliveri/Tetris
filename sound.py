# -*- coding: utf-8 -*-

import pygame
import os

from constants.sound import MUSICS_DIRECTORY, EFFECTS_DIRECTORY, DEFAULT_MUSIC


class SoundEngine:
    """Class SoundEngine. Class representing the sound engine."""

    def __init__(self):
        """Constructor for the class SoundEngine."""
        pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)
        pygame.mixer.init()
        
        self._musics_library = [MUSICS_DIRECTORY+name for name in os.listdir(MUSICS_DIRECTORY)]
        self._music_current = [elem for elem in self._musics_library if DEFAULT_MUSIC in elem][0]
        self._effects_library = {}

        for name in os.listdir(EFFECTS_DIRECTORY):
            self._effects_library[name] = pygame.mixer.Sound(name)
            
        self._play_music_current()
            
    def __del__(self):
        """Destructor for the class SoundEngine."""
        pygame.mixer.quit()
        
    def _play_music_current(self):
        """Function that loads and plays in a loop attribute _music_current."""
        pygame.mixer.music.load(self._music_current)
        pygame.mixer.music.play(-1)
        
    def change_music(self):
        """Function that changes the music being played."""
        self._music_current = self._musics_library[(self._musics_library.index(self._music_current)+1)%len(self._musics_library)]
        self._play_music_current()