import pygame as pg
from settings import *
from engine import *





pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption(TITULO)
clock = pg.time.Clock()
pg.mixer.music.load("./music/Prueba_SONYsonido.ogg")
pg.mixer.music.play(-1)

#helpert test
img_helpert = pg.image.load("imgs/helpert-normaldialog.png").convert_alpha()
img_helpert = pg.transform.scale(img_helpert,(400,500))

while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT: sys.exit()
    dt = clock.tick(FPS) / 1000
    screen.blit(img_helpert, (700, 350))
    pg.display.flip()