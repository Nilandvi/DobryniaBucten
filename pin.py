from settings import *
from load_image import *
from titr import titry

btns = [load_image_safe("1.png"), load_image_safe("2.png"), load_image_safe("3.png"), load_image_safe("4.png"),
        load_image_safe("5.png"), load_image_safe("6.png"), load_image_safe("7.png"), load_image_safe("8.png"),
        load_image_safe("9.png"), load_image_safe("del.png"), load_image_safe("0.png"), load_image_safe("enter.png")]
btnsa = [load_image_safe("1a.png"), load_image_safe("2a.png"), load_image_safe("3a.png"), load_image_safe("4a.png"),
         load_image_safe("5a.png"), load_image_safe("6a.png"), load_image_safe("7a.png"), load_image_safe("8a.png"),
         load_image_safe("9a.png"), load_image_safe("dela.png"), load_image_safe("0a.png"),
         load_image_safe("entera.png")]

button_positions = [(20, 100), (140, 100), (260, 100), (20, 220), (140, 220), (260, 220), (20, 340), (140, 340),
                    (260, 340), (20, 460), (140, 460), (260, 460)]

def drawing():
    screen.fill((250, 128, 114))
    screen.blit(pygame.transform.scale(load_image_safe("shifer.png"), (880, 460)), (400,0))
    pygame.draw.rect(screen, (205, 92, 92), (0, 0, 400, 680), 15)

    for i, pos in enumerate(button_positions):
        screen.blit(btns[i], pos)

def rurun():
    textbox = TextBox(screen, 100, 20, 200, 50, fontSize=40, borderColour=(70, 130, 180), textColour=(64, 224, 208), radius=10,)
    textbox.disable()

    drawing()

    password = ""


    button_digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "del", "0", "Enter"]

    # Loop for handling events
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONUP:
                # Check which button was clicked
                for i, pos in enumerate(button_positions):
                    if pos[0] <= pygame.mouse.get_pos()[0] <= pos[0] + 100 and pos[1] <= pygame.mouse.get_pos()[1] <= pos[1] + 100:
                        # If the button is the "Enter" button, check the password
                        if button_digits[i] == "Enter":
                            if password == "9056":
                                password = ""
                                print("Пароль верный, теперь напиши переход на катсцену")
                                #звук хороший
                                titry()
                                return

                            else:
                                password = ""
                                #звук ошибки
                                drawing()
                        if button_digits[i] == "del":
                            password = ""
                            drawing()
                        else:
                            screen.blit(btnsa[i], pos)
                            password += button_digits[i]
        if len(password) == 5:
            password = ""
            drawing()

        textbox.setText(password)
        pygame_widgets.update(pygame.event.get())
        pygame.display.update()
