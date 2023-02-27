from settings import *
from load_image import *
from dobrynia import Hodit
from Boardd import Board
from res import *
from button import Buttn
from test_from_options import run_options

def location_cave():
    lstx = []
    index = 0
    lsty = []
    m = 0

    all_sprites = pygame.sprite.Group()
    border1 = pygame.sprite.Group()
    border2 = pygame.sprite.Group()
    border3 = pygame.sprite.Group()
    border4 = pygame.sprite.Group()
    border5 = pygame.sprite.Group()
    border6 = pygame.sprite.Group()
    tree_sprites = pygame.sprite.Group()
    dobrinya = pygame.sprite.Group()
    b = pygame.sprite.Group()
    buttn = pygame.sprite.Group()

    class Border(pygame.sprite.Sprite):
        def __init__(self, x1, y1, x2, y2, name):
            super().__init__(b)
            if x1 == x2:
                self.add(name)
                self.image = pygame.Surface([1, y2 - y1])
                self.rect = pygame.Rect(x1, y1, 1, y2 - y1)
            else:
                self.add(name)
                self.image = pygame.Surface([x2 - x1, 1])
                self.rect = pygame.Rect(x1, y1, x2 - x1, 1)


    board = Board(40, 21)
    speed = 11
    if lines[16].rstrip() == '1':
        speed += 5
    clock = pygame.time.Clock()
    a = Hodit(dobrinya)
    k = Buttn(2, 1280 - 120, 680 - 128, buttn)

    running = True
    board.random_spawn_trees(50, lstx, lsty, tree_sprites, 'rock_.png', 30, 17)
    Border(1, 70, WIDTH - 160, 70, border1)
    Border(WIDTH - 75, 70, WIDTH - 3, 70, border1)
    Border(40, 3, 40, HEIGHT - 3, border2)
    Border(3, HEIGHT - 3, WIDTH - 3, HEIGHT - 3, border3)
    Border(WIDTH - 40, 3, WIDTH - 40, HEIGHT - 3, border4)
    pg.display.flip()
    flag1 = False
    flag2 = False
    flag3 = False
    flag4 = False
    spin = False
    shiz = False
    pygame.mixer.music.load('sounds\\cave.mp3')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(float(lines[34]))
    board.set_backgorund('cave.png')
    s = pygame.mixer.Sound('sounds\\hag.ogg')
    s.set_volume(0.35)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEMOTION:
                pass
            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_a:
                    if a.update2(border2):
                        a.pupac(lstx, lsty, speed)
                        flag1 = True
                        index = 7

                if event.key == pygame.K_s:
                    if a.update3(border3):
                        a.pupa2c(lstx, lsty, speed)
                        flag2 = True
                        index = 4

                if event.key == pygame.K_w:
                    if a.update1(border1):
                        a.pupa3c(lstx, lsty, speed)
                        flag3 = True
                        index = 1

                if event.key == pygame.K_d:
                    if a.update4(border4):
                        a.pupa4c(lstx, lsty, speed)
                        flag4 = True
                        index = 10

                if event.key == pygame.K_e:
                    if a.update5(border4):
                        spin = True
                        index = 0

                if event.key == pygame.K_q:
                    if a.update6(border4):
                        shiz = True
                        index = 0
                if event.key == pygame.K_ESCAPE:
                    lines[36] = '3'
                    with open('base.txt', 'w') as fi:
                        fi.writelines(lines)
                        fi.close()
                    run_options()

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    flag1 = False
                if event.key == pygame.K_s:
                    flag2 = False
                if event.key == pygame.K_w:
                    flag3 = False
                if event.key == pygame.K_d:
                    flag4 = False
                if event.key == pygame.K_e:
                    spin = False
                if event.key == pygame.K_q:
                    shiz = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                board.f += 1
                board.rubit(dobrinya, lstx, lsty, tree_sprites, lines, event.pos, 2)
                res_count(screen, lines)

        if spin:
            if a.update5(border4):
                a.image = a.images[index]
                dis = pg.image.load('icons\\dislike.png')
                dis_rect = dis.get_rect(bottomright=((a.rect.x + 80), (a.rect.y + 15)))
                sc.blit(dis, dis_rect)
                pg.display.update()
                index += 1
                if index >= 12:
                    index = 0
        if shiz:
            if a.update6(border4):
                a.image = a.images[index]
                imgs = ["icons\\m1.png", "icons\\m2.png", "icons\\m3.png", "icons\\m4.png"]
                m += 1
                dis = pg.image.load(imgs[m])
                dis_rect = dis.get_rect(bottomright=((a.rect.x + 40), (a.rect.y + 15)))
                sc.blit(dis, dis_rect)
                pg.display.update()
                index += 1
                if index >= 12:
                    index = 0
                if m >= 3:
                    m = 0

        if flag1:
            if a.update2(border2):
                a.pupac(lstx, lsty, speed)
                a.rect.x -= speed
            a.image = a.images[index]
            index += 1
            if index >= 9:
                index = 7
        if flag2:
            if a.update3(border3):
                a.pupa2c(lstx, lsty, speed)
                a.rect.y += speed
            a.image = a.images[index]
            index += 1
            if index >= 6:
                index = 4
        if flag3:
            if a.update1(border1):
                a.pupa3c(lstx, lsty, speed)
                a.rect.y -= speed

            a.image = a.images[index]
            index += 1
            if index >= 3:
                index = 1

        if flag4:
            if a.update4(border4):
                a.pupa4c(lstx, lsty, speed)
                a.rect.x += speed
            a.image = a.images[index]
            index += 1
            if index >= 12:
                index = 10
        board.draw(screen)
        buttn.draw(screen)
        all_sprites.draw(screen)
        tree_sprites.draw(screen)
        dobrinya.draw(screen)
        res_count(screen, lines)

        if flag1 or flag2 or flag3 or flag4 or spin or shiz:
            s.play(1, 0)

        if a.rect.x >= WIDTH - 140 and a.rect.y <= 50:
            pygame.mixer.music.stop()
            s.stop()
            break
        elif a.rect.x >= 1280 - 120 and a.rect.y >= 680 - 128:
            board.random_spawn_trees(1, lstx, lsty, tree_sprites, 'rock_.png', 30, 17)
        else:
            clock.tick(30)
            pg.display.update()
