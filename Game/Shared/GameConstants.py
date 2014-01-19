import os
import numpy as np


class GameConstants(object):

    SCREEN_SIZE = (800, 600)
    BRICK_SIZE = (100, 30)
    BALL_SIZE = (16, 16)
    PAD_SIZE = (139, 13)
    PAD_MAX_SPEED = 10
    PADDING_BELOW_PAD = 2
    PAD_INITIAL_POSITION = np.array(
        [np.round((SCREEN_SIZE[0] - PAD_SIZE[0]) / 2.0),
         SCREEN_SIZE[1] - PAD_SIZE[1] - PADDING_BELOW_PAD], np.int32)

    SPEEDBRICK_IMAGE = os.path.join(
        "Game", "Assets", "Bricks", "speedbrick.png")
    LIFEBRICK_IMAGE = os.path.join("Game", "Assets", "Bricks", "lifebrick.png")

    BEEP_SOUND = os.path.join("Game", "Assets", "Sounds", "beep.ogg")
