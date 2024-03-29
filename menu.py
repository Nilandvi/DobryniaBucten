import pygame

from settings import *
from Options_7_version import run_opt

bg = pygame.image.load("img\\menu.png")
screen = pygame.display.set_mode((1280, 680))
screen.blit(bg, (0, 0))
pygame.display.set_caption('Dobrynia Bucten')
s = pygame.mixer.Sound('sounds\\sche.wav')

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
    onClick=lambda: playa() #функция когда кнопка нажата
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
    onClick=lambda: running_opt()
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
    s.play()
    exitbtn.hide()
    settingsbtn.hide()
    playbtn.hide()
    pygame.mixer.music.stop()
    import exapp
    quit()

def playa():
    s.play()
    exitbtn.hide()
    settingsbtn.hide()
    playbtn.hide()
    import start
    quit()

def running_opt():
    s.play()
    exitbtn.hide()
    settingsbtn.hide()
    playbtn.hide()
    pygame.mixer.music.stop()
    run_opt()
    quit()

class Eye:
    def __init__(self, pos, r):
        self.pos = pos
        self.pos2 = pos
        self.length = int(r * 0.6)
        self.r = r

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.pos, (self.r + 5), 0)
        pygame.draw.circle(screen, (30, 144, 255), self.pos2, 22, 0)
        pygame.draw.circle(screen, (0, 0, 0), self.pos2, self.r // 3.3, 0)

    def update(self, mouse_pos):
        x1, y1 = self.pos
        x2, y2 = mouse_pos
        dx,dy = x2-x1,y2-y1
        rads = math.atan2(dx, dy)
        degs = math.degrees(rads)
        self.pos2 = (x1 + self.length*math.cos((-degs + 90) * 3.14 / 180 ),
                     y1 + self.length*math.sin((-degs + 90) * 3.14 / 180))


eye_lst = []
eye_lst.append(Eye((923, 540), 45))
eye_lst.append(Eye((1081, 540), 45))
pygame.mixer.music.load('sounds\\load.mp3')
pygame.mixer.music.play(-1)

running = True
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
            exit()
        elif event.type == pygame.MOUSEBUTTONUP:
            pass
        elif event.type == pygame.MOUSEMOTION:
            for i in eye_lst:
                i.update(event.pos)

    ##################################
    for i in eye_lst:
        i.draw(screen)

    pygame_widgets.update(events)
    pygame.display.update()
    pygame.display.flip()

pygame.quit()