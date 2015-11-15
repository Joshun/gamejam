import json

from Rooms.Room import *
from Rooms.TilesetLoader import *


class RoomCollection(object):
    def __init__(self, description_file, overlay, player):
        self.__rooms = {}
        self.__current_room = None
        self.__player = player

        with open(description_file) as df:
            json_data = json.load(df)
            room_keys = json_data.keys()
            for room_id in room_keys:
                print(room_id)
                room_name = json_data[room_id]["room_name"]
                room_description = json_data[room_id]["description"]
                room_fixed = json_data[room_id]["room_type"] == "fixed"
                room_tilemap = json_data[room_id]["tile_map"]

                print("Trying to load", room_id)
                room_tilemap_data = TilesetLoader(room_tilemap)
                new_room = Room(room_tilemap_data, room_name, room_description, overlay, player) if room_fixed else Room(room_tilemap_data, room_name, room_description, overlay, player, fixed=False)
                self.__rooms[room_id] = new_room

        # getting the start room
        self.__current_room = self.get_room_by_id("start")
        self.__current_room.player_enter()

    def get_rooms_dict(self):
        return self.__rooms

    def get_room_by_id(self, room_id):
        return self.__rooms[room_id]

    def change_room(self, room_id):
        self.__current_room = self.get_room_by_id(room_id)
        self.__current_room.player_enter()
        return self.__current_room

    def draw_current(self, screen):
        self.__current_room.draw(screen)

    def update_current(self, player, delta_time):
        self.__current_room.update(player, delta_time)

    def get_current(self):
        return self.__current_room

    def set_collection(self, collection):
        for key in self.__rooms:
            self.__rooms[key].set_room_collection(collection)
