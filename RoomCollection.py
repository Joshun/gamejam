import json

class RoomCollection(object):
    def __init__(self, description_file):
        self.__rooms = {}

        with open(description_file) as df:
            json_data = json.load(df)
            room_keys = json_data.keys()
            for room in room_keys:
                # room_description =
                pass