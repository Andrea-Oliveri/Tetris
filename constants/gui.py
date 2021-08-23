# -*- coding: utf-8 -*-

from pygame.locals import USEREVENT

# Constant defining the period at which the game will update (chosen to have a framerate close to 60 Hz)
REFRESH_PERIOD = 16

# Constant defined as the id of the event triggered by the pygame timers.
FRAME_EVENT = USEREVENT+1

# Constant defining the DAS Delay in ms
DAS_DELAY = 250

# Constant defining the DAS Period in ms (chosen to allow close to 20 Hz frequency)
DAS_RATE = 50