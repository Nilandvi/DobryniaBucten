import pygame
import pygame as pg
import sys
import os
import random
from pygame.locals import *
import time

pygame.init()
WIDTH, HEIGHT = 1280, 680
width, height = 1280, 680
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.blit(pygame.image.load("data\\cave.png"), (0, 0))

with open('a.txt') as fp2:
    lines = fp2.readlines()

def res_count(screen, file):
    wood, rock, clay = pygame.image.load('data\\oak.png'), pygame.image.load('data\\rock.png'), pygame.image.load('data\\clay.png')
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

all_sprites = pygame.sprite.Group()
horizontal_borders = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()

class Rock:
    def __init__(self, x, y):
        dog_surf = pg.image.load('data\\rock.png')
        dog_rect = dog_surf.get_rect(
        bottomright=(x, y))
        screen.blit(dog_surf, dog_rect)

class Border(pygame.sprite.Sprite):
    # строго вертикальный или строго горизонтальный отрезок
    def __init__(self, x1, y1, x2, y2):
        super().__init__(all_sprites)
        if x1 == x2:
            self.add(vertical_borders)
            self.image = pygame.Surface([1, y2 - y1])
            self.rect = pygame.Rect(x1, y1, 1, y2 - y1)
        else:
            self.add(horizontal_borders)
            self.image = pygame.Surface([x2 - x1, 1])
            self.rect = pygame.Rect(x1, y1, x2 - x1, 1)

Border(207, 0, 207, 16)
Border(190, 16, 207, 16)
Border(190, 16, 190, 144)
Border(190, 144, 206, 144)
Border(207, 145, 207, 175)
Border(209, 175, 221, 175)
Border(224, 175, 224, 206)
Border(224, 206, 238, 206)
Border(238, 208, 238, 239)
Border(238, 239, 254, 239)
Border(254, 239, 254, 256)
Border(254, 256, 268, 256)
Border(269, 256, 271, 273)
Border(271, 273, 287, 271)
Border(287, 271, 287, 288)
Border(286, 288, 303, 289)
Border(300, 290, 303, 306)
Border(303, 304, 317, 306)
Border(317, 305, 319, 321)
Border(319, 321, 334, 320)
Border(334, 320, 334, 334)
Border(335, 334, 352, 338)
Border(352, 338, 352, 352)
Border(352, 352, 366, 353)
Border(366, 353, 366, 415)
Border(368, 415, 382, 416)
Border(382, 416, 382, 450)
Border(383, 450, 397, 449)
Border(397, 449, 397, 512)
Border(399, 512, 414, 512)
Border(414, 512, 414, 545)
Border(415, 544, 430, 545)
Border(430, 545, 432, 561)
Border(432, 561, 445, 561)
Border(445, 561, 445, 670)
Border(447, 670, 461, 670)
Border(461, 671, 463, 679)
Border(1249, 384, 1279, 384)
Border(1249, 384, 1249, 398)
Border(1185, 398, 1249, 402)
Border(1185, 402, 1185, 416)
Border(1170, 416, 1185, 416)
Border(1170, 416, 1170, 434)
Border(1154, 434, 1167, 434)
Border(1154, 434, 1154, 449)
Border(1137, 449, 1154, 449)
Border(1137, 449, 1137, 465)
Border(1120, 465, 1136, 465)
Border(1120, 467, 1120, 480)
Border(1104, 480, 1120, 480)
Border(1104, 481, 1104, 498)
Border(1089, 498, 1105, 498)
Border(1071, 511, 1071, 576)
Border(1057, 576, 1071, 576)
Border(1057, 576, 1057, 637)
Border(1041, 637, 1057, 641)
Border(1041, 641, 1041, 653)
Border(1024, 653, 1041, 653)
Border(1024, 656, 1024, 679)





for i in range(1000):
    Rock(random.randint(475, 1015), random.randint(19, 664))
for g in range(5):
    Rock(random.randint(230, 443), random.randint(14, 239))

count = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
                print(pygame.mouse.get_pos())
                count += 1
                if count == 2:
                    print("=====")
                    count = 0
    res_count(screen, lines)
    all_sprites.draw(screen)
    pg.display.update()


