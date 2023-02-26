import pygame

from settings import *
from design import *
from res import res_count

bg = pygame.image.load("locations\\bar_counter.png")
screen.blit(bg, (0, 0))
outputs = [output, output1, output2, output3, output4, output5]
sliders = [slider, slider1, slider2, slider3, slider4, slider5]
colors = [(0, 255, 255), (32, 178, 170), (240, 230, 140), (0, 206, 209), (144, 238, 144), (128, 0, 0)]
font = pygame.font.Font(None, 100)
flags = [0, 0, 0, 0, 0]
playbtn = Button(
    screen, #слой на котором кнопка
    800, # корда х
    500, # корда у
    200, # ширина кнопки
    100, # высота кнопки
    text='Х', # текст кнопки
    textColour=(255, 255, 255), # цвет текста
    fontSize=50, # размер шрифта
    margin=20, # Минимальное расстояние между текстом / изображением и краем.
    inactiveColour=(50, 205, 50), # цвет кнопки
    hoverColour=(152, 251, 152), # цвет кнопки при наведении
    pressedColour=(0, 255, 127), # цвет кнопки при нажатии
    radius=20, # скругление кнопки
    onClick=lambda: shot()) #функция когда кнопка нажата

def generate_random_numbers(n, limit):
    random_numbers = []
    for _ in range(n):
        random_numbers.append(random.randint(0, limit))
    return random_numbers

random_numbers = generate_random_numbers(6, 50)

def shot():
    global random_numbers
    tru = 0
    for i in range(6):
        if sliders[i].getValue() == random_numbers[i]:
            tru += 1
    if tru != 6:
        print(tru)
    elif tru == 6:
        a = int(lines[8]) + 5
        lines[8] = lines[8].replace(lines[8], str(a) + '\n')
        with open('base.txt', 'w') as fi:
            fi.writelines(lines)
            fi.close()
        screen.blit(bg, (0, 0))
        random_numbers = generate_random_numbers(6, 50)


def draw():
    for i in range(len(sliders)):
        if sliders[i].getValue() == random_numbers[i]:
            pygame.draw.rect(screen, colors[i], (20, 540 - 66 * i, 70, 66))
        else:
            pass
            #звук разливайки


def draw_rec():
    pygame.draw.rect(screen, (66,203,29), (20, 206, 70, 402), 5)


running = True
while running:
    events = pygame.event.get()
    for event in pygame.event.get():
        draw_rec()
        if event.type == pygame.QUIT: 
            running = False
        elif event.type == pygame.MOUSEMOTION:
            draw()
        for i in range(len(outputs)):
            outputs[i].setText(sliders[i].getValue())
        for g in range(6):
            text = font.render(str(random_numbers[g]), True, (139, 0, 139))
            screen.blit(text, (900, 90 + 70 * g))
        res_count(screen, lines)
        pygame_widgets.update(events)
        pg.display.update()
        pygame.display.flip()

pygame.quit()