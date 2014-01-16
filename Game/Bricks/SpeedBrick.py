from Game.Bricks import Brick
from Game.Shared.GameConstants import GameConstants
import pygame


class SpeedBrick(Brick):

    def __init__(self, position, game, color=None,
                 sprite=pygame.image.load(GameConstants.SPEEDBRICK_IMAGE)):
        super(SpeedBrick, self).__init__(position,
                                         game, color=None, sprite=sprite)
