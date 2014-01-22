import os
from Game.Bricks import *
from Game.Shared.GameConstants import GameConstants
import numpy as np
import random


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

    def loadRandom(self):
        self.bricks = []

        x, y = 0, 0

        maxBricks = int(GameConstants.SCREEN_SIZE[0] / GameConstants.BRICK_SIZE[0])

        numSpecialBricks = 0

        numRows = random.randint(2, 8)

        for row in list(range(0, numRows)):
            for brick in list(range(0, maxBricks)):

                brickType = random.randint(0, 4)

                brick = None

                if brickType == 1 or numSpecialBricks > 6:
                    brick = Brick(np.array([x, y], np.int32), self.game)
                elif brickType == 2:
                    brick = SpeedBrick(np.array([x, y], np.int32), self.game)
                    numSpecialBricks += 1
                elif brickType == 3:
                    brick = LifeBrick(np.array([x, y], np.int32), self.game)
                    numSpecialBricks += 1
                elif brickType == 4:
                    brick =BallSpawningBrick(np.array([x, y], np.int32), self.game)

                if brick is not None:
                    self.bricks.append(brick)
                    self.amountOfBricksLeft += 1

                x += GameConstants.BRICK_SIZE[0]

            x = 0
            y += GameConstants.BRICK_SIZE[1]


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
                    brick = Brick(np.array([x, y], np.int32), self.game)
                elif char == "2":
                    brick = SpeedBrick(np.array([x, y], np.int32), self.game)
                elif char == "3":
                    brick = LifeBrick(np.array([x, y], np.int32), self.game)

                if brick is not None:
                    self.bricks.append(brick)
                    self.amountOfBricksLeft += 1

                x += GameConstants.BRICK_SIZE[0]

            x = 0
            y += GameConstants.BRICK_SIZE[1]
