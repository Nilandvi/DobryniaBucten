import pygame
import sys
from pygame.locals import *
import pygame_widgets
from pygame_widgets.button import Button

pygame.init()
WIDTH = 1280
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bg = pygame.image.load("img\\menu.png")
screen.blit(bg, (0, 0))
pygame.display.set_caption('Dobrynia Bucten')

playbtn = Button(
    screen, #слой на котором кнопка
    100, # корда х
    200, # корда у
    500, # ширина кнопки
    100, # высота кнопки
    text='Играть', # текст кнопки
    textColour=(255, 255, 255), # цвет текста
    fontSize=50, # размер шрифта
    margin=20, # Минимальное расстояние между текстом / изображением и краем.
    inactiveColour=(255, 165, 0), # цвет кнопки
    hoverColour=(255, 215, 0), # цвет кнопки при наведении
    pressedColour=(255, 255, 0), # цвет кнопки при нажатии
    radius=20, # скругление кнопки
    onClick=lambda: print('Нажата кнопка играть') #функция когда кнопка нажата
)

settingsbtn = Button(
    screen,
    100,
    350,
    500,
    100,
    text='Настройки',
    textColour=(255, 255, 255),
    fontSize=50,
    margin=20,
    inactiveColour=(255, 165, 0),
    hoverColour=(255, 215, 0),
    pressedColour=(255, 255, 0),
    radius=20,
    onClick=lambda: print('Нажата кнопка настройки')
)

exitbtn = Button(
    screen,
    100,
    500,
    500,
    100,
    text='Выход',
    textColour=(255, 255, 255),
    fontSize=50,
    margin=20,
    inactiveColour=(255, 165, 0),
    hoverColour=(255, 215, 0),
    pressedColour=(255, 255, 0),
    radius=20,
    onClick=lambda: exitt()
)

def exitt():
    print("Нажата кнопка выхода")
    exitbtn.hide()
    settingsbtn.hide()
    playbtn.hide()
    import exapp
    quit()

running = True
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
            exit()
    pygame_widgets.update(events)
    pygame.display.update()
    pygame.display.flip()