import pygame as pg
import pytmx


class TilesetLoader(object):

    def __init__(self, tileset_file):
        self.__tiled_map = pytmx.load_pygame(tileset_file, pixelalpha=True)
        self.__tile_properties = []

        for layer_num in range(len(self.__tiled_map.layers)):
            for gid_property in self.__tiled_map.get_tile_properties_by_layer(layer_num):
                self.__tile_properties.append(gid_property)

        print(self.get_all_tiles_with_property("pstart"))

    def get_all_tiles_with_property(self, tproperty):
        tiles = []
        for gid, properties in self.__tile_properties:
            if tproperty in properties:
                tiles.append ((gid,properties))
        return tiles

    def draw(self, screen):

        for layer in self.__tiled_map.visible_layers:
            for x, y, image in layer.tiles():
                image_width = image.get_width()
                image_height = image.get_height()
                image_rect = pg.Rect(x*image_width, y*image_height, image_width, image_height)

                screen.blit(image, image_rect)
