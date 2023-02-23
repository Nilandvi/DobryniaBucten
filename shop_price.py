from settings import *

font_shop = pygame.font.Font(None, 40)
color = (98, 99, 155)


lst = [
    {"name": "oak", "price": "", 'image': pygame.image.load('icons\\oak.png')},
    {"name": "rock", "price": "", 'image': pygame.image.load('icons\\rock.png')},
    {"name": "clay", "price": "", 'image': pygame.image.load('icons\\clay.png')},
    {"name": "coin", "price": "", 'image': pygame.image.load('icons\\coin.png')},
    {"name": "arrow", "price":"",'image': pygame.image.load('icons\\arrow.png')},
    {"name": "boost", "price":"", 'image': pygame.image.load('shop\\speed.png'), "aimage": pygame.image.load('shop\\a_speed.png'), 'y': 0},
    {"name": "barup", "description": "Почему бы не повысить доходы?", "price": [300, 1000, 100, 20], 'image': pygame.image.load('shop\\bar.png'), 
 "aimage": pygame.image.load('shop\\a_bar.png'), "result": pygame.image.load('shop\\bar.png'), "count": "1"}
]
