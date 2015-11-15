from Entities.Character import Character
from abc import abstractmethod, ABCMeta
import math
import random


class Enemy(Character, metaclass=ABCMeta):
    def __init__(self, start_pos, speed, anim_speed, health, weapon, sprite):
        super().__init__(start_pos, speed, anim_speed, health, sprite)
        self.weapon = weapon

    def update_pos(self, player):
        self.check_pos()
        pos_x, pos_y = self.get_centre()
        player_pos_x, player_pos_y = player.get_centre()

        x_diff = pos_x - player_pos_x
        y_diff = pos_y - player_pos_y

        scale = 1

        print(x_diff, y_diff)
        if abs(x_diff) < 2 and abs(y_diff) < self.weapon.range:
            pass
        elif abs(y_diff) < 2 and abs(x_diff) < self.weapon.range:
            pass
        elif abs(x_diff) < abs(y_diff):
            if x_diff < 0:
                scale = -1
            self.rect.x -= self.speed * scale
        elif abs(y_diff) < abs(x_diff):
            if y_diff < 0:
                scale = -1
            self.rect.y -= self.speed * scale

    @abstractmethod
    def update(self, delta, player):
        pass

    @abstractmethod
    def draw(self, surface):
        pass
