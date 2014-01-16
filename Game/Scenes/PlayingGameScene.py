from Game.Scenes.Scene import Scene


class PlayingGameScene(Scene):

    def __init__(self, game):
        super(PlayingGameScene, self).__init__(game)

    def handleEvents(self, events):
        super(PlayingGameScene, self).handleEvents(events)

    def render(self):
        super(PlayingGameScene, self).render()

        for ball in self.game.balls:
            ball.updatePosition()

            self.game.screen.blit(ball.sprite, ball.position)

        for brick in self.game.level.bricks:
            self.game.screen.blit(brick.sprite, brick.position)
