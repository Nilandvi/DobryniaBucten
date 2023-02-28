from settings import *
from load_image import *

def titry():
    pygame.font.init()
    meters = int(lines[30].strip()) // 45
    font = pygame.font.SysFont('Comic Sans MS', 30)
    screen.fill((0, 0, 0))
    pygame.mixer.music.load('sounds\\final.mp3')
    pygame.mixer.music.play(-1)

    messages = [
        "Добрыня. Так много в этом слове...",
        "Все начиналось с детской мечты. Маленькое ведерко захотело обрести свое счастье",
        "Построить бар и стать полностью не зависимым от сових родственников",
        "Добрыня долго шел к своей мечте. И вот наконец, купив билет в отдаленное село",
        "Место, где о циливизации ничего не слыхали, он решил открыть свой маленький бар..",
        f"Постройка давалась далего не легко. За все время Добрыня сломал {lines[20].strip()} объектов",
        f"Среди которых добыл {lines[22].strip()} досок, {lines[24].strip()} камней, {lines[26].strip()} глины!",
        f"Заработал целых {lines[28].strip()} золотых монеток! приготовив {lines[32].strip()} коктейлей!",
        f"За все время прошел аж {str(meters)} метра! Знаете, по меркам ведра, это очень много!",
        "Это огромный подвиг как для ведерка Добрыни, так и для Вас,",
        "что помогли осуществить его мечту!",
        "Спасибо Вам за это, с уважением, команда разработчиков DobryniaBucten!",
        "Это был очень увлекательный опыт, и надеюсь вам понравилась наша игра!",
        "Наша команда:",
        "Nilandvi - разработчик, дизайнер, менеджер, тех. писатель, проектировщик, архитектор",
        "Gui Tomioka - разробатчик, дизайнер, системный аналитик, архитектор",
        "KrostonKD - раработчик, креативщик",
        "Kapibar4 - гейм дизайнер, мотиватор",
        "Интересное вышло приключение. Хорошего дня!"
        "<3"
    ]

    x = 20
    y = 20
    current_message = 0
    end = 0

    while current_message < len(messages):
        message = messages[current_message]
        line = ''
        for char in message:
            # Добавить букву в текущую строку
            new_line = line + char
            line = new_line
            # Отобразить текущую строку на экране
            text_surface = font.render(line, True, (255,255,255))
            screen.blit(text_surface, (x, y))
            pygame.display.update()
            # Задержка перед выводом следующей буквы
            time.sleep(0.05)
        # Перейти на новую строку
        y += font.size(line)[1]
        current_message += 1
        end += 1
        if current_message == 11:
            screen.fill((0,0,0))
            y = 0
        if end == 19:
            screen.blit(load_image_location("end.png"), (0,0))
            pygame.display.update()

        # Ожидание нажатия кнопки мыши, чтобы продолжить вывод текста
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    break
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            else:
                continue
            break


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
