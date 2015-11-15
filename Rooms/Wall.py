class Wall:
    def __init__(self, rect):
        self.__rect = rect

    def get_rect(self):
        return self.__rect

    def is_colliding(self, rect):
        return self.__rect.colliderect(rect)