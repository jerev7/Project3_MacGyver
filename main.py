#! /usr/bin/env python3
# coding: utf-8
#Importation des bibliothèques nécessaires

import pygame

#from pygame.locals import *


#Initialisation de la bibliothèque Pygame

pygame.init()


#Création de la fenêtre

window = pygame.display.set_mode((640, 480), pygame.RESIZABLE)

# Chargement et collage du fond
background = pygame.image.load("data/background.jpg").convert()
window.blit(background, (0, 0))

#Personnage
character = pygame.image.load("data/perso.png").convert_alpha()
#character.set_colorkey((0, 0, 0))

window.blit(character, (200, 300))


#Rafraîchissement de l'écran
pygame.display.flip()

#Boucle infini

carryOn = 1

while carryOn:
	for event in pygame.event.get(): # On parcours la liste de tous les evenement reçus
		if event.type == pygame.QUIT:
			carryOn = 0
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				carryOn = 0

pygame.quit()