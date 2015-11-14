import pygame
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
        super().__init()
        self.pos = pos
        self.speed = speed
        self.health = health

    @abstractmethod
    def draw(self, surface):
        pass
