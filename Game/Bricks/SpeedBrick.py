from Game.Bricks import Brick
from Game.Shared.GameConstants import GameConstants
import pygame


class SpeedBrick(Brick):

    def __init__(self, position, game, points=500, color=(255, 174, 0),
                 sprite=pygame.Surface(GameConstants.BRICK_SIZE)):

        super(SpeedBrick, self).__init__(position, game, points=points, color=color, sprite=sprite)

        pygame.font.init()
        font = pygame.font.Font(None, 16)
        renderedText = font.render("ZOOM !", True, (255, 0, 208))
        textWidth,textHeight = renderedText.get_size()
        blitX = int(GameConstants.BRICK_SIZE[0] / 2.0) - int(textWidth / 2.0)
        blitY = int(GameConstants.BRICK_SIZE[1] / 2.0) - int(textHeight / 2.0)
        self.sprite.blit(renderedText, (blitX,blitY))

    def hit(self, ball):
        ball.velocity[0] = int(1.5 * ball.velocity[0])
        ball.velocity[1] = int(1.5 * ball.velocity[1])

        super(SpeedBrick,self).hit(ball)