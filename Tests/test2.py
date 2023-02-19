import pygame
import random

# Define constants
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 640
CELL_SIZE = 32
CHARACTER_SPEED = 8
MAX_RED_CELLS = 20

# Initialize Pygame
pygame.init()

# Create the game window
game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Define colors
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Define classes

class Character:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, CELL_SIZE, CELL_SIZE)

    def move(self, direction):
        if direction == "UP":
            self.y -= CHARACTER_SPEED
        elif direction == "DOWN":
            self.y += CHARACTER_SPEED
        elif direction == "LEFT":
            self.x -= CHARACTER_SPEED
        elif direction == "RIGHT":
            self.x += CHARACTER_SPEED
        self.rect = pygame.Rect(self.x, self.y, CELL_SIZE, CELL_SIZE)

    def draw(self):
        pygame.draw.rect(game_window, BLUE, self.rect)

class RedCell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, CELL_SIZE, CELL_SIZE)

    def draw(self):
        pygame.draw.rect(game_window, RED, self.rect)

class CellField:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = [[True for _ in range(self.width)] for _ in range(self.height)]
        self.red_cells = []
        self.generate_red_cells()

    def generate_red_cells(self):
        while len(self.red_cells) < MAX_RED_CELLS:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            if self.cells[y][x]:
                self.red_cells.append(RedCell(x * CELL_SIZE, y * CELL_SIZE))
                self.cells[y][x] = False

    def collect_red_cells(self, character_rect):
        count = 0
        for cell in self.red_cells:
            if cell.rect.colliderect(character_rect):
                self.cells[cell.y // CELL_SIZE][cell.x // CELL_SIZE] = True
                self.red_cells.remove(cell)
                self.generate_red_cells()
                count += 1
        return count

    def check_collision(self, rect):
        for y in range(self.height):
            for x in range(self.width):
                if not self.cells[y][x]:
                    cell_rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                    if rect.colliderect(cell_rect):
                        return True
        return False

    def draw(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.cells[y][x]:
                    pygame.draw.rect(game_window, GREEN, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        for cell in self.red_cells:
            cell.draw()

# Create objects
character = Character(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
cell_field = CellField(WINDOW_WIDTH // CELL_SIZE, WINDOW_HEIGHT // CELL_SIZE)

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_w:
                character.move("UP")
            elif event.key == pygame.K_s:
                character.move("DOWN")
            elif event.key == pygame.K_a:
                character.move("LEFT")
            elif event.key == pygame.K_d:
                character.move("RIGHT")
            elif event.key == pygame.K_e:
                character_rect = pygame.Rect(character.x, character.y, CELL_SIZE, CELL_SIZE)
                count = cell_field.collect_red_cells(character_rect)
                print(f"Collected {count} red cells")

    # Move the character
    character_rect = pygame.Rect(character.x, character.y, CELL_SIZE, CELL_SIZE)
    if not cell_field.check_collision(character_rect):
        character.draw()
    else:
        character.move("UP")

    # Draw the cells
    cell_field.draw()
    # Update the screen
    pygame.display.update()

# Quit Pygame
pygame.quit()
