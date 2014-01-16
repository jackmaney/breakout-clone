import pygame
import sys


class Scene(object):

    def __init__(self, game):
        self.game = game
        self.texts = []

    def render(self):
        pass

    def handleEvents(self, events):

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

    def clearText(self):
        self.texts = []

    def addText(self, text, x=0, y=0,
                color=(255, 255, 255), background=(0, 0, 0), size=17):
        pass
