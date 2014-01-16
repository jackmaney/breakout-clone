import os


class GameConstants(object):

    SCREEN_SIZE = (800, 600)
    BRICK_SIZE = (100, 30)
    BALL_SIZE = (16, 16)
    PAD_SIZE = (139, 13)

    SPEEDBRICK_IMAGE = os.path.join(
        "Game", "Assets", "Bricks", "speedbrick.png")
    LIFEBRICK_IMAGE = os.path.join("Game", "Assets", "Bricks", "lifebrick.png")
