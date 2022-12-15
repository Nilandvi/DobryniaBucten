import pygame
import pygame as pg
import sys
import os
import random

pygame.init()
WIDTH = 1280
HEIGHT = 680

screen = pygame.display.set_mode((WIDTH, HEIGHT))
sc = screen

circle_lst = []


def load_image(name, colorkey=None):
    fullname = os.path.join('img', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


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

    def render(self, src):
        flag = True
        pygame.draw.rect(src,
                         (0, 255, 127), ((0 + self.left, 0 + self.top),
                                         (self.width * self.cell_size, self.height * self.cell_size)), 0)
        for i in range(self.height):
            for j in range(self.width):
                if self.board[i][j] == 1:
                    image = load_image('test_tree.png')
                    sc.blit(image, (32 * (j - 1), 32 * (i - 1)))
                    flag = False

                elif self.board[i][j] == 2:
                    color = (128, 128, 0)
                    line_width = 0
                else:
                    color = (0, 255, 127)
                    line_width = 0
                if flag:
                    pygame.draw.rect(src,
                                     color,
                                     ((j * self.cell_size + self.left, i * self.cell_size + self.top),
                                     (self.cell_size, self.cell_size)),
                                     line_width)

    def on_click(self, pos):
        x, y = pos
        x = (x - self.left) // self.cell_size
        y = (y - self.top) // self.cell_size
        if 0 <= x < self.width and 0 <= y < self.height:
            self.board[y][x] += 1
            self.board[y][x] %= 3
            print(x, y)

    def random_spawn_trees(self, sc):
        pass


board = Board(40, 21)
running = True
while running:
    sc.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEMOTION:
            pass
        elif event.type == pygame.MOUSEBUTTONUP:
            pass
        elif event.type == pygame.MOUSEBUTTONDOWN:
            board.on_click(event.pos)
        elif event.type == pygame.KEYDOWN:
            pass
        elif event.type == pygame.KEYUP:
            pass
    screen.fill((0, 0, 0))
    board.render(screen)

    pg.display.update()
