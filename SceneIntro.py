import pygame
from abc import abstractmethod

class SceneIntro():
    """docstring for Overlay"""
    def __init__(self, location, paragraph):
        self.font = pygame.font.Font(None, 24)

        self.location = location
        self.paragraph = paragraph

    def draw(self, screen):
        background = pygame.Surface((screen.get_size()[0],50))
        background = background.convert()
        background.fill((250, 250, 250, 50))
        text = self.font.render(self.paragraph, 1, (10, 10, 10))
        textpos = text.get_rect()
        textpos.centerx = background.get_rect().centerx
        background.blit(text, textpos)
        screen.blit(background, (0, 0))

    def update(self):
        pass
