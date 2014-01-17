from Game.Shared import *
import pygame


class Pad(GameObject):

    def __init__(self, position, game,
                 color=(255, 0, 255),
                 sprite = pygame.Surface(GameConstants.PAD_SIZE)):

        if color is not None:
            sprite.fill(color)

        super(Pad, self).__init__(position, game,
                                  GameConstants.PAD_SIZE, sprite)

    def updatePosition(self):
        destinationX = pygame.mouse.get_pos()[0]

        x = self.position[0]

        if abs(self.position[0] - destinationX) <= GameConstants.PAD_MAX_SPEED:
            x = destinationX
        elif self.position[0] < destinationX:
            x += GameConstants.PAD_MAX_SPEED
        elif self.position[0] > destinationX:
            x -= GameConstants.PAD_MAX_SPEED

        self.position = (x, self.position[1])

        self.keepInWindow()
