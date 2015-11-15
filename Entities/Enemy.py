from Entities.Character import Character
from abc import abstractmethod, ABCMeta
import random
import numpy as np


class Enemy(Character, metaclass=ABCMeta):
    def __init__(self, start_pos, speed, anim_speed, health, direction, weapon, sprite):
        super().__init__(start_pos, speed, anim_speed, health, sprite)
        self.direction = direction
        self.weapon = weapon

    def update_pos(self, player, delta_time):
        player_pos = np.array(player.rect.center).astype(int)
        enemy_pos = np.array(self.rect.center).astype(int)

        diff_vec = player_pos - enemy_pos
        move_vector = np.zeros((2,)).astype(int)
        move_vector[np.argmax(np.abs(diff_vec))] = np.sign(diff_vec[np.argmax(np.abs(diff_vec))])

        if np.linalg.norm(diff_vec, ord=1) > self.weapon.range:
            self.rect.x += move_vector[0]
            self.rect.y += move_vector[1]

            if move_vector[0] < 0:
                self.direction = "left"
            elif move_vector[0] > 0:
                self.direction = "right"
            elif move_vector[1] < 0:
                self.direction = "up"
            elif move_vector[1] > 0:
                self.direction = "down"

    @abstractmethod
    def update(self, delta, player):
        pass

    @abstractmethod
    def draw(self, surface):
        pass

    def is_colliding(self, rect):
        return self.rect.colliderect(rect)

    def die(self):
        pass
