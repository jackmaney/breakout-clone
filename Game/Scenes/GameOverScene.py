from Game.Scenes.Scene import Scene
import pygame
import re
from Game import Highscore


class GameOverScene(Scene):

    def __init__(self, game):
        super(GameOverScene, self).__init__(game)

        self.playerName = ""

        #self.highScoreSprite = pygame.

    def render(self):
        super(GameOverScene, self).render()

        self.clearText()

        self.addText("Your name: ", 300, 200, size=30)
        self.addText(self.playerName, 420,200, size=30)



        # self.addText("Game Over!", 400, 400, size=50)
        # self.addText("Press any key to start again.", 500, 500, size=25)

    def handleEvents(self, events):
        super(GameOverScene, self).handleEvents(events)

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game = self.game
                    Highscore().add(self.playerName, game.score)
                    game.changeScene("highScore")
                elif event.key == pygame.K_BACKSPACE and len(self.playerName) > 0:
                    self.playerName = self.playerName[:-1]
                else:
                    self.playerName += event.unicode


