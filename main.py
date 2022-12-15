import pygame
from pygame.color import THECOLORS


class Board:
    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 32
        self.lst = []

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size
        for i in range(self.height):
            for j in range(self.width):
                pygame.draw.rect(screen, (46, 139, 87), (self.left, self.top, self.cell_size, self.cell_size), 1)
                if i == 0 and j == 0:
                    self.lst.append(self.left)
                    self.lst.append(self.top)
                self.left += cell_size
                if i == self.height - 1 and j == self.width - 1:
                    self.lst.append(self.left)
                    self.lst.append(self.top + self.cell_size)
                    print(*self.lst)
            self.top += cell_size
            self.left = left

    def render(self, screen):
        for i in range(self.height):
            for j in range(self.width):
                pygame.draw.rect(screen, (46, 139, 87), (self.left, self.top, self.cell_size, self.cell_size), 1)
                if i == 0 and j == 0:
                    self.lst.append(self.left)
                    self.lst.append(self.top)
                self.left += self.cell_size
                if i == self.height - 1 and j == self.width - 1:
                    self.lst.append(self.left)
                    self.lst.append(self.top + self.cell_size)

            self.top += self.cell_size
            self.left = 10

    def get_cell(self, mouse_pos):
        mouse_pos2 = list(mouse_pos)
        if (int(mouse_pos2[0]) < self.lst[0] or int(mouse_pos2[1] < self.lst[1])) or \
                (int(mouse_pos2[0]) > int(self.lst[2]) or int(mouse_pos2[1]) > int(self.lst[3])):
            print(None)
            return None
        else:
            print(mouse_pos)
            return mouse_pos

    def on_click(self, cell_coords):
        pass
#           for j in range(self.width):
#                self.clc = list(cell_coords)
#                if self.clc[0] <= self.left or self.clc[1] <= self.top:
#                    print(i, j)
#                self.left += self.cell_size
#            self.top += self.cell_size
#            self.left = 10

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)


if __name__ == '__main__':
    size = w, h = 1820, 980
    screen = pygame.display.set_mode(size, pygame.RESIZABLE)
    screen.fill(THECOLORS['mediumseagreen'])
    running = True
    board = Board(56, 30)
    board.render(screen)

    pygame.display.flip()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.get_click(event.pos)
