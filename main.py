#! /usr/bin/env python3
#coding: utf-8

"""This file is the main code file"""

import pygame
import objects


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SCREENWIDTH = 450
SCREENHEIGHT = 450
BLOCK = 30

#We open the text file which contains the map of the labyrinth
with open("data/map", "r") as text_file:
    CONTENT = text_file.read()

def create_map(map_file):
    """Function used to add walls on the background"""
    new_map = map_file.split("\n")
    for line_number, line in enumerate(new_map):
        line_list = list(line)
        count = 0
        while count < len(line_list):
            if "0" in line_list[count]:
                y_map = (line_number) * BLOCK
                x_map = count * BLOCK
                wall = objects.Wall(x_map, y_map)
                WALL_GRP.add(wall)
            count += 1

SIZE = (SCREENWIDTH, SCREENHEIGHT)

#Creating all different sprite groups
BG_GRP = pygame.sprite.Group()
MAIN_CHAR_GRP = pygame.sprite.Group()
WALL_GRP = pygame.sprite.Group()
ITEM_GRP = pygame.sprite.Group()
BOSS_GRP = pygame.sprite.Group()
BLOOD_GRP = pygame.sprite.Group()
TEXT_GRP = pygame.sprite.Group()

def create_item(location):
    """Function used to create each item of the game"""
    collision_nbr = 1
    while collision_nbr != 0:
        item = objects.Item(location)
        collision_nbr = 0
        #We test if the new item has not been created at the same place
        #than another item already existing
        if pygame.sprite.spritecollide(item, ITEM_GRP, False):
            collision_nbr += 1
        else:
            ITEM_GRP.add(item)
        #Then we test if the item has not been created at the
        #same place than walls, Mac Gyver, or the boss
        if pygame.sprite.groupcollide(ITEM_GRP, WALL_GRP, True, False):
            collision_nbr += 1
        if pygame.sprite.groupcollide(ITEM_GRP, MAIN_CHAR_GRP, True, False):
            collision_nbr += 1
        if pygame.sprite.groupcollide(ITEM_GRP, BOSS_GRP, True, False):
            collision_nbr += 1
    return item

def main():
    """Function to run everything the program needs in pygame interface"""
    items_picked_up = 0
    items_number = 0

    pygame.init()

    # We hide the mouse
    pygame.mouse.set_visible(0)

    screen = pygame.display.set_mode((SIZE), pygame.FULLSCREEN)

    #Game title
    pygame.display.set_caption("Mac Gyver Labyrinthe")

    background = objects.Background()
    BG_GRP.add(background)

    mac_gyver = objects.MainCharacter()
    MAIN_CHAR_GRP.add(mac_gyver)

    boss = objects.Boss()
    BOSS_GRP.add(boss)

    create_map(CONTENT)

    ether = create_item("data/ether2.png")
    items_number += 1
    needle = create_item("data/seringue2.png")
    items_number += 1
    plastic = create_item("data/tube_plastique2.png")
    items_number += 1


    carry_on = True
    clock = pygame.time.Clock()
    while carry_on:
        moved_up = 0
        moved_down = 0
        moved_left = 0
        moved_right = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                carry_on = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    carry_on = False
                if event.key == pygame.K_DOWN:
                    if (mac_gyver.rect.y + BLOCK) < SCREENHEIGHT:
                        mac_gyver.moveDown(BLOCK)
                        moved_down += 1
                if event.key == pygame.K_UP:
                    if (mac_gyver.rect.y - BLOCK) >= 0:
                        mac_gyver.moveUp(BLOCK)
                        moved_up += 1
                if event.key == pygame.K_LEFT:
                    if (mac_gyver.rect.x - BLOCK) >= 0:
                        mac_gyver.moveLeft(BLOCK)
                        moved_left += 1
                if event.key == pygame.K_RIGHT:
                    if (mac_gyver.rect.x + BLOCK) < SCREENWIDTH:
                        mac_gyver.moveRight(BLOCK)
                        moved_right += 1
            #updating the sprites
            BG_GRP.update()
            MAIN_CHAR_GRP.update()
            WALL_GRP.update()
            ITEM_GRP.update()
            BOSS_GRP.update()
            coll_mac_vs_boss = pygame.sprite.groupcollide(MAIN_CHAR_GRP, BOSS_GRP, False, False)
            coll_mac_vs_item = pygame.sprite.groupcollide(MAIN_CHAR_GRP, ITEM_GRP, False, True)
            coll_mac_vs_wall = pygame.sprite.groupcollide(MAIN_CHAR_GRP, WALL_GRP, False, False)

            if coll_mac_vs_item:
                items_picked_up += 1
            if coll_mac_vs_wall:
                if moved_down == 1:
                    mac_gyver.moveUp(BLOCK)
                elif moved_up == 1:
                    mac_gyver.moveDown(BLOCK)
                elif moved_left == 1:
                    mac_gyver.moveRight(BLOCK)
                elif moved_right == 1:
                    mac_gyver.moveLeft(BLOCK)

            BG_GRP.draw(screen)
            WALL_GRP.draw(screen)
            ITEM_GRP.draw(screen)
            pygame.font.init()

            #some variables for each line of the inventory
            bag_text = "Items picked up :"
            ether_full = "Ether : 1/1"
            ether_empty = "Ether : 0/1"
            plastic_empty = "Plastic 0/1"
            plastic_full = "Plastic : 1/1"
            needle_empty = "Needle : 0/1"
            needle_full = "Needle : 1/1"

            myfont = pygame.font.SysFont('Comic Sans MS', 30)
            screen.blit(myfont.render(bag_text, False, (0, 0, 0)), (0, 330))

            #it will determine how the inventory is
            #displayed depending on which item the user has already picked up
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
            #those are the two ending situation, defeat or victory
            if coll_mac_vs_boss:
                if items_picked_up == items_number:
                    pygame.sprite.groupcollide(MAIN_CHAR_GRP, BOSS_GRP, False, True)
                    MAIN_CHAR_GRP.draw(screen)
                    BOSS_GRP.draw(screen)
                    victory_image = objects.Text("data/win.png", 100, 100, 150, 150)
                    TEXT_GRP.add(victory_image)
                    TEXT_GRP.draw(screen)
                    screen.blit(myfont2.render(victory_sentence1, \
                        False, (0, 0, 0), (255, 255, 255)), (0, 0))
                    screen.blit(myfont2.render(victory_sentence2, \
                        False, (0, 0, 0), (255, 255, 255)), (0, 30))
                    pygame.display.flip()
                    pygame.time.wait(7000)
                    carry_on = False
                else:
                    pygame.sprite.groupcollide(MAIN_CHAR_GRP, BOSS_GRP, True, False)
                    BOSS_GRP.draw(screen)
                    blood = objects.Blood(390)
                    BLOOD_GRP.add(blood)
                    BLOOD_GRP.draw(screen)
                    defeat_image = objects.Text("data/loose.jpeg", 100, 100, 150, 150)
                    TEXT_GRP.add(defeat_image)
                    TEXT_GRP.draw(screen)
                    screen.blit(myfont2.render(defeat_sentence1, \
                        False, (0, 0, 0), (255, 255, 255)), (0, 0))
                    screen.blit(myfont2.render(defeat_sentence2, \
                        False, (0, 0, 0), (255, 255, 255)), (0, 30))
                    pygame.display.flip()
                    pygame.time.wait(7000)
                    carry_on = False
            #if it's not ended then program goes on
            else:
                MAIN_CHAR_GRP.draw(screen)
                BOSS_GRP.draw(screen)
                pygame.display.flip()

            #Number of frames per secong e.g. 60
            clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
