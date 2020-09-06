import pygame as pg
from settings import *
from engine import *


pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption(TITULO)
doge_map = Map("example.txt", screen)
doge_map.load()
knight = Nameless(64,64,screen, doge_map)
pg.key.set_repeat(1, 100)
while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT: sys.exit()
        doge_map.camera.update(knight)
        doge_map.draw()
        knight.update()
        screen.blit(knight.image, doge_map.camera.apply(knight))
        pg.display.flip()

