import pygame
from pygame.locals import *
pygame.init()

WIDTH, HEIGHT = size = 1280, 680
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill((0,0,0))
pygame.display.set_caption('Texture See Test')

with open('a.txt') as fp:
    lines = fp.readlines()

class ResCount():
    wood = pygame.image.load('data\\oak.png')
    rock = pygame.image.load('data\\rock.png')
    clay = pygame.image.load('data\\clay.png')
    screen.blit(wood, (0, 0))
    screen.blit(rock, (100, 0))
    screen.blit(clay, (200, 0))
    font = pygame.font.Font(None, 40)
    textw = font.render(lines[2].strip(), True, (98, 99, 155))
    textr = font.render(lines[4].strip(), True, (98, 99, 155))
    textc = font.render(lines[6].strip(), True, (98, 99, 155))
    screen.blit(textw, (35, 5))
    screen.blit(textr, (135, 5))
    screen.blit(textc, (235, 5))

running = True
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
            exit()
        elif event.type == pygame.MOUSEBUTTONUP:
            print(pygame.mouse.get_pos())

    ##################################
    pygame.display.update()
    pygame.display.flip()

pygame.quit()