
class GameObject(object):

    def __init__(self, position, size, sprite):
        self.position = position
        self.size = size
        self.sprite = sprite

    def intersectsX(self, other):

        if self.position[0] >= other.position[0] \
                and self.position[0] <= other.position[0] + other.size[0]:
            return True

        if (self.position[0] + self.size[0]) > other.position[0] \
                and self.position[0] + self.size[0] <= other.position[0] + other.size[0]:
            return True

        return False

    def intersectsY(self, other):

        if self.position[1] >= other.position[1] \
                and self.position[1] <= other.position[1] + other.size[1]:
            return True

        if self.position[1] + self.size[1] > other.position[1] \
                and self.position[1] + self.size[1] <= other.position[1] + other.size[1]:
            return True

        return False

    def intersects(self, other):
        return self.intersectsX(other) and self.intersectsY(other)
