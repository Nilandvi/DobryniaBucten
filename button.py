from settings import *
from load_image import *

buttn = pygame.sprite.Group()


class Buttn(pygame.sprite.Sprite):
    def __init__(self, name, x, y):
        super().__init__(buttn)
        dob = load_image_icons(name).convert_alpha()
        self.images = []
        self.image = dob
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
