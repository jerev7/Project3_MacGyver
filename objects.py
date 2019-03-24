#coding: utf-8

import pygame


class MainCharacter(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()
        
        #chargement_image = pygame.image.load("data/MacGyver2.png").convert_alpha()
        #cheveux_macGyver = chargement_image.subsurface(pygame.Rect(0, 0, 10, 10))
        #self.image = pygame.transform.scale(cheveux_macGyver, (30, 30))

        chargement_image = pygame.image.load("data/MacGyver.png").convert_alpha()
        self.image = pygame.transform.scale(chargement_image, (30, 30))
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
        chargement_image = pygame.image.load("data/map.png").convert()
        self.image = pygame.transform.scale(chargement_image, (450, 450))


       # self.image = pygame.image.load("data/fond.jpg").convert()
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0       

class Wall(pygame.sprite.Sprite):
    def __init__(self, position_x, position_y):

        super().__init__()
        chargement_image = pygame.image.load("data/wall.png").convert_alpha()
        self.image = pygame.transform.scale(chargement_image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.x = int(position_x)
        self.rect.y = int(position_y)
    

