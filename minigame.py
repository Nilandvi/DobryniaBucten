import pygame
from settings import *
from design import *
from res import res_count




def generate_random_numbers(n, limit):
    random_numbers = []
    for _ in range(n):
        random_numbers.append(random.randint(0, limit))
    return random_numbers


def draw():
    global colors
    for i in range(len(sliders)):
        if sliders[i].getValue() == random_numbers[i]:
            pygame.draw.rect(screen, colors[i], (20, 540 - 66 * i, 70, 66))
        else:
            pass
    pygame.draw.rect(screen, (66,203,29), (20, 206, 70, 402), 5)        #звук разливайки

def shot():
    global random_numbers
    tru = 0
    for i in range(6):
        if sliders[i].getValue() == random_numbers[i]:
            tru += 1
    if tru == 6:
        if int(lines[40]) >= 40:
            lines[40] = lines[40].replace(lines[40], str(int(lines[40]) - 40) + '\n')
            a = int(lines[8]) + 5
            lines[8] = lines[8].replace(lines[8], str(a) + '\n')
            with open('base.txt', 'w') as fi:
                fi.writelines(lines)
                fi.close()
            screen.blit(bg, (0, 0))
            random_numbers = generate_random_numbers(6, 50)
            #Звук успеха
        else:
            pass #звук не тру
    else:
        pass #звук отсутствия достаточного кол-ва ресов


def run_minigame():
    global outputs, sliders, colors, bg, random_numbers
    random_numbers = generate_random_numbers(6, 50)
    outputs = [output, output1, output2, output3, output4, output5]
    sliders = [slider, slider1, slider2, slider3, slider4, slider5]
    colors = [(0, 255, 255), (32, 178, 170), (240, 230, 140), (0, 206, 209), (144, 238, 144), (128, 0, 0)]
    bg = pygame.image.load("locations\\bar_counter.png")
    screen.blit(bg, (0, 0))
    font = pygame.font.Font(None, 100)
    flags = [0, 0, 0, 0, 0]
    playbtn = Button(
        screen, 850,530,200,60, text='Налить',textColour=(255, 255, 255),fontSize=50,margin=20,
        inactiveColour=(50, 205, 50),hoverColour=(152, 251, 152), pressedColour=(0, 255, 127),
        radius=20,onClick=lambda: shot())
    fl = 0
    running = True
    while running:
        events = pygame.event.get()
        for event in pygame.event.get():
            draw()

            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEMOTION:
                draw()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 50 <= x <= 90 and 45 <= y <= 80:
                    fl += 1


            for i in range(len(outputs)):
                outputs[i].setText(sliders[i].getValue())
            for g in range(6):
                text = font.render(str(random_numbers[g]), True, (139, 0, 139))
                screen.blit(text, (900, 90 + 70 * g))
            res_count(screen, lines)
            pygame_widgets.update(events)
            pg.display.update()
            pygame.display.flip()
            screen.blit(bg, (0, 0))
        if fl:
            break
    if fl:
        pygame.mixer.music.load('sounds\\ost.mp3')
        pygame.mixer.music.play(-1)
        return