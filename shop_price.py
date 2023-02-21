from settings import *

font_shop = pygame.font.Font(None, 40)
color = (98, 99, 155)


lst =[
    {"name": "oak", "price": "", 'image': pygame.image.load('icons\\oak.png'), 'y': 0},
    {"name": "rock", "price": "", 'image': pygame.image.load('icons\\rock.png'), 'y': 0},
    {"name": "clay", "price": "", 'image': pygame.image.load('icons\\clay.png'), 'y': 0},
    {"name": "coin", "price": "", 'image': pygame.image.load('icons\\coin.png'), 'y': 0},
    {"name": "arrow", "price":"",'image': pygame.image.load('icons\\arrow.png'), 'y': 0},
    {"name": "boost", "price":"", 'image': pygame.image.load('shop\\speed.png'), "aimage": pygame.image.load('shop\\a_speed.png'), 'y': 0},
    {"name": "barup", "price":"", 'image': pygame.image.load('shop\\bar.png'), "aimage": pygame.image.load('shop\\a_bar.png'), 'y': 0}]
#как устаканим экономику дополним