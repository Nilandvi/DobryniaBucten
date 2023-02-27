from main_cave import location_cave
from main_beach import location_beach
from shop import run_shop
from settings import *
from res import *
from load_image import *
from home import Home
from dobrynia import Hodit
from res import *
from Boardd import Board
from button import Buttn
from shop_on_main import Shop
from bar import run_bar

lstx = []
index = 0
lsty = []
m = 0

all_sprites = pygame.sprite.Group()
border1 = pygame.sprite.Group()
border2 = pygame.sprite.Group()
border3 = pygame.sprite.Group()
border4 = pygame.sprite.Group()
tree_sprites = pygame.sprite.Group()
dobrinya = pygame.sprite.Group()
b = pygame.sprite.Group()
home = pygame.sprite.Group()
shop1 = pygame.sprite.Group()
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
h = Home(home)
k = Buttn(0, 1280 - 120, 680 - 128, buttn)
sh = Shop(shop1)
running = True
board.random_spawn_trees(50, lstx, lsty, tree_sprites, 'test__tree2.png', 30, 17)

Border(380, 130, 515, 130, border1)
Border(573, 130, 715, 130, border1)
Border(9, 183, 9, HEIGHT - 3, border2)
Border(715, 1, 715, 130, border2)
Border(375, 1, 375, 130, border4)
Border(3, HEIGHT - 53, WIDTH - 3, HEIGHT - 3, border3)
Border(WIDTH - 9, 143, WIDTH - 9, HEIGHT - 3, border4)
Border(1, 1, WIDTH - 1, 1, border1)
Border(755, 130, 850, 130, border1)
Border(908, 130, 1000, 130, border1)
Border(1000, 1, 1000, 130, border2)
Border(755, 1, 755, 130, border4)
pg.display.flip()
flag1 = False
flag2 = False
flag3 = False
flag4 = False
spin = False
shiz = False
pygame.mixer.music.load('sounds\\ost1.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(float(lines[34]))
board.set_backgorund('test_grass4.png')
s = pygame.mixer.Sound('sounds\\sshag.ogg')
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
                    a.pupam(lstx, lsty, speed)
                    flag1 = True
                    index = 7

            if event.key == pygame.K_s:
                if a.update3(border3):
                    a.pupa2m(lstx, lsty, speed)
                    flag2 = True
                    index = 4

            if event.key == pygame.K_w:
                if a.update1(border1):
                    a.pupa3m(lstx, lsty, speed)
                    flag3 = True
                    index = 1

            if event.key == pygame.K_d:
                if a.update4(border4):
                    a.pupa4m(lstx, lsty, speed)
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
                lines[36] = '1'
                with open('base.txt', 'w') as fi:
                    fi.writelines(lines)
                    fi.close()
                import test_from_options
                exit()

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
            board.rubit(dobrinya, lstx, lsty, tree_sprites, lines, event.pos, 0)
            res_count(screen, lines)
    inn = h.hohome()
    for i in home.sprites():
        i.image = h.images[inn]
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
            a.pupam(lstx, lsty, speed)
            a.rect.x -= speed
        a.image = a.images[index]
        index += 1
        if index >= 9:
            index = 7
    if flag2:
        if a.update3(border3):
            a.pupa2m(lstx, lsty, speed)
            a.rect.y += speed
        a.image = a.images[index]
        index += 1
        if index >= 6:
            index = 4
    if flag3:
        if a.update1(border1):
            a.pupa3m(lstx, lsty, speed)
            a.rect.y -= speed

        a.image = a.images[index]
        index += 1
        if index >= 3:
            index = 1

    if flag4:
        if a.update4(border4):
            a.pupa4m(lstx, lsty, speed)
            a.rect.x += speed
        a.image = a.images[index]
        index += 1
        if index >= 12:
            index = 10

    if flag1 or flag2 or flag3 or flag4 or spin or shiz:
        s.play(1, 0)
    board.draw(screen)
    buttn.draw(screen)
    all_sprites.draw(screen)
    tree_sprites.draw(screen)
    dobrinya.draw(screen)
    home.draw(screen)
    shop1.draw(screen)
    res_count(screen, lines)
    if a.rect.x <= 80 and a.rect.y <= 121:
        location_cave()
        a.rect.x = 524
        a.rect.y = 200
        flag1 = False
        flag2 = False
        flag3 = False
        flag4 = False
        spin = False
        shiz = False
    elif a.rect.x >= 1230 and a.rect.y <= 121:
        location_beach()
        a.rect.x = 524
        a.rect.y = 200
        flag1 = False
        flag2 = False
        flag3 = False
        flag4 = False
        spin = False
        shiz = False
    elif a.rect.x >= 1280 - 120 and a.rect.y >= 680 - 128:
        board.random_spawn_trees(1, lstx, lsty, tree_sprites, 'test__tree2.png', 30, 17)
    elif 515 <= a.rect.x <= 573 and 110 <= a.rect.y <= 150:
        if lines[14] == '3' + '\n' or lines[14] == '4' + '\n':
            run_bar()
            a.rect.x = 524
            a.rect.y = 200
            flag1 = False
            flag2 = False
            flag3 = False
            flag4 = False
            spin = False
            shiz = False
    elif 850 <= a.rect.x <= 905 and 120 <= a.rect.y <= 140:
        run_shop()
        a.rect.x = 524
        a.rect.y = 200
        flag1 = False
        flag2 = False
        flag3 = False
        flag4 = False
        spin = False
        shiz = False

    else:
        clock.tick(30)
        pg.display.update()

