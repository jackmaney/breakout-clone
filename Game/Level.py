import os
from Game.Bricks import *
from Game.Shared.GameConstants import GameConstants
import numpy as np
import random


class Level(object):
    def __init__(self, game, initialLevel=0):
        self.game = game
        self.bricks = []
        self.amountOfBricksLeft = 0
        self.currentLevel = initialLevel
        self.load(initialLevel)

    def brickHit(self):
        self.amountOfBricksLeft -= 1

    def loadNextLevel(self):
        self.load(self.currentLevel + 1)

    def loadRandom(self):
        self.bricks = []

        x, y = 0, 0

        maxBricks = int(GameConstants.SCREEN_SIZE[0] / GameConstants.BRICK_SIZE[0])

        numSpecialBricks = 0
        maxNumSpecialBricks = 3
        maxNumRows = 3

        numRows = random.randint(2, maxNumRows)

        for i in list(range(0, numRows)):
            for j in list(range(0, maxBricks)):

                brickType = random.randint(0, 4)

                brick = None

                if brickType == 1 or numSpecialBricks > maxNumSpecialBricks:
                    brick = Brick(np.array([x, y], np.int32), self.game)
                elif brickType == 2:
                    brick = SpeedBrick(np.array([x, y], np.int32), self.game)
                    numSpecialBricks += 1
                elif brickType == 3:
                    brick = LifeBrick(np.array([x, y], np.int32), self.game)
                    numSpecialBricks += 1
                elif brickType == 4:
                    brick = BallSpawningBrick(np.array([x, y], np.int32), self.game)
                    numSpecialBricks += 1

                if brick is not None:
                    self.bricks.append(brick)
                    self.amountOfBricksLeft += 1

                x += GameConstants.BRICK_SIZE[0]

            x = 0
            y += GameConstants.BRICK_SIZE[1]

    def load(self, level):

        self.currentLevel = level

        levelFile = os.path.join(".", "Game", "Assets", "Levels",
                                 "level" + str(level) + ".dat")
        self.bricks = []

        try:
            x, y = 0, 0
            with open(levelFile) as f:
                for line in open(levelFile):
                    for char in line:
                        brick = None
                        if char == "1":
                            brick = Brick(np.array([x, y], np.int32), self.game)
                        elif char == "2":
                            brick = SpeedBrick(np.array([x, y], np.int32), self.game)
                        elif char == "3":
                            brick = LifeBrick(np.array([x, y], np.int32), self.game)
                        elif char == "4":
                            brick = BallSpawningBrick(np.array([x, y], np.int32), self.game)

                        if brick is not None:
                            self.bricks.append(brick)
                            self.amountOfBricksLeft += 1

                        x += GameConstants.BRICK_SIZE[0]

                    x = 0
                    y += GameConstants.BRICK_SIZE[1]
        except IOError:
            self.loadRandom()

        file = os.path.join(".", "Game", "Assets", "Levels",
                            "level" + str(level) + ".dat")

