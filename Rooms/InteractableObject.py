class InteractableObject:
    def __init__(self, rect):
        self.__rect = rect

    def is_colliding(self, rect):
        return self.__rect.colliderect(rect)