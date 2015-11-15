import pygame
from SpriteSheet import SpriteSheet
from abc import abstractmethod, ABCMeta
from CONFIG import *


# Abstract class for players
class Character(pygame.sprite.Sprite, metaclass=ABCMeta):
    def __init__(self, pos, move_speed, anim_speed, health, sprite_file):
        """
        :param pos: (x, y)
        :param move_speed: character movement speed
        :param anim_speed: character animation speed, higher = slower!
        :param health: int
        :param sprite_file: images for the character
        :return:
        """
        super().__init__()

        self.pos = pos
        self.speed = move_speed
        self.health = health

        self.anim_index = 0
        self.sprite_sheet = SpriteSheet(sprite_file)
        self.images = []
        self.anim_speed = anim_speed
        self.time_elapsed = 0
        self.rect = None

    def get_centre(self):
        pos_x = self.rect.x + self.rect.w/2
        pos_y = self.rect.y + self.rect.h/2

        return pos_x, pos_y

    @abstractmethod
    def draw(self, surface):
        pass

    def check_pos(self):
        pass

    def collision_fix(self, rect):
        self.rect.x = rect.x + rect.width
        self.rect.y = rect.y + rect.height

    def is_colliding(self, rect):
        pos_x, pos_y = self.get_centre()
        if pos_x - 8 <= rect.x <= pos_x + 8:
            if pos_y - 8 <= rect.y <= pos_y + 8:
                return True
        return False

    def hit(self, amount):
        health = self.health - amount

        if health < 0:
            health = 0
            
        self.health = health

    def move_to(self, x, y):
        self.rect.x = x
        self.rect.y = y

    @abstractmethod
    def die(self):
        pass
