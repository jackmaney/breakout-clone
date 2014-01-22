from Game.Scenes.Scene import Scene
import pygame


class MenuScene(Scene):
    def __init__(self, game):
        super(MenuScene, self).__init__(game)

        self.addText("Press 1 to start the game", x=300, y=200, size=30)
        self.addText("Press 2 to display the high scores", x=300, y=240, size=30)
        self.addText("Press Escape to quit", x=300, y=280, size=30)

    def handleEvents(self, events):
        super(MenuScene, self).handleEvents(events)

        for event in events:
            if event.type == pygame.KEYDOWN:
                key = event.unicode
                if key == "1":
                    self.game.reset()
                elif key == "2":
                    self.game.changeScene("highScore")
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit(0)