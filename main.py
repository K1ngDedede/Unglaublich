import sys, pygame as pg
from settings import *
from sprites import *


class Jogo:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITULO)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)

    def new(self):
        self.all_sprites = pg.sprite.Group()

    def run(self):
        self.jugando = True
        while self.jugando:
            self.dt = self.clock.tick(FPS)/1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        self.all_sprites.update()

    def dibujar_grilla(self):
        for x in range(0, WIDTH, TAM_CUADRO):
            pg.draw.line(self.screen, LIGHT_GRAY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TAM_CUADRO):
            pg.draw.line(self.screen, LIGHT_GRAY, (0, y), (WIDTH, y))

    def draw(self):
        self.dibujar_grilla()
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT: sys.exit()


jogo = Jogo()
while True:
    jogo.new()
    jogo.run()

