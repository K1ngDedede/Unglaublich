from os import path
import pygame as pg

class Map:

    def __init__(self, filename):
        #Matrix of tiles
        self.nig = []
        self.filename = filename

    def load(self):


class Tile:

    def __init__(self, image_filename):
        self.image_filename = image_filename

    def load_image(self):
        self.image = pg.image.load(self.image_filename)
