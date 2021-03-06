from Game.Scenes.Scene import Scene
import pygame
from Game import Highscore


class HighscoreScene(Scene):
    def __init__(self, game):
        super(HighscoreScene, self).__init__(game)

    def render(self):
        self.clearText()

        highscore = Highscore()

        x = 350
        y = 100
        for score in highscore.scores:
            self.addText(score["name"], x, y, size=30)
            self.addText(str(score["score"]), x + 200, y, size=30)

            y += 30

        self.addText("Press Escape to quit", x, y + 60, size=30)
        self.addText("or any other key to start a new game", x, y+100, size=30)

        super(HighscoreScene, self).render()

    def handleEvents(self, events):
        super(HighscoreScene, self).handleEvents(events)

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit(0)
                else:
                    self.game.reset()
