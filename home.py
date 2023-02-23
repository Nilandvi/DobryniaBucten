from settings import *
from load_image import *

home = pygame.sprite.Group()

class Home(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(home)
        dob = load_image_icons('test_home1.png').convert_alpha()
        self.images = []
        self.image = dob
        self.rect = self.image.get_rect()
        self.rect.x = 352
        self.rect.y = 1
