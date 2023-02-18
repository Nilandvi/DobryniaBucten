import pygame
import pygame_widgets
from pygame_widgets.button import Button
from pygame_widgets.slider import Slider


# инициализируем pygame и создаем окно
pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Музыкальный плеер")

# создаем кнопки для управления громкостью
font = pygame.font.Font(None, 25)
volume_text = font.render("Громкость", True, (0, 0, 0))
volume_rect = volume_text.get_rect(center=(200, 85))

# создаем слайдер для регулировки громкости
volume_slider = Slider(screen, 150, 150, 100, 30, min=0, max=10, step=1)

# загружаем музыкальный файл
pygame.mixer.music.load("music.ogg")

# создаем кнопки управления музыкой
play_button = Button(screen, 100, 250, 75, 25, text="Воспроизвести",
                     fontSize=15, margin=5, onClick=lambda: play())
pause_button = Button(screen, 225, 250, 75, 25, text="Пауза",
                      fontSize=15, margin=5, onClick=lambda: pause())

def play():
    print("lol")
    pygame.mixer.music.play()
def pause():
    pygame.mixer.music.pause()

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
