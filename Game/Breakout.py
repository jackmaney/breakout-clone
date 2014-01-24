import pygame
import numpy as np
from Game import *
from Game.Scenes import *
from Game.Shared import GameConstants


class Breakout(object):
    def __init__(self):

        self.paused = True

        self.lives = 5
        self.score = 0

        self.pad = None
        self.resetPad()

        self.level = Level(self)

        self.balls = None
        self.resetBalls()

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

        self.currentScene = self.scenes["menuScene"]

        beep = pygame.mixer.Sound(GameConstants.BEEP_SOUND)
        self.sounds = {
            "beep": beep
        }

    def start(self):

        while True:
            self.clock.tick(60)

            self.screen.fill((0, 0, 0))

            self.currentScene.handleEvents(pygame.event.get())
            self.currentScene.render()

            pygame.display.update()

    def changeScene(self, scene):
        self.currentScene = self.scenes[scene]

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
        self.paused = True
        self.lives = 5
        self.score = 0
        self.resetPad()
        self.resetBalls()
        self.level.load(0)
        self.changeScene("playingGame")

    def removeBrick(self, brick):

        try:
            self.level.bricks.remove(brick)
        except ValueError:
            # Not terribly graceful, but I don't want the game dying...
            # will think of a better way
            pass

    def repositionBalls(self):
        new = []

        centerX = int(GameConstants.SCREEN_SIZE[0] / 2.0) - int(GameConstants.BALL_SIZE[0] / 2.0)
        initialX = centerX

        numBalls = len(self.balls)
        y = self.pad.position[1] - GameConstants.BALL_SIZE[1] - GameConstants.VERTICAL_PAD_BALL_BUFFER

        if numBalls % 2 == 1 and numBalls > 1:
            # The center of the screen cuts right through the (int(numBalls/2) + 1)^th ball.
            # So, we have half of a ball-width, int(numBalls/2) full ball-widths,
            # and int(numBalls/2) - 1 horizontal paddings.

            initialX -= int(GameConstants.BALL_SIZE[0] / 2.0) - int(numBalls / 2) * GameConstants.BALL_SIZE[0] - int(
                numBalls / 2) * GameConstants.HORIZONTAL_BALL_BUFFER

        elif numBalls % 2 == 0:
            # The first numBalls/2 are to the left of the center of the screen.
            # But we also have the horizontal buffer in between...

            initialX -= (numBalls / 2) * (GameConstants.BALL_SIZE[0] + GameConstants.HORIZONTAL_BALL_BUFFER)

        x = initialX

        for i in list(range(numBalls)):
            new.append(Ball(self, position=[x, y]))
            x += GameConstants.BALL_SIZE[0] + GameConstants.HORIZONTAL_BALL_BUFFER

        self.balls = new


    def resetBalls(self):
        self.balls = [
            Ball(self)
        ]

    def resetPad(self):
        self.pad = Pad(self)
