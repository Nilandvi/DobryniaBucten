from settings import lines
from load_image import *


class Home(pygame.sprite.Sprite):
    def __init__(self, home):
        super().__init__(home)
        dob = load_image_icons('test_home3.png').convert_alpha()
        self.images = [dob, load_image_icons('test_home2.png').convert_alpha(),
                       load_image_icons('test_home1.png').convert_alpha(),
                       load_image_icons('test_home1.png').convert_alpha()]
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.x = 352
        self.rect.y = 1
    def hohome(self):
        global lines
        if lines[14] == '2' + '\n':
            res = 1
        elif lines[14] == '3' + '\n':
            res = 2
        elif lines[14] == '4' + '\n':
            res = 3
        else:
            res = 0
        return res
