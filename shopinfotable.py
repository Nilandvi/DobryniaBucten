from settings import *
from shop_price import *


class InfoTable:
    def __init__(self, name):
        self.screen = (340, 350)
        self.bg_color = (0, 0, 0)
        self.title_font = pygame.font.SysFont('comicsansms', 40)
        self.info_font = pygame.font.SysFont('comicsansms', 20)
        self.title_text = 'Информация'
        self.title_color, self.info_color, self.price_color = (0, 255, 127), (102, 205, 170), (0, 139, 139)
        self.true_color, self.wrong_color = (0, 255, 0), (255, 0, 0)
        self.title_pos, self.info_pos = (1110, 20), (1110, 50)
        self.icon_pos = [(950, 70 + i * 45) for i in range(4)]
        self.price_pos = [(1050, 90 + i * 45) for i in range(4)]
        self.icon_size = (40, 40)
        self.icons = [
        pygame.transform.scale(pygame.image.load('icons\\oak.png'), self.icon_size), 
        pygame.transform.scale(pygame.image.load('icons\\rock.png'), self.icon_size), 
        pygame.transform.scale(pygame.image.load('icons\\clay.png'), self.icon_size), 
        pygame.transform.scale(pygame.image.load('icons\\coin.png'), self.icon_size)]
        self.arrow = pygame.transform.scale(pygame.image.load('icons\\arrow.png'), self.icon_size)
        item = next((item for item in lst if item["name"] == name), None)
        if item is not None:
            self.boost = lines[16]
            self.flag = 0
            self.result = item["result"]
            self.info_text = item["description"]
            self.count = item["count"]
            self.prices = [
                self.title_font.render(str(item["price"][0]), True, self.price_color),
                self.title_font.render(str(item["price"][1]), True, self.price_color),
                self.title_font.render(str(item["price"][2]), True, self.price_color),
                self.title_font.render(str(item["price"][3]), True, self.price_color),
            ]
            
            if int(lines[2]) >= item["price"][0] and int(lines[4]) >= item["price"][1] and int(lines[6]) >= item["price"][2] and  int(lines[8]) >= item["price"][3]:
                self.flag = 1
        else:
            self.info_text = "No information available for this item."

    
    def draw(self):
        title = self.title_font.render(self.title_text, True, self.title_color)
        title_rect = title.get_rect(center=self.title_pos)
        screen.blit(title, title_rect)

        info = self.info_font.render(self.info_text, True, self.info_color)
        info_rect = info.get_rect(center=self.info_pos)
        screen.blit(info, info_rect)
        screen.blit(self.arrow, (1130, 150))
        screen.blit(self.result, (1200, 120))
        screen.blit(self.title_font.render(self.count, True, self.title_color), (1232, 180))
        if self.flag == 1:
            if lines[16] == "1":
                screen.blit(self.title_font.render("Куплено", True, self.true_color), (980, 250))
            else:
                screen.blit(self.title_font.render("V Доступно", True, self.true_color), (980, 250))
        else:
            if lines[16] == "1":
                screen.blit(self.title_font.render("Куплено", True, self.true_color), (980, 250))
            else:
                screen.blit(self.title_font.render("X Недоступно", True, self.wrong_color), (980, 250))
        for i in range(len(self.icons)):
            rect = self.prices[i].get_rect(center=self.price_pos[i])
            screen.blit(self.prices[i], rect)
            screen.blit(self.icons[i], self.icon_pos[i])
        pygame.display.flip()
        pygame.display.update()