import pygame
from pygame_widgets.button import Button
WIDTH = 600
HEIGHT = 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()

volumes = 0.5
musics = ["sche.wav", "dwij.wav"]
click = pygame.mixer.Sound(musics[0])
wake = pygame.mixer.Sound(musics[1])

x = 0.5
pygame.mixer.music.load('F:\PyCharm Community Edition 2021.3.2\pythonProject3\DobryniaBucten-main\data\music.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(x)
wake.set_volume(volumes)
font = pygame.font.SysFont('Montserrat', 40)

display_text2 = font.render("|||||", True, (0, 0, 0))
unicodect2 = display_text2.get_rect()
unicodect2.topright = [150, 150]


valm2 = Button(
    screen,  # слой на котором кнопка
    10,  # корда х
    150,  # корда у
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
    onClick=lambda: valusmin()  # функция когда кнопка нажата
)


valp2 = Button(
    screen,
    160,
    150,
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
    onClick=lambda: valusplu()
)


def valusmin():
    global volumes
    if volumes <= 0:
        volumes = 0
        click.set_volume(volumes)
        wake.set_volume(volumes)
    elif volumes >= 0:
        click.set_volume(volumes - 0.1)
        wake.set_volume(volumes - 0.1)
        volumes -= 0.1
    skalas()


def valusplu():
    global volumes
    if volumes >= 1:
        volumes = 1
        click.set_volume(volumes)
        wake.set_volume(volumes)
    elif volumes <= 1:
        click.set_volume(volumes + 0.1)
        wake.set_volume(volumes + 0.1)
        volumes += 0.1
    skalas()


def skalas():
    print(volumes)
    stik = ["*", "|", "||", "|||", "||||", "|||||", "||||||", "|||||||", "||||||||", "|||||||||", "||||||||||"]
    if volumes < 0.09:
        print("*")
        display_text2 = font.render(stik[0], True, (0, 0, 0))
    elif volumes >= 0.1 and volumes < 0.19:
        display_text2 = font.render(stik[1], True, (0, 0, 0))
    elif volumes >= 0.1 and volumes < 0.29:
        display_text2 = font.render(stik[2], True, (0, 0, 0))
    elif volumes >= 0.2 and volumes <= 0.39:
        display_text2 = font.render(stik[3], True, (0, 0, 0))
    elif volumes >= 0.3 and volumes <= 0.49:
        display_text2 = font.render(stik[4], True, (0, 0, 0))
    elif volumes >= 0.4 and volumes <= 0.59:
        display_text2 = font.render(stik[5], True, (0, 0, 0))
    elif volumes >= 0.5 and volumes <= 0.69:
        display_text2 = font.render(stik[6], True, (0, 0, 0))
    elif volumes >= 0.6 and volumes <= 0.79:
        display_text2 = font.render(stik[7], True, (0, 0, 0))
    elif volumes >= 0.7 and volumes <= 0.89:
        display_text2 = font.render(stik[8], True, (0, 0, 0))
    elif volumes >= 0.8 and volumes <= 0.99:
        display_text2 = font.render(stik[9], True, (0, 0, 0))
    elif volumes >= 0.9 and volumes <= 1.99:
        display_text2 = font.render(stik[10], True, (0, 0, 0))
    unicodect2 = display_text2.get_rect()
    unicodect2.topright = [150, 59]
    screen.blit(display_text2, unicodect2)
    text = pygame.transform.flip(display_text2, True, False)
    screen.blit(text, (70, 59))
