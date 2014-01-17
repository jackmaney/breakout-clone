from Game.Shared import *
import pygame


class Pad(GameObject):

    def __init__(self, position, game,
                 color=(255, 0, 255),
                 sprite = pygame.Surface(GameConstants.PAD_SIZE)):
        super(Pad, self).__init__(position, GameConstants.PAD_SIZE, sprite)

        if color is not None:
            self.sprite.fill(color)
