#!/usr/bin/python3
import sys

import pygame
from pygame.locals import *
import gvars
from gamemap import GameMap

def run():
    print('running')

    red_dot_imgf = "img/red_dot.png"
    background_imgf = "img/background.jpg"
    test_tile_imgf = "img/test_tile.png"


    pygame.init()

    
    gm = GameMap()

    background = pygame.image.load(background_imgf).convert()
    mouse_c = pygame.image.load(red_dot_imgf).convert()
    test_tile = pygame.image.load(test_tile_imgf).convert()
    x,y = 0,0

    while True:
        x, y = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type ==  QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONUP:
                x, y = pygame.mouse.get_pos()
                tile = gm.get_tile(x,y)
                if tile is not None:
                    tile.visible = False
            if event.type == pygame.KEYDOWN:
                pass
        press = pygame.key.get_pressed()
        if press[pygame.K_LEFT]:
            gvars.offset_x -= 8
        if press[pygame.K_RIGHT]:
            gvars.offset_x += 8
        if press[pygame.K_UP]:
            gvars.offset_y -= 3
        if press[pygame.K_DOWN]:
            gvars.offset_y += 3


        #print(x)
        #background = pygame.transform.scale(background, (200,200))
        gvars.screen.blit(background, (0,0))
        gm.render()
        pygame.display.update()

if __name__ == '__main__':
    run()