import pygame

class InfoTable:
    def __init__(self):
        self.width = 340
        self.height = 350
        self.bg_color = (0, 0, 0)
        self.font = pygame.font.SysFont('comicsansms', 40)
        self.font1 = pygame.font.SysFont('comicsansms', 20)
        self.title_text = 'Информация'
        self.info_text = 'Инфа о товаре лооол'
        self.title_color = (0, 255, 127)
        self.info_color = (102, 205, 170)
        self.title_pos = (self.width//2, 20)
        self.info_pos = (self.width//2, 50)
        self.icon_pos = [(50, 100 + i * 45) for i in range(4)]
        self.icon_size = (40, 40)
        self.icons = []
        self.screen = pygame.display.set_mode((self.width, self.height))

    def load_icons(self, icon_files):
        for file in icon_files:
            icon = pygame.image.load(file).convert_alpha()
            icon = pygame.transform.scale(icon, self.icon_size)
            self.icons.append(icon)

    def draw(self):
        self.screen.fill(self.bg_color)
        title = self.font.render(self.title_text, True, self.title_color)
        title_rect = title.get_rect(center=self.title_pos)
        self.screen.blit(title, title_rect)
        info = self.font1.render(self.info_text, True, self.info_color)
        info_rect = info.get_rect(center=self.info_pos)
        self.screen.blit(info, info_rect)
        for i in range(len(self.icons)):
            self.screen.blit(self.icons[i], self.icon_pos[i])
        pygame.display.flip()