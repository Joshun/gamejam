from Entities.Character import Character
from abc import abstractmethod, ABCMeta
import math
import random


class Enemy(Character, metaclass=ABCMeta):
    def __init__(self, start_pos, speed, anim_speed, health, weapon, sprite):
        super().__init__(start_pos, speed, anim_speed, health, sprite)
        self.weapon = weapon
        self.move_away = random.randint(0, 1)

    def update_pos(self, player, delta_time):
        pos_x, pos_y = self.get_centre()
        player_pos_x, player_pos_y = player.get_centre()

        x_diff = pos_x - player_pos_x
        y_diff = pos_y - player_pos_y
        dist = math.sqrt(pow(x_diff, 2) + pow(y_diff, 2))

        if dist - 2 <= self.weapon.range <= dist + 2:
            # print("should be shooting")
            self.weapon.shoot(delta_time)
            # print(delta_time)
        elif dist > self.weapon.range:
            scale = 1
            if abs(x_diff) > abs(y_diff):
                if x_diff > 0:
                    scale = -1
                self.rect.x += self.speed * scale
            elif abs(x_diff) < abs(y_diff):
                if y_diff > 0:
                    scale = -1
                self.rect.y += self.speed * scale
        elif dist < self.weapon.range:
            scale = 1
            if self.move_away == 0:
                if pos_x < player_pos_x:
                    scale = -1
                self.rect.x += self.speed * scale
            else:
                if pos_y < player_pos_y:
                    scale = -1
                self.rect.y += self.speed * scale

    @abstractmethod
    def update(self, delta, player):
        pass

    @abstractmethod
    def draw(self, surface):
        pass
