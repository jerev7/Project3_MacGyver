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
blood_sprite = pygame.sprite.Group()
letter_sprites = pygame.sprite.Group()

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
create_item("data/tube_plastique.png")
items_number += 1


def write_words(word, x_starting_position, y_starting_position):
    for letter in word:
        if letter == " ":
            x_starting_position += 30
        else:
            each_letter = objects.Letters(letter, x_starting_position, y_starting_position)
            letter_sprites.add(each_letter)
            x_starting_position += 30


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
        
        collision_MacGyver_vs_boss = pygame.sprite.groupcollide(main_character_sprite, boss_sprite, False, False)
        collision_MacGyver_vs_item = pygame.sprite.groupcollide(main_character_sprite, item_sprites, False, True)
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

        if collision_MacGyver_vs_item:
            pygame.event.set_blocked(pygame.KEYDOWN)
            items_picked_up += 1
            write_words("ITEMS PICKED UP", 0, 120)
            if items_picked_up == 1: 
                write_words("I OF III", 120, 180)
            elif items_picked_up == 2:
                write_words("II OF III", 90, 180)
            elif items_picked_up == 3:
                write_words("III OF III", 60, 180)
            letter_sprites.draw(screen)            
            pygame.display.flip()
            pygame.time.wait(1000)
            #time.sleep(2)
            pygame.event.set_allowed(pygame.KEYDOWN)  

        background_sprite.draw(screen)
        wall_sprites.draw(screen)
        item_sprites.draw(screen)
        
        if collision_MacGyver_vs_boss:
            if items_picked_up == items_number:
                pygame.sprite.groupcollide(main_character_sprite, boss_sprite, False, True)
                main_character_sprite.draw(screen)
                boss_sprite.draw(screen)
                victory_text = objects.Text("data/win.png")
                text_sprite.add(victory_text)
                text_sprite.draw(screen)
                pygame.display.flip()
                input("The game is over : press Enter to leave")
                carryOn = False
            else:
                pygame.sprite.groupcollide(main_character_sprite, boss_sprite, True, False)
                boss_sprite.draw(screen)
                blood = objects.Blood(390)
                blood_sprite.add(blood)
                blood_sprite.draw(screen)
                loose_text = objects.Text("data/loose.jpeg")
                text_sprite.add(loose_text)
                text_sprite.draw(screen)
                pygame.display.flip()
                carryOn = False
                input("You are dead cause you haven't collected all the needed items to defeat the keeper, leave now by pressing Enter and start again !!")
        else:
            main_character_sprite.draw(screen)
            boss_sprite.draw(screen)
            pygame.display.flip()

        #Number of frames per secong e.g. 60
        clock.tick(60)

pygame.quit()
