import pygame as pg
from settings import *
from engine import *


pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption(TITULO)
doge_map = Map("example.txt", screen)
doge_map.load()
knight2 = Nameless(1,1,screen, doge_map, False)
knight = Nameless(1,1,screen, doge_map, True)
party = Party([knight, knight2], screen)
pg.key.set_repeat(1, 500)
clock = pg.time.Clock()
pg.mixer.music.load("./music/Prueba_SONYsonido.ogg")
pg.mixer.music.play(-1)
while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT: sys.exit()
    dt = clock.tick(FPS) / 1000
    party.update()
    party.draw()
    pg.display.flip()

