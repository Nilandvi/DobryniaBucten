import pygame
from load_image_loc import load_image

lstx = []
index = 0
lsty = []



class Hodit(pygame.sprite.Sprite):
    def __init__(self, dobr):
        super().__init__(dobr)
        dob = load_image('test_dobryny.png').convert_alpha()
        self.images = []
        self.images.append(load_image('test_dobryny.png').convert_alpha())
        self.images.append(load_image('dobryny_ass.png').convert_alpha())
        self.images.append(load_image('dobryny_ass_left.png').convert_alpha())
        self.images.append(load_image('dobryny_ass_right.png').convert_alpha())
        self.images.append(load_image('test_dobryny.png').convert_alpha())
        self.images.append(load_image('dobryny_before_left.png').convert_alpha())
        self.images.append(load_image('dobryny_before_right.png').convert_alpha())
        self.images.append(load_image('dobryny_side.png').convert_alpha())
        self.images.append(load_image('dobryny_side_left.png').convert_alpha())
        self.images.append(load_image('dobryny_side_right.png').convert_alpha())
        self.images.append(load_image('dobryny_side1.png').convert_alpha())
        self.images.append(load_image('dobryny_side1_left.png').convert_alpha())
        self.images.append(load_image('dobryny_side1_right.png').convert_alpha())
        self.image = dob
        self.rect = self.image.get_rect()
        self.rect.x = 534
        self.rect.y = 160

    def update1(self, bord):
        if pygame.sprite.spritecollideany(self, bord):
            return False
        else:
            return True

    def update2(self, bord):
        if pygame.sprite.spritecollideany(self, bord):
            return False
        else:
            return True

    def update3(self, bord):
        if pygame.sprite.spritecollideany(self, bord):
            return False
        else:
            return True

    def update4(self, bord):
        if pygame.sprite.spritecollideany(self, bord):
            return False
        else:
            return True

    def update5(self, bord):
        if pygame.sprite.spritecollideany(self, bord):
            return False
        else:
            return True

    def update6(self, bord):
        if pygame.sprite.spritecollideany(self, bord):
            return False
        else:
            return True

    def pupam(self, lstx, lsty):
        for x in range(len(lstx)):
            a = self.rect.x // 32 + 3
            b = self.rect.y // 32 + 4
            if a == lstx[x] + 2 and b == lsty[x] + 3 or a == lstx[x] + 3 and b == lsty[x] + 2 or \
                    a == lstx[x] + 3 and b == lsty[x] + 1:
                self.rect.x += 11

    def pupa2m(self, lstx, lsty):
        for x in range(len(lstx)):
            a = self.rect.x // 32 + 2
            b = self.rect.y // 32 + 3
            if a == lstx[x] and b == lsty[x] or a == lstx[x] + 1 and b == lsty[x] or a == lstx[x] - 1 and b == lsty[x]:
                self.rect.y -= 11

    def pupa3m(self, lstx, lsty):
        for x in range(len(lstx)):
            a = self.rect.x // 32 + 1
            b = self.rect.y // 32 + 1
            if a == lstx[x] and b == lsty[x] or a == lstx[x] - 2 and b == lsty[x] or a == lstx[x] - 1 and b == lsty[x]:
                self.rect.y += 11

    def pupa4m(self, lstx, lsty):
        for x in range(len(lstx)):
            a = self.rect.x // 32 + 1
            b = self.rect.y // 32 + 1
            if a == lstx[x] - 1 and b == lsty[x] or a == lstx[x] - 2 and b == lsty[x] - 1 or \
                    a == lstx[x] - 2 and b == lsty[x] - 2:
                self.rect.x -= 11

    def pupac(self, lstx, lsty):
        for x in range(len(lstx)):
            a = self.rect.x // 32 + 2
            b = self.rect.y // 32 + 2
            if a == lstx[x] and b == lsty[x]:
                self.rect.x += 11

    def pupa2c(self, lstx, lsty):
        for x in range(len(lstx)):
            a = self.rect.x // 32 + 2
            b = self.rect.y // 32 + 3
            if a == lstx[x] and b == lsty[x] or a == lstx[x] - 1 and b == lsty[x]:
                self.rect.y -= 11

    def pupa3c(self, lstx, lsty):
        for x in range(len(lstx)):
            a = self.rect.x // 32 + 2
            b = self.rect.y // 32 + 2
            if a == lstx[x] and b == lsty[x] or a == lstx[x] - 1 and b == lsty[x]:
                self.rect.y += 11

    def pupa4c(self, lstx, lsty):
        for x in range(len(lstx)):
            a = self.rect.x // 32 + 3
            b = self.rect.y // 32 + 3
            if a == lstx[x] and b == lsty[x] + 1:
                self.rect.x -= 11

