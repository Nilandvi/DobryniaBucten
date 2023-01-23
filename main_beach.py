import pygame
import pygame as pg
import sys
import os
import random
from pygame.locals import *
import time

flags = FULLSCREEN | DOUBLEBUF
pygame.init()
WIDTH = 1280
HEIGHT = 680
screen = pygame.display.set_mode((WIDTH, HEIGHT))
sc = screen
lstx = []
index = 0
lsty = []
m = 0
with open('a.txt') as fp2:
    lines = fp2.readlines()


def res_count(screen, file):
    wood = pygame.image.load('data\\oak.png')
    rock = pygame.image.load('data\\rock.png')
    clay = pygame.image.load('data\\clay.png')
    screen.blit(wood, (0, 0))
    screen.blit(rock, (100, 0))
    screen.blit(clay, (200, 0))
    font = pygame.font.Font(None, 40)
    textw = font.render(file[2].strip(), True, (98, 99, 155))
    textr = font.render(file[4].strip(), True, (98, 99, 155))
    textc = font.render(file[6].strip(), True, (98, 99, 155))
    screen.blit(textw, (35, 5))
    screen.blit(textr, (135, 5))
    screen.blit(textc, (235, 5))


def load_image(name):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


all_sprites = pygame.sprite.Group()
border1 = pygame.sprite.Group()
border2 = pygame.sprite.Group()
border3 = pygame.sprite.Group()
border4 = pygame.sprite.Group()
border5 = pygame.sprite.Group()
border6 = pygame.sprite.Group()
tree_sprites = pygame.sprite.Group()
dobrinya = pygame.sprite.Group()
b = pygame.sprite.Group()


class Border(pygame.sprite.Sprite):
    def __init__(self, x1, y1, x2, y2, name):
        super().__init__(b)
        if x1 == x2:
            self.add(name)
            self.image = pygame.Surface([1, y2 - y1])
            self.rect = pygame.Rect(x1, y1, 1, y2 - y1)
        else:
            self.add(name)
            self.image = pygame.Surface([x2 - x1, 1])
            self.rect = pygame.Rect(x1, y1, x2 - x1, 1)


class Hodit(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(dobrinya)
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
        self.rect.x = 110
        self.rect.y = 10

    def update1(self):
        if pygame.sprite.spritecollideany(self, border1):
            return False
        else:
            return True

    def update2(self):
        if pygame.sprite.spritecollideany(self, border2):
            return False
        else:
            return True

    def update3(self):
        if pygame.sprite.spritecollideany(self, border3):
            return False
        else:
            return True

    def update4(self):
        if pygame.sprite.spritecollideany(self, border4):
            return False
        else:
            return True

    def update5(self):
        if pygame.sprite.spritecollideany(self, border5):
            return False
        else:
            return True

    def update6(self):
        if pygame.sprite.spritecollideany(self, border6):
            return False
        else:
            return True



class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 0
        self.top = 0
        self.cell_size = 32
        self.f = 0

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def on_click(self, pos):
        x, y = pos
        x = (x - self.left) // self.cell_size
        y = (y - self.top) // self.cell_size
        if 0 <= x < self.width and 0 <= y < self.height:
            return x, y

    def random_spawn_trees(self, n):
        for i in range(n):
            x = random.randint(2, 27)
            y = random.randint(9, 14)
            if x in lstx or x + 1 in lstx or x + 2 in lstx or x + 3 in lstx:
                if y in lsty or y + 1 in lsty or y + 2 in lsty or y + 3 in lsty or y + 4 in lsty:
                    continue
            lstx.append(x + 1)
            lsty.append(y + 1)
            self.board[y][x] = 10
            if self.board[y][x] == 10:
                image = load_image('clay_test2.png').convert_alpha()
                tree = pygame.sprite.Sprite(tree_sprites)
                tree.image = image
                tree.rect = tree.image.get_rect()

                tree.rect.x = 32 * (x - 1)
                tree.rect.y = 32 * (y - 1)

    def rerender(self, src):
        phone = load_image('test_beach1.png').convert_alpha()
        src.blit(phone, (0, 0))

    def rubit(self):
        self.aa = 0
        self.a = 0
        for i in dobrinya.sprites():
            xd = i.rect.x
            yd = i.rect.y
        b = board.on_click(event.pos)
        x, y = b
        for i in range(len(lstx)):
            for j in range(len(lsty)):
                if x == lstx[i] and y == lsty[j]:
                    if lines[9].strip() == "1":
                        self.f += 1
                        break
        if self.f == 6:
            self.f = 0
            for sp in tree_sprites.sprites():
                ix = sp.rect.x // 32 + 1
                iy = sp.rect.y // 32 + 1
                print(ix + 1, iy + 1)
                print(xd // 32 + 3)
                print(yd // 32 + 2)

                if ix + 1 == x + 2 and iy + 1 == y + 2:
                    if (ix + 1 == xd // 32 + 3 or ix + 1 == xd // 32 or ix + 1 == xd // 32 + 2 or
                        ix + 1 == xd // 32 + 4 or ix + 1 == xd // 32 + 1) and \
                            (iy + 1 == yd // 32 + 3 or iy + 1 == yd // 32 + 2 or iy + 1 == yd // 32 or
                             iy + 1 == yd // 32 + 1):
                        sp.kill()
                        print(ix)
                        print(iy)
                        lstx.remove(ix + 1)
                        lsty.remove(iy + 1)
                        print(lstx)
                        print(lsty)
                        wod = int(lines[6])
                        wod += random.randrange(10, 20)
                        lines[6] = lines[6].replace(lines[6], str(wod) + '\n')
                        with open('a.txt', 'w') as fi:
                            fi.writelines(lines)
                            fi.close()


board = Board(40, 21)
clock = pygame.time.Clock()
a = Hodit()

running = True
board.random_spawn_trees(50)
print(lstx)
print(lsty)
Border(1, 1, WIDTH - 1, 1, border1)
Border(9, 90, 9, HEIGHT - 3, border2)
Border(3, HEIGHT - 200, WIDTH - 390, HEIGHT - 200, border3)
Border(WIDTH - 9, 3, WIDTH - 9, HEIGHT - 3, border4)
Border(WIDTH - 260, HEIGHT - 200, WIDTH - 9, HEIGHT - 3, border3)
Border(212, 90, WIDTH - 1, 1, border1)
Border(212, 60, WIDTH - 1, 30, border3)
Border(202, 60, 202, 85, border4)
Border(WIDTH - 270, HEIGHT - 200, WIDTH - 270, HEIGHT - 40, border4)
Border(WIDTH - 380, HEIGHT - 200, WIDTH - 380, HEIGHT - 40, border2)
Border(WIDTH - 380, HEIGHT - 40, WIDTH - 270, HEIGHT - 40, border3)
Border(9, 90, 110, 90, border1)
Border(9, 60, 110, 60, border3)
Border(120, 60, 120, 85, border2)
pg.display.flip()
flag1 = False
flag2 = False
flag3 = False
flag4 = False
spin = False
shiz = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEMOTION:
            pass
        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_a:
                if a.update2():
                    flag1 = True
                    index = 7

            if event.key == pygame.K_s:
                if a.update3():
                    flag2 = True
                    index = 4

            if event.key == pygame.K_w:
                if a.update1():
                    flag3 = True
                    index = 1

            if event.key == pygame.K_d:
                if a.update4():
                    flag4 = True
                    index = 10

            if event.key == pygame.K_e:
                if a.update5():
                    spin = True
                    index = 0

            if event.key == pygame.K_q:
                if a.update6():
                    shiz = True
                    index = 0

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                flag1 = False
            if event.key == pygame.K_s:
                flag2 = False
            if event.key == pygame.K_w:
                flag3 = False
            if event.key == pygame.K_d:
                flag4 = False
            if event.key == pygame.K_e:
                spin = False
            if event.key == pygame.K_q:
                shiz = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            board.f += 1
            board.rubit()
            with open('a.txt', 'r') as f:
                l = f.readlines()
            res_count(screen, l)

    if spin:
        if a.update5():
            a.image = a.images[index]
            dis = pg.image.load('data\\dislike.png')
            dis_rect = dis.get_rect(bottomright=((a.rect.x + 80), (a.rect.y + 15)))
            sc.blit(dis, dis_rect)
            pg.display.update()
            index += 1
            if index >= 12:
                index = 0
    if shiz:
        if a.update6():
            a.image = a.images[index]
            imgs = ["data\\m1.png", "data\\m2.png", "data\\m3.png", "data\\m4.png"]
            m += 1
            dis = pg.image.load(imgs[m])
            dis_rect = dis.get_rect(bottomright=((a.rect.x + 40), (a.rect.y + 15)))
            sc.blit(dis, dis_rect)
            pg.display.update()
            index += 1
            if index >= 12:
                index = 0
            if m >= 3:
                m = 0

    if flag1:
        if a.update2():
            a.rect.x -= 11
        a.image = a.images[index]
        index += 1
        if index >= 9:
            index = 7
    if flag2:
        if a.update3():
            a.rect.y += 11
        a.image = a.images[index]
        index += 1
        if index >= 6:
            index = 4
    if flag3:
        if a.update1():
            a.rect.y -= 11

        a.image = a.images[index]
        index += 1
        if index >= 3:
            index = 1

    if flag4:
        if a.update4():
            a.rect.x += 11
        a.image = a.images[index]
        index += 1
        if index >= 12:
            index = 10
    board.rerender(screen)
    all_sprites.draw(screen)
    tree_sprites.draw(screen)
    dobrinya.draw(screen)
    res_count(screen, lines)
    if a.rect.x <= 80 and a.rect.y <= 40:
        print('уходим')
    clock.tick(30)

    pg.display.update()
