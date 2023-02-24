from settings import *
from load_image import *
from dobrynia import Hodit
from Boardd import Board
from res import *
from button import Buttn
from button import buttn

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
clock = pygame.time.Clock()
a = Hodit(dobrinya)
k = Buttn('cobl.png')

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

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEMOTION:
            pass
        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_a:
                if a.update2(border2):
                    a.pupac(lstx, lsty)
                    flag1 = True
                    index = 7

            if event.key == pygame.K_s:
                if a.update3(border3):
                    a.pupa2c(lstx, lsty)
                    flag2 = True
                    index = 4

            if event.key == pygame.K_w:
                if a.update1(border1):
                    a.pupa3c(lstx, lsty)
                    flag3 = True
                    index = 1

            if event.key == pygame.K_d:
                if a.update4(border4):
                    a.pupa4c(lstx, lsty)
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
            with open('base.txt', 'r') as f:
                l = f.readlines()
            res_count(screen, l)

    if spin:
        if a.update5(border4):
            a.image = a.images[index]
            dis = pg.image.load('data\\dislike.png')
            dis_rect = dis.get_rect(bottomright=((a.rect.x + 80), (a.rect.y + 15)))
            sc.blit(dis, dis_rect)
            pg.display.update()
            index += 1
            if index >= 12:
                index = 0
    if shiz:
        if a.update6(border4):
            a.image = a.images[index]
            imgs = ["data\\m1.png", "data\\m2.png", "data\\m3.png", "data\\m4.png"]
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
            a.pupac(lstx, lsty)
            a.rect.x -= 11
        a.image = a.images[index]
        index += 1
        if index >= 9:
            index = 7
    if flag2:
        if a.update3(border3):
            a.pupa2c(lstx, lsty)
            a.rect.y += 11
        a.image = a.images[index]
        index += 1
        if index >= 6:
            index = 4
    if flag3:
        if a.update1(border1):
            a.pupa3c(lstx, lsty)
            a.rect.y -= 11

        a.image = a.images[index]
        index += 1
        if index >= 3:
            index = 1

    if flag4:
        if a.update4(border4):
            a.pupa4c(lstx, lsty)
            a.rect.x += 11
        a.image = a.images[index]
        index += 1
        if index >= 12:
            index = 10
    board.rerender(screen, 'cave.png')
    buttn.draw(screen)
    all_sprites.draw(screen)
    tree_sprites.draw(screen)
    dobrinya.draw(screen)
    res_count(screen, lines)


    if a.rect.x >= WIDTH - 140 and a.rect.y <= 50:
        os.system('start main.py')
        exit()
    elif a.rect.x >= 1280 - 120 and a.rect.y >= 680 - 128:
        board.random_spawn_trees(1, lstx, lsty, tree_sprites, 'rock_.png', 30, 17)
    else:
        clock.tick(30)
        pg.display.update()
