import sys

import pygame
from pygame.locals import *

size = width, height = 1000, 800
screen = pygame.display.set_mode(size)

test_tile_imgf = "img/test_tile.png"
test_tile = pygame.image.load(test_tile_imgf)