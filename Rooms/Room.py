import sys

import pygame as pg

from Rooms.Door import *

from Loaders.CharacterLoader import *

class Room(object):
    """Base class for a Room"""
    def __init__(self, tiled_map, name, description, overlay):
        self.visited = False
        self.__name = name
        self.__description = description
        self.__room_collection = []
        self.__tiled_map = tiled_map
        self.__room_collection = []
        self.__tiled_map_objects = self.__tiled_map.get_objects()
        self.__entry_point = self.__init_entry_point()
        self.__doors = self.__setup_doors(self.__tiled_map.get_all_objects_with_property("next_room"))
        self.__characters = self.__setup_characters(self.__tiled_map.get_all_objects_with_property("character"))

        self.__overlay = overlay

        # self.__doors = self.__setup_doors(self.__tiled_map.get_all_tiles_with_property("next_room"))

    def player_enter(self):
        if not self.visited:
            self.visited = True
            self.__overlay.update_scene_intro(self.__name, [self.__description])

    def __init_entry_point(self):
        entry_point_test = self.__tiled_map.get_all_objects_with_property("entry_point")
        if len(entry_point_test) == 0:
            # apologies for the Steve Maddock style code
            print("Error! Room ", self, "has no entry point.")
            sys.exit(1)
        else:
            entry_point = entry_point_test[0]
            return entry_point

    def get_entry_point(self):
        return self.__entry_point

    def __setup_characters(self, characters_list):
        return CharacterLoader(characters_list).get_characters()

    def __setup_doors(self, doors_list):
        doors = []
        for obj in doors_list:
            doors.append(Door(obj.properties["next_room"], pg.Rect(obj.x, obj.y, obj.width, obj.height)))
        return doors

    def set_room_collection(self, room_collection):
        self.__room_collection = room_collection

    def draw(self, screen):
        self.__tiled_map.draw(screen)
        for obj in self.__characters:
            obj.draw(screen)

    def update(self, player, delta_time):
        for obj in self.__doors:
            obj.player_action(player, self.__room_collection)
        for obj in self.__characters:
            obj.update(delta_time, player)
            # print("Trying to update character", obj)
