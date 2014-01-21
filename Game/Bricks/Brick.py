from Game.Shared import GameObject
from Game.Shared import GameConstants
import pygame


class Brick(GameObject):
    def __init__(self, position, game, points=100, color=(0, 255, 0),
                 sprite=pygame.Surface(GameConstants.BRICK_SIZE)):
        self.position = position
        self.color = color
        self.sprite = sprite
        self.points = points

        if color is not None:
            self.sprite.fill(color)

        super(Brick, self).__init__(position, game,
                                    GameConstants.BRICK_SIZE, sprite)

        self.hitPoints = 100
        self.lives = 1

    def isDestroyed(self):
        return self.lives <= 0

    def hit(self, ball):
        self.lives -= 1
        if self.isDestroyed():
            self.game.score += self.points
            self.game.removeBrick(self)

    def getHitSound(self):
        pass
