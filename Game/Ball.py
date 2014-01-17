from Game.Shared import *
import pygame


class Ball(GameObject):

    def __init__(self, position, game,
                 sprite=pygame.Surface(GameConstants.BALL_SIZE),
                 color=(255, 255, 255)):

        self.speed = 3
        self.increment = [2, 2]
        self.direction = [1, 1]
        self.inMotion = 0
        self.sprite = sprite
        self.color = color
        self.sprite.fill(color)

        super(Ball, self).__init__(position, game,
                                   GameConstants.BALL_SIZE, sprite)

    def resetSpeed(self):
        self.speed = 3

    def setMotion(self, isMoving):
        self.inMotion = isMoving
        self.resetSpeed()

    def changeDirection(self, other):

        x, y = None, None

        xLeft = self.intersectsXLeft(other)
        xRight = self.intersectsXRight(other)
        yAbove = self.intersectsYAbove(other)
        yBelow = self.intersectsYBelow(other)

        if yBelow:
            x = self.position[0]
            y = other.position[1] + other.size[1]
            self.direction[1] *= -1
        elif yAbove:
            x = self.position[0]
            y = other.position[1] - self.size[1]
            self.direction[1] *= -1
        elif xLeft:
            x = other.position[0] - self.size[0]
            y = self.position[1]
            self.direction[0] *= -1
        else:
            x = other.position[0] + other.size[0]
            y = self.position[1]
            self.direction[0] *= -1

        if x is not None and y is not None:
            self.position = (x, y)

    # Moves ball
    def updatePosition(self):
        newX = self.position[0] + self.increment[0] * \
            self.speed * self.direction[0]
        newY = self.position[1] + self.increment[1] * \
            self.speed * self.direction[1]

        self.position = [newX, newY]

        self.keepInWindow()

    def keepInWindow(self):
        if self.outOfBoundsLeft() or self.outOfBoundsRight():
            self.direction[0] *= -1
        elif self.outOfBoundsAbove() or self.outOfBoundsBelow():
            self.direction[1] *= -1

        super(Ball, self).keepInWindow()
