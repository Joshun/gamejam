import pygame as pg
import pytmx


class TilesetLoader(object):

    def __init__(self, tileset_file):
        self.__tiled_map = pytmx.load_pygame(tileset_file, pixelalpha=True)
        self.__objects = []


        for layer in self.__tiled_map.layers:
            if isinstance(layer, pytmx.pytmx.TiledObjectGroup):
                for obj in layer:
                    self.__objects.append(obj)

        print(self.get_all_objects_with_property("pstart"))

    def get_all_objects_with_property(self, tproperty):
        objects = []
        for obj in self.__objects:
            if tproperty in obj.properties:
                objects.append(obj)
        return objects

    def draw(self, screen):

        for layer in self.__tiled_map.visible_layers:
            if isinstance(layer, pytmx.pytmx.TiledTileLayer):
                for x, y, image in layer.tiles():
                    image_width = image.get_width()
                    image_height = image.get_height()
                    image_rect = pg.Rect(x*image_width, y*image_height, image_width, image_height)

                    screen.blit(image, image_rect)
