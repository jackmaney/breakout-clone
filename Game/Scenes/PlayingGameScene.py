from Game.Scenes.Scene import Scene
from Game.Shared import *
import pygame
import numpy as np
import random


class PlayingGameScene(Scene):

    def __init__(self, game):
        super(PlayingGameScene, self).__init__(game)

    def handleEvents(self, events):
        super(PlayingGameScene, self).handleEvents(events)

        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                self.game.paused = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.paused = True

    def render(self):

        super(PlayingGameScene, self).render()

        if len(self.game.level.bricks) == 0:
            self.game.paused = True
            self.game.resetPad()
            self.game.resetBalls()

            self.game.level.loadNextLevel()

        if self.game.lives <= 0:
            self.game.changeScene("gameOver")

        balls = self.game.balls

        for ball in balls:

            if ball.intersects(self.game.pad):
                self.game.playSound("beep")
                ball.changeDirection(self.game.pad)

            for otherBall in balls:
                if ball != otherBall and ball.intersects(otherBall):
                    ball.changeDirection(otherBall)

            for brick in self.game.level.bricks:
                if ball.intersects(brick):
                    brick.hit(ball)
                    ball.changeDirection(brick)
                    break

            if not self.game.paused and not ball.paused:
                ball.updatePosition()

            if ball.isDead():
                self.game.paused = True
                self.game.reduceLives()
                self.game.repositionBalls()
                for b in self.game.balls:
                    b.resetVelocity()
                self.game.resetPad()

            ball.render()

        for brick in self.game.level.bricks:
            if not brick.isDestroyed():
                brick.render()

        if not self.game.paused:
            self.game.pad.updatePosition()

        self.game.pad.render()

        self.clearText()

        self.addText("Score: " + str(self.game.score), x=0,
                     y=GameConstants.SCREEN_SIZE[1] - 60, size=30)
        self.addText("Lives: " + str(self.game.lives), x=0,
                     y=GameConstants.SCREEN_SIZE[1] - 30, size=30)
