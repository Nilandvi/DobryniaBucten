from settings import lines
from load_image import *


class Chest(pygame.sprite.Sprite):
    def __init__(self, home):
        super().__init__(home)
        dob = load_image_icons('chest.png').convert_alpha()
        self.image = dob
        self.rect = self.image.get_rect()
        self.rect.x = 1200
        self.rect.y = 200