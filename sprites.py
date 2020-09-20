import pygame as pg
from settings import *
import engine as tomas
vec = pg.math.Vector2

class Nameless(pg.sprite.Sprite):

    def __init__(self, x, y, screen, map):
        self.groups = map.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.x = x*64
        self.y = y*64
        self.image = pg.image.load("imgs/nameless_pixelart3.png").convert_alpha()
        self.speed = PLAYER_SPEED
        self.screen = screen
        self.rect = self.image.get_rect()
        self.map = map
        self.vel = vec(0,0)
        self.current_direction = 3

    def keys(self):
        self.vel = vec(0,0)
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.vel.y = -self.speed
            self.current_direction = 0
        elif keys[pg.K_a]:
            self.vel.x = -self.speed
            self.current_direction = 1
        elif keys[pg.K_s]:
            self.vel.y = self.speed
            self.current_direction = 2
        elif keys[pg.K_d]:
            self.vel.x = self.speed
            self.current_direction = 3

    def collide(self, dir):
        collides = pg.sprite.spritecollide(self, self.map.collidable_tiles, False)
        if dir == "x" and collides:
            if self.vel.x > 0:
                self.x = collides[0].rect.left - self.rect.width
            if self.vel.x < 0:
                self.x = collides[0].rect.right
            self.vel.x = 0
            self.rect.x = self.x
        if dir == "y" and collides:
            if self.vel.y > 0:
                self.y = collides[0].rect.top - self.rect.height
            if self.vel.y < 0:
                self.y = collides[0].rect.bottom
            self.vel.y = 0
            self.rect.y = self.y

    def get_current_tile(self):
        return self.map.nig[int((self.y+(self.rect.height/2))/64)][int((self.x+(self.rect.width/2))/64)]

    def update(self):
        self.keys()
        self.maurisio()
        self.x += self.vel.x
        self.y += self.vel.y
        self.rect.x = self.x
        self.collide("x")
        self.rect.y = self.y
        self.collide("y")


    #Verifies if there is a map transition and if there is, the map changes accordingly
    def maurisio(self):
        currentTile = self.get_current_tile()
        if currentTile.adyacent_map_filename != "":
            #load map
            new_map = tomas.Map(currentTile.adyacent_map_filename, self.screen)
            self.map = new_map
            self.groups = self.map.all_sprites
            self.map.load()
            self.x = currentTile.x_spawn * 64
            self.y = currentTile.y_spawn * 64
            self.vel = vec(0, 0)