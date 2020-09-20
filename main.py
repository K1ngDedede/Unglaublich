import pygame as pg
from settings import *
from engine import *


pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption(TITULO)
doge_map = Map("example.txt", screen)
doge_map.load()
knight = Nameless(1,1,screen, doge_map)
pg.key.set_repeat(1, 500)
clock = pg.time.Clock()
while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT: sys.exit()
    dt = clock.tick(FPS) / 1000
    knight.map.camera.update(knight)
    knight.map.draw()
    knight.update()
    screen.blit(knight.image, knight.map.camera.apply(knight))
    pg.display.flip()

