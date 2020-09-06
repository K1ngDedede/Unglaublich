import pygame as pg
from settings import *
vec = pg.math.Vector2

class Nameless(pg.sprite.Sprite):

    def __init__(self, x, y, screen, map):
        self.groups = map.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.x = x
        self.y = y
        self.image = pg.image.load("imgs/nameless_pixelart3.png").convert_alpha()
        self.speed = 20
        self.screen = screen
        self.rect = self.image.get_rect()
        self.map = map
        self.vel = vec(0,0)

    def keys(self):
        self.vel = vec(0,0)
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.vel.y = -self.speed
        elif keys[pg.K_a]:
            self.vel.x = -self.speed
        elif keys[pg.K_s]:
            self.vel.y = self.speed
        elif keys[pg.K_d]:
            self.vel.x = self.speed

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


    def update(self):
        self.keys()
        self.x += self.vel.x
        self.y += self.vel.y
        self.rect.x = self.x
        self.collide("x")
        self.rect.y = self.y
        self.collide("y")

