from settings import lines
from load_image import *


class Shop(pygame.sprite.Sprite):
    def __init__(self, shop):
        super().__init__(shop)
        dob = load_image_icons('shop_map.png').convert_alpha()
        self.images = []
        self.image = dob
        self.rect = self.image.get_rect()
        self.rect.x = 690
        self.rect.y = 1