from Game.Shared import *
import pygame


class Ball(GameObject):

    def __init__(self, position, game,
                 sprite=pygame.Surface(GameConstants.BALL_SIZE),
                 color=(255, 255, 255)):

        self.game = game
        self.speed = 3
        self.increment = [2, 2]
        self.direction = [1, 1]
        self.inMotion = 0
        self.sprite = sprite
        self.color = color
        self.sprite.fill(color)

        super(Ball, self).__init__(position, GameConstants.BALL_SIZE, sprite)

    def resetSpeed(self):
        self.speed = 3

    def setMotion(self, isMoving):
        self.inMotion = isMoving
        self.resetSpeed()

    def changeDirection(self, gameObject):
        pass

    # Moves ball
    def updatePosition(self):
        self.position = pygame.mouse.get_pos()

    # Is ball outside bounds?
    def isBallDead(self):
        pass
