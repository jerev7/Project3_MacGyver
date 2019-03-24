#! /usr/bin/env python3
#coding: utf-8
#Importation des bibliothèques nécessaires

import pygame
import objects

#from pygame.locals import *

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SCREENWIDTH=450
SCREENHEIGHT=450
 
size = (SCREENWIDTH, SCREENHEIGHT)

#Initialisation de la bibliothèque Pygame

pygame.init()


#Création de la fenêtre
screen = pygame.display.set_mode((size), pygame.RESIZABLE)

# Titre du jeu
pygame.display.set_caption("Mac Gyver Labyrinthe")

#This will be a list that will contain all the sprites we intend to use in our game.
background_sprite = pygame.sprite.Group()
main_character_sprite = pygame.sprite.Group()
wall_sprites = pygame.sprite.Group()
item_sprites = pygame.sprite.Group()

background = objects.Background()
background_sprite.add(background)

MacGyver = objects.MainCharacter()
main_character_sprite.add(MacGyver)


wall = objects.Wall(60, 90)
wall_sprites.add(wall)
#Allowing the user to close the window...
carryOn = True
clock=pygame.time.Clock()
 
while carryOn:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                carryOn=False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    carryOn = False
                if event.key == pygame.K_DOWN:
                    if (MacGyver.rect.y + 30) < SCREENHEIGHT:
                        MacGyver.moveDown(30)
                if event.key == pygame.K_UP:
                    if (MacGyver.rect.y - 30) >= 0: 
                        MacGyver.moveUp(30)
                if event.key == pygame.K_LEFT:
                    if (MacGyver.rect.x - 30) >= 0:
                        MacGyver.moveLeft(30)
                if event.key == pygame.K_RIGHT:
                    if (MacGyver.rect.x + 30) < SCREENWIDTH:
                        MacGyver.moveRight(30)
        #Game Logic
        background_sprite.update()
        main_character_sprite.update()
        wall_sprites.update()
 
        
        #Now let's draw all the sprites in one go. (For now we only have 1 sprite!)
        background_sprite.draw(screen)
        wall_sprites.draw(screen)
        main_character_sprite.draw(screen)
 
        #Refresh Screen
        pygame.display.flip()
 
        #Number of frames per secong e.g. 60
        clock.tick(60)
 
pygame.quit()
