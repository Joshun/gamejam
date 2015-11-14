import pygame
from SpriteSheet import SpriteSheet
from abc import abstractmethod, ABCMeta


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

    @abstractmethod
    def draw(self, surface):
        pass

    def is_colliding(self, rect):
        return
