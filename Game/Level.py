
class Level:

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
        pass
