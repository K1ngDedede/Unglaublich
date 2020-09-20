from os import path
import pygame as pg
import sys
from settings import *
from sprites import *

class Map:

    def __init__(self, filename, screen):
        #Matrix of tiles
        self.nig = []
        self.all_sprites = pg.sprite.Group()
        self.tiles = pg.sprite.Group()
        self.collidable_tiles = pg.sprite.Group()
        self.action_tiles = pg.sprite.Group()
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
                self.nig[row].append(Tile(tile_filename, adyacent_filename, tile_poggers, tile_x, tile_y, self))
                col+=1
            row+=1
        self.height = len(self.nig)
        self.width = len(self.nig[0])
        self.height_px = self.height * TILESIZE
        self.width_px = self.width * TILESIZE
        world_file.close()
        self.camera = Camera(self.width_px, self.height_px)

    def draw(self):
        for tile in self.tiles:
                self.screen.blit(tile.image, self.camera.apply(tile))


class Tile(pg.sprite.Sprite):

    def __init__(self, image_filename, adyacent_map_filename, poggers, x, y, map):
        if not poggers:
            self.groups = map.tiles, map.all_sprites, map.collidable_tiles
        else:
            self.groups = map.tiles, map.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.map = map
        self.x_spawn = ""
        self.y_spawn = ""
        self.image_filename = "imgs/"+image_filename
        if adyacent_map_filename != "":
            self.adyacent_map_filename = adyacent_map_filename.split("-")[0]
            self.x_spawn = int(adyacent_map_filename.split("-")[1])
            self.y_spawn = int(adyacent_map_filename.split("-")[2])
        else:
            self.adyacent_map_filename = ""
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

def get_opposite_direction(direction: int)->str:
    return directions[(direction+2)%4]


