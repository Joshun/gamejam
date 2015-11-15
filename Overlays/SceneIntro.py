import pygame
from abc import abstractmethod

class SceneIntro():
    """docstring for Overlay"""
    def __init__(self, location, lines):
        self.font = pygame.font.Font(None, 24)

        self.location = location
        self.lines = lines[0]
        self.closed = False
        self.offset = 0

    def draw(self, screen):
        if self.closed:
            self.offset += 3
        
        bg = self.setup_background((screen.get_size()[0],70-self.offset))
        self.display_location(bg)
        self.display_paragraph(bg)
        screen.blit(bg, (0, 0))

    def setup_background(self, size):
        if size[1] < 0:
            size = (size[0],0)
        background = pygame.Surface(size,50)
        background = background.convert()
        background.fill((250, 250, 250, 50))
        return background

    def display_location(self, background):
        text = self.font.render(self.location, 1, (0, 0, 0))
        self.font.set_bold(True)
        textpos = text.get_rect().move((0,10))
        textpos.centerx = background.get_rect().centerx
        background.blit(text, textpos)
        self.font.set_bold(False)

    def display_paragraph(self, background):
        text = self.font.render(self.lines + " [SPACE]", 1, (100, 100, 100))
        textpos = text.get_rect().move((0,40))
        textpos.centerx = background.get_rect().centerx
        background.blit(text, textpos)

    def next(self):

        self.closed = True

