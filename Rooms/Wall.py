class Wall:
    def __init__(self, rect, solid=True):
        self.__rect = rect
        self.__solid = solid

    def get_rect(self):
        return self.__rect

    def is_colliding(self, rect):
        return self.__rect.colliderect(rect)

    def is_solid(self):
        return self.__solid
