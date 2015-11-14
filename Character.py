import pygame
from abc import abstractmethod

# Abstract class for players
class Character(pygame.sprite.Sprite):
    def __init__(self):
        super().__init()

    @abstractmethod
    def update(self, keys):
        pass

    @abstractmethod
    def draw(self, surface):
        pass
