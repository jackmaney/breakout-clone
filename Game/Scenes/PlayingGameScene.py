from Game.Scenes.Scene import Scene
import pygame


class PlayingGameScene(Scene):

    def __init__(self, game):
        super(PlayingGameScene, self).__init__(game)

    def handleEvents(self, events):
        super(PlayingGameScene, self).handleEvents(events)

    def render(self):
        super(PlayingGameScene, self).render()

        balls = self.game.balls

        for ball in balls:

            if ball.intersects(self.game.pad):
                ball.changeDirection(self.game.pad)

            for otherBall in balls:
                if ball != otherBall and ball.intersects(otherBall):
                    ball.changeDirection(otherBall)

            for brick in self.game.level.bricks:
                if ball.intersects(brick):
                    brick.hit()
                    ball.changeDirection(brick)
                    break

            ball.updatePosition()

            ball.render()

        for brick in self.game.level.bricks:
            if not brick.isDestroyed():
                brick.render()

        self.game.pad.updatePosition()
        self.game.pad.render()
