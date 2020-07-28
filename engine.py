from os import path
import pygame as pg
import sys
from settings import *
from sprites import *

class Map:

    def __init__(self, filename, screen):
        #Matrix of tiles
        self.nig = []
        self.filename = "worlds/"+filename
        self.screen = screen

    def load(self):
        world_file = open(self.filename, "r")
        row = 0
        for line in world_file:
            col = 0
            line = line.strip()
            self.nig.append([])
            row_tiles = line.split(",")
            for tile in row_tiles:
                tile = tile.split(":")
                tile_filename = tile[0]
                adyacent_filename = tile[1]
                tile_poggers = int(tile[2])
                tile_x = col * TILESIZE
                tile_y = row * TILESIZE
                self.nig[row].append(Tile(tile_filename, adyacent_filename, tile_poggers, tile_x, tile_y))
                col+=1
            row+=1
        self.height = len(self.nig)
        self.width = len(self.nig[0])
        self.height_px = self.height * TILESIZE
        self.width_px = self.width * TILESIZE
        world_file.close()
        self.camera = Camera(self.width_px, self.height_px)

    def draw(self):
        for row in self.nig:
            for tile in row:
                self.screen.blit(tile.image, self.camera.apply(tile))


class Tile(pg.sprite.Sprite):

    def __init__(self, image_filename, adyacent_map_filename, poggers, x, y):
        self.image_filename = "imgs/"+image_filename
        self.adyacent_map_filename = adyacent_map_filename
        #poggers indicates whether a tile is walkable or not
        self.poggers = poggers
        self.x = x
        self.y = y
        self.image = pg.image.load(self.image_filename).convert()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y




class Camera:
    def __init__(self, width, height):
        self.camera = pg.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        x = -target.rect.x + int(WIDTH / 2)
        y = -target.rect.y + int(HEIGHT / 2)

        # limit scrolling to map size
        x = min(0, x)  # left
        y = min(0, y)  # top
        x = max(-(self.width - WIDTH), x)  # right
        y = max(-(self.height - HEIGHT), y)  # bottom
        self.camera = pg.Rect(x, y, self.width, self.height)

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption(TITULO)
doge_map = Map("example.txt", screen)
doge_map.load()
knight = Nameless(0,0,screen)
pg.key.set_repeat(1, 50)
while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT: sys.exit()
        doge_map.camera.update(knight)
        doge_map.draw()
        knight.update()
        screen.blit(knight.image, doge_map.camera.apply(knight))
        pg.display.flip()
