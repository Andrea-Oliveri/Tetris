# -*- coding: utf-8 -*-

# Constant defining the directory in which the sounds are stored.
MUSICS_DIRECTORY = "./assets/sounds/musics/"
EFFECTS_DIRECTORY = "./assets/sounds/effects/"

# Constant defining the name of the music files used while playing and while in
# the menu.
GAME_MUSIC = ["A-Type.mp3", "B-Type.mp3", "C-Type.mp3"]
MENU_MUSIC = ["Menu.mp3"]

# Constant associating for each sound effect's action the file to play.
SOUND_EFFECTS = {"menu_move": "menu/move.wav",                # OK
                 "menu_select": "menu/select.wav",            # OK
                 "menu_back": "menu/back.wav",                # OK
                 "game_count": "game/count.wav",
                 "game_move": "game/move.wav",                # OK
                 "game_rotate": "game/rotate.wav",            # OK
                 "game_hold": "game/hold.wav",                # OK
                 "game_alert": "game/alert.wav",              # NOT IMPLEMENTED?
                 "game_landing": "game/landing.wav",          
                 "game_lock": "game/lock.wav",                # OK
                 "game_soft_drop": "game/soft_drop.wav",      # OK
                 "game_hard_drop": "game/hard_drop.wav",      # OK
                 "game_single": "game/single.wav",            # OK
                 "game_double": "game/double.wav",            # OK
                 "game_triple": "game/triple.wav",            # OK
                 "game_tetris": "game/tetris.wav",            # OK
                 "game_tspin": "game/tspin.wav",              # NOT IMPLEMENTED
                 "game_perfect": "game/perfect.wav",          # OK
                 "game_pause": "game/pause.wav",              # OK
                 "game_gameover": "game/gameover.wav"}        # OK