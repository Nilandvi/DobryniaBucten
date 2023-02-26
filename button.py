from settings import *
from load_image import *


class Buttn(pygame.sprite.Sprite):
    def __init__(self, name, x, y ,buttn):
        super().__init__(buttn)
        dob = load_image_icons('wall-e.png').convert_alpha()
        self.images = [dob, load_image_icons('sand.png').convert_alpha(), load_image_icons('cobl.png').convert_alpha()]
        self.image = self.images[name]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
