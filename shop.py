import os

from settings import *
from res import *
from shopinfotable import InfoTable
from shop_price import *
from load_image import *
from tranzaction import *


# Определение цветов
def run_shop():
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
    s2 = pygame.mixer.Sound('sounds\\cash.ogg')
    s3 = pygame.mixer.Sound('sounds\\error.ogg')
    while messages:
        for event in pygame.event.get():
            pass
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
        time.sleep(1)
    # Основной игровой цикл
    pygame.mixer.music.load('sounds\\shop.mp3')
    pygame.mixer.music.play(-1)
    while True:
        res_count(screen, lines)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                if 523 <= pygame.mouse.get_pos()[0] <= 584 and 150 <= pygame.mouse.get_pos()[1] <= 214:
                    if lines[14][0] == "1":
                        tranz("barup_lvl1")
                        s2.play()
                    elif lines[14][0] == "2":
                        tranz("barup_lvl2")
                        s2.play()
                    elif lines[14][0] == "3":
                        tranz("barup_lvl3")
                        s2.play()
                    elif lines[14][0] == "4":
                        s3.play()
                if 659 <= pygame.mouse.get_pos()[0] <= 724 and 150 <= pygame.mouse.get_pos()[1] <= 214:
                    if lines[16][0] == "0":
                        tranz("boost")
                        s2.play()
                    else:
                        s3.play()
                if 511 <= pygame.mouse.get_pos()[0] <= 575 and 56 <= pygame.mouse.get_pos()[1] <= 120:
                    tranz("wood")
                    if int(lines[2].strip()) >= 100:
                        s2.play()
                    else:
                        s3.play()
                if 625 <= pygame.mouse.get_pos()[0] <= 689 and 56 <= pygame.mouse.get_pos()[1] <= 120:
                    tranz("stone")
                    if int(lines[4].strip()) >= 100:
                        s2.play()
                    else:
                        s3.play()
                if 747 <= pygame.mouse.get_pos()[0] <= 811 and 56 <= pygame.mouse.get_pos()[1] <= 120:
                    tranz("clay")
                    if int(lines[6].strip()) >= 100:
                        s2.play()
                    else:
                        s3.play()
                if 523 <= pygame.mouse.get_pos()[0] <= 587 and 250 <= pygame.mouse.get_pos()[1] <= 314:
                    tranz("fruit")
                    if int(lines[40].strip()) >= 100:
                        s2.play()
                    else:
                        s3.play()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 1005 <= x <= 1045 and 101 <= y <= 135:
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load('sounds\\ost1.mp3')
                    pygame.mixer.music.play(-1)
                    return

        if lines[14][0] == "1":
            screen.blit(pygame.transform.scale(pygame.image.load('shop\\bar1.png'), (64, 64)), (523, 150))
        if lines[14][0] == "2":
            screen.blit(pygame.transform.scale(pygame.image.load('shop\\bar2.png'), (64, 64)), (523, 150))
        if lines[14][0] == "3":
            screen.blit(pygame.transform.scale(pygame.image.load('shop\\bar3.png'), (64, 64)), (523, 150))
        if lines[14][0] == "4":
            screen.blit(pygame.transform.scale(pygame.image.load('shop\\bar4.png'), (64, 64)), (523, 150))
        screen.blit(pygame.transform.scale(pygame.image.load('shop\\speed.png'), (64, 64)), (659, 150))
        screen.blit(pygame.transform.scale(pygame.image.load('shop\\oak.png'), (64, 64)), (511, 56))
        screen.blit(pygame.transform.scale(pygame.image.load('shop\\rock.png'), (64, 64)), (625, 56))
        screen.blit(pygame.transform.scale(pygame.image.load('shop\\clay.png'), (64, 64)), (747, 56))
        screen.blit(pygame.transform.scale(pygame.image.load('shop\\resour.png'), (64, 64)), (523, 250))
        bbar = "barup_lvl" + lines[14][0]
        abbar = "shop\\a_bar" + lines[14][0] + ".png"
        regions = [(523, 150, bbar, abbar), (659, 150, 'boost', 'shop\\a_speed.png'), (511, 48, 'wood', 'shop\\a_oak.png'), (625, 56, 'stone', 'shop\\a_rock.png'), (747, 56, 'clay', 'shop\\a_clay.png'), (523, 250, 'fruit', 'shop\\a_resour.png')]

        for region in regions:
            x, y, table_type, image_path = region
            if x <= pygame.mouse.get_pos()[0] <= x + 61 and y <= pygame.mouse.get_pos()[1] <= y + 64:
                table = InfoTable(table_type)
                abup = pygame.transform.scale(pygame.image.load(image_path), (64, 64))
                screen.blit(abup, (x, y))
                pygame.draw.rect(screen, (205, 133, 63), (940, 0, 340, 350))
                pygame.draw.rect(screen, (210, 105, 30), (940, 0, 340, 350), 5)
                table.draw()


        pygame.display.update()
        screen.blit(bg, (0, 0))