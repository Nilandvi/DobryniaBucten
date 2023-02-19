from settings import *
from maps import cave
from character import *
from ban import *
bg = pygame.image.load("data\\cave.png")
screen.blit(bg, (0, 0))
entities = pygame.sprite.Group() # Все объекты
platforms = [] # то, во что мы будем врезаться или опираться
entities.add(hero)
index = 0

for y in range(len(cave)):
    for x in range(len(cave[y])):
        if cave[y][x] == 1:
            pygame.draw.rect(screen, (255, 0, 0), (x * cell, y * cell, cell, cell), 2)
        elif cave[y][x] == 2:
            pygame.draw.rect(screen, (0, 255, 0), (x * cell, y * cell, cell, cell), 2)
            pf = Platform(x * cell, y * cell)
            entities.add(pf)
            platforms.append(pf)
        elif cave[y][x] == 3:
            pygame.draw.rect(screen, (0, 0, 255), (x * cell, y * cell, cell, cell), 2)
            

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
    #screen.blit(bg, (0, 0))
    screen.blit(hero.image, hero.rect)
    pg.display.update()
    clock.tick(30)
pygame.quit()
