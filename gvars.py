import sys

import pygame
from pygame.locals import *

size = width, height = 1000, 800
screen = pygame.display.set_mode(size)

test_tile_imgf = "img/test_tile.png"
test_tile = pygame.image.load(test_tile_imgf)

offset_x = 0
offset_y = 0
zoom_factor = 1

def convert_mouse(pos_x, pos_y):
    return pos_x + offset_x, pos_y + offset_y

def convert(pos_x, pos_y):
    return pos_x - offset_x, pos_y - offset_y

def render(img, pos_x, pos_y):
    screen.blit(test_tile, convert(pos_x, pos_y))