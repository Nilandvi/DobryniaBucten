from settings import *
from maps import bar
from character import *
from ban import *
bg = pygame.image.load("map.png")
screen.blit(bg, (0, 0))
entities = pygame.sprite.Group() # Все объекты
platforms = [] # то, во что мы будем врезаться или опираться
entities.add(hero)
index = 0

for y in range(len(bar)):
    for x in range(len(bar[y])):
        if bar[y][x] == 2:
                pf = Platform(x * cell, y * cell)
                entities.add(pf)
                platforms.append(pf)


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
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                left = False
            if event.key == pygame.K_d:
                right = False
            if event.key == pygame.K_w:
                up = False
            if event.key == pygame.K_s:
                down = False
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
    hero.update(left, right, down, up, platforms)
    entities.draw(screen)
    screen.blit(bg, (0, 0))
    screen.blit(hero.image, hero.rect)
    pg.display.update()
    clock.tick(30)
pygame.quit()