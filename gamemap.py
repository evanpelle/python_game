import pygame

from const import *





class GameMap:

    def __init__(self):
        self.width = 10
        self.height = 10
        self.grid = []
        for x in range(self.width):
            self.grid.append([])
            for y in range(self.height):
                offset = 0 if y%2 else (Tile.width - Tile.render_offset_x)/2
                self.grid[x].append(Tile(
                    x*(Tile.width-Tile.render_offset_x)\
                    + offset, y*(Tile.height-Tile.render_offset_y)))

    def get_tile(self, mouse_x, mouse_y):
        tile_y = ((mouse_y - 10)//(Tile.height - Tile.render_offset_y))
        #print("tyle_y: " + str(tile_y))
        #print("mous_y: " + str(mouse_y))
        offset = 0 if tile_y%2 else (Tile.width - Tile.render_offset_x)/2
        tile_x = (int) ((mouse_x - offset)//(Tile.width - Tile.render_offset_x))
        print("mouse_x: " + str(mouse_x))
        print("tile_x: " + str(tile_x))
        try:
            return self.grid[tile_x][tile_y]
        except:
            return None

    def render(self):
        for row in self.grid:
            for tile in row:
                tile.render()

class Tile:
    render_offset_x = 10
    render_offset_y = 22
    height = 100
    width = 100

    def __init__(self, posX=0, posY=0):
        self.posX = posX
        self.posY = posY
        self.visible = True

    def render(self):
        if self.visible:
            screen.blit(test_tile, (self.posX, self.posY))
