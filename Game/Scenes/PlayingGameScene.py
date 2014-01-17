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

            for otherBall in balls:
                if ball != otherBall and ball.intersects(otherBall):
                    ball.changeDirection(otherBall)

            for brick in self.game.level.bricks:
                if ball.intersects(brick):
                    brick.hit()
                    ball.changeDirection(brick)
                    break

            ball.updatePosition()

            self.game.screen.blit(ball.sprite, ball.position)

        for brick in self.game.level.bricks:
            if not brick.isDestroyed():
                self.game.screen.blit(brick.sprite, brick.position)

        self.game.pad.position = (
            pygame.mouse.get_pos()[0], self.game.pad.position[1])
        self.game.pad.keepInWindow()
        self.game.screen.blit(self.game.pad.sprite, self.game.pad.position)
