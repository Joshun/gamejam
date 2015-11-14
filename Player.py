import Character


class Player(Character):
    def __init__(self, start_pos, health):
        speed = 1
        super().__init__(start_pos, speed, health)

    def update(self, keys):
        pass

    def draw(self, surface):
        pass