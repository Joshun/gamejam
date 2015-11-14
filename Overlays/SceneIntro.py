import pygame
from abc import abstractmethod

class SceneIntro():
    """docstring for Overlay"""
    def __init__(self, location, lines):
        self.font = pygame.font.Font(None, 24)

        self.location = location
        self.current_line = 0
        self.lines = lines
        self.closed = False

    def draw(self, screen):
        if not self.closed:
            bg = self.setup_background((screen.get_size()[0],70))
            self.display_location(bg)
            self.display_paragraph(bg)
            screen.blit(bg, (0, 0))

    def setup_background(self, size):
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
        text = self.font.render(self.lines[self.current_line], 1, (100, 100, 100))
        textpos = text.get_rect().move((0,40))
        textpos.centerx = background.get_rect().centerx
        background.blit(text, textpos)

    def next(self):
        self.current_line += 1
        if self.current_line == len(self.lines):
            self.closed = True

