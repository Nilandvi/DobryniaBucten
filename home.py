import pygame
import pygame as pg
import sys
import os
import random
from pygame.locals import *
import time
from load_image import load_image

pygame.init()
home = pygame.sprite.Group()


class Home(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(home)
        dob = load_image('test_home1.png').convert_alpha()
        self.images = []
        self.image = dob
        self.rect = self.image.get_rect()
        self.rect.x = 352
        self.rect.y = 1
