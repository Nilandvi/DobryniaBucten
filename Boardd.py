import pygame
import random
from load_image import *
from res import *


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 0
        self.top = 0
        self.cell_size = 32
        self.f = 0
        self.background = None

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

    def random_spawn_trees(self, n, lstx, lsty, sprites, name, c, cc):
        for i in range(n):
            x = random.randint(2, c)
            y = random.randint(9, cc)
            if x in lstx or x + 1 in lstx or x + 2 in lstx or x + 3 in lstx:
                if y in lsty or y + 1 in lsty or y + 2 in lsty or y + 3 in lsty or y + 4 in lsty:
                    continue
            lstx.append(x + 1)
            lsty.append(y + 1)
            self.board[y][x] = 10
            if self.board[y][x] == 10:
                image = load_image_icons(name).convert_alpha()
                tree = pygame.sprite.Sprite(sprites)
                tree.image = image
                tree.rect = tree.image.get_rect()

                tree.rect.x = 32 * (x - 1)
                tree.rect.y = 32 * (y - 1)

    def draw(self, src):
        if self.background:
            src.blit(self.background, (0, 0))

    def set_backgorund(self, name):
        self.background = load_image_location(name).convert_alpha()

    def rubit(self, dobrinya, lstx, lsty, tree_sprites, lines, event, flag):
        self.aa = 0
        self.a = 0
        for i in dobrinya.sprites():
            xd = i.rect.x
            yd = i.rect.y
        b = self.on_click(event)
        x, y = b
        for ii in range(len(lstx)):
            for j in range(len(lsty)):
                if x == lstx[ii] and y == lsty[j]:
                    if lines[9].strip() == "1":
                        self.f += 1
                        self.aa = ii
                        self.a = j
                        break
        if self.f == 6:
            self.f = 0
            for sp in tree_sprites.sprites():
                if flag == 0:
                    ix = sp.rect.x // 32 + 1
                    iy = sp.rect.y // 32 + 1
                    if sp.rect.x == 32 * (x - 1) and sp.rect.y == 32 * (y - 2):
                        if (ix == xd // 32 + 1 or ix == xd // 32 + 2 or ix == xd // 32 + 3 or
                            ix == xd // 32 - 1 or ix == xd // 32 - 2 or ix == xd // 32 - 3 or ix == xd // 32 + 2) \
                                and (iy == yd // 32 or iy == yd // 32 - 1):
                            sp.kill()
                            lstx.remove(ix + 1)
                            lsty.remove(iy + 1)
                            wod = int(lines[2])
                            kek = int(lines[20].rstrip()) + 1
                            wod += random.randrange(10, 20)
                            lines[2] = lines[2].replace(lines[2], str(wod) + '\n')
                            lines[22] = lines[22].replace(lines[22], str(wod) + '\n')
                            lines[20] = lines[20].replace(lines[20], str(kek) + '\n')
                            with open('base.txt', 'w') as fi:
                                fi.writelines(lines)
                                fi.close()
                if flag == 1:
                    ix = sp.rect.x // 32 + 1
                    iy = sp.rect.y // 32 + 1
                    if ix + 1 == x + 2 and iy + 1 == y + 2:
                        if (ix + 1 == xd // 32 + 3 or ix + 1 == xd // 32 or ix + 1 == xd // 32 + 2 or
                            ix + 1 == xd // 32 + 4 or ix + 1 == xd // 32 + 1) and \
                                (iy + 1 == yd // 32 + 3 or iy + 1 == yd // 32 + 2 or iy + 1 == yd // 32 or
                                 iy + 1 == yd // 32 + 1):
                                    sp.kill()
                                    lstx.remove(ix + 1)
                                    lsty.remove(iy + 1)
                                    wod = int(lines[6])
                                    wod += random.randrange(10, 20)
                                    kek = int(lines[20].rstrip()) + 1
                                    lines[6] = lines[6].replace(lines[6], str(wod) + '\n')
                                    lines[26] = lines[26].replace(lines[26], str(wod) + '\n')
                                    lines[20] = lines[20].replace(lines[20], str(kek) + '\n')
                                    with open('base.txt', 'w') as fi:
                                        fi.writelines(lines)
                                        fi.close()
                if flag == 2:
                    ix = sp.rect.x // 32 + 1
                    iy = sp.rect.y // 32 + 1
                    if ix + 1 == x + 2 and iy + 1 == y + 2:
                        if (ix + 1 == xd // 32 + 3 or ix + 1 == xd // 32 or ix + 1 == xd // 32 + 2 or
                            ix + 1 == xd // 32 + 4 or ix + 1 == xd // 32 + 1) and \
                                (iy + 1 == yd // 32 + 3 or iy + 1 == yd // 32 + 2 or iy + 1 == yd // 32 or
                                 iy + 1 == yd // 32 + 1):
                            sp.kill()
                            lstx.remove(ix + 1)
                            lsty.remove(iy + 1)
                            wod = int(lines[4])
                            wod += random.randrange(10, 20)
                            kek = int(lines[20].rstrip()) + 1
                            lines[24] = lines[24].replace(lines[24], str(wod) + '\n')
                            lines[20] = lines[20].replace(lines[20], str(kek) + '\n')
                            lines[4] = lines[4].replace(lines[4], str(wod) + '\n')
                            with open('base.txt', 'w') as fi:
                                fi.writelines(lines)
                                fi.close()

