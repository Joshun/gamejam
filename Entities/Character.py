import pygame
from SpriteSheet import SpriteSheet
from abc import abstractmethod


# Abstract class for players
class Character(pygame.sprite.Sprite):
    def __init__(self, pos, speed, health, sprite_file):
        """
        :param pos: (x, y)
        :param speed: float
        :param health: int
        :return:
        """
        super().__init__()
        self.pos = pos
        self.speed = speed
        self.health = health

        self.sprite_sheet = SpriteSheet(sprite_file)


    @abstractmethod
    def draw(self, surface):
        pass
