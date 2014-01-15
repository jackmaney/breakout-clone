from Game.Shared import *


class Ball(GameObject):

    def __init__(self, position, sprite, game):
        self.game = game
        self.speed = 3
        self.increment = [2, 2]
        self.direction = [1, 1]
        self.inMotion = 0

        GameObject.__init__(self, position, GameConstants.BALL_SIZE, sprite)

    def resetSpeed(self):
        self.speed = 3

    def setMotion(self, isMoving):
        self.inMotion = isMoving
        self.resetSpeed()

    def changeDirection(self, gameObject):
        pass

    # Moves ball
    def updatePosition(self):
        pass

    # Is ball outside bounds?
    def isBallDead(self):
        pass
