import pygame
from shop import InfoTable

pygame.init()

table = InfoTable()
table.load_icons(['C:\\Users\\Nilandvi\\OneDrive\\Документы\\GitHub\\DobryniaBucten\\icons\\oak.png', 'C:\\Users\\Nilandvi\\OneDrive\\Документы\\GitHub\\DobryniaBucten\\icons\\rock.png',
 'C:\\Users\\Nilandvi\\OneDrive\\Документы\\GitHub\\DobryniaBucten\\icons\\clay.png', 'C:\\Users\\Nilandvi\\OneDrive\\Документы\\GitHub\\DobryniaBucten\\icons\\coin.png'])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    table.draw()