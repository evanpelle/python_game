#!venv/bin/python3

import sys

import pygame
from pygame.locals import *

from const import screen
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

    while True:
        x, y = pygame.mouse.get_pos()
        tile = gm.get_tile(x,y)
        if tile is not None:
            tile.visible = False
        for event in pygame.event.get():
            if event.type ==  QUIT:
                pygame.quit()
                sys.exit()
        screen.blit(background, (0,0))
        gm.render()
        pygame.display.update()

if __name__ == '__main__':
    run()