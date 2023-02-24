import time

from settings import *
from maps import bar
from character import *
from ban import *
import os
bg = pygame.image.load("locations\\bar.png")
screen = sc = pygame.display.set_mode((1280, 640))
screen.blit(bg, (0, 0))
entities = pygame.sprite.Group() # Все объекты
platforms = [] # то, во что мы будем врезаться или опираться
entities.add(hero)
index = 0
pygame.mixer.music.load("sounds\\ost.mp3")

for y in range(len(bar)):
    for x in range(len(bar[y])):
        if bar[y][x] == 2:
                pf = Platform(x * cell, y * cell)
                entities.add(pf)
                platforms.append(pf)
pygame.mixer.music.play()
pygame.mixer.music.set_volume(float(lines[34]))

runGame = True
while runGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: runGame = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                left = True
                index = 8
            if event.key == pygame.K_d:
                right = True
                index = 12
            if event.key == pygame.K_w:
                up = True
                index = 4
            if event.key == pygame.K_s:
                down = True
                index = 0
            if event.key == pygame.K_ESCAPE:
                lines[36] = '4'
                with open('base.txt', 'w') as fi:
                    fi.writelines(lines)
                    fi.close()
                import test_from_options
                exit()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                left = False
            if event.key == pygame.K_d:
                right = False
            if event.key == pygame.K_w:
                up = False
            if event.key == pygame.K_s:
                down = False
    s = pygame.mixer.Sound('sounds\\shag.ogg')
    s.set_volume(0.4)
    if left:
        hero.image = anims[index]
        index += 1
        if index >= 12:
            index = 8
    if right:
        hero.image = anims[index]
        index += 1
        if index >= 15:
            index = 12
    if up:
        hero.image = anims[index]
        index += 1
        if index >= 8:
            index = 4
    if down:
        hero.image = anims[index]
        index += 1
        if index >= 4:
            index = 0

    if down or up or left or right:
        s.play()
        time.sleep(0.05)


    hero.update(left, right, down, up, platforms)
    entities.draw(screen)
    screen.blit(bg, (0, 0))
    screen.blit(hero.image, hero.rect)
    if 300 <= hero.rect.x <= 510 and 584 <= hero.rect.y <= 680:
        os.system('start main.py')
        sys.exit()
    pg.display.update()
    clock.tick(30)
pygame.quit()
