import pygame as pg
import pytmx


class TilesetLoader(object):

    def __init__(self, tileset_file):
        self.__tiled_map = pytmx.load_pygame(tileset_file)

    def draw(self, screen):
        for layer in self.__tiled_map.layers:
            for obj in layer:
                image_rect = pg.Rect(obj.x, obj.y, obj.width, obj.height)
                screen.blit(obj.image, image_rect)



