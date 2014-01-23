import pygame
from Game.Shared import GameConstants
from Game.Bricks import Brick
from Game.Ball import Ball


class BallSpawningBrick(Brick):
    def __init__(self, position, game, points=400, color=(150, 150, 150),
                 sprite=pygame.Surface(GameConstants.BRICK_SIZE)):
        super(BallSpawningBrick, self).__init__(position, game, points=points,
                                                color=color, sprite=sprite)
        pygame.font.init()
        font = pygame.font.Font(None, 16)
        renderedText = font.render("Extra", True, (0, 0, 0))
        textWidth, textHeight = renderedText.get_size()
        blitX = int(GameConstants.BRICK_SIZE[0] / 2.0) - int(textWidth / 2.0)
        blitY = int(GameConstants.BRICK_SIZE[1] / 2.0) - int(textHeight / 2.0)
        self.sprite.blit(renderedText, (blitX, blitY))

    def hit(self, ball):

        super(BallSpawningBrick,self).hit(ball)

        positionX = self.position[0] + int(GameConstants.BRICK_SIZE[0] / 2.0) - int(GameConstants.BALL_SIZE[0] / 2.0)
        positionY = self.position[1] + int(GameConstants.BRICK_SIZE[1] / 2.0) - int(GameConstants.BALL_SIZE[1] / 2.0)

        self.game.balls.append(Ball(self.game, position=(positionX, positionY)))
