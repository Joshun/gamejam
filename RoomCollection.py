import json
from Room import *
from TilesetLoader import *


class RoomCollection(object):
    def __init__(self, description_file):
        self.__rooms = {}

        with open(description_file) as df:
            json_data = json.load(df)
            room_keys = json_data.keys()
            for room_id in room_keys:
                print(room_id)
                room_name = json_data[room_id]["room_name"]
                room_description = json_data[room_id]["description"]
                room_tilemap = json_data[room_id]["tile_map"]

                room_tilemap_data = TilesetLoader(room_tilemap)
                new_room = Room(room_tilemap_data)
                self.__rooms[room_id] = new_room

    def get_rooms_dict(self):
        return self.__rooms


RoomCollection("RoomDescriptions.json")