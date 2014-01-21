from Game.Bricks import Brick
from Game.Shared.GameConstants import GameConstants
import pygame


class LifeBrick(Brick):
    def __init__(self, position, game, points=500, color=(222, 27, 206),
                 sprite=pygame.Surface(GameConstants.BRICK_SIZE)):

        super(LifeBrick, self).__init__(position, game, points=points, color=color, sprite=sprite)

        pygame.font.init()
        font = pygame.font.Font(None, 16)
        renderedText = font.render("1 UP", True, (206, 222, 27))
        textWidth,textHeight = renderedText.get_size()
        blitX = int(GameConstants.BRICK_SIZE[0] / 2.0) - int(textWidth / 2.0)
        blitY = int(GameConstants.BRICK_SIZE[1] / 2.0) - int(textHeight / 2.0)
        self.sprite.blit(renderedText, (blitX,blitY))

    def hit(self, ball):
        self.game.lives += 1

        super(LifeBrick,self).hit(ball)