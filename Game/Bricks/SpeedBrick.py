from Game.Bricks import Brick
from Game.Shared.GameConstants import GameConstants
import pygame


class SpeedBrick(Brick):

    def __init__(self, position, game, points=300, color=None,
        sprite=pygame.image.load(GameConstants.SPEEDBRICK_IMAGE)):

        super(SpeedBrick, self).__init__(position, game, points=points, color=None, sprite=sprite)

    def hit(self, ball):
        ball.velocity[0] = int(1.5 * ball.velocity[0])
        ball.velocity[1] = int(1.5 * ball.velocity[1])

        super(SpeedBrick,self).hit(ball)