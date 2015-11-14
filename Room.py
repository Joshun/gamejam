from Door import *

class Room(object):
    """Base class for a Room"""
    def __init__(self, tiled_map):
        self.__tiled_map = tiled_map
        self.__character_tiles = self.__tiled_map.get_all_objects_with_property("character")
        self.__doors = self.__setup_doors(self.__tiled_map.get_all_objects_with_property("next_room"))
        # self.__doors = self.__setup_doors(self.__tiled_map.get_all_tiles_with_property("next_room"))
        # self.__door_tiles = self.__tiled_map.get_all_tiles_with_property("next_room")
        # self.__setup_doors(self.__door_tiles)

        # self.interative_objects = i_objs
        print(self.__doors)

    def __setup_doors(self, doors_list):
        doors = []
        for obj in doors_list:
            doors.append(Door(obj.properties["next_room"]))
        return doors




    def draw(self, screen):
        self.__tiled_map.draw(screen)

    def update(self,screen):
        pass