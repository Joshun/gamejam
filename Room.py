class Room(object):
    """Base class for a Room"""
    def __init__(self, tiled_map):
        self.__tiled_map = tiled_map
        self.__characters = tiled_map.get_all_tiles_with_property("character")
        # self.interative_objects = i_objs

    def draw(self, screen):
        self.__tiled_map.draw(screen)

    def update(self,screen):
        pass