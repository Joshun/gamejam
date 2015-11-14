import pygame as pg
import pytmx

from pytmx.util_pygame import load_pygame

class TilesetLoader(object):

    def __init__(self, tileset_file):
        self.__tiled_map = load_pygame(tileset_file, pixelalpha=True)
        self.__tile_properties = []

        for layer_num in range(len(self.__tiled_map.layers)):
            for gid_property in self.__tiled_map.get_tile_properties_by_layer(layer_num):
                self.__tile_properties.append(gid_property)

        print(self.get_all_tiles_with_property("pstart"))



    def get_all_tiles_with_property(self, tproperty):
        for gid, properties in self.__tile_properties:
            if tproperty in properties:
                return (gid,properties)


    def draw(self, screen):

        for layer in self.__tiled_map.visible_layers:
            for x, y, image in layer.tiles():
                image_rect = pg.Rect(x*16, y*16, 16, 16)

                screen.blit(image, image_rect)
                # pg.draw.rect(screen,pg.Color(255,255,255), image_rect)
                # pg.Surface.blit(image, screen, image_rect)
                # pg.image.save(image, "out")
    #
    # def get_objects(self):
    #     return self.__objects
    #
    # def get_object_properties(self):
    #     for obj in self.__objects:
    #         print(obj.properties)




