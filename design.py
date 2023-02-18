from settings import *
font = pygame.font.Font(None, 50)

slider = Slider(screen, 550, 120, 200, 40, min=0, max=50, step=1)
output = TextBox(screen, 780, 120, 50, 50, fontSize=30)
slider1 = Slider(screen, 550, 190, 200, 40, min=0, max=50, step=1)
output1 = TextBox(screen, 780, 190, 50, 50, fontSize=30)
slider2 = Slider(screen, 550, 260, 200, 40, min=0, max=50, step=1)
output2 = TextBox(screen, 780, 260, 50, 50, fontSize=30)
slider3 = Slider(screen, 550, 330, 200, 40, min=0, max=50, step=1)
output3 = TextBox(screen, 780, 330, 50, 50, fontSize=30)
slider4 = Slider(screen, 550, 400, 200, 40, min=0, max=50, step=1)
output4 = TextBox(screen, 780, 400, 50, 50, fontSize=30)
slider5 = Slider(screen, 550, 470, 200, 40, min=0, max=50, step=1)
output5 = TextBox(screen, 780, 470, 50, 50, fontSize=30)

ex = Button(
    screen, #слой на котором кнопка
    10, # корда х
    10, # корда у
    50, # ширина кнопки
    50, # высота кнопки
    text='Х', # текст кнопки
    textColour=(255, 255, 255), # цвет текста
    fontSize=50, # размер шрифта
    margin=20, # Минимальное расстояние между текстом / изображением и краем.
    inactiveColour=(50, 205, 50), # цвет кнопки
    hoverColour=(152, 251, 152), # цвет кнопки при наведении
    pressedColour=(0, 255, 127), # цвет кнопки при нажатии
    radius=20, # скругление кнопки
    onClick=lambda: retur()) #функция когда кнопка нажата

def retur():
    pygame.quit()



output.disable()