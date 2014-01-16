import pygame
from Game import *
from Game.Scenes import *
from Game.Shared import GameConstants


class Breakout(object):

    def __init__(self):
        self.lives = 5
        self.score = 0

        self.level = Level(self)
        self.level.load(0)

        self.pad = Pad((0, 0), None)
        self.balls = [Ball((0, 0), None, self)]

        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption(
            "Breakout Clone (Game Programming with Python and Pygame)")

        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode(
            GameConstants.SCREEN_SIZE, pygame.DOUBLEBUF, 32)

        pygame.mouse.set_visible(False)

        self.scenes = {
            "playingGame": PlayingGameScene(self),
            "gameOver": GameOverScene(self),
            "highScore": HighscoreScene(self),
            "menuScene": MenuScene(self)
        }

        self.currentScene = self.scenes["playingGame"]

        self.sounds = {}

    def start(self):

        while True:
            self.clock.tick(60)

            self.screen.fill((0, 0, 0))

            self.currentScene.handleEvents(pygame.event.get())
            self.currentScene.render()

            pygame.display.update()

    def changeScene(self, scene):
        pass

    def getLevel(self):
        pass

    def getScore(self):
        pass

    def increaseScore(self, score):
        pass

    def getLives(self):
        pass

    def getBalls(self):
        pass

    def getPad(self):
        pass

    def playSound(self, soundClip):
        pass

    def reduceLives(self):
        pass

    def increaseLives(self):
        pass

    def reset(self):
        pass

Breakout().start()
