#! /usr/bin/env python3
#coding: utf-8

import pygame
import objects



WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SCREENWIDTH=450
SCREENHEIGHT=450
 
size = (SCREENWIDTH, SCREENHEIGHT)

items_picked_up = 0
items_number = 0

# For the walls position, keys will be the x coordinates and values will be the y coordinates.
wall_position = {0 : [90, 120, 150, 270, 300, 330, 390, 420], 30 : [0, 30, 90, 210, 270, 330, 390, 420], 60 : [30, 90, 150, 180, 210, 270, 420],
90 : [90, 180, 330, 360, 420], 120 : [30, 60, 90, 120, 180, 210, 240, 270, 330, 360],
150 : [240, 360], 180 : [0, 30, 90, 120, 150, 240, 300, 360, 390, 420],
210 :[240, 300], 240 : [30, 60, 90, 120, 150, 180, 210, 240, 300, 330, 360, 390],
270: [30, 120, 240, 390], 300 : [30, 90, 180, 240, 270, 300, 330, 360, 390],
330 : [120, 180], 360 :[0, 60, 90, 120, 180, 240, 300, 330, 360, 390, 420], 390 : [0, 120, 240],
420 :[0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360, 390]}

pygame.init()

# We hide the mouse
pygame.mouse.set_visible(0)

screen = pygame.display.set_mode((size), pygame.FULLSCREEN)

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

background = objects.Background()
background_sprite.add(background)

mac_gyver = objects.MainCharacter()
main_character_sprite.add(mac_gyver)

boss = objects.Boss()
boss_sprite.add(boss)


def draw_walls(): # Function used to draw all the walls as sprites on the map
       
    for x, y_list in wall_position.items():
        for y in y_list:
            wall = objects.Wall(x, y)
            wall_sprites.add(wall)
draw_walls()

def create_item(location): # Function used to create each item of the game

    collision_nbr = 1
    while collision_nbr != 0:
        item = objects.Item(location)
        

        collision_nbr = 0
        # We test if the new item has not been created at the same place than another item already existing
        if pygame.sprite.spritecollide(item, item_sprites, True):
            collision_nbr += 1
        else:
            item_sprites.add(item)
        # Then we test if the item has not been created at the same place than walls, Mac Gyver, or the boss
        if pygame.sprite.groupcollide(item_sprites, wall_sprites, True, False):
            collision_nbr += 1
        if pygame.sprite.groupcollide(item_sprites, main_character_sprite, True, False):
            collision_nbr += 1
        if pygame.sprite.groupcollide(item_sprites, boss_sprite, True, False):
            collision_nbr += 1
    return item

ether = create_item("data/ether2.png")
items_number += 1
needle = create_item("data/seringue2.png")
items_number += 1
plastic = create_item("data/tube_plastique2.png")
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
                if (mac_gyver.rect.y + 30) < SCREENHEIGHT:
                    mac_gyver.moveDown(30)
                    moved_down += 1
            if event.key == pygame.K_UP:
                if (mac_gyver.rect.y - 30) >= 0: 
                    mac_gyver.moveUp(30)
                    moved_up += 1
            if event.key == pygame.K_LEFT:
                if (mac_gyver.rect.x - 30) >= 0:
                    mac_gyver.moveLeft(30)
                    moved_left += 1
            if event.key == pygame.K_RIGHT:
                if (mac_gyver.rect.x + 30) < SCREENWIDTH:
                    mac_gyver.moveRight(30)
                    moved_right += 1
                
        #updating the sprites
        background_sprite.update()
        main_character_sprite.update()
        wall_sprites.update()
        item_sprites.update()
        boss_sprite.update()
        
        collision_mac_gyver_vs_boss = pygame.sprite.groupcollide(main_character_sprite, boss_sprite, False, False)
        collision_mac_gyver_vs_item = pygame.sprite.groupcollide(main_character_sprite, item_sprites, False, True)
        collision_mac_gyver_vs_walls = pygame.sprite.groupcollide(main_character_sprite, wall_sprites, False, False)

        if collision_mac_gyver_vs_item:
            items_picked_up += 1
        
        if collision_mac_gyver_vs_walls:
            if moved_down == 1:
                mac_gyver.moveUp(30)
            elif moved_up == 1:
                mac_gyver.moveDown(30)
            elif moved_left == 1:
                mac_gyver.moveRight(30)
            elif moved_right == 1:
                mac_gyver.moveLeft(30)

        background_sprite.draw(screen)
        wall_sprites.draw(screen)
        item_sprites.draw(screen)
        
        pygame.font.init()

        bag_text = "Items picked up :"
        ether_full = "Ether : 1/1"
        ether_empty = "Ether : 0/1"
        plastic_empty = "Plastic 0/1"
        plastic_full = "Plastic : 1/1"
        needle_empty = "Needle : 0/1"
        needle_full = "Needle : 1/1"

        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        screen.blit(myfont.render(bag_text, False, (0, 0, 0)), (0, 330))

        if pygame.sprite.Sprite.alive(ether):
            screen.blit(myfont.render(ether_empty, False, (0, 0, 0)), (0, 360))
        else:
            screen.blit(myfont.render(ether_full, False, (0, 0, 0)), (0, 360))
        if pygame.sprite.Sprite.alive(plastic):
            screen.blit(myfont.render(plastic_empty, False, (0, 0, 0)), (0, 390))
        else:
            screen.blit(myfont.render(plastic_full, False, (0, 0, 0)), (0, 390))
        if pygame.sprite.Sprite.alive(needle):
            screen.blit(myfont.render(needle_empty, False, (0, 0, 0)), (0, 420))
        else:
            screen.blit(myfont.render(needle_full, False, (0, 0, 0)), (0, 420))

        myfont2 = pygame.font.SysFont('Comic Sans MS', 22, True)

        victory_sentence1 = "You managed to make the keeper fall asleep with all"
        victory_sentence2 = "items you found and escaped the labyrinth !!" 
        defeat_sentence1 = "The keeper was awake and killed you ! You need"
        defeat_sentence2 = "to find all items before trying to escape !"
        
        if collision_mac_gyver_vs_boss:
            if items_picked_up == items_number:
                pygame.sprite.groupcollide(main_character_sprite, boss_sprite, False, True)
                main_character_sprite.draw(screen)
                boss_sprite.draw(screen)
                victory_image = objects.Text("data/win.png", 100, 100, 150, 150)
                text_sprite.add(victory_image)
                text_sprite.draw(screen)
                screen.blit(myfont2.render(victory_sentence1, False, (0, 0, 0), (255, 255, 255)), (0, 0))
                screen.blit(myfont2.render(victory_sentence2, False, (0, 0, 0), (255, 255, 255)), (0, 30))
                pygame.display.flip()
                pygame.time.wait(7000)
                carryOn = False
            else:
                pygame.sprite.groupcollide(main_character_sprite, boss_sprite, True, False)
                boss_sprite.draw(screen)
                blood = objects.Blood(390)
                blood_sprite.add(blood)
                blood_sprite.draw(screen)
                defeat_image = objects.Text("data/loose.jpeg", 100, 100, 150, 150)
                text_sprite.add(defeat_image)
                text_sprite.draw(screen)
                screen.blit(myfont2.render(defeat_sentence1, False, (0, 0, 0), (255, 255, 255)), (0, 0))
                screen.blit(myfont2.render(defeat_sentence2, False, (0, 0, 0), (255, 255, 255)), (0, 30))
                pygame.display.flip()
                pygame.time.wait(7000)
                carryOn = False
                
        else:
            main_character_sprite.draw(screen)
            boss_sprite.draw(screen)
            pygame.display.flip()

        #Number of frames per secong e.g. 60
        clock.tick(60)

pygame.quit()
