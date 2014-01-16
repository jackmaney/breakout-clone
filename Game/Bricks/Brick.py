from Game.Shared import GameObject
from Game.Shared import GameConstants


class Brick(GameObject):

    def __init__(self, position, sprite, game):
        self.game = game

        super(Brick, self).__init__(position, GameConstants.BRICK_SIZE, sprite)

        self.hitPoints = 100
        self.lives = 1

    def isDestroyed(self):
        return self.lives <= 0

    def hit(self):
        self.lives -= 1

    def getHitSound(self):
        pass
