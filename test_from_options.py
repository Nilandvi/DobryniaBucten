import os

import pygame
import pygame_widgets
from pygame_widgets.button import Button
from pygame_widgets.slider import Slider
from settings import *


# инициализируем pygame и создаем окно
pygame.init()

def play():
    print("lol")
    pygame.mixer.music.play()
def pause():
    pygame.mixer.music.pause()
def run_options():
    screen = pygame.display.set_mode((400, 300))
    pygame.display.set_caption("Музыкальный плеер")

    # создаем кнопки для управления громкостью
    font = pygame.font.Font(None, 25)
    volume_text = font.render("Громкость", True, (0, 0, 0))
    volume_rect = volume_text.get_rect(center=(200, 85))

    # создаем слайдер для регулировки громкости
    volume_slider = Slider(screen, 150, 150, 100, 30, min=0, max=10, step=1)

    # загружаем музыкальный файл
    pygame.mixer.music.load("sounds\\ost.mp3")

    # создаем кнопки управления музыкой
    play_button = Button(screen, 100, 250, 75, 25, text="Воспроизвести",
                         fontSize=15, margin=5, onClick=lambda: play())
    pause_button = Button(screen, 225, 250, 75, 25, text="Пауза",
                          fontSize=15, margin=5, onClick=lambda: pause())

    # главный цикл программы
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # обрабатываем события кнопок регулировки громкости
            volume = int(volume_slider.getValue())
            volume_indicator = "|" * volume
            volume_indicator_text = font.render(volume_indicator, True, (0, 0, 0))
            volume_indicator_rect = volume_indicator_text.get_rect(center=(200, 200))
            pygame.mixer.music.set_volume(volume / 10)
            lines[34] = str(volume / 10) + '\n'
            with open('base.txt', 'w') as fi:
                fi.writelines(lines)
                fi.close()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if lines[36] == '4':
                        screen = pygame.display.set_mode((1280, 680))
                        return
                    if lines[36].rstrip() == '1':
                        screen = pygame.display.set_mode((1280, 680))
                        return
                    if lines[36] == '2':
                        screen = pygame.display.set_mode((1280, 680))
                        return
                    if lines[36] == '3':
                        screen = pygame.display.set_mode((1280, 680))
                        return

            # прослушиваем события для каждой кнопки
            play_button.listen(event)
            pause_button.listen(event)

        events = pygame.event.get()
        screen.fill((255, 255, 255))
        pygame_widgets.update(events)
        # отрисовываем элементы управления
        screen.blit(volume_text, volume_rect)
        screen.blit(volume_indicator_text, volume_indicator_rect)
        volume_slider.draw()
        play_button.draw()
        pause_button.draw()

        pygame.display.update()
        pygame.time.delay(10)
