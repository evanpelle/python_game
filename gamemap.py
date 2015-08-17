import main

test_tile_imgf = "img/test_tile.png"
test_tile = pygame.image.load(test_tile_imgf).convert()



class GameMap:

    def __init__(self):
        self.width = 10
        self.height = 10
        self.grid = []
        for i in range(self.width):
            self.grid.append([])
            for j in range(self.height):
                self.grid[i].append(Tile(i*30, j*30))

    def render(self):
        for row in self.grid:
            for t in row:
                t.render()

class Tile:

    def __init__(self, posX=0, posY=0):
        self.posX = posX
        self.posY = posY

    def render(self):
        screen.blit(test_tile, (self.posX, self.posY))