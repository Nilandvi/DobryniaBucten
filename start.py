import pygame
from pygame.locals import *
import time
pygame.init()
#Подгружаю кадры
frames = ["img\\cuts\\sfr1.png", "img\\cuts\\sfr2.png", "img\\cuts\\sfr3.png", "img\\cuts\\sfr4.png", "img\\cuts\\sfr5.png", "img\\cuts\\sfr0.png"]
WIDTH, HEIGHT = size = 1280, 680
screen = pygame.display.set_mode((WIDTH, HEIGHT))
#заливаю бг картинкой
bg = pygame.image.load(frames[0])
screen.blit(bg, (0, 0))
pygame.display.set_caption('Dobrynia Bucten')
count = -1 #счетчик



running = True
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
            exit()
        elif event.type == pygame.MOUSEBUTTONUP:
            for i in range(254): #Это должен быть цикл который бы затемнял картинку по 1 пикселю и был плавный переход
                ##################https://younglinux.info/pygame/surface
                surf = pygame.Surface((1280, 680))
                surf.fill((0, 0, 0))
                surf.set_alpha(i)
                screen.blit(surf, (0, 0))
                time.sleep(0.1)
            count += 1
            bg = pygame.image.load(frames[count]) #Когда юзер тыкает переключаем картинку на IDшник картинки что в списке, 
            screen.blit(bg, (0, 0))
            for g in range(254): #растемнение. 
                surf = pygame.Surface((1280, 680))
                surf.fill((0, 0, 0))
                surf.set_alpha(255 - g)
                screen.blit(surf, (0, 0))
                time.sleep(0.1)
                #Лучше использовать pygame.clock, но sleep я использовал как временный вариант для теста, как это все работает.
        if count == 5:
            import main

    ##################################

    pygame.display.update()
    pygame.display.flip()

pygame.quit()