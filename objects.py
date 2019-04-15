#coding: utf-8

import pygame
import random


class MainCharacter(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()
        
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
        chargement_image = pygame.image.load("data/fond.jpg").convert()
        self.image = pygame.transform.scale(chargement_image, (450, 450))
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


class Item(pygame.sprite.Sprite):
    
    def __init__(self, file_location):

        super().__init__()

        chargement_image = pygame.image.load(file_location).convert_alpha()
        self.image = pygame.transform.scale(chargement_image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, 450, 30)
        self.rect.y = random.randrange(0, 450, 30)       

class Boss(pygame.sprite.Sprite):
    
    def __init__(self):

        super().__init__()
        chargement_image = pygame.image.load("data/Gardien.png").convert_alpha()
        self.image = pygame.transform.scale(chargement_image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.x = 420
        self.rect.y = 420

class Text(pygame.sprite.Sprite):
    
    def __init__(self, location, scale_x, scale_y, rect_x, rect_y):

        super().__init__()
        chargement_image = pygame.image.load(location).convert_alpha()
        self.image = pygame.transform.scale(chargement_image, (scale_x, scale_y))
        self.rect = self.image.get_rect()
        self.rect.x = rect_x
        self.rect.y = rect_y

class Blood(pygame.sprite.Sprite):
    
    def __init__(self, x_position):

        super().__init__()
        chargement_image = pygame.image.load("data/items.png").convert_alpha()
        blood = chargement_image.subsurface(pygame.Rect(224, 0, 32, 32))
        self.image = pygame.transform.scale(blood, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.x = x_position
        self.rect.y = 420
