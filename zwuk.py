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

zvukmus = 0.5
pygame.mixer.music.load('sounds\\music.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(zvukmus)
wake.set_volume(volumes)
font = pygame.font.SysFont('Montserrat', 40)

display_text2 = font.render("|||||", True, (0, 0, 0))
unicodect2 = display_text2.get_rect()
unicodect2.topright = [150, 150]
text = pygame.transform.flip(display_text2, True, False)



display_text1 = font.render("|||||", True, (0, 0, 0))
unicodect1 = display_text1.get_rect()
unicodect1.topright = [150, 59]
text1 = pygame.transform.flip(display_text1, True, False)
screen.blit(text1, (70, 59))


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
    global display_text2
    print(volumes)
    stik1 = ["*", "|", "||", "|||", "||||", "|||||", "||||||", "|||||||", "||||||||", "|||||||||", "||||||||||"]
    symbol_map1 = {
        (0, 0.09): stik1[0],
        (0.09, 0.19): stik1[1],
        (0.19, 0.29): stik1[2],
        (0.29, 0.39): stik1[3],
        (0.39, 0.49): stik1[4],
        (0.49, 0.59): stik1[5],
        (0.59, 0.69): stik1[6],
        (0.69, 0.79): stik1[7],
        (0.79, 0.89): stik1[8],
        (0.89, 2.0): stik1[9],
    }
    for range1_, symbol1 in symbol_map1.items():
        if range1_[0] <= zvukmus <= range1_[1]:
            display_text2 = font.render(symbol1, True, (0, 0, 0))
            break
    unicodect2.topright = [150, 159]