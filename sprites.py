import pygame as pg
from settings import *

class Nameless(pg.sprite.Sprite):

    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.image = pg.image.load("imgs/buff_doge.png").convert_alpha()
        self.speed = 64
        self.screen = screen
        self.rect = self.image.get_rect()

    def keys(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.move(0, -self.speed)
        elif keys[pg.K_a]:
            self.move(-self.speed, 0)
        elif keys[pg.K_s]:
            self.move(0, self.speed)
        elif keys[pg.K_d]:
            self.move(self.speed, 0)

    def move(self, x, y):
        #if 0 <=self.x+x <= WIDTH and 0 <=self.y+y <= HEIGHT:
        self.x += x
        self.y += y
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.keys()

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))