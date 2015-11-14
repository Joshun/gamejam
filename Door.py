class Door(object):
    def __init__(self, next_room):
        self.__next_room = next_room

    def get_next_room(self):
        return self.__next_room

    def player_action(self, player, room_collection):
        pass
