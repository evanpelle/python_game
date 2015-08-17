#!venv/bin/python3

import sys, pygame
from pygame.locals import *

red_dot_imgf = "img/red_dot.png"
background_imgf = "background.jpg"

pygame.init()

size = width, height = 600, 500

screen = pygame.display.set_mode(size)

background = pygame.image.load(background_imgf).convert()
mouse_c = pygame.image.load(red_dot_imgf).convert()

while True:
    for event in pygame.event.get():
        if event.type ==  QUIT:
            pygame.quit()
            sys.exit()

    x, y = pygame.mouse.get_pos()
    print(x)
    screen.blit(background, (0,0))
    screen.blit(mouse_c, (x,y))
    pygame.display.update()