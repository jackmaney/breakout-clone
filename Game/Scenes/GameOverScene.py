from Game.Scenes.Scene import Scene
import pygame


class GameOverScene(Scene):

    def __init__(self, game):
        super(GameOverScene, self).__init__(game)

    def render(self):
        super(GameOverScene, self).render()

        self.clearText()
        self.addText("Game Over!", 400, 400, size=50)
        self.addText("Press any key to start again.", 500, 500, size=25)

    def handleEvents(self, events):
        super(GameOverScene, self).handleEvents(events)

        for event in events:
            if event.type == pygame.KEYDOWN:
                self.game.reset()
