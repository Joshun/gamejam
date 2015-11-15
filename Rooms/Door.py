class Door(object):
    def __init__(self, next_room, rect):
        self.__next_room = next_room
        self.__rect = rect

    def get_next_room(self):
        return self.__next_room

    def player_action(self, player, room_collection):
        # print("testing ", player.rect, " against ", self.__rect)
        if player.is_colliding(self.__rect):
            print(room_collection)
            print(self.__next_room)
            room_collection.change_room(self.__next_room)
