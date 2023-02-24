from settings import *
from res import *
from shopinfotable import InfoTable
from load_image import *

# Определение цветов
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
bg = pygame.image.load("locations\\shop.png")


screen.blit(bg, (0, 0))
pygame.draw.rect(screen, BLACK, (0, 490, 800, 680))
# Настройка шрифта
font = pygame.font.SysFont('Comic Sans MS', 30)
pygame.mixer.music.load("sounds\\voice_sans.mp3")
# Определение текста и его позиций
messages = [
    "Добро пожаловать в Bucten shop!",
    f"У тебя на счету {lines[8].strip()} монеток!",
    "Желаешь что нибудь Продать, а может прикупить?",
]
x = 20
y = 500

while messages:
    message = messages.pop(0)
    line = ''
    for char in message:
        # Добавить букву в текущую строку
        new_line = line + char
        line = new_line
        # Отобразить текущую строку на экране
        text_surface = font.render(line, True, WHITE)
        screen.blit(text_surface, (x, y))
        pygame.display.update()
        if char != " ":
            pygame.mixer.music.play()
        # Задержка перед выводом следующей буквы
        time.sleep(0.05)
    # Перейти на новую строку
    y += font.size(line)[1]
    pygame.display.update()
    time.sleep(0.01)

# Основной игровой цикл
while True:
    res_count(screen, lines)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONUP:
            print(pygame.mouse.get_pos())
        #elif event.type == pygame.MOUSEMOTION:
    
    screen.blit(pygame.transform.scale(pygame.image.load('shop\\bar.png'), (64, 64)), (523, 224))
    screen.blit(pygame.transform.scale(pygame.image.load('shop\\speed.png'), (64, 64)), (659, 224))
    screen.blit(pygame.transform.scale(pygame.image.load('shop\\oak.png'), (64, 64)), (511, 65))
    screen.blit(pygame.transform.scale(pygame.image.load('shop\\rock.png'), (64, 64)), (625, 56))
    screen.blit(pygame.transform.scale(pygame.image.load('shop\\clay.png'), (64, 64)), (747, 56))
    
    if 523 <= pygame.mouse.get_pos()[0] <= 584 and 224 <= pygame.mouse.get_pos()[1] <= 288:
        table = InfoTable("barup")
        abup = pygame.transform.scale(pygame.image.load('shop\\a_bar.png'), (64, 64))
        screen.blit(abup, (523, 224))
        pygame.draw.rect(screen, (	205, 133, 63), (940, 0, 340, 350))
        pygame.draw.rect(screen, (210, 105, 30), (940, 0, 340, 350), 5)
        table.draw()
    if 659 <= pygame.mouse.get_pos()[0] <= 724 and 224 <= pygame.mouse.get_pos()[1] <= 288:
        table = InfoTable("boost")
        abup = pygame.transform.scale(pygame.image.load('shop\\a_speed.png'), (64, 64))
        screen.blit(abup, (659, 224))
        pygame.draw.rect(screen, (	205, 133, 63), (940, 0, 340, 350))
        pygame.draw.rect(screen, (210, 105, 30), (940, 0, 340, 350), 5)
        table.draw()
    if 511 <= pygame.mouse.get_pos()[0] <= 575 and 56 <= pygame.mouse.get_pos()[1] <= 120:
        table = InfoTable("wood")
        abup = pygame.transform.scale(pygame.image.load('shop\\a_oak.png'), (64, 64))
        screen.blit(abup, (511, 57))
        pygame.draw.rect(screen, (	205, 133, 63), (940, 0, 340, 350))
        pygame.draw.rect(screen, (210, 105, 30), (940, 0, 340, 350), 5)
        table.draw()    
    if 625 <= pygame.mouse.get_pos()[0] <= 689 and 56 <= pygame.mouse.get_pos()[1] <= 120:
        table = InfoTable("stone")
        abup = pygame.transform.scale(pygame.image.load('shop\\a_rock.png'), (64, 64))
        screen.blit(abup, (625, 56))
        pygame.draw.rect(screen, (	205, 133, 63), (940, 0, 340, 350))
        pygame.draw.rect(screen, (210, 105, 30), (940, 0, 340, 350), 5)
        table.draw()
    if 747 <= pygame.mouse.get_pos()[0] <= 811 and 56 <= pygame.mouse.get_pos()[1] <= 120:
        table = InfoTable("clay")
        abup = pygame.transform.scale(pygame.image.load('shop\\a_clay.png'), (64, 64))
        screen.blit(abup, (747, 56))
        pygame.draw.rect(screen, (	205, 133, 63), (940, 0, 340, 350))
        pygame.draw.rect(screen, (210, 105, 30), (940, 0, 340, 350), 5)
        table.draw()

    pygame.display.update()
    screen.blit(bg, (0, 0))












#(522, 278)
#(744, 278)