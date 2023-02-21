from settings import *

def res_count(screen, file):
    resources = [
        {'image': pygame.image.load('icons\\oak.png'), 'x': 0},
        {'image': pygame.image.load('icons\\rock.png'), 'x': 100},
        {'image': pygame.image.load('icons\\clay.png'), 'x': 200},
        {'image': pygame.image.load('icons\\coin.png'), 'x': 300},
    ]
    font = pygame.font.Font(None, 40)
    color = (98, 99, 155)
    for i, resource in enumerate(resources):
        screen.blit(resource['image'], (resource['x'], 0))
        text = font.render(file[2 * i + 2].strip(), True, color)
        screen.blit(text, (35 + i * 100, 5))
