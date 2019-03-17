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

# Chargement et collage du fond
background = pygame.image.load("data/fond.jpg").convert()
screen.blit(background, (0, 0))
#Personnage
MacGyver = objects.MainCharacter()
screen.blit(MacGyver.picture, MacGyver.rect)


#Rafraîchissement de l'écran
pygame.display.flip()

#Fonction pour pouvoir rester appuyé sur les touches:
#pygame.key.set_repeat(400, 30)
#Boucle infini

carryOn = True

while carryOn:
	pygame.time.Clock().tick(30)
	for event in pygame.event.get(): # On parcours la liste de tous les evenement reçus
		if event.type == pygame.QUIT:
			carryOn = False
		if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					carryOn = False
		if (MacGyver.rect.x <= (SCREENWIDTH-30) and MacGyver.rect.x >= 0) and (MacGyver.rect.y <= (SCREENHEIGHT-30) and MacGyver.rect.y >= 0):	
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_DOWN:
					MacGyver.moveDown(30)
				if event.key == pygame.K_UP:
					MacGyver.moveUp(30)
				if event.key == pygame.K_LEFT:
					MacGyver.moveLeft(30)
				if event.key == pygame.K_RIGHT:
					MacGyver.moveRight(30)
	

	
	screen.blit(background, (0, 0))
	screen.blit(MacGyver.picture, (MacGyver.rect.x, MacGyver.rect.y))
	
	#Game Logic
	
	pygame.display.flip()
	


