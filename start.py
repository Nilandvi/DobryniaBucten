import pygame
from pygame.locals import *
pygame.init()

frames = ["img\\cuts\\sfr1.png", "img\\cuts\\sfr2.png", "img\\cuts\\sfr3.png", "img\\cuts\\sfr4.png", "img\\cuts\\sfr5.png", "img\\cuts\\sfr0.png"]
WIDTH, HEIGHT = size = 1280, 680
screen = pygame.display.set_mode((WIDTH, HEIGHT))

bg = pygame.image.load(frames[0])
screen.blit(bg, (0, 0))
pygame.display.set_caption('Dobrynia Bucten')
count = -1

running = True
while running:
    events = pygame.event.get()
    for event in events:
        if count == 4:
            import main
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
            exit()
        elif event.type == pygame.MOUSEBUTTONUP:
            count += 1
            bg = pygame.image.load(frames[count])
            screen.blit(bg, (0, 0))
        if count == 5:
            import main

    ##################################

    pygame.display.update()
    pygame.display.flip()

pygame.quit()