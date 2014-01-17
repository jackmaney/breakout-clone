from Game.Shared.GameConstants import *


class GameObject(object):

    def __init__(self, position, game, size, sprite):
        self.position = position
        self.size = size
        self.sprite = sprite
        self.game = game

    def intersectsXLeft(self, other):

        return self.position[0] + self.size[0] > other.position[0] and \
            self.position[0] + \
            self.size[0] <= other.position[0] + other.size[0]

    def intersectsXRight(self, other):

        return self.position[0] >= other.position[0] and \
            self.position[0] <= other.position[0] + other.size[0]

    def intersectsX(self, other):

        return self.intersectsXLeft(other) or self.intersectsXRight(other)

    def intersectsYAbove(self, other):

        return self.position[1] + self.size[1] > other.position[1] and \
            self.position[1] + \
            self.size[1] <= other.position[1] + other.size[1]

    def intersectsYBelow(self, other):

        return self.position[1] >= other.position[1] and \
            self.position[1] <= other.position[1] + other.size[1]

    def intersectsY(self, other):

        return self.intersectsYAbove(other) or self.intersectsYBelow(other)

    def intersects(self, other):

        return self.intersectsX(other) and self.intersectsY(other)

    def outOfBoundsLeft(self):
        return self.position[0] < 0

    def outOfBoundsRight(self):
        return self.position[0] + self.size[0] > GameConstants.SCREEN_SIZE[0]

    def outOfBoundsAbove(self):
        return self.position[1] < 0

    def outOfBoundsBelow(self):
        return self.position[1] + self.size[1] > GameConstants.SCREEN_SIZE[1]

    def keepInWindow(self):

        x, y = self.position

        if self.outOfBoundsLeft():
            x = 0
        elif self.outOfBoundsRight():
            x = GameConstants.SCREEN_SIZE[0] - self.size[0]
        elif self.outOfBoundsAbove():
            y = 0
        elif self.outOfBoundsBelow():
            y = GameConstants.SCREEN_SIZE[1] - self.size[1]

        self.position = (x, y)

    def render(self):
        self.game.screen.blit(self.sprite, self.position)
