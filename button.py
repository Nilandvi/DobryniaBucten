from settings import *
from load_image import *

buttn = pygame.sprite.Group()


class Buttn(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(buttn)
        dob = load_image_icons('wall-e.png').convert_alpha()
        self.images = []
        self.image = dob
        self.rect = self.image.get_rect()
        self.rect.x = 1280 - 80
        self.rect.y = 680 - 121