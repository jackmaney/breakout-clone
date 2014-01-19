from Game.Shared import *
import pygame
import numpy as np
import math


class Ball(GameObject):

    def __init__(self, position, game,
                 sprite=pygame.Surface(GameConstants.BALL_SIZE),
                 color=(255, 255, 255)):

        self.velocity = np.array(
    [np.random.choice(list(range(-6, 0)) + list(range(1, 7))), np.random.randint(1, 5)])

        self.initialPosition = position.copy()
        self.inMotion = 0
        self.sprite = sprite
        self.color = color
        self.sprite.fill(color)
        self.paused = False

        super(Ball, self).__init__(position, game,
                                   GameConstants.BALL_SIZE, sprite)

    def speed(self):
        return math.sqrt(np.vectorize(lambda x: x * x)(self.velocity).sum())

    def changeDirection(self, other):

        x, y = None, None

        xLeft = self.intersectsXLeft(other)
        xRight = self.intersectsXRight(other)
        yAbove = self.intersectsYAbove(other)
        yBelow = self.intersectsYBelow(other)

        if yBelow:
            x = self.position[0]
            y = other.position[1] + other.size[1]
            self.velocity[1] *= -1
        elif yAbove:
            x = self.position[0]
            y = other.position[1] - self.size[1]
            self.velocity[1] *= -1
        elif xLeft:
            x = other.position[0] - self.size[0]
            y = self.position[1]
            self.velocity[0] *= -1
        else:
            x = other.position[0] + other.size[0]
            y = self.position[1]
            self.velocity[0] *= -1

        if x is not None and y is not None:
            self.position = np.array([x, y], np.int32)

    # Moves ball
    def updatePosition(self):

        if not self.paused:
            self.position += self.velocity

            self.keepInWindow()

    def keepInWindow(self):
        if self.outOfBoundsLeft() or self.outOfBoundsRight():
            self.velocity[0] *= -1
        elif self.outOfBoundsAbove() or self.outOfBoundsBelow():
            self.velocity[1] *= -1

        super(Ball, self).keepInWindow()

    def isDead(self):
        return self.position[1] + self.size[1] >= GameConstants.SCREEN_SIZE[1]
