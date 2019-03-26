#! /usr/bin/env python3
#coding: utf-8

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

#Game title
pygame.display.set_caption("Mac Gyver Labyrinthe")

#creating all different sprite groups.
background_sprite = pygame.sprite.Group()
main_character_sprite = pygame.sprite.Group()
wall_sprites = pygame.sprite.Group()
item_sprites = pygame.sprite.Group()

background = objects.Background()
background_sprite.add(background)

MacGyver = objects.MainCharacter()
main_character_sprite.add(MacGyver)

needle = objects.Item()
item_sprites.add(needle)

# For the wall_position, keys will be the x coordinates and values will be the y coordinates.
wall_position = {0 : [90, 120, 150, 270, 300, 330, 390], 30 : [0, 30, 90, 210, 270, 330, 390, 420], 60 : [30, 90, 150, 180, 210, 270, 420],
90 : [90, 180, 330, 360, 420], 120 : [30, 60, 90, 120, 180, 210, 240, 270, 330, 360],
150 : [240, 360], 180 : [0, 30, 90, 120, 150, 240, 300, 360, 390, 420],
210 :[240, 300], 240 : [30, 60, 90, 120, 150, 180, 210, 240, 300, 330, 360, 390],
270: [30, 120, 240, 390], 300 : [30, 90, 180, 240, 270, 300, 330, 360, 390],
330 : [120, 180], 360 :[0, 60, 90, 120, 180, 240, 300, 330, 360, 390, 420], 390 : [0, 120, 240],
420 :[0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360, 390]}


def draw_walls(): # Function used to draw all the walls as sprites on the map
       
    for x, y_list in wall_position.items():
        for y in y_list:
            wall = objects.Wall(x, y)
            wall_sprites.add(wall)

draw_walls()

carryOn = True
clock=pygame.time.Clock()
while carryOn:
        moved_up = 0
        moved_down = 0
        moved_left = 0
        moved_right = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                carryOn = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    carryOn = False
                if event.key == pygame.K_DOWN:
                    if (MacGyver.rect.y + 30) < SCREENHEIGHT:
                        MacGyver.moveDown(30)
                        moved_down += 1
                if event.key == pygame.K_UP:
                    if (MacGyver.rect.y - 30) >= 0: 
                        MacGyver.moveUp(30)
                        moved_up += 1
                if event.key == pygame.K_LEFT:
                    if (MacGyver.rect.x - 30) >= 0:
                        MacGyver.moveLeft(30)
                        moved_left += 1
                if event.key == pygame.K_RIGHT:
                    if (MacGyver.rect.x + 30) < SCREENWIDTH:
                        MacGyver.moveRight(30)
                        moved_right += 1

        #updating the sprites
        background_sprite.update();main_character_sprite.update();wall_sprites.update();item_sprites.update() 
        #pygame.sprite.groupcollide(main_character_sprite, item_sprites, False, True)
        collision_MacGyver_vs_walls = pygame.sprite.groupcollide(main_character_sprite, wall_sprites, False, False)
        if collision_MacGyver_vs_walls:
            if moved_down == 1:
                MacGyver.moveUp(30)
            elif moved_up == 1:
                MacGyver.moveDown(30)
            elif moved_left == 1:
                MacGyver.moveRight(30)
            elif moved_right == 1:
                MacGyver.moveLeft(30)
        #Now let's draw all the sprites in one go. 
        background_sprite.draw(screen);wall_sprites.draw(screen);main_character_sprite.draw(screen);item_sprites.draw(screen)     
        #if pygame.sprite.groupcollide(main_character_sprite, wall_sprites, False, False):
        #    if moved_down == 1:
        #        MacGyver.moveUp(30)
        #Refresh Screen
        pygame.display.flip()
 
        #Number of frames per secong e.g. 60
        clock.tick(60)
 
pygame.quit()
