from settings import *

class Platform(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((cell, cell))
        self.image.fill(Color(cell))
        self.rect = Rect(x, y, cell, cell)