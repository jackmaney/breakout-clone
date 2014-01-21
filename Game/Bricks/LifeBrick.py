from Game.Bricks import Brick
from Game.Shared.GameConstants import GameConstants
import pygame


class LifeBrick(Brick):
    def __init__(self, position, game, points=500, color=None,
                 sprite=pygame.image.load(GameConstants.LIFEBRICK_IMAGE)):

        super(LifeBrick, self).__init__(position, game, points=points, color=None, sprite=sprite)
