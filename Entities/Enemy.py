from Entities.Character import Character
from abc import abstractmethod, ABCMeta


class Enemy(Character, metaclass=ABCMeta):
    def __init__(self, start_pos, speed, anim_speed, health, weapon, sprite):
        super().__init__(start_pos, speed, anim_speed, health, sprite)
        self.weapon = weapon

    @abstractmethod
    def update(self, delta, player):
        pass

    @abstractmethod
    def draw(self, surface):
        pass
