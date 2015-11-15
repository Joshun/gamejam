import sys

import pygame as pg

from Rooms.Door import *
from Rooms.Wall import *
from Rooms.InteractableObject import *

from CONFIG import *

from Loaders.CharacterLoader import *

class Room(object):
    """Base class for a Room"""
    def __init__(self, tiled_map, name, description, overlay, player, fixed=True):
        self.visited = False
        self.__fixed = fixed
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
        self.__walls = self.__setup_walls(self.__tiled_map.get_all_objects_with_property("wall"))

        # self.overlay = overlay
        self.__player = player
        # self.__interactable_objects = self.__tiled_map.get_all_objects_with_property("interactable")
        print(self.__tiled_map.get_all_objects_with_property("entry_point"))

    def __setup_walls(self, wall_list):
        walls = []
        for obj in wall_list:
            wall_rect = pg.Rect(obj.x, obj.y, obj.width, obj.height)
            if "interactable" in obj.properties:
                description = obj.properties["description"]
                no_reset = "no_reset" in obj.properties
                if no_reset:
                    walls.append(InteractableObject(wall_rect, self.__overlay, description, reset=False))
                else:
                    walls.append(InteractableObject(wall_rect, self.__overlay, description))
            else:
                walls.append(Wall(wall_rect))
        return walls

    def player_enter(self):
        print("Player at entry point", self.__entry_point.x, self.__entry_point.y)
        self.__player.move_to(self.__entry_point.x, self.__entry_point.y)
        if not self.visited:
            self.visited = True
            self.__player.play_sfx("talk")
            self.__overlay.update_scene_intro(self.__name, [self.__description])
        for wall in self.__walls:
            if isinstance(wall, InteractableObject):
                wall.reset()

    def __init_entry_point(self):
        entry_point_test = self.__tiled_map.get_all_objects_with_property("entry_point")
        print(entry_point_test)
        if len(entry_point_test) == 0:
            # apologies for the Steve Maddock style code
            print("Error! Room ", self, "has no entry point.")
            sys.exit(1)
        else:
            entry_point = entry_point_test[0]
            return entry_point

    def get_entry_point(self):
        return self.__entry_point

    def is_fixed(self):
        return self.__fixed

    @staticmethod
    def __setup_characters(characters_list):
        return CharacterLoader(characters_list).get_characters()

    @staticmethod
    def __setup_doors(doors_list):
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
        for door in self.__doors:
            door.player_action(player, self.__room_collection)
        for character in self.__characters:
            character.update(delta_time, player)

        player.test_for_collisions(self.__walls)

        for wall in self.__walls:
            if wall.is_solid():
                for character in self.__characters:
                    if wall.is_colliding(character.rect):
                        character.process_collision()
            else:
                if isinstance(wall, InteractableObject):
                    if wall.is_colliding(player.rect):
                        wall.display_text()
