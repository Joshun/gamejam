class Wall:
    def __init__(self, rect):
        self.__rect = rect

    def get_centre(self):
        pos_x = self.rect.x + self.rect.w/2
        pos_y = self.rect.y + self.rect.h/2
        return pos_x, pos_y

    def is_colliding(self, rect):
        pos_x, pos_y = self.get_centre()
        if pos_x - 8 <= rect.x <= pos_x + 8:
            if pos_y - 8 <= rect.y <= pos_y + 8:
                return True
        return False

    def get_rect(self):
        return self.__rect

    def check_collision(self, rect):
        pos_x, pos_y = self.get_centre()
        if pos_x - 8 <= rect.x <= pos_x + 8:
            if pos_y - 8 <= rect.y <= pos_y + 8:
                return True
        return False