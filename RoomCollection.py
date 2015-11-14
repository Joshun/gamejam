import json

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


RoomCollection("RoomDescriptions.json")