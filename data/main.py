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
circle_lst = []


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
        pass

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

    def random_spawn_trees(self):
        for i in range(40):
            x = random.randint(2, 25)
            y = random.randint(9, 19)
            self.board[y][x] = 2
            if self.board[y][x] == 2:
                image = load_image('test_tree.png').convert_alpha()
                tree = pygame.sprite.Sprite(tree_sprites)
                tree.image = image
                tree.rect = tree.image.get_rect()

                tree.rect.x = 32 * (x - 1)
                tree.rect.y = 32 * (y - 1)

    def rerender(self, src):
        phone = load_image('test_grass.png').convert_alpha()
        src.blit(phone, (0, 0))


board = Board(40, 21)
clock = pygame.time.Clock()
a = Hodit()
running = True
board.random_spawn_trees()
Border(3, 3, WIDTH - 3, 3, border1)
Border(3, 203, 3, HEIGHT - 3, border2)
Border(3, HEIGHT - 3, WIDTH - 3, HEIGHT - 3, border3)
Border(WIDTH - 3, 203, WIDTH - 3, HEIGHT - 3, border4)
pg.display.flip()
flag1 = False
flag2 = False
flag3 = False
flag4 = False

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
                else:
                    flag1 = False
            if event.key == pygame.K_s:
                if a.update3():
                    flag2 = True
                else:
                    flag2 = False
            if event.key == pygame.K_w:
                if a.update1():
                    flag3 = True
                else:
                    flag3 = False
            if event.key == pygame.K_d:
                if a.update4():
                    flag4 = True
                else:
                    flag4 = False
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                flag1 = False
            if event.key == pygame.K_s:
                flag2 = False
            if event.key == pygame.K_w:
                flag3 = False
            if event.key == pygame.K_d:
                flag4 = False
        elif event.type == pygame.MOUSEBUTTONUP:
            pass
        elif event.type == pygame.MOUSEBUTTONDOWN:
            b = board.on_click(event.pos)

    if flag1:
        if a.update2():
            a.rect.x -= 20
    if flag2:
        if a.update3():
            a.rect.y += 20
    if flag3:
        if a.update1():
            a.rect.y -= 20
    if flag4:
        if a.update4():
            a.rect.x += 20
    board.rerender(screen)
    all_sprites.draw(screen)
    tree_sprites.draw(screen)
    res_count(screen)

    clock.tick(30)

    pg.display.update()
