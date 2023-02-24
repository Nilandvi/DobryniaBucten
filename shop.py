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
    
    bars = [(523, 224), (659, 224), (511, 56), (625, 56), (747, 56)]
    table = InfoTable("barup")
    abup = pygame.image.load("shop\\a_bar.png")
    bar = pygame.image.load("shop\\bar.png")

    for bar_pos in bars:
        if bar_pos[0] <= pygame.mouse.get_pos()[0] <= bar_pos[0] + 61 and bar_pos[1] <= pygame.mouse.get_pos()[1] <= bar_pos[1] + 64:
            screen.blit(abup, bar_pos)
            pygame.draw.rect(screen, BLACK, (940, 0, 340, 350))
            table.draw()
        else:
            screen.blit(bar, bar_pos)
    
    pygame.display.update()
    screen.blit(bg, (0, 0))












#(522, 278)
#(744, 278)