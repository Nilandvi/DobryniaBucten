import time

from settings import *
from maps import bar
from character import *
from ban import *
import os
from test_from_options import run_options
from minigame import run_minigame

def run_bar(left, right, up, down):
    bg = pygame.image.load("locations\\bar.png")
    screen.blit(bg, (0, 0))
    entities = pygame.sprite.Group() # Все объекты
    platforms = [] # то, во что мы будем врезаться или опираться
    entities.add(hero)
    index = 0
    pygame.mixer.music.load("sounds\\ost.mp3")
    hero.rect.x = 400
    hero.rect.y = 300

    for y in range(len(bar)):
        for x in range(len(bar[y])):
            if bar[y][x] == 2:
                    pf = Platform(x * cell, y * cell)
                    entities.add(pf)
                    platforms.append(pf)
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(float(lines[34]))
    running = True
    while running:
        for events in pygame.event.get():
            if events.type == pygame.QUIT: running = False
            elif events.type == pygame.KEYDOWN:
                if events.key == pygame.K_a:
                    left = True
                    index = 8
                if events.key == pygame.K_d:
                    right = True
                    index = 12
                if events.key == pygame.K_w:
                    up = True
                    index = 4
                if events.key == pygame.K_s:
                    down = True
                    index = 0
                if events.key == pygame.K_ESCAPE:
                    lines[36] = '4'
                    with open('base.txt', 'w') as fi:
                        fi.writelines(lines)
                        fi.close()
                    run_options()
            elif events.type == pygame.KEYUP:
                if events.key == pygame.K_a:
                    left = False
                if events.key == pygame.K_d:
                    right = False
                if events.key == pygame.K_w:
                    up = False
                if events.key == pygame.K_s:
                    down = False
        s = pygame.mixer.Sound('sounds\\shag.ogg')
        s.set_volume(0.35)
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
            s.play(1, 0, 1000)
        else:
            s.stop()
        hero.update(left, right, down, up, platforms)
        entities.draw(screen)
        screen.blit(bg, (0, 0))
        screen.blit(hero.image, hero.rect)
        if 300 <= hero.rect.x <= 510 and 584 <= hero.rect.y <= 680:
            pygame.mixer.music.stop()
            s.stop()
            pygame.mixer.music.load('sounds\\ost1.mp3')
            pygame.mixer.music.play(-1)
            down = False
            up = False
            right = False
            left = False
            break
        elif 715 <= hero.rect.x <= 894 and 205 <= hero.rect.y <= 251:
            pygame.mixer.music.stop()
            s.stop()
            hero.rect.x = 400
            hero.rect.y = 300
            run_minigame()
            down = False
            up = False
            right = False
            left = False
        pg.display.update()
        clock.tick(30)
    return
