from Game.Shared import *
import pygame
import numpy as np
import math
import random


class Ball(GameObject):
    def __init__(self, game, position=None, velocity=None,
                 sprite=pygame.Surface(GameConstants.BALL_SIZE),
                 color=(255, 255, 255)):

        self.sprite = sprite
        self.velocity = None
        if velocity is None:
            self.resetVelocity()
        else:
            self.velocity = np.array(velocity, np.int32)

        self.position = None
        if position is None:
            x = game.pad.position[0] + int((game.pad.sprite.get_size()[0] / 2.0) - \
                                           (self.sprite.get_size()[0] / 2.0))
            y = game.pad.position[1] - self.sprite.get_size()[1] - GameConstants.VERTICAL_PAD_BALL_BUFFER
            self.position = np.array([x, y], np.int32)
        else:
            self.position = np.array(position, np.int32)

        self.initialPosition = self.position.copy()
        self.inMotion = 0

        self.color = color
        self.sprite.fill(color)
        self.paused = False

        super(Ball, self).__init__(self.position, game,
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
        elif xRight:
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
            self.game.playSound("hittingWall")
            self.velocity[0] *= -1
        elif self.outOfBoundsAbove() or self.outOfBoundsBelow():
            if self.outOfBoundsAbove():
                self.game.playSound("hittingWall")
            self.velocity[1] *= -1

        super(Ball, self).keepInWindow()

    def isDead(self):
        return self.position[1] + self.size[1] >= GameConstants.SCREEN_SIZE[1]

    def resetVelocity(self):
        self.velocity = np.array(
            [random.choice(list(range(-10, 0)) + list(range(1, 10))),
             np.random.randint(-10, -1)])
