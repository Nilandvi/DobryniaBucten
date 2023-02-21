import pygame

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

