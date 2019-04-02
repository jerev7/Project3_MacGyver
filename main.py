#! /usr/bin/env python3
#coding: utf-8

import pygame
import objects
import os
import time
from data import *
#from pygame.locals import *

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SCREENWIDTH=450
SCREENHEIGHT=450
 
size = (SCREENWIDTH, SCREENHEIGHT)

items_picked_up = 0
items_number = 0
pygame.init()


screen = pygame.display.set_mode((size), pygame.RESIZABLE)

#Game title
pygame.display.set_caption("Mac Gyver Labyrinthe")

#creating all different sprite groups.
background_sprite = pygame.sprite.Group()
main_character_sprite = pygame.sprite.Group()
wall_sprites = pygame.sprite.Group()
item_sprites = pygame.sprite.Group()
boss_sprite = pygame.sprite.Group()
text_sprite = pygame.sprite.Group()


background = objects.Background()
background_sprite.add(background)

MacGyver = objects.MainCharacter()
main_character_sprite.add(MacGyver)


boss = objects.Boss()
boss_sprite.add(boss)


def draw_walls(): # Function used to draw all the walls as sprites on the map
       
    for x, y_list in wall_position.items():
        for y in y_list:
            wall = objects.Wall(x, y)
            wall_sprites.add(wall)
draw_walls()

def create_item(location):

    collision_nbr = 1
    while collision_nbr != 0:
        item = objects.Item(location)
        collision_nbr = 0
        # We test if the new item has not been created at the same place than another item already existing
        if pygame.sprite.spritecollide(item, item_sprites, True):
            collision_nbr += 1
        item_sprites.add(item)
        # Then we test if the item has not been created at the same place than walls, Mac Gyver, or the boss
        if pygame.sprite.groupcollide(item_sprites, wall_sprites, True, False):
            collision_nbr += 1
        if pygame.sprite.groupcollide(item_sprites, main_character_sprite, True, False):
            collision_nbr += 1
        if pygame.sprite.groupcollide(item_sprites, boss_sprite, True, False):
            collision_nbr += 1

create_item("data/ether.png")
items_number += 1
create_item("data/seringue.png")
items_number += 1



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
        background_sprite.update()
        main_character_sprite.update()
        wall_sprites.update()
        item_sprites.update()
        boss_sprite.update()
        text_sprite.update() 
        
        collision_MacGyver_vs_boss = pygame.sprite.groupcollide(main_character_sprite, boss_sprite, False, False)
        collision_MacGyver_vs_item = pygame.sprite.groupcollide(main_character_sprite, item_sprites, False, True)
        collision_MacGyver_vs_walls = pygame.sprite.groupcollide(main_character_sprite, wall_sprites, False, False)
        
        if collision_MacGyver_vs_item:
            items_picked_up += 1


        if collision_MacGyver_vs_walls:
            if moved_down == 1:
                MacGyver.moveUp(30)
            elif moved_up == 1:
                MacGyver.moveDown(30)
            elif moved_left == 1:
                MacGyver.moveRight(30)
            elif moved_right == 1:
                MacGyver.moveLeft(30)    

        background_sprite.draw(screen)
        wall_sprites.draw(screen)
        item_sprites.draw(screen)     
        
        #Refresh Screen
        
        if collision_MacGyver_vs_boss:
            if items_picked_up == items_number:
                pygame.sprite.groupcollide(main_character_sprite, boss_sprite, False, True)
                main_character_sprite.draw(screen)
                boss_sprite.draw(screen)
                victory_text = objects.Text("data/win.png")
                text_sprite.add(victory_text)
                text_sprite.draw(screen)
                pygame.display.flip()
                #time.sleep(0.1)
                input("Partie terminée : appuyez sur entrée pour quitter")
                carryOn = False
            else:
                pygame.sprite.groupcollide(main_character_sprite, boss_sprite, True, False)
                boss_sprite.draw(screen)
                loose_text = objects.Text("data/loose.jpeg")
                text_sprite.add(loose_text)
                text_sprite.draw(screen)
                pygame.display.flip()
                input("Vous êtes mort, relancez le jeu pour recommencer la partie (appuyez sur entrée pour quitter)")
                carryOn = False
        else:
            main_character_sprite.draw(screen)
            boss_sprite.draw(screen)
            pygame.display.flip()
        
        #Number of frames per secong e.g. 60
        clock.tick(60)

pygame.quit()
