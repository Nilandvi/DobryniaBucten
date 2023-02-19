import pygame_widgets
from zwuk import *
from pygame_widgets.button import Button

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
dobr = pygame.sprite.Group()

class Dobr(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(dobr)
        fofof = pygame.image.load('img\\dobr.png')
        self.image = fofof
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0


w = 0
WIDTH = 600
HEIGHT = 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bg = pygame.image.load("img\\nastroiki1.png")
screen.blit(bg, (0, 0))
clock = pygame.time.Clock()

pygame.display.set_caption('Dobrynia Bucten')
font = pygame.font.SysFont('Montserrat', 40)

display_text = font.render("Громкость Музыки", True, (0, 0, 0))
unicodect = display_text.get_rect(topright=[260, 5])

display_text1 = font.render("|||||", True, (0, 0, 0))
unicodect1 = display_text1.get_rect()
unicodect1.topright = [150, 59]
text1 = pygame.transform.flip(display_text1, True, False)
screen.blit(text1, (70, 59))

display_text2 = font.render("|||||", True, (0, 0, 0))
unicodect2 = display_text2.get_rect()
unicodect2.topright = [150, 150]
text = pygame.transform.flip(display_text2, True, False)

display_text3 = font.render("Громкость Звука", True, (0, 0, 0))
unicodect3 = display_text3.get_rect(topright=[235, 110])

display_text4 = font.render("Рамка вкл/выкл", True, (0, 0, 0))
unicodect4 = display_text4.get_rect(topright=[520, 10])




screen.blit(bg, (0, 0))
screen.blit(display_text, unicodect)
screen.blit(display_text3, unicodect3)


def toggle_frame():
    global screen, w
    if w == 0:
        flags = pygame.NOFRAME
        pygame.display.set_mode((600, 300), flags)
        w = 1
    else:
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        w = 0
    skala()


nobtn = Button(
    screen,  # слой на котором кнопка
    10,  # корда х
    50,  # корда у
    50,  # ширина кнопки
    50,  # высота кнопки
    text='-',  # текст кнопки
    textColour=(0, 0, 0),  # цвет текста
    fontSize=50,  # размер шрифта
    margin=20,  # Минимальное расстояние между текстом / изображением и краем.
    inactiveColour=(255, 165, 0),  # цвет кнопки
    hoverColour=(255, 215, 0),  # цвет кнопки при наведении
    pressedColour=(255, 255, 0),  # цвет кнопки при нажатии
    radius=20,  # скругление кнопки
    onClick=lambda: no()  # функция когда кнопка нажата
)


yesbtn = Button(
    screen,
    160,
    50,
    50,
    50,
    text='+',
    textColour=(0, 0, 0),
    fontSize=50,
    margin=20,
    inactiveColour=(255, 165, 0),
    hoverColour=(255, 215, 0),
    pressedColour=(255, 255, 0),
    radius=20,
    onClick=lambda: yestoex()
)

frame = Button(
    screen,
    300,
    50,
    180,
    50,
    text='[              ]',
    textColour=(0, 0, 0),
    fontSize=50,
    margin=20,
    inactiveColour=(255, 165, 0),
    hoverColour=(255, 215, 0),
    pressedColour=(255, 255, 0),
    radius=20,
    onClick=lambda: toggle_frame()
)


def no():
    global zvukmus
    if zvukmus <= 0:
        zvukmus = 0
    elif zvukmus >= 0:
        pygame.mixer.music.set_volume(zvukmus - 0.1)
        zvukmus -= 0.1
    skala()


def yestoex():
    global zvukmus
    if zvukmus >= 1:
        zvukmus = 1
    elif zvukmus <= 1:
        pygame.mixer.music.set_volume(zvukmus + 0.1)
        zvukmus += 0.1
    skala()


def skala():
    global display_text1
    #print(zvukmus)
    stik = ["*", "|", "||", "|||", "||||", "|||||", "||||||", "|||||||", "||||||||", "|||||||||", "||||||||||"]
    symbol_map = {
        (0, 0.09): stik[0],
        (0.09, 0.19): stik[1],
        (0.19, 0.29): stik[2],
        (0.29, 0.39): stik[3],
        (0.39, 0.49): stik[4],
        (0.49, 0.59): stik[5],
        (0.59, 0.69): stik[6],
        (0.69, 0.79): stik[7],
        (0.79, 0.89): stik[8],
        (0.89, 2.0): stik[9],
    }
    for range_, symbol in symbol_map.items():
        if range_[0] <= zvukmus <= range_[1]:
            display_text1 = font.render(symbol, True, (0, 0, 0))
            break
    unicodect1.topright = [150, 59]

running, moving = True, False
z, y = 0, 0
x_old, y_old, x_new, y_new = 0, 0, 0, 0
dibri = Dobr()
while running:
    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        wake.play()
    if key[pygame.K_a]:
        wake.play()
    if key[pygame.K_s]:
        wake.play()
    if key[pygame.K_d]:
        wake.play()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if z < event.pos[0] < z + 32 and y < event.pos[1] < y + 32:
                moving = True
        if event.type == pygame.MOUSEMOTION:
            if moving:
                x_new, y_new = event.rel
                z, y = x_new, y_new
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                moving = False
        if moving:
            dibri.image = pygame.image.load('img\\dobr2.png')
            dibri.rect.x = pygame.mouse.get_pos()[0]
            dibri.rect.y = pygame.mouse.get_pos()[1]
            z = dibri.rect.x
            y = dibri.rect.y
            pygame.display.update()
            # он пищит
        else:
            dibri.image = pygame.image.load('img\\dobr.png')
            # он больше не пищит
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            moving = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            click.play()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                click.play()


    screen.blit(display_text, unicodect)
    #text = pygame.transform.flip(display_text1, True, False)
    text2 = pygame.transform.flip(display_text2, True, False)
    #screen.blit(text, (70, 59))
    screen.blit(text2, (70, 159))
    screen.blit(display_text3, unicodect3)
    pygame_widgets.update(pygame.event.get())
    pygame.display.flip()
    pygame.display.update()
    screen.blit(bg, (0, 0))
    dobr.draw(screen)
    clock.tick(60)


    clock.tick(60)
    pygame.display.update()