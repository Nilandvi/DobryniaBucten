import pygame
import pygame as pg
import sys
import os
import random
from pygame.locals import *
import time
from load_image_loc import load_image

pygame.init()
buttn = pygame.sprite.Group()


class Buttn(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(buttn)
        dob = load_image('wall-e.png').convert_alpha()
        self.images = []
        self.image = dob
        self.rect = self.image.get_rect()
        self.rect.x = 1280 - 80
        self.rect.y = 680 - 121
