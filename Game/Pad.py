from Game.Shared import *


class Pad(GameObject):

    def __init__(self, position, sprite):
        GameObject.__init__(self, position, GameConstants.PAD_SIZE, sprite)
