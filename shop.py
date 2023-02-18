from settings import *


# Определение цветов
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
bg = pygame.image.load("img\\menu.png")
screen.blit(bg, (0, 0))
pygame.draw.rect(screen, BLACK, (0, 490, 800, 680))
# Настройка шрифта
font = pygame.font.SysFont('Comic Sans MS', 30)
pygame.mixer.music.load("voice_sans.mp3")
# Определение текста и его позиций
messages = [
    "Добро пожаловать в Bucten shop!",
    "У тебя на счету нихуя денег!",
    "Желаешь что нибудь Продать, а может прикупить?",
]
x = 20
y = 500

# Основной игровой цикл
while True:
    # Проверка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONUP:
            # Если пользователь кликнул мышкой, вывести следующую строку
            if messages:
                message = messages.pop(0)
                text_surface = font.render(message, True, WHITE)
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

    # Ожидание короткого времени перед проверкой событий снова
    time.sleep(0.05)
    
