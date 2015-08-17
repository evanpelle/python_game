#!venv/bin/python3

import sys

import pygame
from pygame.locals import *

from gamemap import GameMap

def run():

    red_dot_imgf = "img/red_dot.png"
    background_imgf = "img/background.jpg"
    test_tile_imgf = "img/test_tile.png"


    pygame.init()

    size = width, height = 600, 500

    screen = pygame.display.set_mode(size)
    #gm = gamemap.GameMap()

    background = pygame.image.load(background_imgf).convert()
    mouse_c = pygame.image.load(red_dot_imgf).convert()
    test_tile = pygame.image.load(test_tile_imgf).convert()

    while True:
        for event in pygame.event.get():
            if event.type ==  QUIT:
                pygame.quit()
                sys.exit()

        x, y = pygame.mouse.get_pos()
        print(x)
        # gm.render()
        screen.blit(test_tile, (0,0))
        pygame.display.update()
if __name__ == 'main':
    run()