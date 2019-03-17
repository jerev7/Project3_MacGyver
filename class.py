#coding: utf-8

import pygame

class MainCharacter():

	def __init__(self):

		
		self.picture = pygame.image.load("data/MacGyver2.png").convert_alpha()
		self.rect = self.picture.get_rect()
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

class Background():

	def __init__(self, chemin):
		self.picture = pygame.image.load(chemin).convert()



