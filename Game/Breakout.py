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
        self.balls = [
            Ball((0, 0), self)]

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
        self.currentScene = scene

    def increaseScore(self, score):
        self.score += score

    def playSound(self, soundClip):
        sound = self.sounds[soundClip]

        sound.stop()
        sound.play()

    def reduceLives(self):
        self.lives -= 1

    def increaseLives(self):
        self.lives += 1

    def reset(self):
        pass

Breakout().start()
