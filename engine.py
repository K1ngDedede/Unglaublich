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

class Party:

    def __init__(self, sprites, screen):
        self.size = len(sprites)
        self.sprites = sprites
        self.leader = self.sprites[0]
        self.screen = screen

    def update(self):
        self.leader.update()
        for i in range(1, self.size):
            self.sprites[i].current_direction = self.sprites[i-1].current_direction
            self.sprites[i].update()
            self.sprites[i].x = self.sprites[i - 1].past_x
            self.sprites[i].y = self.sprites[i - 1].past_y
        self.leader.map.camera.update(self.leader)
        self.maurisio()

    def draw(self):
        self.leader.map.draw()
        for sprite in self.sprites:
            self.screen.blit(sprite.image, sprite.map.camera.apply(sprite))

    #Verifies if there is a map transition and if there is, the map changes accordingly
    def maurisio(self):
        currentTile = self.leader.get_current_tile()
        if currentTile.adyacent_map_filename != "":
            #load map
            new_map = Map(currentTile.adyacent_map_filename, self.screen)
            for sprite in self.sprites:
                sprite.map = new_map
                sprite.groups = sprite.map.all_sprites
            self.leader.map.load()
            self.leader.x = currentTile.x_spawn * 64
            self.leader.y = currentTile.y_spawn * 64
            self.leader.vel = vec(0, 0)



def get_opposite_direction(direction: int)->str:
    return directions[(direction+2)%4]


