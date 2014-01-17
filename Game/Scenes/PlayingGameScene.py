from Game.Scenes.Scene import Scene
import pygame


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
                    brick.hit()
                    ball.changeDirection(brick)
                    break

            if not self.game.paused:
                ball.updatePosition()

            ball.render()

        for brick in self.game.level.bricks:
            if not brick.isDestroyed():
                brick.render()

        if not self.game.paused:
            self.game.pad.updatePosition()
        self.game.pad.render()
