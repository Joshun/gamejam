from Door import *

class Room(object):
    """Base class for a Room"""
    def __init__(self, tiled_map):
        self.__room_collection = []
        self.__tiled_map = tiled_map
        self.__room_collection = []
        self.__tiled_map_objects = self.__tiled_map.get_objects()
        self.__character_tiles = self.__tiled_map.get_all_objects_with_property("character")
        self.__doors = self.__setup_doors(self.__tiled_map.get_all_objects_with_property("next_room"))

        # self.__doors = self.__setup_doors(self.__tiled_map.get_all_tiles_with_property("next_room"))

        print(self.__doors)

    def __setup_doors(self, doors_list):
        doors = []
        for obj in doors_list:
            doors.append(Door(obj.properties["next_room"], (obj.x, obj.y), self.__room_collection))
        return doors

    def set_room_collection(self, room_collection):
        self.__room_collection = room_collection

    def draw(self, screen):
        self.__tiled_map.draw(screen)

    def update(self, screen, player):
        for obj in self.__doors:
            obj.player_action(player, self.__room_collection)