import pygame
import pygame as pg
import sys
import os
import random
from pygame.locals import *
from test_file import res_count

flags = FULLSCREEN | DOUBLEBUF
pygame.init()
WIDTH = 1280
HEIGHT = 680
screen = pygame.display.set_mode((WIDTH, HEIGHT))
sc = screen
lstx = []
lsty = []
with open('a.txt') as fp:

    lines = fp.readlines()


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
tree_sprites = pygame.sprite.Group()


class Border(pygame.sprite.Sprite):
    def __init__(self, x1, y1, x2, y2, name):
        super().__init__(all_sprites)
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
        super().__init__(all_sprites)
        dob = load_image('test_dobryny.png').convert_alpha()
        self.image = dob
        self.rect = self.image.get_rect()
        self.rect.x = 640
        self.rect.y = 140

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

    def updatetrees(self):
        for i in tree_sprites.sprites():
            if pygame.sprite.collide_mask(self, i):
                return False
        return True


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 0
        self.top = 0
        self.cell_size = 32

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
            x = random.randint(2, 32)
            y = random.randint(9, 19)
            if x in lstx or x + 1 in lstx:
                if y in lsty or y + 1 in lsty:
                    continue
            lstx.append(x)
            lsty.append(y)
            self.board[y][x] = 9
            if self.board[y][x] == 9:
                image = load_image('test_tree.png').convert_alpha()
                tree = pygame.sprite.Sprite(tree_sprites)
                tree.image = image
                tree.rect = tree.image.get_rect()

                tree.rect.x = 32 * (x - 1)
                tree.rect.y = 32 * (y - 1)

    def rerender(self, src):
        phone = load_image('test_grass.png').convert_alpha()
        src.blit(phone, (0, 0))

    def rubit(self):
        b = board.on_click(event.pos)
        x, y = b
        for i in lstx:
            for j in lsty:
                if x == i and y == j:
                    if lines[9].strip() == "1":
                        self.board[y][x] -= 1
                if self.board[y][x] == 0:
                    for i in tree_sprites.sprites():
                        if i.rect.x == 32 * (x - 1) and i.rect.y == 32 * (y - 1):
                            i.kill()
                            wod = int(lines[2])
                            wod += random.randrange(10, 20)
                            lines[2] = lines[2].replace(lines[2], str(wod) + '\n')
                            with open('a.txt', 'w') as f:
                                f.writelines(lines)
                                f.close()
                            res_count(screen)

                        else:
                            pass


board = Board(40, 21)
clock = pygame.time.Clock()
a = Hodit()
running = True
board.random_spawn_trees(50)
Border(3, 3, WIDTH - 3, 3, border1)
Border(3, 203, 3, HEIGHT - 3, border2)
Border(3, HEIGHT - 3, WIDTH - 3, HEIGHT - 3, border3)
Border(WIDTH - 3, 203, WIDTH - 3, HEIGHT - 3, border4)
pg.display.flip()
flag1 = False
flag2 = False
flag3 = False
flag4 = False
print(lstx)
print(lsty)
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
            if event.key == pygame.K_s:
                if a.update3():
                    flag2 = True
            if event.key == pygame.K_w:
                if a.update1():
                    flag3 = True
            if event.key == pygame.K_d:
                if a.update4():
                    flag4 = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                flag1 = False
            if event.key == pygame.K_s:
                flag2 = False
            if event.key == pygame.K_w:
                flag3 = False
            if event.key == pygame.K_d:
                flag4 = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            b = board.rubit()

    if flag1:
        if a.update2():
            a.rect.x -= 15
    if flag2:
        if a.update3():
            a.rect.y += 15
    if flag3:
        if a.update1():
            a.rect.y -= 15
    if flag4:
        if a.update4():
            a.rect.x += 15
    board.rerender(screen)
    all_sprites.draw(screen)
    tree_sprites.draw(screen)
    res_count(screen)

    clock.tick(30)

    pg.display.update()
