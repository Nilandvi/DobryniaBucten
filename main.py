from settings import *
from res import *
from load_image import *
from home import Home
from home import home

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


class Hodit(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(dobrinya)
        dob = load_image_data('test_dobryny.png').convert_alpha()
        self.images = []
        self.images.append(load_image_data('test_dobryny.png').convert_alpha())
        self.images.append(load_image_data('dobryny_ass.png').convert_alpha())
        self.images.append(load_image_data('dobryny_ass_left.png').convert_alpha())
        self.images.append(load_image_data('dobryny_ass_right.png').convert_alpha())
        self.images.append(load_image_data('test_dobryny.png').convert_alpha())
        self.images.append(load_image_data('dobryny_before_left.png').convert_alpha())
        self.images.append(load_image_data('dobryny_before_right.png').convert_alpha())
        self.images.append(load_image_data('dobryny_side.png').convert_alpha())
        self.images.append(load_image_data('dobryny_side_left.png').convert_alpha())
        self.images.append(load_image_data('dobryny_side_right.png').convert_alpha())
        self.images.append(load_image_data('dobryny_side1.png').convert_alpha())
        self.images.append(load_image_data('dobryny_side1_left.png').convert_alpha())
        self.images.append(load_image_data('dobryny_side1_right.png').convert_alpha())
        self.image = dob
        self.rect = self.image.get_rect()
        self.rect.x = 534
        self.rect.y = 160

    def update1(self):
        if pygame.sprite.spritecollideany(self, border1):
            return False
        else:
            return True

    def update2(self):
        if pygame.sprite.spritecollideany(self, border2):
            return False
        else:
            return True

    def update3(self):
        if pygame.sprite.spritecollideany(self, border3):
            return False
        else:
            return True

    def update4(self):
        if pygame.sprite.spritecollideany(self, border4):
            return False
        else:
            return True

    def update5(self):
        if pygame.sprite.spritecollideany(self, border4):
            return False
        else:
            return True

    def update6(self):
        if pygame.sprite.spritecollideany(self, border4):
            return False
        else:
            return True

    def pupa(self):
        for x in range(len(lstx)):
            a = self.rect.x // 32 + 3
            b = self.rect.y // 32 + 4
            if a == lstx[x] + 2 and b == lsty[x] + 3 or a == lstx[x] + 3 and b == lsty[x] + 2 or \
                    a == lstx[x] + 3 and b == lsty[x] + 1:
                self.rect.x += 11

    def pupa2(self):
        for x in range(len(lstx)):
            a = self.rect.x // 32 + 2
            b = self.rect.y // 32 + 3
            if a == lstx[x] and b == lsty[x] or a == lstx[x] + 1 and b == lsty[x] or a == lstx[x] - 1 and b == lsty[x]:
                self.rect.y -= 11

    def pupa3(self):
        for x in range(len(lstx)):
            a = self.rect.x // 32 + 1
            b = self.rect.y // 32 + 1
            if a == lstx[x] and b == lsty[x] or a == lstx[x] - 2 and b == lsty[x] or a == lstx[x] - 1 and b == lsty[x]:
                self.rect.y += 11

    def pupa4(self):
        for x in range(len(lstx)):
            a = self.rect.x // 32 + 1
            b = self.rect.y // 32 + 1
            if a == lstx[x] - 1 and b == lsty[x] or a == lstx[x] - 2 and b == lsty[x] - 1 or \
                    a == lstx[x] - 2 and b == lsty[x] - 2:
                self.rect.x -= 11


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 0
        self.top = 0
        self.cell_size = 32
        self.f = 0

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def on_click(self, pos):
        x, y = pos
        x = (x - self.left) // self.cell_size
        y = (y - self.top) // self.cell_size
        if 0 <= x < self.width and 0 <= y < self.height:
            return x, y

    def random_spawn_trees(self, n):
        for i in range(n):
            x = random.randint(2, 30)
            y = random.randint(9, 17)
            if x in lstx or x + 1 in lstx or x + 2 in lstx or x + 3 in lstx:
                if y in lsty or y + 1 in lsty or y + 2 in lsty or y + 3 in lsty or y + 4 in lsty:
                    continue
            lstx.append(x + 1)
            lsty.append(y + 1)
            self.board[y][x] = 10
            if self.board[y][x] == 10:
                image = load_image_icons('test__tree2.png').convert_alpha()
                tree = pygame.sprite.Sprite(tree_sprites)
                tree.image = image
                tree.rect = tree.image.get_rect()

                tree.rect.x = 32 * (x - 1)
                tree.rect.y = 32 * (y - 1)

    def rerender(self, src):
        phone = load_image_location('test_grass4.png').convert_alpha()
        src.blit(phone, (0, 0))

    def rubit(self):
        self.aa = 0
        self.a = 0
        for i in dobrinya.sprites():
            xd = i.rect.x
            yd = i.rect.y
        b = board.on_click(event.pos)
        x, y = b
        for i in range(len(lstx)):
            for j in range(len(lsty)):
                if x == lstx[i] and y == lsty[j]:
                    if lines[9].strip() == "1":
                        self.f += 1
                        self.aa = i
                        self.a = j
                        break
        if self.f == 6:
            self.f = 0
            for sp in tree_sprites.sprites():
                ix = sp.rect.x // 32 + 1
                iy = sp.rect.y // 32 + 1
                if sp.rect.x == 32 * (x - 1) and sp.rect.y == 32 * (y - 2):
                    if (ix == xd // 32 + 1 or ix == xd // 32 + 2 or ix == xd // 32 + 3 or
                        ix == xd // 32 - 1 or ix == xd // 32 - 2 or ix == xd // 32 - 3 or ix == xd // 32 + 2) \
                            and (iy == yd // 32 or iy == yd // 32 - 1):
                        sp.kill()
                        lstx.remove(ix + 1)
                        lsty.remove(iy + 1)
                        wod = int(lines[2])
                        wod += random.randrange(10, 20)
                        lines[2] = lines[2].replace(lines[2], str(wod) + '\n')
                        with open('a.txt', 'w') as fi:
                            fi.writelines(lines)
                            fi.close()


board = Board(40, 21)
clock = pygame.time.Clock()
a = Hodit()
h = Home()
running = True
board.random_spawn_trees(50)

Border(1, 1, WIDTH - 1, 1, border1)
Border(9, 203, 9, HEIGHT - 3, border2)
Border(3, HEIGHT - 53, WIDTH - 3, HEIGHT - 3, border3)
Border(WIDTH - 9, 143, WIDTH - 9, HEIGHT - 3, border4)
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
                if a.update2():
                    a.pupa()
                    flag1 = True
                    index = 7

            if event.key == pygame.K_s:
                if a.update3():
                    a.pupa2()
                    flag2 = True
                    index = 4

            if event.key == pygame.K_w:
                if a.update1():
                    a.pupa3()
                    flag3 = True
                    index = 1

            if event.key == pygame.K_d:
                if a.update4():
                    a.pupa4()
                    flag4 = True
                    index = 10

            if event.key == pygame.K_e:
                if a.update5():
                    spin = True
                    index = 0

            if event.key == pygame.K_q:
                if a.update6():
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
            board.rubit()
            with open('a.txt', 'r') as f:
                l = f.readlines()
            res_count(screen, l)

    if spin:
        if a.update5():
            a.image = a.images[index]
            dis = pg.image.load('data\\dislike.png')
            dis_rect = dis.get_rect(bottomright=((a.rect.x + 80), (a.rect.y + 15)))
            sc.blit(dis, dis_rect)
            pg.display.update()
            index += 1
            if index >= 12:
                index = 0
    if shiz:
        if a.update6():
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
        if a.update2():
            a.pupa()
            a.rect.x -= 11
        a.image = a.images[index]
        index += 1
        if index >= 9:
            index = 7
    if flag2:
        if a.update3():
            a.pupa2()
            a.rect.y += 11
        a.image = a.images[index]
        index += 1
        if index >= 6:
            index = 4
    if flag3:
        if a.update1():
            a.pupa3()
            a.rect.y -= 11

        a.image = a.images[index]
        index += 1
        if index >= 3:
            index = 1

    if flag4:
        if a.update4():
            a.pupa4()
            a.rect.x += 11
        a.image = a.images[index]
        index += 1
        if index >= 12:
            index = 10
    board.rerender(screen)
    all_sprites.draw(screen)
    tree_sprites.draw(screen)
    dobrinya.draw(screen)
    home.draw(screen)

    res_count(screen, lines)
    if a.rect.x <= 80 and a.rect.y <= 121:
        pygame.quit()
        import main_cave
    elif a.rect.x >= 1230 and a.rect.y <= 121:
        pygame.quit()
        import main_beach
    else:
        clock.tick(30)
        pg.display.update()
