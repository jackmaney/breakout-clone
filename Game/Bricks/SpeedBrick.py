from Game.Bricks import Brick
from Game.Shared.GameConstants import GameConstants
import pygame


class SpeedBrick(Brick):

    def __init__(self, position, game, points=300, color=None,
        sprite=pygame.image.load(GameConstants.SPEEDBRICK_IMAGE)):

        super(SpeedBrick, self).__init__(position, game, points=points, color=None, sprite=sprite)
