#coding: utf-8

import pygame

class MainCharacter(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()
        self.image = pygame.image.load("data/MacGyver2.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def moveRight(self, pixels):
        self.rect.x += pixels

    def moveLeft(self, pixels):
        self.rect.x -= pixels

    def moveUp(self, pixels):
        self.rect.y -= pixels

    def moveDown(self, pixels):
        self.rect.y += pixels

class Background(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()
        self.image = pygame.image.load("data/fond.jpg").convert()
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0        



