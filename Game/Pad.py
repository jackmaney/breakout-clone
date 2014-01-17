from Game.Shared import *
import pygame


class Pad(GameObject):

    def __init__(self, position, game,
                 color=(255, 0, 255),
                 sprite = pygame.Surface(GameConstants.PAD_SIZE)):

        if color is not None:
            sprite.fill(color)

        super(Pad, self).__init__(position, game,
                                  GameConstants.PAD_SIZE, sprite)
