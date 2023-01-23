import pygame_widgets
from zwuk import *

from pygame_widgets.button import Button
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()

w = 0
WIDTH = 600
HEIGHT = 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bg = pygame.image.load("img\\nastroiki1.png")
screen.blit(bg, (0, 0))

pygame.display.set_caption('Dobrynia Bucten')
font = pygame.font.SysFont('Montserrat', 40)

display_text = font.render("Громкость Музыки", True, (0, 0, 0))
unicodect = display_text.get_rect()
unicodect.topright = [260, 5]

display_text3 = font.render("Громкость Звука", True, (0, 0, 0))
unicodect3 = display_text3.get_rect()
unicodect3.topright = [235, 110]

display_text1 = font.render("|||||", True, (0, 0, 0))
unicodect1 = display_text1.get_rect()
unicodect1.topright = [150, 59]
screen.blit(bg, (0, 0))
screen.blit(display_text, unicodect)
screen.blit(display_text3, unicodect3)


text = pygame.transform.flip(display_text1, True, False)
screen.blit(text, (70, 59))

class Border(pygame.sprite.Sprite):
    def __init__(self, x1, y1, x2, y2, name):
        super().__init__()
        if x1 == x2:
            self.add(name)
            self.image = pygame.Surface([1, y2 - y1])
            self.rect = pygame.Rect(x1, y1, 1, y2 - y1)
        else:
            self.add(name)
            self.image = pygame.Surface([x2 - x1, 1])
            self.rect = pygame.Rect(x1, y1, x2 - x1, 1)


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
    global x
    if x <= 0:
        x = 0
    elif x >= 0:
        pygame.mixer.music.set_volume(x - 0.1)
        x -= 0.1
        pygame.mixer.music.get_volume()
    skala()


def yestoex():
    global x
    if x >= 1:
        x = 1
    elif x <= 1:
        pygame.mixer.music.set_volume(x + 0.1)
        x += 0.1
        pygame.mixer.music.get_volume()
    skala()


def skala():
    print(x)
    stik = ["*", "|", "||", "|||", "||||", "|||||", "||||||", "|||||||", "||||||||", "|||||||||", "||||||||||"]
    if x < 0.09:
        print("*")
        display_text1 = font.render(stik[0], True, (0, 0, 0))
    elif x >= 0.1 and x < 0.19:
        display_text1 = font.render(stik[1], True, (0, 0, 0))
    elif x >= 0.1 and x < 0.29:
        display_text1 = font.render(stik[2], True, (0, 0, 0))
    elif x >= 0.2 and x <= 0.39:
        display_text1 = font.render(stik[3], True, (0, 0, 0))
    elif x >= 0.3 and x <= 0.49:
        display_text1 = font.render(stik[4], True, (0, 0, 0))
    elif x >= 0.4 and x <= 0.59:
        display_text1 = font.render(stik[5], True, (0, 0, 0))
    elif x >= 0.5 and x <= 0.69:
        display_text1 = font.render(stik[6], True, (0, 0, 0))
    elif x >= 0.6 and x <= 0.79:
        display_text1 = font.render(stik[7], True, (0, 0, 0))
    elif x >= 0.7 and x <= 0.89:
        display_text1 = font.render(stik[8], True, (0, 0, 0))
    elif x >= 0.8 and x <= 0.99:
        display_text1 = font.render(stik[9], True, (0, 0, 0))
    elif x >= 0.9 and x <= 1.99:
        display_text1 = font.render(stik[10], True, (0, 0, 0))
    unicodect1 = display_text1.get_rect()
    unicodect1.topright = [150, 59]
    screen.blit(bg, (0, 0))
    screen.blit(display_text, unicodect)
    text = pygame.transform.flip(display_text1, True, False)
    screen.blit(text, (70, 59))
    screen.blit(display_text3, unicodect3)



running, moving = True, False
x, y = 0, 0
x_old, y_old, x_new, y_new = 0, 0, 0, 0
while running:
    # key = pygame.key.get_pressed()
    # if key[pygame.K_w]:
    #     wake.play()
    # if key[pygame.K_a]:
    #     wake.play()
    # if key[pygame.K_s]:
    #     wake.play()
    # if key[pygame.K_d]:
    #     wake.play()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if x < event.pos[0] < x + 32 and y < event.pos[1] < y + 32:
                moving = True
        if event.type == pygame.MOUSEMOTION:
            if moving:
                x_new, y_new = event.rel
                x, y = x + x_new, y + y_new
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                moving = False
        if moving == True:
            sun_surf = pygame.image.load('img\\dobr2.png')
            # он пищит
        else:
            sun_surf = pygame.image.load('img\\dobr.png')
            # он больше не пищит
            screen.blit(sun_surf, (x, y, 32, 32))
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            moving = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            click.play()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                click.play()
        screen.blit(sun_surf, (x, y, 32, 32))
        pygame.display.flip()


    pygame_widgets.update(pygame.event.get())
    pygame.display.update()
