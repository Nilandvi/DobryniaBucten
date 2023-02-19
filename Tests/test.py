import pygame
import random
import math

# Инициализация Pygame
pygame.init()

# Константы игры

WIDTH = 1280
HEIGHT = 640
CELL_SIZE = 32
ROW_COUNT = HEIGHT // CELL_SIZE
COLUMN_COUNT = WIDTH // CELL_SIZE
BREAK_DISTANCE = 16
RED_CELL_COUNT = 10
GREEN = (20, 180, 20)
RED = (180, 20, 20)
BLUE = (20, 20, 180)
player_row = ROW_COUNT // 2
player_column = COLUMN_COUNT // 2
player_rect = pygame.Rect(player_column * CELL_SIZE, player_row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
# Создаем игровое окно
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Игра")

# Создаем сетку из клеток
grid = [[GREEN for column in range(COLUMN_COUNT)] for row in range(ROW_COUNT)]

# Генерируем случайные красные клетки
red_cells = []
while len(red_cells) < RED_CELL_COUNT:
    row = random.randint(0, ROW_COUNT - 1)
    column = random.randint(0, COLUMN_COUNT - 1)
    if (row, column) not in red_cells:
        red_cells.append((row, column))
        grid[row][column] = RED

# Создаем персонажа
player_rect = pygame.Rect(player_column * CELL_SIZE, player_row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
player_speed = 5
move_up = False
move_down = False
move_left = False
move_right = False

# Функция для отрисовки игрового поля
def draw_grid():
    for row in range(ROW_COUNT):
        for column in range(COLUMN_COUNT):
            pygame.draw.rect(screen, grid[row][column], (column * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 0)

# Функция для отрисовки персонажа
def draw_player():
    pygame.draw.rect(screen, BLUE, player_rect)

# Функция для обновления окна
def update_window():
    screen.fill((0, 0, 0))
    draw_grid()
    draw_player()
    pygame.display.update()

def handle_key_press(key):
    global player_rect
    global player_row, player_column

    if key == pygame.K_w:
        player_rect.move_ip(0, -CELL_SIZE)
    elif key == pygame.K_a:
        player_rect.move_ip(-CELL_SIZE, 0)
    elif key == pygame.K_s:
        player_rect.move_ip(0, CELL_SIZE)
    elif key == pygame.K_d:
        player_rect.move_ip(CELL_SIZE, 0)


    # Ограничиваем движение персонажа в пределах экрана
    player_row = max(0, min(player_row, ROW_COUNT - 1))
    player_column = max(0, min(player_column, COLUMN_COUNT - 1))

# Главный цикл игры
while True:
    # Обрабатываем события
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            handle_key_press(event.key)

    # Обновляем окно
    update_window()

