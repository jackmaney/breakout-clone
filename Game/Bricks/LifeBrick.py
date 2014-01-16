from Game.Bricks import Brick
from Game.Shared.GameConstants import GameConstants
import pygame


class LifeBrick(Brick):

    def __init__(self, position, game, color=None,
                 sprite=pygame.image.load(GameConstants.LIFEBRICK_IMAGE)):
        super(LifeBrick, self).__init__(position,
                                        game, color=None, sprite=sprite)
