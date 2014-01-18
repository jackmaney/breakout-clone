import pygame
import sys


class Scene(object):

    def __init__(self, game):
        self.game = game
        self.texts = []

    def render(self):
        for text in self.texts:
            self.game.screen.blit(text["renderedText"], text["coordinates"])

    def handleEvents(self, events):

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

    def clearText(self):
        self.texts = []

    def addText(self, text, x=0, y=0,
                color=(255, 255, 255), background=(0, 0, 0), size=17):
        font = pygame.font.Font(None, size)
        self.texts.append(
            {"renderedText": font.render(text, True, color, background), "coordinates": (x, y)})
