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
all_sprites_list = pygame.sprite.Group()

background = objects.Background()
all_sprites_list.add(background)

MacGyver = objects.MainCharacter()
all_sprites_list.add(MacGyver)

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
                    MacGyver.moveDown(30)
                if event.key == pygame.K_UP:
                    MacGyver.moveUp(30)
                if event.key == pygame.K_LEFT:
                    MacGyver.moveLeft(30)
                if event.key == pygame.K_RIGHT:
                    MacGyver.moveRight(30)    
        #Game Logic
        all_sprites_list.update()
 
        #Drawing on Screen
        #screen.fill(GREEN)
       
        
        #Now let's draw all the sprites in one go. (For now we only have 1 sprite!)
        all_sprites_list.draw(screen)
 
        #Refresh Screen
        pygame.display.flip()
 
        #Number of frames per secong e.g. 60
        clock.tick(60)
 
pygame.quit()
