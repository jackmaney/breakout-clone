import os
from Game.Bricks import *
from Game.Shared.GameConstants import GameConstants


class Level(object):

    def __init__(self, game):
        self.game = game
        self.bricks = []
        self.amountOfBricksLeft = 0
        self.currentLevel = 0

    def brickHit(self):
        self.amountOfBricksLeft -= 1

    def loadNextLevel(self):
        pass

    def load(self, level):
        self.currentLevel = level
        self.bricks = []

        x, y = 0, 0

        file = os.path.join(".", "Game", "Assets", "Levels",
                            "level" + str(level) + ".dat")
        for line in open(file):
            for char in line:
                brick = None
                if char == "1":
                    brick = Brick((x, y), self.game)
                elif char == "2":
                    brick = SpeedBrick((x, y), self.game)
                elif char == "3":
                    brick = LifeBrick((x, y), self.game)

                if brick is not None:
                    self.bricks.append(brick)
                    self.amountOfBricksLeft += 1

                x += GameConstants.BRICK_SIZE[0]

            x = 0
            y += GameConstants.BRICK_SIZE[1]
