from Entities.Character import Character
from abc import abstractmethod, ABCMeta


class Enemy(Character, metaclass=ABCMeta):
    def __init__(self, start_pos, speed, anim_speed, health, sprite):
        super().__init__(start_pos, speed, anim_speed, health, sprite)

    @abstractmethod
    def update(self, delta):
        pass

    @abstractmethod
    def draw(self, surface):
        pass
